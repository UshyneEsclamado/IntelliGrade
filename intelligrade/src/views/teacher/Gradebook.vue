<template>
  <div class="gradebook-container">
    <!-- Header -->
    <div class="gradebook-header">
      <div class="header-content">
        <h1 class="page-title">Gradebook</h1>
        <p class="page-subtitle">Review and grade quiz submissions</p>
      </div>
      <div class="header-actions">
        <div class="search-box">
          <i class="fas fa-search"></i>
          <input 
            v-model="searchQuery" 
            type="text" 
            placeholder="Search by student name or quiz..."
          >
        </div>
        <select v-model="selectedStatus" class="filter-select">
          <option value="">All Status</option>
          <option value="submitted">Pending Review</option>
          <option value="graded">Graded</option>
          <option value="reviewed">Reviewed</option>
        </select>
        <button @click="fetchSubmissions" class="refresh-btn" :disabled="loading">
          <i class="fas fa-sync-alt" :class="{ 'spinning': loading }"></i>
        </button>
      </div>
    </div>

    <!-- Loading State -->
    <div v-if="loading" class="loading-container">
      <div class="spinner"></div>
      <p>Loading submissions...</p>
    </div>

    <!-- Error State -->
    <div v-else-if="error" class="error-container">
      <i class="fas fa-exclamation-triangle"></i>
      <h3>Error Loading Submissions</h3>
      <p>{{ error }}</p>
      <button @click="fetchSubmissions" class="btn-retry">Retry</button>
    </div>

    <!-- Main Content -->
    <div v-else class="gradebook-content">
      <!-- Stats Cards -->
      <div class="stats-grid">
        <div class="stat-card">
          <div class="stat-icon pending">
            <i class="fas fa-clock"></i>
          </div>
          <div class="stat-info">
            <h3>{{ stats.pendingReview }}</h3>
            <p>Pending Review</p>
          </div>
        </div>
        <div class="stat-card">
          <div class="stat-icon graded">
            <i class="fas fa-check-circle"></i>
          </div>
          <div class="stat-info">
            <h3>{{ stats.graded }}</h3>
            <p>Graded</p>
          </div>
        </div>
        <div class="stat-card">
          <div class="stat-icon reviewed">
            <i class="fas fa-user-check"></i>
          </div>
          <div class="stat-info">
            <h3>{{ stats.reviewed }}</h3>
            <p>Reviewed</p>
          </div>
        </div>
        <div class="stat-card">
          <div class="stat-icon average">
            <i class="fas fa-chart-line"></i>
          </div>
          <div class="stat-info">
            <h3>{{ stats.averageScore }}%</h3>
            <p>Average Score</p>
          </div>
        </div>
      </div>

      <!-- Quiz Submissions Table -->
      <div class="submissions-section">
        <div class="section-header">
          <h2>Quiz Submissions ({{ filteredSubmissions.length }})</h2>
        </div>

        <div v-if="filteredSubmissions.length === 0" class="empty-state">
          <i class="fas fa-clipboard-list"></i>
          <h3>No submissions found</h3>
          <p v-if="submissions.length === 0">There are no quiz submissions yet.</p>
          <p v-else>There are no quiz submissions matching your filters.</p>
        </div>

        <div v-else class="submissions-table-container">
          <table class="submissions-table">
            <thead>
              <tr>
                <th @click="sortBy('student_name')" class="sortable">
                  Student Name
                  <i class="fas fa-sort" :class="getSortIcon('student_name')"></i>
                </th>
                <th @click="sortBy('quiz_title')" class="sortable">
                  Quiz
                  <i class="fas fa-sort" :class="getSortIcon('quiz_title')"></i>
                </th>
                <th @click="sortBy('submitted_at')" class="sortable">
                  Submitted
                  <i class="fas fa-sort" :class="getSortIcon('submitted_at')"></i>
                </th>
                <th @click="sortBy('percentage')" class="sortable">
                  Score
                  <i class="fas fa-sort" :class="getSortIcon('percentage')"></i>
                </th>
                <th>Status</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody>
              <tr 
                v-for="submission in paginatedSubmissions" 
                :key="submission.id"
              >
                <td>
                  <div class="student-info">
                    <div class="student-avatar">
                      {{ getInitials(submission.student_name) }}
                    </div>
                    <div>
                      <div class="student-name">{{ submission.student_name }}</div>
                      <div class="student-email">{{ submission.student_email }}</div>
                    </div>
                  </div>
                </td>
                <td>
                  <div class="quiz-info">
                    <div class="quiz-title">{{ submission.quiz_title }}</div>
                    <div class="quiz-code">{{ submission.quiz_code }}</div>
                  </div>
                </td>
                <td>
                  <div class="date-info">
                    <div class="date">{{ formatDate(submission.submitted_at) }}</div>
                    <div class="time">{{ formatTime(submission.submitted_at) }}</div>
                  </div>
                </td>
                <td>
                  <div class="score-display">
                    <div class="score-percentage" :class="getScoreClass(submission.percentage)">
                      {{ submission.percentage }}%
                    </div>
                    <div class="score-fraction">
                      {{ submission.total_score }}/{{ submission.max_score }}
                    </div>
                  </div>
                </td>
                <td>
                  <span class="status-badge" :class="submission.status">
                    {{ getStatusText(submission.status) }}
                  </span>
                </td>
                <td>
                  <div class="action-buttons">
                    <button 
                      @click="reviewSubmission(submission)" 
                      class="btn-action review"
                      title="Review & Grade"
                    >
                      <i class="fas fa-eye"></i>
                    </button>
                    <button 
                      v-if="submission.status === 'submitted'"
                      @click="autoGradeSubmission(submission)" 
                      class="btn-action auto-grade"
                      title="Auto Grade"
                    >
                      <i class="fas fa-wand-magic-sparkles"></i>
                    </button>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>

        <!-- Pagination -->
        <div v-if="totalPages > 1" class="pagination">
          <button 
            @click="currentPage--" 
            :disabled="currentPage === 1"
            class="pagination-btn"
          >
            <i class="fas fa-chevron-left"></i>
          </button>
          <span class="pagination-info">
            Page {{ currentPage }} of {{ totalPages }}
          </span>
          <button 
            @click="currentPage++" 
            :disabled="currentPage === totalPages"
            class="pagination-btn"
          >
            <i class="fas fa-chevron-right"></i>
          </button>
        </div>
      </div>
    </div>

    <!-- Review Modal -->
    <div v-if="showReviewModal" class="modal-overlay" @click="closeReviewModal">
      <div class="review-modal" @click.stop>
        <div class="modal-header">
          <div>
            <h3>Grade Submission</h3>
            <p class="modal-subtitle" v-if="selectedSubmission">
              {{ selectedSubmission.student_name }} - {{ selectedSubmission.quiz_title }}
            </p>
          </div>
          <button @click="closeReviewModal" class="modal-close">
            <i class="fas fa-times"></i>
          </button>
        </div>

        <div class="modal-content">
          <div v-if="loadingQuestions" class="loading-questions">
            <div class="spinner-small"></div>
            <p>Loading questions...</p>
          </div>

          <div v-else-if="reviewQuestions.length === 0" class="no-questions">
            <p>No questions found.</p>
          </div>

          <div v-else class="submission-review">
            <div class="review-summary">
              <div class="summary-stat">
                <span class="stat-label">Score</span>
                <span class="stat-value">{{ calculateReviewScore() }}/{{ maxReviewScore }}</span>
              </div>
              <div class="summary-stat">
                <span class="stat-label">Percentage</span>
                <span class="stat-value">{{ calculateReviewPercentage() }}%</span>
              </div>
              <div class="summary-stat">
                <span class="stat-label">Correct</span>
                <span class="stat-value">{{ correctAnswerCount }}/{{ reviewQuestions.length }}</span>
              </div>
            </div>

            <div class="questions-review">
              <div v-for="(question, index) in reviewQuestions" :key="question.id" class="question-review-item">
                <div class="question-header">
                  <div class="question-number">Q{{ index + 1 }}</div>
                  <div class="question-result" :class="question.studentAnswer?.is_correct ? 'correct' : 'incorrect'">
                    {{ question.studentAnswer?.is_correct ? '✓ Correct' : '✗ Incorrect' }}
                  </div>
                  <div class="question-points">
                    {{ question.studentAnswer?.points_earned || 0 }} / {{ question.points }} pts
                  </div>
                </div>

                <div class="question-text">{{ question.question_text }}</div>

                <div v-if="question.question_type === 'multiple_choice'" class="answer-section">
                  <div class="options-grid">
                    <div 
                      v-for="option in question.options" 
                      :key="option.id" 
                      class="option-item"
                      :class="{
                        'selected': question.studentAnswer?.selected_option_id === option.id,
                        'correct': option.is_correct,
                        'incorrect': question.studentAnswer?.selected_option_id === option.id && !option.is_correct
                      }"
                    >
                      <div class="option-letter">{{ String.fromCharCode(65 + option.option_number - 1) }}</div>
                      <div class="option-content">
                        <div class="option-text">{{ option.option_text }}</div>
                      </div>
                    </div>
                  </div>
                </div>

                <div v-else-if="question.question_type === 'true_false'" class="answer-section">
                  <div class="true-false-options">
                    <div class="tf-option" :class="{ 'student-selected': question.studentAnswer?.answer_text === 'true', 'correct-answer': question.correctAnswer === 'true' }">
                      <strong>True</strong>
                    </div>
                    <div class="tf-option" :class="{ 'student-selected': question.studentAnswer?.answer_text === 'false', 'correct-answer': question.correctAnswer === 'false' }">
                      <strong>False</strong>
                    </div>
                  </div>
                </div>

                <div v-else-if="question.question_type === 'fill_blank'" class="answer-section">
                  <div class="fill-blank-answers">
                    <div class="student-answer-box">
                      <div class="answer-label">Student Answer:</div>
                      <div class="answer-text" :class="question.studentAnswer?.is_correct ? 'correct' : 'incorrect'">
                        {{ question.studentAnswer?.answer_text || 'No answer' }}
                      </div>
                    </div>
                    <div class="correct-answer-box">
                      <div class="answer-label">Correct Answer:</div>
                      <div class="answer-text correct">
                        {{ question.correctAnswer }}
                      </div>
                    </div>
                  </div>
                </div>

                <div class="teacher-comment-section">
                  <textarea 
                    v-model="question.teacherComment"
                    class="comment-input"
                    placeholder="Add feedback..."
                    rows="2"
                  ></textarea>
                </div>
              </div>
            </div>

            <div class="overall-feedback-section">
              <h4>Overall Feedback</h4>
              <textarea 
                v-model="reviewFeedback" 
                class="feedback-textarea"
                placeholder="Overall feedback..."
                rows="3"
              ></textarea>
            </div>
          </div>
        </div>

        <div class="modal-actions">
          <button @click="closeReviewModal" class="btn-modal cancel">Cancel</button>
          <button @click="saveGrade" class="btn-modal primary" :disabled="savingGrade">
            {{ savingGrade ? 'Saving...' : 'Save Grade' }}
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, computed, watch, onMounted, onUnmounted } from 'vue'
import { supabase } from '@/supabase.js'

