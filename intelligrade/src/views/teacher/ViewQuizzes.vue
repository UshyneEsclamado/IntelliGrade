<template>
  <div class="view-quizzes-container" :class="{ 'dark-mode': isDarkMode }">
    <!-- Simple Header Section -->
    <div class="section-header-card">
      <div class="section-header-content">
        <div class="section-header-left">
          <div class="section-header-icon">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="currentColor">
              <path d="M14,2H6A2,2 0 0,0 4,4V20A2,2 0 0,0 6,22H18A2,2 0 0,0 20,20V8L14,2M18,20H6V4H13V9H18V20Z" />
            </svg>
          </div>
          <div class="header-text">
            <div class="section-header-title">Quiz Management</div>
            <div class="section-header-subtitle">{{ subjectName }} (Grade {{ gradeLevel }}) - {{ sectionName }} ({{ sectionCode }})</div>
          </div>
        </div>
        
        <div class="header-actions">
          <!-- Create Quiz button removed as requested -->
          <button @click="goBack" class="back-btn">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M20,11V13H8L13.5,18.5L12.08,19.92L4.16,12L12.08,4.08L13.5,5.5L8,11H20Z" />
            </svg>
            Back to Section
          </button>
        </div>
      </div>
    </div>

    <!-- Main Content -->
    <div class="main-wrapper">
      <!-- Loading State -->
      <div v-if="isLoading" class="loading-state">
        <div class="loading-spinner"></div>
        <p>Loading quizzes...</p>
      </div>

      <!-- Error State -->
      <div v-else-if="error" class="error-state">
        <div class="error-icon">
          <svg width="48" height="48" viewBox="0 0 24 24" fill="currentColor">
            <path d="M11,15H13V17H11V15M11,7H13V13H11V7M12,2C6.47,2 2,6.5 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2M12,20A8,8 0 0,1 4,12A8,8 0 0,1 12,4A8,8 0 0,1 20,12A8,8 0 0,1 12,20Z" />
          </svg>
        </div>
        <h3>Error Loading Quizzes</h3>
        <p>{{ error }}</p>
        <button @click="fetchQuizzes" class="retry-btn">Try Again</button>
      </div>

      <!-- Empty State -->
      <div v-else-if="quizzes.length === 0" class="empty-state">
        <div class="empty-icon">
          <svg width="80" height="80" viewBox="0 0 24 24" fill="currentColor">
            <path d="M14,2H6A2,2 0 0,0 4,4V20A2,2 0 0,0 6,22H18A2,2 0 0,0 20,20V8L14,2M18,20H6V4H13V9H18V20Z" />
          </svg>
        </div>
        <h3>No Quizzes Available</h3>
        <p>You haven't created any quizzes for this section yet.</p>
        <button @click="navigateToCreateQuiz" class="create-quiz-btn">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
            <path d="M19,13H13V19H11V13H5V11H11V5H13V11H19V13Z" />
          </svg>
          Create Your First Quiz
        </button>
      </div>

      <!-- Quizzes List -->
      <div v-else class="quizzes-grid">
        <div v-for="quiz in quizzes" :key="quiz.id" class="quiz-card">
          <div class="quiz-header">
            <div class="quiz-info">
              <h3 class="quiz-title">{{ quiz.title }}</h3>
              <div class="quiz-code-display">
                <span class="code-label">Quiz Code:</span>
                <span class="code-value">{{ quiz.quiz_code || 'N/A' }}</span>
              </div>
              <p v-if="quiz.description" class="quiz-description">{{ quiz.description }}</p>
              <div class="quiz-meta">
                <span class="quiz-questions">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M9,22A1,1 0 0,1 8,21V18H4A2,2 0 0,1 2,16V4C2,2.89 2.9,2 4,2H20A2,2 0 0,1 22,4V16A2,2 0 0,1 20,18H13.9L10.2,21.71C10,21.9 9.75,22 9.5,22V22H9M10,16V19.08L13.08,16H20V4H4V16H10Z" />
                  </svg>
                  {{ quiz.question_count || 0 }} Questions
                </span>
                <span class="quiz-points">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M12,17.27L18.18,21L16.54,13.97L22,9.24L14.81,8.62L12,2L9.19,8.62L2,9.24L7.45,13.97L5.82,21L12,17.27Z" />
                  </svg>
                  {{ quiz.total_points || 0 }} Points
                </span>
                <span v-if="quiz.has_time_limit && quiz.time_limit_minutes" class="quiz-time">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M12,20A8,8 0 0,0 20,12A8,8 0 0,0 12,4A8,8 0 0,0 4,12A8,8 0 0,0 12,20M12,2A10,10 0 0,1 22,12A10,10 0 0,1 12,22C6.47,22 2,17.5 2,12A10,10 0 0,1 12,2M12.5,7V12.25L17,14.92L16.25,16.15L11,13V7H12.5Z" />
                  </svg>
                  {{ quiz.time_limit_minutes }} Minutes
                </span>
              </div>
            </div>
            <div class="quiz-status">
              <span :class="['status-badge', quiz.status]">
                {{ formatStatus(quiz.status) }}
              </span>
            </div>
          </div>

          <div class="quiz-stats">
            <div class="stat">
              <span class="stat-icon">🔁</span>
              <span class="stat-number">{{ quiz.attempts_allowed === 999 ? '∞' : quiz.attempts_allowed }}</span>
              <span class="stat-label">Attempts</span>
            </div>
            <div class="stat">
              <span class="stat-icon">📅</span>
              <span class="stat-number">{{ formatDate(quiz.created_at) }}</span>
              <span class="stat-label">Created</span>
            </div>
            <div class="stat">
              <span class="stat-icon">🔀</span>
              <span class="stat-number">{{ quiz.shuffle_questions ? 'Yes' : 'No' }}</span>
              <span class="stat-label">Shuffle</span>
            </div>
          </div>

          <div class="quiz-actions">
            <button @click="viewQuizDetails(quiz)" class="action-btn primary">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                <path d="M12,9A3,3 0 0,0 9,12A3,3 0 0,0 12,15A3,3 0 0,0 15,12A3,3 0 0,0 12,9M12,17A5,5 0 0,1 7,12A5,5 0 0,1 12,7A5,5 0 0,1 17,12A5,5 0 0,1 12,17M12,4.5C7,4.5 2.73,7.61 1,12C2.73,16.39 7,19.5 12,19.5C17,19.5 21.27,16.39 23,12C21.27,7.61 17,4.5 12,4.5Z" />
              </svg>
              View Details
            </button>
            
            <button @click="editQuiz(quiz)" class="action-btn secondary">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                <path d="M20.71,7.04C21.1,6.65 21.1,6 20.71,5.63L18.37,3.29C18,2.9 17.35,2.9 16.96,3.29L15.12,5.12L18.87,8.87M3,17.25V21H6.75L17.81,9.93L14.06,6.18L3,17.25Z" />
              </svg>
              Edit
            </button>

            <button 
              @click="toggleQuizStatus(quiz)" 
              :class="['action-btn', quiz.status === 'published' ? 'warning' : 'success']"
            >
              <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                <path v-if="quiz.status === 'published'" d="M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2M12,4A8,8 0 0,1 20,12A8,8 0 0,1 12,20A8,8 0 0,1 4,12A8,8 0 0,1 12,4M14.5,9L12,11.5L9.5,9L8,10.5L10.5,13L8,15.5L9.5,17L12,14.5L14.5,17L16,15.5L13.5,13L16,10.5L14.5,9Z" />
                <path v-else d="M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2M12,4A8,8 0 0,1 20,12A8,8 0 0,1 12,20A8,8 0 0,1 4,12A8,8 0 0,1 12,4M11,16.5L18,9.5L16.5,8L11,13.5L7.5,10L6,11.5L11,16.5Z" />
              </svg>
              {{ quiz.status === 'published' ? 'Unpublish' : 'Publish' }}
            </button>

            <button @click="deleteQuiz(quiz)" class="action-btn danger">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                <path d="M19,4H15.5L14.5,3H9.5L8.5,4H5V6H19M6,19A2,2 0 0,0 8,21H16A2,2 0 0,0 18,19V7H6V19Z" />
              </svg>
              Delete
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Quiz Details Modal -->
    <div v-if="selectedQuiz" class="modal-overlay" @click="closeModal">
      <div class="modal-content quiz-details-modal" @click.stop>
        <div class="modal-header">
          <h2>{{ selectedQuiz.title }}</h2>
          <button @click="closeModal" class="close-btn">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
              <path d="M19,6.41L17.59,5L12,10.59L6.41,5L5,6.41L10.59,12L5,17.59L6.41,19L12,13.41L17.59,19L19,17.59L13.41,12L19,6.41Z" />
            </svg>
          </button>
        </div>

        <div class="modal-body">
          <div class="quiz-overview">
            <!-- Quiz Code Display -->
            <div class="quiz-code-section">
              <div class="code-display-box">
                <span class="code-label-large">Quiz Code</span>
                <span class="code-value-large">{{ selectedQuiz.quiz_code || 'N/A' }}</span>
              </div>
            </div>

            <p v-if="selectedQuiz.description" class="quiz-description-modal">{{ selectedQuiz.description }}</p>
            
            <div class="overview-stats">
              <div class="stat-item">
                <span class="stat-value">{{ selectedQuiz.question_count || 0 }}</span>
                <span class="stat-label">Questions</span>
              </div>
              <div class="stat-item">
                <span class="stat-value">{{ selectedQuiz.total_points || 0 }}</span>
                <span class="stat-label">Total Points</span>
              </div>
              <div class="stat-item">
                <span class="stat-value">{{ selectedQuiz.has_time_limit && selectedQuiz.time_limit_minutes ? selectedQuiz.time_limit_minutes + ' min' : 'No Limit' }}</span>
                <span class="stat-label">Time Limit</span>
              </div>
              <div class="stat-item">
                <span class="stat-value">{{ selectedQuiz.attempts_allowed === 999 ? '∞' : selectedQuiz.attempts_allowed }}</span>
                <span class="stat-label">Attempts</span>
              </div>
            </div>
          </div>

          <div class="questions-preview">
            <h4>Questions Preview</h4>
            
            <!-- Loading State -->
            <div v-if="loadingQuestions" class="loading-questions">
              <div class="loading-spinner-small"></div>
              <p>Loading questions...</p>
            </div>

            <!-- Questions List -->
            <div v-else-if="selectedQuizQuestions.length > 0" class="questions-list">
              <div v-for="(question, index) in selectedQuizQuestions" :key="question.id" class="question-preview">
                <div class="question-number">{{ question.question_number }}</div>
                <div class="question-content">
                  <p class="question-text">{{ question.question_text }}</p>
                  <div class="question-meta">
                    <span class="question-type">{{ formatQuestionType(question.question_type) }}</span>
                    <span class="question-points">{{ question.points }} pts</span>
                  </div>
                </div>
              </div>
            </div>

            <!-- No Questions State -->
            <div v-else class="no-questions">
              <p>No questions found for this quiz.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { supabase } from '../../supabase.js'
