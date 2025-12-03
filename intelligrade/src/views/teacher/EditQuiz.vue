<template>
  <div class="dashboard-container">
    <!-- Top Navigation Bar -->
    <nav class="top-navbar">
      <div class="navbar-content">
        <!-- Left: Logo and Brand -->
        <div class="navbar-left">
          <div class="brand-logo">
            <img src="@/assets/LOGO WAY BG.png" alt="IntelliGrade" class="logo-img" />
            <span class="brand-name">IntelliGrade</span>
          </div>
        </div>
        <!-- Center: Empty space for clean look -->
        <div class="navbar-center">
        </div>
        
        <!-- Right: User Profile -->
        <div class="navbar-right">
          <div class="user-profile-wrapper">
            <div class="user-profile rounded-bg">
              <div class="user-avatar">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
                  <circle cx="12" cy="7" r="4"></circle>
                </svg>
              </div>
              <span class="user-name">{{ fullName }}</span>
            </div>
          </div>
        </div>
      </div>
    </nav>

    <!-- Sidebar Navigation -->
    <aside class="sidebar" style="background:#3D8D7A; border-right:none;">
      <nav class="sidebar-nav">
        <router-link to="/teacher/dashboard" class="sidebar-item rounded-bg">
          <div class="sidebar-icon">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M10 20v-6h4v6m5-8h3L12 3 2 12h3v8h5v-6h4v6h5v-8z" />
            </svg>
          </div>
          <span class="sidebar-tooltip">Dashboard</span>
        </router-link>
        <router-link to="/teacher/subjects" class="sidebar-item rounded-bg active">
          <div class="sidebar-icon">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <rect x="3" y="7" width="18" height="13" rx="2" />
              <path d="M3 7l9-4 9 4" />
            </svg>
          </div>
          <span class="sidebar-tooltip">Classes</span>
        </router-link>
        <router-link to="/teacher/gradebook" class="sidebar-item rounded-bg">
          <div class="sidebar-icon">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <rect x="4" y="4" width="16" height="16" rx="2" />
              <path d="M8 2v4M16 2v4" />
            </svg>
          </div>
          <span class="sidebar-tooltip">Gradebook</span>
        </router-link>
        <router-link to="/teacher/upload-assessment" class="sidebar-item rounded-bg">
          <div class="sidebar-icon">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M12 19V6M5 12l7-7 7 7" />
              <rect x="5" y="19" width="14" height="2" rx="1" />
            </svg>
          </div>
          <span class="sidebar-tooltip">Upload Assessment</span>
        </router-link>
        <router-link to="/teacher/analytics" class="sidebar-item rounded-bg">
          <div class="sidebar-icon">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <rect x="3" y="12" width="4" height="8" />
              <rect x="10" y="8" width="4" height="12" />
              <rect x="17" y="4" width="4" height="16" />
            </svg>
          </div>
          <span class="sidebar-tooltip">Analytics</span>
        </router-link>
        <router-link to="/teacher/messages" class="sidebar-item rounded-bg">
          <div class="sidebar-icon">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <rect x="3" y="5" width="18" height="14" rx="2" />
              <path d="M3 5l9 6 9-6" />
            </svg>
          </div>
          <span class="sidebar-tooltip">Messages</span>
        </router-link>
      </nav>
    </aside>

    <!-- Main Content Area -->
    <main class="main-content">
      <!-- Page Header -->
      <div class="subjects-header">
        <div class="header-left">
          <div class="header-icon-wrapper">
            <div class="header-icon">
              <svg width="32" height="32" viewBox="0 0 24 24" fill="currentColor">
                <path d="M20.71,7.04C21.1,6.65 21.1,6 20.71,5.63L18.37,3.29C18,2.9 17.35,2.9 16.96,3.29L15.12,5.12L18.87,8.87M3,17.25V21H6.75L17.81,9.93L14.06,6.18L3,17.25Z" />
              </svg>
            </div>
          </div>
          <div>
            <h1>Edit Quiz</h1>
            <p>{{ quiz.title || 'Loading...' }}</p>
          </div>
        </div>
        <div class="header-right">
          <button @click="saveQuiz" :disabled="isSaving" class="create-subject-btn">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M15,9H5V5H15M12,19A3,3 0 0,1 9,16A3,3 0 0,1 12,13A3,3 0 0,1 15,16A3,3 0 0,1 12,19M17,3H5C3.89,3 3,3.9 3,5V19A2,2 0 0,0 5,21H19A2,2 0 0,0 21,19V7L17,3Z" />
            </svg>
            {{ isSaving ? 'Saving...' : 'Save Changes' }}
          </button>
          <button @click="goBack" class="create-subject-btn secondary">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M10 19l-7-7 7-7m-7 7h18"></path>
            </svg>
            Back
          </button>
        </div>
      </div>

      <!-- Main Content -->
  <div class="content-wrapper">
      <!-- Loading State -->
      <div v-if="isLoading" class="loading-state">
        <div class="loading-spinner"></div>
        <p>Loading quiz...</p>
      </div>

      <!-- Error State -->
      <div v-else-if="error" class="empty-state">
        <div class="empty-icon">
          <svg width="64" height="64" viewBox="0 0 24 24" fill="currentColor">
            <path d="M11,15H13V17H11V15M11,7H13V13H11V7M12,2C6.47,2 2,6.5 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2M12,20A8,8 0 0,1 4,12A8,8 0 0,1 12,4A8,8 0 0,1 20,12A8,8 0 0,1 12,20Z" />
          </svg>
        </div>
        <h3 class="empty-title">Error Loading Quiz</h3>
        <p class="empty-desc">{{ error }}</p>
        <button @click="loadQuiz" class="create-quiz-btn">Try Again</button>
      </div>

      <!-- Edit Form -->
      <div v-else class="edit-form">
        <!-- Quiz Settings Card -->
        <div class="form-card">
          <div class="card-header">
            <h3>Quiz Settings</h3>
          </div>
          <div class="card-body">
            <div class="form-group">
              <label for="title">Quiz Title *</label>
              <input 
                type="text" 
                id="title" 
                v-model="quiz.title" 
                placeholder="Enter quiz title"
                required
              />
            </div>

            <div class="form-group">
              <label for="description">Description</label>
              <textarea 
                id="description" 
                v-model="quiz.description" 
                placeholder="Enter quiz description (optional)"
                rows="3"
              ></textarea>
            </div>

            <div class="form-row">
              <div class="form-group">
                <label for="status">Status</label>
                <select id="status" v-model="quiz.status">
                  <option value="draft">Draft</option>
                  <option value="published">Published</option>
                  <option value="archived">Archived</option>
                </select>
              </div>

              <div class="form-group">
                <label for="attempts">Attempts Allowed *</label>
                <input 
                  type="number" 
                  id="attempts" 
                  v-model.number="quiz.attempts_allowed" 
                  min="1"
                  max="999"
                  required
                />
                <small>Use 999 for unlimited attempts</small>
              </div>
            </div>

            <div class="form-row">
              <div class="form-group checkbox-group">
                <label>
                  <input type="checkbox" v-model="quiz.has_time_limit" />
                  <span>Enable Time Limit</span>
                </label>
              </div>

              <div class="form-group" v-if="quiz.has_time_limit">
                <label for="timeLimit">Time Limit (minutes) *</label>
                <input 
                  type="number" 
                  id="timeLimit" 
                  v-model.number="quiz.time_limit_minutes" 
                  min="1"
                  :required="quiz.has_time_limit"
                />
              </div>
            </div>

            <div class="form-row">
              <div class="form-group checkbox-group">
                <label>
                  <input type="checkbox" v-model="quiz.shuffle_questions" />
                  <span>Shuffle Questions</span>
                </label>
              </div>

              <div class="form-group checkbox-group">
                <label>
                  <input type="checkbox" v-model="quiz.shuffle_options" />
                  <span>Shuffle Options</span>
                </label>
              </div>
            </div>

            <div class="form-row">
              <div class="form-group">
                <label for="startDate">Start Date</label>
                <input 
                  type="datetime-local" 
                  id="startDate" 
                  v-model="quiz.start_date" 
                />
              </div>

              <div class="form-group">
                <label for="endDate">End Date</label>
                <input 
                  type="datetime-local" 
                  id="endDate" 
                  v-model="quiz.end_date" 
                />
              </div>
            </div>
          </div>
        </div>

        <!-- Questions Card -->
        <div class="form-card">
          <div class="card-header">
            <h3>Questions ({{ questions.length }})</h3>
            <button @click="addQuestion" class="add-question-btn">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                <path d="M19,13H13V19H11V13H5V11H11V5H13V11H19V13Z" />
              </svg>
              Add Question
            </button>
          </div>
          <div class="card-body">
            <div v-if="questions.length === 0" class="no-questions">
              <p>No questions added yet. Click "Add Question" to get started.</p>
            </div>

            <div v-else class="questions-list">
              <div 
                v-for="(question, index) in questions" 
                :key="question.id || `new-${index}`"
                class="question-item"
              >
                <div class="question-header">
                  <div class="question-number">{{ index + 1 }}</div>
                  <button @click="removeQuestion(index)" class="delete-question-btn">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor">
                      <path d="M19,4H15.5L14.5,3H9.5L8.5,4H5V6H19M6,19A2,2 0 0,0 8,21H16A2,2 0 0,0 18,19V7H6V19Z" />
                    </svg>
                  </button>
                </div>

                <div class="question-content">
                  <div class="form-group">
                    <label>Question Type *</label>
                    <select v-model="question.question_type" @change="onQuestionTypeChange(question)">
                      <option value="multiple_choice">Multiple Choice</option>
                      <option value="true_false">True/False</option>
                      <option value="fill_blank">Fill in the Blank</option>
                    </select>
                  </div>

                  <div class="form-group">
                    <label>Question Text *</label>
                    <textarea 
                      v-model="question.question_text" 
                      placeholder="Enter your question"
                      rows="2"
                      required
                    ></textarea>
                  </div>

                  <div class="form-group">
                    <label>Points *</label>
                    <input 
                      type="number" 
                      v-model.number="question.points" 
                      min="0.01"
                      step="0.01"
                      required
                    />
                  </div>

                  <!-- Multiple Choice Options -->
                  <div v-if="question.question_type === 'multiple_choice'" class="options-section">
                    <label>Options *</label>
                    <div class="options-list">
                      <div 
                        v-for="(option, optIndex) in question.options" 
                        :key="optIndex"
                        class="option-item"
                      >
                        <input 
                          type="radio" 
                          :name="`correct-${question.id || index}`"
                          :checked="option.is_correct"
                          @change="setCorrectOption(question, optIndex)"
                        />
                        <input 
                          type="text" 
                          v-model="option.option_text" 
                          :placeholder="`Option ${optIndex + 1}`"
                          required
                        />
                        <button 
                          v-if="question.options.length > 2"
                          @click="removeOption(question, optIndex)"
                          class="remove-option-btn"
                        >
                          <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                            <path d="M19,6.41L17.59,5L12,10.59L6.41,5L5,6.41L10.59,12L5,17.59L6.41,19L12,13.41L17.59,19L19,17.59L13.41,12L19,6.41Z" />
                          </svg>
                        </button>
                      </div>
                    </div>
                    <button @click="addOption(question)" class="add-option-btn">
                      Add Option
                    </button>
                  </div>

                  <!-- True/False Answer -->
                  <div v-else-if="question.question_type === 'true_false'" class="answer-section">
                    <label>Correct Answer *</label>
                    <select v-model="question.answer.correct_answer" required>
                      <option value="true">True</option>
                      <option value="false">False</option>
                    </select>
                  </div>

                  <!-- Fill in the Blank Answer -->
                  <div v-else-if="question.question_type === 'fill_blank'" class="answer-section">
                    <div class="form-group">
                      <label>Correct Answer *</label>
                      <input 
                        type="text" 
                        v-model="question.answer.correct_answer" 
                        placeholder="Enter the correct answer"
                        required
                      />
                    </div>
                    <div class="form-group checkbox-group">
                      <label>
                        <input type="checkbox" v-model="question.answer.case_sensitive" />
                        <span>Case Sensitive</span>
                      </label>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Save Button (Bottom) -->
        <div class="form-actions">
          <button @click="goBack" class="cancel-btn">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M10 19l-7-7 7-7m-7 7h18"></path>
            </svg>
            Cancel
          </button>
          <button @click="saveQuiz" :disabled="isSaving" class="save-btn-large">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M15,9H5V5H15M12,19A3,3 0 0,1 9,16A3,3 0 0,1 12,13A3,3 0 0,1 15,16A3,3 0 0,1 12,19M17,3H5C3.89,3 3,3.9 3,5V19A2,2 0 0,0 5,21H19A2,2 0 0,0 21,19V7L17,3Z" />
            </svg>
            {{ isSaving ? 'Saving Changes...' : 'Save All Changes' }}
          </button>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { supabase } from '../../supabase.js'
