<template>
  <div class="view-quizzes-page">
    <!-- Header Section - Same style as CreateQuiz -->
    <div class="header-section">
      <div class="header-content">
        <div class="header-left">
          <div class="header-icon-wrapper">
            <div class="header-icon">
              <svg width="28" height="28" viewBox="0 0 24 24" fill="currentColor">
                <path d="M14,2H6A2,2 0 0,0 4,4V20A2,2 0 0,0 6,22H18A2,2 0 0,0 20,20V8L14,2M18,20H6V4H13V9H18V20Z" />
              </svg>
            </div>
          </div>
          <div class="header-text">
            <h1 class="header-title">Quiz Management</h1>
            <p class="header-subtitle">{{ subjectName }}<span v-if="sectionName"> - {{ sectionName }}</span></p>
            <div class="header-breadcrumb">
              <span class="breadcrumb-item">Grade {{ gradeLevel }}</span>
              <span class="breadcrumb-separator">•</span>
              <span class="breadcrumb-item">{{ sectionCode }}</span>
            </div>
          </div>
        </div>
        <div class="header-actions">
          <button @click="navigateToCreateQuiz" class="action-btn primary">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M19,13H13V19H11V13H5V11H11V5H13V11H19V13Z" />
            </svg>
            Create Quiz
          </button>
          <button @click="goBack" class="action-btn secondary">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M20,11V13H8L13.5,18.5L12.08,19.92L4.16,12L12.08,4.08L13.5,5.5L8,11H20Z" />
            </svg>
            Back to Sections
          </button>
        </div>
      </div>
    </div>

    <!-- Main Content Container - Same as CreateQuiz -->
    <div class="main-container">
      <div class="container">
        <!-- Loading State -->
        <div v-if="isLoading" class="status-card loading-card">
          <div class="status-icon">
            <div class="spinner"></div>
          </div>
          <h3 class="status-title">Loading Quiz Data...</h3>
          <p class="status-description">Please wait while we fetch your quizzes.</p>
        </div>

        <!-- Error State -->
        <div v-else-if="error" class="status-card error-card">
          <div class="status-icon error-icon">
            <svg width="80" height="80" viewBox="0 0 24 24" fill="currentColor">
              <path d="M11,15H13V17H11V15M11,7H13V13H11V7M12,2C6.47,2 2,6.5 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2M12,20A8,8 0 0,1 4,12A8,8 0 0,1 12,4A8,8 0 0,1 20,12A8,8 0 0,1 12,20Z" />
            </svg>
          </div>
          <h3 class="status-title">Error Loading Quizzes</h3>
          <p class="status-description">{{ error }}</p>
          <div class="status-actions">
            <button @click="fetchQuizzes" class="btn btn-primary">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                <path d="M4,11V13H16L10.5,18.5L11.92,19.92L19.84,12L11.92,4.08L10.5,5.5L16,11H4Z"/>
              </svg>
              Try Again
            </button>
          </div>
        </div>

        <!-- Empty State -->
        <div v-else-if="quizzes.length === 0" class="status-card empty-state-card">
          <div class="status-icon">
            <svg width="80" height="80" viewBox="0 0 24 24" fill="currentColor">
              <path d="M14,2H6A2,2 0 0,0 4,4V20A2,2 0 0,0 6,22H18A2,2 0 0,0 20,20V8L14,2M18,20H6V4H13V9H18V20Z" />
            </svg>
          </div>
          <h3 class="status-title">No Quizzes Available</h3>
          <p class="status-description">You haven't created any quizzes for this section yet.</p>
          <div class="status-actions">
            <button @click="navigateToCreateQuiz" class="create-quiz-btn">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                <path d="M19,13H13V19H11V13H5V11H11V5H13V11H19V13Z" />
              </svg>
              Create Your First Quiz
            </button>
          </div>
        </div>

        <!-- Quizzes Grid -->
        <div v-else class="content-section">
          <div class="section-header">
            <div class="section-icon">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                <path d="M14,2H6A2,2 0 0,0 4,4V20A2,2 0 0,0 6,22H18A2,2 0 0,0 20,20V8L14,2M18,20H6V4H13V9H18V20Z" />
              </svg>
            </div>
            <div class="section-content">
              <h2 class="section-title">Your Quizzes</h2>
              <p class="section-subtitle">{{ quizzes.length }} quiz{{ quizzes.length !== 1 ? 'es' : '' }} created</p>
            </div>
          </div>

          <div class="quizzes-grid-modern">
            <div v-for="quiz in quizzes" :key="quiz.id" class="quiz-card-modern">
              <div class="quiz-card-header">
                <div class="quiz-status-badge" :class="quiz.status">
                  <span class="status-indicator"></span>
                  {{ formatStatus(quiz.status) }}
                </div>
                <div class="quiz-menu">
                  <button @click="deleteQuiz(quiz)" class="menu-btn danger">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor">
                      <path d="M19,4H15.5L14.5,3H9.5L8.5,4H5V6H19M6,19A2,2 0 0,0 8,21H16A2,2 0 0,0 18,19V7H6V19Z" />
                    </svg>
                  </button>
                </div>
              </div>

              <div class="quiz-card-body">
                <h3 class="quiz-title-modern">{{ quiz.title }}</h3>
                
                <!-- Quiz Code Display -->
                <div class="quiz-code-modern">
                  <span class="code-icon">
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor">
                      <path d="M8,3A2,2 0 0,0 6,5V9A2,2 0 0,1 4,11H3V13H4A2,2 0 0,1 6,15V19A2,2 0 0,0 8,21H10V19H8V14A2,2 0 0,0 6,12A2,2 0 0,0 8,10V5H10V3M16,3A2,2 0 0,1 18,5V9A2,2 0 0,0 20,11H21V13H20A2,2 0 0,0 18,15V19A2,2 0 0,1 16,21H14V19H16V14A2,2 0 0,1 18,12A2,2 0 0,1 16,10V5H14V3H16Z" />
                    </svg>
                  </span>
                  <span class="code-text">{{ quiz.quiz_code || 'N/A' }}</span>
                </div>

                <p v-if="quiz.description" class="quiz-description-modern">{{ quiz.description }}</p>

                <!-- Quiz Stats -->
                <div class="quiz-stats-modern">
                  <div class="stat-item-modern">
                    <div class="stat-icon-modern">
                      <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                        <path d="M9,22A1,1 0 0,1 8,21V18H4A2,2 0 0,1 2,16V4C2,2.89 2.9,2 4,2H20A2,2 0 0,1 22,4V16A2,2 0 0,1 20,18H13.9L10.2,21.71C10,21.9 9.75,22 9.5,22V22H9M10,16V19.08L13.08,16H20V4H4V16H10Z" />
                      </svg>
                    </div>
                    <div class="stat-content-modern">
                      <span class="stat-number-modern">{{ quiz.question_count || 0 }}</span>
                      <span class="stat-label-modern">Questions</span>
                    </div>
                  </div>

                  <div class="stat-item-modern">
                    <div class="stat-icon-modern">
                      <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                        <path d="M12,17.27L18.18,21L16.54,13.97L22,9.24L14.81,8.62L12,2L9.19,8.62L2,9.24L7.45,13.97L5.82,21L12,17.27Z" />
                      </svg>
                    </div>
                    <div class="stat-content-modern">
                      <span class="stat-number-modern">{{ quiz.total_points || 0 }}</span>
                      <span class="stat-label-modern">Points</span>
                    </div>
                  </div>

                  <div class="stat-item-modern" v-if="quiz.has_time_limit && quiz.time_limit_minutes">
                    <div class="stat-icon-modern">
                      <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                        <path d="M12,20A8,8 0 0,0 20,12A8,8 0 0,0 12,4A8,8 0 0,0 4,12A8,8 0 0,0 12,20M12,2A10,10 0 0,1 22,12A10,10 0 0,1 12,22C6.47,22 2,17.5 2,12A10,10 0 0,1 12,2M12.5,7V12.25L17,14.92L16.25,16.15L11,13V7H12.5Z" />
                      </svg>
                    </div>
                    <div class="stat-content-modern">
                      <span class="stat-number-modern">{{ quiz.time_limit_minutes }}</span>
                      <span class="stat-label-modern">Minutes</span>
                    </div>
                  </div>

                  <div class="stat-item-modern">
                    <div class="stat-icon-modern">
                      <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                        <path d="M1,4 L1,10 L7,10"/>
                      </svg>
                    </div>
                    <div class="stat-content-modern">
                      <span class="stat-number-modern">{{ quiz.attempts_allowed === 999 ? '∞' : quiz.attempts_allowed }}</span>
                      <span class="stat-label-modern">Attempts</span>
                    </div>
                  </div>
                </div>

                <!-- Quiz Meta Info -->
                <div class="quiz-meta-modern">
                  <span class="meta-item-modern">
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor">
                      <path d="M19 3h-1V1h-2v2H8V1H6v2H5c-1.11 0-1.99.9-1.99 2L3 19c0 1.1.89 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm0 16H5V8h14v11zM7 10h5v5H7z"/>
                    </svg>
                    Created {{ formatDate(quiz.created_at) }}
                  </span>
                  <span class="meta-item-modern" v-if="quiz.shuffle_questions">
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor">
                      <path d="M14,20H16V18H20V16H16A2,2 0 0,1 14,14V10A2,2 0 0,1 16,8H20V6H16V4H14V6L12,8V10L14,12V14L12,16V18L14,20M10,8V10L12,12L10,14V16L4,10L10,8Z" />
                    </svg>
                    Shuffle Enabled
                  </span>
                </div>
              </div>

              <div class="quiz-card-footer">
                <button @click="viewQuizDetails(quiz)" class="action-btn-modern primary">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M12,9A3,3 0 0,0 9,12A3,3 0 0,0 12,15A3,3 0 0,0 15,12A3,3 0 0,0 12,9M12,17A5,5 0 0,1 7,12A5,5 0 0,1 12,7A5,5 0 0,1 17,12A5,5 0 0,1 12,17M12,4.5C7,4.5 2.73,7.61 1,12C2.73,16.39 7,19.5 12,19.5C17,19.5 21.27,16.39 23,12C21.27,7.61 17,4.5 12,4.5Z" />
                  </svg>
                  View Details
                </button>

                <button @click="editQuiz(quiz)" class="action-btn-modern secondary">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M20.71,7.04C21.1,6.65 21.1,6 20.71,5.63L18.37,3.29C18,2.9 17.35,2.9 16.96,3.29L15.12,5.12L18.87,8.87M3,17.25V21H6.75L17.81,9.93L14.06,6.18L3,17.25Z" />
                  </svg>
                  Edit
                </button>

                <button 
                  @click="toggleQuizStatus(quiz)" 
                  :class="['action-btn-modern', quiz.status === 'published' ? 'warning' : 'success']"
                >
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                    <path v-if="quiz.status === 'published'" d="M8.5,8.64L13.77,12L8.5,15.36V8.64M6.5,5V19L17.5,12"/>
                    <path v-else d="M12,2A10,10 0 0,1 22,12A10,10 0 0,1 12,22A10,10 0 0,1 2,12A10,10 0 0,1 12,2M11,16.5L18,9.5L16.5,8L11,13.5L7.5,10L6,11.5L11,16.5Z"/>
                  </svg>
                  {{ quiz.status === 'published' ? 'Unpublish' : 'Publish' }}
                </button>
              </div>
            </div>
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
  try {
    await router.push({ name: 'MySubjects' })
  } catch (error) {
    router.back()
  }
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
/* =============================================== */
/* MAIN PAGE STYLES - Matching CreateQuiz.vue */
/* =============================================== */

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.view-quizzes-page {
  min-height: 100vh;
  background: #f8fafc;
  font-family: 'Inter', sans-serif;
  display: flex;
  flex-direction: column;
}