import { useDarkMode } from '../../composables/useDarkMode.js'

const { isDarkMode, initDarkMode } = useDarkMode()
const router = useRouter()
const route = useRoute()

const subjectId = ref(route.params.subjectId)
const sectionId = ref(route.params.sectionId)
const subjectName = ref(route.query.subjectName || '')
const sectionName = ref(route.query.sectionName || '')
const gradeLevel = ref(route.query.gradeLevel || '')
const sectionCode = ref(route.query.sectionCode || '')

const quizzes = ref([])
const selectedQuiz = ref(null)
const selectedQuizQuestions = ref([])
const isLoading = ref(false)
const loadingQuestions = ref(false)
const error = ref(null)
const teacherId = ref(null)

let quizSubscription = null

const loadTeacherInfo = async () => {
  try {
    const { data: { user }, error: userError } = await supabase.auth.getUser()
    if (userError) throw new Error('Authentication failed')
    if (!user) throw new Error('Please login to continue')

    const { data: profile, error: profileError } = await supabase
      .from('profiles')
      .select('id')
      .eq('auth_user_id', user.id)
      .single()
    if (profileError || !profile) throw new Error('Profile not found')

    const { data: teacher, error: teacherError } = await supabase
      .from('teachers')
      .select('id')
      .eq('profile_id', profile.id)
      .single()
    if (teacherError || !teacher) throw new Error('Teacher profile not found')

    teacherId.value = teacher.id
    return teacher.id
  } catch (err) {
    throw err
  }
}

