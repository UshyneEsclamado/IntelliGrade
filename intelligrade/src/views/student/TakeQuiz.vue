
<template>
  <div class="take-quiz-page">
    <!-- Header Section -->
    <div class="page-header">
      <div class="header-container">
        <div class="header-content">
          <div class="quiz-info">
            <div class="quiz-icon">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                <path d="M14,2H6A2,2 0 0,0 4,4V20A2,2 0 0,0 6,22H18A2,2 0 0,0 20,20V8L14,2M18,20H6V4H13V9H18V20Z" />
              </svg>
            </div>
            <div class="quiz-details">
              <h1>{{ hasAvailableQuizzes ? quiz.title : 'Quiz Center' }}</h1>
              <p>{{ quiz.subject_name }} • {{ quiz.section }}</p>
            </div>
          </div>
          <div class="quiz-status">
            <div v-if="quizStarted && !quizSubmitted && quiz.has_time_limit" class="timer-display">
              <div class="timer-icon" :class="{ 'warning': timeRemaining < 300, 'critical': timeRemaining <= 60 }">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2M16.2,16.2L11,13V7H12.5V12.2L17,14.7L16.2,16.2Z" />
                </svg>
              </div>
              <div class="timer-content">
                <div class="timer-value" :class="{ 'warning': timeRemaining < 300, 'critical': timeRemaining <= 60 }">
                  {{ formatTime(timeRemaining) }}
                </div>
                <div class="timer-label">Time Left</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Main Content -->
    <div class="main-content">
      <!-- Quiz Welcome Screen -->
      <div v-if="!quizStarted && !quizSubmitted" class="welcome-section slide-up">
        <!-- No Quizzes Available State -->
        <div v-if="!hasAvailableQuizzes" class="no-quiz-card">
          <div class="no-quiz-icon">
            <svg width="64" height="64" viewBox="0 0 24 24" fill="currentColor">
              <path d="M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2M12,17A5,5 0 0,1 7,12A5,5 0 0,1 12,7A5,5 0 0,1 17,12A5,5 0 0,1 12,17Z" />
            </svg>
          </div>
          <h2>No Available Quizzes</h2>
          <p>There are currently no quizzes available for this subject. Please check back later or contact your teacher.</p>
          <div class="no-quiz-actions">
            <button @click="$router.push('/student/subjects')" class="btn btn-primary">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                <path d="M20,11V13H8L13.5,18.5L12.08,19.92L4.16,12L12.08,4.08L13.5,5.5L8,11H20Z" />
              </svg>
              Back to Subjects
            </button>
          </div>
        </div>

        <!-- Regular Welcome Card (when quiz is available) -->
        <div v-else class="welcome-card">
          <div class="welcome-header">
            <div class="quiz-badge">
              <svg width="32" height="32" viewBox="0 0 24 24" fill="currentColor">
                <path d="M14,2H6A2,2 0 0,0 4,4V20A2,2 0 0,0 6,22H18A2,2 0 0,0 20,20V8L14,2M18,20H6V4H13V9H18V20Z" />
              </svg>
            </div>
            <h2>{{ quiz.title }}</h2>
            <p v-if="quiz.description" class="quiz-description">{{ quiz.description }}</p>
          </div>

          <!-- Quiz Information Grid -->
          <div class="info-grid">
            <div class="info-card">
              <div class="info-icon">📅</div>
              <div class="info-label">Available Until</div>
              <div class="info-value">{{ formatDate(quiz.end_date) }}</div>
            </div>
            
            <div class="info-card">
              <div class="info-icon">⏱</div>
              <div class="info-label">Time Limit</div>
              <div class="info-value">
                {{ quiz.has_time_limit ? quiz.time_limit_minutes + ' min' : 'No limit' }}
              </div>
            </div>
            
            <div class="info-card">
              <div class="info-icon">📝</div>
              <div class="info-label">Questions</div>
              <div class="info-value">{{ quiz.total_questions }}</div>
            </div>
            
            <div class="info-card">
              <div class="info-icon">🔁</div>
              <div class="info-label">Attempts</div>
              <div class="info-value">{{ attemptsUsed }} / {{ quiz.attempts_allowed }}</div>
            </div>
          </div>

          <!-- Alert Messages -->
          <div v-if="attemptsUsed >= quiz.attempts_allowed" class="alert alert-error">
            <div class="alert-icon">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                <path d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z"/>
              </svg>
            </div>
            <div class="alert-content">
              <div class="alert-title">No Attempts Remaining</div>
              <div class="alert-text">You have used all {{ quiz.attempts_allowed }} attempt(s) for this quiz.</div>
            </div>
          </div>

          <div v-else-if="quiz.has_time_limit" class="alert alert-warning">
            <div class="alert-icon">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                <path d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z"/>
              </svg>
            </div>
            <div class="alert-content">
              <div class="alert-title">Time Limit Active</div>
              <div class="alert-text">You have {{ quiz.time_limit_minutes }} minutes to complete this quiz once you start.</div>
            </div>
          </div>

          <!-- Start Button -->
          <div class="start-section">
            <button 
              v-if="attemptsUsed < quiz.attempts_allowed"
              @click="startQuiz" 
              class="start-button"
            >
              <div class="start-icon">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M14.752 11.168l-3.197-2.132A1 1 0 0010 9.87v4.263a1 1 0 001.555.832l3.197-2.132a1 1 0 000-1.664z"/>
                  <path d="M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
                </svg>
              </div>
              <span>Start Quiz</span>
              <div class="start-arrow">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M13 7l5 5m0 0l-5 5m5-5H6"/>
                </svg>
              </div>
            </button>
          </div>
        </div>

        <!-- Previous Attempts -->
        <div v-if="hasAvailableQuizzes && previousAttempts.length > 0" class="attempts-card">
          <div class="attempts-header">
            <div class="attempts-icon">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                <path d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
              </svg>
            </div>
            <h3>Previous Attempts</h3>
          </div>
          <div class="attempts-list">
            <div v-for="(attempt, index) in previousAttempts" :key="index" class="attempt-item">
              <div class="attempt-info">
                <div class="attempt-number">Attempt {{ index + 1 }}</div>
                <div class="attempt-date">{{ formatDateTime(attempt.submitted_at) }}</div>
              </div>
              <div class="attempt-score">
                <div class="score-percentage" :class="getScoreColor(attempt.percentage)">
                  {{ attempt.percentage }}%
                </div>
                <div class="score-points">{{ attempt.total_score }} / {{ attempt.max_score }}</div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Quiz Interface -->
      <div v-if="quizStarted && !quizSubmitted" class="quiz-interface slide-up">
        <!-- Progress Bar -->
        <div class="progress-section">
          <div class="progress-card">
            <div class="progress-header">
              <div class="progress-info">
                <span class="progress-text">Question {{ currentQuestionIndex + 1 }} of {{ questions.length }}</span>
                <span class="progress-percentage">{{ Math.round(((currentQuestionIndex + 1) / questions.length) * 100) }}%</span>
              </div>
              <div v-if="quiz.has_time_limit" class="timer-compact">
                <div class="timer-compact-icon" :class="{ 'warning': timeRemaining < 300, 'critical': timeRemaining <= 60 }">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2M16.2,16.2L11,13V7H12.5V12.2L17,14.7L16.2,16.2Z" />
                  </svg>
                </div>
                <span class="timer-compact-text" :class="{ 'warning': timeRemaining < 300, 'critical': timeRemaining <= 60 }">
                  {{ formatTime(timeRemaining) }}
                </span>
              </div>
            </div>
            <div class="progress-bar">
              <div class="progress-fill" :style="{ width: ((currentQuestionIndex + 1) / questions.length) * 100 + '%' }"></div>
            </div>
          </div>
        </div>

        <!-- Question Card -->
        <div class="question-section">
          <div class="question-card">
            <div class="question-header">
              <div class="question-number-badge">{{ currentQuestionIndex + 1 }}</div>
              <div class="question-info">
                <h2 class="question-title">{{ currentQuestion.question_text }}</h2>
                <div class="question-points">{{ currentQuestion.points }} {{ currentQuestion.points === 1 ? 'point' : 'points' }}</div>
              </div>
            </div>

            <div class="question-content">
              <!-- Multiple Choice -->
              <div v-if="currentQuestion.question_type === 'multiple_choice'" class="answer-options">
                <div 
                  v-for="(option, index) in currentQuestion.options" 
                  :key="option.id"
                  class="answer-option"
                  :class="{ 'selected': studentAnswers[currentQuestion.id]?.selected_option_id === option.id }"
                  @click="selectOption(currentQuestion.id, option.id)"
                >
                  <div class="option-indicator">{{ String.fromCharCode(65 + index) }}</div>
                  <span class="option-text">{{ option.option_text }}</span>
                  <div class="option-check">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                      <path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/>
                    </svg>
                  </div>
                </div>
              </div>

              <!-- True/False -->
              <div v-if="currentQuestion.question_type === 'true_false'" class="tf-options">
                <div 
                  class="tf-option"
                  :class="{ 'selected': studentAnswers[currentQuestion.id]?.answer_text === 'true' }"
                  @click="selectTrueFalse(currentQuestion.id, 'true')"
                >
                  <div class="tf-icon true-icon">✅</div>
                  <div class="tf-label">True</div>
                </div>
                
                <div 
                  class="tf-option"
                  :class="{ 'selected': studentAnswers[currentQuestion.id]?.answer_text === 'false' }"
                  @click="selectTrueFalse(currentQuestion.id, 'false')"
                >
                  <div class="tf-icon false-icon">❌</div>
                  <div class="tf-label">False</div>
                </div>
              </div>

              <!-- Fill in the Blank -->
              <div v-if="currentQuestion.question_type === 'fill_blank'" class="fill-section">
                <input 
                  type="text"
                  v-model="studentAnswers[currentQuestion.id].answer_text"
                  placeholder="Type your answer here..."
                  class="fill-input"
                />
              </div>
            </div>
          </div>
        </div>

        <!-- Navigation Section -->
        <div class="navigation-section">
          <div class="navigation-card">
            <div class="nav-buttons">
              <button 
                @click="previousQuestion" 
                :disabled="currentQuestionIndex === 0"
                class="nav-btn nav-btn-secondary"
                :class="{ 'disabled': currentQuestionIndex === 0 }"
              >
                <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M15 19l-7-7 7-7"/>
                </svg>
                Previous
              </button>

              <button 
                v-if="currentQuestionIndex < questions.length - 1"
                @click="nextQuestion" 
                class="nav-btn nav-btn-primary"
              >
                Next
                <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M9 5l7 7-7 7"/>
                </svg>
              </button>

              <button 
                v-else
                @click="showSubmitModal = true" 
                class="nav-btn nav-btn-submit"
              >
                <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/>
                </svg>
                Submit Quiz
              </button>
            </div>

            <!-- Question Navigator -->
            <div class="question-navigator">
              <div class="navigator-title">Questions</div>
              <div class="question-dots">
                <button
                  v-for="(q, index) in questions"
                  :key="q.id"
                  @click="goToQuestion(index)"
                  class="question-dot"
                  :class="{
                    'current': index === currentQuestionIndex,
                    'answered': isQuestionAnswered(q.id),
                    'unanswered': !isQuestionAnswered(q.id)
                  }"
                >
                  {{ index + 1 }}
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Quiz Completion -->
      <div v-if="quizSubmitted" class="completion-section slide-up">
        <div class="completion-card">
          <div class="completion-icon">
            <svg width="64" height="64" viewBox="0 0 24 24" fill="currentColor">
              <path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/>
            </svg>
          </div>
          <h2>Quiz Submitted Successfully!</h2>
          <p>Your answers have been recorded. You can view your results in the Grades section once they are available.</p>
          <div class="completion-actions">
            <button @click="$router.push('/student/subjects')" class="btn btn-secondary">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                <path d="M20,11V13H8L13.5,18.5L12.08,19.92L4.16,12L12.08,4.08L13.5,5.5L8,11H20Z" />
              </svg>
              Back to Subjects
            </button>
            <button @click="$router.push('/student/grades')" class="btn btn-primary">
              View Grades
              <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                <path d="M13 7l5 5m0 0l-5 5m5-5H6"/>
              </svg>
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Submit Confirmation Modal -->
    <div v-if="showSubmitModal" class="modal-overlay" @click="showSubmitModal = false">
      <div class="modal-content" @click.stop>
        <div class="modal-header">
          <svg class="w-12 h-12 text-yellow-500 mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/>
          </svg>
          <h3 class="text-2xl font-bold text-gray-800">Submit Quiz?</h3>
        </div>
        <div class="modal-body">
          <p class="text-gray-600 mb-4">Are you sure you want to submit? You cannot change your answers after submission.</p>
          <div class="bg-blue-50 rounded-lg p-4 border-l-4 border-blue-500">
            <div class="flex items-center justify-between text-sm">
              <span class="text-gray-700">Answered Questions:</span>
              <span class="font-bold text-blue-600">{{ answeredCount }} / {{ questions.length }}</span>
            </div>
            <div v-if="answeredCount < questions.length" class="flex items-center justify-between text-sm mt-2">
              <span class="text-gray-700">Unanswered:</span>
              <span class="font-bold text-red-600">{{ questions.length - answeredCount }}</span>
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <button @click="showSubmitModal = false" class="btn-secondary flex-1">
            Cancel
          </button>
          <button @click="submitQuiz" class="btn-submit flex-1">
            <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
            </svg>
            Yes, Submit
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { supabase } from '../../supabase.js'

