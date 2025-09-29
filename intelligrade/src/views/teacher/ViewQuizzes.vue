<template>
  <div class="view-quizzes-container" :class="{ 'dark-mode': isDarkMode }">
    <!-- Enhanced Header Section -->
    <div class="section-header-card">
      <div class="header-bg-decoration"></div>
      <div class="floating-shapes">
        <div class="shape shape-1"></div>
        <div class="shape shape-2"></div>
        <div class="shape shape-3"></div>
      </div>
      
      <div class="section-header-content">
        <div class="section-header-left">
          <div class="section-header-icon">
            <svg width="40" height="40" viewBox="0 0 24 24" fill="currentColor">
              <path d="M14,2H6A2,2 0 0,0 4,4V20A2,2 0 0,0 6,22H18A2,2 0 0,0 20,20V8L14,2M18,20H6V4H13V9H18V20Z" />
            </svg>
          </div>
          <div class="header-text">
            <div class="section-header-title">Quiz Management</div>
            <div class="section-header-subtitle">{{ subjectName }} (Grade {{ gradeLevel }})</div>
            <div class="section-header-description">{{ sectionName }} - {{ sectionCode }}</div>
          </div>
        </div>
        
        <div class="header-actions">
          <button @click="navigateToCreateQuiz" class="create-quiz-btn">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M19,13H13V19H11V13H5V11H11V5H13V11H19V13Z" />
            </svg>
            Create New Quiz
          </button>
          <button @click="goBack" class="back-button">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M10 19l-7-7 7-7m-7 7h18"></path>
            </svg>
            Back to Subjects
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
        <button @click="navigateToCreateQuiz" class="create-first-quiz-btn">
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
              <div class="quiz-meta">
                <span class="quiz-questions">{{ quiz.question_count }} Questions</span>
                <span class="quiz-points">{{ quiz.total_points }} Points</span>
                <span v-if="quiz.time_limit" class="quiz-time">{{ quiz.time_limit }} Minutes</span>
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
              <span class="stat-number">{{ quiz.attempts || 0 }}</span>
              <span class="stat-label">Attempts</span>
            </div>
            <div class="stat">
              <span class="stat-number">{{ quiz.average_score || 0 }}%</span>
              <span class="stat-label">Avg Score</span>
            </div>
            <div class="stat">
              <span class="stat-number">{{ formatDate(quiz.created_at) }}</span>
              <span class="stat-label">Created</span>
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
            <div class="overview-stats">
              <div class="stat-item">
                <span class="stat-value">{{ selectedQuiz.question_count }}</span>
                <span class="stat-label">Questions</span>
              </div>
              <div class="stat-item">
                <span class="stat-value">{{ selectedQuiz.total_points }}</span>
                <span class="stat-label">Total Points</span>
              </div>
              <div class="stat-item">
                <span class="stat-value">{{ selectedQuiz.time_limit || 'No Limit' }}</span>
                <span class="stat-label">Time Limit</span>
              </div>
            </div>
          </div>

          <div class="questions-preview">
            <h4>Questions Preview</h4>
            <div v-if="selectedQuizQuestions.length > 0" class="questions-list">
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
            <div v-else class="loading-questions">
              <p>Loading questions...</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { supabase } from '../../supabase.js'
import { useDarkMode } from '../../composables/useDarkMode.js'

// Dark mode
const { isDarkMode, initDarkMode } = useDarkMode()

const router = useRouter()
const route = useRoute()

// Get data from route
const subjectId = ref(route.params.subjectId)
const sectionId = ref(route.params.sectionId)
const subjectName = ref(route.query.subjectName || '')
const sectionName = ref(route.query.sectionName || '')
const gradeLevel = ref(route.query.gradeLevel || '')
const sectionCode = ref(route.query.sectionCode || '')

// State
const quizzes = ref([])
const selectedQuiz = ref(null)
const selectedQuizQuestions = ref([])
const isLoading = ref(false)
const error = ref(null)