import { useDarkMode } from '../../composables/useDarkMode.js'
import { useTeacherAuth } from '../../composables/useTeacherAuth.js'

// Dark mode
const { isDarkMode, initDarkMode } = useDarkMode()

// Teacher auth
const { teacherInfo, initializeAuth } = useTeacherAuth()

const router = useRouter()
const route = useRoute()

// Get quiz ID and route params from query
const quizId = ref(route.params.quizId)
const subjectId = ref(route.query.subjectId)
const sectionId = ref(route.query.sectionId)
const subjectName = ref(route.query.subjectName)
const sectionName = ref(route.query.sectionName)
const gradeLevel = ref(route.query.gradeLevel)
const sectionCode = ref(route.query.sectionCode)

// State
const quiz = ref({
  title: '',
  description: '',
  status: 'draft',
  has_time_limit: false,
  time_limit_minutes: null,
  attempts_allowed: 1,
  shuffle_questions: false,
  shuffle_options: false,
  start_date: null,
  end_date: null,
  quiz_code: ''
})

const questions = ref([])
const isLoading = ref(false)
const isSaving = ref(false)
const error = ref(null)
const fullName = ref('Teacher')

// TIMEZONE UTILITY FUNCTIONS - Matching CreateQuiz.vue exactly
const formatPHTime = (utcDateString) => {
  if (!utcDateString) return 'Not set';
  try {
    const utcDate = new Date(utcDateString);
    const options = {
      year: 'numeric',
      month: 'short',
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit',
      timeZone: 'Asia/Manila',
      hour12: true
    };
    return utcDate.toLocaleString('en-PH', options) + ' PHT';
  } catch (error) {
    console.error('Error formatting PH time:', error);
    return 'Invalid date';
  }
};