const fetchQuizzes = async () => {
  isLoading.value = true
  error.value = null
  
  try {
    if (!teacherId.value) await loadTeacherInfo()

    const { data: quizzesData, error: quizzesError } = await supabase
      .from('quizzes')
      .select(`*, quiz_questions(id, points)`)
      .eq('subject_id', subjectId.value)
      .eq('section_id', sectionId.value)
      .eq('teacher_id', teacherId.value)
      .order('created_at', { ascending: false })

    if (quizzesError) throw quizzesError

    quizzes.value = (quizzesData || []).map(quiz => {
      const questions = quiz.quiz_questions || []
      return {
        ...quiz,
        question_count: questions.length,
        total_points: questions.reduce((sum, q) => sum + (q.points || 0), 0),
        quiz_questions: undefined
      }
    })
  } catch (err) {
    error.value = err.message
    if (err.message.includes('login') || err.message.includes('not found')) {
      alert('Session expired. Please login again.')
      router.push('/login')
    }
  } finally {
    isLoading.value = false
  }
}

const viewQuizDetails = async (quiz) => {
  selectedQuiz.value = quiz
  selectedQuizQuestions.value = []
  loadingQuestions.value = true
  
  try {
    const { data: questions, error } = await supabase
      .from('quiz_questions')
      .select('*')
      .eq('quiz_id', quiz.id)
      .order('question_number')
    
    if (error) throw error
    selectedQuizQuestions.value = questions || []
  } catch (err) {
    selectedQuizQuestions.value = []
    alert('Error loading quiz questions: ' + err.message)
  } finally {
    loadingQuestions.value = false
  }
}

