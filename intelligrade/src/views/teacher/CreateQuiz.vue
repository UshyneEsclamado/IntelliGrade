<template>
  <div class="create-quiz-page">
    <!-- Header Section -->
    <div class="page-header">
      <div class="header-container">
        <div class="header-content">
          <div class="subject-info">
            <div class="subject-icon">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                <path d="M14,2H6A2,2 0 0,0 4,4V20A2,2 0 0,0 6,22H18A2,2 0 0,0 20,20V8L14,2M18,20H6V4H13V9H18V20Z" />
              </svg>
            </div>
            <div class="subject-details">
              <h1>{{ subject.name }}</h1>
              <p>{{ subject.teacher }}</p>
            </div>
          </div>
          <button @click="goBack" class="back-btn">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M20,11V13H8L13.5,18.5L12.08,19.92L4.16,12L12.08,4.08L13.5,5.5L8,11H20Z" />
            </svg>
            Back
          </button>
        </div>
      </div>
    </div>

    <!-- Progress Steps -->
    <div v-if="currentStep !== 'landing'" class="progress-container">
      <div class="progress-card">
        <div class="progress-track">
          <div v-for="(step, index) in steps" :key="index" class="progress-step">
            <div class="step-indicator" :class="{ 
              'active': getStepIndex(currentStep) >= index,
              'completed': getStepIndex(currentStep) > index 
            }">
              <span v-if="getStepIndex(currentStep) > index" class="checkmark">✓</span>
              <span v-else class="step-number">{{ index + 1 }}</span>
            </div>
            <span class="step-label">{{ step }}</span>
            <div v-if="index < steps.length - 1" class="step-connector" :class="{ 'completed': getStepIndex(currentStep) > index }"></div>
          </div>
        </div>
      </div>
    </div>

    <!-- Main Content -->
    <div class="main-content">
      <!-- Landing State -->
      <div v-if="currentStep === 'landing'" class="landing-section">
        <div class="landing-card">
          <div class="landing-icon">
            <svg width="64" height="64" viewBox="0 0 24 24" fill="currentColor">
              <path d="M14,2H6A2,2 0 0,0 4,4V20A2,2 0 0,0 6,22H18A2,2 0 0,0 20,20V8L14,2M18,20H6V4H13V9H18V20Z" />
            </svg>
          </div>
          <h2>Create a New Quiz</h2>
          <p>Design an engaging quiz experience for your students with our intuitive quiz builder</p>
          <button @click="currentStep = 'details'" class="start-btn">
            <span>Start Creating</span>
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M13 7l5 5m0 0l-5 5m5-5H6"/>
            </svg>
          </button>
        </div>
      </div>

      <!-- Quiz Details -->
      <div v-if="currentStep === 'details'" class="content-card slide-up">
        <div class="section-header">
          <div class="section-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
              <path d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
            </svg>
          </div>
          <h2 class="section-title">Quiz Details</h2>
        </div>
        
        <div class="form-section">
          <div class="form-group">
            <label class="form-label">Quiz Title *</label>
            <input v-model="quiz.title" type="text" placeholder="e.g., English Quiz 1" class="form-input" />
          </div>

          <div class="form-group">
            <label class="form-label">Description / Instructions</label>
            <textarea v-model="quiz.description" rows="4" placeholder="Add instructions or context for this quiz..." class="form-input form-textarea"></textarea>
          </div>

          <div class="form-group">
            <label class="form-label">Number of Questions *</label>
            <input v-model.number="quiz.numberOfQuestions" type="number" min="1" placeholder="e.g., 10" class="form-input" />
          </div>

          <div class="action-buttons">
            <button @click="currentStep = 'landing'" class="btn btn-secondary">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                <path d="M15 19l-7-7 7-7"/>
              </svg>
              Back
            </button>
            <button @click="proceedToQuestions" class="btn btn-primary flex-1">
              Continue to Questions
              <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                <path d="M13 7l5 5m0 0l-5 5m5-5H6"/>
              </svg>
            </button>
          </div>
        </div>
      </div>

      <!-- Add Questions -->
      <div v-if="currentStep === 'questions'" class="content-card slide-up">
        <div class="section-header">
          <div class="section-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
              <path d="M8.228 9c.549-1.165 2.03-2 3.772-2 2.21 0 4 1.343 4 3 0 1.4-1.278 2.575-3.006 2.907-.542.104-.994.54-.994 1.093m0 3h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
            </svg>
          </div>
          <div>
            <h2 class="section-title">Build Your Questions</h2>
            <div class="question-counter">
              {{ quiz.questions.length }} / {{ quiz.numberOfQuestions }}
            </div>
          </div>
        </div>

        <!-- Question Cards -->
        <div class="questions-container">
          <div v-for="(question, index) in quiz.questions" :key="index" class="question-card">
            <div class="question-header">
              <div class="question-number">
                <div class="question-badge">{{ index + 1 }}</div>
                <h3 class="question-title">Question {{ index + 1 }}</h3>
              </div>
              <button @click="removeQuestion(index)" class="btn btn-danger">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"/>
                </svg>
              </button>
            </div>

            <div class="question-content">
              <div class="form-group">
                <label class="form-label">Question Type</label>
                <select v-model="question.type" class="form-input form-select">
                  <option value="multiple_choice">Multiple Choice</option>
                  <option value="true_false">True/False</option>
                  <option value="fill_blank">Fill in the Blanks</option>
                </select>
              </div>

              <div class="form-group">
                <label class="form-label">Question Text</label>
                <textarea v-model="question.text" rows="3" placeholder="Enter your question here..." class="form-input form-textarea"></textarea>
              </div>

              <!-- Multiple Choice Options -->
              <div v-if="question.type === 'multiple_choice'" class="option-group">
                <label class="form-label">Answer Options</label>
                <div v-for="(option, optIndex) in question.options" :key="optIndex" class="option-item">
                  <input 
                    type="radio" 
                    :name="'correct-' + index" 
                    :checked="question.correctAnswer === optIndex" 
                    @change="question.correctAnswer = optIndex" 
                    class="option-radio"
                  />
                  <input 
                    v-model="question.options[optIndex]" 
                    type="text" 
                    :placeholder="'Option ' + (optIndex + 1)" 
                    class="option-input"
                  />
                  <button v-if="question.options.length > 2" @click="removeOption(index, optIndex)" class="remove-option-btn">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                      <path d="M6 18L18 6M6 6l12 12"/>
                    </svg>
                  </button>
                </div>
                <button @click="addOption(index)" class="btn btn-success">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M12 6v6m0 0v6m0-6h6m-6 0H6"/>
                  </svg>
                  Add Option
                </button>
              </div>

              <!-- True/False Options -->
              <div v-if="question.type === 'true_false'" class="option-group">
                <label class="form-label">Correct Answer</label>
                <div class="tf-options">
                  <label class="tf-option" :class="question.correctAnswer === 'true' ? 'selected' : ''">
                    <input type="radio" v-model="question.correctAnswer" value="true" class="hidden" />
                    <div class="tf-icon">✅</div>
                    <div class="tf-label">True</div>
                  </label>
                  <label class="tf-option" :class="question.correctAnswer === 'false' ? 'selected' : ''">
                    <input type="radio" v-model="question.correctAnswer" value="false" class="hidden" />
                    <div class="tf-icon">❌</div>
                    <div class="tf-label">False</div>
                  </label>
                </div>
              </div>

              <!-- Fill in the Blanks -->
              <div v-if="question.type === 'fill_blank'" class="form-group">
                <label class="form-label">Correct Answer (exact match)</label>
                <input v-model="question.correctAnswer" type="text" placeholder="Enter the correct answer..." class="form-input" />
              </div>
            </div>
          </div>
        </div>

        <!-- Action Buttons -->
        <div class="action-buttons">
          <button v-if="quiz.questions.length < quiz.numberOfQuestions" @click="addQuestion" class="btn btn-success">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M12 6v6m0 0v6m0-6h6m-6 0H6"/>
            </svg>
            Add Another Question
          </button>
          <button @click="currentStep = 'details'" class="btn btn-secondary">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M15 19l-7-7 7-7"/>
            </svg>
            Back
          </button>
          <button v-if="quiz.questions.length > 0" @click="currentStep = 'settings'" class="btn btn-primary flex-1">
            Continue to Settings
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M13 7l5 5m0 0l-5 5m5-5H6"/>
            </svg>
          </button>
        </div>
      </div>

      <!-- Quiz Settings -->
      <div v-if="currentStep === 'settings'" class="glass-card p-8 slide-up">
        <div class="flex items-center mb-8">
          <div class="w-14 h-14 bg-gradient-to-br from-purple-500 to-pink-600 rounded-xl flex items-center justify-center mr-4 shadow-lg">
            <svg class="w-7 h-7 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"/>
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/>
            </svg>
          </div>
          <h2 class="text-2xl font-bold text-gray-800">Quiz Settings</h2>
        </div>

        <div class="space-y-6">
          <!-- Time Limit -->
          <div class="setting-card">
            <div class="flex items-center justify-between">
              <div class="flex items-center">
                <span class="text-3xl mr-4">⏱</span>
                <div>
                  <h3 class="font-bold text-gray-800">Time Limit</h3>
                  <p class="text-sm text-gray-600">Set a time constraint for this quiz</p>
                </div>
              </div>
              <label class="toggle-switch">
                <input v-model="quiz.settings.hasTimeLimit" type="checkbox" />
                <span class="toggle-slider"></span>
              </label>
            </div>
            <div v-if="quiz.settings.hasTimeLimit" class="mt-4">
              <input v-model.number="quiz.settings.timeLimit" type="number" min="1" placeholder="Minutes" class="input-field" />
            </div>
          </div>

          <!-- Attempts Allowed -->
          <div class="setting-card">
            <div class="flex items-center mb-4">
              <span class="text-3xl mr-4">🔁</span>
              <div>
                <h3 class="font-bold text-gray-800">Attempts Allowed</h3>
                <p class="text-sm text-gray-600">How many times can students retake this quiz?</p>
              </div>
            </div>
            <input v-model.number="quiz.settings.attemptsAllowed" type="number" min="1" placeholder="e.g., 1, 2, or unlimited" class="input-field" />
          </div>

          <!-- Shuffle -->
          <div class="setting-card">
            <div class="flex items-center justify-between">
              <div class="flex items-center">
                <span class="text-3xl mr-4">🔀</span>
                <div>
                  <h3 class="font-bold text-gray-800">Shuffle Questions/Options</h3>
                  <p class="text-sm text-gray-600">Randomize question and answer order</p>
                </div>
              </div>
              <label class="toggle-switch">
                <input v-model="quiz.settings.shuffle" type="checkbox" />
                <span class="toggle-slider"></span>
              </label>
            </div>
          </div>

          <!-- Schedule -->
          <div class="setting-card">
            <div class="flex items-center mb-4">
              <span class="text-3xl mr-4">📅</span>
              <div>
                <h3 class="font-bold text-gray-800">Schedule</h3>
                <p class="text-sm text-gray-600">Set when students can access this quiz</p>
              </div>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div class="input-group">
                <label class="input-label-small">Start Date & Time</label>
                <input v-model="quiz.settings.startDate" type="datetime-local" class="input-field" />
              </div>
              <div class="input-group">
                <label class="input-label-small">End Date & Time</label>
                <input v-model="quiz.settings.endDate" type="datetime-local" class="input-field" />
              </div>
            </div>
          </div>

          <div class="flex gap-3 pt-4">
            <button @click="currentStep = 'questions'" class="btn-secondary">
              <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"/>
              </svg>
              Back
            </button>
            <button @click="currentStep = 'preview'" class="btn-primary flex-1">
              Preview Quiz
              <svg class="w-5 h-5 ml-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/>
              </svg>
            </button>
          </div>
        </div>
      </div>

      <!-- Preview -->
      <div v-if="currentStep === 'preview'" class="space-y-6 slide-up">
        <div class="glass-card p-8">
          <div class="text-center mb-10">
            <div class="inline-block px-6 py-2 bg-gradient-to-r from-green-500 to-emerald-600 text-white rounded-full font-bold mb-4 shadow-lg">
              PREVIEW MODE
            </div>
            <h2 class="text-3xl font-bold bg-gradient-to-r from-indigo-600 to-purple-600 bg-clip-text text-transparent mb-3">
              {{ quiz.title }}
            </h2>
            <p class="text-gray-600 mb-6">{{ quiz.description }}</p>
            <div class="flex justify-center gap-8 text-sm">
              <div class="stat-badge">
                <span class="text-2xl">⏱</span>
                <span v-if="quiz.settings.hasTimeLimit">{{ quiz.settings.timeLimit }} min</span>
                <span v-else>No limit</span>
              </div>
              <div class="stat-badge">
                <span class="text-2xl">📝</span>
                <span>{{ quiz.questions.length }} questions</span>
              </div>
              <div class="stat-badge">
                <span class="text-2xl">🔁</span>
                <span>{{ quiz.settings.attemptsAllowed }} attempt(s)</span>
              </div>
            </div>
          </div>

          <div class="space-y-5">
            <div v-for="(question, index) in quiz.questions" :key="index" class="preview-card">
              <div class="flex items-start mb-4">
                <div class="w-8 h-8 bg-gradient-to-br from-indigo-500 to-purple-600 rounded-lg flex items-center justify-center mr-3 flex-shrink-0">
                  <span class="text-white font-bold text-sm">{{ index + 1 }}</span>
                </div>
                <h3 class="font-semibold text-gray-800 text-lg">{{ question.text }}</h3>
              </div>
              
              <!-- MCQ Preview -->
              <div v-if="question.type === 'multiple_choice'" class="space-y-3 ml-11">
                <div v-for="(option, optIndex) in question.options" :key="optIndex" 
                     :class="['preview-option', question.correctAnswer === optIndex ? 'correct-option' : '']">
                  <input type="radio" disabled class="mr-3" />
                  <span>{{ option }}</span>
                  <span v-if="question.correctAnswer === optIndex" class="ml-auto text-green-600 font-bold">✓</span>
                </div>
              </div>

              <!-- True/False Preview -->
              <div v-if="question.type === 'true_false'" class="space-y-3 ml-11">
                <div :class="['preview-option', question.correctAnswer === 'true' ? 'correct-option' : '']">
                  <input type="radio" disabled class="mr-3" />
                  <span>True</span>
                  <span v-if="question.correctAnswer === 'true'" class="ml-auto text-green-600 font-bold">✓</span>
                </div>
                <div :class="['preview-option', question.correctAnswer === 'false' ? 'correct-option' : '']">
                  <input type="radio" disabled class="mr-3" />
                  <span>False</span>
                  <span v-if="question.correctAnswer === 'false'" class="ml-auto text-green-600 font-bold">✓</span>
                </div>
              </div>

              <!-- Fill Blank Preview -->
              <div v-if="question.type === 'fill_blank'" class="ml-11">
                <input type="text" disabled placeholder="Student answer here..." class="input-field bg-gray-50" />
                <p class="text-sm text-green-600 mt-3 font-semibold">✓ Correct Answer: {{ question.correctAnswer }}</p>
              </div>
            </div>
          </div>

          <div class="flex gap-3 pt-8">
            <button @click="currentStep = 'settings'" class="btn-secondary">
              <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 17l-5-5m0 0l5-5m-5 5h12"/>
              </svg>
              Edit Quiz
            </button>
            <button @click="publishQuiz" class="btn-publish flex-1">
              <svg class="w-6 h-6 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
              </svg>
              Publish Quiz Now
              <svg class="w-5 h-5 ml-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 10l7-7m0 0l7 7m-7-7v18"/>
              </svg>
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'CreateQuiz',
  data() {
    return {
      currentStep: 'landing',
      steps: ['Details', 'Questions', 'Settings', 'Preview'],
      subject: {
        name: 'English A1',
        teacher: 'Ms. Cruz'
      },
      quiz: {
        title: '',
        description: '',
        numberOfQuestions: null,
        questions: [],
        settings: {
          hasTimeLimit: false,
          timeLimit: 30,
          attemptsAllowed: 1,
          shuffle: false,
          startDate: '',
          endDate: ''
        }
      }
    };
  },
  methods: {
    goBack() {
      // Navigate back to previous page or teacher dashboard
      this.$router.go(-1) || this.$router.push('/teacher');
    },
    getStepIndex(step) {
      const stepMap = {
        'landing': -1,
        'details': 0,
        'questions': 1,
        'settings': 2,
        'preview': 3
      };
      return stepMap[step];
    },
    proceedToQuestions() {
      if (!this.quiz.title || !this.quiz.numberOfQuestions) {
        alert('Please fill in all required fields');
        return;
      }
      this.currentStep = 'questions';
    },
    addQuestion() {
      if (this.quiz.questions.length >= this.quiz.numberOfQuestions) {
        return;
      }
      this.quiz.questions.push({
        type: 'multiple_choice',
        text: '',
        options: ['', '', '', ''],
        correctAnswer: null
      });
    },
    removeQuestion(index) {
      this.quiz.questions.splice(index, 1);
    },
    addOption(questionIndex) {
      this.quiz.questions[questionIndex].options.push('');
    },
    removeOption(questionIndex, optionIndex) {
      this.quiz.questions[questionIndex].options.splice(optionIndex, 1);
    },
    async publishQuiz() {
      try {
        // TODO: Integrate with Supabase
        console.log('Publishing quiz:', this.quiz);
        
        // Show success animation
        alert('🎉 Quiz published successfully! Students can now take this quiz.');
        
        // Reset form or redirect
        // this.$router.push('/quiz-management');
      } catch (error) {
        console.error('Error publishing quiz:', error);
        alert('Error publishing quiz. Please try again.');
      }
    }
  }
};
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
}

