<template>
  <div class="subjects-container">
    <!-- Header Section (Uniform Card Style) -->
    <div class="section-header-card minimal-header-card">
      <div class="section-header-left">
        <div class="section-header-icon minimal-header-icon">
          <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M19,3H5C3.9,3 3,3.9 3,5V19C3,20.1 3.9,21 5,21H19C20.1,21 21,20.1 21,19V5C21,3.9 20.1,3 19,3M5,19V5H19V19H5Z" />
          </svg>
        </div>
        <div>
          <div class="section-header-title minimal-header-title">My Subjects</div>
          <div class="section-header-sub minimal-header-sub">View and manage your enrolled subjects</div>
        </div>
      </div>
      <div class="section-header-stats">
        <div class="stat-item">
          <span class="stat-number">{{ totalSubjects }}</span>
          <span class="stat-label">Total Subjects</span>
        </div>
        <button @click="showJoinModal = true" class="join-class-btn">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
            <path d="M19,13H13V19H11V13H5V11H11V5H13V11H19V13Z" />
          </svg>
          Join Class
        </button>
      </div>
    </div>

    <!-- Filter and Search -->
    <div class="controls-section">
      <div class="search-box">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
          <path d="M9.5,3A6.5,6.5 0 0,1 16,9.5C16,11.11 15.41,12.59 14.44,13.73L14.71,14H15.5L20.5,19L19,20.5L14,15.5V14.71L13.73,14.44C12.59,15.41 11.11,16 9.5,16A6.5,6.5 0 0,1 3,9.5A6.5,6.5 0 0,1 9.5,3M9.5,5C7,5 5,7 5,9.5C5,12 7,14 9.5,14C12,14 14,12 14,9.5C14,7 12,5 9.5,5Z" />
        </svg>
        <input 
          type="text" 
          v-model="searchQuery" 
          placeholder="Search subjects..."
          class="search-input"
        />
      </div>
      <div class="filter-tabs">
        <button 
          v-for="filter in filters" 
          :key="filter.key"
          @click="activeFilter = filter.key"
          :class="['filter-tab', { 'active': activeFilter === filter.key }]"
        >
          {{ filter.label }}
        </button>
      </div>
    </div>

    <!-- Subjects Grid -->
    <div class="subjects-grid">
      <div 
        v-for="subject in filteredSubjects" 
        :key="subject.id" 
        class="subject-card"
        @click="viewSubjectDetails(subject)"
      >
        <div class="subject-header">
          <div class="subject-icon" :style="{ background: subject.color }">
            <span>{{ subject.code.substring(0, 2) }}</span>
          </div>
          <div class="subject-status">
            <span :class="['status-badge', subject.status]">{{ subject.status }}</span>
          </div>
        </div>
        
        <div class="subject-content">
          <h3 class="subject-title">{{ subject.name }}</h3>
          <p class="subject-code">{{ subject.code }}</p>
          <p class="subject-instructor">{{ subject.instructor }}</p>
          <p class="subject-section">Section: {{ subject.section }}</p>
          <p class="subject-grade">Grade {{ subject.gradeLevel }}</p>
        </div>
        
        <div class="subject-stats compact">
          <div class="stat">
            <span class="stat-value">{{ subject.completedQuizzes }}</span>
            <span class="stat-text">Completed</span>
          </div>
          <div class="stat">
            <span class="stat-value">{{ subject.availableQuizzes }}</span>
            <span class="stat-text">Available</span>
          </div>
          <div class="stat">
            <span class="stat-value">{{ subject.currentGrade || '--' }}</span>
            <span class="stat-text">Grade</span>
          </div>
        </div>
        <div class="subject-actions compact">
          <!-- Dynamic Quiz Button -->
          <button 
            v-if="subject.availableQuizzes > 0"
            class="action-btn primary pulse" 
            @click.stop="takeQuiz(subject)"
            :title="`${subject.availableQuizzes} quiz${subject.availableQuizzes > 1 ? 'es' : ''} available`"
          >
            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
              <path d="M14,2H6A2,2 0 0,0 4,4V20A2,2 0 0,0 6,22H18A2,2 0 0,0 20,20V8L14,2M18,20H6V4H13V9H18V20Z" />
            </svg>
            Take Quiz ({{ subject.availableQuizzes }})
          </button>
          
          <button 
            v-else-if="subject.completedQuizzes > 0"
            class="action-btn completed"
            @click.stop="viewCompletedQuizzes(subject)"
            disabled
          >
            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
              <path d="M21,7L9,19L3.5,13.5L4.91,12.09L9,16.17L19.59,5.59L21,7Z" />
            </svg>
            All Quizzes Completed
          </button>
          
          <button 
            v-else
            class="action-btn disabled"
            disabled
          >
            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
              <path d="M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2M12,17A5,5 0 0,1 7,12A5,5 0 0,1 12,7A5,5 0 0,1 17,12A5,5 0 0,1 12,17Z" />
            </svg>
            No Quizzes Yet
          </button>

          <button class="action-btn secondary" @click.stop="viewGrades(subject)">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
              <path d="M19,3H5C3.9,3 3,3.9 3,5V19C3,20.1 3.9,21 5,21H19C20.1,21 21,20.1 21,19V5C21,3.9 20.1,3 19,3M19,19H5V5H19V19M17,12H7V10H17V12M15,16H7V14H15V16M17,8H7V6H17V8Z" />
            </svg>
            Grades
          </button>
        </div>
      </div>
    </div>

    <!-- Empty State -->
    <div v-if="filteredSubjects.length === 0" class="empty-state">
      <div class="empty-icon">
        <svg width="64" height="64" viewBox="0 0 24 24" fill="currentColor">
          <path d="M19,3H5C3.9,3 3,3.9 3,5V19C3,20.1 3.9,21 5,21H19C20.1,21 21,20.1 21,19V5C21,3.9 20.1,3 19,3M5,19V5H19V19H5Z" />
        </svg>
      </div>
      <h3>No subjects found</h3>
      <p>{{ searchQuery || activeFilter !== 'all' ? 'Try adjusting your search or filter criteria' : 'Join your first class to get started' }}</p>
      <button v-if="!searchQuery && activeFilter === 'all'" @click="showJoinModal = true" class="join-first-btn">
        Join Your First Class
      </button>
    </div>

    <!-- Join Class Modal -->
    <div v-if="showJoinModal" class="modal-overlay" @click="closeJoinModal">
      <div class="modal-content" @click.stop>
        <div class="modal-header">
          <h2>Join a Class</h2>
          <button @click="closeJoinModal" class="close-btn">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
              <path d="M19,6.41L17.59,5L12,10.59L6.41,5L5,6.41L10.59,12L5,17.59L6.41,19L12,13.41L17.59,19L19,17.59L13.41,12L19,6.41Z" />
            </svg>
          </button>
        </div>

        <form @submit.prevent="joinClass" class="join-form">
          <div class="form-group">
            <label for="sectionCode">Section Code</label>
            <div class="input-with-icon">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                <path d="M12,17A2,2 0 0,0 14,15C14,13.89 13.1,13 12,13A2,2 0 0,0 10,15A2,2 0 0,0 12,17M18,8A2,2 0 0,1 20,10V20A2,2 0 0,1 18,22H6A2,2 0 0,1 4,20V10C4,8.89 4.9,8 6,8H7V6A5,5 0 0,1 12,1A5,5 0 0,1 17,6V8H18M12,3A3,3 0 0,0 9,6V8H15V6A3,3 0 0,0 12,3Z" />
              </svg>
              <input
                id="sectionCode"
                v-model="joinForm.sectionCode"
                type="text"
                placeholder="Enter section code (e.g., MAT7-A01234B)"
                required
                :class="{ 'error': joinError }"
                @input="clearJoinError"
              />
            </div>
            <small class="form-help">Ask your teacher for the section code to join their class</small>
            <div v-if="joinError" class="error-message">{{ joinError }}</div>
          </div>

          <div v-if="previewSubject" class="subject-preview">
            <h3>Class Preview</h3>
            <div class="preview-card">
              <div class="preview-icon" :style="{ background: previewSubject.color }">
                {{ previewSubject.code.substring(0, 2) }}
              </div>
              <div class="preview-info">
                <h4>{{ previewSubject.name }}</h4>
                <p>Grade {{ previewSubject.grade_level }}</p>
                <p>Section: {{ previewSubject.section }}</p>
                <p>Instructor: {{ previewSubject.instructor }}</p>
              </div>
            </div>
          </div>

          <div class="modal-actions">
            <button type="button" @click="closeJoinModal" class="cancel-btn">Cancel</button>
            <button type="submit" :disabled="isJoining || !joinForm.sectionCode" class="join-btn">
              {{ isJoining ? 'Joining...' : 'Join Class' }}
            </button>
          </div>
        </form>
      </div>
    </div>

    <!-- Loading Overlay -->
    <div v-if="isLoading" class="loading-overlay">
      <div class="loading-content">
        <div class="loading-spinner"></div>
        <p>{{ loadingMessage }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import { supabase } from '../../supabase.js'

export default {
  name: 'StudentSubjects',
  data() {
    return {
      searchQuery: '',
      activeFilter: 'all',
      showJoinModal: false,
      isJoining: false,
      isLoading: false,
      loadingMessage: '',
      joinError: '',
      previewSubject: null,
      filters: [
        { key: 'all', label: 'All Subjects' },
        { key: 'active', label: 'Active' },
        { key: 'completed', label: 'Completed' },
        { key: 'pending', label: 'Pending' }
      ],
      subjects: [], // Real-time data from Supabase only
      joinForm: {
        sectionCode: ''
      },
      pollingInterval: null,
    };
  },
  computed: {
    totalSubjects() {
      return this.subjects.length;
    },
    filteredSubjects() {
      let filtered = this.subjects;
      
      // Filter by status
      if (this.activeFilter !== 'all') {
        filtered = filtered.filter(subject => subject.status === this.activeFilter);
      }
      
      // Filter by search query
      if (this.searchQuery) {
        filtered = filtered.filter(subject => 
          subject.name.toLowerCase().includes(this.searchQuery.toLowerCase()) ||
          subject.code.toLowerCase().includes(this.searchQuery.toLowerCase()) ||
          subject.instructor.toLowerCase().includes(this.searchQuery.toLowerCase())
        );
      }
      
      return filtered;
    }
  },
  methods: {
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
              // COMPREHENSIVE TEACHER LOOKUP - Let's find where the teacher data is!
              // Get teacher information - Look in teachers table directly
              let teacherName = 'Teacher Not Assigned'
              if (subject.teacher_id) {
                console.log('Looking up teacher with ID:', subject.teacher_id)
                
                // Look up teacher in teachers table (since there's no users table)
                const { data: teacherData, error: teacherError } = await supabase
                  .from('teachers')
                  .select('name, email')
                  .eq('id', subject.teacher_id)
                  .maybeSingle()

                console.log('Teacher lookup in teachers table:', { teacherData, teacherError })

                if (teacherData && teacherData.name) {
                  teacherName = teacherData.name.trim()
                  console.log('✅ Found teacher:', teacherName)
                } else if (teacherData && teacherData.email) {
                  // Fallback to email if no name
                  teacherName = teacherData.email.split('@')[0]
                  console.log('📧 Using email as teacher name:', teacherName)
                } else {
                  console.warn('❌ Teacher not found for ID:', subject.teacher_id)
                  teacherName = 'Teacher Not Found'
                }
              } else {
                console.log('⚠️ No teacher_id assigned to subject:', subject.name)
                teacherName = 'No Teacher Assigned'
              }

              // Get ALL quizzes for this section first
              const { data: allQuizzes, error: allQuizzesError } = await supabase
                .from('quizzes')
                .select('id, title, is_published, due_date, created_at')
                .eq('section_id', sectionId)

              console.log('All quizzes for section', sectionId, ':', allQuizzes)

              // Calculate stats (simplified for now to focus on teacher issue)
              const totalQuizzes = allQuizzes ? allQuizzes.length : 0
              const completedQuizzes = 0 // We'll fix this after teacher issue
              const availableQuizzes = 0 // We'll fix this after teacher issue
              let currentGrade = '--'
              let overallScore = null

              const finalSubject = {
                id: subjectId,
                name: subject.name,
                code: enrollment.sections.section_code,
                section: enrollment.sections.name,
                instructor: teacherName, // This should now show the actual teacher name
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
        this.subjects = []
        alert(`Failed to load subjects: ${error.message}`)
      } finally {
        this.isLoading = false
      }
    },

    generateSubjectColor(subjectName) {
      const colors = ['#3D8D7A', '#6366f1', '#f59e0b', '#ef4444', '#8b5cf6', '#10b981']
      const hash = subjectName.split('').reduce((a, b) => {
        a = ((a << 5) - a) + b.charCodeAt(0)
        return a & a
      }, 0)
      return colors[Math.abs(hash) % colors.length]
    },

    async validateSectionCode() {
      if (!this.joinForm.sectionCode) return

      try {
        console.log('Validating section code:', this.joinForm.sectionCode.toUpperCase())

        // Look up section by section code with proper joins
        const { data: section, error } = await supabase
          .from('sections')
          .select(`
            id,
            name,
            section_code,
            class_id,
            subjects!class_id(
              id,
              name,
              grade_level,
              teacher_id
            )
          `)
          .eq('section_code', this.joinForm.sectionCode.toUpperCase())
          .single()

        console.log('Section validation result:', section)
        console.log('Section validation error:', error)

        if (error || !section) {
          this.joinError = 'Invalid section code. Please check with your teacher.'
          this.previewSubject = null
          return
        }

        // Check if already enrolled
        const { data: { user } } = await supabase.auth.getUser()
        const { data: existingEnrollment } = await supabase
          .from('enrollments')
          .select('id')
          .eq('student_id', user.id)
          .eq('section_id', section.id)
          .single()

        console.log('Existing enrollment check:', existingEnrollment)

        if (existingEnrollment) {
          this.joinError = 'You are already enrolled in this class.'
          this.previewSubject = null
          return
        }

        // Show preview
        this.previewSubject = {
          id: section.subjects.id,
          name: section.subjects.name,
          code: section.section_code,
          section: section.name,
          instructor: 'Teacher', // Simplified since we removed teachers join
          grade_level: section.subjects.grade_level,
          color: this.generateSubjectColor(section.subjects.name)
        }
        this.joinError = ''

        console.log('Preview subject:', this.previewSubject)

      } catch (error) {
        console.error('Error validating section code:', error)
        this.joinError = 'Error validating section code. Please try again.'
        this.previewSubject = null
      }
    },

    async joinClass() {
      if (!this.joinForm.sectionCode) return

      this.isJoining = true
      this.joinError = ''

      try {
        const { data: { user } } = await supabase.auth.getUser()
        if (!user) throw new Error('Please login to join a class')

        console.log('Starting join process for user:', user.id)
        console.log('Section code:', this.joinForm.sectionCode.toUpperCase())

        // Validate section code again
        const { data: section, error: sectionError } = await supabase
          .from('sections')
          .select(`
            id, 
            name,
            section_code,
            class_id,
            subjects!class_id(
              id,
              name
            )
          `)
          .eq('section_code', this.joinForm.sectionCode.toUpperCase())
          .single()

        console.log('Section found for join:', section)
        console.log('Section error:', sectionError)

        if (sectionError || !section) {
          throw new Error('Invalid section code. Please check with your teacher.')
        }

        // Check for existing enrollment
        const { data: existingEnrollment } = await supabase
          .from('enrollments')
          .select('id')
          .eq('student_id', user.id)
          .eq('section_id', section.id)
          .single()

        if (existingEnrollment) {
          throw new Error('You are already enrolled in this class.')
        }

        console.log('Creating enrollment for section:', section.id)

        // Create enrollment with both section_id and class_id
        const { data: newEnrollment, error: enrollmentError } = await supabase
          .from('enrollments')
          .insert([{
            student_id: user.id,
            section_id: section.id,
            class_id: section.class_id
          }])
          .select()
          .single()

        console.log('Enrollment created:', newEnrollment)
        console.log('Enrollment error:', enrollmentError)

        if (enrollmentError) throw enrollmentError

        // Update section student count
        const { error: updateError } = await supabase.rpc('increment_student_count', {
          section_id: section.id
        })

        if (updateError) console.warn('Failed to update student count:', updateError)

        // Success
        await this.fetchSubjects()
        this.closeJoinModal()
        alert(`Successfully joined ${section.subjects.name}!`)

      } catch (error) {
        console.error('Error joining class:', error)
        this.joinError = error.message
      } finally {
        this.isJoining = false
      }
    },

    clearJoinError() {
      this.joinError = ''
      this.previewSubject = null
      // Add debounced validation
      clearTimeout(this.validationTimeout)
      this.validationTimeout = setTimeout(() => {
        if (this.joinForm.sectionCode.length >= 8) {
          this.validateSectionCode()
        }
      }, 500)
    },

    closeJoinModal() {
      this.showJoinModal = false
      this.joinForm.sectionCode = ''
      this.joinError = ''
      this.previewSubject = null
    },

    viewSubjectDetails(subject) {
      console.log('Viewing subject details:', subject)
      // Navigate to subject details page
    },

    takeQuiz(subject) {
      // Navigate to available quiz for this subject/section
      this.$router.push({
        name: 'TakeQuiz',
        params: {
          subjectId: subject.id,
          sectionId: subject.sectionId
        },
        query: {
          subjectName: subject.name,
          sectionName: subject.section,
          availableQuizzes: subject.availableQuizzes
        }
      })
    },

    viewCompletedQuizzes(subject) {
      // Navigate to completed quizzes view
      this.$router.push({
        name: 'CompletedQuizzes',
        params: {
          subjectId: subject.id,
          sectionId: subject.sectionId
        },
        query: {
          subjectName: subject.name
        }
      })
    },

    viewGrades(subject) {
      // Navigate to comprehensive grades view
      this.$router.push({
        name: 'StudentGrades',
        params: {
          subjectId: subject.id,
          sectionId: subject.sectionId
        },
        query: {
          subjectName: subject.name,
          sectionName: subject.section,
          instructor: subject.instructor,
          currentGrade: subject.currentGrade,
          overallScore: subject.overallScore
        }
      })
    },
  },
  mounted() {
    this.fetchSubjects();
    this.pollingInterval = setInterval(this.fetchSubjects, 30000); // Poll every 30 seconds
  },
  beforeUnmount() {
    if (this.pollingInterval) clearInterval(this.pollingInterval);
    if (this.validationTimeout) clearTimeout(this.validationTimeout);
  }
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

.subjects-container {
  padding: 2rem;
  max-width: 1400px;
  margin: 0 auto;
  font-family: 'Inter', sans-serif;
  background: var(--bg-primary);
  min-height: 100vh;
}

/* Modern section header card style (shared with dashboard/settings) */
.section-header-card {
  display: flex;
  align-items: center;
  background: var(--bg-card);
  border-radius: 24px;
  box-shadow: 0 4px 24px 0 var(--shadow-medium);
  border: 1.5px solid var(--border-color-hover);
  padding: 2.2rem 2.5rem;
  margin-bottom: 2.2rem;
  min-height: 110px;
  gap: 2.2rem;
  justify-content: space-between;
}

.minimal-header-card {
  border-radius: 28px;
  box-shadow: 0 8px 32px 0 var(--shadow-strong);
  background: var(--bg-card);
  border: 1.5px solid var(--border-color-hover);
  padding: 3.5rem 4.5rem;
  min-height: 170px;
  gap: 3.5rem;
}

.minimal-header-icon {
  width: 88px;
  height: 88px;
  background: #4dbb98;
  border-radius: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #fff;
  box-shadow: none;
}

.minimal-header-title {
  font-size: 2.5rem;
  font-weight: 700;
  color: var(--text-primary);
  margin-bottom: 0.12rem;
  letter-spacing: -0.01em;
}

.minimal-header-sub {
  font-size: 1.25rem;
  color: var(--text-secondary);
  font-weight: 400;
  margin-bottom: 0;
}

.section-header-left {
  display: flex;
  align-items: center;
  gap: 1.5rem;
}

.section-header-stats {
  display: flex;
  align-items: center;
  gap: 2rem;
}

.stat-item {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.stat-number {
  font-size: 2.5rem;
  font-weight: 800;
  color: #3D8D7A;
  line-height: 1;
}

.stat-label {
  font-size: 0.875rem;
  font-weight: 600;
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-top: 0.5rem;
}

.join-class-btn {
  background: linear-gradient(135deg, #3D8D7A 0%, #A3D1C6 100%);
  color: white;
  border: none;
  padding: 1rem 2rem;
  border-radius: 16px;
  font-weight: 600;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  transition: all 0.3s ease;
  font-size: 1rem;
  font-family: 'Inter', sans-serif;
}

.join-class-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 12px 32px rgba(61, 141, 122, 0.3);
}

.controls-section {
  background: var(--bg-card-translucent);
  backdrop-filter: blur(20px);
  border-radius: 20px;
  padding: 2rem;
  margin-bottom: 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 2rem;
  box-shadow: 0 8px 32px var(--shadow-light);
  border: 1px solid var(--border-color-light);
}

.search-box {
  display: flex;
  align-items: center;
  background: var(--bg-input);
  border: 1px solid var(--border-color-light);
  border-radius: 16px;
  padding: 1rem 1.5rem;
  gap: 1rem;
  min-width: 300px;
  transition: all 0.3s ease;
}

.search-box:focus-within {
  border-color: var(--border-color-focus);
  background: var(--bg-input-focus);
}

.search-box svg {
  color: #3D8D7A;
  flex-shrink: 0;
}

.search-input {
  border: none;
  background: transparent;
  outline: none;
  font-size: 1rem;
  color: var(--text-primary);
  width: 100%;
  font-family: 'Inter', sans-serif;
}

.search-input::placeholder {
  color: var(--text-placeholder);
}

.filter-tabs {
  display: flex;
  gap: 0.5rem;
}

.filter-tab {
  background: var(--bg-input);
  border: 1px solid var(--border-color-light);
  border-radius: 12px;
  padding: 0.75rem 1.5rem;
  cursor: pointer;
  transition: all 0.3s ease;
  font-weight: 600;
  color: var(--text-primary);
  font-family: 'Inter', sans-serif;
}

.filter-tab:hover {
  background: var(--bg-hover);
  transform: translateY(-1px);
}

.filter-tab.active {
  background: linear-gradient(135deg, #3D8D7A 0%, #A3D1C6 100%);
  color: white;
  border-color: transparent;
  box-shadow: 0 4px 16px rgba(61, 141, 122, 0.2);
}

.subjects-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 1.2rem;
  margin-bottom: 1.2rem;
}

.subject-card {
  background: var(--bg-card-translucent);
  backdrop-filter: blur(20px);
  border-radius: 18px;
  padding: 1.5rem;
  box-shadow: 0 4px 16px var(--shadow-light);
  border: 1px solid var(--border-color-light);
  transition: all 0.2s ease;
  cursor: pointer;
  display: flex;
  flex-direction: column;
  gap: 1.2rem;
}

.subject-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 16px 48px var(--shadow-medium);
}

.subject-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
}

