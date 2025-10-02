<template>
  <div class="take-quiz-page" :class="{ 'dark-mode': isDarkMode }">
    <!-- Quiz Header -->
    <div class="quiz-header-card">
      <div class="header-bg-decoration"></div>
      <div class="floating-shapes">
        <div class="shape shape-1"></div>
        <div class="shape shape-2"></div>
        <div class="shape shape-3"></div>
      </div>
      
      <div class="quiz-header-content">
        <div class="quiz-header-left">
          <div class="quiz-header-icon">
            <svg width="36" height="36" viewBox="0 0 24 24" fill="currentColor">
              <path d="M14,2H6A2,2 0 0,0 4,4V20A2,2 0 0,0 6,22H18A2,2 0 0,0 20,20V8L14,2M18,20H6V4H13V9H18V20Z" />
            </svg>
          </div>
          
          <div class="header-text">
            <div class="quiz-header-title">{{ quiz?.title || 'Loading Quiz...' }}</div>
            <div class="quiz-header-subtitle">{{ quiz?.subject_name }} - {{ quiz?.section_name }}</div>
            <div class="quiz-header-description" v-if="quiz">
              {{ quiz.total_points }} points • {{ quiz.questions?.length || 0 }} questions
              <span v-if="quiz.time_limit"> • {{ quiz.time_limit }} minutes</span>
            </div>
          </div>
        </div>
        
        <div class="header-actions">
          <!-- Timer Display -->
          <div v-if="quiz?.time_limit && quizStarted && !quizCompleted" class="timer-display">
            <div class="timer-icon">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                <path d="M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2M16.2,16.2L11,13V7H12.5V12.2L17,14.7L16.2,16.2Z" />
              </svg>
            </div>
            <div class="timer-content">
              <div class="timer-value" :class="{ 'warning': timeRemaining <= 300, 'critical': timeRemaining <= 60 }">
                {{ formatTime(timeRemaining) }}
              </div>
              <div class="timer-label">Time Remaining</div>
            </div>
          </div>
          
          <button @click="goBack" class="back-button">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M20,11V13H8L13.5,18.5L12.08,19.92L4.16,12L12.08,4.08L13.5,5.5L8,11H20Z" />
            </svg>
            Back to Dashboard
          </button>
        </div>
      </div>
    </div>

    <!-- Main Content -->
    <div class="main-wrapper">
      <!-- Loading State -->
      <div v-if="isLoading" class="loading-card">
        <div class="loading-spinner"></div>
        <p>Loading quiz...</p>
      </div>

      <!-- Quiz Instructions (Before Start) -->
      <div v-else-if="!quizStarted && quiz" class="instructions-card">
        <div class="card-header">
          <div class="card-header-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
              <path d="M11,9H13V7H11M12,20C7.59,20 4,16.41 4,12C4,7.59 7.59,4 12,4C16.41,4 20,7.59 20,12C20,16.41 16.41,20 12,20M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2M11,17H13V11H11V17Z" />
            </svg>
          </div>
          <div class="card-header-content">
            <h2>Quiz Instructions</h2>
            <p>Please read the following instructions carefully before starting</p>
          </div>
        </div>

        <div class="instructions-content">
          <div class="quiz-details">
            <div class="detail-item">
              <strong>Total Questions:</strong> {{ quiz.questions?.length || 0 }}
            </div>
            <div class="detail-item">
              <strong>Total Points:</strong> {{ quiz.total_points }}
            </div>
            <div class="detail-item" v-if="quiz.time_limit">
              <strong>Time Limit:</strong> {{ quiz.time_limit }} minutes
            </div>
            <div class="detail-item">
              <strong>Attempts Allowed:</strong> {{ quiz.attempts_allowed }}
            </div>
            <div class="detail-item" v-if="previousAttempts > 0">
              <strong>Previous Attempts:</strong> {{ previousAttempts }}
            </div>
          </div>

          <div class="instructions-list">
            <h3>Important Notes:</h3>
            <ul>
              <li>Read each question carefully before answering</li>
              <li v-if="quiz.time_limit">You have {{ quiz.time_limit }} minutes to complete this quiz</li>
              <li>Your progress will be automatically saved</li>
              <li v-if="quiz.shuffle_questions">Questions may appear in a different order</li>
              <li v-if="quiz.shuffle_choices">Answer choices may be shuffled</li>
              <li>You can review and change your answers before submitting</li>
              <li>Once submitted, you cannot change your answers</li>
            </ul>
          </div>

          <div class="quiz-actions">
            <button 
              @click="startQuiz" 
              class="start-quiz-btn"
              :disabled="!canTakeQuiz"
            >
              <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                <path d="M8,5.14V19.14L19,12.14L8,5.14Z" />
              </svg>
              Start Quiz
            </button>
            
            <p v-if="!canTakeQuiz" class="quiz-unavailable">
              {{ quizUnavailableReason }}
            </p>
          </div>
        </div>
      </div>

      <!-- Quiz Taking Interface -->
      <div v-else-if="quizStarted && !quizCompleted" class="quiz-interface">
        <!-- Progress Bar -->
        <div class="progress-card">
          <div class="progress-header">
            <span class="progress-text">Question {{ currentQuestionIndex + 1 }} of {{ shuffledQuestions.length }}</span>
            <span class="progress-percentage">{{ Math.round(((currentQuestionIndex + 1) / shuffledQuestions.length) * 100) }}%</span>
          </div>
          <div class="progress-bar">
            <div 
              class="progress-fill" 
              :style="{ width: ((currentQuestionIndex + 1) / shuffledQuestions.length) * 100 + '%' }"
            ></div>
          </div>
        </div>

        <!-- Current Question -->
        <div class="question-card">
          <div class="question-header">
            <h3>Question {{ currentQuestionIndex + 1 }}</h3>
            <span class="question-points">{{ currentQuestion.points }} {{ currentQuestion.points === 1 ? 'point' : 'points' }}</span>
          </div>

          <div class="question-content">
            <div class="question-text" v-html="formatQuestionText(currentQuestion.question_text)"></div>

            <!-- Multiple Choice Questions -->
            <div v-if="currentQuestion.question_type === 'multiple-choice'" class="answer-section">
              <div class="choice-list">
                <div 
                  v-for="(choice, index) in currentQuestion.shuffled_choices || currentQuestion.choices" 
                  :key="index"
                  class="choice-item"
                  @click="selectChoice(index)"
                >
                  <input 
                    type="radio" 
                    :name="'question-' + currentQuestionIndex" 
                    :value="index"
                    v-model="studentAnswers[currentQuestionIndex]"
                    :id="'choice-' + currentQuestionIndex + '-' + index"
                  />
                  <label :for="'choice-' + currentQuestionIndex + '-' + index" class="choice-label">
                    <span class="choice-letter">{{ String.fromCharCode(65 + index) }}</span>
                    <span class="choice-text">{{ choice }}</span>
                  </label>
                </div>
              </div>
            </div>

            <!-- True/False Questions -->
            <div v-else-if="currentQuestion.question_type === 'true-false'" class="answer-section">
              <div class="tf-choices">
                <div class="tf-choice" @click="selectTrueFalse(true)">
                  <input 
                    type="radio" 
                    :name="'question-' + currentQuestionIndex" 
                    value="true"
                    v-model="studentAnswers[currentQuestionIndex]"
                    id="true-option"
                  />
                  <label for="true-option" class="tf-label">
                    <div class="tf-icon true-icon">
                      <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                        <path d="M21,7L9,19L3.5,13.5L4.91,12.09L9,16.17L19.59,5.59L21,7Z" />
                      </svg>
                    </div>
                    <span>True</span>
                  </label>
                </div>
                
                <div class="tf-choice" @click="selectTrueFalse(false)">
                  <input 
                    type="radio" 
                    :name="'question-' + currentQuestionIndex" 
                    value="false"
                    v-model="studentAnswers[currentQuestionIndex]"
                    id="false-option"
                  />
                  <label for="false-option" class="tf-label">
                    <div class="tf-icon false-icon">
                      <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                        <path d="M19,6.41L17.59,5L12,10.59L6.41,5L5,6.41L10.59,12L5,17.59L6.41,19L12,13.41L17.59,19L19,17.59L13.41,12L19,6.41Z" />
                      </svg>
                    </div>
                    <span>False</span>
                  </label>
                </div>
              </div>
            </div>

            <!-- Fill in the Blanks Questions -->
            <div v-else-if="currentQuestion.question_type === 'fill-in-blanks'" class="answer-section">
              <div class="blanks-container">
                <div 
                  v-for="blankIndex in (currentQuestion.blank_count || 0)" 
                  :key="blankIndex"
                  class="blank-input-group"
                >
                  <label :for="'blank-' + blankIndex" class="blank-label">Blank {{ blankIndex }}:</label>
                  <input 
                    type="text" 
                    :id="'blank-' + blankIndex"
                    :value="getBlankValue(blankIndex - 1)"
                    @input="updateBlankAnswer(blankIndex - 1, ($event.target as HTMLInputElement).value)"
                    class="blank-input"
                    :placeholder="'Enter answer for blank ' + blankIndex"
                  />
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Navigation Controls -->
        <div class="navigation-card">
          <div class="nav-controls">
            <button 
              @click="previousQuestion" 
              class="nav-btn prev-btn"
              :disabled="currentQuestionIndex === 0"
            >
              <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                <path d="M15.41,16.58L10.83,12L15.41,7.41L14,6L8,12L14,18L15.41,16.58Z" />
              </svg>
              Previous
            </button>

            <div class="question-navigation">
              <div class="question-numbers">
                <button 
                  v-for="(question, index) in shuffledQuestions" 
                  :key="index"
                  @click="goToQuestion(index)"
                  :class="[
                    'question-number',
                    { 
                      'current': index === currentQuestionIndex,
                      'answered': isQuestionAnswered(index),
                      'unanswered': !isQuestionAnswered(index)
                    }
                  ]"
                >
                  {{ index + 1 }}
                </button>
              </div>
            </div>

            <button 
              v-if="currentQuestionIndex < shuffledQuestions.length - 1"
              @click="nextQuestion" 
              class="nav-btn next-btn"
            >
              Next
              <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                <path d="M8.59,16.58L13.17,12L8.59,7.41L10,6L16,12L10,18L8.59,16.58Z" />
              </svg>
            </button>

            <button 
              v-else
              @click="showSubmitConfirmation = true" 
              class="submit-quiz-btn"
              :disabled="isSubmitting"
            >
              <svg v-if="isSubmitting" width="20" height="20" viewBox="0 0 24 24" fill="currentColor" class="spinner">
                <path d="M12,4V2A10,10 0 0,0 2,12H4A8,8 0 0,1 12,4Z" />
              </svg>
              <svg v-else width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                <path d="M9,16.17L4.83,12L3.41,13.41L9,19L21,7L19.59,5.59L9,16.17Z" />
              </svg>
              {{ isSubmitting ? 'Submitting...' : 'Submit Quiz' }}
            </button>
          </div>
        </div>
      </div>

      <!-- Quiz Results -->
      <div v-else-if="quizCompleted && quizResult" class="results-card">
        <div class="results-header">
          <div class="results-icon">
            <svg width="48" height="48" viewBox="0 0 24 24" fill="currentColor">
              <path d="M21,7L9,19L3.5,13.5L4.91,12.09L9,16.17L19.59,5.59L21,7Z" />
            </svg>
          </div>
          <h2>Quiz Completed!</h2>
          <p>Your results have been submitted successfully</p>
        </div>

        <div class="results-content">
          <div class="score-display">
            <div class="score-circle">
              <div class="score-value">{{ quizResult.score }}%</div>
              <div class="score-fraction">{{ quizResult.points_earned }}/{{ quiz.total_points }}</div>
            </div>
          </div>

          <div class="results-details">
            <div class="detail-row">
              <span class="detail-label">Questions Answered:</span>
              <span class="detail-value">{{ quizResult.questions_answered }}/{{ shuffledQuestions.length }}</span>
            </div>
            <div class="detail-row">
              <span class="detail-label">Correct Answers:</span>
              <span class="detail-value">{{ quizResult.correct_answers }}</span>
            </div>
            <div class="detail-row">
              <span class="detail-label">Time Taken:</span>
              <span class="detail-value">{{ formatTime(quizResult.time_taken) }}</span>
            </div>
            <div class="detail-row">
              <span class="detail-label">Attempt:</span>
              <span class="detail-value">{{ previousAttempts + 1 }}/{{ quiz.attempts_allowed }}</span>
            </div>
          </div>

          <div class="results-actions">
            <button @click="goBack" class="back-to-dashboard-btn">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                <path d="M10,20V14H14V20H19V12H22L12,3L2,12H5V20H10Z" />
              </svg>
              Back to Dashboard
            </button>
            
            <button 
              v-if="canRetakeQuiz" 
              @click="retakeQuiz" 
              class="retake-btn"
            >
              <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                <path d="M17.65,6.35C16.2,4.9 14.21,4 12,4A8,8 0 0,0 4,12A8,8 0 0,0 12,20C15.73,20 18.84,17.45 19.73,14H17.65C16.83,16.33 14.61,18 12,18A6,6 0 0,1 6,12A6,6 0 0,1 12,6C13.66,6 15.14,6.69 16.22,7.78L13,11H20V4L17.65,6.35Z" />
              </svg>
              Retake Quiz
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Submit Confirmation Modal -->
    <div v-if="showSubmitConfirmation" class="modal-overlay" @click.self="showSubmitConfirmation = false">
      <div class="modal-content">
        <div class="modal-header">
          <h3>Submit Quiz?</h3>
          <button @click="showSubmitConfirmation = false" class="close-btn">&times;</button>
        </div>
        
        <div class="modal-body">
          <p>Are you sure you want to submit your quiz?</p>
          
          <div class="submission-summary">
            <div class="summary-item">
              <span class="summary-label">Questions Answered:</span>
              <span class="summary-value">{{ answeredQuestionsCount }}/{{ shuffledQuestions.length }}</span>
            </div>
            <div class="summary-item" v-if="unansweredQuestionsCount > 0">
              <span class="summary-label">Unanswered Questions:</span>
              <span class="summary-value warning">{{ unansweredQuestionsCount }}</span>
            </div>
          </div>
          
          <p v-if="unansweredQuestionsCount > 0" class="warning-text">
            You have {{ unansweredQuestionsCount }} unanswered question(s). These will be marked as incorrect.
          </p>
          
          <p class="info-text">
            Once submitted, you cannot change your answers.
          </p>
        </div>
        
        <div class="modal-actions">
          <button @click="showSubmitConfirmation = false" class="cancel-btn">
            Cancel
          </button>
          <button @click="submitQuiz" class="confirm-submit-btn" :disabled="isSubmitting">
            <svg v-if="isSubmitting" width="20" height="20" viewBox="0 0 24 24" fill="currentColor" class="spinner">
              <path d="M12,4V2A10,10 0 0,0 2,12H4A8,8 0 0,1 12,4Z" />
            </svg>
            {{ isSubmitting ? 'Submitting...' : 'Submit Quiz' }}
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted, onUnmounted, nextTick } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { supabase } from '../../supabase'
import { useDarkMode } from '../../composables/useDarkMode'