/* Base Styles */
.create-quiz-page {
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

.subject-info {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.subject-icon {
  width: 48px;
  height: 48px;
  background: linear-gradient(135deg, var(--primary-green), var(--mint-green));
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--white);
}

.subject-details h1 {
  font-size: 1.875rem;
  font-weight: 700;
  color: var(--gray-800);
  margin: 0;
}

.subject-details p {
  color: var(--gray-600);
  margin: 0.25rem 0 0 0;
  font-size: 0.95rem;
}

.back-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1.5rem;
  background: var(--gray-100);
  color: var(--gray-600);
  border: 1px solid var(--gray-300);
  border-radius: 10px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s ease;
}

.back-btn:hover {
  background: var(--gray-200);
  color: var(--gray-700);
  transform: translateY(-1px);
}

/* Progress Section */
.progress-container {
  max-width: 1200px;
  margin: 2rem auto;
  padding: 0 2rem;
}

.progress-card {
  background: var(--white);
  border-radius: 16px;
  padding: 2rem;
  box-shadow: var(--shadow-md);
  border: 1px solid rgba(61, 141, 122, 0.1);
}

.progress-track {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 2rem;
}

.progress-step {
  display: flex;
  flex-direction: column;
  align-items: center;
  position: relative;
}

.step-indicator {
  width: 48px;
  height: 48px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 600;
  transition: all 0.3s ease;
  background: var(--gray-200);
  color: var(--gray-500);
  border: 3px solid var(--gray-200);
}