export default {
  name: 'TakeQuiz',
  data() {
    return {
      quiz: {
        id: null,
        title: 'Quiz Loading...',
        description: '',
        subject_name: this.$route.query.subjectName || 'Subject',
        section: this.$route.query.sectionName || 'Section',
        total_questions: 0,
        has_time_limit: false,
        time_limit_minutes: 0,
        attempts_allowed: 1,
        end_date: '',
        start_date: ''
      },
      questions: [],
      currentQuestionIndex: 0,
      studentAnswers: {},
      quizStarted: false,
      quizSubmitted: false,
      showSubmitModal: false,
      timeRemaining: 0,
      timerInterval: null,
      attemptsUsed: 0,
      previousAttempts: [],
      hasAvailableQuizzes: false,
      availableQuizzes: [],
      currentUser: null,
      studentInfo: null,
      currentAttemptId: null
    };
  },
  computed: {
    currentQuestion() {
      return this.questions[this.currentQuestionIndex] || {};
    },
    progressPercentage() {
      return ((this.currentQuestionIndex + 1) / this.questions.length) * 100;
    },
    answeredCount() {
      return Object.values(this.studentAnswers).filter(answer => 
        answer.selected_option_id || answer.answer_text
      ).length;
    }
  },
  methods: {
    async initializeAuth() {
      try {
        console.log('TakeQuiz: Initializing authentication...')
        
        const { data: { session }, error: sessionError } = await supabase.auth.getSession()
        
        if (sessionError || !session?.user) {
          console.log('TakeQuiz: No session found')
          await this.$router.push('/login')
          return false
        }
        
        this.currentUser = session.user
        console.log('TakeQuiz: Session found for user:', session.user.id)
        
        const { data: profile, error: profileError } = await supabase
          .from('profiles')
          .select('id, role')
          .eq('auth_user_id', session.user.id)
          .single()
        
        if (profileError || !profile || profile.role !== 'student') {
          console.log('TakeQuiz: Invalid profile or role')
          await this.$router.push('/login')
          return false
        }

        const { data: student, error: studentError } = await supabase
          .from('students')
          .select('*')
          .eq('profile_id', profile.id)
          .eq('is_active', true)
          .single()

        if (studentError || !student) {
          console.log('TakeQuiz: Student not found')
          await this.$router.push('/login')
          return false
        }

        this.studentInfo = student
        console.log('TakeQuiz: Student info loaded:', student.id)
        return true

      } catch (error) {
        console.error('TakeQuiz: Authentication error:', error)
        await this.$router.push('/login')
        return false
      }
    },

    async checkQuizAvailability() {
      try {
        const sectionId = this.$route.params.sectionId

        console.log('TakeQuiz: Checking availability for section:', sectionId)
        console.log('TakeQuiz: Student ID:', this.studentInfo?.id)

        if (!sectionId || !this.studentInfo) {
          console.log('TakeQuiz: Missing section ID or student info')
          this.hasAvailableQuizzes = false
          return
        }

        const now = new Date().toISOString()
        console.log('TakeQuiz: Current time:', now)

        // Get all published quizzes for this section (temporarily remove date filters for debugging)
        const { data: quizzes, error: quizError } = await supabase
          .from('quizzes')
          .select('*')
          .eq('section_id', sectionId)
          .eq('is_published', true)

        console.log('TakeQuiz: Query result - quizzes:', quizzes)
        console.log('TakeQuiz: Query error:', quizError)

        if (quizError) {
          console.error('TakeQuiz: Error fetching quizzes:', quizError)
          this.hasAvailableQuizzes = false
          return
        }

        if (!quizzes || quizzes.length === 0) {
          console.log('TakeQuiz: No published quizzes found for this section')
          this.hasAvailableQuizzes = false
          return
        }

        console.log('TakeQuiz: Found', quizzes.length, 'published quiz(es)')

        // Check attempts for each quiz
        const availableQuizzes = []
        for (const quiz of quizzes) {
          console.log('TakeQuiz: Checking quiz:', quiz.title, 'ID:', quiz.id)
          
          const { count, error: countError } = await supabase
            .from('quiz_results')
            .select('id', { count: 'exact' })
            .eq('quiz_id', quiz.id)
            .eq('student_id', this.studentInfo.id)

          if (countError) {
            console.error('TakeQuiz: Error checking attempts:', countError)
            continue
          }

          const attemptsUsed = count || 0
          console.log('TakeQuiz: Attempts used:', attemptsUsed, '/', quiz.attempts_allowed)

          if (attemptsUsed < quiz.attempts_allowed) {
            availableQuizzes.push({
              ...quiz,
              attemptsUsed
            })
            console.log('TakeQuiz: Quiz is available')
          } else {
            console.log('TakeQuiz: Quiz has no remaining attempts')
          }
        }

        console.log('TakeQuiz: Total available quizzes:', availableQuizzes.length)

        this.availableQuizzes = availableQuizzes
        this.hasAvailableQuizzes = availableQuizzes.length > 0
        
        if (this.hasAvailableQuizzes) {
          console.log('TakeQuiz: Loading first available quiz')
          await this.loadQuizData(availableQuizzes[0])
        } else {
          console.log('TakeQuiz: No available quizzes (all used up or none exist)')
        }
        
      } catch (error) {
        console.error('TakeQuiz: Error in checkQuizAvailability:', error)
        this.hasAvailableQuizzes = false
      }
    },

    async loadQuizData(quizData) {
      try {
        console.log('TakeQuiz: Loading quiz data:', quizData.title)
        
        this.quiz = {
          id: quizData.id,
          title: quizData.title,
          description: quizData.description || '',
          subject_name: this.$route.query.subjectName || 'Subject',
          section: this.$route.query.sectionName || 'Section',
          total_questions: quizData.total_questions || 0,
          has_time_limit: quizData.has_time_limit,
          time_limit_minutes: quizData.time_limit_minutes || 0,
          attempts_allowed: quizData.attempts_allowed,
          end_date: quizData.end_date,
          start_date: quizData.start_date
        }

        this.attemptsUsed = quizData.attemptsUsed || 0
        
        await this.loadPreviousAttempts()
        
        console.log('TakeQuiz: Quiz data loaded successfully')
        
      } catch (error) {
        console.error('TakeQuiz: Error loading quiz data:', error)
      }
    },

    async loadPreviousAttempts() {
      try {
        const { data: attempts, error } = await supabase
          .from('quiz_results')
          .select('score, total_score, submitted_at')
          .eq('quiz_id', this.quiz.id)
          .eq('student_id', this.studentInfo.id)
          .order('submitted_at', { ascending: false })

        if (error) throw error

        this.previousAttempts = (attempts || []).map(attempt => ({
          total_score: attempt.score,
          max_score: attempt.total_score,
          percentage: Math.round((attempt.score / attempt.total_score) * 100),
          submitted_at: attempt.submitted_at
        }))

        console.log('TakeQuiz: Loaded', this.previousAttempts.length, 'previous attempt(s)')

      } catch (error) {
        console.error('TakeQuiz: Error loading previous attempts:', error)
        this.previousAttempts = []
      }
    },

    async startQuiz() {
      try {
        console.log('TakeQuiz: Starting quiz...')
        
        const { data: attempt, error: attemptError } = await supabase
          .from('quiz_results')
          .insert([{
            quiz_id: this.quiz.id,
            student_id: this.studentInfo.id,
            score: 0,
            total_score: 0,
            started_at: new Date().toISOString(),
            submitted_at: null
          }])
          .select()
          .single()

        if (attemptError) {
          console.error('TakeQuiz: Error creating attempt:', attemptError)
          alert('Failed to start quiz. Please try again.')
          return
        }

        this.currentAttemptId = attempt.id
        this.quizStarted = true

        console.log('TakeQuiz: Attempt created with ID:', attempt.id)

        if (this.quiz.has_time_limit) {
          this.timeRemaining = this.quiz.time_limit_minutes * 60
          this.startTimer()
          console.log('TakeQuiz: Timer started for', this.quiz.time_limit_minutes, 'minutes')
        }

        await this.loadQuestions()

      } catch (error) {
        console.error('TakeQuiz: Error starting quiz:', error)
        alert('Failed to start quiz. Please try again.')
      }
    },

    async loadQuestions() {
      try {
        console.log('TakeQuiz: Loading questions for quiz ID:', this.quiz.id)
        
        const { data: questions, error: questionsError } = await supabase
          .from('questions')
          .select(`
            id,
            question_number,
            question_type,
            question_text,
            points,
            correct_answer,
            question_options (
              id,
              option_text,
              is_correct
            )
          `)
          .eq('quiz_id', this.quiz.id)
          .order('question_number', { ascending: true })

        if (questionsError) throw questionsError

        this.questions = questions.map(q => ({
          id: q.id,
          question_number: q.question_number,
          question_type: q.question_type,
          question_text: q.question_text,
          points: q.points,
          correct_answer: q.correct_answer,
          options: q.question_options || []
        }))
        
        this.questions.forEach(q => {
          this.studentAnswers[q.id] = {
            question_id: q.id,
            selected_option_id: null,
            answer_text: '',
            points_possible: q.points
          }
        })

        console.log('TakeQuiz: Loaded', this.questions.length, 'question(s)')

      } catch (error) {
        console.error('TakeQuiz: Error loading questions:', error)
        alert('Failed to load questions. Please refresh the page.')
      }
    },

    startTimer() {
      this.timerInterval = setInterval(() => {
        if (this.timeRemaining > 0) {
          this.timeRemaining--
        } else {
          this.autoSubmitQuiz()
        }
      }, 1000)
    },

    formatTime(seconds) {
      const mins = Math.floor(seconds / 60)
      const secs = seconds % 60
      return `${mins}:${secs.toString().padStart(2, '0')}`
    },

    formatDate(dateString) {
      return new Date(dateString).toLocaleDateString()
    },

    formatDateTime(dateString) {
      return new Date(dateString).toLocaleString()
    },

    getScoreColor(percentage) {
      if (percentage >= 90) return 'text-green-600'
      if (percentage >= 75) return 'text-blue-600'
      if (percentage >= 60) return 'text-yellow-600'
      return 'text-red-600'
    },

    nextQuestion() {
      if (this.currentQuestionIndex < this.questions.length - 1) {
        this.currentQuestionIndex++
      }
    },

    previousQuestion() {
      if (this.currentQuestionIndex > 0) {
        this.currentQuestionIndex--
      }
    },

    goToQuestion(index) {
      this.currentQuestionIndex = index
    },

    isQuestionAnswered(questionId) {
      const answer = this.studentAnswers[questionId]
      return !!(answer?.selected_option_id || answer?.answer_text)
    },

    selectOption(questionId, optionId) {
      this.studentAnswers[questionId].selected_option_id = optionId
    },

    selectTrueFalse(questionId, value) {
      this.studentAnswers[questionId].answer_text = value
    },

    async submitQuiz() {
      try {
        console.log('TakeQuiz: Submitting quiz...')
        
        if (this.timerInterval) {
          clearInterval(this.timerInterval)
        }
        
        this.showSubmitModal = false

        let totalScore = 0
        let earnedScore = 0
        const answerRecords = []

        for (const question of this.questions) {
          const studentAnswer = this.studentAnswers[question.id]
          totalScore += question.points
          let isCorrect = false
          let pointsEarned = 0

          if (question.question_type === 'multiple_choice') {
            const selectedOption = question.options.find(
              opt => opt.id === studentAnswer.selected_option_id
            )
            if (selectedOption && selectedOption.is_correct) {
              isCorrect = true
              pointsEarned = question.points
              earnedScore += question.points
            }
          } else if (question.question_type === 'true_false') {
            if (studentAnswer.answer_text?.toLowerCase() === question.correct_answer?.toLowerCase()) {
              isCorrect = true
              pointsEarned = question.points
              earnedScore += question.points
            }
          } else if (question.question_type === 'fill_blank') {
            if (studentAnswer.answer_text?.trim().toLowerCase() === question.correct_answer?.trim().toLowerCase()) {
              isCorrect = true
              pointsEarned = question.points
              earnedScore += question.points
            }
          }

          answerRecords.push({
            quiz_result_id: this.currentAttemptId,
            question_id: question.id,
            selected_option_id: studentAnswer.selected_option_id,
            answer_text: studentAnswer.answer_text || null,
            is_correct: isCorrect,
            points_earned: pointsEarned
          })
        }

        console.log('TakeQuiz: Score:', earnedScore, '/', totalScore)

        const { error: answersError } = await supabase
          .from('student_answers')
          .insert(answerRecords)

        if (answersError) throw answersError

        const { error: updateError } = await supabase
          .from('quiz_results')
          .update({
            score: earnedScore,
            total_score: totalScore,
            submitted_at: new Date().toISOString()
          })
          .eq('id', this.currentAttemptId)

        if (updateError) throw updateError

        console.log('TakeQuiz: Quiz submitted successfully')
        this.quizSubmitted = true

      } catch (error) {
        console.error('TakeQuiz: Error submitting quiz:', error)
        alert('Failed to submit quiz. Please try again.')
      }
    },

    autoSubmitQuiz() {
      alert('Time is up! Your quiz will be automatically submitted.')
      this.submitQuiz()
    }
  },

  async mounted() {
    console.log('TakeQuiz: Component mounted')
    console.log('TakeQuiz: Route params:', this.$route.params)
    console.log('TakeQuiz: Route query:', this.$route.query)
    
    const authSuccess = await this.initializeAuth()
    if (!authSuccess) {
      console.log('TakeQuiz: Auth failed, redirecting...')
      return
    }
    
    await this.checkQuizAvailability()
  },

  beforeUnmount() {
    console.log('TakeQuiz: Component unmounting')
    if (this.timerInterval) {
      clearInterval(this.timerInterval)
    }
  }
}
</script>