const router = useRouter()
const route = useRoute()
const { isDarkMode, initDarkMode } = useDarkMode()

// Props from route
const quizId = ref(route.params.quizId as string)

// State management
const isLoading = ref(true)
const quiz = ref<any>(null)
const quizStarted = ref(false)
const quizCompleted = ref(false)
const currentQuestionIndex = ref(0)
const shuffledQuestions = ref<any[]>([])
const studentAnswers = ref<any[]>([])
const timeRemaining = ref(0)
const timer = ref<NodeJS.Timeout | null>(null)
const previousAttempts = ref(0)
const currentAttemptId = ref<string | null>(null)
const startTime = ref<Date | null>(null)
const isSubmitting = ref(false)
const showSubmitConfirmation = ref(false)
const quizResult = ref<any>(null)
const currentStudentId = ref<string | null>(null)

// Computed properties
const currentQuestion = computed(() => {
  return shuffledQuestions.value[currentQuestionIndex.value] || {}
})

const canTakeQuiz = computed(() => {
  if (!quiz.value) return false
  
  // Check if attempts exceeded
  if (previousAttempts.value >= quiz.value.attempts_allowed) {
    return false
  }
  
  // Check if quiz is within date range
  const now = new Date()
  if (quiz.value.start_date && new Date(quiz.value.start_date) > now) {
    return false
  }
  if (quiz.value.end_date && new Date(quiz.value.end_date) < now) {
    return false
  }
  
  return true
})