const editQuiz = async (quiz) => {
  try {
    await router.push({
      name: 'EditQuiz',
      params: { quizId: quiz.id },
      query: {
        subjectId: subjectId.value,
        sectionId: sectionId.value,
        subjectName: subjectName.value,
        sectionName: sectionName.value,
        gradeLevel: gradeLevel.value,
        sectionCode: sectionCode.value
      }
    })
  } catch (error) {
    alert('Error navigating to edit page: ' + error.message)
  }
}

const toggleQuizStatus = async (quiz) => {
  const newStatus = quiz.status === 'published' ? 'draft' : 'published'
  if (!confirm(`Are you sure you want to ${newStatus === 'published' ? 'publish' : 'unpublish'} this quiz?`)) return
  
  try {
    const { error } = await supabase
      .from('quizzes')
      .update({ status: newStatus, updated_at: new Date().toISOString() })
      .eq('id', quiz.id)
    
    if (error) throw error
    quiz.status = newStatus
    alert(`Quiz ${newStatus === 'published' ? 'published' : 'unpublished'} successfully!`)
  } catch (err) {
    alert(`Error updating quiz: ${err.message}`)
  }
}

const deleteQuiz = async (quiz) => {
  if (!confirm(`Are you sure you want to delete "${quiz.title}"?\n\nThis action cannot be undone and will delete all associated questions, student attempts, and results.`)) return
  
  try {
    const { error } = await supabase.from('quizzes').delete().eq('id', quiz.id)
    if (error) throw error
    quizzes.value = quizzes.value.filter(q => q.id !== quiz.id)
    alert('Quiz deleted successfully!')
  } catch (err) {
    alert(`Error deleting quiz: ${err.message}`)
  }
}

const navigateToCreateQuiz = async () => {
  try {
    await router.push({
      name: 'CreateQuiz',
      params: { subjectId: subjectId.value, sectionId: sectionId.value },
      query: {
        subjectName: subjectName.value,
        sectionName: sectionName.value,
        gradeLevel: gradeLevel.value,
        sectionCode: sectionCode.value
      }
    })
  } catch (error) {
    console.error('Navigation error:', error)
  }
}

const goBack = async () => {
  // Go back to MySubjects.vue and set viewMode to 'section-detail' with correct params
  router.push({
    name: 'MySubjects',
    params: {
      subjectId: subjectId.value,
      sectionId: sectionId.value
    },
    query: {
      viewMode: 'section-detail',
      subjectName: subjectName.value,
      sectionName: sectionName.value,
      gradeLevel: gradeLevel.value,
      sectionCode: sectionCode.value
    }
  });
}

const closeModal = () => {
  selectedQuiz.value = null
  selectedQuizQuestions.value = []
  loadingQuestions.value = false
}