<style scoped>
/* Color Theme Variables */
:root {
  --primary-green: #3D8D7A;
  --light-green: #B3D8A8;
  --mint-green: #A3D1C6;
  --white: #FFFFFF;
  --gray-50: #f9fafb;
  --gray-100: #f3f4f6;
  --gray-200: #e5e7eb;
  --gray-300: #d1d5db;
  --gray-400: #9ca3af;
  --gray-500: #6b7280;
  --gray-600: #4b5563;
  --gray-700: #374151;
  --gray-800: #1f2937;
  --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
  --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
  --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
  --shadow-xl: 0 20px 25px -5px rgba(0, 0, 0, 0.1);
  --warning-color: #f59e0b;
  --critical-color: #ef4444;
  --success-color: #10b981;
}

/* Base Styles */
.take-quiz-page {
  min-height: 100vh;
  background: linear-gradient(135deg, var(--light-green) 0%, var(--mint-green) 100%);
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
}

/* Header Section */
.page-header {
  background: var(--white);
  box-shadow: var(--shadow-md);
  border-bottom: 3px solid var(--primary-green);
}

.header-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem;
}

.header-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.5rem 0;
}

.quiz-info {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.quiz-icon {
  width: 48px;
  height: 48px;
  background: linear-gradient(135deg, var(--primary-green), var(--mint-green));
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--white);
}