const quizUnavailableReason = computed(() => {
  if (!quiz.value) return 'Quiz not found'
  
  if (previousAttempts.value >= quiz.value.attempts_allowed) {
    return `You have used all ${quiz.value.attempts_allowed} allowed attempts`
  }
  
  const now = new Date()
  if (quiz.value.start_date && new Date(quiz.value.start_date) > now) {
    return `Quiz starts on ${new Date(quiz.value.start_date).toLocaleDateString()}`
  }
  if (quiz.value.end_date && new Date(quiz.value.end_date) < now) {
    return `Quiz ended on ${new Date(quiz.value.end_date).toLocaleDateString()}`
  }
  
  return 'Quiz is not available'
})

const answeredQuestionsCount = computed(() => {
  return studentAnswers.value.filter(answer => {
    if (Array.isArray(answer)) {
      return answer.some(a => a !== null && a !== undefined && a !== '')
    }
    return answer !== null && answer !== undefined && answer !== ''
  }).length
})

const unansweredQuestionsCount = computed(() => {
  return shuffledQuestions.value.length - answeredQuestionsCount.value
})

const canRetakeQuiz = computed(() => {
  return quiz.value && previousAttempts.value < quiz.value.attempts_allowed
})

// Authentication
const getCurrentUser = async () => {
  try {
    const { data: { user }, error: authError } = await supabase.auth.getUser()
    if (authError) throw authError
    
    if (!user) return null
    
    const { data: profile, error: profileError } = await supabase
      .from('profiles')
      .select('id, auth_user_id, role')
      .eq('auth_user_id', user.id)
      .single()
    
    if (profileError) throw profileError
    
    if (profile.role !== 'student') return null
    
    const { data: studentData, error: studentError } = await supabase
      .from('students')
      .select('id')
      .eq('profile_id', profile.id)
      .single()
    
    if (studentError) throw studentError
    
    currentStudentId.value = studentData.id
    return studentData.id
    
  } catch (error) {
    console.error('Error getting current user:', error)
    return null
  }
}