const convertPHTimeToUTC = (phDateString) => {
  if (!phDateString) return null;
  try {
    // The datetime-local input gives us local time without timezone info
    // We need to interpret this as Philippines time and convert to UTC
    const localDate = new Date(phDateString);
    
    // Get the timezone offset for Philippines (should be -480 minutes for UTC+8)
    const phOffset = -8 * 60; // UTC+8 = -480 minutes
    const localOffset = localDate.getTimezoneOffset(); // Browser's timezone offset
    
    // Calculate the difference between local timezone and Philippines timezone
    const offsetDiff = localOffset - phOffset;
    
    // Adjust the date to treat the input as Philippines time
    const utcTime = new Date(localDate.getTime() + (offsetDiff * 60 * 1000));
    
    console.log('🕐 Converting PH to UTC:');
    console.log('  Input PH time:', phDateString);
    console.log('  Local offset:', localOffset);
    console.log('  PH offset:', phOffset);
    console.log('  Offset diff:', offsetDiff);
    console.log('  Result UTC:', utcTime.toISOString());
    
    return utcTime.toISOString();
  } catch (error) {
    console.error('Error converting PH time to UTC:', error);
    return null;
  }
};

const convertUTCtoPHForInput = (utcDateString) => {
  if (!utcDateString) return '';
  try {
    const utcDate = new Date(utcDateString);
    
    // Convert UTC to Philippines time for the datetime-local input
    const phTime = new Intl.DateTimeFormat('sv-SE', {
      timeZone: 'Asia/Manila',
      year: 'numeric',
      month: '2-digit',
      day: '2-digit',
      hour: '2-digit',
      minute: '2-digit'
    }).format(utcDate).replace(' ', 'T');
    
    console.log('🕐 Converting UTC to PH input:');
    console.log('  UTC input:', utcDateString);
    console.log('  PH output:', phTime);
    
    return phTime;
  } catch (error) {
    console.error('Error converting UTC to PH for input:', error);
    return '';
  }
};

const debugTimeConversion = () => {
  const now = new Date();
  console.log('🕐 EDITQUIZ TIMEZONE DEBUG:');
  console.log('Browser timezone offset (minutes):', now.getTimezoneOffset());
  console.log('Current local time:', now.toString());
  console.log('Current UTC time:', now.toISOString());
  console.log('Formatted as PH time:', formatPHTime(now.toISOString()));
};

// Load quiz data - REAL-TIME, NO TIMEOUTS
const loadQuiz = async () => {
  isLoading.value = true
  error.value = null
  
  try {
  console.log('Loading quiz:', quizId.value)
    
    // Fetch quiz details
    const { data: quizData, error: quizError } = await supabase
      .from('quizzes')
      .select('*')
      .eq('id', quizId.value)
      .single()
    
    if (quizError) {
  console.error('Quiz fetch error:', quizError)
      throw quizError
    }

  console.log('Quiz data loaded:', quizData)
    
    // FIXED: Use proper timezone conversion for datetime-local inputs
    quiz.value = {
      ...quizData,
      start_date: quizData.start_date ? convertUTCtoPHForInput(quizData.start_date) : null,
      end_date: quizData.end_date ? convertUTCtoPHForInput(quizData.end_date) : null
    }
    
    // Fetch questions
  console.log('Loading questions for quiz:', quizId.value)
    const { data: questionsData, error: questionsError } = await supabase
      .from('quiz_questions')
      .select('*')
      .eq('quiz_id', quizId.value)
      .order('question_number')
    
    if (questionsError) {
      console.error('❌ Questions fetch error:', questionsError)
      throw questionsError
    }

    console.log('✅ Questions loaded:', questionsData?.length || 0)
    
    // Load options and answers for each question
    for (const question of questionsData || []) {
      if (question.question_type === 'multiple_choice') {
        console.log('Loading options for question:', question.id)
        const { data: options, error: optionsError } = await supabase
          .from('question_options')
          .select('*')
          .eq('question_id', question.id)
          .order('option_number')
        
        if (optionsError) {
          console.error('❌ Options fetch error:', optionsError)
          throw optionsError
        }
        
        question.options = options || []
  console.log('Options loaded:', options?.length || 0)
      } else {
  console.log('Loading answer for question:', question.id)
        const { data: answer, error: answerError } = await supabase
          .from('question_answers')
          .select('*')
          .eq('question_id', question.id)
          .single()
        
        if (!answerError && answer) {
          question.answer = answer
          console.log('Answer loaded')
        } else {
          question.answer = {
            correct_answer: question.question_type === 'true_false' ? 'true' : '',
            case_sensitive: false
          }
          console.log('No answer found, using default')
        }
      }
    }
    
    questions.value = questionsData || []
  console.log('All quiz data loaded successfully')
    
  } catch (err) {
  console.error('Error loading quiz:', err)
    error.value = err.message
  } finally {
    isLoading.value = false
  console.log('Load quiz completed')
  }
}