.subject-icon {
  width: 60px;
  height: 60px;
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-weight: 800;
  font-size: 1.25rem;
  box-shadow: 0 8px 32px rgba(61, 141, 122, 0.2);
}

.status-badge {
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
  padding: 0.5rem 1rem;
  border-radius: 12px;
  letter-spacing: 0.5px;
}

.status-badge.active {
  background: rgba(34, 197, 94, 0.2);
  color: #16a34a;
}

.status-badge.completed {
  background: rgba(59, 130, 246, 0.2);
  color: #2563eb;
}

.status-badge.pending {
  background: rgba(255, 193, 7, 0.2);
  color: #e6b000;
}

.subject-content {
  flex: 1;
}

.subject-title {
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--text-primary);
  margin-bottom: 0.5rem;
  line-height: 1.2;
}

.subject-code {
  font-size: 0.875rem;
  font-weight: 600;
  color: var(--text-muted);
  margin-bottom: 0.3rem;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.subject-instructor {
  font-size: 1rem;
  color: var(--text-secondary);
  margin: 0 0 0.3rem 0;
}

.subject-section {
  font-size: 0.9rem;
  color: var(--text-secondary);
  margin: 0;
  font-weight: 600;
}

.subject-grade {
  font-size: 0.875rem;
  color: #3D8D7A;
  margin: 0.3rem 0 0 0;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.subject-stats {
  background: var(--bg-stats);
  border-radius: 16px;
  padding: 1.5rem;
  display: flex;
  justify-content: space-around;
  gap: 1rem;
}

.stat {
  text-align: center;
  flex: 1;
}

.stat-value {
  display: block;
  font-size: 1.5rem;
  font-weight: 800;
  color: #3D8D7A;
  line-height: 1;
}

.stat-text {
  font-size: 0.75rem;
  font-weight: 600;
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-top: 0.5rem;
}

.subject-actions {
  display: flex;
  gap: 0.75rem;
}

.action-btn {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  padding: 0.875rem 1rem;
  border-radius: 12px;
  cursor: pointer;
  transition: all 0.3s ease;
  font-weight: 600;
  font-size: 0.875rem;
  border: none;
  font-family: 'Inter', sans-serif;
}

.action-btn.primary {
  background: linear-gradient(135deg, #3D8D7A 0%, #A3D1C6 100%);
  color: white;
  box-shadow: 0 4px 16px rgba(61, 141, 122, 0.2);
}

.action-btn.primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(61, 141, 122, 0.3);
}

.action-btn.secondary {
  background: var(--bg-secondary);
  color: #3D8D7A;
  border: 1px solid var(--border-color-light);
}

.action-btn.primary.pulse {
  animation: pulse-glow 2s infinite;
}

@keyframes pulse-glow {
  0% { box-shadow: 0 4px 16px rgba(61, 141, 122, 0.2); }
  50% { box-shadow: 0 4px 20px rgba(61, 141, 122, 0.4), 0 0 20px rgba(61, 141, 122, 0.3); }
  100% { box-shadow: 0 4px 16px rgba(61, 141, 122, 0.2); }
}

.action-btn.completed {
  background: rgba(34, 197, 94, 0.1);
  color: #16a34a;
  border: 1px solid rgba(34, 197, 94, 0.2);
  cursor: default;
}

.action-btn.disabled {
  background: rgba(107, 114, 128, 0.1);
  color: #9ca3af;
  border: 1px solid rgba(107, 114, 128, 0.2);
  cursor: not-allowed;
}

.action-btn.disabled:hover {
  transform: none;
  background: rgba(107, 114, 128, 0.1);
}

.empty-state {
  text-align: center;
  padding: 4rem 2rem;
  background: var(--bg-card-translucent);
  backdrop-filter: blur(20px);
  border-radius: 24px;
  box-shadow: 0 8px 32px var(--shadow-light);
  border: 1px solid var(--border-color-light);
}

.empty-icon {
  width: 80px;
  height: 80px;
  background: rgba(61, 141, 122, 0.1);
  border-radius: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #3D8D7A;
  margin: 0 auto 2rem;
}

.empty-state h3 {
  font-size: 1.5rem;
  font-weight: 700;
  color: #3D8D7A;
  margin-bottom: 1rem;
}

.empty-state p {
  color: var(--text-secondary);
  font-size: 1rem;
  margin: 0 0 2rem 0;
}

.join-first-btn {
  background: linear-gradient(135deg, #3D8D7A 0%, #A3D1C6 100%);
  color: white;
  border: none;
  padding: 1rem 2rem;
  border-radius: 16px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  font-size: 1rem;
  font-family: 'Inter', sans-serif;
}

.join-first-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 12px 32px rgba(61, 141, 122, 0.3);
}

/* Modal Styles */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.6);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
  padding: 2rem;
}