// Quiz loading
const loadQuiz = async () => {
  try {
    console.log('Loading quiz:', quizId.value)
    
    // Load quiz details with subject and section info
    const { data: quizData, error: quizError } = await supabase
      .from('quizzes')
      .select(`
        *,
        sections!inner(
          id,
          name,
          subjects!inner(
            id,
            name
          )
        )
      `)
      .eq('id', quizId.value)
      .single()
    
    if (quizError) throw quizError
    
    if (!quizData) {
      alert('Quiz not found')
      router.push('/student')
      return
    }
    
    // Check if student is enrolled in this section
    const { data: enrollment, error: enrollmentError } = await supabase
      .from('enrollments')
      .select('id')
      .eq('student_id', currentStudentId.value)
      .eq('section_id', quizData.section_id)
      .eq('status', 'active')
      .single()
    
    if (enrollmentError || !enrollment) {
      alert('You are not enrolled in this course')
      router.push('/student')
      return
    }
    
    // Load quiz questions
    const { data: questions, error: questionsError } = await supabase
      .from('quiz_questions')
      .select('*')
      .eq('quiz_id', quizId.value)
      .order('question_number')
    
    if (questionsError) throw questionsError
    
    // Process questions and prepare for display
    const processedQuestions = questions.map(q => {
      let processedQuestion = {
        ...q,
        blank_count: 0,
        shuffled_choices: null
      }
      
      // Handle fill-in-blanks questions
      if (q.question_type === 'fill-in-blanks') {
        const blankCount = (q.question_text.match(/____/g) || []).length
        processedQuestion.blank_count = blankCount
      }
      
      // Shuffle choices if enabled
      if (q.question_type === 'multiple-choice' && quizData.shuffle_choices && q.choices) {
        const shuffled = [...q.choices].sort(() => Math.random() - 0.5)
        processedQuestion.shuffled_choices = shuffled
        
        // Update correct answer index based on shuffled order
        const originalCorrectChoice = q.choices[parseInt(q.correct_answer)]
        processedQuestion.correct_answer = shuffled.indexOf(originalCorrectChoice).toString()
      }
      
      return processedQuestion
    })
    
    // Set quiz data
    quiz.value = {
      ...quizData,
      subject_name: quizData.sections?.subjects?.name || 'Unknown Subject',
      section_name: quizData.sections?.name || 'Unknown Section',
      questions: processedQuestions
    }
    
    // Shuffle questions if enabled
    if (quizData.shuffle_questions) {
      shuffledQuestions.value = [...processedQuestions].sort(() => Math.random() - 0.5)
    } else {
      shuffledQuestions.value = processedQuestions
    }
    
    // Initialize student answers array
    studentAnswers.value = shuffledQuestions.value.map(q => {
      if (q.question_type === 'fill-in-blanks') {
        return Array(q.blank_count).fill('')
      }
      return null
    })
    
    // Load previous attempts
    await loadPreviousAttempts()
    
    console.log('Quiz loaded successfully:', quiz.value)
    
  } catch (error) {
    console.error('Error loading quiz:', error)
    alert('Error loading quiz. Please try again.')
    router.push('/student')
  } finally {
    isLoading.value = false
  }
}

const loadPreviousAttempts = async () => {
  try {
    const { count } = await supabase
      .from('quiz_attempts')
      .select('*', { count: 'exact', head: true })
      .eq('quiz_id', quizId.value)
      .eq('student_id', currentStudentId.value)
    
    previousAttempts.value = count || 0
    
  } catch (error) {
    console.error('Error loading previous attempts:', error)
  }
}

// Quiz control functions
const startQuiz = async () => {
  if (!canTakeQuiz.value) return
  
  try {
    // Create new quiz attempt
    const { data: attempt, error } = await supabase
      .from('quiz_attempts')
      .insert({
        quiz_id: quizId.value,
        student_id: currentStudentId.value,
        attempt_number: previousAttempts.value + 1,
        started_at: new Date().toISOString(),
        status: 'in_progress'
      })
      .select()
      .single()
    
    if (error) throw error
    
    currentAttemptId.value = attempt.id
    startTime.value = new Date()
    quizStarted.value = true
    
    // Start timer if time limit exists
    if (quiz.value.time_limit) {
      timeRemaining.value = quiz.value.time_limit * 60 // Convert to seconds
      startTimer()
    }
    
    console.log('Quiz started, attempt ID:', currentAttemptId.value)
    
  } catch (error) {
    console.error('Error starting quiz:', error)
    alert('Error starting quiz. Please try again.')
  }
}

const startTimer = () => {
  timer.value = setInterval(() => {
    timeRemaining.value--
    
    if (timeRemaining.value <= 0) {
      // Auto-submit when time runs out
      submitQuiz(true)
    }
  }, 1000)
}

const stopTimer = () => {
  if (timer.value) {
    clearInterval(timer.value)
    timer.value = null
  }
}

// Navigation functions
const nextQuestion = () => {
  if (currentQuestionIndex.value < shuffledQuestions.value.length - 1) {
    currentQuestionIndex.value++
  }
}

const previousQuestion = () => {
  if (currentQuestionIndex.value > 0) {
    currentQuestionIndex.value--
  }
}

const goToQuestion = (index: number) => {
  currentQuestionIndex.value = index
}

const isQuestionAnswered = (index: number) => {
  const answer = studentAnswers.value[index]
  if (Array.isArray(answer)) {
    return answer.some(a => a !== null && a !== undefined && a !== '')
  }
  return answer !== null && answer !== undefined && answer !== ''
}

// Answer selection functions
const selectChoice = (choiceIndex: number) => {
  if (studentAnswers.value[currentQuestionIndex.value] !== undefined) {
    studentAnswers.value[currentQuestionIndex.value] = choiceIndex
  }
}

const selectTrueFalse = (value: boolean) => {
  if (studentAnswers.value[currentQuestionIndex.value] !== undefined) {
    studentAnswers.value[currentQuestionIndex.value] = value.toString()
  }
}

// Helper functions for fill-in-blanks
const getBlankValue = (blankIndex: number) => {
  const currentAnswer = studentAnswers.value[currentQuestionIndex.value]
  if (Array.isArray(currentAnswer) && currentAnswer[blankIndex] !== undefined) {
    return currentAnswer[blankIndex]
  }
  return ''
}

const updateBlankAnswer = (blankIndex: number, value: string) => {
  const currentAnswer = studentAnswers.value[currentQuestionIndex.value]
  if (Array.isArray(currentAnswer)) {
    currentAnswer[blankIndex] = value
  }
}