.dark .view-quizzes-page {
  background: #0f172a;
}

/* Header Section - Same as CreateQuiz */
.header-section {
  background: linear-gradient(135deg, #3D8D7A 0%, #2D6A5A 100%);
  padding: 2rem 1.5rem;
  position: relative;
  overflow: hidden;
}

.dark .header-section {
  background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
}

.header-section::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 20"><defs><radialGradient id="a" cx="50%" cy="0%" r="100%"><stop offset="0%" stop-color="%23ffffff" stop-opacity="0.1"/><stop offset="100%" stop-color="%23ffffff" stop-opacity="0"/></radialGradient></defs><rect width="100" height="20" fill="url(%23a)"/></svg>') repeat-x;
  opacity: 0.5;
}

.header-content {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
  position: relative;
  z-index: 1;
}

.header-left {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.header-icon-wrapper {
  position: relative;
}

.header-icon {
  width: 60px;
  height: 60px;
  background: rgba(255, 255, 255, 0.15);
  backdrop-filter: blur(10px);
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.2);
}

.dark .header-icon {
  background: rgba(255, 255, 255, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.1);
}

.header-text h1.header-title {
  font-size: 2rem;
  font-weight: 800;
  color: white;
  margin: 0 0 0.5rem 0;
  letter-spacing: -0.025em;
}