.modal-content {
  background: white;
  border-radius: 20px;
  max-width: 500px;
  width: 100%;
  max-height: 90vh;
  overflow-y: auto;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 2rem 2rem 1rem;
  border-bottom: 1px solid rgba(61, 141, 122, 0.1);
}

.modal-header h2 {
  color: #3D8D7A;
  font-size: 1.5rem;
  font-weight: 700;
  margin: 0;
}

.close-btn {
  background: none;
  border: none;
  color: #666;
  cursor: pointer;
  transition: all 0.3s ease;
  padding: 0.5rem;
  border-radius: 8px;
}

.close-btn:hover {
  color: #3D8D7A;
  background: rgba(61, 141, 122, 0.1);
}

.join-form {
  padding: 2rem;
}

.form-group {
  margin-bottom: 2rem;
}

.form-group label {
  display: block;
  margin-bottom: 0.75rem;
  color: #3D8D7A;
  font-weight: 600;
  font-size: 1rem;
}

.input-with-icon {
  position: relative;
  display: flex;
  align-items: center;
}

.input-with-icon svg {
  position: absolute;
  left: 1rem;
  color: #3D8D7A;
  z-index: 1;
}

.input-with-icon input {
  width: 100%;
  padding: 1rem 1rem 1rem 3rem;
  border: 2px solid rgba(61, 141, 122, 0.1);
  border-radius: 12px;
  font-size: 1rem;
  transition: all 0.3s ease;
  font-family: 'Inter', sans-serif;
}