// Quiz submission
const submitQuiz = async (autoSubmit = false) => {
  if (isSubmitting.value) return
  
  isSubmitting.value = true
  showSubmitConfirmation.value = false
  
  try {
    stopTimer()
    
    const endTime = new Date()
    const timeTaken = startTime.value ? 
      Math.round((endTime.getTime() - startTime.value.getTime()) / 1000) : 0
    
    // Prepare answers for grading
    const answers = shuffledQuestions.value.map((question, index) => {
      const studentAnswer = studentAnswers.value[index]
      
      return {
        quiz_attempt_id: currentAttemptId.value,
        question_id: question.id,
        student_answer: Array.isArray(studentAnswer) ? 
          JSON.stringify(studentAnswer) : 
          String(studentAnswer || ''),
        is_correct: false, // Will be determined by grading
        points_earned: 0   // Will be determined by grading
      }
    })
    
    // Insert quiz answers
    const { error: answersError } = await supabase
      .from('quiz_answers')
      .insert(answers)
    
    if (answersError) throw answersError
    
    // Grade the quiz
    const gradingResult = await gradeQuiz(shuffledQuestions.value, studentAnswers.value)
    
    // Update quiz attempt with results
    const { error: updateError } = await supabase
      .from('quiz_attempts')
      .update({
        completed_at: endTime.toISOString(),
        time_taken: timeTaken,
        score: gradingResult.score,
        points_earned: gradingResult.pointsEarned,
        total_questions: shuffledQuestions.value.length,
        correct_answers: gradingResult.correctAnswers,
        status: 'completed',
        auto_submitted: autoSubmit
      })
      .eq('id', currentAttemptId.value)
    
    if (updateError) throw updateError
    
    // Update individual answer records with grading results
    for (let i = 0; i < gradingResult.questionResults.length; i++) {
      const result = gradingResult.questionResults[i]
      const questionId = shuffledQuestions.value[i].id
      
      await supabase
        .from('quiz_answers')
        .update({
          is_correct: result.isCorrect,
          points_earned: result.pointsEarned
        })
        .eq('quiz_attempt_id', currentAttemptId.value)
        .eq('question_id', questionId)
    }
    
    // Set results and mark as completed
    quizResult.value = {
      score: gradingResult.score,
      points_earned: gradingResult.pointsEarned,
      correct_answers: gradingResult.correctAnswers,
      questions_answered: answeredQuestionsCount.value,
      time_taken: timeTaken
    }
    
    quizCompleted.value = true
    
    console.log('Quiz submitted successfully:', quizResult.value)
    
  } catch (error) {
    console.error('Error submitting quiz:', error)
    alert('Error submitting quiz. Please try again.')
  } finally {
    isSubmitting.value = false
  }
}

// Auto-grading function
const gradeQuiz = async (questions: any[], answers: any[]) => {
  let correctAnswers = 0
  let pointsEarned = 0
  const questionResults: any[] = []
  
  for (let i = 0; i < questions.length; i++) {
    const question = questions[i]
    const studentAnswer = answers[i]
    let isCorrect = false
    let earnedPoints = 0
    
    if (question.question_type === 'multiple-choice') {
      const correctIndex = parseInt(question.correct_answer)
      isCorrect = studentAnswer === correctIndex
      
    } else if (question.question_type === 'true-false') {
      isCorrect = studentAnswer === question.correct_answer
      
    } else if (question.question_type === 'fill-in-blanks') {
      const correctAnswers = JSON.parse(question.correct_answer)
      if (Array.isArray(studentAnswer) && Array.isArray(correctAnswers)) {
        // Check each blank
        let correctBlanks = 0
        for (let j = 0; j < correctAnswers.length; j++) {
          if (studentAnswer[j] && 
              studentAnswer[j].toLowerCase().trim() === 
              correctAnswers[j].toLowerCase().trim()) {
            correctBlanks++
          }
        }
        // Partial credit for fill-in-blanks
        const blankPercentage = correctBlanks / correctAnswers.length
        isCorrect = blankPercentage >= 0.5 // 50% threshold
        earnedPoints = Math.round(question.points * blankPercentage)
      }
    }
    
    if (isCorrect && question.question_type !== 'fill-in-blanks') {
      earnedPoints = question.points
      correctAnswers++
    } else if (question.question_type === 'fill-in-blanks' && earnedPoints > 0) {
      correctAnswers++ // Count as correct if partial credit earned
    }
    
    pointsEarned += earnedPoints
    
    questionResults.push({
      isCorrect,
      pointsEarned: earnedPoints
    })
  }
  
  const score = Math.round((pointsEarned / quiz.value.total_points) * 100)
  
  return {
    score,
    pointsEarned,
    correctAnswers,
    questionResults
  }
}

// Utility functions
const formatTime = (seconds: number) => {
  if (seconds < 0) seconds = 0
  
  const hours = Math.floor(seconds / 3600)
  const minutes = Math.floor((seconds % 3600) / 60)
  const secs = seconds % 60
  
  if (hours > 0) {
    return `${hours}:${minutes.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`
  }
  return `${minutes}:${secs.toString().padStart(2, '0')}`
}

const formatQuestionText = (text: string) => {
  if (!text) return ''
  
  // Replace ____ with input fields for fill-in-blanks
  return text.replace(/____/g, '<span class="blank-placeholder">_____</span>')
}

const retakeQuiz = () => {
  // Reset quiz state
  quizStarted.value = false
  quizCompleted.value = false
  currentQuestionIndex.value = 0
  quizResult.value = null
  currentAttemptId.value = null
  
  // Re-initialize answers
  studentAnswers.value = shuffledQuestions.value.map(q => {
    if (q.question_type === 'fill-in-blanks') {
      return Array(q.blank_count).fill('')
    }
    return null
  })
  
  // Reload attempts count
  loadPreviousAttempts()
}

const goBack = async () => {
  // Stop timer if running
  stopTimer()
  
  // If quiz is in progress, warn user
  if (quizStarted.value && !quizCompleted.value) {
    const confirmLeave = confirm(
      'Are you sure you want to leave? Your progress will be lost.'
    )
    if (!confirmLeave) return
  }
  
  await router.push('/student')
}

onUnmounted(() => {
  stopTimer()
})

// Handle page refresh/close during quiz - inside onMounted
onMounted(async () => {
  initDarkMode()
  
  const studentId = await getCurrentUser()
  if (!studentId) {
    alert('Please log in to take this quiz')
    router.push('/login')
    return
  }
  
  await loadQuiz()
  
  // Add beforeunload listener
  const handleBeforeUnload = (e: BeforeUnloadEvent) => {
    if (quizStarted.value && !quizCompleted.value) {
      e.preventDefault()
      e.returnValue = 'You have an active quiz. Are you sure you want to leave?'
    }
  }
  
  window.addEventListener('beforeunload', handleBeforeUnload)
  
  // Clean up on unmount
  onUnmounted(() => {
    window.removeEventListener('beforeunload', handleBeforeUnload)
  })
})
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

/* Base Styling */
.take-quiz-page {
  padding: 2rem;
  max-width: 1200px;
  margin: 0 auto;
  font-family: 'Inter', sans-serif;
  background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
  min-height: 100vh;
  color: #1e293b;
  transition: all 0.3s ease;
}

