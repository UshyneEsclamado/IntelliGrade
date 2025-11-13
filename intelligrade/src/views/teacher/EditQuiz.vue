<template>
  <div class="edit-quiz-container" :class="{ 'dark-mode': isDarkMode }">
    <!-- Enhanced Header Section -->
    <div class="section-header-card">
      <div class="section-header-content">
        <div class="section-header-left">
          <div class="section-header-icon">
            <svg width="40" height="40" viewBox="0 0 24 24" fill="currentColor">
              <path d="M20.71,7.04C21.1,6.65 21.1,6 20.71,5.63L18.37,3.29C18,2.9 17.35,2.9 16.96,3.29L15.12,5.12L18.87,8.87M3,17.25V21H6.75L17.81,9.93L14.06,6.18L3,17.25Z" />
            </svg>
          </div>
          <div class="header-text">
            <div class="section-header-title">Edit Quiz</div>
            <div class="section-header-subtitle">{{ quiz.title || 'Loading...' }}</div>
            <div class="section-header-description" v-if="quiz.quiz_code">
              Quiz Code: <span class="code-highlight">{{ quiz.quiz_code }}</span>
            </div>
          </div>
        </div>
        
        <div class="header-actions">
          <button @click="saveQuiz" :disabled="isSaving" class="save-btn">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M15,9H5V5H15M12,19A3,3 0 0,1 9,16A3,3 0 0,1 12,13A3,3 0 0,1 15,16A3,3 0 0,1 12,19M17,3H5C3.89,3 3,3.9 3,5V19A2,2 0 0,0 5,21H19A2,2 0 0,0 21,19V7L17,3Z" />
            </svg>
            {{ isSaving ? 'Saving...' : 'Save Changes' }}
          </button>
          <button @click="goBack" class="back-button">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M10 19l-7-7 7-7m-7 7h18"></path>
            </svg>
            Back to Quiz Management
          </button>
        </div>
      </div>
    </div>

    <!-- Main Content -->
  <div class="main-wrapper">
      <!-- Loading State -->
      <div v-if="isLoading" class="loading-state">
        <div class="loading-spinner"></div>
        <p>Loading quiz...</p>
      </div>

      <!-- Error State -->
      <div v-else-if="error" class="error-state">
        <div class="error-icon">
          <svg width="48" height="48" viewBox="0 0 24 24" fill="currentColor">
            <path d="M11,15H13V17H11V15M11,7H13V13H11V7M12,2C6.47,2 2,6.5 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2M12,20A8,8 0 0,1 4,12A8,8 0 0,1 12,4A8,8 0 0,1 20,12A8,8 0 0,1 12,20Z" />
          </svg>
        </div>
        <h3>Error Loading Quiz</h3>
        <p>{{ error }}</p>
        <button @click="loadQuiz" class="retry-btn">Try Again</button>
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
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { supabase } from '../../supabase.js'
import { useDarkMode } from '../../composables/useDarkMode.js'

// Dark mode
const { isDarkMode, initDarkMode } = useDarkMode()

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
    
    // Format dates for datetime-local input
    quiz.value = {
      ...quizData,
      start_date: quizData.start_date ? formatDateForInput(quizData.start_date) : null,
      end_date: quizData.end_date ? formatDateForInput(quizData.end_date) : null
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

// Format date for datetime-local input
const formatDateForInput = (dateString) => {
  if (!dateString) return null
  const date = new Date(dateString)
  return date.toISOString().slice(0, 16)
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
        start_date: quiz.value.start_date || null,
        end_date: quiz.value.end_date || null,
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
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

* { margin: 0; padding: 0; box-sizing: border-box; }

.edit-quiz-container {
  min-height: 100vh;
  background: #FBFFE4;
  padding: 1.5rem;
  font-family: 'Inter', sans-serif;
}
.edit-quiz-container.dark-mode {
  background: #181c20;
}

/* Header Card - Matching MySubjects Style */
.section-header-card {
  background: white;
  border: 1.5px solid #3D8D7A;
  border-radius: 16px;
  padding: 1.5rem;
  margin-bottom: 1.5rem;
  box-shadow: 0 2px 8px rgba(61, 141, 122, 0.1);
}
.dark-mode .section-header-card {
  background: #23272b;
  border: 1.5px solid #A3D1C6;
  box-shadow: 0 2px 8px rgba(163, 209, 198, 0.1);
}

.section-header-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.section-header-left {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.section-header-icon {
  width: 56px;
  height: 56px;
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
  font-size: 1.5rem;
  font-weight: 700;
  color: #1f2937;
  margin: 0 0 0.25rem 0;
  line-height: 1.3;
}
.dark-mode .section-header-title {
  color: #f9fafb;
}

.section-header-subtitle {
  font-size: 0.875rem;
  color: #6b7280;
  margin: 0;
}
.dark-mode .section-header-subtitle {
  color: #A3D1C6;
}

.section-header-description {
  font-size: 0.75rem;
  color: #9ca3af;
}
.dark-mode .section-header-description {
  color: #9ca3af;
}

.code-highlight {
  font-family: 'Courier New', monospace;
  font-weight: 700;
  color: #3b82f6;
  background: rgba(59, 130, 246, 0.1);
  padding: 0.25rem 0.5rem;
  border-radius: 4px;
}

.header-actions {
  display: flex;
  gap: 0.75rem;
}

.save-btn, .back-button {
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

.save-btn:hover:not(:disabled) {
  background: #A3D1C6;
  color: #23272b;
  border-color: #20c997;
  transform: translateY(-1px);
}

.save-btn:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.back-button:hover {
  background: #A3D1C6;
  color: #23272b;
  border-color: #20c997;
  transform: translateY(-1px);
}

.dark-mode .save-btn,
.dark-mode .back-button {
  background: #20c997;
  color: #181c20;
  border: 1px solid #A3D1C6;
}

.dark-mode .save-btn:hover:not(:disabled),
.dark-mode .back-button:hover {
  background: #A3D1C6;
  color: #23272b;
  border-color: #20c997;
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

/* Responsive Design */
@media (max-width: 768px) {
  .edit-quiz-container {
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
</style>