// Methods
const fetchQuizzes = async () => {
  isLoading.value = true
  error.value = null
  
  try {
    const { data: { user } } = await supabase.auth.getUser()
    if (!user) throw new Error('Please login to continue')

    // Fetch quizzes with question count
    const { data: quizzesData, error: quizzesError } = await supabase
      .from('quizzes')
      .select(`
        *,
        quiz_questions!inner(id, points)
      `)
      .eq('subject_id', subjectId.value)
      .eq('section_id', sectionId.value)
      .eq('teacher_id', user.id)
      .order('created_at', { ascending: false })

    if (quizzesError) throw quizzesError

    // Process quiz data to add question count and total points
    quizzes.value = (quizzesData || []).map(quiz => ({
      ...quiz,
      question_count: quiz.quiz_questions.length,
      total_points: quiz.quiz_questions.reduce((sum, q) => sum + q.points, 0)
    }))

  } catch (err) {
    console.error('Error fetching quizzes:', err)
    error.value = err.message
  } finally {
    isLoading.value = false
  }
}

const viewQuizDetails = async (quiz) => {
  selectedQuiz.value = quiz
  
  // Fetch questions for this quiz
  try {
    const { data: questions, error } = await supabase
      .from('quiz_questions')
      .select('*')
      .eq('quiz_id', quiz.id)
      .order('question_number')
    
    if (error) throw error
    selectedQuizQuestions.value = questions || []
  } catch (err) {
    console.error('Error fetching quiz questions:', err)
    selectedQuizQuestions.value = []
  }
}

const editQuiz = async (quiz) => {
  // Navigate to edit quiz (you'll need to create this route)
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
    console.error('Navigation error:', error)
  }
}

const toggleQuizStatus = async (quiz) => {
  const newStatus = quiz.status === 'published' ? 'draft' : 'published'
  
  try {
    const { error } = await supabase
      .from('quizzes')
      .update({ status: newStatus })
      .eq('id', quiz.id)
    
    if (error) throw error
    
    quiz.status = newStatus
    alert(`Quiz ${newStatus === 'published' ? 'published' : 'unpublished'} successfully!`)
  } catch (err) {
    console.error('Error updating quiz status:', err)
    alert(`Error updating quiz: ${err.message}`)
  }
}

const deleteQuiz = async (quiz) => {
  if (!confirm(`Are you sure you want to delete "${quiz.title}"? This action cannot be undone.`)) return
  
  try {
    const { error } = await supabase
      .from('quizzes')
      .delete()
      .eq('id', quiz.id)
    
    if (error) throw error
    
    quizzes.value = quizzes.value.filter(q => q.id !== quiz.id)
    alert('Quiz deleted successfully!')
  } catch (err) {
    console.error('Error deleting quiz:', err)
    alert(`Error deleting quiz: ${err.message}`)
  }
}

const navigateToCreateQuiz = async () => {
  try {
    await router.push({
      name: 'CreateQuiz',
      params: {
        subjectId: subjectId.value,
        sectionId: sectionId.value
      },
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
    console.error('Navigation error:', error)
  }
}

const closeModal = () => {
  selectedQuiz.value = null
  selectedQuizQuestions.value = []
}

const formatStatus = (status) => {
  return status.charAt(0).toUpperCase() + status.slice(1)
}

const formatDate = (dateString) => {
  return new Date(dateString).toLocaleDateString()
}

const formatQuestionType = (type) => {
  const types = {
    'multiple-choice': 'Multiple Choice',
    'true-false': 'True/False',
    'short-answer': 'Short Answer'
  }
  return types[type] || type
}

// Lifecycle
onMounted(() => {
  initDarkMode()
  fetchQuizzes()
})
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

.view-quizzes-container {
  padding: 2rem;
  max-width: 1400px;
  margin: 0 auto;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  background: var(--bg-primary);
  min-height: 100vh;
  color: var(--primary-text-color);
  transition: all 0.3s ease;
}

/* Enhanced Header Design */
.section-header-card {
  position: relative;
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.95) 0%, rgba(248, 250, 252, 0.9) 100%);
  backdrop-filter: blur(20px);
  border-radius: 32px;
  padding: 3.5rem;
  margin-bottom: 2.5rem;
  min-height: 180px;
  box-shadow: 
    0 20px 60px rgba(0, 0, 0, 0.05),
    0 8px 32px rgba(0, 0, 0, 0.03),
    inset 0 1px 0 rgba(255, 255, 255, 0.8);
  border: 2px solid rgba(255, 255, 255, 0.3);
  overflow: hidden;
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}