const formatStatus = (status) => status ? status.charAt(0).toUpperCase() + status.slice(1) : 'Unknown'

const formatDate = (dateString) => {
  if (!dateString) return 'N/A'
  return new Date(dateString).toLocaleDateString('en-US', { year: 'numeric', month: 'short', day: 'numeric' })
}

const formatQuestionType = (type) => {
  const types = {
    'multiple_choice': 'Multiple Choice',
    'true_false': 'True/False',
    'fill_blank': 'Fill in the Blank'
  }
  return types[type] || type
}

const setupRealtimeSubscription = () => {
  if (!teacherId.value) return

  quizSubscription = supabase
    .channel('quiz-changes')
    .on('postgres_changes', {
        event: '*',
        schema: 'public',
        table: 'quizzes',
        filter: `teacher_id=eq.${teacherId.value}`
      },
      (payload) => {
        if (payload.eventType === 'INSERT') {
          fetchQuizzes()
        } else if (payload.eventType === 'UPDATE') {
          const index = quizzes.value.findIndex(q => q.id === payload.new.id)
          if (index !== -1) {
            quizzes.value[index] = {
              ...payload.new,
              question_count: quizzes.value[index].question_count,
              total_points: quizzes.value[index].total_points
            }
          }
        } else if (payload.eventType === 'DELETE') {
          quizzes.value = quizzes.value.filter(q => q.id !== payload.old.id)
        }
      }
    )
    .subscribe()
}

onMounted(async () => {
  initDarkMode()
  
  if (!subjectId.value || !sectionId.value) {
    error.value = 'Missing required parameters'
    alert('Missing subject or section information. Redirecting back...')
    router.push('/teacher/subjects')
    return
  }

  await fetchQuizzes()
  setupRealtimeSubscription()
})

onUnmounted(() => {
  if (quizSubscription) supabase.removeChannel(quizSubscription)
})
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

.view-quizzes-container {
  padding: 2rem;
  max-width: 1400px;
  margin: 0 auto;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  background: #FBFFE4;
  min-height: 100vh;
  color: #374151;
  transition: all 0.3s ease;
}

/* Simple Header Section */
.section-header-card {
  background: white;
  border-radius: 12px;
  padding: 1.25rem 1.5rem;
  margin-bottom: 2rem;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.section-header-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 1rem;
}

.section-header-left {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.section-header-icon {
  width: 48px;
  height: 48px;
  background: #3D8D7A;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  flex-shrink: 0;
}

.header-text {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}

.section-header-title {
  font-size: 1.25rem;
  font-weight: 600;
  color: #1f2937;
  margin: 0 0 0.25rem 0;
}

.section-header-subtitle {
  font-size: 0.875rem;
  color: #6b7280;
  margin: 0;
}

.header-actions {
  display: flex;
  gap: 0.75rem;
}

.create-quiz-btn, .back-button {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.625rem 1.25rem;
  border-radius: 8px;
  font-weight: 500;
  font-size: 0.875rem;
  transition: all 0.2s;
  cursor: pointer;
  border: none;
}

.create-quiz-btn {
  background: #3D8D7A;
  color: white;
}

.create-quiz-btn:hover {
  background: #2d6a5a;
}


.back-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem 1.25rem;
  border-radius: 8px;
  font-weight: 500;
  font-size: 0.875rem;
  transition: all 0.2s;
  cursor: pointer;
  text-decoration: none;
  outline: none;
  border: 2px solid #20c997;
  background: #20c997;
  color: #181c20;
  box-shadow: 0 2px 8px rgba(61, 141, 122, 0.10);
}
.back-btn:hover {
  background: #A3D1C6;
  color: #23272b;
  border-color: #20c997;
  box-shadow: 0 4px 16px rgba(61, 141, 122, 0.18);
}
.dark-mode .back-btn {
  background: #20c997;
  color: #181c20;
  border-color: #A3D1C6;
}
.dark-mode .back-btn:hover {
  background: #A3D1C6;
  color: #23272b;
  border-color: #20c997;
}

/* Main Wrapper */
.main-wrapper {
  margin-top: 2rem;
}

/* States */
.loading-state, .error-state, .empty-state {
  text-align: center;
  padding: 3rem 2rem;
  background: white;
  border-radius: 12px;
}