.input-with-icon input:focus {
  outline: none;
  border-color: #3D8D7A;
  box-shadow: 0 0 0 3px rgba(61, 141, 122, 0.1);
}

.input-with-icon input.error {
  border-color: #ef4444;
}

.form-help {
  display: block;
  margin-top: 0.5rem;
  font-size: 0.875rem;
  color: var(--text-muted);
}

.error-message {
  margin-top: 0.5rem;
  padding: 0.75rem;
  background: rgba(239, 68, 68, 0.1);
  border: 1px solid rgba(239, 68, 68, 0.2);
  border-radius: 8px;
  color: #dc2626;
  font-size: 0.875rem;
  font-weight: 500;
}

.subject-preview {
  margin: 2rem 0;
  padding: 1.5rem;
  background: rgba(251, 255, 228, 0.5);
  border-radius: 16px;
  border: 1px solid rgba(61, 141, 122, 0.1);
}

.subject-preview h3 {
  color: #3D8D7A;
  font-size: 1.1rem;
  font-weight: 600;
  margin-bottom: 1rem;
}

.preview-card {
  display: flex;
  align-items: center;
  gap: 1rem;
  background: white;
  padding: 1rem;
  border-radius: 12px;
  border: 1px solid rgba(61, 141, 122, 0.1);
}