.section-header-card:hover {
  transform: translateY(-2px);
  box-shadow: 
    0 32px 80px rgba(0, 0, 0, 0.08),
    0 12px 40px rgba(0, 0, 0, 0.04),
    inset 0 1px 0 rgba(255, 255, 255, 0.9);
}

.header-bg-decoration {
  position: absolute;
  top: -50%;
  right: -20%;
  width: 120%;
  height: 200%;
  background: radial-gradient(ellipse at center, rgba(79, 70, 229, 0.08) 0%, transparent 70%);
  z-index: 1;
}

.floating-shapes {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 1;
  pointer-events: none;
}

.shape {
  position: absolute;
  border-radius: 50%;
  background: linear-gradient(135deg, rgba(79, 70, 229, 0.1) 0%, rgba(124, 58, 237, 0.05) 100%);
}

.shape-1 {
  width: 120px;
  height: 120px;
  top: -30px;
  right: 10%;
  animation: float 6s ease-in-out infinite;
}

.shape-2 {
  width: 80px;
  height: 80px;
  bottom: -20px;
  right: 25%;
  animation: float 8s ease-in-out infinite reverse;
}

.shape-3 {
  width: 60px;
  height: 60px;
  top: 50%;
  right: 5%;
  animation: float 7s ease-in-out infinite;
}

@keyframes float {
  0%, 100% { transform: translateY(0) rotate(0deg); }
  50% { transform: translateY(-20px) rotate(10deg); }
}

.header-bg-decoration {
  position: absolute;
  top: -50%;
  right: -20%;
  width: 120%;
  height: 200%;
  background: radial-gradient(ellipse at center, rgba(61, 141, 122, 0.08) 0%, transparent 70%);
  z-index: 1;
}

.floating-shapes {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 1;
  pointer-events: none;
}

.shape {
  position: absolute;
  border-radius: 50%;
  background: linear-gradient(135deg, rgba(61, 141, 122, 0.1) 0%, rgba(163, 209, 198, 0.05) 100%);
}

.shape-1 {
  width: 100px;
  height: 100px;
  top: -20px;
  right: 15%;
  animation: float 6s ease-in-out infinite;
}

.shape-2 {
  width: 60px;
  height: 60px;
  bottom: -10px;
  right: 25%;
  animation: float 8s ease-in-out infinite reverse;
}

@keyframes float {
  0%, 100% { transform: translateY(0) rotate(0deg); }
  50% { transform: translateY(-15px) rotate(10deg); }
}

.section-header-content {
  position: relative;
  z-index: 2;
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
}

.section-header-left {
  display: flex;
  align-items: center;
  gap: 2.5rem;
}