.loading-spinner {
  width: 32px;
  height: 32px;
  border: 3px solid #A3D1C6;
  border-left: 3px solid #3D8D7A;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin: 0 auto 1rem;
}

.loading-spinner-small {
  width: 24px;
  height: 24px;
  border: 2px solid #A3D1C6;
  border-left: 2px solid #3D8D7A;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin: 0 auto 0.5rem;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

.error-icon, .empty-icon {
  color: #9ca3af;
  margin-bottom: 1rem;
  display: flex;
  justify-content: center;
}

.empty-state h3, .error-state h3 {
  color: #3D8D7A;
  font-size: 1.25rem;
  font-weight: 600;
  margin-bottom: 0.5rem;
}

.empty-state p, .error-state p {
  color: #6b7280;
  margin-bottom: 1.5rem;
}


/* Uniform system-wide quiz button style */
.create-quiz-btn {
  background: #20c997;
  color: #181c20;
  border: 2px solid #20c997;
  border-radius: 8px;
  padding: 0.6rem 1.5rem;
  font-weight: 400;
  font-size: 1rem;
  cursor: pointer;
  transition: background 0.2s, color 0.2s, border-color 0.2s, box-shadow 0.2s;
  margin-top: 0.7rem;
  box-shadow: 0 2px 8px rgba(61, 141, 122, 0.10);
  display: inline-flex;
  width: auto;
  min-width: 0;
  margin-left: 0;
  margin-right: 0;
  align-items: center;
  gap: 0.5rem;
}
.create-quiz-btn:hover {
  background: #A3D1C6;
  color: #23272b;
  border-color: #20c997;
  box-shadow: 0 4px 16px rgba(61, 141, 122, 0.18);
}
.dark-mode .create-quiz-btn {
  background: #20c997;
  color: #181c20;
  border-color: #A3D1C6;
}
.dark-mode .create-quiz-btn:hover {
  background: #A3D1C6;
  color: #23272b;
  border-color: #20c997;
}

/* Quizzes Grid */
.quizzes-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
  gap: 1.5rem;
}

.quiz-card {
  background: white;
  border: 1px solid #e5e7eb;
  border-radius: 12px;
  padding: 1.5rem;
  transition: all 0.2s ease;
}

.quiz-card:hover {
  border-color: #3D8D7A;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(61, 141, 122, 0.1);
}

.quiz-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 1rem;
  gap: 1rem;
}

.quiz-info {
  flex: 1;
}

.quiz-title {
  color: #3D8D7A;
  font-size: 1.125rem;
  font-weight: 600;
  margin: 0 0 0.5rem 0;
}

.quiz-code-display {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.4rem 0.8rem;
  background: linear-gradient(135deg, rgba(59, 130, 246, 0.1) 0%, rgba(139, 92, 246, 0.1) 100%);
  border: 1px solid rgba(59, 130, 246, 0.3);
  border-radius: 8px;
  margin-bottom: 0.5rem;
  font-size: 0.85rem;
}

.code-label {
  font-weight: 600;
  color: #6b7280;
}

.code-value {
  font-family: 'Courier New', monospace;
  font-weight: 700;
  color: #3b82f6;
  letter-spacing: 1px;
}

.quiz-status {
  flex-shrink: 0;
}

.status-badge {
  padding: 0.25rem 0.75rem;
  border-radius: 12px;
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
}

.status-badge.draft {
  background: #e5e7eb;
  color: #6b7280;
}

.status-badge.published {
  background: #B3D8A8;
  color: #3D8D7A;
}

.status-badge.archived {
  background: #fef3c7;
  color: #92400e;
}

.quiz-description {
  color: #6b7280;
  font-size: 0.875rem;
  margin-bottom: 1rem;
  line-height: 1.5;
}

.quiz-meta {
  display: flex;
  gap: 1rem;
  margin-bottom: 1rem;
  flex-wrap: wrap;
}

.quiz-questions, .quiz-points, .quiz-time {
  display: flex;
  align-items: center;
  gap: 0.25rem;
  font-size: 0.875rem;
  color: #6b7280;
}

.quiz-stats {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 0.75rem;
  margin-bottom: 1rem;
  padding: 1rem;
  background: #FBFFE4;
  border-radius: 8px;
}

.stat {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
}