.step-indicator.active,
.step-indicator.completed {
  background: linear-gradient(135deg, var(--primary-green), var(--mint-green));
  color: var(--white);
  border-color: var(--primary-green);
  transform: scale(1.05);
  box-shadow: 0 4px 12px rgba(61, 141, 122, 0.3);
}

.step-label {
  margin-top: 0.75rem;
  font-size: 0.875rem;
  font-weight: 500;
  color: var(--gray-600);
}

.step-indicator.active + .step-label,
.step-indicator.completed + .step-label {
  color: var(--primary-green);
  font-weight: 600;
}

.step-connector {
  position: absolute;
  top: 24px;
  left: 48px;
  width: 2rem;
  height: 3px;
  background: var(--gray-200);
  transition: all 0.3s ease;
}

.step-connector.completed {
  background: linear-gradient(to right, var(--primary-green), var(--mint-green));
}

/* Main Content */
.main-content {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem 2rem;
}

/* Landing Section */
.landing-section {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 60vh;
}

.landing-card {
  background: var(--white);
  border-radius: 24px;
  padding: 4rem 3rem;
  text-align: center;
  box-shadow: var(--shadow-xl);
  border: 1px solid rgba(61, 141, 122, 0.1);
  max-width: 600px;
  width: 100%;
}