.quiz-details h1 {
  font-size: 1.875rem;
  font-weight: 700;
  color: var(--gray-800);
  margin: 0;
}

.quiz-details p {
  color: var(--gray-600);
  margin: 0.25rem 0 0 0;
  font-size: 0.95rem;
}

/* Timer Display */
.timer-display {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  background: rgba(61, 141, 122, 0.1);
  border: 2px solid var(--primary-green);
  border-radius: 12px;
  padding: 1rem 1.5rem;
}

.timer-icon {
  width: 36px;
  height: 36px;
  background: var(--primary-green);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--white);
  transition: all 0.3s ease;
}

.timer-icon.warning {
  background: var(--warning-color);
  animation: pulse 2s infinite;
}

.timer-icon.critical {
  background: var(--critical-color);
  animation: pulse 1s infinite;
}

.timer-value {
  font-size: 1.25rem;
  font-weight: 700;
  color: var(--gray-800);
}

.timer-value.warning {
  color: var(--warning-color);
}

.timer-value.critical {
  color: var(--critical-color);
}

.timer-label {
  font-size: 0.875rem;
  color: var(--gray-600);
  margin: 0;
}

/* Main Content */
.main-content {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
}

/* Welcome Section */
.welcome-section {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.welcome-card {
  background: var(--white);
  border-radius: 24px;
  padding: 3rem;
  box-shadow: var(--shadow-xl);
  border: 1px solid rgba(61, 141, 122, 0.1);
}

.welcome-header {
  text-align: center;
  margin-bottom: 2.5rem;
}

.quiz-badge {
  width: 80px;
  height: 80px;
  background: linear-gradient(135deg, var(--primary-green), var(--mint-green));
  border-radius: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 1.5rem;
  color: var(--white);
  animation: bounce-slow 3s ease-in-out infinite;
}

.welcome-header h2 {
  font-size: 2.25rem;
  font-weight: 700;
  color: var(--gray-800);
  margin: 0 0 1rem 0;
}

.quiz-description {
  font-size: 1.125rem;
  color: var(--gray-600);
  line-height: 1.6;
  margin: 0;
}

/* Info Grid */
.info-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1.5rem;
  margin-bottom: 2rem;
}