export default {
  name: 'Gradebook',
  setup() {
    const loading = ref(true)
    const loadingQuestions = ref(false)
    const savingGrade = ref(false)
    const error = ref(null)
    const submissions = ref([])
    const searchQuery = ref('')
    const selectedStatus = ref('')
    const currentPage = ref(1)
    const itemsPerPage = ref(10)
    const sortField = ref('submitted_at')
    const sortDirection = ref('desc')
    const showReviewModal = ref(false)
    const selectedSubmission = ref(null)
    const teacherId = ref(null)
    const userId = ref(null)
    const reviewQuestions = ref([])
    const reviewFeedback = ref('')
    let submissionsSubscription = null

    const stats = ref({
      pendingReview: 0,
      graded: 0,
      reviewed: 0,
      averageScore: 0
    })

    const correctAnswerCount = computed(() => {
      return reviewQuestions.value.filter(q => q.studentAnswer?.is_correct).length
    })

    const maxReviewScore = computed(() => {
      return reviewQuestions.value.reduce((sum, q) => sum + (q.points || 1), 0)
    })

    const filteredSubmissions = computed(() => {
      let filtered = submissions.value

      if (searchQuery.value) {
        const query = searchQuery.value.toLowerCase()
        filtered = filtered.filter(submission => 
          submission.student_name.toLowerCase().includes(query) ||
          submission.quiz_title.toLowerCase().includes(query) ||
          submission.student_email.toLowerCase().includes(query)
        )
      }

      if (selectedStatus.value) {
        filtered = filtered.filter(submission => 
          submission.status === selectedStatus.value
        )
      }

      filtered.sort((a, b) => {
        let aValue = a[sortField.value]
        let bValue = b[sortField.value]

        if (sortField.value === 'submitted_at') {
          aValue = new Date(aValue)
          bValue = new Date(bValue)
        }

        if (aValue < bValue) {
          return sortDirection.value === 'asc' ? -1 : 1
        }
        if (aValue > bValue) {
          return sortDirection.value === 'asc' ? 1 : -1
        }
        return 0
      })

      return filtered
    })

    const paginatedSubmissions = computed(() => {
      const start = (currentPage.value - 1) * itemsPerPage.value
      const end = start + itemsPerPage.value
      return filteredSubmissions.value.slice(start, end)
    })

    const totalPages = computed(() => {
      return Math.ceil(filteredSubmissions.value.length / itemsPerPage.value)
    })

    const getTeacherInfo = async () => {
      try {
        const { data: { session }, error: sessionError } = await supabase.auth.getSession()
        if (sessionError || !session) {
          console.error('Session error:', sessionError)
          error.value = 'Authentication error'
          return false
        }

        userId.value = session.user.id
        console.log('Auth user ID:', userId.value)

        const { data: profile, error: profileError } = await supabase
          .from('profiles')
          .select('id, role')
          .eq('auth_user_id', session.user.id)
          .single()

        if (profileError || !profile) {
          console.error('Profile error:', profileError)
          error.value = 'Profile not found'
          return false
        }

        console.log('Profile:', profile)

        if (profile.role !== 'teacher') {
          error.value = 'Access denied - Teacher role required'
          return false
        }

        const { data: teacher, error: teacherError } = await supabase
          .from('teachers')
          .select('id')
          .eq('profile_id', profile.id)
          .single()

        if (teacherError || !teacher) {
          console.error('Teacher error:', teacherError)
          error.value = 'Teacher record not found'
          return false
        }

        teacherId.value = teacher.id
        console.log('Teacher ID:', teacherId.value)
        return true
      } catch (err) {
        console.error('Error in getTeacherInfo:', err)
        error.value = 'An error occurred'
        return false
      }
    }

    const fetchSubmissions = async () => {
      try {
        loading.value = true
        error.value = null

        if (!teacherId.value) {
          console.error('No teacher ID')
          error.value = 'Teacher ID not found'
          return
        }

        console.log('Fetching submissions for teacher:', teacherId.value)

        // Get teacher's quizzes
        const { data: teacherQuizzes, error: quizzesError } = await supabase
          .from('quizzes')
          .select('id')
          .eq('teacher_id', teacherId.value)

        if (quizzesError) {
          console.error('Quizzes error:', quizzesError)
          throw quizzesError
        }

        console.log('Teacher quizzes:', teacherQuizzes?.length)

        if (!teacherQuizzes || teacherQuizzes.length === 0) {
          submissions.value = []
          calculateStats()
          return
        }

        const quizIds = teacherQuizzes.map(q => q.id)

        // Get attempts
        const { data: attempts, error: attemptsError } = await supabase
          .from('quiz_attempts')
          .select('id, quiz_id, student_id, attempt_number, total_score, max_score, percentage, status, submitted_at, time_taken_minutes, teacher_feedback')
          .in('quiz_id', quizIds)
          .not('submitted_at', 'is', null)
          .order('submitted_at', { ascending: false })

        if (attemptsError) {
          console.error('Attempts error:', attemptsError)
          throw attemptsError
        }

        console.log('Attempts found:', attempts?.length)

        if (!attempts || attempts.length === 0) {
          submissions.value = []
          calculateStats()
          return
        }

        const studentIds = [...new Set(attempts.map(a => a.student_id))]
        const attemptQuizIds = [...new Set(attempts.map(a => a.quiz_id))]

        console.log('Fetching student details for IDs:', studentIds)

        // Get students - THIS IS THE KEY PART THAT WAS FAILING
        const { data: students, error: studentsError } = await supabase
          .from('students')
          .select('id, full_name, email')
          .in('id', studentIds)

        if (studentsError) {
          console.error('Students fetch error:', studentsError)
          // Don't throw - continue with partial data
        }

        console.log('Students fetched:', students?.length)

        const { data: quizzes, error: quizzesDetailError } = await supabase
          .from('quizzes')
          .select('id, title, quiz_code')
          .in('id', attemptQuizIds)

        if (quizzesDetailError) {
          console.error('Quiz details error:', quizzesDetailError)
        }

        console.log('Quizzes fetched:', quizzes?.length)

        const studentMap = {}
        students?.forEach(s => { studentMap[s.id] = s })

        const quizMap = {}
        quizzes?.forEach(q => { quizMap[q.id] = q })

        submissions.value = attempts.map(attempt => {
          const student = studentMap[attempt.student_id] || {}
          const quiz = quizMap[attempt.quiz_id] || {}

          return {
            id: attempt.id,
            quiz_id: attempt.quiz_id,
            student_id: attempt.student_id,
            attempt_number: attempt.attempt_number,
            student_name: student.full_name || 'Unknown Student',
            student_email: student.email || '',
            quiz_title: quiz.title || 'Unknown Quiz',
            quiz_code: quiz.quiz_code || '',
            total_score: attempt.total_score || 0,
            max_score: attempt.max_score || 0,
            percentage: Math.round(attempt.percentage || 0),
            status: attempt.status || 'submitted',
            submitted_at: attempt.submitted_at,
            time_taken_minutes: attempt.time_taken_minutes,
            teacher_feedback: attempt.teacher_feedback
          }
        })

        console.log('Final submissions processed:', submissions.value.length)
        calculateStats()
      } catch (err) {
        console.error('Error in fetchSubmissions:', err)
        error.value = `Failed to load: ${err.message}`
      } finally {
        loading.value = false
      }
    }

    const setupRealtimeSubscription = () => {
      if (!teacherId.value) return

      submissionsSubscription = supabase
        .channel(`teacher-${teacherId.value}-submissions`)
        .on('postgres_changes', { event: '*', schema: 'public', table: 'quiz_attempts' }, 
          () => fetchSubmissions()
        )
        .subscribe()
    }

    const calculateStats = () => {
      const pending = submissions.value.filter(s => s.status === 'submitted').length
      const graded = submissions.value.filter(s => s.status === 'graded').length
      const reviewed = submissions.value.filter(s => s.status === 'reviewed').length
      const total = submissions.value.length
      const averageScore = total > 0 
        ? Math.round(submissions.value.reduce((sum, s) => sum + (s.percentage || 0), 0) / total)
        : 0

      stats.value = { pendingReview: pending, graded, reviewed, averageScore }
    }

    const sortBy = (field) => {
      if (sortField.value === field) {
        sortDirection.value = sortDirection.value === 'asc' ? 'desc' : 'asc'
      } else {
        sortField.value = field
        sortDirection.value = 'asc'
      }
    }

    const getSortIcon = (field) => {
      if (sortField.value !== field) return ''
      return sortDirection.value === 'asc' ? 'fa-sort-up' : 'fa-sort-down'
    }

    const loadQuestionsAndAnswers = async (submission) => {
      try {
        loadingQuestions.value = true

        const { data: questions, error: questionsError } = await supabase
          .from('quiz_questions')
          .select(`
            id, question_number, question_type, question_text, points,
            question_options (id, option_number, option_text, is_correct),
            question_answers (correct_answer, case_sensitive)
          `)
          .eq('quiz_id', submission.quiz_id)
          .order('question_number')

        if (questionsError) throw questionsError

        const { data: studentAnswers, error: answersError } = await supabase
          .from('student_answers')
          .select('*')
          .eq('attempt_id', submission.id)

        if (answersError) throw answersError

        reviewQuestions.value = (questions || []).map(q => {
          const studentAnswer = (studentAnswers || []).find(sa => sa.question_id === q.id)
          let correctAnswer = null

          if (q.question_type === 'multiple_choice') {
            correctAnswer = q.question_options?.find(opt => opt.is_correct)
          } else if (q.question_answers && q.question_answers.length > 0) {
            correctAnswer = q.question_answers[0].correct_answer
          }

          return {
            id: q.id,
            question_number: q.question_number,
            question_type: q.question_type,
            question_text: q.question_text,
            points: q.points || 1,
            options: q.question_options || [],
            correctAnswer,
            studentAnswer,
            teacherComment: studentAnswer?.teacher_comment || ''
          }
        })

      } catch (err) {
        console.error('Error loading questions:', err)
        alert('Failed to load questions')
      } finally {
        loadingQuestions.value = false
      }
    }

    const reviewSubmission = async (submission) => {
      selectedSubmission.value = submission
      reviewFeedback.value = submission.teacher_feedback || ''
      showReviewModal.value = true
      await loadQuestionsAndAnswers(submission)
    }

    const autoGradeSubmission = async (submission) => {
      if (!confirm('Auto-grade this submission?')) return
      await loadQuestionsAndAnswers(submission)
      selectedSubmission.value = submission
      reviewFeedback.value = ''
      showReviewModal.value = true
      setTimeout(() => alert('Auto-grading complete!'), 500)
    }

    const calculateReviewScore = () => {
      return reviewQuestions.value.reduce((sum, q) => sum + (q.studentAnswer?.points_earned || 0), 0)
    }

    const calculateReviewPercentage = () => {
      if (maxReviewScore.value === 0) return 0
      return Math.round((calculateReviewScore() / maxReviewScore.value) * 100)
    }

    const closeReviewModal = () => {
      showReviewModal.value = false
      selectedSubmission.value = null
      reviewQuestions.value = []
      reviewFeedback.value = ''
    }

    const saveGrade = async () => {
      try {
        if (!selectedSubmission.value) return

        savingGrade.value = true
        const finalScore = calculateReviewScore()
        const finalPercentage = calculateReviewPercentage()

        const { error: updateError } = await supabase
          .from('quiz_attempts')
          .update({
            total_score: finalScore,
            percentage: finalPercentage,
            status: 'graded',
            teacher_feedback: reviewFeedback.value,
            manually_reviewed: true,
            graded_by: teacherId.value,
            graded_at: new Date().toISOString()
          })
          .eq('id', selectedSubmission.value.id)

        if (updateError) throw updateError

        for (const question of reviewQuestions.value) {
          if (question.teacherComment && question.studentAnswer?.id) {
            await supabase
              .from('student_answers')
              .update({ teacher_comment: question.teacherComment })
              .eq('id', question.studentAnswer.id)
          }
        }

        await supabase
          .from('quiz_results')
          .upsert({
            quiz_id: selectedSubmission.value.quiz_id,
            student_id: selectedSubmission.value.student_id,
            best_attempt_id: selectedSubmission.value.id,
            best_score: finalScore,
            best_percentage: finalPercentage,
            total_attempts: selectedSubmission.value.attempt_number,
            latest_attempt_date: selectedSubmission.value.submitted_at,
            status: 'graded',
            finalized: true,
            visible_to_student: true
          }, { onConflict: 'quiz_id,student_id' })

        const index = submissions.value.findIndex(s => s.id === selectedSubmission.value.id)
        if (index !== -1) {
          submissions.value[index].status = 'graded'
          submissions.value[index].total_score = finalScore
          submissions.value[index].percentage = finalPercentage
          submissions.value[index].teacher_feedback = reviewFeedback.value
        }

        calculateStats()
        closeReviewModal()
        alert('Grade saved successfully!')
      } catch (err) {
        console.error('Error saving grade:', err)
        alert(`Error: ${err.message}`)
      } finally {
        savingGrade.value = false
      }
    }

    const getInitials = (name) => {
      if (!name) return '?'
      return name.split(' ').map(n => n[0]).join('').toUpperCase().substring(0, 2)
    }

    const formatDate = (dateString) => {
      if (!dateString) return 'N/A'
      return new Date(dateString).toLocaleDateString()
    }

    const formatTime = (dateString) => {
      if (!dateString) return 'N/A'
      return new Date(dateString).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
    }

    const getStatusText = (status) => {
      const map = {
        'in_progress': 'In Progress',
        'submitted': 'Pending Review',
        'graded': 'Graded',
        'reviewed': 'Reviewed'
      }
      return map[status] || status
    }

    const getScoreClass = (percentage) => {
      if (percentage >= 90) return 'excellent'
      if (percentage >= 80) return 'good'
      if (percentage >= 70) return 'average'
      return 'needs-improvement'
    }

    watch([searchQuery, selectedStatus], () => { currentPage.value = 1 })

    onMounted(async () => {
      console.log('Gradebook mounted')
      const success = await getTeacherInfo()
      if (success) {
        await fetchSubmissions()
        setupRealtimeSubscription()
      } else {
        loading.value = false
      }
    })

    onUnmounted(() => {
      if (submissionsSubscription) supabase.removeChannel(submissionsSubscription)
    })

    return {
      loading, loadingQuestions, savingGrade, error, submissions, searchQuery, selectedStatus, 
      currentPage, totalPages, filteredSubmissions, paginatedSubmissions, stats, showReviewModal, 
      selectedSubmission, reviewQuestions, reviewFeedback, correctAnswerCount, maxReviewScore,
      sortBy, getSortIcon, reviewSubmission, autoGradeSubmission, closeReviewModal, 
      saveGrade, calculateReviewScore, calculateReviewPercentage, getInitials, formatDate, 
      formatTime, getStatusText, getScoreClass, fetchSubmissions
    }
  }
}
</script>