.landing-icon {
  width: 80px;
  height: 80px;
  background: linear-gradient(135deg, var(--primary-green), var(--mint-green));
  border-radius: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 2rem;
  color: var(--white);
}

.landing-card h2 {
  font-size: 2.25rem;
  font-weight: 700;
  color: var(--gray-800);
  margin-bottom: 1rem;
}

.landing-card p {
  font-size: 1.125rem;
  color: var(--gray-600);
  margin-bottom: 2.5rem;
  line-height: 1.6;
}

.start-btn {
  display: inline-flex;
  align-items: center;
  gap: 0.75rem;
  padding: 1rem 2.5rem;
  background: linear-gradient(135deg, var(--primary-green), var(--mint-green));
  color: var(--white);
  border: none;
  border-radius: 14px;
  font-weight: 600;
  font-size: 1.1rem;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 4px 12px rgba(61, 141, 122, 0.3);
}

.start-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 20px rgba(61, 141, 122, 0.4);
}

/* Card Styles */
.content-card {
  background: var(--white);
  border-radius: 20px;
  padding: 2.5rem;
  box-shadow: var(--shadow-lg);
  border: 1px solid rgba(61, 141, 122, 0.1);
  margin-bottom: 2rem;
}

/* Form Styles */
.form-section {
  margin-bottom: 2rem;
}