.info-card {
  background: linear-gradient(135deg, rgba(163, 209, 198, 0.1) 0%, rgba(179, 216, 168, 0.1) 100%);
  border: 2px solid var(--mint-green);
  border-radius: 16px;
  padding: 1.5rem;
  text-align: center;
  transition: all 0.3s ease;
}

.info-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 25px rgba(163, 209, 198, 0.3);
  border-color: var(--primary-green);
}

.info-icon {
  font-size: 2rem;
  margin-bottom: 0.75rem;
  display: block;
}

.info-label {
  font-size: 0.875rem;
  color: var(--gray-600);
  font-weight: 500;
  margin-bottom: 0.5rem;
}

.info-value {
  font-size: 1.125rem;
  font-weight: 700;
  color: var(--gray-800);
}

/* Alerts */
.alert {
  display: flex;
  align-items: flex-start;
  gap: 1rem;
  padding: 1.5rem;
  border-radius: 12px;
  margin-bottom: 2rem;
}

.alert-error {
  background: linear-gradient(135deg, #fee2e2 0%, #fecaca 100%);
  border: 2px solid #f87171;
  color: #991b1b;
}

.alert-warning {
  background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);
  border: 2px solid #fbbf24;
  color: #92400e;
}

.alert-icon {
  width: 24px;
  height: 24px;
  flex-shrink: 0;
}