// Question management
const addQuestion = () => {
  console.log('Adding new question')
  questions.value.push({
    question_number: questions.value.length + 1,
    question_type: 'multiple_choice',
    question_text: '',
    points: 1,
    options: [
      { option_number: 1, option_text: '', is_correct: true },
      { option_number: 2, option_text: '', is_correct: false }
    ]
  })
}

const removeQuestion = (index) => {
  if (confirm('Are you sure you want to remove this question?')) {
  console.log('Removing question:', index + 1)
    questions.value.splice(index, 1)
    // Renumber questions
    questions.value.forEach((q, i) => {
      q.question_number = i + 1
    })
  console.log('Question removed and renumbered')
  }
}

const onQuestionTypeChange = (question) => {
  console.log('Question type changed to:', question.question_type)
  if (question.question_type === 'multiple_choice') {
    question.options = [
      { option_number: 1, option_text: '', is_correct: true },
      { option_number: 2, option_text: '', is_correct: false }
    ]
    delete question.answer
  } else {
    question.answer = {
      correct_answer: question.question_type === 'true_false' ? 'true' : '',
      case_sensitive: false
    }
    delete question.options
  }
}

const addOption = (question) => {
  console.log('Adding option to question')
  const optionNumber = question.options.length + 1
  question.options.push({
    option_number: optionNumber,
    option_text: '',
    is_correct: false
  })
}

const removeOption = (question, index) => {
  console.log('Removing option:', index + 1)
  question.options.splice(index, 1)
  // Renumber options
  question.options.forEach((opt, i) => {
    opt.option_number = i + 1
  })
}

const setCorrectOption = (question, index) => {
  console.log('Setting correct option:', index + 1)
  question.options.forEach((opt, i) => {
    opt.is_correct = i === index
  })
}

// Save quiz - REAL-TIME, NO TIMEOUTS
const saveQuiz = async () => {
  console.log('Starting save quiz process...')
  
  // Validation
  if (!quiz.value.title.trim()) {
    alert('Please enter a quiz title')
    return
  }
  
  if (questions.value.length === 0) {
    alert('Please add at least one question')
    return
  }
  
  // Validate questions
  for (let i = 0; i < questions.value.length; i++) {
    const q = questions.value[i]
    
    if (!q.question_text.trim()) {
      alert(`Please enter text for question ${i + 1}`)
      return
    }
    
    if (q.question_type === 'multiple_choice') {
      if (!q.options || q.options.length < 2) {
        alert(`Question ${i + 1} must have at least 2 options`)
        return
      }
      
      if (!q.options.some(opt => opt.is_correct)) {
        alert(`Please select a correct answer for question ${i + 1}`)
        return
      }
      
      if (q.options.some(opt => !opt.option_text.trim())) {
        alert(`Please fill in all options for question ${i + 1}`)
        return
      }
    } else if (q.question_type === 'fill_blank' || q.question_type === 'true_false') {
      if (!q.answer || !q.answer.correct_answer) {
        alert(`Please provide a correct answer for question ${i + 1}`)
        return
      }
    }
  }
  
  isSaving.value = true
  
  try {
    // Step 1: Update quiz settings
  console.log('Updating quiz settings...')
    
    // Convert dates to UTC for storage
    const startDateUTC = convertPHTimeToUTC(quiz.value.start_date);
    const endDateUTC = convertPHTimeToUTC(quiz.value.end_date);
    
    // Debug timezone conversion during save
    console.log('🕐 EDIT SAVE TIMEZONE DEBUG:');
    console.log('Original start date input:', quiz.value.start_date);
    console.log('Converted start date UTC:', startDateUTC);
    console.log('Formatted back to PH:', formatPHTime(startDateUTC));
    console.log('Original end date input:', quiz.value.end_date);
    console.log('Converted end date UTC:', endDateUTC);
    console.log('Formatted back to PH:', formatPHTime(endDateUTC));
    
    const { error: quizError } = await supabase
      .from('quizzes')
      .update({
        title: quiz.value.title,
        description: quiz.value.description,
        status: quiz.value.status,
        has_time_limit: quiz.value.has_time_limit,
        time_limit_minutes: quiz.value.has_time_limit ? quiz.value.time_limit_minutes : null,
        attempts_allowed: quiz.value.attempts_allowed,
        shuffle_questions: quiz.value.shuffle_questions,
        shuffle_options: quiz.value.shuffle_options,
        start_date: startDateUTC,
        end_date: endDateUTC,
        number_of_questions: questions.value.length,
        updated_at: new Date().toISOString()
      })
      .eq('id', quizId.value)
    
    if (quizError) {
      console.error('❌ Quiz update error:', quizError)
      throw quizError
    }
    
  console.log('Quiz settings updated')
    
    // Step 2: Get all existing question IDs
  console.log('Fetching existing questions...')
    const { data: existingQuestions, error: fetchError } = await supabase
      .from('quiz_questions')
      .select('id')
      .eq('quiz_id', quizId.value)
    
    if (fetchError) {
      console.error('❌ Fetch questions error:', fetchError)
      throw fetchError
    }
    
    // Step 3: Delete old questions (cascade to options and answers)
    if (existingQuestions && existingQuestions.length > 0) {
  console.log(`Deleting ${existingQuestions.length} existing questions...`)
      const questionIds = existingQuestions.map(q => q.id)
      
      const { error: deleteError } = await supabase
        .from('quiz_questions')
        .delete()
        .in('id', questionIds)
      
      if (deleteError) {
        console.error('❌ Delete questions error:', deleteError)
        throw deleteError
      }
      
  console.log('Old questions deleted')
    }
    
    // Step 4: Insert new questions with their options/answers
  console.log(`Inserting ${questions.value.length} new questions...`)
    
    for (let i = 0; i < questions.value.length; i++) {
      const question = questions.value[i]
  console.log(`Processing question ${i + 1}...`)
      
      // Insert question
      const { data: insertedQuestion, error: questionError } = await supabase
        .from('quiz_questions')
        .insert({
          quiz_id: quizId.value,
          question_number: question.question_number,
          question_type: question.question_type,
          question_text: question.question_text,
          points: question.points
        })
        .select()
        .single()
      
      if (questionError) {
        console.error(`❌ Question ${i + 1} insert error:`, questionError)
        throw new Error(`Failed to save question ${i + 1}: ${questionError.message}`)
      }
      
  console.log(`Question ${i + 1} inserted:`, insertedQuestion.id)
      
      // Insert options or answers
      if (question.question_type === 'multiple_choice') {
  console.log(`Inserting ${question.options.length} options...`)
        
        const optionsToInsert = question.options.map(opt => ({
          question_id: insertedQuestion.id,
          option_number: opt.option_number,
          option_text: opt.option_text,
          is_correct: opt.is_correct
        }))
        
        const { error: optionsError } = await supabase
          .from('question_options')
          .insert(optionsToInsert)
        
        if (optionsError) {
          console.error(`❌ Options insert error for question ${i + 1}:`, optionsError)
          throw new Error(`Failed to save options for question ${i + 1}: ${optionsError.message}`)
        }
        
  console.log(`Options inserted for question ${i + 1}`)
      } else {
  console.log(`Inserting answer for question ${i + 1}...`)
        
        const { error: answerError } = await supabase
          .from('question_answers')
          .insert({
            question_id: insertedQuestion.id,
            correct_answer: question.answer.correct_answer,
            case_sensitive: question.answer.case_sensitive || false
          })
        
        if (answerError) {
          console.error(`❌ Answer insert error for question ${i + 1}:`, answerError)
          throw new Error(`Failed to save answer for question ${i + 1}: ${answerError.message}`)
        }
        
  console.log(`Answer inserted for question ${i + 1}`)
      }
    }
    
  console.log('All questions saved successfully!')
    alert('Quiz updated successfully!')
    goBack()
    
  } catch (err) {
    console.error('❌ Error saving quiz:', err)
    alert(`Error saving quiz: ${err.message || 'Unknown error occurred'}`)
  } finally {
    isSaving.value = false
  console.log('Save quiz completed')
  }
}