.section-header {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 2rem;
  padding-bottom: 1rem;
  border-bottom: 2px solid var(--gray-100);
}

.section-icon {
  width: 48px;
  height: 48px;
  background: linear-gradient(135deg, var(--primary-green), var(--mint-green));
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--white);
}

.section-title {
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--gray-800);
  margin: 0;
}

.form-group {
  margin-bottom: 1.5rem;
}

.form-label {
  display: block;
  font-weight: 600;
  color: var(--gray-700);
  margin-bottom: 0.5rem;
  font-size: 0.95rem;
}

.form-input {
  width: 100%;
  padding: 0.875rem 1rem;
  border: 2px solid var(--gray-200);
  border-radius: 10px;
  font-size: 0.95rem;
  transition: all 0.3s ease;
  background: var(--white);
}

.form-input:focus {
  outline: none;
  border-color: var(--primary-green);
  box-shadow: 0 0 0 3px rgba(61, 141, 122, 0.1);
}

.form-textarea {
  resize: vertical;
  min-height: 100px;
}

.form-select {
  appearance: none;
  background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' fill='none' viewBox='0 0 20 20'%3e%3cpath stroke='%236b7280' stroke-linecap='round' stroke-linejoin='round' stroke-width='1.5' d='m6 8 4 4 4-4'/%3e%3c/svg%3e");
  background-position: right 0.5rem center;
  background-repeat: no-repeat;
  background-size: 1.5em 1.5em;
  padding-right: 2.5rem;
}