.alert-title {
  font-weight: 700;
  font-size: 1.125rem;
  margin-bottom: 0.25rem;
}

.alert-text {
  font-size: 0.95rem;
  line-height: 1.5;
}

/* Start Button */
.start-section {
  text-align: center;
}

.start-button {
  display: inline-flex;
  align-items: center;
  gap: 1rem;
  padding: 1.25rem 3rem;
  background: linear-gradient(135deg, var(--primary-green), var(--mint-green));
  color: var(--white);
  border: none;
  border-radius: 16px;
  font-size: 1.25rem;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 8px 25px rgba(61, 141, 122, 0.4);
}

.start-button:hover {
  transform: translateY(-3px) scale(1.02);
  box-shadow: 0 12px 35px rgba(61, 141, 122, 0.6);
}

.start-icon, .start-arrow {
  flex-shrink: 0;
}

/* Previous Attempts */
.attempts-card {
  background: var(--white);
  border-radius: 20px;
  padding: 2rem;
  box-shadow: var(--shadow-lg);
  border: 1px solid rgba(61, 141, 122, 0.1);
}

.attempts-header {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 1.5rem;
  padding-bottom: 1rem;
  border-bottom: 2px solid var(--gray-100);
}

.attempts-icon {
  width: 48px;
  height: 48px;
  background: linear-gradient(135deg, var(--primary-green), var(--mint-green));
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--white);
}

.attempts-header h3 {
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--gray-800);
  margin: 0;
}

.attempts-list {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.attempt-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.25rem;
  background: var(--gray-50);
  border: 2px solid var(--gray-200);
  border-radius: 12px;
  transition: all 0.3s ease;
}

.attempt-item:hover {
  border-color: var(--mint-green);
  background: rgba(163, 209, 198, 0.05);
  transform: translateX(4px);
}

.attempt-number {
  font-weight: 600;
  color: var(--gray-800);
  font-size: 1.125rem;
}

.attempt-date {
  font-size: 0.875rem;
  color: var(--gray-600);
  margin-top: 0.25rem;
}

.score-percentage {
  font-size: 1.5rem;
  font-weight: 700;
}

.score-points {
  font-size: 0.875rem;
  color: var(--gray-600);
  margin-top: 0.25rem;
}

/* Quiz Interface */
.quiz-interface {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

/* Progress Section */
.progress-card {
  background: var(--white);
  border-radius: 16px;
  padding: 1.5rem;
  box-shadow: var(--shadow-md);
  border: 1px solid rgba(61, 141, 122, 0.1);
}

.progress-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
}

.progress-text {
  font-size: 1rem;
  font-weight: 600;
  color: var(--gray-800);
}

.progress-percentage {
  font-size: 1rem;
  font-weight: 700;
  color: var(--primary-green);
}

.timer-compact {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem 1rem;
  background: rgba(61, 141, 122, 0.1);
  border-radius: 8px;
}

.timer-compact-icon {
  color: var(--primary-green);
}

.timer-compact-icon.warning {
  color: var(--warning-color);
}

.timer-compact-icon.critical {
  color: var(--critical-color);
  animation: pulse 1s infinite;
}

.timer-compact-text {
  font-weight: 600;
  color: var(--gray-800);
}

.timer-compact-text.warning {
  color: var(--warning-color);
}