.stat-icon {
  font-size: 1.25rem;
  margin-bottom: 0.25rem;
}

.stat-number {
  font-weight: 700;
  color: #3D8D7A;
  font-size: 0.9rem;
}

.stat-label {
  font-size: 0.7rem;
  color: #6b7280;
  text-transform: uppercase;
}

.quiz-actions {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 0.5rem;
}

.action-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  padding: 0.5rem 0.75rem;
  border: none;
  border-radius: 6px;
  font-size: 0.875rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s ease;
  text-align: center;
}

.action-btn.primary {
  background: #3D8D7A;
  color: white;
}

.action-btn.primary:hover {
  background: #2d6a5a;
}

.action-btn.secondary {
  background: #B3D8A8;
  color: #3D8D7A;
}

.action-btn.secondary:hover {
  background: #a0c995;
}

.action-btn.success {
  background: #22c55e;
  color: white;
}

.action-btn.success:hover {
  background: #16a34a;
}

.action-btn.warning {
  background: #f59e0b;
  color: white;
}

.action-btn.warning:hover {
  background: #d97706;
}

.action-btn.danger {
  background: #ef4444;
  color: white;
}

.action-btn.danger:hover {
  background: #dc2626;
}

/* Modal Styles */
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

.modal-content {
  background: white;
  border-radius: 12px;
  max-width: 600px;
  width: 100%;
  max-height: 80vh;
  overflow-y: auto;
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.5rem;
  border-bottom: 1px solid #e5e7eb;
}

.modal-header h2 {
  color: #3D8D7A;
  font-size: 1.25rem;
  font-weight: 600;
  margin: 0;
}

.close-btn {
  background: none;
  border: none;
  color: #6b7280;
  cursor: pointer;
  padding: 0.5rem;
  border-radius: 6px;
  transition: all 0.2s ease;
}

.close-btn:hover {
  color: #3D8D7A;
  background: #f3f4f6;
}

.modal-body {
  padding: 1.5rem;
}

.quiz-overview {
  margin-bottom: 1.5rem;
}

.quiz-code-section {
  margin-bottom: 1.5rem;
  padding-bottom: 1.5rem;
  border-bottom: 2px solid rgba(0, 0, 0, 0.1);
}

.code-display-box {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 1.5rem;
  background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%);
  border: 2px solid #3b82f6;
  border-radius: 16px;
  box-shadow: 0 4px 15px rgba(59, 130, 246, 0.2);
}

.code-label-large {
  font-size: 0.9rem;
  font-weight: 600;
  color: #6b7280;
  text-transform: uppercase;
  letter-spacing: 1px;
  margin-bottom: 0.5rem;
}

.code-value-large {
  font-family: 'Courier New', monospace;
  font-size: 2rem;
  font-weight: 800;
  color: #3b82f6;
  letter-spacing: 3px;
  text-shadow: 0 2px 4px rgba(59, 130, 246, 0.2);
}

.quiz-description-modal {
  color: #6b7280;
  margin-bottom: 1.5rem;
  line-height: 1.6;
}

.overview-stats {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1rem;
  margin-bottom: 1.5rem;
}

.stat-item {
  text-align: center;
  padding: 1rem;
  background: #FBFFE4;
  border-radius: 8px;
  border: 1px solid #A3D1C6;
}

.stat-value {
  display: block;
  font-size: 1.25rem;
  font-weight: 700;
  color: #3D8D7A;
  margin-bottom: 0.25rem;
}

.stat-label {
  font-size: 0.75rem;
  color: #6b7280;
  text-transform: uppercase;
}

.questions-preview h4 {
  color: #3D8D7A;
  font-size: 1.125rem;
  font-weight: 600;
  margin-bottom: 1rem;
}

.questions-list {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
  max-height: 300px;
  overflow-y: auto;
  padding-right: 0.5rem;
}

.question-preview {
  display: flex;
  gap: 0.75rem;
  padding: 1rem;
  background: #FBFFE4;
  border-radius: 8px;
  border: 1px solid #A3D1C6;
}

.question-number {
  background: #3D8D7A;
  color: white;
  width: 28px;
  height: 28px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 600;
  font-size: 0.875rem;
  flex-shrink: 0;
}

.question-content {
  flex: 1;
}