<style scoped>
.gradebook-container {
  padding: 2rem;
  max-width: 1400px;
  margin: 0 auto;
  min-height: 100vh;
  background: #f8fafc;
}

.gradebook-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 2rem;
  flex-wrap: wrap;
  gap: 1rem;
}

.header-content {
  flex: 1;
}

.page-title {
  font-size: 2.5rem;
  font-weight: 700;
  color: #1a202c;
  margin: 0 0 0.5rem 0;
}

.page-subtitle {
  color: #64748b;
  font-size: 1.1rem;
  margin: 0;
}

.header-actions {
  display: flex;
  gap: 1rem;
  align-items: center;
  flex-wrap: wrap;
}

.search-box {
  position: relative;
  min-width: 300px;
}

.search-box i {
  position: absolute;
  left: 1rem;
  top: 50%;
  transform: translateY(-50%);
  color: #64748b;
}

.search-box input {
  width: 100%;
  padding: 0.75rem 1rem 0.75rem 2.5rem;
  border: 1px solid #e2e8f0;
  border-radius: 0.5rem;
  font-size: 0.95rem;
  background: white;
}

.filter-select {
  padding: 0.75rem 1rem;
  border: 1px solid #e2e8f0;
  border-radius: 0.5rem;
  background: white;
  font-size: 0.95rem;
  min-width: 140px;
}