.timer-compact-text.critical {
  color: var(--critical-color);
}

.progress-bar {
  width: 100%;
  height: 8px;
  background: var(--gray-200);
  border-radius: 10px;
  overflow: hidden;
}

.progress-fill {
  height: 100%;
  background: linear-gradient(90deg, var(--primary-green) 0%, var(--mint-green) 100%);
  transition: width 0.3s ease;
}

/* Question Section */
.question-card {
  background: var(--white);
  border-radius: 20px;
  padding: 2.5rem;
  box-shadow: var(--shadow-lg);
  border: 1px solid rgba(61, 141, 122, 0.1);
}

.question-header {
  display: flex;
  align-items: flex-start;
  gap: 1.5rem;
  margin-bottom: 2rem;
  padding-bottom: 1.5rem;
  border-bottom: 2px solid var(--gray-100);
}

.question-number-badge {
  width: 48px;
  height: 48px;
  background: linear-gradient(135deg, var(--primary-green), var(--mint-green));
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--white);
  font-weight: 700;
  font-size: 1.25rem;
  flex-shrink: 0;
  box-shadow: 0 4px 12px rgba(61, 141, 122, 0.3);
}

.question-info {
  flex: 1;
}

.question-title {
  font-size: 1.5rem;
  font-weight: 600;
  color: var(--gray-800);
  line-height: 1.4;
  margin: 0 0 0.5rem 0;
}

.question-points {
  font-size: 0.95rem;
  color: var(--gray-600);
  font-weight: 500;
}

/* Answer Options */
.answer-options {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.answer-option {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1.25rem 1.5rem;
  background: var(--white);
  border: 3px solid var(--gray-200);
  border-radius: 16px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.answer-option:hover {
  border-color: var(--mint-green);
  background: rgba(163, 209, 198, 0.05);
  transform: translateX(4px);
}

.answer-option.selected {
  border-color: var(--primary-green);
  background: rgba(61, 141, 122, 0.05);
  box-shadow: 0 4px 12px rgba(61, 141, 122, 0.2);
}

.option-indicator {
  width: 36px;
  height: 36px;
  background: var(--gray-200);
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  color: var(--gray-600);
  flex-shrink: 0;
  transition: all 0.3s ease;
}

.answer-option.selected .option-indicator {
  background: linear-gradient(135deg, var(--primary-green), var(--mint-green));
  color: var(--white);
}

.option-text {
  flex: 1;
  font-size: 1rem;
  line-height: 1.5;
  color: var(--gray-800);
}

.option-check {
  width: 24px;
  height: 24px;
  color: transparent;
  transition: all 0.3s ease;
}

.answer-option.selected .option-check {
  color: var(--success-color);
}

/* True/False Options */
.tf-options {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.5rem;
}

.tf-option {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 2rem;
  background: var(--white);
  border: 3px solid var(--gray-200);
  border-radius: 20px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.tf-option:hover {
  border-color: var(--mint-green);
  background: rgba(163, 209, 198, 0.05);
  transform: translateY(-4px);
  box-shadow: 0 8px 25px rgba(163, 209, 198, 0.3);
}

.tf-option.selected {
  border-color: var(--primary-green);
  background: rgba(61, 141, 122, 0.05);
  box-shadow: 0 8px 25px rgba(61, 141, 122, 0.3);
  transform: scale(1.02);
}

.tf-icon {
  font-size: 3rem;
  margin-bottom: 1rem;
}

.tf-label {
  font-size: 1.25rem;
  font-weight: 600;
  color: var(--gray-800);
}

/* Fill Input */
.fill-section {
  margin-top: 1rem;
}

.fill-input {
  width: 100%;
  padding: 1.25rem 1.5rem;
  border: 3px solid var(--gray-200);
  border-radius: 12px;
  font-size: 1.125rem;
  transition: all 0.3s ease;
  background: var(--white);
}

.fill-input:focus {
  outline: none;
  border-color: var(--primary-green);
  box-shadow: 0 0 0 4px rgba(61, 141, 122, 0.1);
}

/* Navigation Section */
.navigation-card {
  background: var(--white);
  border-radius: 16px;
  padding: 1.5rem;
  box-shadow: var(--shadow-md);
  border: 1px solid rgba(61, 141, 122, 0.1);
}

.nav-buttons {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1.5rem;
}

.nav-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.875rem 1.5rem;
  border: none;
  border-radius: 10px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
}

.nav-btn-secondary {
  background: var(--gray-100);
  color: var(--gray-600);
  border: 2px solid var(--gray-300);
}

.nav-btn-secondary:hover:not(.disabled) {
  background: var(--gray-200);
  color: var(--gray-700);
  transform: translateY(-1px);
}

.nav-btn-secondary.disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.nav-btn-primary {
  background: linear-gradient(135deg, var(--primary-green), var(--mint-green));
  color: var(--white);
  box-shadow: 0 4px 12px rgba(61, 141, 122, 0.3);
}

.nav-btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 16px rgba(61, 141, 122, 0.4);
}

.nav-btn-submit {
  background: linear-gradient(135deg, var(--success-color), #34d399);
  color: var(--white);
  box-shadow: 0 4px 12px rgba(16, 185, 129, 0.3);
}

.nav-btn-submit:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 16px rgba(16, 185, 129, 0.4);
}

/* Question Navigator */
.question-navigator {
  border-top: 2px solid var(--gray-100);
  padding-top: 1.5rem;
}

.navigator-title {
  font-size: 0.875rem;
  font-weight: 600;
  color: var(--gray-600);
  margin-bottom: 1rem;
  text-align: center;
}

.question-dots {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  justify-content: center;
}

.question-dot {
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 10px;
  border: 2px solid var(--gray-300);
  background: var(--white);
  color: var(--gray-600);
  font-weight: 600;
  font-size: 0.875rem;
  cursor: pointer;
  transition: all 0.3s ease;
}

.question-dot:hover {
  border-color: var(--mint-green);
  transform: scale(1.1);
}

.question-dot.current {
  background: linear-gradient(135deg, var(--primary-green), var(--mint-green));
  border-color: var(--primary-green);
  color: var(--white);
  box-shadow: 0 4px 12px rgba(61, 141, 122, 0.3);
}

.question-dot.answered {
  background: rgba(179, 216, 168, 0.2);
  border-color: var(--light-green);
  color: var(--primary-green);
}

.question-dot.answered.current {
  background: linear-gradient(135deg, var(--success-color), #34d399);
  border-color: var(--success-color);
  color: var(--white);
}

/* Completion Section */
.completion-section {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 60vh;
}

.completion-card {
  background: var(--white);
  border-radius: 24px;
  padding: 4rem 3rem;
  text-align: center;
  box-shadow: var(--shadow-xl);
  border: 1px solid rgba(61, 141, 122, 0.1);
  max-width: 600px;
  width: 100%;
}

.completion-icon {
  width: 80px;
  height: 80px;
  background: linear-gradient(135deg, var(--success-color), #34d399);
  border-radius: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 2rem;
  color: var(--white);
  animation: bounce-slow 2s ease-in-out infinite;
}

.completion-card h2 {
  font-size: 2.25rem;
  font-weight: 700;
  color: var(--gray-800);
  margin-bottom: 1rem;
}

.completion-card p {
  font-size: 1.125rem;
  color: var(--gray-600);
  margin-bottom: 2.5rem;
  line-height: 1.6;
}

.completion-actions {
  display: flex;
  gap: 1rem;
  justify-content: center;
}

/* Buttons */
.btn {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.875rem 1.5rem;
  border-radius: 12px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  border: none;
  font-size: 0.95rem;
}

.btn-primary {
  background: linear-gradient(135deg, var(--primary-green), var(--mint-green));
  color: var(--white);
  box-shadow: 0 4px 12px rgba(61, 141, 122, 0.3);
}

.btn-primary:hover {
  transform: translateY(-1px);
  box-shadow: 0 6px 16px rgba(61, 141, 122, 0.4);
}

.btn-secondary {
  background: var(--white);
  color: var(--gray-600);
  border: 2px solid var(--gray-300);
}

.btn-secondary:hover {
  background: var(--gray-50);
  color: var(--gray-700);
  border-color: var(--gray-400);
}

/* Modal Styles */
.modal-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.6);
  backdrop-filter: blur(4px);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 50;
  animation: fadeIn 0.3s ease;
}

.modal-content {
  background: var(--white);
  border-radius: 24px;
  max-width: 500px;
  width: 90%;
  box-shadow: var(--shadow-xl);
  animation: slideUp 0.3s ease;
}

.modal-header {
  padding: 2rem 2rem 1rem;
  text-align: center;
}

.modal-header h3 {
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--gray-800);
  margin: 1rem 0 0 0;
}