const goBack = () => {
  console.log('Navigating back to quiz management')
  router.push({
    name: 'ViewQuizzes',
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
}

// Lifecycle
onMounted(async () => {
  console.log('EditQuiz component mounted')
  initDarkMode()
  
  // Initialize auth and load teacher name
  try {
    await initializeAuth()
    
    // Load teacher name
    if (teacherInfo.value?.id) {
      try {
        const { data: teacher, error: teacherError } = await supabase
          .from('teachers')
          .select('full_name')
          .eq('id', teacherInfo.value.id)
          .single()
        
        if (!teacherError && teacher) {
          fullName.value = teacher.full_name || 'Teacher'
          console.log('✅ Teacher loaded:', { id: teacherInfo.value.id, name: fullName.value })
        }
      } catch (err) {
        console.warn('⚠️ Failed to load teacher name:', err)
        // Continue anyway - name is not critical
      }
    }
  } catch (err) {
    console.warn('⚠️ Auth initialization warning:', err)
  }
  
  // Debug timezone conversion
  debugTimeConversion();
  
  if (!quizId.value) {
    console.error('❌ Quiz ID is missing')
    error.value = 'Quiz ID is missing'
    return
  }
  
  await loadQuiz()
  console.log('Component initialization complete')
})
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

/* Reset and Base */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.dashboard-container {
  min-height: 100vh;
  background: #f8fafc;
  font-family: 'Inter', sans-serif;
  padding-left: 80px;
  padding-top: 64px;
}

/* Top Navigation Bar */
.top-navbar {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  height: 64px;
  background: linear-gradient(135deg, #3D8D7A, #2d6a5a);
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  z-index: 1000;
  box-shadow: 0 2px 8px rgba(61, 141, 122, 0.15);
}

.navbar-content {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 100%;
  max-width: 100%;
  margin: 0 auto;
  padding: 0 2rem;
}

.navbar-left {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.brand-logo {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  color: white;
  font-weight: 700;
  text-decoration: none;
}

.logo-img {
  width: 40px;
  height: 40px;
  object-fit: contain;
  filter: brightness(0) invert(1);
}

.brand-name {
  font-size: 1.5rem;
  font-weight: 800;
  color: white;
  letter-spacing: -0.5px;
}

.navbar-center {
  flex: 1;
}

.navbar-right {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.user-profile-wrapper {
  position: relative;
}

.user-profile {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  background: rgba(255, 255, 255, 0.1);
  padding: 0.625rem 1.25rem;
  border-radius: 50px;
  cursor: pointer;
  transition: all 0.2s;
}

.user-profile:hover {
  background: rgba(255, 255, 255, 0.2);
}

.user-avatar {
  width: 32px;
  height: 32px;
  background: rgba(255, 255, 255, 0.2);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
}

.user-name {
  color: white;
  font-weight: 600;
  font-size: 0.875rem;
}

/* Sidebar Navigation */
.sidebar {
  position: fixed;
  left: 0;
  top: 64px;
  bottom: 0;
  width: 80px;
  background: #3D8D7A;
  z-index: 999;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 1.5rem 0;
}

.sidebar-nav {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
  width: 100%;
  align-items: center;
}

.sidebar-item {
  position: relative;
  width: 56px;
  height: 56px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 12px;
  transition: all 0.2s;
  cursor: pointer;
  text-decoration: none;
}

.sidebar-item:hover {
  background: rgba(255, 255, 255, 0.1);
}

.sidebar-item.active {
  background: rgba(255, 255, 255, 0.2);
}

.sidebar-icon {
  display: flex;
  align-items: center;
  justify-content: center;
}

.sidebar-tooltip {
  position: absolute;
  left: 100%;
  margin-left: 1rem;
  background: #23272b;
  color: white;
  padding: 0.5rem 1rem;
  border-radius: 6px;
  font-size: 0.875rem;
  font-weight: 500;
  white-space: nowrap;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.2s;
  z-index: 1000;
}

.sidebar-item:hover .sidebar-tooltip {
  opacity: 1;
}

.rounded-bg {
  border-radius: 12px;
}

/* Main Content */
.main-content {
  padding: 2rem;
  max-width: 1400px;
  margin: 0 auto;
}

/* Page Header */
.subjects-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
  flex-wrap: wrap;
  gap: 1.5rem;
}

.header-left {
  display: flex;
  align-items: center;
  gap: 1.25rem;
}

.header-icon-wrapper {
  display: flex;
  align-items: center;
  justify-content: center;
}

.header-icon {
  width: 64px;
  height: 64px;
  background: linear-gradient(135deg, #3D8D7A, #2d6a5a);
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  box-shadow: 0 4px 12px rgba(61, 141, 122, 0.25);
}

.subjects-header h1 {
  font-size: 2rem;
  font-weight: 800;
  color: #1e293b;
  margin-bottom: 0.25rem;
}

.subjects-header p {
  color: #64748b;
  font-size: 1rem;
  font-weight: 500;
}

.header-right {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.create-subject-btn {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  background: #3D8D7A;
  color: white;
  border: none;
  padding: 0.875rem 1.75rem;
  border-radius: 12px;
  font-size: 0.9375rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
  box-shadow: 0 2px 8px rgba(61, 141, 122, 0.2);
}

.create-subject-btn:hover:not(:disabled) {
  background: #2d6a5a;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(61, 141, 122, 0.3);
}

.create-subject-btn:disabled {
  opacity: 0.6;
  cursor: not-allowed;
  transform: none;
}

.create-subject-btn.secondary {
  background: transparent;
  color: #3D8D7A;
  border: 2px solid #3D8D7A;
}

.create-subject-btn.secondary:hover:not(:disabled) {
  background: rgba(61, 141, 122, 0.1);
  border-color: #2d6a5a;
  color: #2d6a5a;
}

/* Loading State */
.loading-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 4rem 2rem;
  text-align: center;
}

.loading-spinner {
  width: 48px;
  height: 48px;
  border: 4px solid #e2e8f0;
  border-top: 4px solid #3D8D7A;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin-bottom: 1rem;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

/* Empty State */
.empty-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 4rem 2rem;
  text-align: center;
  background: white;
  border-radius: 16px;
  border: 1px solid #e2e8f0;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
}

.dark .empty-state {
  background: #23272b;
  border-color: #374151;
}

.empty-icon {
  margin-bottom: 1.5rem;
  color: #94a3b8;
}

.empty-title {
  font-size: 1.5rem;
  font-weight: 600;
  color: #1e293b;
  margin-bottom: 0.5rem;
}

.dark .empty-title {
  color: #f1f5f9;
}

.empty-desc {
  color: #64748b;
  font-size: 1rem;
  margin-bottom: 1.5rem;
}

.dark .empty-desc {
  color: #94a3b8;
}

.create-quiz-btn {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  background: #3D8D7A;
  color: white;
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 10px;
  font-size: 0.9375rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
  box-shadow: 0 2px 8px rgba(61, 141, 122, 0.2);
}

.create-quiz-btn:hover {
  background: #2d6a5a;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(61, 141, 122, 0.3);
}

.dark .create-quiz-btn {
  background: #A3D1C6;
  color: #181c20;
}

.dark .create-quiz-btn:hover {
  background: #8ebfb3;
}

/* Form Cards */
.edit-form {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.form-card {
  background: white;
  border-radius: 16px;
  border: 1px solid #e2e8f0;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
  overflow: hidden;
}

.dark .form-card {
  background: #23272b;
  border-color: #374151;
}

.card-header {
  padding: 1.25rem 1.5rem;
  border-bottom: 1px solid #e2e8f0;
  background: #f8fafc;
}

.dark .card-header {
  background: #1e2329;
  border-bottom-color: #374151;
}

.card-header h3 {
  font-size: 1.125rem;
  font-weight: 600;
  color: #1e293b;
  margin: 0;
}

.dark .card-header h3 {
  color: #f1f5f9;
}

.card-body {
  padding: 1.5rem;
}

/* Form Elements */
.form-group {
  margin-bottom: 1.25rem;
}

.form-group:last-child {
  margin-bottom: 0;
}

.form-group label {
  display: block;
  font-size: 0.875rem;
  font-weight: 600;
  color: #374151;
  margin-bottom: 0.5rem;
}

.dark .form-group label {
  color: #e5e7eb;
}

.form-group input[type="text"],
.form-group input[type="number"],
.form-group input[type="datetime-local"],
.form-group select,
.form-group textarea {
  width: 100%;
  padding: 0.75rem 1rem;
  border: 1.5px solid #d1d5db;
  border-radius: 8px;
  font-size: 0.9375rem;
  color: #1f2937;
  background: white;
  transition: all 0.2s;
}

.dark .form-group input,
.dark .form-group select,
.dark .form-group textarea {
  background: #1e2329;
  border-color: #374151;
  color: #f1f5f9;
}

.form-group input:focus,
.form-group select:focus,
.form-group textarea:focus {
  outline: none;
  border-color: #3D8D7A;
  box-shadow: 0 0 0 3px rgba(61, 141, 122, 0.1);
}

.form-group small {
  display: block;
  margin-top: 0.375rem;
  font-size: 0.8125rem;
  color: #6b7280;
}

.dark .form-group small {
  color: #9ca3af;
}

.form-row {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.25rem;
  margin-bottom: 1.25rem;
}

.checkbox-group label {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  cursor: pointer;
  font-weight: 500;
}

.checkbox-group input[type="checkbox"] {
  width: auto;
  margin: 0;
  cursor: pointer;
}

/* Questions Section */
.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.add-question-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  background: #3D8D7A;
  color: white;
  border: none;
  padding: 0.625rem 1rem;
  border-radius: 8px;
  font-size: 0.875rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s;
}

.add-question-btn:hover {
  background: #2d6a5a;
  transform: translateY(-1px);
  box-shadow: 0 2px 8px rgba(61, 141, 122, 0.2);
}

.dark .add-question-btn {
  background: #A3D1C6;
  color: #181c20;
}

.dark .add-question-btn:hover {
  background: #8ebfb3;
}

.no-questions {
  text-align: center;
  padding: 3rem 1.5rem;
  color: #6b7280;
  font-size: 0.9375rem;
}

.dark .no-questions {
  color: #9ca3af;
}

.questions-list {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.question-item {
  background: #f8fafc;
  border: 1.5px solid #e2e8f0;
  border-radius: 12px;
  padding: 1.25rem;
  transition: all 0.2s;
}

.dark .question-item {
  background: #1e2329;
  border-color: #374151;
}

.question-item:hover {
  border-color: #3D8D7A;
  box-shadow: 0 2px 8px rgba(61, 141, 122, 0.1);
}

.question-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
}

.question-number {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 36px;
  height: 36px;
  background: #3D8D7A;
  color: white;
  border-radius: 50%;
  font-weight: 700;
  font-size: 0.9375rem;
}

.dark .question-number {
  background: #A3D1C6;
  color: #181c20;
}

.delete-question-btn {
  background: #ef4444;
  color: white;
  border: none;
  padding: 0.5rem;
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.2s;
  display: flex;
  align-items: center;
  justify-content: center;
}

.delete-question-btn:hover {
  background: #dc2626;
  transform: scale(1.05);
}

.question-content {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.options-section,
.answer-section {
  margin-top: 0.5rem;
}

.options-list {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
  margin-bottom: 0.75rem;
}

.option-item {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.option-item input[type="radio"] {
  width: auto;
  margin: 0;
  cursor: pointer;
}

.option-item input[type="text"] {
  flex: 1;
  padding: 0.625rem 0.875rem;
  border: 1.5px solid #d1d5db;
  border-radius: 6px;
  font-size: 0.875rem;
}

.dark .option-item input[type="text"] {
  background: #23272b;
  border-color: #374151;
  color: #f1f5f9;
}

.remove-option-btn {
  background: transparent;
  color: #ef4444;
  border: none;
  padding: 0.375rem;
  cursor: pointer;
  border-radius: 4px;
  transition: all 0.2s;
}

.remove-option-btn:hover {
  background: rgba(239, 68, 68, 0.1);
  transform: scale(1.1);
}

.add-option-btn {
  background: transparent;
  color: #3D8D7A;
  border: 1.5px dashed #3D8D7A;
  padding: 0.625rem 1rem;
  border-radius: 6px;
  font-size: 0.875rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s;
}

.add-option-btn:hover {
  background: rgba(61, 141, 122, 0.05);
  border-style: solid;
}

.dark .add-option-btn {
  color: #A3D1C6;
  border-color: #A3D1C6;
}

.dark .add-option-btn:hover {
  background: rgba(163, 209, 198, 0.1);
}

/* Main Content */
.main-wrapper {
  margin-top: 2rem;
}

/* States - Matching MySubjects Style */
.loading-state, .error-state {
  background: white;
  border: 1.5px solid #e5e7eb;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.04);
  padding: 2.5rem 1.5rem;
  margin: 2rem auto;
  max-width: 480px;
  text-align: center;
  color: #1f2937;
  transition: all 0.18s ease;
}
.dark-mode .loading-state,
.dark-mode .error-state {
  background: #23272b;
  border: 1.5px solid #374151;
  color: #A3D1C6;
  box-shadow: 0 2px 8px rgba(32, 201, 151, 0.13);
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

@keyframes spin {
  to { transform: rotate(360deg); }
}

.error-icon {
  color: #ef4444;
  margin-bottom: 1rem;
  display: flex;
  justify-content: center;
}

.error-state h3 {
  color: #1f2937;
  font-size: 1.25rem;
  font-weight: 700;
  margin-bottom: 0.5rem;
  line-height: 1.3;
}
.dark-mode .error-state h3 {
  color: #f9fafb;
}

.error-state p {
  color: #10b981;
  margin-bottom: 1.5rem;
  font-size: 0.95rem;
  font-weight: 600;
}
.dark-mode .error-state p {
  color: #34d399;
}

.retry-btn {
  background: #20c997;
  color: #181c20;
  border: 1px solid #A3D1C6;
  padding: 0.5rem 1.25rem;
  border-radius: 8px;
  font-size: 0.875rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  outline: none;
}
.retry-btn:hover {
  background: #A3D1C6;
  color: #23272b;
  border-color: #20c997;
  transform: translateY(-1px);
}
.dark-mode .retry-btn {
  background: #20c997;
  color: #181c20;
  border: 1px solid #A3D1C6;
}
.dark-mode .retry-btn:hover {
  background: #A3D1C6;
  color: #23272b;
  border-color: #20c997;
}

/* Form Cards - Enhanced Design */
.edit-form {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.form-card {
  background: white;
  border: 1.5px solid #e5e7eb;
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0,0,0,0.04);
  transition: all 0.18s ease;
}
.dark-mode .form-card {
  background: #23272b;
  border: 1.5px solid #374151;
  box-shadow: 0 2px 8px rgba(32, 201, 151, 0.13);
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.5rem;
  background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
  border-bottom: 1px solid #e2e8f0;
}
.dark-mode .card-header {
  background: #1f2937;
  border-bottom: 1px solid #374151;
}

.card-header h3 {
  color: #1f2937;
  font-size: 1.25rem;
  font-weight: 700;
  margin: 0;
}
.dark-mode .card-header h3 {
  color: #f9fafb;
}

.add-question-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  background: #20c997;
  color: #181c20;
  border: 1px solid #A3D1C6;
  padding: 0.5rem 1rem;
  border-radius: 8px;
  font-weight: 500;
  font-size: 0.875rem;
  cursor: pointer;
  transition: all 0.2s;
  outline: none;
}

.add-question-btn:hover {
  background: #A3D1C6;
  color: #23272b;
  border-color: #20c997;
  transform: translateY(-1px);
}
.dark-mode .add-question-btn {
  background: #20c997;
  color: #181c20;
  border: 1px solid #A3D1C6;
}
.dark-mode .add-question-btn:hover {
  background: #A3D1C6;
  color: #23272b;
  border-color: #20c997;
}

.card-body {
  padding: 1.5rem;
}

/* Form Groups */
.form-group {
  margin-bottom: 1.5rem;
}

.form-group label {
  display: block;
  font-weight: 600;
  color: #374151;
  margin-bottom: 0.5rem;
  font-size: 0.875rem;
}

.form-group input[type="text"],
.form-group input[type="number"],
.form-group input[type="datetime-local"],
.form-group textarea,
.form-group select {
  width: 100%;
  padding: 0.75rem;
  border: 2px solid #A3D1C6;
  border-radius: 8px;
  font-size: 0.875rem;
  transition: all 0.2s;
  background: #FBFFE4;
}

.form-group input:focus,
.form-group textarea:focus,
.form-group select:focus {
  outline: none;
  border-color: #3D8D7A;
  box-shadow: 0 0 0 3px rgba(61, 141, 122, 0.1);
}

.form-group small {
  display: block;
  margin-top: 0.25rem;
  font-size: 0.75rem;
  color: #6b7280;
}

.form-row {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1rem;
}

.checkbox-group label {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  cursor: pointer;
  font-weight: 500;
}

.checkbox-group input[type="checkbox"] {
  width: auto;
  cursor: pointer;
}

/* Questions List - Enhanced Organization */
.no-questions {
  text-align: center;
  padding: 2rem;
  color: #6b7280;
}
.dark-mode .no-questions {
  color: #9ca3af;
}

.questions-list {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.question-item {
  background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
  border: 1.5px solid #e5e7eb;
  border-radius: 12px;
  padding: 1.5rem;
  transition: all 0.2s;
}

.question-item:hover {
  border-color: #10b981;
  box-shadow: 0 4px 12px rgba(16, 185, 129, 0.08);
  background: linear-gradient(135deg, #f0fdfa 0%, #ecfdf5 100%);
}

.dark-mode .question-item {
  background: #1f2937;
  border-color: #374151;
}

.dark-mode .question-item:hover {
  border-color: #20c997;
  background: #1f2937;
}

.question-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
  padding-bottom: 1rem;
  border-bottom: 2px solid #e2e8f0;
}
.dark-mode .question-header {
  border-bottom-color: #374151;
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
  font-weight: 700;
  font-size: 1rem;
}
.dark-mode .question-number {
  background: #A3D1C6;
  color: #23272b;
}

.delete-question-btn {
  background: #ef4444;
  color: white;
  border: none;
  padding: 0.5rem;
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.2s;
  display: flex;
  align-items: center;
  justify-content: center;
}

.delete-question-btn:hover {
  background: #dc2626;
}

.question-content {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

/* Options Section */
.options-section {
  margin-top: 1rem;
}

.options-section > label {
  display: block;
  font-weight: 600;
  color: #374151;
  margin-bottom: 0.75rem;
  font-size: 0.875rem;
}

.options-list {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
  margin-bottom: 0.75rem;
}

.option-item {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  background: white;
  padding: 0.75rem;
  border: 2px solid #e5e7eb;
  border-radius: 8px;
}
.dark-mode .option-item {
  background: #23272b;
  border-color: #4b5563;
}

.option-item input[type="radio"] {
  cursor: pointer;
  width: auto;
}

.option-item input[type="text"] {
  flex: 1;
  padding: 0.5rem;
  border: 1px solid #d1d5db;
  border-radius: 6px;
  font-size: 0.875rem;
  background: #f8f9fa;
}

.option-item input[type="text"]:focus {
  outline: none;
  border-color: #10b981;
  box-shadow: 0 0 0 2px rgba(16, 185, 129, 0.1);
}

.dark-mode .option-item input[type="text"] {
  background: #374151;
  border-color: #4b5563;
  color: #e5e7eb;
}

.remove-option-btn {
  background: #ef4444;
  color: white;
  border: none;
  padding: 0.5rem;
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.2s;
  display: flex;
  align-items: center;
  justify-content: center;
}

.remove-option-btn:hover {
  background: #dc2626;
}

.add-option-btn {
  background: #B3D8A8;
  color: #3D8D7A;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 6px;
  font-weight: 600;
  font-size: 0.875rem;
  cursor: pointer;
  transition: all 0.2s;
}

.add-option-btn:hover {
  background: #a0c995;
}

/* Answer Section */
.answer-section {
  margin-top: 1rem;
}

.answer-section label {
  display: block;
  font-weight: 600;
  color: #374151;
  margin-bottom: 0.5rem;
  font-size: 0.875rem;
}

.answer-section select,
.answer-section input[type="text"] {
  width: 100%;
  padding: 0.75rem;
  border: 2px solid #A3D1C6;
  border-radius: 8px;
  font-size: 0.875rem;
  background: white;
}

.answer-section select:focus,
.answer-section input[type="text"]:focus {
  outline: none;
  border-color: #3D8D7A;
  box-shadow: 0 0 0 3px rgba(61, 141, 122, 0.1);
}

/* Form Actions */
.form-actions {
  display: flex;
  gap: 1rem;
  justify-content: center;
  padding: 2rem 0;
}

.cancel-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  background: white;
  color: #374151;
  border: 1px solid #d1d5db;
  padding: 0.75rem 2rem;
  border-radius: 8px;
  font-weight: 500;
  font-size: 0.875rem;
  cursor: pointer;
  transition: all 0.2s;
  outline: none;
}

.cancel-btn:hover {
  background: #f3f4f6;
  border-color: #9ca3af;
}

.save-btn-large {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  background: #3D8D7A;
  color: white;
  border: none;
  padding: 0.75rem 3rem;
  border-radius: 8px;
  font-weight: 700;
  font-size: 1rem;
  cursor: pointer;
  transition: all 0.2s;
  box-shadow: 0 2px 8px rgba(61, 141, 122, 0.2);
}

.save-btn-large:hover:not(:disabled) {
  background: #2d6a5a;
  box-shadow: 0 4px 12px rgba(61, 141, 122, 0.3);
  transform: translateY(-1px);
}

.save-btn-large:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

/* Responsive Design for Navbar */
@media (max-width: 1200px) {
  .main-content {
    padding: 1.5rem;
  }
}

@media (max-width: 1024px) {
  .main-content {
    padding: 1rem;
  }
  
  .navbar-center {
    gap: 0.25rem;
  }
  
  .nav-item {
    padding: 0.5rem 1rem;
    font-size: 0.7rem;
  }
}

@media (max-width: 768px) {
  .main-content {
    padding: 1rem;
  }
  
  .page-header {
    padding: 1rem;
    margin-bottom: 1.5rem;
  }
  
  .section-header-content {
    flex-direction: column;
    gap: 1rem;
    align-items: stretch;
  }
  
  .navbar-content {
    padding: 0 0.5rem;
  }
  
  .brand-name {
    display: none;
  }
  
  .export-btn span {
    display: none;
  }
  
  .header-actions {
    flex-direction: column;
  }
  
  .form-row {
    grid-template-columns: 1fr;
  }
  
  .option-item {
    flex-wrap: wrap;
  }
  
  .form-actions {
    flex-direction: column;
    align-items: center;
  }
  
  .save-btn-large {
    width: 100%;
    justify-content: center;
  }

  .section-header-icon {
    width: 48px;
    height: 48px;
  }
  
  .section-header-title {
    font-size: 1.25rem;
  }
}

/* Custom Scrollbar Styling - Green Theme */
::-webkit-scrollbar {
  width: 8px;
  height: 8px;
}

::-webkit-scrollbar-track {
  background: #f1f5f9;
  border-radius: 10px;
}

::-webkit-scrollbar-thumb {
  background: linear-gradient(135deg, #3D8D7A, #20c997);
  border-radius: 10px;
  border: 1px solid #e2e8f0;
  transition: all 0.3s ease;
}

::-webkit-scrollbar-thumb:hover {
  background: linear-gradient(135deg, #2d6a5a, #18a577);
  box-shadow: 0 2px 8px rgba(61, 141, 122, 0.3);
}

::-webkit-scrollbar-thumb:active {
  background: linear-gradient(135deg, #1e5a4a, #146e5a);
}

::-webkit-scrollbar-corner {
  background: #f1f5f9;
}

/* Firefox Scrollbar */
* {
  scrollbar-width: thin;
  scrollbar-color: #3D8D7A #f1f5f9;
}

/* Dark mode scrollbar */
.dark ::-webkit-scrollbar-track {
  background: #1a1d21;
}

.dark ::-webkit-scrollbar-thumb {
  background: linear-gradient(135deg, #20c997, #18a577);
  border: 1px solid #374151;
}

.dark ::-webkit-scrollbar-thumb:hover {
  background: linear-gradient(135deg, #18a577, #146e5a);
  box-shadow: 0 2px 8px rgba(32, 201, 151, 0.3);
}

.dark ::-webkit-scrollbar-corner {
  background: #1a1d21;
}

/* Main content scroll behavior */
.main-content {
  scroll-behavior: smooth;
  overflow-y: auto;
  overflow-x: hidden;
}

</style>