/* Button Styles */
.btn {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.875rem 1.5rem;
  border-radius: 10px;
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

.btn-success {
  background: linear-gradient(135deg, var(--light-green), var(--mint-green));
  color: var(--primary-green);
  border: 2px solid var(--light-green);
}

.btn-success:hover {
  background: var(--light-green);
  transform: translateY(-1px);
}

.btn-danger {
  background: #fee2e2;
  color: #dc2626;
  border: 2px solid #fecaca;
}

.btn-danger:hover {
  background: #fecaca;
}

/* Question Card */
.question-card {
  background: var(--white);
  border: 2px solid var(--gray-200);
  border-radius: 16px;
  padding: 1.5rem;
  margin-bottom: 1.5rem;
  transition: all 0.3s ease;
}

.question-card:hover {
  border-color: var(--mint-green);
  box-shadow: 0 4px 12px rgba(163, 209, 198, 0.2);
}

.question-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1.5rem;
  padding-bottom: 1rem;
  border-bottom: 1px solid var(--gray-200);
}

.question-number {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.question-badge {
  width: 36px;
  height: 36px;
  background: linear-gradient(135deg, var(--primary-green), var(--mint-green));
  color: var(--white);
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 0.9rem;
}

.question-title {
  font-size: 1.125rem;
  font-weight: 600;
  color: var(--gray-800);
  margin: 0;
}

/* Options */
.option-group {
  margin-top: 1rem;
}

.option-item {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.75rem;
  border: 2px solid var(--gray-200);
  border-radius: 10px;
  margin-bottom: 0.75rem;
  transition: all 0.3s ease;
}

.option-item:hover {
  border-color: var(--mint-green);
  background: rgba(163, 209, 198, 0.05);
}

.option-radio {
  width: 20px;
  height: 20px;
  accent-color: var(--primary-green);
}

.option-input {
  flex: 1;
  border: none;
  background: transparent;
  font-size: 0.95rem;
  padding: 0.25rem;
}

.option-input:focus {
  outline: none;
}

.remove-option-btn {
  width: 32px;
  height: 32px;
  background: #fee2e2;
  color: #dc2626;
  border: none;
  border-radius: 6px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.3s ease;
}

.remove-option-btn:hover {
  background: #fecaca;
  transform: scale(1.05);
}

/* True/False Options */
.tf-options {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
  margin-top: 1rem;
}

.tf-option {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 1.5rem;
  border: 3px solid var(--gray-200);
  border-radius: 16px;
  cursor: pointer;
  transition: all 0.3s ease;
  background: var(--white);
}

.tf-option:hover {
  border-color: var(--mint-green);
  background: rgba(163, 209, 198, 0.05);
}

.tf-option.selected {
  border-color: var(--primary-green);
  background: rgba(61, 141, 122, 0.05);
}

.tf-icon {
  font-size: 2rem;
  margin-bottom: 0.5rem;
}

.tf-label {
  font-weight: 600;
  color: var(--gray-700);
}

/* Settings Card */
.setting-item {
  background: var(--white);
  border: 2px solid var(--gray-200);
  border-radius: 16px;
  padding: 1.5rem;
  margin-bottom: 1rem;
  transition: all 0.3s ease;
}

.setting-item:hover {
  border-color: var(--mint-green);
}

.setting-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
}