.modal-body {
  padding: 0 2rem 1.5rem;
}

.modal-body p {
  color: var(--gray-600);
  line-height: 1.6;
  margin-bottom: 1rem;
}

.modal-footer {
  padding: 1.5rem 2rem;
  border-top: 1px solid var(--gray-200);
  display: flex;
  gap: 1rem;
}

.btn-submit {
  background: linear-gradient(135deg, var(--success-color), #34d399);
  color: var(--white);
  flex: 1;
}

.btn-submit:hover {
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(16, 185, 129, 0.3);
}

/* Score Colors */
.text-green-600 { color: var(--success-color); }
.text-blue-600 { color: #3b82f6; }
.text-yellow-600 { color: var(--warning-color); }
.text-red-600 { color: var(--critical-color); }

/* Animations */
@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

@keyframes slideUp {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes pulse {
  0%, 100% { transform: scale(1); }
  50% { transform: scale(1.05); }
}

@keyframes bounce-slow {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-10px); }
}

.slide-up {
  animation: slideUp 0.5s ease-out;
}

/* Responsive Design */
@media (max-width: 768px) {
  .take-quiz-page {
    padding: 1rem;
  }
  
  .header-container {
    padding: 0 1rem;
  }
  
  .header-content {
    flex-direction: column;
    gap: 1rem;
    text-align: center;
  }
  
  .main-content {
    padding: 1rem;
  }
  
  .welcome-card, .question-card, .completion-card {
    padding: 2rem 1.5rem;
  }
  
  .info-grid {
    grid-template-columns: 1fr;
  }
  
  .tf-options {
    grid-template-columns: 1fr;
  }
  
  .nav-buttons {
    flex-direction: column;
    gap: 1rem;
  }
  
  .completion-actions, .modal-footer {
    flex-direction: column;
  }
  
  .btn {
    justify-content: center;
  }
  
  .question-dots {
    gap: 0.25rem;
  }
  
  .question-dot {
    width: 36px;
    height: 36px;
    font-size: 0.75rem;
  }
}

/* Utility Classes */
.w-12 { width: 3rem; }
.h-12 { height: 3rem; }
.text-yellow-500 { color: var(--warning-color); }
.text-2xl { font-size: 1.5rem; }
.font-bold { font-weight: 700; }
.text-gray-800 { color: var(--gray-800); }
.text-gray-600 { color: var(--gray-600); }
.text-blue-600 { color: #3b82f6; }
.text-red-600 { color: var(--critical-color); }
.text-sm { font-size: 0.875rem; }
.mb-4 { margin-bottom: 1rem; }
.mt-2 { margin-top: 0.5rem; }
.w-5 { width: 1.25rem; }
.h-5 { height: 1.25rem; }
.mr-2 { margin-right: 0.5rem; }
.bg-blue-50 { background-color: #eff6ff; }
.rounded-lg { border-radius: 0.5rem; }
.p-4 { padding: 1rem; }
.border-l-4 { border-left-width: 4px; }
.border-blue-500 { border-color: #3b82f6; }
.flex-1 { flex: 1; }
.btn-secondary.flex-1 { flex: 1; }
.btn-submit.flex-1 { flex: 1; }
</style>