/* CSS Variables */
:root {
  --primary-color: #10b981;
  --primary-color-light: #34d399;
  --primary-color-dark: #059669;
  --accent-color: #6366f1;
  --accent-light: #8b5cf6;
  --success-color: #22c55e;
  --warning-color: #f59e0b;
  --error-color: #ef4444;
  --bg-primary: #f8fafc;
  --bg-secondary: #f1f5f9;
  --card-background: rgba(255, 255, 255, 0.95);
  --border-color: #e2e8f0;
  --text-primary: #1e293b;
  --text-secondary: #64748b;
  --shadow-light: rgba(0, 0, 0, 0.05);
  --shadow-medium: rgba(0, 0, 0, 0.1);
  --shadow-strong: rgba(0, 0, 0, 0.15);
}

/* Quiz Header */
.quiz-header-card {
  position: relative;
  background: linear-gradient(135deg, var(--accent-color) 0%, var(--accent-light) 100%);
  border-radius: 24px;
  padding: 2rem;
  color: white;
  margin-bottom: 2rem;
  overflow: hidden;
  box-shadow: 0 10px 40px rgba(99, 102, 241, 0.3);
}

.header-bg-decoration {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 24px;
  z-index: 1;
}

.floating-shapes {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
  z-index: 1;
}

.shape {
  position: absolute;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 50%;
  animation: float 6s ease-in-out infinite;
}

.shape-1 {
  width: 80px;
  height: 80px;
  top: -20px;
  right: 10%;
  animation-delay: 0s;
}

.shape-2 {
  width: 60px;
  height: 60px;
  top: 50%;
  right: 5%;
  animation-delay: 2s;
}

.shape-3 {
  width: 100px;
  height: 100px;
  bottom: -30px;
  left: 15%;
  animation-delay: 4s;
}

@keyframes float {
  0%, 100% { transform: translateY(0px) rotate(0deg); }
  50% { transform: translateY(-20px) rotate(180deg); }
}

.quiz-header-content {
  position: relative;
  z-index: 2;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.quiz-header-left {
  display: flex;
  align-items: center;
  gap: 1.5rem;
}

.quiz-header-icon {
  width: 48px;
  height: 48px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.header-text {
  flex: 1;
}

.quiz-header-title {
  font-size: 1.75rem;
  font-weight: 700;
  margin: 0 0 0.5rem 0;
}

.quiz-header-subtitle {
  font-size: 1.1rem;
  font-weight: 500;
  margin: 0 0 0.25rem 0;
  opacity: 0.9;
}

.quiz-header-description {
  font-size: 0.95rem;
  font-weight: 400;
  margin: 0;
  opacity: 0.8;
}

.header-actions {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.timer-display {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  background: rgba(255, 255, 255, 0.15);
  border-radius: 12px;
  padding: 0.75rem 1rem;
  backdrop-filter: blur(10px);
}

.timer-content {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}

.timer-value {
  font-size: 1.1rem;
  font-weight: 600;
  line-height: 1;
}

.timer-value.warning {
  color: #fbbf24;
}

.timer-value.critical {
  color: #f87171;
  animation: pulse 1s infinite;
}

@keyframes pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.5; }
}

.timer-label {
  font-size: 0.8rem;
  opacity: 0.8;
  margin: 0;
}

.back-button {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  background: rgba(255, 255, 255, 0.15);
  border: none;
  border-radius: 12px;
  padding: 0.75rem 1rem;
  color: white;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s ease;
  backdrop-filter: blur(10px);
}

.back-button:hover {
  background: rgba(255, 255, 255, 0.25);
  transform: translateY(-1px);
}

/* Main Content */
.main-wrapper {
  position: relative;
  z-index: 2;
}

/* Loading State */
.loading-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background: var(--card-background);
  border-radius: 20px;
  padding: 4rem 2rem;
  text-align: center;
  box-shadow: 0 8px 32px var(--shadow-light);
}

.loading-spinner {
  width: 48px;
  height: 48px;
  border: 4px solid var(--border-color);
  border-top: 4px solid var(--accent-color);
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin-bottom: 1rem;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

/* Instructions Card */
.instructions-card {
  background: var(--card-background);
  border-radius: 20px;
  padding: 2rem;
  margin-bottom: 2rem;
  box-shadow: 0 8px 32px var(--shadow-light);
  border: 1px solid var(--border-color);
}

.card-header {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 1.5rem;
  padding-bottom: 1rem;
  border-bottom: 1px solid var(--border-color);
}

.card-header-icon {
  color: var(--accent-color);
}

.card-header-content h2 {
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--text-primary);
  margin: 0;
}

.card-header-content p {
  font-size: 0.95rem;
  color: var(--text-secondary);
  margin: 0.25rem 0 0 0;
}

.instructions-content {
  color: var(--text-primary);
}

.quiz-details {
  background: rgba(99, 102, 241, 0.05);
  border-radius: 12px;
  padding: 1.5rem;
  margin-bottom: 1.5rem;
  border-left: 4px solid var(--accent-color);
}

.detail-item {
  margin-bottom: 0.75rem;
  font-size: 0.95rem;
}

.detail-item:last-child {
  margin-bottom: 0;
}

.detail-item strong {
  color: var(--accent-color);
  font-weight: 600;
}

.instructions-list h3 {
  color: var(--text-primary);
  font-size: 1.1rem;
  font-weight: 600;
  margin: 0 0 1rem 0;
}

.instructions-list ul {
  padding-left: 1.5rem;
  margin: 0;
}

.instructions-list li {
  margin-bottom: 0.5rem;
  color: var(--text-secondary);
  line-height: 1.5;
}

.quiz-actions {
  margin-top: 2rem;
  text-align: center;
}

.start-quiz-btn {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  background: linear-gradient(135deg, var(--primary-color) 0%, var(--primary-color-light) 100%);
  color: white;
  border: none;
  border-radius: 16px;
  padding: 1rem 2rem;
  font-size: 1.1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 8px 24px rgba(16, 185, 129, 0.3);
}

.start-quiz-btn:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 12px 32px rgba(16, 185, 129, 0.4);
}

.start-quiz-btn:disabled {
  opacity: 0.6;
  cursor: not-allowed;
  transform: none;
}

.quiz-unavailable {
  margin-top: 1rem;
  color: var(--error-color);
  font-weight: 500;
  font-size: 0.95rem;
}

/* Quiz Interface */
.quiz-interface {
  background: var(--card-background);
  border-radius: 20px;
  padding: 2rem;
  box-shadow: 0 8px 32px var(--shadow-light);
  border: 1px solid var(--border-color);
}

/* Progress Card */
.progress-card {
  background: linear-gradient(135deg, rgba(99, 102, 241, 0.1) 0%, rgba(139, 92, 246, 0.1) 100%);
  border-radius: 16px;
  padding: 1.5rem;
  margin-bottom: 2rem;
  border: 1px solid rgba(99, 102, 241, 0.2);
}