.setting-info {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.setting-emoji {
  font-size: 2rem;
}

.setting-details h3 {
  font-size: 1.125rem;
  font-weight: 600;
  color: var(--gray-800);
  margin: 0 0 0.25rem 0;
}

.setting-details p {
  font-size: 0.875rem;
  color: var(--gray-600);
  margin: 0;
}

/* Toggle Switch */
.toggle-switch {
  position: relative;
  display: inline-block;
  width: 56px;
  height: 32px;
}

.toggle-switch input {
  opacity: 0;
  width: 0;
  height: 0;
}

.toggle-slider {
  position: absolute;
  cursor: pointer;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: var(--gray-300);
  border-radius: 34px;
  transition: 0.4s;
}

.toggle-slider:before {
  position: absolute;
  content: "";
  height: 24px;
  width: 24px;
  left: 4px;
  bottom: 4px;
  background: var(--white);
  border-radius: 50%;
  transition: 0.4s;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
}

.toggle-switch input:checked + .toggle-slider {
  background: var(--primary-green);
}

.toggle-switch input:checked + .toggle-slider:before {
  transform: translateX(24px);
}

/* Preview Styles */
.preview-card {
  background: var(--white);
  border: 2px solid var(--gray-200);
  border-radius: 16px;
  padding: 1.5rem;
  margin-bottom: 1rem;
}

.preview-option {
  display: flex;
  align-items: center;
  padding: 0.75rem;
  background: var(--gray-50);
  border: 1px solid var(--gray-200);
  border-radius: 8px;
  margin-bottom: 0.5rem;
}

.preview-option.correct {
  background: rgba(179, 216, 168, 0.2);
  border-color: var(--light-green);
}

/* Action Buttons */
.action-buttons {
  display: flex;
  gap: 1rem;
  margin-top: 2rem;
  padding-top: 2rem;
  border-top: 2px solid var(--gray-100);
}

/* Responsive Design */
@media (max-width: 768px) {
  .create-quiz-page {
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
  
  .progress-container {
    padding: 0 1rem;
  }
  
  .progress-track {
    flex-direction: column;
    gap: 1rem;
  }
  
  .step-connector {
    display: none;
  }
  
  .main-content {
    padding: 0 1rem 2rem;
  }
  
  .landing-card {
    padding: 2rem 1.5rem;
  }
  
  .content-card {
    padding: 1.5rem;
  }
  
  .tf-options {
    grid-template-columns: 1fr;
  }
  
  .action-buttons {
    flex-direction: column;
  }
  
  .btn {
    justify-content: center;
  }
}

/* Animation */
@keyframes slideUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.slide-up {
  animation: slideUp 0.5s ease-out;
}

/* Question Styles */
.questions-container {
  margin-bottom: 2rem;
}

.question-counter {
  background: linear-gradient(135deg, var(--primary-green), var(--mint-green));
  color: var(--white);
  padding: 0.5rem 1rem;
  border-radius: 12px;
  font-weight: 700;
  font-size: 0.9rem;
  margin-left: auto;
}

.question-content {
  padding-top: 1rem;
}

/* Delete Button */
.delete-btn {
  width: 36px;
  height: 36px;
  background: #fee2e2;
  color: #dc2626;
  border: none;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.3s ease;
}

.delete-btn:hover {
  background: #fecaca;
  transform: scale(1.1);
}

/* Input Field Styles */
.input-field {
  width: 100%;
  padding: 0.875rem 1rem;
  border: 2px solid var(--gray-200);
  border-radius: 10px;
  font-size: 0.95rem;
  transition: all 0.3s ease;
  background: var(--white);
}

.input-field:focus {
  outline: none;
  border-color: var(--primary-green);
  box-shadow: 0 0 0 3px rgba(61, 141, 122, 0.1);
}

/* Publish Button */
.btn-publish {
  background: linear-gradient(135deg, #10b981 0%, #059669 100%);
  color: var(--white);
  padding: 1rem 2.5rem;
  font-size: 1.1rem;
  font-weight: 700;
  box-shadow: 0 8px 25px rgba(16, 185, 129, 0.5);
}

.btn-publish:hover {
  transform: translateY(-2px) scale(1.02);
  box-shadow: 0 12px 35px rgba(16, 185, 129, 0.7);
}

/* Add Option Button */
.btn-add-option {
  background: rgba(163, 209, 198, 0.2);
  color: var(--primary-green);
  border: 2px dashed var(--primary-green);
  padding: 0.625rem 1rem;
  font-size: 0.875rem;
  border-radius: 8px;
  margin-top: 0.75rem;
}

.btn-add-option:hover {
  background: rgba(163, 209, 198, 0.3);
  transform: translateY(-1px);
}

/* Setting Card */
.setting-card {
  background: var(--white);
  border: 2px solid var(--gray-200);
  border-radius: 16px;
  padding: 1.5rem;
  margin-bottom: 1rem;
  transition: all 0.3s ease;
}

.setting-card:hover {
  border-color: var(--mint-green);
  box-shadow: 0 4px 12px rgba(163, 209, 198, 0.2);
}

/* Stat Badge */
.stat-badge {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.5rem;
  padding: 1rem 1.5rem;
  background: linear-gradient(135deg, rgba(163, 209, 198, 0.2) 0%, rgba(179, 216, 168, 0.2) 100%);
  border: 1px solid var(--mint-green);
  border-radius: 12px;
  font-weight: 600;
  color: var(--primary-green);
}

/* Utilities */
.flex-1 {
  flex: 1;
}

.text-center {
  text-align: center;
}

.hidden {
  display: none;
}

.grid-cols-2 {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1rem;
}

/* Additional spacing utilities */
.space-y-6 > * + * {
  margin-top: 1.5rem;
}

.space-y-5 > * + * {
  margin-top: 1.25rem;
}

.space-y-3 > * + * {
  margin-top: 0.75rem;
}

.gap-3 {
  gap: 0.75rem;
}

.gap-4 {
  gap: 1rem;
}

.pt-4 {
  padding-top: 1rem;
}

.pt-8 {
  padding-top: 2rem;
}

.mb-4 {
  margin-bottom: 1rem;
}

.mb-6 {
  margin-bottom: 1.5rem;
}

.mb-8 {
  margin-bottom: 2rem;
}

.mb-10 {
  margin-bottom: 2.5rem;
}

.mt-3 {
  margin-top: 0.75rem;
}

.mt-4 {
  margin-top: 1rem;
}

.mr-2 {
  margin-right: 0.5rem;
}

.mr-3 {
  margin-right: 0.75rem;
}

.ml-2 {
  margin-left: 0.5rem;
}

.ml-11 {
  margin-left: 2.75rem;
}

.ml-auto {
  margin-left: auto;
}

.w-5 {
  width: 1.25rem;
}

.h-5 {
  height: 1.25rem;
}

.w-6 {
  width: 1.5rem;
}

.h-6 {
  height: 1.5rem;
}

.w-8 {
  width: 2rem;
}

.h-8 {
  height: 2rem;
}

.text-sm {
  font-size: 0.875rem;
}

.text-lg {
  font-size: 1.125rem;
}

.text-2xl {
  font-size: 1.5rem;
}

.text-3xl {
  font-size: 1.875rem;
}

.font-bold {
  font-weight: 700;
}

.font-semibold {
  font-weight: 600;
}

.text-white {
  color: var(--white);
}

.text-green-600 {
  color: #10b981;
}

.bg-gray-50 {
  background-color: var(--gray-50);
}

.inline-block {
  display: inline-block;
}

.inline-flex {
  display: inline-flex;
}

.items-center {
  align-items: center;
}

.items-start {
  align-items: flex-start;
}

.justify-center {
  justify-content: center;
}

.justify-between {
  justify-content: space-between;
}

.flex-col {
  flex-direction: column;
}

.flex-shrink-0 {
  flex-shrink: 0;
}

.bg-gradient-to-r {
  background: linear-gradient(to right, var(--primary-green), var(--mint-green));
}

.bg-gradient-to-br {
  background: linear-gradient(135deg, var(--primary-green), var(--mint-green));
}

.rounded-full {
  border-radius: 9999px;
}

.rounded-lg {
  border-radius: 0.5rem;
}

.rounded-xl {
  border-radius: 0.75rem;
}

.shadow-lg {
  box-shadow: var(--shadow-lg);
}

.px-6 {
  padding-left: 1.5rem;
  padding-right: 1.5rem;
}

.py-2 {
  padding-top: 0.5rem;
  padding-bottom: 0.5rem;
}

.py-3 {
  padding-top: 0.75rem;
  padding-bottom: 0.75rem;
}

.p-8 {
  padding: 2rem;
}

.disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.glass-card {
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(10px);
  border-radius: 20px;
  border: 1px solid rgba(61, 141, 122, 0.1);
  box-shadow: var(--shadow-lg);
}
</style>