.header-text p.header-subtitle {
  font-size: 1.1rem;
  color: rgba(255, 255, 255, 0.9);
  margin: 0 0 0.25rem 0;
  font-weight: 500;
}

.header-breadcrumb {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.875rem;
  color: rgba(255, 255, 255, 0.8);
}

.breadcrumb-item {
  font-weight: 500;
}

.breadcrumb-separator {
  color: rgba(255, 255, 255, 0.6);
}

.header-actions {
  display: flex;
  gap: 1rem;
}

.action-btn {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1.5rem;
  border-radius: 10px;
  font-weight: 600;
  font-size: 0.875rem;
  text-decoration: none;
  transition: all 0.2s ease;
  border: none;
  cursor: pointer;
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.2);
}

.action-btn.primary {
  background: rgba(16, 185, 129, 0.9);
  color: white;
  border: 1px solid rgba(16, 185, 129, 0.5);
  box-shadow: 0 4px 20px rgba(16, 185, 129, 0.3);
}

.action-btn.primary:hover {
  background: #059669;
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(16, 185, 129, 0.4);
}

.action-btn.secondary {
  background: rgba(255, 255, 255, 0.15);
  color: white;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
}

.action-btn.secondary:hover {
  background: rgba(255, 255, 255, 0.25);
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
}