.question-text {
  color: #374151;
  font-weight: 500;
  margin: 0 0 0.5rem 0;
  line-height: 1.5;
}

.question-meta {
  display: flex;
  gap: 0.75rem;
  font-size: 0.75rem;
}

.question-type {
  background: #B3D8A8;
  color: #3D8D7A;
  padding: 0.25rem 0.5rem;
  border-radius: 4px;
  font-weight: 500;
}

.question-points {
  background: #A3D1C6;
  color: #3D8D7A;
  padding: 0.25rem 0.5rem;
  border-radius: 4px;
  font-weight: 500;
}

.loading-questions {
  text-align: center;
  padding: 2rem;
  color: #6b7280;
}

.no-questions {
  text-align: center;
  padding: 2rem;
  color: #6b7280;
}

/* Dark Mode */
.dark-mode {
  background: #23272b;
  color: #A3D1C6;
}

.dark-mode .section-header-card,
.dark-mode .quiz-card,
.dark-mode .loading-state,
.dark-mode .error-state,
.dark-mode .empty-state,
.dark-mode .modal-content {
  background: #2d3238;
  border-color: #3D8D7A;
  color: #A3D1C6;
}

.dark-mode .section-header-title {
  color: #A3D1C6;
}

.dark-mode .section-header-subtitle {
  color: #9ca3af;
}

.dark-mode .quiz-title {
  color: #A3D1C6;
}

.dark-mode .quiz-description,
.dark-mode .quiz-description-modal {
  color: #9ca3af;
}

.dark-mode .quiz-questions,
.dark-mode .quiz-points,
.dark-mode .quiz-time {
  color: #9ca3af;
}

.dark-mode .quiz-stats {
  background: #1a1e21;
}

.dark-mode .stat-number {
  color: #A3D1C6;
}

.dark-mode .stat-label {
  color: #9ca3af;
}

.dark-mode .status-badge.published {
  background: #3D8D7A;
  color: #FBFFE4;
}

.dark-mode .modal-header {
  border-bottom-color: #3D8D7A;
}

.dark-mode .modal-header h2 {
  color: #A3D1C6;
}

.dark-mode .close-btn {
  color: #9ca3af;
}

.dark-mode .close-btn:hover {
  background: #3D8D7A;
  color: #FBFFE4;
}

.dark-mode .stat-item {
  background: #1a1e21;
  border-color: #3D8D7A;
}

.dark-mode .stat-value {
  color: #A3D1C6;
}

.dark-mode .question-preview {
  background: #1a1e21;
  border-color: #3D8D7A;
}

.dark-mode .question-number {
  background: #A3D1C6;
  color: #23272b;
}

.dark-mode .question-text {
  color: #A3D1C6;
}

.dark-mode .question-type,
.dark-mode .question-points {
  background: #3D8D7A;
  color: #FBFFE4;
}

.dark-mode .loading-questions,
.dark-mode .no-questions {
  color: #9ca3af;
}

.dark-mode .code-display-box {
  background: linear-gradient(135deg, rgba(59, 130, 246, 0.1) 0%, rgba(139, 92, 246, 0.1) 100%);
  border-color: #3b82f6;
}

.dark-mode .code-value-large {
  color: #60a5fa;
}

.dark-mode .quiz-code-display {
  background: rgba(59, 130, 246, 0.15);
  border-color: rgba(59, 130, 246, 0.4);
}

.dark-mode .code-value {
  color: #60a5fa;
}

.dark-mode .quiz-code-section {
  border-bottom-color: rgba(163, 209, 198, 0.2);
}

.dark-mode .back-button {
  background: #3a3f45;
  color: #A3D1C6;
}

.dark-mode .back-button:hover {
  background: #444951;
}

/* Responsive Design */
@media (max-width: 768px) {
  .view-quizzes-container {
    padding: 1rem;
  }
  
  .section-header-content {
    flex-direction: column;
    gap: 1rem;
    align-items: stretch;
  }
  
  .header-actions {
    flex-direction: column;
  }
  
  .quizzes-grid {
    grid-template-columns: 1fr;
  }
  
  .quiz-actions {
    grid-template-columns: 1fr;
  }
  
  .modal-overlay {
    padding: 0.5rem;
  }
  
  .overview-stats {
    grid-template-columns: repeat(2, 1fr);
  }
}
</style>