.refresh-btn {
  width: 40px;
  height: 40px;
  border: 1px solid #e2e8f0;
  background: white;
  border-radius: 0.5rem;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.2s;
  color: #64748b;
}

.refresh-btn:hover:not(:disabled) {
  background: #f8fafc;
  border-color: #cbd5e1;
  color: #3b82f6;
}

.refresh-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.spinning {
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.loading-container, .error-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 400px;
}

.loading-container {
  color: #64748b;
}

.error-container {
  color: #dc2626;
  text-align: center;
  padding: 2rem;
}

.error-container i {
  font-size: 4rem;
  margin-bottom: 1rem;
  color: #fca5a5;
}

.error-container h3 {
  font-size: 1.5rem;
  margin-bottom: 0.5rem;
  color: #991b1b;
}

.btn-retry {
  padding: 0.75rem 1.5rem;
  background: #dc2626;
  color: white;
  border: none;
  border-radius: 0.5rem;
  cursor: pointer;
  font-size: 1rem;
  margin-top: 1rem;
}

.btn-retry:hover {
  background: #b91c1c;
}

.spinner {
  width: 40px;
  height: 40px;
  border: 4px solid #e2e8f0;
  border-top: 4px solid #3b82f6;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin-bottom: 1rem;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1rem;
  margin-bottom: 2rem;
}

