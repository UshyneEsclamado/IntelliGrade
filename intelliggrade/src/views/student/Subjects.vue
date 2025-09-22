async fetchSubjects() {
      try {
        const { data: { user } } = await supabase.auth.getUser()
        if (!user) {
          console.log('No user found')
          return
        }

        this.loadingMessage = 'Loading subjects...'
        this.isLoading = true

        console.log('Current user ID:', user.id)

        // First, get enrollments with section and subject details
        const { data: enrollments, error } = await supabase
          .from('enrollments')
          .select(`
            id,
            created_at,
            section_id,
            sections!inner(
              id,
              name,
              section_code,
              class_id,
              subjects!inner(
                id,
                name,
                grade_level,
                teacher_id
              )
            )
          `)
          .eq('student_id', user.id)

        if (error) {
          console.error('Database error:', error)
          throw error
        }

        console.log('Fetched enrollments:', enrollments)

        // For each enrollment, get teacher details and quiz data
        const subjectsWithRealTimeData = await Promise.all(
          enrollments.map(async (enrollment) => {
            const sectionId = enrollment.sections.id
            const subjectId = enrollment.sections.subjects.id
            const subject = enrollment.sections.subjects

            console.log('Processing subject:', subject.name, 'with teacher_id:', subject.teacher_id)

            try {
              // Get teacher information with comprehensive approach
              let teacherName = 'Teacher Not Assigned'
              if (subject.teacher_id) {
                console.log('Looking up teacher with ID:', subject.teacher_id)
                
                // Try multiple approaches to find teacher
                // 1. Check teachers table first
                const { data: teacherData, error: teacherError } = await supabase
                  .from('teachers')
                  .select('first_name, last_name, email')
                  .eq('id', subject.teacher_id)
                  .maybeSingle()

                console.log('Teachers table lookup:', { teacherData, teacherError })

                if (teacherData && teacherData.first_name) {
                  teacherName = `${teacherData.first_name} ${teacherData.last_name}`.trim()
                  console.log('Found teacher in teachers table:', teacherName)
                } else {
                  // 2. Try users table with teacher role
                  const { data: userData, error: userError } = await supabase
                    .from('users')
                    .select('first_name, last_name, email, role')
                    .eq('id', subject.teacher_id)
                    .maybeSingle()

                  console.log('Users table lookup:', { userData, userError })

                  if (userData && userData.first_name) {
                    teacherName = `${userData.first_name} ${userData.last_name}`.trim()
                    console.log('Found teacher in users table:', teacherName)
                  } else {
                    // 3. Try without role filter in case role is different
                    const { data: anyUser, error: anyUserError } = await supabase
                      .from('users')
                      .select('first_name, last_name, email')
                      .eq('id', subject.teacher_id)
                      .maybeSingle()

                    console.log('Users table (any role) lookup:', { anyUser, anyUserError })

                    if (anyUser && anyUser.first_name) {
                      teacherName = `${anyUser.first_name} ${anyUser.last_name}`.trim()
                      console.log('Found user (any role):', teacherName)
                    } else {
                      console.warn('Teacher not found in any table for ID:', subject.teacher_id)
                      teacherName = `Teacher ID: ${subject.teacher_id.substring(0, 8)}...`
                    }
                  }
                }
              } else {
                console.log('No teacher_id assigned to subject:', subject.name)
              }

              // Get ALL quizzes for this section first
              const { data: allQuizzes, error: allQuizzesError } = await supabase
                .from('quizzes')
                .select('id, title, is_published, due_date, created_at')
                .eq('section_id', sectionId)

              console.log('All quizzes for section', sectionId, ':', allQuizzes)

              if (allQuizzesError) {
                console.warn('Error fetching all quizzes:', allQuizzesError)
              }

              // Get student quiz attempts separately
              const { data: studentAttempts, error: attemptsError } = await supabase
                .from('student_quiz_attempts')
                .select('quiz_id, completed_at, score, created_at')
                .eq('student_id', user.id)
                .in('quiz_id', (allQuizzes || []).map(q => q.id))

              console.log('Student attempts for user', user.id, ':', studentAttempts)

              if (attemptsError) {
                console.warn('Error fetching student attempts:', attemptsError)
              }

              // Calculate stats
              const totalQuizzes = allQuizzes ? allQuizzes.length : 0
              const completedAttempts = studentAttempts ? studentAttempts.filter(attempt => 
                attempt.completed_at && attempt.score !== null
              ) : []
              
              const completedQuizzes = completedAttempts.length

              const availableQuizzes = allQuizzes ? allQuizzes.filter(quiz => {
                const isPublished = quiz.is_published
                const notExpired = new Date(quiz.due_date) > new Date()
                const notCompleted = !studentAttempts?.find(attempt => 
                  attempt.quiz_id === quiz.id && attempt.completed_at
                )
                return isPublished && notExpired && notCompleted
              }).length : 0

              // Calculate current grade
              let currentGrade = '--'
              let overallScore = null

              console.log('Grade calculation for', subject.name, ':')
              console.log('- Total quizzes:', totalQuizzes)
              console.log('- Completed attempts:', completedAttempts.length)
              console.log('- Completed attempts data:', completedAttempts)

              if (completedAttempts.length > 0) {
                const totalScore = completedAttempts.reduce((sum, attempt) => {
                  const score = parseFloat(attempt.score) || 0
                  console.log('- Adding score:', score, 'from attempt:', attempt)
                  return sum + score
                }, 0)
                
                overallScore = Math.round((totalScore / completedAttempts.length) * 100) / 100

                console.log('- Total score:', totalScore)
                console.log('- Average score:', overallScore)

                // Convert to letter grade
                if (overallScore >= 95) currentGrade = 'A+'
                else if (overallScore >= 90) currentGrade = 'A'
                else if (overallScore >= 87) currentGrade = 'A-'
                else if (overallScore >= 83) currentGrade = 'B+'
                else if (overallScore >= 80) currentGrade = 'B'
                else if (overallScore >= 77) currentGrade = 'B-'
                else if (overallScore >= 73) currentGrade = 'C+'
                else if (overallScore >= 70) currentGrade = 'C'
                else if (overallScore >= 67) currentGrade = 'C-'
                else if (overallScore >= 60) currentGrade = 'D'
                else currentGrade = 'F'

                console.log('- Final grade:', currentGrade)
              } else {
                console.log('- No completed attempts found')
                currentGrade = totalQuizzes > 0 ? 'N/A' : '--'
              }

              const finalSubject = {
                id: subjectId,
                name: subject.name,
                code: enrollment.sections.section_code,
                section: enrollment.sections.name,
                instructor: teacherName,
                gradeLevel: subject.grade_level,
                color: this.generateSubjectColor(subject.name),
                status: 'active',
                completedQuizzes,
                availableQuizzes,
                totalQuizzes,
                currentGrade,
                overallScore,
                enrollmentId: enrollment.id,
                sectionId: sectionId
              }

              console.log('Final processed subject:', finalSubject)
              return finalSubject

            } catch (err) {
              console.error(`Error processing subject ${subject.name}:`, err)
              
              // Return basic data if detailed stats fail
              return {
                id: subjectId,
                name: subject.name,
                code: enrollment.sections.section_code,
                section: enrollment.sections.name,
                instructor: 'Error Loading Teacher',
                gradeLevel: subject.grade_level,
                color: this.generateSubjectColor(subject.name),
                status: 'active',
                completedQuizzes: 0,
                availableQuizzes: 0,
                totalQuizzes: 0,
                currentGrade: '--',
                overallScore: null,
                enrollmentId: enrollment.id,
                sectionId: sectionId
              }
            }
          })
        )

        this.subjects = subjectsWithRealTimeData
        console.log('All processed subjects:', this.subjects)

      } catch (error) {
        console.error('Error fetching subjects:', error)
        this.subjects = [] // Clear subjects on error
        
        // Show user-friendly error
        alert(`Failed to load subjects: ${error.message}`)
      } finally {
        this.isLoading = false
      }
    },