.section-header-icon {
  width: 80px;
  height: 80px;
  background: linear-gradient(135deg, #10b981 0%, #059669 100%);
  border-radius: 24px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #fff;
  box-shadow: 0 8px 24px rgba(79, 70, 229, 0.3);
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.section-header-icon:hover {
  transform: translateY(-2px);
}

.header-text {
  display: flex;
  flex-direction: column;
  gap: 0.3rem;
}

.section-header-title {
  font-size: 2rem;
  font-weight: 800;
  color: #10b981;
  margin-bottom: 0.25rem;
  letter-spacing: -0.025em;
}

.section-header-subtitle {
  font-size: 1.1rem;
  font-weight: 600;
  color: #64748b;
}

.section-header-description {
  font-size: 0.9rem;
  color: #94a3b8;
}

.header-actions {
  display: flex;
  gap: 1rem;
  align-items: center;
}

.create-quiz-btn {
  background: linear-gradient(135deg, #10b981 0%, #059669 100%);
  color: white;
  border: none;
  padding: 0.875rem 1.75rem;
  border-radius: 0.75rem;
  cursor: pointer;
  font-weight: 600;
  font-size: 0.875rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  box-shadow: 0 4px 14px rgba(16, 185, 129, 0.3);
}

.create-quiz-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(16, 185, 129, 0.4);
}

.back-button {
  background: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(10px);
  border: 2px solid rgba(148, 163, 184, 0.2);
  color: #64748b;
  padding: 0.875rem 1.75rem;
  border-radius: 0.75rem;
  cursor: pointer;
  font-weight: 600;
  font-size: 0.875rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.back-button:hover {
  background: rgba(148, 163, 184, 0.1);
  border-color: rgba(148, 163, 184, 0.3);
  transform: translateY(-1px);
}

.back-button {
  background: rgba(255, 255, 255, 0.8);
  border: 1px solid rgba(203, 213, 225, 0.5);
  border-radius: 16px;
  padding: 0.875rem 1.5rem;
  backdrop-filter: blur(10px);
  display: flex;
  align-items: center;
  gap: 0.5rem;
  color: #64748b;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
}

.back-button:hover {
  background: rgba(255, 255, 255, 0.95);
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1);
}

.main-wrapper {
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(20px);
  border-radius: 32px;
  padding: 3rem;
  box-shadow: 
    0 20px 60px rgba(0, 0, 0, 0.05),
    0 8px 32px rgba(0, 0, 0, 0.03),
    inset 0 1px 0 rgba(255, 255, 255, 0.8);
  border: 2px solid rgba(255, 255, 255, 0.3);
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

/* States */
.loading-state, .error-state, .empty-state {
  text-align: center;
  padding: 4rem 2rem;
}

.loading-spinner {
  width: 40px;
  height: 40px;
  border: 4px solid rgba(61, 141, 122, 0.1);
  border-left: 4px solid #10b981;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin: 0 auto 1rem;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

.error-icon, .empty-icon {
  color: #94a3b8;
  margin-bottom: 1.5rem;
}

.empty-state h3, .error-state h3 {
  color: #374151;
  font-size: 1.5rem;
  font-weight: 600;
  margin-bottom: 0.5rem;
}

.empty-state p, .error-state p {
  color: #6b7280;
  margin-bottom: 2rem;
}

.create-first-quiz-btn, .retry-btn {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  background: linear-gradient(135deg, #10b981 0%, #059669 100%);
  color: white;
  border: none;
  padding: 1rem 2rem;
  border-radius: 16px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
}

.create-first-quiz-btn:hover, .retry-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 12px 32px rgba(61, 141, 122, 0.3);
}

/* Quizzes Grid */
.quizzes-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
  gap: 2rem;
}

.quiz-card {
  background: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(20px);
  border: 2px solid rgba(255, 255, 255, 0.2);
  border-radius: 24px;
  padding: 2.5rem;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  box-shadow: 
    0 8px 32px rgba(0, 0, 0, 0.06),
    0 4px 16px rgba(0, 0, 0, 0.04);
  position: relative;
  overflow: hidden;
}

.quiz-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 4px;
  background: linear-gradient(90deg, #10b981, #059669, #10b981);
  border-radius: 1.25rem 1.25rem 0 0;
}

.quiz-card:hover {
  border-color: rgba(79, 70, 229, 0.3);
  transform: translateY(-4px);
  box-shadow: 
    0 20px 50px rgba(0, 0, 0, 0.1),
    0 8px 32px rgba(79, 70, 229, 0.15);
}

.quiz-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 1.5rem;
}

.quiz-title {
  color: #3D8D7A;
  font-size: 1.25rem;
  font-weight: 700;
  margin: 0 0 0.5rem 0;
}

.quiz-meta {
  display: flex;
  gap: 1rem;
  font-size: 0.85rem;
  color: #6b7280;
}

.quiz-meta span {
  display: flex;
  align-items: center;
  gap: 0.25rem;
}

.status-badge {
  padding: 0.3rem 0.8rem;
  border-radius: 12px;
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.status-badge.draft {
  background: rgba(156, 163, 175, 0.1);
  color: #6b7280;
}

.status-badge.published {
  background: rgba(16, 185, 129, 0.1);
  color: #10b981;
}

.status-badge.archived {
  background: rgba(239, 68, 68, 0.1);
  color: #ef4444;
}

.quiz-stats {
  display: flex;
  justify-content: space-between;
  margin: 1.5rem 0;
  padding: 1rem;
  background: rgba(248, 250, 252, 0.8);
  border-radius: 12px;
}

.stat {
  text-align: center;
}

.stat-number {
  display: block;
  font-size: 1.25rem;
  font-weight: 700;
  color: #3D8D7A;
}

.stat-label {
  font-size: 0.75rem;
  color: #6b7280;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.quiz-actions {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(100px, 1fr));
  gap: 0.75rem;
}

.action-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.4rem;
  padding: 0.6rem 1rem;
  border: none;
  border-radius: 10px;
  font-size: 0.8rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  text-align: center;
}

.action-btn.primary {
  background: linear-gradient(135deg, #3b82f6 0%, #60a5fa 100%);
  color: white;
}

.action-btn.secondary {
  background: linear-gradient(135deg, #8b5cf6 0%, #a78bfa 100%);
  color: white;
}

.action-btn.success {
  background: linear-gradient(135deg, #10b981 0%, #34d399 100%);
  color: white;
}

.action-btn.warning {
  background: linear-gradient(135deg, #f59e0b 0%, #fbbf24 100%);
  color: white;
}

.action-btn.danger {
  background: linear-gradient(135deg, #ef4444 0%, #f87171 100%);
  color: white;
}

.action-btn:hover {
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
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
  border-radius: 24px;
  max-width: 800px;
  width: 100%;
  max-height: 90vh;
  overflow-y: auto;
  box-shadow: 0 25px 70px rgba(0, 0, 0, 0.3);
}

.quiz-details-modal {
  max-width: 900px;
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 2rem 2rem 1rem;
  border-bottom: 1px solid rgba(0, 0, 0, 0.1);
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
  color: #6b7280;
  cursor: pointer;
  padding: 0.5rem;
  border-radius: 8px;
  transition: all 0.3s ease;
}

.close-btn:hover {
  color: #3D8D7A;
  background: rgba(61, 141, 122, 0.1);
}

.modal-body {
  padding: 2rem;
}

.quiz-overview {
  margin-bottom: 2rem;
}

.overview-stats {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
  gap: 1.5rem;
  margin-bottom: 2rem;
}

.stat-item {
  text-align: center;
  padding: 1.5rem;
  background: rgba(248, 250, 252, 0.8);
  border-radius: 16px;
  border: 1px solid rgba(203, 213, 225, 0.3);
}

.stat-value {
  display: block;
  font-size: 1.5rem;
  font-weight: 800;
  color: #3D8D7A;
  margin-bottom: 0.25rem;
}

.stat-label {
  font-size: 0.8rem;
  color: #6b7280;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.questions-preview {
  margin-top: 2rem;
}

.questions-preview h4 {
  color: #3D8D7A;
  font-size: 1.2rem;
  font-weight: 600;
  margin-bottom: 1.5rem;
}

.questions-list {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  max-height: 400px;
  overflow-y: auto;
}

.question-preview {
  display: flex;
  align-items: flex-start;
  gap: 1rem;
  padding: 1.5rem;
  background: rgba(248, 250, 252, 0.5);
  border-radius: 12px;
  border: 1px solid rgba(203, 213, 225, 0.2);
}

.question-number {
  background: #3D8D7A;
  color: white;
  width: 32px;
  height: 32px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 600;
  font-size: 0.9rem;
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
  gap: 1rem;
  font-size: 0.8rem;
}

.question-type {
  background: rgba(59, 130, 246, 0.1);
  color: #3b82f6;
  padding: 0.25rem 0.6rem;
  border-radius: 8px;
  font-weight: 600;
}

.question-points {
  background: rgba(16, 185, 129, 0.1);
  color: #10b981;
  padding: 0.25rem 0.6rem;
  border-radius: 8px;
  font-weight: 600;
}

.loading-questions {
  text-align: center;
  padding: 2rem;
  color: #6b7280;
}

/* Responsive Design */
@media (max-width: 768px) {
  .view-quizzes-container {
    padding: 1rem;
  }
  
  .section-header-card {
    padding: 2rem;
    margin-bottom: 2rem;
  }
  
  .section-header-content {
    flex-direction: column;
    align-items: stretch;
    gap: 1.5rem;
  }
  
  .section-header-left {
    gap: 1.5rem;
  }
  
  .header-actions {
    flex-direction: column;
    align-items: stretch;
  }
  
  .quizzes-grid {
    grid-template-columns: 1fr;
    gap: 1.5rem;
  }
  
  .quiz-card {
    padding: 1.5rem;
  }
  
  .quiz-actions {
    grid-template-columns: repeat(2, 1fr);
  }
  
  .modal-overlay {
    padding: 1rem;
  }
  
  .overview-stats {
    grid-template-columns: repeat(2, 1fr);
    gap: 1rem;
  }
  
  .question-preview {
    padding: 1rem;
  }
  
  .question-meta {
    flex-direction: column;
    gap: 0.5rem;
  }
}

/* Dark Mode Styles */
.view-quizzes-container.dark-mode {
  background: var(--bg-primary);
  color: var(--primary-text-color);
}

.dark-mode .section-header-card {
  background: var(--bg-secondary);
  border: 1px solid var(--border-color);
}

.dark-mode .section-header-title {
  color: var(--primary-text-color);
}

.dark-mode .section-header-subtitle {
  color: var(--accent-color);
}

.dark-mode .section-header-description {
  color: var(--secondary-text-color);
}

.dark-mode .create-quiz-btn {
  background: linear-gradient(135deg, var(--accent-color) 0%, #4a9b87 100%);
}

.dark-mode .back-button {
  background: var(--bg-card);
  border: 2px solid var(--border-color);
  color: var(--secondary-text-color);
}

.dark-mode .back-button:hover {
  border-color: var(--accent-color);
  color: var(--accent-color);
}

.dark-mode .loading-state {
  color: var(--secondary-text-color);
}

.dark-mode .loading-spinner {
  border: 4px solid rgba(95, 179, 160, 0.2);
  border-left: 4px solid var(--accent-color);
}

.dark-mode .error-state {
  background: var(--error-bg);
  border: 1px solid rgba(217, 83, 79, 0.4);
  color: var(--error-color);
}

.dark-mode .empty-state {
  color: var(--secondary-text-color);
}

.dark-mode .empty-state h3 {
  color: var(--primary-text-color);
}

.dark-mode .quiz-card {
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.3);
}

.dark-mode .quiz-card:hover {
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
  border-color: var(--accent-color);
}

.dark-mode .quiz-title {
  color: var(--primary-text-color);
}

.dark-mode .quiz-description {
  color: var(--secondary-text-color);
}

.dark-mode .quiz-meta-item {
  background: var(--bg-accent);
  color: var(--secondary-text-color);
}

.dark-mode .quiz-status {
  color: var(--primary-text-color);
}

.dark-mode .quiz-actions .quiz-action-btn {
  background: var(--bg-secondary);
  border: 1px solid var(--border-color);
  color: var(--secondary-text-color);
}

.dark-mode .quiz-actions .quiz-action-btn:hover {
  border-color: var(--accent-color);
  color: var(--accent-color);
}

.dark-mode .quiz-actions .quiz-action-btn.primary {
  background: var(--accent-color);
  color: white;
}

.dark-mode .quiz-actions .quiz-action-btn.primary:hover {
  background: var(--accent-hover);
}

.dark-mode .quiz-actions .quiz-action-btn.danger {
  background: var(--error-bg);
  border-color: var(--error-color);
  color: var(--error-color);
}

.dark-mode .quiz-actions .quiz-action-btn.danger:hover {
  background: rgba(217, 83, 79, 0.3);
}

.dark-mode .quiz-details-modal {
  background: var(--bg-secondary);
}

.dark-mode .modal-overlay {
  background: rgba(0, 0, 0, 0.8);
}

.dark-mode .modal-header h3 {
  color: var(--primary-text-color);
}

.dark-mode .modal-close {
  background: rgba(239, 68, 68, 0.2);
  color: #f87171;
}

.dark-mode .modal-close:hover {
  background: rgba(239, 68, 68, 0.3);
}

.dark-mode .quiz-details h4 {
  color: var(--primary-text-color);
}

.dark-mode .detail-item {
  color: var(--secondary-text-color);
}

.dark-mode .detail-item strong {
  color: var(--primary-text-color);
}

.dark-mode .questions-preview {
  background: var(--bg-accent);
  border: 1px solid var(--border-color);
}

.dark-mode .questions-preview h4 {
  color: var(--primary-text-color);
}

.dark-mode .question-preview {
  background: var(--bg-card);
  border: 1px solid var(--border-color);
}

.dark-mode .question-number {
  background: var(--accent-color);
}

.dark-mode .question-text {
  color: var(--primary-text-color);
}

.dark-mode .question-type {
  background: var(--bg-accent-hover);
  color: var(--accent-color);
}

.dark-mode .question-points {
  color: var(--secondary-text-color);
}

.dark-mode .loading-questions {
  color: var(--secondary-text-color);
}
</style>