.progress-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
}

.progress-text, .progress-percentage {
  font-size: 0.95rem;
  font-weight: 600;
  color: var(--accent-color);
}

.progress-bar {
  background: rgba(99, 102, 241, 0.2);
  border-radius: 8px;
  height: 8px;
  overflow: hidden;
}

.progress-fill {
  background: linear-gradient(135deg, var(--accent-color) 0%, var(--accent-light) 100%);
  height: 100%;
  transition: width 0.3s ease;
}

/* Question Card */
.question-card {
  margin-bottom: 2rem;
}

.question-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1.5rem;
  padding-bottom: 1rem;
  border-bottom: 2px solid var(--border-color);
}

.question-header h3 {
  font-size: 1.3rem;
  font-weight: 700;
  color: var(--text-primary);
  margin: 0;
}

.question-points {
  background: var(--accent-color);
  color: white;
  padding: 0.5rem 1rem;
  border-radius: 12px;
  font-size: 0.9rem;
  font-weight: 600;
}

.question-content {
  color: var(--text-primary);
}

.question-text {
  font-size: 1.1rem;
  line-height: 1.6;
  margin-bottom: 2rem;
  color: var(--text-primary);
}

.blank-placeholder {
  display: inline-block;
  min-width: 100px;
  padding: 0.25rem 0.5rem;
  background: rgba(99, 102, 241, 0.1);
  border-bottom: 2px solid var(--accent-color);
  color: var(--accent-color);
  font-weight: 600;
  margin: 0 0.25rem;
}

/* Answer Sections */
.answer-section {
  margin-top: 1.5rem;
}

/* Multiple Choice */
.choice-list {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.choice-item {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1rem 1.5rem;
  background: rgba(248, 250, 252, 0.8);
  border: 2px solid var(--border-color);
  border-radius: 16px;
  cursor: pointer;
  transition: all 0.2s ease;
}

.choice-item:hover {
  background: rgba(99, 102, 241, 0.05);
  border-color: var(--accent-color);
  transform: translateY(-1px);
}

.choice-item input[type="radio"]:checked + .choice-label {
  color: var(--accent-color);
  font-weight: 600;
}

.choice-item:has(input[type="radio"]:checked) {
  background: rgba(99, 102, 241, 0.1);
  border-color: var(--accent-color);
}

.choice-label {
  display: flex;
  align-items: center;
  gap: 1rem;
  cursor: pointer;
  flex: 1;
}

.choice-letter {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 32px;
  height: 32px;
  background: var(--accent-color);
  color: white;
  border-radius: 50%;
  font-weight: 600;
  font-size: 0.9rem;
}

.choice-text {
  font-size: 1rem;
  line-height: 1.4;
}

/* True/False */
.tf-choices {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
}

.tf-choice {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 1rem;
  padding: 1.5rem;
  background: rgba(248, 250, 252, 0.8);
  border: 2px solid var(--border-color);
  border-radius: 16px;
  cursor: pointer;
  transition: all 0.2s ease;
}

.tf-choice:hover {
  background: rgba(99, 102, 241, 0.05);
  border-color: var(--accent-color);
  transform: translateY(-1px);
}

.tf-choice:has(input[type="radio"]:checked) {
  background: rgba(99, 102, 241, 0.1);
  border-color: var(--accent-color);
}

.tf-label {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  cursor: pointer;
  font-size: 1.1rem;
  font-weight: 600;
}

.tf-icon {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.true-icon {
  background: var(--success-color);
  color: white;
}

.false-icon {
  background: var(--error-color);
  color: white;
}

/* Fill in Blanks */
.blanks-container {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.blank-input-group {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.blank-label {
  font-weight: 600;
  color: var(--text-primary);
  min-width: 100px;
}

.blank-input {
  flex: 1;
  padding: 0.75rem 1rem;
  border: 2px solid var(--border-color);
  border-radius: 12px;
  font-size: 1rem;
  transition: all 0.2s ease;
}

.blank-input:focus {
  outline: none;
  border-color: var(--accent-color);
  box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.1);
}

/* Navigation */
.navigation-card {
  background: rgba(248, 250, 252, 0.8);
  border-radius: 16px;
  padding: 1.5rem;
  border: 1px solid var(--border-color);
}

.nav-controls {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 1rem;
}

.nav-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  background: rgba(100, 116, 139, 0.1);
  border: 1px solid rgba(100, 116, 139, 0.2);
  color: var(--text-secondary);
  border-radius: 12px;
  padding: 0.75rem 1.25rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
}

.nav-btn:hover:not(:disabled) {
  background: rgba(100, 116, 139, 0.2);
  color: var(--text-primary);
  transform: translateY(-1px);
}

.nav-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.submit-quiz-btn {
  background: linear-gradient(135deg, var(--primary-color) 0%, var(--primary-color-light) 100%);
  border: none;
  color: white;
  box-shadow: 0 4px 12px rgba(16, 185, 129, 0.3);
}

.submit-quiz-btn:hover:not(:disabled) {
  background: linear-gradient(135deg, var(--primary-color-dark) 0%, var(--primary-color) 100%);
  box-shadow: 0 6px 16px rgba(16, 185, 129, 0.4);
}

.question-navigation {
  flex: 1;
  display: flex;
  justify-content: center;
}

.question-numbers {
  display: flex;
  gap: 0.5rem;
  flex-wrap: wrap;
  justify-content: center;
}

.question-number {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 40px;
  height: 40px;
  border: none;
  border-radius: 50%;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
  background: rgba(100, 116, 139, 0.1);
  color: var(--text-secondary);
}

.question-number:hover {
  transform: scale(1.1);
}

.question-number.current {
  background: var(--accent-color);
  color: white;
  box-shadow: 0 4px 12px rgba(99, 102, 241, 0.3);
}

.question-number.answered {
  background: var(--success-color);
  color: white;
}

.question-number.unanswered {
  background: rgba(245, 158, 11, 0.2);
  color: var(--warning-color);
}

/* Results Card */
.results-card {
  background: var(--card-background);
  border-radius: 20px;
  padding: 2rem;
  box-shadow: 0 8px 32px var(--shadow-light);
  border: 1px solid var(--border-color);
  text-align: center;
}

.results-header {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 2rem;
}

.results-icon {
  width: 64px;
  height: 64px;
  background: var(--success-color);
  color: white;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 1rem;
}

.results-header h2 {
  font-size: 1.75rem;
  font-weight: 700;
  color: var(--text-primary);
  margin: 0 0 0.5rem 0;
}

.results-header p {
  color: var(--text-secondary);
  margin: 0;
}

.results-content {
  margin-bottom: 2rem;
}

.score-display {
  margin-bottom: 2rem;
}

.score-circle {
  display: inline-flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 120px;
  height: 120px;
  background: linear-gradient(135deg, var(--accent-color) 0%, var(--accent-light) 100%);
  border-radius: 50%;
  color: white;
  margin: 0 auto;
  position: relative;
}

.score-value {
  font-size: 2rem;
  font-weight: 700;
  line-height: 1;
}

.score-fraction {
  font-size: 0.9rem;
  opacity: 0.9;
  margin-top: 0.25rem;
}

.results-details {
  background: rgba(248, 250, 252, 0.8);
  border-radius: 16px;
  padding: 1.5rem;
  margin-bottom: 2rem;
}

.detail-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 0.75rem;
}

.detail-row:last-child {
  margin-bottom: 0;
}

.detail-label {
  font-weight: 600;
  color: var(--text-secondary);
}

.detail-value {
  font-weight: 600;
  color: var(--text-primary);
}

.results-actions {
  display: flex;
  gap: 1rem;
  justify-content: center;
}

.back-to-dashboard-btn, .retake-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.875rem 1.5rem;
  border-radius: 12px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
  border: none;
}