.preview-icon {
  width: 48px;
  height: 48px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-weight: 700;
  font-size: 1.1rem;
  flex-shrink: 0;
}

.preview-info h4 {
  color: #3D8D7A;
  font-size: 1.1rem;
  font-weight: 700;
  margin-bottom: 0.25rem;
}

.preview-info p {
  color: var(--text-secondary);
  font-size: 0.9rem;
  margin: 0.1rem 0;
}

.modal-actions {
  display: flex;
  gap: 1rem;
  justify-content: flex-end;
  margin-top: 2rem;
}

.cancel-btn {
  background: transparent;
  color: #666;
  border: 2px solid #ddd;
  padding: 0.75rem 1.5rem;
  border-radius: 10px;
  cursor: pointer;
  font-weight: 600;
  transition: all 0.3s ease;
  font-family: 'Inter', sans-serif;
}

.cancel-btn:hover {
  border-color: #3D8D7A;
  color: #3D8D7A;
}

.join-btn {
  background: linear-gradient(135deg, #3D8D7A 0%, #A3D1C6 100%);
  color: white;
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 10px;
  cursor: pointer;
  font-weight: 600;
  transition: all 0.3s ease;
  font-family: 'Inter', sans-serif;
}

.join-btn:hover {
  transform: translateY(-1px);
  box-shadow: 0 6px 20px rgba(61, 141, 122, 0.3);
}

.join-btn:disabled {
  opacity: 0.6;
  cursor: not-allowed;
  transform: none;
}

/* Loading Styles */
.loading-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.6);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1100;
}

.loading-content {
  background: white;
  padding: 2rem;
  border-radius: 16px;
  text-align: center;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
}

.loading-spinner {
  width: 40px;
  height: 40px;
  border: 4px solid rgba(61, 141, 122, 0.1);
  border-left: 4px solid #3D8D7A;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin: 0 auto 1rem;
}

@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

/* Responsive Design */
@media (max-width: 768px) {
  .subjects-container {
    padding: 1rem;
  }

  .minimal-header-card {
    flex-direction: column;
    text-align: center;
    padding: 2rem;
    gap: 1.5rem;
  }

  .section-header-stats {
    flex-direction: column;
    gap: 1rem;
  }

  .controls-section {
    flex-direction: column;
    gap: 1.5rem;
  }

  .search-box {
    min-width: auto;
    width: 100%;
  }

  .filter-tabs {
    flex-wrap: wrap;
    justify-content: center;
  }

  .subjects-grid {
    grid-template-columns: 1fr;
    gap: 1.5rem;
  }

  .subject-actions {
    flex-direction: column;
  }
}
  .modal-overlay {
    padding: 1rem;
  }

  .modal-actions {
    flex-direction: column;
  }

  .preview-card {
    flex-direction: column;
    align: center;
  }
</style>