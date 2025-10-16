<template>
  <div class="create-quiz-page">
    <!-- Enhanced Header Section -->
    <div class="section-header-card">
      <div class="header-bg-decoration"></div>
      <div class="floating-shapes">
        <div class="shape shape-1"></div>
        <div class="shape shape-2"></div>
        <div class="shape shape-3"></div>
        <div class="shape shape-4"></div>
        <div class="shape shape-5"></div>
      </div>
      
      <div class="section-header-content">
        <div class="section-header-left">
          <div class="section-header-icon">
            <svg width="36" height="36" viewBox="0 0 24 24" fill="currentColor">
              <path d="M14,2H6A2,2 0 0,0 4,4V20A2,2 0 0,0 6,22H18A2,2 0 0,0 20,20V8L14,2M18,20H6V4H13V9H18V20Z" />
            </svg>
          </div>
          
          <div class="header-text">
            <h1 class="section-header-title">Create New Quiz</h1>
            <p class="section-header-subtitle">{{ subject.name }}<span v-if="section.name"> - {{ section.name }}</span></p>
            <p class="section-header-description">{{ teacherInfo.full_name }} • {{ teacherInfo.role.toUpperCase() }}</p>
          </div>
        </div>
        
        <div class="header-actions">
          <button @click="goBack" class="back-btn">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M20,11V13H8L13.5,18.5L12.08,19.92L4.16,12L12.08,4.08L13.5,5.5L8,11H20Z" />
            </svg>
            Back to Subjects
          </button>
        </div>
      </div>
    </div>

    <!-- Enhanced Progress Steps -->
    <div v-if="currentStep !== 'landing'" class="progress-container">
      <div class="progress-card">
        <div class="progress-track">
          <div v-for="(step, index) in steps" :key="index" class="progress-step">
            <div class="step-line" :class="{ 'completed': getStepIndex(currentStep) > index }"></div>
            <div class="step-indicator" :class="{ 
              'active': getStepIndex(currentStep) >= index,
              'completed': getStepIndex(currentStep) > index 
            }">
              <div class="step-circle">
                <span v-if="getStepIndex(currentStep) > index" class="checkmark">✓</span>
                <span v-else class="step-number">{{ index + 1 }}</span>
              </div>
            </div>
            <span class="step-label">{{ step }}</span>
          </div>
        </div>
      </div>
    </div>

    <!-- Main Content -->
    <div class="main-content">
      <!-- Landing State with Enhanced Design -->
      <div v-if="currentStep === 'landing'" class="landing-section">
        <div class="landing-card">
          <div class="landing-icon">
            <div class="icon-bg">
              <svg width="64" height="64" viewBox="0 0 24 24" fill="currentColor">
                <path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z"/>
              </svg>
            </div>
            <div class="icon-glow"></div>
          </div>
          <h2>Create a New Quiz</h2>
          <p>Design an engaging quiz experience for your students with our intuitive AI-powered quiz builder</p>
          <div class="features-preview">
            <div class="feature-item">
              <span class="feature-icon">🎯</span>
              <span>Smart Questions</span>
            </div>
            <div class="feature-item">
              <span class="feature-icon">⚡</span>
              <span>Instant Grading</span>
            </div>
            <div class="feature-item">
              <span class="feature-icon">📊</span>
              <span>Analytics</span>
            </div>
          </div>
          <button @click="currentStep = 'details'" class="create-quiz-btn">
            <span class="btn-content">
              <span>Start Creating</span>
              <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                <path d="M13 7l5 5m0 0l-5 5m5-5H6"/>
              </svg>
            </span>
            <div class="btn-bg"></div>
          </button>
        </div>
      </div>

      <!-- Quiz Details with Enhanced Design -->
      <div v-if="currentStep === 'details'" class="content-card slide-up">
        <div class="section-header">
          <div class="section-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
              <path d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
            </svg>
          </div>
          <div class="section-content">
            <h2 class="section-title">Quiz Details</h2>
            <p class="section-subtitle">Set up the basic information for your quiz</p>
          </div>
        </div>
        
        <div class="form-section">
          <div class="form-grid">
            <div class="form-group">
              <label class="form-label">
                <span class="label-icon">📝</span>
                Quiz Title *
              </label>
              <input v-model="quiz.title" type="text" placeholder="e.g., Biology Chapter 5 Quiz" class="form-input enhanced-input" />
            </div>

            <div class="form-group">
              <label class="form-label">
                <span class="label-icon">🔢</span>
                Number of Questions *
              </label>
              <input v-model.number="quiz.numberOfQuestions" type="number" min="1" max="50" placeholder="e.g., 10" class="form-input enhanced-input" />
            </div>
          </div>

          <div class="form-group">
            <label class="form-label">
              <span class="label-icon">📋</span>
              Description / Instructions
            </label>
            <textarea v-model="quiz.description" rows="4" placeholder="Add instructions or context for this quiz..." class="form-input form-textarea enhanced-input"></textarea>
          </div>

          <div class="action-buttons">
            <button @click="currentStep = 'landing'" class="btn btn-secondary">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                <path d="M15 19l-7-7 7-7"/>
              </svg>
              Back
            </button>
            <button @click="proceedToQuestions" class="btn btn-primary">
              Continue to Questions
              <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                <path d="M13 7l5 5m0 0l-5 5m5-5H6"/>
              </svg>
            </button>
          </div>
        </div>
      </div>

      <!-- Add Questions with Enhanced Design -->
      <div v-if="currentStep === 'questions'" class="content-card slide-up">
        <div class="section-header">
          <div class="section-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
              <path d="M8.228 9c.549-1.165 2.03-2 3.772-2 2.21 0 4 1.343 4 3 0 1.4-1.278 2.575-3.006 2.907-.542.104-.994.54-.994 1.093m0 3h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
            </svg>
          </div>
          <div class="section-content">
            <h2 class="section-title">Build Your Questions</h2>
            <div class="question-counter">
              <span class="counter-icon">🎯</span>
              {{ quiz.questions.length }} / {{ quiz.numberOfQuestions }}
            </div>
          </div>
        </div>

        <!-- Question Cards with Enhanced Design -->
        <div class="questions-container">
          <div v-for="(question, index) in quiz.questions" :key="index" class="question-card enhanced-card">
            <div class="question-header">
              <div class="question-number">
                <div class="question-badge">{{ index + 1 }}</div>
                <h3 class="question-title">Question {{ index + 1 }}</h3>
              </div>
              <button @click="removeQuestion(index)" class="btn btn-danger delete-btn">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"/>
                </svg>
              </button>
            </div>

            <div class="question-content">
              <div class="form-group">
                <label class="form-label">
                  <span class="label-icon">🔧</span>
                  Question Type
                </label>
                <select v-model="question.type" class="form-input form-select enhanced-input">
                  <option value="multiple_choice">📝 Multiple Choice</option>
                  <option value="true_false">✅ True/False</option>
                  <option value="fill_blank">📝 Fill in the Blanks</option>
                </select>
              </div>

              <div class="form-group">
                <label class="form-label">
                  <span class="label-icon">❓</span>
                  Question Text
                </label>
                <textarea v-model="question.text" rows="3" placeholder="Enter your question here..." class="form-input form-textarea enhanced-input"></textarea>
              </div>

              <!-- Multiple Choice Options with Enhanced Design -->
              <div v-if="question.type === 'multiple_choice'" class="option-group">
                <label class="form-label">
                  <span class="label-icon">📋</span>
                  Answer Options
                </label>
                <div class="options-container">
                  <div v-for="(option, optIndex) in question.options" :key="optIndex" class="option-item enhanced-option">
                    <input 
                      type="radio" 
                      :name="'correct-' + index" 
                      :checked="question.correctAnswer === optIndex" 
                      @change="question.correctAnswer = optIndex" 
                      class="option-radio"
                    />
                    <div class="option-letter">{{ String.fromCharCode(65 + optIndex) }}</div>
                    <input 
                      v-model="question.options[optIndex]" 
                      type="text" 
                      :placeholder="'Option ' + String.fromCharCode(65 + optIndex)" 
                      class="option-input"
                    />
                    <button v-if="question.options.length > 2" @click="removeOption(index, optIndex)" class="remove-option-btn">
                      <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                        <path d="M6 18L18 6M6 6l12 12"/>
                      </svg>
                    </button>
                  </div>
                </div>
                <button @click="addOption(index)" class="btn btn-success add-option-btn">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M12 6v6m0 0v6m0-6h6m-6 0H6"/>
                  </svg>
                  Add Option
                </button>
              </div>

              <!-- True/False Options with Enhanced Design -->
              <div v-if="question.type === 'true_false'" class="option-group">
                <label class="form-label">
                  <span class="label-icon">✅</span>
                  Correct Answer
                </label>
                <div class="tf-options">
                  <label class="tf-option" :class="question.correctAnswer === 'true' ? 'selected' : ''">
                    <input type="radio" v-model="question.correctAnswer" value="true" class="hidden" />
                    <div class="tf-content">
                      <div class="tf-icon">✅</div>
                      <div class="tf-label">True</div>
                    </div>
                  </label>
                  <label class="tf-option" :class="question.correctAnswer === 'false' ? 'selected' : ''">
                    <input type="radio" v-model="question.correctAnswer" value="false" class="hidden" />
                    <div class="tf-content">
                      <div class="tf-icon">❌</div>
                      <div class="tf-label">False</div>
                    </div>
                  </label>
                </div>
              </div>

              <!-- Fill in the Blanks with Enhanced Design -->
              <div v-if="question.type === 'fill_blank'" class="form-group">
                <label class="form-label">
                  <span class="label-icon">✏️</span>
                  Correct Answer (exact match)
                </label>
                <input v-model="question.correctAnswer" type="text" placeholder="Enter the correct answer..." class="form-input enhanced-input" />
              </div>
            </div>
          </div>

          <!-- Add Question Card -->
          <div v-if="quiz.questions.length < quiz.numberOfQuestions" class="add-question-card" @click="addQuestion">
            <div class="add-question-content">
              <div class="add-question-icon">
                <svg width="48" height="48" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M12 6v6m0 0v6m0-6h6m-6 0H6"/>
                </svg>
              </div>
              <h3>Add Another Question</h3>
              <p>Click to create question {{ quiz.questions.length + 1 }}</p>
            </div>
          </div>
        </div>

        <!-- Action Buttons -->
        <div class="action-buttons">
          <button @click="currentStep = 'details'" class="btn btn-secondary">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M15 19l-7-7 7-7"/>
            </svg>
            Back
          </button>
          <button v-if="quiz.questions.length > 0" @click="currentStep = 'settings'" class="btn btn-primary">
            Continue to Settings
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M13 7l5 5m0 0l-5 5m5-5H6"/>
            </svg>
          </button>
        </div>
      </div>

      <!-- Quiz Settings with Enhanced Design -->
      <div v-if="currentStep === 'settings'" class="content-card slide-up">
        <div class="section-header">
          <div class="section-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"/>
            </svg>
          </div>
          <div class="section-content">
            <h2 class="section-title">Quiz Settings</h2>
            <p class="section-subtitle">Configure how your quiz will work</p>
          </div>
        </div>

        <div class="settings-grid">
          <!-- Time Limit Setting -->
          <div class="setting-card enhanced-setting">
            <div class="setting-header">
              <div class="setting-info">
                <span class="setting-emoji">⏱️</span>
                <div class="setting-details">
                  <h3>Time Limit</h3>
                  <p>Set a time constraint for this quiz</p>
                </div>
              </div>
              <label class="toggle-switch">
                <input v-model="quiz.settings.hasTimeLimit" type="checkbox" />
                <span class="toggle-slider"></span>
              </label>
            </div>
            <div v-if="quiz.settings.hasTimeLimit" class="setting-content">
              <div class="time-input-group">
                <input v-model.number="quiz.settings.timeLimit" type="number" min="1" max="180" placeholder="30" class="form-input time-input" />
                <span class="time-unit">minutes</span>
              </div>
            </div>
          </div>

          <!-- Attempts Setting -->
          <div class="setting-card enhanced-setting">
            <div class="setting-header">
              <div class="setting-info">
                <span class="setting-emoji">🔁</span>
                <div class="setting-details">
                  <h3>Attempts Allowed</h3>
                  <p>How many times can students retake?</p>
                </div>
              </div>
            </div>
            <div class="setting-content">
              <div class="attempts-options">
                <label class="attempt-option" :class="quiz.settings.attemptsAllowed === 1 ? 'selected' : ''">
                  <input type="radio" v-model.number="quiz.settings.attemptsAllowed" :value="1" class="hidden" />
                  <span class="attempt-number">1</span>
                  <span class="attempt-label">Once</span>
                </label>
                <label class="attempt-option" :class="quiz.settings.attemptsAllowed === 2 ? 'selected' : ''">
                  <input type="radio" v-model.number="quiz.settings.attemptsAllowed" :value="2" class="hidden" />
                  <span class="attempt-number">2</span>
                  <span class="attempt-label">Twice</span>
                </label>
                <label class="attempt-option" :class="quiz.settings.attemptsAllowed === 999 ? 'selected' : ''">
                  <input type="radio" v-model.number="quiz.settings.attemptsAllowed" :value="999" class="hidden" />
                  <span class="attempt-number">∞</span>
                  <span class="attempt-label">Unlimited</span>
                </label>
              </div>
            </div>
          </div>

          <!-- Shuffle Setting -->
          <div class="setting-card enhanced-setting">
            <div class="setting-header">
              <div class="setting-info">
                <span class="setting-emoji">🔀</span>
                <div class="setting-details">
                  <h3>Shuffle Questions</h3>
                  <p>Randomize question and answer order</p>
                </div>
              </div>
              <label class="toggle-switch">
                <input v-model="quiz.settings.shuffle" type="checkbox" />
                <span class="toggle-slider"></span>
              </label>
            </div>
          </div>

          <!-- Schedule Setting -->
          <div class="setting-card enhanced-setting schedule-card">
            <div class="setting-header">
              <div class="setting-info">
                <span class="setting-emoji">📅</span>
                <div class="setting-details">
                  <h3>Schedule</h3>
                  <p>Set when students can access this quiz</p>
                </div>
              </div>
            </div>
            <div class="setting-content">
              <div class="schedule-grid">
                <div class="form-group">
                  <label class="form-label-small">
                    <span class="label-icon">🕐</span>
                    Start Date & Time (PHT)
                  </label>
                  <input v-model="quiz.settings.startDate" type="datetime-local" class="form-input enhanced-input" />
                  <small class="timezone-note">Philippines Time (UTC+8)</small>
                </div>
                <div class="form-group">
                  <label class="form-label-small">
                    <span class="label-icon">🕕</span>
                    End Date & Time (PHT)
                  </label>
                  <input v-model="quiz.settings.endDate" type="datetime-local" class="form-input enhanced-input" />
                  <small class="timezone-note">Philippines Time (UTC+8)</small>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="action-buttons">
          <button @click="currentStep = 'questions'" class="btn btn-secondary">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M15 19l-7-7 7-7"/>
            </svg>
            Back
          </button>
          <button @click="currentStep = 'preview'" class="btn btn-primary">
            Preview Quiz
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/>
            </svg>
          </button>
        </div>
      </div>

      <!-- Preview with Enhanced Design -->
      <div v-if="currentStep === 'preview'" class="content-card slide-up">
        <div class="preview-header">
          <div class="preview-badge">
            <span class="badge-icon">👁️</span>
            PREVIEW MODE
          </div>
          <h2 class="preview-title">{{ quiz.title }}</h2>
          <p class="preview-description">{{ quiz.description }}</p>
          <div class="preview-stats">
            <div class="stat-card">
              <div class="stat-icon">⏱️</div>
              <div class="stat-value">
                <span v-if="quiz.settings.hasTimeLimit">{{ quiz.settings.timeLimit }} min</span>
                <span v-else>No limit</span>
              </div>
              <div class="stat-label">Time</div>
            </div>
            <div class="stat-card">
              <div class="stat-icon">📝</div>
              <div class="stat-value">{{ quiz.questions.length }}</div>
              <div class="stat-label">Questions</div>
            </div>
            <div class="stat-card">
              <div class="stat-icon">🔁</div>
              <div class="stat-value">{{ quiz.settings.attemptsAllowed === 999 ? '∞' : quiz.settings.attemptsAllowed }}</div>
              <div class="stat-label">Attempts</div>
            </div>
          </div>
        </div>

        <div class="preview-questions">
          <div v-for="(question, index) in quiz.questions" :key="index" class="preview-card enhanced-preview">
            <div class="preview-question-header">
              <div class="preview-question-number">{{ index + 1 }}</div>
              <div class="question-type-badge" :class="question.type">
                <span v-if="question.type === 'multiple_choice'">📝 MCQ</span>
                <span v-else-if="question.type === 'true_false'">✅ T/F</span>
                <span v-else>✏️ Fill</span>
              </div>
            </div>
            <h3 class="preview-question-text">{{ question.text }}</h3>
            
            <!-- MCQ Preview -->
            <div v-if="question.type === 'multiple_choice'" class="preview-options">
              <div v-for="(option, optIndex) in question.options" :key="optIndex" 
                   :class="['preview-option', question.correctAnswer === optIndex ? 'correct-option' : '']">
                <div class="option-marker">{{ String.fromCharCode(65 + optIndex) }}</div>
                <span class="option-text">{{ option }}</span>
                <span v-if="question.correctAnswer === optIndex" class="correct-mark">✓</span>
              </div>
            </div>

            <!-- True/False Preview -->
            <div v-if="question.type === 'true_false'" class="preview-options">
              <div :class="['preview-option', question.correctAnswer === 'true' ? 'correct-option' : '']">
                <div class="option-marker">✅</div>
                <span class="option-text">True</span>
                <span v-if="question.correctAnswer === 'true'" class="correct-mark">✓</span>
              </div>
              <div :class="['preview-option', question.correctAnswer === 'false' ? 'correct-option' : '']">
                <div class="option-marker">❌</div>
                <span class="option-text">False</span>
                <span v-if="question.correctAnswer === 'false'" class="correct-mark">✓</span>
              </div>
            </div>

            <!-- Fill Blank Preview -->
            <div v-if="question.type === 'fill_blank'" class="preview-fill-blank">
              <div class="fill-blank-input">
                <input type="text" disabled placeholder="Student answer here..." class="form-input" />
              </div>
              <div class="correct-answer-display">
                <span class="correct-label">✓ Correct Answer:</span>
                <span class="correct-text">{{ question.correctAnswer }}</span>
              </div>
            </div>
          </div>
        </div>

        <div class="action-buttons">
          <button @click="currentStep = 'settings'" class="btn btn-secondary">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M11 17l-5-5m0 0l5-5m-5 5h12"/>
            </svg>
            Edit Quiz
          </button>
          <button @click="publishQuiz" :disabled="isPublishing" class="btn btn-publish">
            <svg v-if="!isPublishing" width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
              <path d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
            </svg>
            <div v-else class="spinner"></div>
            <span>{{ isPublishing ? 'Publishing...' : 'Publish Quiz Now' }}</span>
            <svg v-if="!isPublishing" width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M5 10l7-7m0 0l7 7m-7-7v18"/>
            </svg>
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted, onUnmounted } from 'vue';
import { useRouter, useRoute } from 'vue-router';
import { supabase } from '@/supabase.js';