.dark .action-btn.secondary {
  background: rgba(255, 255, 255, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.1);
}

.dark .action-btn.secondary:hover {
  background: rgba(255, 255, 255, 0.2);
}

/* Main Content Container - Same as CreateQuiz */
.main-container {
  flex: 1;
  padding: 2rem 1.5rem;
  display: flex;
  flex-direction: column;
}

.dark .main-container {
  background: transparent;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  width: 100%;
  flex: 1;
  display: flex;
  flex-direction: column;
}

/* Status Cards - Same as CreateQuiz Landing */
.status-card {
  background: white;
  border-radius: 16px;
  border: 1px solid rgba(226, 232, 240, 0.5);
  padding: 3rem 2rem;
  max-width: 600px;
  width: 100%;
  text-align: center;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
  transition: all 0.3s ease;
  margin: 2rem auto;
}

.dark .status-card {
  background: #1e293b;
  border-color: #334155;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.25);
}

.loading-card,
.empty-state-card {
  border-color: rgba(61, 141, 122, 0.3);
}

.error-card {
  border-color: rgba(239, 68, 68, 0.3);
}

.status-icon {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-bottom: 1.5rem;
  color: #64748b;
}

.error-icon {
  color: #ef4444;
}

.dark .status-icon {
  color: #94a3b8;
}

.status-title {
  font-size: 1.5rem;
  font-weight: 700;
  color: #1e293b;
  margin-bottom: 0.75rem;
  line-height: 1.3;
  letter-spacing: -0.025em;
}

.dark .status-title {
  color: #f1f5f9;
}

.status-description {
  font-size: 1rem;
  color: #64748b;
  margin-bottom: 2rem;
  line-height: 1.6;
  max-width: 450px;
  margin-left: auto;
  margin-right: auto;
}

.dark .status-description {
  color: #94a3b8;
}

.status-actions {
  display: flex;
  justify-content: center;
  gap: 1rem;
  flex-wrap: wrap;
}