.back-to-dashboard-btn {
  background: linear-gradient(135deg, var(--accent-color) 0%, var(--accent-light) 100%);
  color: white;
}

.retake-btn {
  background: rgba(34, 197, 94, 0.1);
  color: var(--success-color);
  border: 1px solid rgba(34, 197, 94, 0.2);
}

.back-to-dashboard-btn:hover {
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(99, 102, 241, 0.3);
}

.retake-btn:hover {
  background: rgba(34, 197, 94, 0.2);
  transform: translateY(-1px);
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
  backdrop-filter: blur(4px);
}

.modal-content {
  background: var(--card-background);
  border-radius: 20px;
  padding: 2rem;
  width: 90%;
  max-width: 500px;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
  position: relative;
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1.5rem;
  padding-bottom: 1rem;
  border-bottom: 1px solid var(--border-color);
}

.modal-header h3 {
  font-size: 1.25rem;
  font-weight: 700;
  color: var(--text-primary);
  margin: 0;
}

.close-btn {
  background: none;
  border: none;
  font-size: 1.5rem;
  color: var(--text-secondary);
  cursor: pointer;
  padding: 0;
  width: 32px;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  transition: all 0.2s ease;
}

.close-btn:hover {
  background: rgba(100, 116, 139, 0.1);
  color: var(--text-primary);
}

.modal-body {
  margin-bottom: 2rem;
}

.modal-body p {
  color: var(--text-primary);
  line-height: 1.6;
  margin-bottom: 1rem;
}

.submission-summary {
  background: rgba(248, 250, 252, 0.8);
  border-radius: 12px;
  padding: 1rem;
  margin: 1rem 0;
}

.summary-item {
  display: flex;
  justify-content: space-between;
  margin-bottom: 0.5rem;
}

.summary-item:last-child {
  margin-bottom: 0;
}

.summary-label {
  font-weight: 600;
  color: var(--text-secondary);
}

.summary-value {
  font-weight: 600;
  color: var(--text-primary);
}

.summary-value.warning {
  color: var(--warning-color);
}

.warning-text {
  color: var(--warning-color);
  font-weight: 500;
  background: rgba(245, 158, 11, 0.1);
  padding: 0.75rem;
  border-radius: 8px;
  border-left: 4px solid var(--warning-color);
}

.info-text {
  color: var(--text-secondary);
  font-style: italic;
}

.modal-actions {
  display: flex;
  gap: 1rem;
  justify-content: flex-end;
}

.cancel-btn, .confirm-submit-btn {
  padding: 0.75rem 1.5rem;
  border-radius: 12px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
  border: none;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.cancel-btn {
  background: rgba(100, 116, 139, 0.1);
  color: var(--text-secondary);
  border: 1px solid rgba(100, 116, 139, 0.2);
}

.confirm-submit-btn {
  background: linear-gradient(135deg, var(--primary-color) 0%, var(--primary-color-light) 100%);
  color: white;
}

.cancel-btn:hover {
  background: rgba(100, 116, 139, 0.2);
  color: var(--text-primary);
}

.confirm-submit-btn:hover:not(:disabled) {
  background: linear-gradient(135deg, var(--primary-color-dark) 0%, var(--primary-color) 100%);
  transform: translateY(-1px);
}

.confirm-submit-btn:disabled {
  opacity: 0.7;
  cursor: not-allowed;
}

.spinner {
  animation: spin 1s linear infinite;
}

/* Responsive Design */
@media (max-width: 768px) {
  .take-quiz-page {
    padding: 1rem;
  }
  
  .quiz-header-content {
    flex-direction: column;
    gap: 1rem;
    text-align: center;
  }
  
  .quiz-header-left {
    flex-direction: column;
    gap: 1rem;
  }
  
  .header-actions {
    width: 100%;
    justify-content: center;
  }
  
  .timer-display {
    order: -1;
  }
  
  .instructions-card,
  .quiz-interface,
  .results-card {
    padding: 1.5rem;
  }
  
  .tf-choices {
    grid-template-columns: 1fr;
  }
  
  .nav-controls {
    flex-direction: column;
    gap: 1rem;
  }
  
  .question-navigation {
    order: -1;
  }
  
  .results-actions {
    flex-direction: column;
  }
  
  .modal-content {
    padding: 1.5rem;
    margin: 1rem;
  }
  
  .modal-actions {
    flex-direction: column-reverse;
  }
}

/* Dark Mode */
.dark-mode {
  --bg-primary: #0f172a;
  --bg-secondary: #1e293b;
  --card-background: rgba(30, 41, 59, 0.95);
  --border-color: #334155;
  --text-primary: #f1f5f9;
  --text-secondary: #94a3b8;
  --shadow-light: rgba(0, 0, 0, 0.3);
  --shadow-medium: rgba(0, 0, 0, 0.4);
  --shadow-strong: rgba(0, 0, 0, 0.5);
}

.dark-mode .take-quiz-page {
  background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
}

.dark-mode .choice-item,
.dark-mode .tf-choice,
.dark-mode .progress-card,
.dark-mode .navigation-card,
.dark-mode .results-details,
.dark-mode .submission-summary {
  background: rgba(15, 23, 42, 0.8);
}

.dark-mode .choice-item:hover,
.dark-mode .tf-choice:hover {
  background: rgba(99, 102, 241, 0.1);
}

.dark-mode .blank-input {
  background: rgba(15, 23, 42, 0.8);
  color: var(--text-primary);
}
</style>