export default {
  name: 'CreateQuiz',
  setup() {
    const router = useRouter();
    const route = useRoute();
    
    const currentStep = ref('landing');
    const steps = ['Details', 'Questions', 'Settings', 'Preview'];
    const isPublishing = ref(false);
    
    const teacherInfo = ref({
      full_name: 'Loading...',
      email: '',
      role: 'teacher',
      teacher_id: null
    });

    const subject = ref({
      id: '',
      name: 'Subject'
    });

    const section = ref({
      id: '',
      name: ''
    });

    const quiz = ref({
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
    });

    // Timeout wrapper for database operations
    const withTimeout = (promise, timeoutMs = 15000) => {
      return Promise.race([
        promise,
        new Promise((_, reject) => 
          setTimeout(() => reject(new Error('Operation timed out')), timeoutMs)
        )
      ]);
    };

    // Convert Philippines time to UTC for storage
    const convertPHTimeToUTC = (phDateString) => {
      if (!phDateString) return null;
      try {
        const phDate = new Date(phDateString);
        const utcTime = new Date(phDate.getTime() - (8 * 60 * 60 * 1000));
        return utcTime.toISOString();
      } catch (error) {
        console.error('Error converting PH time to UTC:', error);
        return null;
      }
    };

    // Real-time subscription
    let quizSubscription = null;

    const loadTeacherInfo = async () => {
      try {
        const { data: { session }, error: sessionError } = await supabase.auth.getSession();
        
        if (sessionError || !session?.user) {
          console.error('No session found');
          router.push('/login');
          return false;
        }

        const { data: profile, error: profileError } = await supabase
          .from('profiles')
          .select('id, role, full_name, email')
          .eq('auth_user_id', session.user.id)
          .single();

        if (profileError || !profile) {
          console.error('Profile error:', profileError);
          alert('Failed to load profile. Please try logging in again.');
          return false;
        }

        const { data: teacher, error: teacherError } = await supabase
          .from('teachers')
          .select('*')
          .eq('profile_id', profile.id)
          .single();

        if (teacherError || !teacher) {
          console.error('Teacher error:', teacherError);
          alert('Teacher profile not found. Please contact support.');
          return false;
        }

        teacherInfo.value = {
          full_name: teacher.full_name,
          email: teacher.email,
          role: profile.role,
          teacher_id: teacher.id
        };

        console.log('✅ Teacher info loaded:', teacherInfo.value.teacher_id);
        return true;
      } catch (error) {
        console.error('Error loading teacher info:', error);
        alert('Failed to load teacher information. Please refresh the page.');
        return false;
      }
    };

    const loadRouteParams = () => {
      const subjectId = route.params.subjectId;
      const sectionId = route.params.sectionId;
      const subjectName = route.query.subjectName || 'Subject';
      const sectionName = route.query.sectionName || '';

      if (!subjectId || !sectionId) {
        console.error('Missing required route parameters');
        return false;
      }

      subject.value = { id: subjectId, name: subjectName };
      section.value = { id: sectionId, name: sectionName };

      console.log('✅ Route params loaded:', { subjectId, sectionId });
      return true;
    };

    const setupRealtimeSubscription = () => {
      if (!teacherInfo.value.teacher_id) return;
      
      quizSubscription = supabase
        .channel('quiz-changes')
        .on(
          'postgres_changes',
          {
            event: 'INSERT',
            schema: 'public',
            table: 'quizzes',
            filter: `teacher_id=eq.${teacherInfo.value.teacher_id}`
          },
          (payload) => {
            console.log('📡 New quiz created (real-time):', payload.new);
          }
        )
        .subscribe();
    };

    const goBack = () => {
      if (currentStep.value === 'landing') {
        router.back();
      } else {
        if (confirm('Are you sure you want to go back? Unsaved changes will be lost.')) {
          router.back();
        }
      }
    };

    const getStepIndex = (step) => {
      const stepMap = {
        'landing': -1,
        'details': 0,
        'questions': 1,
        'settings': 2,
        'preview': 3
      };
      return stepMap[step];
    };

    const proceedToQuestions = () => {
      if (!quiz.value.title || !quiz.value.title.trim()) {
        alert('Please enter a quiz title');
        return;
      }
      if (!quiz.value.numberOfQuestions) {
        alert('Please enter the number of questions');
        return;
      }
      if (quiz.value.numberOfQuestions < 1 || quiz.value.numberOfQuestions > 50) {
        alert('Number of questions must be between 1 and 50');
        return;
      }
      currentStep.value = 'questions';
    };

    const addQuestion = () => {
      if (quiz.value.questions.length >= quiz.value.numberOfQuestions) {
        alert(`You can only add ${quiz.value.numberOfQuestions} questions`);
        return;
      }
      quiz.value.questions.push({
        type: 'multiple_choice',
        text: '',
        options: ['', '', '', ''],
        correctAnswer: null
      });
    };

    const removeQuestion = (index) => {
      if (confirm('Are you sure you want to remove this question?')) {
        quiz.value.questions.splice(index, 1);
      }
    };

    const addOption = (questionIndex) => {
      if (quiz.value.questions[questionIndex].options.length < 6) {
        quiz.value.questions[questionIndex].options.push('');
      } else {
        alert('Maximum 6 options allowed per question');
      }
    };

    const removeOption = (questionIndex, optionIndex) => {
      if (quiz.value.questions[questionIndex].options.length > 2) {
        quiz.value.questions[questionIndex].options.splice(optionIndex, 1);
        if (quiz.value.questions[questionIndex].correctAnswer === optionIndex) {
          quiz.value.questions[questionIndex].correctAnswer = null;
        } else if (quiz.value.questions[questionIndex].correctAnswer > optionIndex) {
          quiz.value.questions[questionIndex].correctAnswer--;
        }
      } else {
        alert('A question must have at least 2 options');
      }
    };

    const validateQuiz = () => {
      if (!quiz.value.title.trim()) {
        alert('Please enter a quiz title');
        currentStep.value = 'details';
        return false;
      }

      if (quiz.value.questions.length === 0) {
        alert('Please add at least one question');
        currentStep.value = 'questions';
        return false;
      }

      for (let i = 0; i < quiz.value.questions.length; i++) {
        const q = quiz.value.questions[i];
        
        if (!q.text.trim()) {
          alert(`Question ${i + 1}: Please enter question text`);
          currentStep.value = 'questions';
          return false;
        }

        if (q.type === 'multiple_choice') {
          const emptyOptions = q.options.filter(opt => !opt.trim());
          if (emptyOptions.length > 0) {
            alert(`Question ${i + 1}: All answer options must be filled`);
            currentStep.value = 'questions';
            return false;
          }

          if (q.correctAnswer === null || q.correctAnswer === undefined) {
            alert(`Question ${i + 1}: Please select the correct answer`);
            currentStep.value = 'questions';
            return false;
          }
        } else if (q.type === 'true_false') {
          if (!q.correctAnswer) {
            alert(`Question ${i + 1}: Please select True or False as the correct answer`);
            currentStep.value = 'questions';
            return false;
          }
        } else if (q.type === 'fill_blank') {
          if (!q.correctAnswer || !q.correctAnswer.trim()) {
            alert(`Question ${i + 1}: Please enter the correct answer`);
            currentStep.value = 'questions';
            return false;
          }
        }
      }

      if (quiz.value.settings.hasTimeLimit) {
        if (!quiz.value.settings.timeLimit || quiz.value.settings.timeLimit < 1) {
          alert('Please enter a valid time limit (at least 1 minute)');
          currentStep.value = 'settings';
          return false;
        }
      }

      if (quiz.value.settings.startDate && quiz.value.settings.endDate) {
        const startDate = new Date(quiz.value.settings.startDate);
        const endDate = new Date(quiz.value.settings.endDate);
        if (endDate <= startDate) {
          alert('End date must be after start date');
          currentStep.value = 'settings';
          return false;
        }
      }

      return true;
    };

    // ============================================
    // BULLETPROOF PUBLISH FUNCTION WITH TIMEOUTS
    // ============================================
    const publishQuiz = async () => {
      console.log('🚀 Starting quiz publication...');
      
      if (!validateQuiz()) {
        console.log('❌ Validation failed');
        return;
      }

      if (!confirm(`Publish "${quiz.value.title}"?\n\nStudents will be able to see and take this quiz immediately.`)) {
        return;
      }

      isPublishing.value = true;

      try {
        // Verify required data
        if (!subject.value.id || !section.value.id || !teacherInfo.value.teacher_id) {
          throw new Error('Missing required information: subject_id, section_id, or teacher_id');
        }

        console.log('📋 Data verified:', {
          subjectId: subject.value.id,
          sectionId: section.value.id,
          teacherId: teacherInfo.value.teacher_id,
          questions: quiz.value.questions.length
        });

        // Step 1: Create Quiz with timeout
        console.log('📝 Creating quiz...');
        const quizData = {
          subject_id: subject.value.id,
          section_id: section.value.id,
          teacher_id: teacherInfo.value.teacher_id,
          title: quiz.value.title.trim(),
          description: quiz.value.description.trim() || null,
          number_of_questions: parseInt(quiz.value.numberOfQuestions),
          has_time_limit: quiz.value.settings.hasTimeLimit,
          time_limit_minutes: quiz.value.settings.hasTimeLimit ? parseInt(quiz.value.settings.timeLimit) : null,
          attempts_allowed: parseInt(quiz.value.settings.attemptsAllowed),
          shuffle_questions: quiz.value.settings.shuffle,
          shuffle_options: quiz.value.settings.shuffle,
          start_date: convertPHTimeToUTC(quiz.value.settings.startDate),
          end_date: convertPHTimeToUTC(quiz.value.settings.endDate),
          status: 'published'
        };

        const quizInsert = supabase
          .from('quizzes')
          .insert([quizData])
          .select()
          .single();

        const { data: newQuiz, error: quizError } = await withTimeout(quizInsert, 10000);

        if (quizError) throw quizError;
        if (!newQuiz || !newQuiz.id) throw new Error('Quiz creation failed');

        console.log('✅ Quiz created:', newQuiz.id, newQuiz.quiz_code);

        // Step 2: Insert questions with timeout
        console.log('📝 Creating questions...');
        const questionsData = quiz.value.questions.map((q, index) => ({
          quiz_id: newQuiz.id,
          question_number: index + 1,
          question_type: q.type,
          question_text: q.text.trim(),
          points: 1.00
        }));

        const questionsInsert = supabase
          .from('quiz_questions')
          .insert(questionsData)
          .select();

        const { data: insertedQuestions, error: questionsError } = await withTimeout(questionsInsert, 10000);

        if (questionsError) throw questionsError;
        if (!insertedQuestions || insertedQuestions.length !== questionsData.length) {
          throw new Error('Failed to insert all questions');
        }

        console.log(`✅ ${insertedQuestions.length} questions created`);

        // Step 3: Insert options and answers
        const allOptions = [];
        const allAnswers = [];

        for (let i = 0; i < quiz.value.questions.length; i++) {
          const question = quiz.value.questions[i];
          const questionId = insertedQuestions[i].id;

          if (question.type === 'multiple_choice') {
            question.options.forEach((opt, optIndex) => {
              allOptions.push({
                question_id: questionId,
                option_number: optIndex + 1,
                option_text: opt.trim(),
                is_correct: question.correctAnswer === optIndex
              });
            });
          } else if (question.type === 'true_false' || question.type === 'fill_blank') {
            allAnswers.push({
              question_id: questionId,
              correct_answer: String(question.correctAnswer).trim(),
              case_sensitive: question.type === 'fill_blank'
            });
          }
        }

        // Insert options with timeout
        if (allOptions.length > 0) {
          console.log(`📝 Creating ${allOptions.length} options...`);
          const optionsInsert = supabase
            .from('question_options')
            .insert(allOptions);

          const { error: optionsError } = await withTimeout(optionsInsert, 10000);
          if (optionsError) throw optionsError;
          console.log('✅ Options created');
        }

        // Insert answers with timeout
        if (allAnswers.length > 0) {
          console.log(`📝 Creating ${allAnswers.length} answers...`);
          const answersInsert = supabase
            .from('question_answers')
            .insert(allAnswers);

          const { error: answersError } = await withTimeout(answersInsert, 10000);
          if (answersError) throw answersError;
          console.log('✅ Answers created');
        }

        console.log('✅✅✅ QUIZ PUBLISHED SUCCESSFULLY ✅✅✅');

        // Success alert
        alert(`✅ Quiz published successfully!\n\n📝 ${newQuiz.title}\n🔑 Quiz Code: ${newQuiz.quiz_code}\n\nStudents can now take this quiz.`);

        // Navigate immediately
        router.push({
          name: 'ViewQuizzes',
          params: {
            subjectId: subject.value.id,
            sectionId: section.value.id
          },
          query: {
            subjectName: subject.value.name,
            sectionName: section.value.name,
            gradeLevel: route.query.gradeLevel,
            sectionCode: route.query.sectionCode
          }
        });

      } catch (error) {
        console.error('❌ ERROR:', error);

        let errorMessage = '❌ Failed to publish quiz.\n\n';

        if (error.message === 'Operation timed out') {
          errorMessage += '⏱️ The request took too long.\n\n';
          errorMessage += 'Possible causes:\n';
          errorMessage += '• Slow internet connection\n';
          errorMessage += '• Database is busy\n';
          errorMessage += '• Too many questions\n\n';
          errorMessage += '💡 Try reducing the number of questions or retry in a moment.';
        } else if (error.code === '23505') {
          errorMessage += '⚠️ Duplicate entry.\nTry a different quiz title.';
        } else if (error.code === '23503') {
          errorMessage += '⚠️ Invalid data reference.\nPlease refresh and try again.';
        } else {
          errorMessage += `Error: ${error.message}`;
          if (error.code) errorMessage += `\nCode: ${error.code}`;
        }

        alert(errorMessage);
      } finally {
        isPublishing.value = false;
        console.log('🏁 Publishing finished');
      }
    };

    onMounted(async () => {
      console.log('🎬 CreateQuiz mounted');

      const teacherLoaded = await loadTeacherInfo();
      if (!teacherLoaded) {
        router.push('/login');
        return;
      }

      const paramsLoaded = loadRouteParams();
      if (!paramsLoaded) {
        alert('Missing information. Redirecting...');
        router.push('/teacher/subjects');
        return;
      }

      setupRealtimeSubscription();
      console.log('✅ Initialized');
    });

    onUnmounted(() => {
      if (quizSubscription) {
        supabase.removeChannel(quizSubscription);
      }
    });

    return {
      currentStep,
      steps,
      teacherInfo,
      subject,
      section,
      quiz,
      isPublishing,
      goBack,
      getStepIndex,
      proceedToQuestions,
      addQuestion,
      removeQuestion,
      addOption,
      removeOption,
      publishQuiz
    };
  }
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.create-quiz-page {
  min-height: 100vh;
  background: #FBFFE4;
  padding: 1.5rem;
  font-family: 'Inter', sans-serif;
}
.dark .create-quiz-page {
  background: #181c20;
}

/* Header */
.section-header-card {
  background: white;
  border-radius: 16px;
  padding: 1.5rem;
  margin-bottom: 1.5rem;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
}
.dark .section-header-card {
  background: #23272b;
  border: 1px solid #3D8D7A;
  box-shadow: 0 2px 8px rgba(0,0,0,0.25);
}

.section-header-content {
  display: flex;
  align-items: center;
  justify-content: space-between;
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
}

.section-header-title {
  font-size: 1.5rem;
  font-weight: 700;
  color: #1f2937;
  margin-bottom: 0.25rem;
}
.dark .section-header-title {
  color: #A3D1C6;
}

.section-header-subtitle {
  font-size: 0.875rem;
  color: #6b7280;
}
.dark .section-header-subtitle {
  color: #A3D1C6;
}

.section-header-description {
  font-size: 0.813rem;
  color: #94a3b8;
}
.dark .section-header-description {
  color: #A3D1C6;
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
  display: flex;
  align-items: center;
  gap: 0.5rem;
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
.dark .back-btn {
  background: #20c997;
  color: #181c20;
  border-color: #A3D1C6;
}
.dark .back-btn:hover {
  background: #A3D1C6;
  color: #23272b;
  border-color: #20c997;
}

/* Progress */
.progress-card {
  background: white;
  border-radius: 16px;
  padding: 1.5rem;
  margin-bottom: 1.5rem;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
}
.dark .progress-card {
  background: #23272b;
  border: 1px solid #3D8D7A;
  box-shadow: 0 2px 8px rgba(0,0,0,0.25);
}
.progress-track {
  display: flex;
  align-items: center;
  justify-content: space-between;
  position: relative;
  overflow: hidden;
}
.progress-step {
  display: flex;
  flex-direction: column;
  align-items: center;
  position: relative;
  flex: 1;
}
.step-line {
  position: absolute;
  top: 20px;
  left: 50%;
  right: -50%;
  height: 2px;
  background: #e5e7eb;
  z-index: 1;
  transition: all 0.3s ease;
}
.progress-step:last-child .step-line {
  right: 50%;
}
.step-line.completed {
  background: #3D8D7A;
}
.step-indicator {
  position: relative;
  z-index: 2;
  margin-bottom: 0.75rem;
}
.step-circle {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 600;
  font-size: 0.875rem;
  transition: all 0.3s ease;
  background: #e5e7eb;
  color: #6b7280;
}
.step-indicator.active .step-circle,
.step-indicator.completed .step-circle {
  background: #3D8D7A;
  color: white;
}
.step-label {
  font-size: 0.875rem;
  font-weight: 500;
  color: #6b7280;
  text-align: center;
}
.dark .step-label {
  color: #A3D1C6;
}
.step-indicator.active + .step-label,
.step-indicator.completed + .step-label {
  color: #3D8D7A;
  font-weight: 600;
}
.dark .step-indicator.active + .step-label,
.dark .step-indicator.completed + .step-label {
  color: #A3D1C6;
}

/* Main Content */
.main-content {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.content-card {
  background: white;
  border-radius: 16px;
  padding: 1.5rem;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
}
.dark .content-card {
  background: #23272b;
  border: 1px solid #3D8D7A;
  box-shadow: 0 2px 8px rgba(0,0,0,0.25);
}

/* Card Headers */
.card-header {
  margin-bottom: 1.5rem;
}
.card-header h3 {
  font-size: 1.25rem;
  font-weight: 600;
  color: #1f2937;
  margin-bottom: 0.25rem;
}
.dark .card-header h3 {
  color: #A3D1C6;
}
.card-desc {
  font-size: 0.875rem;
  color: #6b7280;
}
.dark .card-desc {
  color: #A3D1C6;
}

/* Buttons */
.btn {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1.25rem;
  border-radius: 8px;
  font-weight: 600;
  font-size: 0.875rem;
  cursor: pointer;
  transition: all 0.2s;
  border: none;
}
.btn-secondary {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.6rem 1.5rem;
  border-radius: 8px;
  font-weight: 600;
  font-size: 1rem;
  transition: background 0.2s, color 0.2s, border-color 0.2s, box-shadow 0.2s;
  cursor: pointer;
  text-decoration: none;
  border: 2px solid #20c997;
  background: transparent;
  color: #A3D1C6;
  box-shadow: none;
}
.btn-secondary:hover {
  background: #23272b;
  color: #20c997;
  border-color: #20c997;
  box-shadow: 0 2px 8px rgba(61, 141, 122, 0.10);
}
.dark .btn-secondary {
  background: transparent;
  color: #A3D1C6;
  border-color: #20c997;
}
.dark .btn-secondary:hover {
  background: #23272b;
  color: #20c997;
  border-color: #20c997;
}
.btn-primary {
  background: #20c997;
  color: #181c20;
  border: 2px solid #20c997;
  border-radius: 8px;
  font-weight: 600;
  font-size: 1rem;
  padding: 0.6rem 2.2rem;
  box-shadow: none;
  transition: background 0.2s, color 0.2s, border-color 0.2s, box-shadow 0.2s;
}
.btn-primary:hover {
  background: #A3D1C6;
  color: #23272b;
  border-color: #20c997;
  box-shadow: 0 2px 8px rgba(61, 141, 122, 0.10);
  transform: translateY(-1px);
}
.btn-danger {
  background: #ef4444;
  color: white;
}
.btn-danger:hover {
  background: #dc2626;
}
.btn-success {
  background: #B3D8A8;
  color: #1f2937;
}
.btn-success:hover {
  background: #9fcf94;
}
.btn-publish {
  background: #A3D1C6;
  color: #1f2937;
  padding: 1rem 2rem;
  font-size: 1rem;
  font-weight: 700;
}
.btn-publish:hover {
  background: #8fbeb6;
  transform: translateY(-2px);
}

/* Landing Section */
.landing-section {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 60vh;
}
/* Card style like dashboard */
.landing-card {
  background: white;
  border-radius: 16px;
  border: 2px solid #3D8D7A;
  padding: 2.5rem 2rem;
  box-shadow: 0 2px 16px rgba(61, 141, 122, 0.10);
  display: flex;
  flex-direction: column;
  align-items: center;
  max-width: 420px;
  width: 100%;
  transition: box-shadow 0.2s, border-color 0.2s;
}
.dark .landing-card {
  background: #181c20;
  border: 1.5px solid #3D8D7A;
  box-shadow: 0 2px 12px rgba(61, 141, 122, 0.10);
}
.landing-icon {
  width: 56px;
  height: 56px;
  background: linear-gradient(135deg, #3D8D7A 60%, #A3D1C6 100%);
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 1.5rem;
  box-shadow: 0 2px 8px rgba(61, 141, 122, 0.10);
}
.landing-title {
  font-size: 1.5rem;
  font-weight: 700;
  color: #1f2937;
  margin-bottom: 0.5rem;
  text-align: center;
}
.dark .landing-title {
  color: #A3D1C6;
}
.landing-desc {
  font-size: 1rem;
  color: #6b7280;
  margin-bottom: 1.5rem;
  text-align: center;
}
.dark .landing-desc {
  color: #A3D1C6;
}
.features-preview {
  display: flex;
  gap: 1.25rem;
  margin-bottom: 2rem;
  width: 100%;
  justify-content: center;
}
.feature-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  background: #FBFFE4;
  border: 2px solid #3D8D7A;
  border-radius: 12px;
  padding: 1.1rem 1.2rem 0.7rem 1.2rem;
  min-width: 110px;
  font-size: 1.05rem;
  color: #3D8D7A;
  font-weight: 500;
  box-shadow: 0 1px 4px rgba(61, 141, 122, 0.07);
  transition: border-color 0.2s, box-shadow 0.2s, background 0.2s;
  cursor: pointer;
}
.feature-item:hover {
  border-color: #B3D8A8;
  background: #B3D8A8;
  color: #1f2937;
  box-shadow: 0 2px 8px rgba(61, 141, 122, 0.13);
}
.dark .feature-item {
  background: #23272b;
  border-color: #3D8D7A;
  color: #A3D1C6;
  box-shadow: 0 1px 4px rgba(61, 141, 122, 0.04);
}
.dark .feature-item:hover {
  background: #3D8D7A;
  color: #FBFFE4;
  border-color: #A3D1C6;
}
.feature-icon {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 0.4rem;
}
.create-quiz-btn {
  background: #20c997;
  color: #181c20;
  border: 2px solid #20c997;
  border-radius: 8px;
  padding: 0.6rem 1.5rem;
  font-weight: 600;
  font-size: 1rem;
  cursor: pointer;
  transition: background 0.2s, color 0.2s, border-color 0.2s, box-shadow 0.2s;
  margin-top: 0.7rem;
  box-shadow: 0 2px 8px rgba(61, 141, 122, 0.10);
}
.create-quiz-btn:hover {
  background: #A3D1C6;
  color: #23272b;
  border-color: #20c997;
  box-shadow: 0 4px 16px rgba(61, 141, 122, 0.18);
}
.dark .create-quiz-btn {
  background: #20c997;
  color: #181c20;
  border-color: #A3D1C6;
}
.dark .create-quiz-btn:hover {
  background: #A3D1C6;
  color: #23272b;
  border-color: #20c997;
}

/* Responsive Design */
@media (max-width: 768px) {
  .create-quiz-page {
    padding: 1rem;
  }
  .section-header-content {
    flex-direction: column;
    gap: 1rem;
    text-align: center;
  }
  .section-header-left {
    flex-direction: column;
    gap: 1rem;
    text-align: center;
  }
  .main-content {
    gap: 1rem;
  }
}

/* Quiz Details Form Grid & Inputs */
.form-section {
  margin-top: 1.5rem;
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}
.form-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.25rem 2rem;
  margin-bottom: 1rem;
}
@media (max-width: 768px) {
  .form-grid {
    grid-template-columns: 1fr;
    gap: 1rem;
  }
}
.form-group {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}
.form-label {
  font-size: 1rem;
  font-weight: 600;
  color: #3D8D7A;
  margin-bottom: 0.2rem;
}
.dark .form-label {
  color: #A3D1C6;
}
.form-input {
  padding: 0.7rem 1rem;
  border-radius: 8px;
  border: 1.5px solid #A3D1C6;
  background: #FBFFE4;
  font-size: 1rem;
  color: #1f2937;
  font-family: 'Inter', sans-serif;
  transition: border-color 0.2s, background 0.2s;
}
.form-input:focus {
  outline: none;
  border-color: #3D8D7A;
  background: #fff;
}
.dark .form-input {
  background: #23272b;
  color: #A3D1C6;
  border-color: #3D8D7A;
}
.dark .form-input:focus {
  background: #181c20;
  border-color: #A3D1C6;
}

/* DateTime Local Calendar Styling */
input[type="datetime-local"]::-webkit-calendar-picker-indicator {
  background: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 20 20' fill='%233D8D7A'%3e%3cpath fill-rule='evenodd' d='M6 2a1 1 0 00-1 1v1H4a2 2 0 00-2 2v10a2 2 0 002 2h12a2 2 0 002-2V6a2 2 0 00-2-2h-1V3a1 1 0 10-2 0v1H7V3a1 1 0 00-1-1zm0 5a1 1 0 000 2h8a1 1 0 100-2H6z' clip-rule='evenodd'/%3e%3c/svg%3e") no-repeat center;
  background-size: 16px 16px;
  cursor: pointer;
  opacity: 1;
  width: 20px;
  height: 20px;
  padding: 0;
  margin: 0;
  border: none;
  background-color: transparent;
}

.dark input[type="datetime-local"]::-webkit-calendar-picker-indicator {
  background: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 20 20' fill='%23A3D1C6'%3e%3cpath fill-rule='evenodd' d='M6 2a1 1 0 00-1 1v1H4a2 2 0 00-2 2v10a2 2 0 002 2h12a2 2 0 002-2V6a2 2 0 00-2-2h-1V3a1 1 0 10-2 0v1H7V3a1 1 0 00-1-1zm0 5a1 1 0 000 2h8a1 1 0 100-2H6z' clip-rule='evenodd'/%3e%3c/svg%3e") no-repeat center;
  background-size: 16px 16px;
}

input[type="datetime-local"]::-webkit-datetime-edit {
  color: #3D8D7A;
  font-family: 'Inter', sans-serif;
}

.dark input[type="datetime-local"]::-webkit-datetime-edit {
  color: #A3D1C6;
}

input[type="datetime-local"]::-webkit-datetime-edit-text {
  color: #6b7280;
  padding: 0 0.25rem;
}

.dark input[type="datetime-local"]::-webkit-datetime-edit-text {
  color: #A3D1C6;
}

input[type="datetime-local"]::-webkit-datetime-edit-month-field,
input[type="datetime-local"]::-webkit-datetime-edit-day-field,
input[type="datetime-local"]::-webkit-datetime-edit-year-field,
input[type="datetime-local"]::-webkit-datetime-edit-hour-field,
input[type="datetime-local"]::-webkit-datetime-edit-minute-field {
  background: transparent;
  color: #3D8D7A;
  font-weight: 500;
  padding: 0.1rem 0.2rem;
  border-radius: 4px;
  border: none;
}

.dark input[type="datetime-local"]::-webkit-datetime-edit-month-field,
.dark input[type="datetime-local"]::-webkit-datetime-edit-day-field,
.dark input[type="datetime-local"]::-webkit-datetime-edit-year-field,
.dark input[type="datetime-local"]::-webkit-datetime-edit-hour-field,
.dark input[type="datetime-local"]::-webkit-datetime-edit-minute-field {
  color: #A3D1C6;
}

input[type="datetime-local"]::-webkit-datetime-edit-month-field:focus,
input[type="datetime-local"]::-webkit-datetime-edit-day-field:focus,
input[type="datetime-local"]::-webkit-datetime-edit-year-field:focus,
input[type="datetime-local"]::-webkit-datetime-edit-hour-field:focus,
input[type="datetime-local"]::-webkit-datetime-edit-minute-field:focus {
  background: rgba(61, 141, 122, 0.1);
  outline: none;
}

.dark input[type="datetime-local"]::-webkit-datetime-edit-month-field:focus,
.dark input[type="datetime-local"]::-webkit-datetime-edit-day-field:focus,
.dark input[type="datetime-local"]::-webkit-datetime-edit-year-field:focus,
.dark input[type="datetime-local"]::-webkit-datetime-edit-hour-field:focus,
.dark input[type="datetime-local"]::-webkit-datetime-edit-minute-field:focus {
  background: rgba(163, 209, 198, 0.1);
}

/* Custom calendar popup styling for supported browsers */
input[type="datetime-local"]::-webkit-calendar-picker-indicator:hover {
  background-color: rgba(61, 141, 122, 0.1);
  border-radius: 4px;
}

.dark input[type="datetime-local"]::-webkit-calendar-picker-indicator:hover {
  background-color: rgba(163, 209, 198, 0.1);
}

/* Enhanced Calendar Popup Styling */
/* Force calendar to use appropriate color scheme */
input[type="datetime-local"] {
  color-scheme: light;
  accent-color: #3D8D7A;
}

.dark input[type="datetime-local"] {
  color-scheme: dark;
  accent-color: #A3D1C6;
}

/* Style the calendar popup directly where browsers support it */
input[type="datetime-local"]::-webkit-calendar-picker-indicator {
  background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='%233D8D7A'%3e%3cpath d='M19 3h-1V1h-2v2H8V1H6v2H5c-1.11 0-1.99.9-1.99 2L3 19c0 1.1.89 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm0 16H5V8h14v11zM7 10h5v5H7z'/%3e%3c/svg%3e");
  background-repeat: no-repeat;
  background-position: center;
  background-size: 18px 18px;
  width: 22px;
  height: 22px;
  cursor: pointer;
  opacity: 1;
  padding: 2px;
  border-radius: 4px;
  transition: background-color 0.2s;
}

.dark input[type="datetime-local"]::-webkit-calendar-picker-indicator {
  background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='%23A3D1C6'%3e%3cpath d='M19 3h-1V1h-2v2H8V1H6v2H5c-1.11 0-1.99.9-1.99 2L3 19c0 1.1.89 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm0 16H5V8h14v11zM7 10h5v5H7z'/%3e%3c/svg%3e");
}

/* Enhanced hover and active states */
input[type="datetime-local"]::-webkit-calendar-picker-indicator:hover {
  background-color: rgba(61, 141, 122, 0.1);
}

.dark input[type="datetime-local"]::-webkit-calendar-picker-indicator:hover {
  background-color: rgba(163, 209, 198, 0.1);
}

input[type="datetime-local"]::-webkit-calendar-picker-indicator:active {
  background-color: rgba(61, 141, 122, 0.2);
  transform: scale(0.95);
}

.dark input[type="datetime-local"]::-webkit-calendar-picker-indicator:active {
  background-color: rgba(163, 209, 198, 0.2);
}

/* Additional webkit calendar styling */
input[type="datetime-local"]::-webkit-inner-spin-button {
  display: none;
}

input[type="datetime-local"]::-webkit-clear-button {
  display: none;
}

/* Force the calendar popup to respect dark mode */
@media (prefers-color-scheme: dark) {
  .dark input[type="datetime-local"] {
    color-scheme: dark;
  }
}

@media (prefers-color-scheme: light) {
  input[type="datetime-local"] {
    color-scheme: light;
  }
}
.enhanced-input {
  box-shadow: 0 1px 4px rgba(61, 141, 122, 0.07);
}
.form-textarea {
  resize: vertical;
  min-height: 80px;
  max-height: 200px;
}

/* Timezone Note Styling */
.timezone-note {
  font-size: 0.75rem;
  color: #6b7280;
  font-style: italic;
  margin-top: 0.25rem;
  display: block;
}
.dark .timezone-note {
  color: #A3D1C6;
}

.form-label-small {
  font-size: 0.875rem;
  font-weight: 600;
  color: #3D8D7A;
  margin-bottom: 0.5rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}
.dark .form-label-small {
  color: #A3D1C6;
}

.label-icon {
  font-size: 1rem;
}
  .action-buttons {
    display: flex;
    justify-content: flex-end;
    gap: 1.1rem;
    margin-top: 2rem;
  }
  .action-buttons .btn-primary {
    min-width: 220px;
    justify-content: center;
  }
@media (max-width: 768px) {
  .action-buttons {
    flex-direction: column;
    align-items: stretch;
    gap: 0.7rem;
  }
}

/* Questions Section Styles */
.questions-container {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.question-card {
  background: #FBFFE4;
  border: 1px solid #A3D1C6;
  border-radius: 12px;
  padding: 1.5rem;
  transition: all 0.2s;
}
.dark .question-card {
  background: #23272b;
  border-color: #3D8D7A;
}

.question-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
  padding-bottom: 0.75rem;
  border-bottom: 1px solid #A3D1C6;
}
.dark .question-header {
  border-bottom-color: #3D8D7A;
}

.question-header h4 {
  font-size: 1.125rem;
  font-weight: 600;
  color: #3D8D7A;
  margin: 0;
}
.dark .question-header h4 {
  color: #A3D1C6;
}

.remove-btn {
  background: none;
  border: none;
  color: #ef4444;
  font-size: 1.25rem;
  cursor: pointer;
  padding: 0.25rem;
  border-radius: 4px;
  transition: background 0.2s;
}
.remove-btn:hover {
  background: rgba(239, 68, 68, 0.1);
}

.question-body {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.form-select {
  padding: 0.7rem 1rem;
  border-radius: 8px;
  border: 1.5px solid #A3D1C6;
  background: #FBFFE4;
  font-size: 1rem;
  color: #1f2937;
  font-family: 'Inter', sans-serif;
  transition: border-color 0.2s, background 0.2s;
}
.form-select:focus {
  outline: none;
  border-color: #3D8D7A;
  background: #fff;
}
.dark .form-select {
  background: #23272b;
  color: #A3D1C6;
  border-color: #3D8D7A;
}
.dark .form-select:focus {
  background: #181c20;
  border-color: #A3D1C6;
}

.option-group {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.options-container {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.option-item {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.5rem;
  border-radius: 8px;
  background: white;
  border: 1px solid #A3D1C6;
}
.dark .option-item {
  background: #181c20;
  border-color: #3D8D7A;
}

.option-radio {
  margin: 0;
}

.option-letter {
  background: #3D8D7A;
  color: white;
  width: 24px;
  height: 24px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.875rem;
  font-weight: 600;
}

.option-input {
  flex: 1;
  padding: 0.5rem;
  border: 1px solid #A3D1C6;
  border-radius: 6px;
  background: #FBFFE4;
  font-size: 0.875rem;
}
.option-input:focus {
  outline: none;
  border-color: #3D8D7A;
}
.dark .option-input {
  background: #23272b;
  color: #A3D1C6;
  border-color: #3D8D7A;
}

.remove-option-btn {
  background: none;
  border: none;
  color: #ef4444;
  font-size: 1.125rem;
  cursor: pointer;
  padding: 0.25rem;
  border-radius: 4px;
  transition: background 0.2s;
}
.remove-option-btn:hover {
  background: rgba(239, 68, 68, 0.1);
}

.btn-add {
  background: #B3D8A8;
  color: #1f2937;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 6px;
  font-size: 0.875rem;
  font-weight: 600;
  cursor: pointer;
  transition: background 0.2s;
  align-self: flex-start;
}
.btn-add:hover {
  background: #9fcf94;
}

.tf-options {
  display: flex;
  gap: 1rem;
}

.tf-option {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1rem;
  border: 1px solid #A3D1C6;
  border-radius: 8px;
  background: white;
  cursor: pointer;
  transition: all 0.2s;
}
.tf-option:hover {
  border-color: #3D8D7A;
  background: #FBFFE4;
}
.tf-option.selected {
  border-color: #3D8D7A;
  background: #FBFFE4;
}
.dark .tf-option {
  background: #23272b;
  border-color: #3D8D7A;
  color: #A3D1C6;
}
.dark .tf-option:hover,
.dark .tf-option.selected {
  background: #181c20;
  border-color: #A3D1C6;
}

.tf-option input {
  margin: 0;
}

.add-question-card {
  background: white;
  border: 2px dashed #A3D1C6;
  border-radius: 12px;
  padding: 2rem;
  text-align: center;
  cursor: pointer;
  transition: all 0.2s;
}
.add-question-card:hover {
  border-color: #3D8D7A;
  background: #FBFFE4;
}
.dark .add-question-card {
  background: #23272b;
  border-color: #3D8D7A;
  color: #A3D1C6;
}
.dark .add-question-card:hover {
  background: #181c20;
  border-color: #A3D1C6;
}

.add-question-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.75rem;
}

.add-question-icon {
  font-size: 2rem;
  color: #3D8D7A;
  width: 48px;
  height: 48px;
  border-radius: 50%;
  background: #FBFFE4;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 0.5rem;
}
.dark .add-question-icon {
  color: #A3D1C6;
  background: #181c20;
}

.add-question-content h4 {
  font-size: 1.125rem;
  font-weight: 600;
  color: #3D8D7A;
  margin: 0;
}
.dark .add-question-content h4 {
  color: #A3D1C6;
}

.add-question-content p {
  font-size: 0.875rem;
  color: #6b7280;
  margin: 0;
}
.dark .add-question-content p {
  color: #A3D1C6;
}

/* Settings Section Styles */
.settings-container {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.setting-group {
  background: #FBFFE4;
  border: 1px solid #A3D1C6;
  border-radius: 12px;
  padding: 1.5rem;
  transition: all 0.2s;
}
.dark .setting-group {
  background: #23272b;
  border-color: #3D8D7A;
}

.setting-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 1rem;
}

.setting-header h4 {
  font-size: 1.125rem;
  font-weight: 600;
  color: #3D8D7A;
  margin: 0 0 0.25rem 0;
}
.dark .setting-header h4 {
  color: #A3D1C6;
}

.setting-header p {
  font-size: 0.875rem;
  color: #6b7280;
  margin: 0;
}
.dark .setting-header p {
  color: #A3D1C6;
}

.setting-content {
  margin-top: 1rem;
}

.toggle-switch {
  position: relative;
  display: inline-block;
  width: 48px;
  height: 24px;
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
  background-color: #ccc;
  transition: 0.2s;
  border-radius: 24px;
}

.toggle-slider:before {
  position: absolute;
  content: "";
  height: 18px;
  width: 18px;
  left: 3px;
  bottom: 3px;
  background-color: white;
  transition: 0.2s;
  border-radius: 50%;
}

.toggle-switch input:checked + .toggle-slider {
  background-color: #3D8D7A;
}

.toggle-switch input:checked + .toggle-slider:before {
  transform: translateX(24px);
}

.time-input-group {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.time-input-group input {
  width: 80px;
}

.time-unit {
  font-size: 0.875rem;
  color: #6b7280;
  font-weight: 500;
}
.dark .time-unit {
  color: #A3D1C6;
}

.attempts-options {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
}

.attempt-option {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1rem;
  border: 1px solid #A3D1C6;
  border-radius: 8px;
  background: white;
  cursor: pointer;
  transition: all 0.2s;
}
.attempt-option:hover {
  border-color: #3D8D7A;
  background: white;
}
.attempt-option.selected {
  border-color: #3D8D7A;
  background: white;
  box-shadow: 0 0 0 2px rgba(61, 141, 122, 0.1);
}
.dark .attempt-option {
  background: #181c20;
  border-color: #3D8D7A;
  color: #A3D1C6;
}
.dark .attempt-option:hover,
.dark .attempt-option.selected {
  background: #181c20;
  border-color: #A3D1C6;
}

.attempt-option input {
  margin: 0;
}

.schedule-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
}

@media (max-width: 768px) {
  .schedule-grid {
    grid-template-columns: 1fr;
  }
  
  .attempts-options {
    flex-direction: column;
  }
  
  .setting-header {
    flex-direction: column;
    align-items: flex-start;
    gap: 1rem;
  }
}

/* Preview Section Styles */
.quiz-preview-info {
  background: #FBFFE4;
  border: 1px solid #A3D1C6;
  border-radius: 12px;
  padding: 1.5rem;
  margin-bottom: 1.5rem;
}
.dark .quiz-preview-info {
  background: #23272b;
  border-color: #3D8D7A;
}

.preview-title {
  font-size: 1.25rem;
  font-weight: 600;
  color: #3D8D7A;
  margin: 0 0 0.5rem 0;
}
.dark .preview-title {
  color: #A3D1C6;
}

.preview-description {
  font-size: 0.875rem;
  color: #6b7280;
  margin: 0 0 1rem 0;
}
.dark .preview-description {
  color: #A3D1C6;
}

.preview-stats {
  display: flex;
  gap: 1.5rem;
  flex-wrap: wrap;
}

.stat-item {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}

.stat-label {
  font-size: 0.75rem;
  font-weight: 500;
  color: #6b7280;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}
.dark .stat-label {
  color: #A3D1C6;
}

.stat-value {
  font-size: 1rem;
  font-weight: 600;
  color: #3D8D7A;
}
.dark .stat-value {
  color: #A3D1C6;
}

.preview-questions {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.preview-question {
  background: white;
  border: 1px solid #A3D1C6;
  border-radius: 12px;
  padding: 1.5rem;
  transition: all 0.2s;
}
.dark .preview-question {
  background: #181c20;
  border-color: #3D8D7A;
}

.question-preview-header {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  margin-bottom: 1rem;
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
  font-size: 0.875rem;
  font-weight: 600;
}

.question-type-tag {
  background: #B3D8A8;
  color: #1f2937;
  padding: 0.25rem 0.75rem;
  border-radius: 20px;
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}
.question-type-tag.multiple_choice {
  background: #B3D8A8;
}
.question-type-tag.true_false {
  background: #A3D1C6;
}
.question-type-tag.fill_blank {
  background: #FBFFE4;
  border: 1px solid #A3D1C6;
}
.dark .question-type-tag {
  color: #1f2937;
}

.question-preview-text {
  font-size: 1rem;
  font-weight: 500;
  color: #1f2937;
  margin: 0 0 1rem 0;
  line-height: 1.5;
}
.dark .question-preview-text {
  color: #A3D1C6;
}

.preview-options {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.preview-option {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.75rem;
  border: 1px solid #e5e7eb;
  border-radius: 8px;
  background: #f9fafb;
  transition: all 0.2s;
}
.preview-option.correct {
  border-color: #3D8D7A;
  background: rgba(61, 141, 122, 0.1);
}
.dark .preview-option {
  background: #23272b;
  border-color: #3D8D7A;
  color: #A3D1C6;
}
.dark .preview-option.correct {
  background: rgba(61, 141, 122, 0.2);
  border-color: #A3D1C6;
}

.option-letter {
  background: #6b7280;
  color: white;
  width: 24px;
  height: 24px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.75rem;
  font-weight: 600;
  flex-shrink: 0;
}
.preview-option.correct .option-letter {
  background: #3D8D7A;
}

.option-text {
  flex: 1;
  font-size: 0.875rem;
  color: #1f2937;
}
.dark .option-text {
  color: #A3D1C6;
}

.correct-indicator {
  color: #3D8D7A;
  font-weight: 600;
  font-size: 1rem;
}
.dark .correct-indicator {
  color: #A3D1C6;
}

.preview-fill-blank {
  padding: 0.75rem;
  border: 1px solid #e5e7eb;
  border-radius: 8px;
  background: #f9fafb;
}
.dark .preview-fill-blank {
  background: #23272b;
  border-color: #3D8D7A;
}

.fill-answer-display {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.answer-label {
  font-size: 0.875rem;
  font-weight: 500;
  color: #6b7280;
}
.dark .answer-label {
  color: #A3D1C6;
}

.answer-text {
  font-size: 0.875rem;
  font-weight: 600;
  color: #3D8D7A;
  background: rgba(61, 141, 122, 0.1);
  padding: 0.25rem 0.5rem;
  border-radius: 4px;
}
.dark .answer-text {
  color: #A3D1C6;
  background: rgba(163, 209, 198, 0.1);
}

@media (max-width: 768px) {
  .preview-stats {
    flex-direction: column;
    gap: 1rem;
  }
  
  .question-preview-header {
    flex-wrap: wrap;
  }
}

/* Custom Modal Styles */
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
  backdrop-filter: blur(4px);
}

.modal-content {
  background: white;
  border-radius: 16px;
  padding: 0;
  max-width: 480px;
  width: 90%;
  max-height: 90vh;
  overflow: hidden;
  box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
  animation: modalSlideIn 0.3s ease-out;
}
.dark .modal-content {
  background: #23272b;
  border: 1px solid #3D8D7A;
  box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.3), 0 10px 10px -5px rgba(0, 0, 0, 0.2);
}

@keyframes modalSlideIn {
  from {
    opacity: 0;
    transform: translateY(-20px) scale(0.95);
  }
}
.modal-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1.5rem;
  border-bottom: 1px solid #e5e7eb;
}
.dark .modal-header {
  border-bottom-color: #3D8D7A;
}

.modal-header h3 {
  font-size: 1.25rem;
  font-weight: 600;
  color: #1f2937;
  margin: 0;
}
.dark .modal-header h3 {
  color: #A3D1C6;
}

.modal-close {
  background: none;
  border: none;
  font-size: 1.5rem;
  color: #6b7280;
  cursor: pointer;
  padding: 0.25rem;
  border-radius: 4px;
  transition: all 0.2s;
  width: 32px;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
}
.modal-close:hover {
  background: rgba(107, 114, 128, 0.1);
  color: #374151;
}
.dark .modal-close {
  color: #A3D1C6;
}
.dark .modal-close:hover {
  background: rgba(163, 209, 198, 0.1);
  color: #A3D1C6;
}

.modal-body {
  padding: 1.5rem;
  display: flex;
  gap: 1rem;
  align-items: flex-start;
}

.modal-icon {
  color: #3D8D7A;
  flex-shrink: 0;
}
.dark .modal-icon {
  color: #A3D1C6;
}

.modal-text {
  flex: 1;
}

.modal-title {
  font-size: 1rem;
  font-weight: 600;
  color: #1f2937;
  margin: 0 0 0.5rem 0;
  line-height: 1.5;
}
.dark .modal-title {
  color: #A3D1C6;
}

.modal-description {
  font-size: 0.875rem;
  color: #6b7280;
  margin: 0;
  line-height: 1.5;
}
.dark .modal-description {
  color: #A3D1C6;
}

.modal-actions {
  display: flex;
  gap: 0.75rem;
  padding: 1.5rem;
  border-top: 1px solid #e5e7eb;
  justify-content: flex-end;
}
.dark .modal-actions {
  border-top-color: #3D8D7A;
}

.modal-actions .btn {
  min-width: 80px;
  justify-content: center;
}

@media (max-width: 640px) {
  .modal-content {
    width: 95%;
    margin: 1rem;
  }
  
  .modal-body {
    flex-direction: column;
    text-align: center;
  }
  
  .modal-actions {
    flex-direction: column-reverse;
  }
  
  .modal-actions .btn {
    width: 100%;
  }
}

</style>