/* Spinner Animation */
.spinner {
  width: 40px;
  height: 40px;
  border: 3px solid #f1f5f9;
  border-top: 3px solid #10b981;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

.dark .spinner {
  border-color: #1e293b;
  border-top-color: #10b981;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

/* Enhanced Create Quiz Button */
.create-quiz-btn {
  background: #10b981;
  color: white;
  border: 1px solid #10b981;
  border-radius: 10px;
  padding: 0.875rem 2rem;
  font-weight: 600;
  font-size: 1rem;
  cursor: pointer;
  transition: all 0.2s ease;
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  box-shadow: 0 2px 12px rgba(16, 185, 129, 0.15);
  min-width: 220px;
  justify-content: center;
}

.create-quiz-btn:hover {
  background: #059669;
  border-color: #047857;
  transform: translateY(-2px);
  box-shadow: 0 4px 20px rgba(16, 185, 129, 0.25);
}

/* Buttons - Same as CreateQuiz */
.btn {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1.5rem;
  border-radius: 8px;
  font-weight: 600;
  font-size: 0.875rem;
  cursor: pointer;
  transition: all 0.2s ease;
  border: none;
  text-decoration: none;
}

.btn-primary {
  background: #10b981;
  color: white;
  border: 1px solid #10b981;
}

.btn-primary:hover {
  background: #059669;
  border-color: #047857;
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(16, 185, 129, 0.25);
}

/* Content Section */
.content-section {
  margin-top: 0;
}

/* Section Headers - Same as CreateQuiz */
.section-header {
  display: flex;
  align-items: flex-start;
  gap: 1rem;
  margin-bottom: 2rem;
  padding-bottom: 1.5rem;
  border-bottom: 1px solid #e2e8f0;
}

.dark .section-header {
  border-bottom-color: #334155;
}

.section-icon {
  width: 48px;
  height: 48px;
  background: linear-gradient(135deg, #10b981 0%, #059669 100%);
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  box-shadow: 0 4px 12px rgba(16, 185, 129, 0.2);
  flex-shrink: 0;
}

.dark .section-icon {
  background: linear-gradient(135deg, #10b981 0%, #059669 100%);
  box-shadow: 0 4px 12px rgba(16, 185, 129, 0.3);
}

.section-content {
  flex: 1;
}

.section-title {
  font-size: 1.5rem;
  font-weight: 700;
  color: #1e293b;
  margin: 0 0 0.5rem 0;
  letter-spacing: -0.025em;
}

.dark .section-title {
  color: #f1f5f9;
}

.section-subtitle {
  font-size: 1rem;
  color: #64748b;
  margin: 0;
  line-height: 1.5;
}

.dark .section-subtitle {
  color: #94a3b8;
}

/* Modern Quizzes Grid */
.quizzes-grid-modern {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(380px, 1fr));
  gap: 2rem;
  margin-top: 1rem;
}

.quiz-card-modern {
  background: white;
  border: 2px solid #e2e8f0;
  border-radius: 16px;
  overflow: hidden;
  transition: all 0.3s ease;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
}

.quiz-card-modern:hover {
  border-color: #10b981;
  box-shadow: 0 8px 24px rgba(16, 185, 129, 0.15);
  transform: translateY(-4px);
}

.dark .quiz-card-modern {
  background: #1e293b;
  border-color: #374151;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.25);
}

.dark .quiz-card-modern:hover {
  border-color: #10b981;
  box-shadow: 0 8px 24px rgba(16, 185, 129, 0.25);
}

/* Quiz Card Header */
.quiz-card-header {
  background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
  border-bottom: 2px solid #e2e8f0;
  padding: 1.5rem 2rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.dark .quiz-card-header {
  background: linear-gradient(135deg, #374151 0%, #1e293b 100%);
  border-bottom-color: #475569;
}

.quiz-status-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem 1rem;
  border-radius: 20px;
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.quiz-status-badge.published {
  background: #dcfce7;
  color: #166534;
  border: 1px solid #bbf7d0;
}

.quiz-status-badge.draft {
  background: #f1f5f9;
  color: #475569;
  border: 1px solid #e2e8f0;
}

.quiz-status-badge.archived {
  background: #fef3c7;
  color: #92400e;
  border: 1px solid #fde68a;
}

.status-indicator {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: currentColor;
}

.quiz-menu {
  display: flex;
  gap: 0.5rem;
}

.menu-btn {
  width: 32px;
  height: 32px;
  border: none;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.2s ease;
}

.menu-btn.danger {
  background: #fef2f2;
  color: #ef4444;
  border: 1px solid #fecaca;
}

.menu-btn.danger:hover {
  background: #ef4444;
  color: white;
}

.dark .menu-btn.danger {
  background: #7f1d1d;
  color: #fca5a5;
  border-color: #991b1b;
}

/* Quiz Card Body */
.quiz-card-body {
  padding: 2rem;
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.quiz-title-modern {
  font-size: 1.25rem;
  font-weight: 700;
  color: #1e293b;
  margin: 0;
  line-height: 1.3;
}

.dark .quiz-title-modern {
  color: #f1f5f9;
}

.quiz-code-modern {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%);
  border: 1px solid #93c5fd;
  border-radius: 8px;
  padding: 0.5rem 0.75rem;
  font-family: 'Courier New', monospace;
  font-size: 0.875rem;
  font-weight: 600;
  color: #1d4ed8;
  align-self: flex-start;
}

.dark .quiz-code-modern {
  background: rgba(59, 130, 246, 0.1);
  border-color: rgba(59, 130, 246, 0.3);
  color: #60a5fa;
}

.code-icon {
  color: #3b82f6;
  display: flex;
  align-items: center;
}

.quiz-description-modern {
  color: #64748b;
  font-size: 0.875rem;
  line-height: 1.6;
  margin: 0;
}

.dark .quiz-description-modern {
  color: #94a3b8;
}

.quiz-stats-modern {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
  gap: 1rem;
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-radius: 12px;
  padding: 1.25rem;
}

.dark .quiz-stats-modern {
  background: #374151;
  border-color: #475569;
}

.stat-item-modern {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.stat-icon-modern {
  width: 32px;
  height: 32px;
  background: #ecfdf5;
  border: 1px solid #a7f3d0;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #059669;
  flex-shrink: 0;
}

.dark .stat-icon-modern {
  background: rgba(16, 185, 129, 0.1);
  border-color: rgba(16, 185, 129, 0.3);
  color: #34d399;
}

.stat-content-modern {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}

.stat-number-modern {
  font-size: 1rem;
  font-weight: 700;
  color: #1e293b;
  line-height: 1;
}

.dark .stat-number-modern {
  color: #f1f5f9;
}

.stat-label-modern {
  font-size: 0.75rem;
  font-weight: 500;
  color: #64748b;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  line-height: 1;
}

.dark .stat-label-modern {
  color: #94a3b8;
}

.quiz-meta-modern {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
  font-size: 0.75rem;
  color: #64748b;
}

.dark .quiz-meta-modern {
  color: #94a3b8;
}

.meta-item-modern {
  display: flex;
  align-items: center;
  gap: 0.25rem;
}

/* Quiz Card Footer */
.quiz-card-footer {
  background: #f8fafc;
  border-top: 1px solid #e2e8f0;
  padding: 1.5rem 2rem;
  display: flex;
  gap: 0.75rem;
  flex-wrap: wrap;
}

.dark .quiz-card-footer {
  background: #374151;
  border-top-color: #475569;
}

.action-btn-modern {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem 1rem;
  border: none;
  border-radius: 8px;
  font-size: 0.75rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
  text-transform: uppercase;
  letter-spacing: 0.025em;
  flex: 1;
  justify-content: center;
  min-width: 100px;
}

.action-btn-modern.primary {
  background: #10b981;
  color: white;
}

.action-btn-modern.primary:hover {
  background: #059669;
  transform: translateY(-1px);
}

.action-btn-modern.secondary {
  background: #f1f5f9;
  color: #475569;
  border: 1px solid #e2e8f0;
}

.action-btn-modern.secondary:hover {
  background: #e2e8f0;
  color: #1e293b;
}

.action-btn-modern.success {
  background: #22c55e;
  color: white;
}

.action-btn-modern.success:hover {
  background: #16a34a;
}

.action-btn-modern.warning {
  background: #f59e0b;
  color: white;
}

.action-btn-modern.warning:hover {
  background: #d97706;
}

.dark .action-btn-modern.secondary {
  background: #475569;
  color: #d1d5db;
  border-color: #6b7280;
}

.dark .action-btn-modern.secondary:hover {
  background: #6b7280;
  color: #f3f4f6;
}

/* Responsive Design */
@media (max-width: 768px) {
  .header-section {
    padding: 1.5rem 1rem;
  }
  
  .header-content {
    flex-direction: column;
    gap: 1.5rem;
    text-align: center;
  }
  
  .header-left {
    flex-direction: column;
    gap: 1rem;
  }
  
  .header-text h1.header-title {
    font-size: 1.5rem;
  }
  
  .header-text p.header-subtitle {
    font-size: 1rem;
  }
  
  .main-container {
    padding: 1.5rem 1rem;
  }

  .quizzes-grid-modern {
    grid-template-columns: 1fr;
    gap: 1.5rem;
  }
  
  .quiz-stats-modern {
    grid-template-columns: repeat(2, 1fr);
  }
  
  .quiz-card-footer {
    flex-direction: column;
    gap: 0.75rem;
  }
  
  .action-btn-modern {
    flex: none;
  }
  
  .status-card {
    padding: 2rem 1.5rem;
    margin: 1rem;
  }
}

/* =============================================== */
/* MODAL STYLES - Matching CreateQuiz Design */
/* =============================================== */

.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.6);
  backdrop-filter: blur(4px);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
  padding: 1rem;
  animation: fadeIn 0.2s ease;
}

@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

.modal-content {
  background: white;
  border-radius: 20px;
  max-width: 700px;
  width: 100%;
  max-height: 85vh;
  overflow-y: auto;
  border: 1px solid #e2e8f0;
  box-shadow: 0 25px 50px rgba(0, 0, 0, 0.25);
  animation: slideUp 0.3s ease;
}

@keyframes slideUp {
  from { 
    opacity: 0;
    transform: translateY(20px) scale(0.95);
  }
  to { 
    opacity: 1;
    transform: translateY(0) scale(1);
  }
}

.dark .modal-content {
  background: #1e293b;
  border-color: #374151;
  box-shadow: 0 25px 50px rgba(0, 0, 0, 0.5);
}

.quiz-details-modal {
  overflow: hidden;
}

.modal-header {
  background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
  border-bottom: 2px solid #e2e8f0;
  padding: 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  position: relative;
}

.dark .modal-header {
  background: linear-gradient(135deg, #374151 0%, #1e293b 100%);
  border-bottom-color: #475569;
}

.modal-header h2 {
  font-size: 1.5rem;
  font-weight: 700;
  color: #1e293b;
  margin: 0;
  letter-spacing: -0.025em;
  max-width: 500px;
}

.dark .modal-header h2 {
  color: #f1f5f9;
}

.close-btn {
  background: #f8fafc;
  border: 2px solid #e2e8f0;
  color: #64748b;
  cursor: pointer;
  padding: 0.75rem;
  border-radius: 12px;
  transition: all 0.2s ease;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 44px;
  height: 44px;
}

.close-btn:hover {
  color: #ef4444;
  background: #fef2f2;
  border-color: #fecaca;
  transform: scale(1.05);
}

.dark .close-btn {
  background: #374151;
  border-color: #475569;
  color: #94a3b8;
}

.dark .close-btn:hover {
  background: #7f1d1d;
  border-color: #991b1b;
  color: #fca5a5;
}

.modal-body {
  padding: 2rem;
}

.quiz-overview {
  margin-bottom: 2rem;
}

.quiz-code-section {
  margin-bottom: 2rem;
  padding-bottom: 1.5rem;
  border-bottom: 1px solid #e2e8f0;
}

.dark .quiz-code-section {
  border-bottom-color: #374151;
}

.code-display-box {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 2rem;
  background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%);
  border: 2px solid #3b82f6;
  border-radius: 16px;
  box-shadow: 0 8px 25px rgba(59, 130, 246, 0.2);
  position: relative;
  overflow: hidden;
}

.dark .code-display-box {
  background: linear-gradient(135deg, rgba(59, 130, 246, 0.1) 0%, rgba(59, 130, 246, 0.05) 100%);
  border-color: #3b82f6;
  box-shadow: 0 8px 25px rgba(59, 130, 246, 0.3);
}

.code-display-box::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: radial-gradient(circle at center, rgba(59, 130, 246, 0.1) 0%, transparent 70%);
}

.code-label-large {
  font-size: 0.875rem;
  font-weight: 600;
  color: #6b7280;
  text-transform: uppercase;
  letter-spacing: 1px;
  margin-bottom: 0.75rem;
  position: relative;
  z-index: 1;
}

.dark .code-label-large {
  color: #94a3b8;
}

.code-value-large {
  font-family: 'JetBrains Mono', 'Courier New', monospace;
  font-size: 2.5rem;
  font-weight: 800;
  color: #3b82f6;
  letter-spacing: 4px;
  text-shadow: 0 2px 8px rgba(59, 130, 246, 0.3);
  position: relative;
  z-index: 1;
}

.dark .code-value-large {
  color: #60a5fa;
}

.quiz-description-modal {
  color: #64748b;
  font-size: 1rem;
  margin-bottom: 1.5rem;
  line-height: 1.6;
}

.dark .quiz-description-modal {
  color: #94a3b8;
}

.overview-stats {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
  gap: 1.5rem;
  margin-bottom: 2rem;
}

.stat-item {
  text-align: center;
  padding: 1.5rem;
  background: white;
  border: 2px solid #e2e8f0;
  border-radius: 12px;
  transition: all 0.2s ease;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
}

.stat-item:hover {
  border-color: #10b981;
  box-shadow: 0 4px 16px rgba(16, 185, 129, 0.15);
  transform: translateY(-2px);
}

.dark .stat-item {
  background: #374151;
  border-color: #475569;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.25);
}

.dark .stat-item:hover {
  border-color: #10b981;
  box-shadow: 0 4px 16px rgba(16, 185, 129, 0.25);
}

.stat-value {
  display: block;
  font-size: 1.5rem;
  font-weight: 800;
  color: #10b981;
  margin-bottom: 0.5rem;
  line-height: 1;
}

.dark .stat-value {
  color: #34d399;
}

.stat-label {
  font-size: 0.75rem;
  color: #64748b;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  font-weight: 600;
}

.dark .stat-label {
  color: #94a3b8;
}

.questions-preview h4 {
  color: #1e293b;
  font-size: 1.25rem;
  font-weight: 700;
  margin-bottom: 1.5rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.dark .questions-preview h4 {
  color: #f1f5f9;
}

.questions-preview h4::before {
  content: '';
  width: 4px;
  height: 20px;
  background: #10b981;
  border-radius: 2px;
}

.questions-list {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  max-height: 350px;
  overflow-y: auto;
  padding-right: 0.5rem;
}

.question-preview {
  display: flex;
  gap: 1rem;
  padding: 1.5rem;
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-radius: 12px;
  transition: all 0.2s ease;
}

.question-preview:hover {
  border-color: #10b981;
  background: #f0fdfa;
  box-shadow: 0 4px 12px rgba(16, 185, 129, 0.1);
}

.dark .question-preview {
  background: #374151;
  border-color: #475569;
}

.dark .question-preview:hover {
  border-color: #10b981;
  background: rgba(16, 185, 129, 0.05);
}

.question-number {
  background: linear-gradient(135deg, #10b981 0%, #059669 100%);
  color: white;
  width: 32px;
  height: 32px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 0.875rem;
  flex-shrink: 0;
  box-shadow: 0 4px 12px rgba(16, 185, 129, 0.3);
}

.question-content {
  flex: 1;
  min-width: 0;
}

.question-text {
  color: #1e293b;
  font-weight: 600;
  margin: 0 0 0.75rem 0;
  line-height: 1.5;
  word-break: break-word;
}

.dark .question-text {
  color: #f1f5f9;
}

.question-meta {
  display: flex;
  gap: 0.75rem;
  font-size: 0.75rem;
  flex-wrap: wrap;
}

.question-type {
  background: #ecfdf5;
  color: #059669;
  padding: 0.375rem 0.75rem;
  border-radius: 6px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.025em;
  border: 1px solid #a7f3d0;
}

.dark .question-type {
  background: rgba(16, 185, 129, 0.1);
  color: #34d399;
  border-color: rgba(16, 185, 129, 0.3);
}

.question-points {
  background: #fef3c7;
  color: #d97706;
  padding: 0.375rem 0.75rem;
  border-radius: 6px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.025em;
  border: 1px solid #fde68a;
}

.dark .question-points {
  background: rgba(245, 158, 11, 0.1);
  color: #fbbf24;
  border-color: rgba(245, 158, 11, 0.3);
}

.loading-questions {
  text-align: center;
  padding: 3rem;
  color: #64748b;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
}

.dark .loading-questions {
  color: #94a3b8;
}

.loading-questions .loading-spinner-small {
  width: 32px;
  height: 32px;
  border: 3px solid #e2e8f0;
  border-top: 3px solid #10b981;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin: 0;
}

.no-questions {
  text-align: center;
  padding: 3rem;
  color: #64748b;
  font-style: italic;
}

.dark .no-questions {
  color: #94a3b8;
}

/* Responsive Modal */
@media (max-width: 768px) {
  .modal-overlay {
    padding: 0.5rem;
  }
  
  .modal-content {
    max-height: 90vh;
  }
  
  .modal-header {
    padding: 1.5rem;
  }
  
  .modal-header h2 {
    font-size: 1.25rem;
  }
  
  .modal-body {
    padding: 1.5rem;
  }
  
  .overview-stats {
    grid-template-columns: repeat(2, 1fr);
    gap: 1rem;
  }
  
  .stat-item {
    padding: 1rem;
  }
  
  .code-display-box {
    padding: 1.5rem;
  }
  
  .code-value-large {
    font-size: 2rem;
    letter-spacing: 3px;
  }
  
  .question-preview {
    padding: 1rem;
    flex-direction: column;
    text-align: center;
  }
  
  .question-number {
    align-self: center;
  }
}</style>