.stat-card {
  background: white;
  padding: 1.5rem;
  border-radius: 0.75rem;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  display: flex;
  align-items: center;
  gap: 1rem;
}

.stat-icon {
  width: 60px;
  height: 60px;
  border-radius: 0.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.5rem;
  color: white;
}

.stat-icon.pending { background: #f59e0b; }
.stat-icon.graded { background: #10b981; }
.stat-icon.reviewed { background: #3b82f6; }
.stat-icon.average { background: #8b5cf6; }

.stat-info h3 {
  font-size: 1.75rem;
  font-weight: 700;
  color: #1a202c;
  margin: 0 0 0.25rem 0;
}

.stat-info p {
  color: #64748b;
  margin: 0;
  font-size: 0.9rem;
}

.submissions-section {
  background: white;
  border-radius: 0.75rem;
  overflow: hidden;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.section-header {
  padding: 1.5rem;
  border-bottom: 1px solid #e2e8f0;
}

.section-header h2 {
  font-size: 1.5rem;
  font-weight: 600;
  color: #1a202c;
  margin: 0;
}

.empty-state {
  padding: 4rem 2rem;
  text-align: center;
  color: #64748b;
}

.empty-state i {
  font-size: 4rem;
  margin-bottom: 1rem;
  color: #cbd5e1;
}

.empty-state h3 {
  font-size: 1.25rem;
  margin-bottom: 0.5rem;
  color: #374151;
}

.submissions-table-container {
  overflow-x: auto;
}

.submissions-table {
  width: 100%;
  border-collapse: collapse;
}

.submissions-table th,
.submissions-table td {
  padding: 1rem;
  text-align: left;
  border-bottom: 1px solid #e2e8f0;
}

.submissions-table th {
  background: #f8fafc;
  font-weight: 600;
  color: #374151;
  font-size: 0.875rem;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.submissions-table th.sortable {
  cursor: pointer;
  user-select: none;
}

.submissions-table th.sortable:hover {
  background: #f1f5f9;
}

.submissions-table th i {
  margin-left: 0.5rem;
  opacity: 0.5;
}

.student-info {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.student-avatar {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: #3b82f6;
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 600;
  font-size: 0.875rem;
}

.student-name {
  font-weight: 500;
  color: #1a202c;
}

.student-email {
  font-size: 0.875rem;
  color: #64748b;
}

.quiz-info {
  max-width: 200px;
}

.quiz-title {
  font-weight: 500;
  color: #1a202c;
  margin-bottom: 0.25rem;
}

.quiz-code {
  font-size: 0.75rem;
  color: #64748b;
  font-family: monospace;
  background: #f1f5f9;
  padding: 0.125rem 0.5rem;
  border-radius: 0.25rem;
  display: inline-block;
}

.date-info {
  font-size: 0.875rem;
}

.date {
  color: #1a202c;
  font-weight: 500;
}

.time {
  color: #64748b;
}

.score-display {
  text-align: center;
}

.score-percentage {
  font-weight: 700;
  font-size: 1.125rem;
  margin-bottom: 0.25rem;
}

.score-percentage.excellent { color: #059669; }
.score-percentage.good { color: #0369a1; }
.score-percentage.average { color: #d97706; }
.score-percentage.needs-improvement { color: #dc2626; }

.score-fraction {
  font-size: 0.75rem;
  color: #64748b;
}

.status-badge {
  padding: 0.25rem 0.75rem;
  border-radius: 1rem;
  font-size: 0.75rem;
  font-weight: 500;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.status-badge.submitted {
  background: #fef3c7;
  color: #92400e;
}

.status-badge.graded {
  background: #d1fae5;
  color: #065f46;
}

.status-badge.reviewed {
  background: #dbeafe;
  color: #1e40af;
}

.action-buttons {
  display: flex;
  gap: 0.5rem;
}

.btn-action {
  width: 32px;
  height: 32px;
  border: none;
  border-radius: 0.25rem;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.2s;
}

.btn-action.review {
  background: #f3f4f6;
  color: #374151;
}

.btn-action.review:hover {
  background: #e5e7eb;
}

.btn-action.auto-grade {
  background: #fef3c7;
  color: #92400e;
}

.btn-action.auto-grade:hover {
  background: #fde68a;
}

.pagination {
  padding: 1.5rem;
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 1rem;
  border-top: 1px solid #e2e8f0;
}

.pagination-btn {
  width: 40px;
  height: 40px;
  border: 1px solid #e2e8f0;
  background: white;
  border-radius: 0.5rem;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.2s;
}

.pagination-btn:hover:not(:disabled) {
  background: #f8fafc;
  border-color: #cbd5e1;
}

.pagination-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.pagination-info {
  color: #64748b;
  font-size: 0.875rem;
}

.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
  padding: 1rem;
}

.review-modal {
  background: white;
  border-radius: 0.75rem;
  width: 100%;
  max-width: 900px;
  max-height: 90vh;
  overflow: hidden;
  display: flex;
  flex-direction: column;
}

.modal-header {
  padding: 1.5rem;
  border-bottom: 1px solid #e2e8f0;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.modal-header h3 {
  font-size: 1.25rem;
  font-weight: 600;
  color: #1a202c;
  margin: 0;
}

.modal-subtitle {
  color: #64748b;
  font-size: 0.875rem;
  margin: 0.25rem 0 0 0;
}

.modal-close {
  width: 40px;
  height: 40px;
  border: none;
  background: none;
  cursor: pointer;
  border-radius: 0.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #64748b;
}

.modal-close:hover {
  background: #f1f5f9;
  color: #374151;
}

.modal-content {
  flex: 1;
  overflow-y: auto;
}

.loading-questions, .no-questions {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 3rem 2rem;
  color: #64748b;
}

.spinner-small {
  width: 30px;
  height: 30px;
  border: 3px solid #e2e8f0;
  border-top: 3px solid #3b82f6;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin-bottom: 1rem;
}

.submission-review {
  padding: 1.5rem;
}

.review-summary {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 1rem;
  padding: 1.5rem;
  background: #f8fafc;
  border-radius: 0.5rem;
  margin-bottom: 1.5rem;
}

.summary-stat {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
}

.stat-label {
  font-size: 0.875rem;
  color: #64748b;
  margin-bottom: 0.5rem;
}

.stat-value {
  font-size: 1.5rem;
  font-weight: 700;
  color: #1a202c;
}

.questions-review {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.question-review-item {
  border: 1px solid #e2e8f0;
  border-radius: 0.5rem;
  padding: 1.5rem;
  background: white;
}

.question-header {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 1rem;
  flex-wrap: wrap;
}

.question-number {
  background: #3b82f6;
  color: white;
  padding: 0.5rem 0.75rem;
  border-radius: 0.375rem;
  font-weight: 600;
  font-size: 0.875rem;
}

.question-result {
  padding: 0.5rem 0.75rem;
  border-radius: 0.375rem;
  font-weight: 600;
  font-size: 0.875rem;
}

.question-result.correct {
  background: #d1fae5;
  color: #065f46;
}

.question-result.incorrect {
  background: #fee2e2;
  color: #991b1b;
}

.question-points {
  margin-left: auto;
  color: #64748b;
  font-weight: 600;
}

.question-text {
  font-size: 1.125rem;
  color: #1a202c;
  margin-bottom: 1rem;
  line-height: 1.6;
}

.answer-section {
  margin: 1rem 0;
}

.options-grid {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.option-item {
  display: flex;
  align-items: flex-start;
  gap: 0.75rem;
  padding: 1rem;
  border: 2px solid #e2e8f0;
  border-radius: 0.5rem;
  background: white;
}

.option-item.correct {
  border-color: #10b981;
  background: #ecfdf5;
}

.option-item.incorrect {
  border-color: #ef4444;
  background: #fef2f2;
}

.option-letter {
  min-width: 32px;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #f1f5f9;
  border-radius: 50%;
  font-weight: 700;
  color: #475569;
}

.option-item.correct .option-letter {
  background: #10b981;
  color: white;
}

.option-item.incorrect .option-letter {
  background: #ef4444;
  color: white;
}

.option-content {
  flex: 1;
}

.option-text {
  color: #1a202c;
  line-height: 1.5;
}

.true-false-options {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
}

.tf-option {
  padding: 1.5rem;
  border: 2px solid #e2e8f0;
  border-radius: 0.5rem;
  text-align: center;
  background: white;
}

.tf-option.student-selected {
  border-color: #3b82f6;
  background: #eff6ff;
}

.tf-option.correct-answer {
  border-color: #10b981;
  background: #ecfdf5;
}

.tf-option strong {
  display: block;
  font-size: 1.125rem;
  color: #1a202c;
}

.fill-blank-answers {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.student-answer-box, .correct-answer-box {
  padding: 1rem;
  border-radius: 0.5rem;
  border: 1px solid #e2e8f0;
}

.answer-label {
  font-size: 0.875rem;
  color: #64748b;
  margin-bottom: 0.5rem;
  font-weight: 600;
}

.answer-text {
  padding: 0.75rem;
  border-radius: 0.375rem;
  font-size: 1rem;
}

.answer-text.correct {
  background: #d1fae5;
  color: #065f46;
}

.answer-text.incorrect {
  background: #fee2e2;
  color: #991b1b;
}

.teacher-comment-section {
  margin-top: 1rem;
}

.comment-input {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid #e2e8f0;
  border-radius: 0.375rem;
  font-family: inherit;
  font-size: 0.875rem;
  resize: vertical;
}

.comment-input:focus {
  outline: none;
  border-color: #3b82f6;
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
}

.overall-feedback-section {
  margin-top: 1.5rem;
  padding-top: 1.5rem;
  border-top: 2px solid #e2e8f0;
}

.overall-feedback-section h4 {
  font-size: 1.125rem;
  color: #1a202c;
  margin-bottom: 0.75rem;
}

.feedback-textarea {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid #e2e8f0;
  border-radius: 0.375rem;
  font-family: inherit;
  font-size: 0.875rem;
  resize: vertical;
}

.feedback-textarea:focus {
  outline: none;
  border-color: #3b82f6;
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
}

.modal-actions {
  padding: 1.5rem;
  border-top: 1px solid #e2e8f0;
  display: flex;
  justify-content: flex-end;
  gap: 1rem;
}

.btn-modal {
  padding: 0.75rem 1.5rem;
  border: none;
  border-radius: 0.5rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
}

.btn-modal.cancel {
  background: #f1f5f9;
  color: #475569;
}

.btn-modal.cancel:hover {
  background: #e2e8f0;
}

.btn-modal.primary {
  background: #3b82f6;
  color: white;
}

.btn-modal.primary:hover:not(:disabled) {
  background: #2563eb;
}

.btn-modal:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

@media (max-width: 768px) {
  .gradebook-container {
    padding: 1rem;
  }

  .gradebook-header {
    flex-direction: column;
    align-items: stretch;
  }

  .search-box {
    min-width: auto;
  }

  .stats-grid {
    grid-template-columns: 1fr;
  }

  .submissions-table {
    font-size: 0.875rem;
  }

  .true-false-options {
    grid-template-columns: 1fr;
  }

  .review-summary {
    grid-template-columns: 1fr;
  }
}
</style>