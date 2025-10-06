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
                    Start Date & Time
                  </label>
                  <input v-model="quiz.settings.startDate" type="datetime-local" class="form-input enhanced-input" />
                </div>
                <div class="form-group">
                  <label class="form-label-small">
                    <span class="label-icon">🕕</span>
                    End Date & Time
                  </label>
                  <input v-model="quiz.settings.endDate" type="datetime-local" class="form-input enhanced-input" />
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

        console.log('Teacher info loaded:', teacherInfo.value);
        return true;
      } catch (error) {
        console.error('Error loading teacher info:', error);
        alert('Failed to load teacher information. Please refresh the page.');
        return false;
      }
    };

    const loadRouteParams = () => {
      console.log('Loading route params...');
      console.log('Route params:', route.params);
      console.log('Route query:', route.query);

      const subjectId = route.params.subjectId;
      const sectionId = route.params.sectionId;
      const subjectName = route.query.subjectName || 'Subject';
      const sectionName = route.query.sectionName || '';

      if (!subjectId || !sectionId) {
        console.error('Missing required route parameters');
        return false;
      }

      subject.value = {
        id: subjectId,
        name: subjectName
      };

      section.value = {
        id: sectionId,
        name: sectionName
      };

      console.log('Route params loaded:', {
        subject: subject.value,
        section: section.value
      });

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
            console.log('New quiz created (real-time):', payload.new);
          }
        )
        .subscribe((status) => {
          console.log('Real-time subscription status:', status);
        });
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

    const publishQuiz = async () => {
      console.log('Starting quiz publication...');
      
      if (!validateQuiz()) {
        console.log('Validation failed');
        return;
      }

      if (!confirm(`Are you sure you want to publish "${quiz.value.title}"?\n\nStudents will be able to see and take this quiz immediately.`)) {
        return;
      }

      isPublishing.value = true;

      try {
        // Verify all required data is present
        if (!subject.value.id || !section.value.id || !teacherInfo.value.teacher_id) {
          throw new Error('Missing required information. Please reload the page and try again.');
        }

        console.log('Creating quiz with:', {
          subjectId: subject.value.id,
          sectionId: section.value.id,
          teacherId: teacherInfo.value.teacher_id
        });

        // Prepare quiz data - FIXED to match database schema
        const quizData = {
          subject_id: subject.value.id,
          section_id: section.value.id,
          teacher_id: teacherInfo.value.teacher_id,
          title: quiz.value.title.trim(),
          description: quiz.value.description.trim() || null,
          number_of_questions: parseInt(quiz.value.numberOfQuestions),
          status: 'published',
          attempts_allowed: parseInt(quiz.value.settings.attemptsAllowed),
          shuffle_questions: quiz.value.settings.shuffle,
          shuffle_options: quiz.value.settings.shuffle,
          start_date: quiz.value.settings.startDate || null,
          end_date: quiz.value.settings.endDate || null,
          has_time_limit: quiz.value.settings.hasTimeLimit,
          time_limit_minutes: quiz.value.settings.hasTimeLimit 
            ? parseInt(quiz.value.settings.timeLimit) 
            : null,
          created_at: new Date().toISOString(),
          updated_at: new Date().toISOString()
        };

        console.log('Inserting quiz:', quizData);

        // Insert quiz into database
        const { data: newQuiz, error: quizError } = await supabase
          .from('quizzes')
          .insert([quizData])
          .select()
          .single();

        if (quizError) {
          console.error('Quiz insertion error:', quizError);
          throw new Error(`Failed to create quiz: ${quizError.message}`);
        }

        if (!newQuiz || !newQuiz.id) {
          throw new Error('Quiz was not created properly');
        }

        console.log('Quiz created with ID:', newQuiz.id);

        // Prepare questions data
        const questionsData = quiz.value.questions.map((q, index) => ({
          quiz_id: newQuiz.id,
          question_number: index + 1,
          question_type: q.type,
          question_text: q.text.trim(),
          points: 1,
          created_at: new Date().toISOString()
        }));

        console.log('Inserting questions:', questionsData);

        // Insert questions
        const { data: insertedQuestions, error: questionsError } = await supabase
          .from('quiz_questions')
          .insert(questionsData)
          .select();

        if (questionsError) {
          console.error('Questions insertion error:', questionsError);
          // Try to delete the quiz if questions failed
          await supabase.from('quizzes').delete().eq('id', newQuiz.id);
          throw new Error(`Failed to add questions: ${questionsError.message}`);
        }

        console.log('Questions created successfully:', insertedQuestions);

        // Now insert options and answers for each question
        for (let i = 0; i < quiz.value.questions.length; i++) {
          const question = quiz.value.questions[i];
          const questionId = insertedQuestions[i].id;

          if (question.type === 'multiple_choice') {
            // Insert options
            const optionsData = question.options.map((opt, optIndex) => ({
              question_id: questionId,
              option_number: optIndex + 1,
              option_text: opt.trim(),
              is_correct: question.correctAnswer === optIndex,
              created_at: new Date().toISOString()
            }));

            const { error: optionsError } = await supabase
              .from('question_options')
              .insert(optionsData);

            if (optionsError) {
              console.error('Options insertion error:', optionsError);
              // Cleanup: delete quiz and questions
              await supabase.from('quizzes').delete().eq('id', newQuiz.id);
              throw new Error(`Failed to add options for question ${i + 1}: ${optionsError.message}`);
            }

          } else if (question.type === 'true_false' || question.type === 'fill_blank') {
            // Insert answer
            const answerData = {
              question_id: questionId,
              correct_answer: String(question.correctAnswer),
              case_sensitive: question.type === 'fill_blank',
              created_at: new Date().toISOString()
            };

            const { error: answerError } = await supabase
              .from('question_answers')
              .insert([answerData]);

            if (answerError) {
              console.error('Answer insertion error:', answerError);
              // Cleanup: delete quiz and questions
              await supabase.from('quizzes').delete().eq('id', newQuiz.id);
              throw new Error(`Failed to add answer for question ${i + 1}: ${answerError.message}`);
            }
          }
        }

        console.log('All questions, options, and answers created successfully');
        
        // Success!
        alert('✅ Quiz published successfully!\n\nStudents can now see and take this quiz.\n\nRedirecting to My Subjects...');
        
        // Small delay
        await new Promise(resolve => setTimeout(resolve, 500));
        
        // Navigate back
        await router.push('/teacher/subjects');
        
      } catch (error) {
        console.error('Error publishing quiz:', error);
        
        let errorMessage = 'Failed to publish quiz.\n\n';
        
        if (error.message) {
          errorMessage += `Error: ${error.message}\n\n`;
        }
        
        if (error.message && error.message.includes('violates foreign key constraint')) {
          errorMessage += 'Database relationship error. Please ensure the subject and section exist.\n\n';
        }
        
        errorMessage += 'Please check your connection and try again.';
        
        alert(errorMessage);
      } finally {
        isPublishing.value = false;
      }
    };

    onMounted(async () => {
      console.log('CreateQuiz component mounted');
      
      // Load teacher information first
      const teacherLoaded = await loadTeacherInfo();
      if (!teacherLoaded) {
        router.push('/login');
        return;
      }
      
      // Load route parameters
      const paramsLoaded = loadRouteParams();
      if (!paramsLoaded) {
        console.error('Failed to load route parameters');
        alert('Missing subject or section information. Redirecting back...');
        router.push('/teacher/subjects');
        return;
      }

      // Setup real-time subscription
      setupRealtimeSubscription();
      
      console.log('Component initialized successfully:', {
        teacher: teacherInfo.value,
        subject: subject.value,
        section: section.value
      });
    });

    onUnmounted(() => {
      if (quizSubscription) {
        supabase.removeChannel(quizSubscription);
        console.log('Real-time subscription cleaned up');
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
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

/* Base Styles */
.create-quiz-page {
  padding: 2rem;
  max-width: 1400px;
  margin: 0 auto;
  background: var(--bg-primary);
  min-height: 100vh;
  color: var(--primary-text-color);
  transition: all 0.3s ease;
}

.section-header-card {
  margin-bottom: 2rem;
  position: relative;
  overflow: hidden;
  background: rgba(248, 250, 252, 0.9);
  backdrop-filter: blur(20px);
  border-radius: 32px;
  padding: 3.5rem;
  border: 1px solid rgba(255, 255, 255, 0.8);
  min-height: 180px;
  box-shadow: 
    0 20px 40px rgba(0, 0, 0, 0.06),
    0 10px 20px rgba(0, 0, 0, 0.04),
    inset 0 1px 0 rgba(255, 255, 255, 0.8);
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.section-header-card:hover {
  transform: translateY(-4px) scale(1.005);
  box-shadow: 
    0 35px 70px rgba(16, 185, 129, 0.12),
    0 20px 40px rgba(0, 0, 0, 0.08),
    0 12px 24px rgba(16, 185, 129, 0.06),
    inset 0 1px 0 rgba(255, 255, 255, 0.95),
    inset 0 0 0 1px rgba(16, 185, 129, 0.1);
  border-color: rgba(16, 185, 129, 0.15);
}

.header-bg-decoration {
  position: absolute;
  top: -50%;
  right: -20%;
  width: 140%;
  height: 220%;
  background: 
    radial-gradient(ellipse 60% 40% at 70% 30%, rgba(16, 185, 129, 0.12) 0%, transparent 60%),
    radial-gradient(ellipse 40% 60% at 30% 70%, rgba(5, 150, 105, 0.08) 0%, transparent 50%),
    linear-gradient(135deg, rgba(16, 185, 129, 0.05) 0%, transparent 80%);
  z-index: 1;
  opacity: 0.8;
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
  gap: 2rem;
}

.section-header-icon {
  width: 88px;
  height: 88px;
  background: 
    linear-gradient(135deg, #10b981 0%, #059669 50%, #047857 100%),
    linear-gradient(225deg, rgba(255, 255, 255, 0.2) 0%, transparent 50%);
  border-radius: 28px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #fff;
  box-shadow: 
    0 12px 32px rgba(16, 185, 129, 0.35),
    0 6px 16px rgba(16, 185, 129, 0.2),
    inset 0 1px 0 rgba(255, 255, 255, 0.3),
    inset 0 -1px 0 rgba(0, 0, 0, 0.1);
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  position: relative;
  overflow: hidden;
}

.section-header-icon:hover {
  transform: translateY(-3px) scale(1.05);
  box-shadow: 
    0 16px 40px rgba(16, 185, 129, 0.4),
    0 8px 20px rgba(16, 185, 129, 0.25),
    inset 0 1px 0 rgba(255, 255, 255, 0.4),
    inset 0 -1px 0 rgba(0, 0, 0, 0.15);
}

.section-header-icon::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.3), transparent);
  transition: left 0.6s;
}

.section-header-icon:hover::before {
  left: 100%;
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

.back-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  background: 
    linear-gradient(135deg, rgba(255,255,255,0.7), rgba(248,250,252,0.7));
  border: 2px solid rgba(16,185,129,0.15);
  border-radius: 12px;
  padding: 0.7rem 1.4rem;
  color: #10b981;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  font-size: 0.95rem;
  position: relative;
  overflow: hidden;
  box-shadow: 0 2px 6px rgba(16, 185, 129, 0.06);
}

.back-btn::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(16, 185, 129, 0.1), transparent);
  transition: left 0.4s ease;
}

.back-btn:hover {
  background: linear-gradient(135deg, #f0fdf4, #dcfce7);
  border-color: #10b981;
  color: #065f46;
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(16, 185, 129, 0.15);
}

.back-btn:hover::before {
  left: 100%;
}

.floating-shapes {
  position: absolute;
  top: 0;
  right: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
  z-index: 1;
  overflow: hidden;
}

.shape {
  position: absolute;
  border-radius: 50%;
  filter: blur(0.5px);
  opacity: 0.8;
}

.shape-1 {
  width: 120px;
  height: 120px;
  top: -25px;
  right: 12%;
  background: 
    radial-gradient(circle at 30% 30%, rgba(16, 185, 129, 0.15) 0%, rgba(16, 185, 129, 0.08) 40%, transparent 70%),
    linear-gradient(135deg, rgba(5, 150, 105, 0.12) 0%, rgba(16, 185, 129, 0.06) 50%, transparent 100%);
  animation: float 8s ease-in-out infinite, shimmer 4s ease-in-out infinite alternate;
  box-shadow: 
    0 8px 32px rgba(16, 185, 129, 0.1),
    inset 0 1px 0 rgba(255, 255, 255, 0.2);
}

.shape-2 {
  width: 80px;
  height: 80px;
  bottom: -15px;
  right: 28%;
  background: 
    radial-gradient(circle at 70% 70%, rgba(5, 150, 105, 0.12) 0%, rgba(16, 185, 129, 0.06) 40%, transparent 70%),
    linear-gradient(225deg, rgba(16, 185, 129, 0.1) 0%, rgba(4, 120, 87, 0.05) 50%, transparent 100%);
  animation: float 10s ease-in-out infinite reverse, pulse 6s ease-in-out infinite;
  box-shadow: 
    0 6px 24px rgba(5, 150, 105, 0.08),
    inset 0 1px 0 rgba(255, 255, 255, 0.15);
}

.shape-3 {
  width: 100px;
  height: 100px;
  top: 45%;
  right: 3%;
  background: 
    radial-gradient(circle at 50% 20%, rgba(16, 185, 129, 0.14) 0%, rgba(5, 150, 105, 0.08) 45%, transparent 75%),
    linear-gradient(315deg, rgba(4, 120, 87, 0.1) 0%, rgba(16, 185, 129, 0.05) 60%, transparent 100%);
  animation: float 12s ease-in-out infinite, rotate 20s linear infinite;
  box-shadow: 
    0 10px 30px rgba(16, 185, 129, 0.12),
    inset 0 1px 0 rgba(255, 255, 255, 0.18);
}

.shape-4 {
  width: 60px;
  height: 60px;
  top: 20%;
  right: 40%;
  background: 
    radial-gradient(circle at 60% 40%, rgba(16, 185, 129, 0.1) 0%, transparent 60%);
  animation: float 9s ease-in-out infinite, fade 8s ease-in-out infinite alternate;
  border-radius: 60% 40% 30% 70% / 60% 30% 70% 40%;
}

.shape-5 {
  width: 40px;
  height: 40px;
  bottom: 30%;
  right: 8%;
  background: 
    linear-gradient(135deg, rgba(5, 150, 105, 0.08) 0%, rgba(16, 185, 129, 0.04) 100%);
  animation: float 7s ease-in-out infinite reverse, scale 5s ease-in-out infinite alternate;
  border-radius: 30% 70% 70% 30% / 30% 30% 70% 70%;
}

@keyframes float {
  0%, 100% { transform: translateY(0) translateX(0) rotate(0deg); }
  25% { transform: translateY(-12px) translateX(8px) rotate(5deg); }
  50% { transform: translateY(-20px) translateX(0) rotate(10deg); }
  75% { transform: translateY(-8px) translateX(-6px) rotate(5deg); }
}

@keyframes shimmer {
  0% { opacity: 0.6; filter: blur(0.5px) brightness(1); }
  100% { opacity: 0.9; filter: blur(0.3px) brightness(1.1); }
}

@keyframes pulse {
  0%, 100% { transform: scale(1); opacity: 0.7; }
  50% { transform: scale(1.1); opacity: 0.9; }
}

@keyframes rotate {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

@keyframes fade {
  0% { opacity: 0.4; }
  100% { opacity: 0.8; }
}

@keyframes scale {
  0% { transform: scale(0.8); }
  100% { transform: scale(1.2); }
}

/* Progress Section */
.progress-container {
  max-width: 1400px;
  margin: 2rem auto;
  padding: 0 2rem;
  position: relative;
  z-index: 5;
}

.progress-card {
  background: rgba(248, 250, 252, 0.9);
  backdrop-filter: blur(20px);
  border-radius: 24px;
  padding: 2.5rem;
  box-shadow: 
    0 12px 40px rgba(16, 185, 129, 0.12),
    0 6px 20px rgba(0, 0, 0, 0.08),
    0 3px 10px rgba(16, 185, 129, 0.06),
    inset 0 1px 0 rgba(255, 255, 255, 0.9);
  border: 2px solid rgba(16, 185, 129, 0.08);
}

.progress-track {
  display: flex;
  align-items: center;
  justify-content: space-between;
  position: relative;
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
  top: 28px;
  left: 50%;
  right: -50%;
  height: 3px;
  background: linear-gradient(90deg, #e2e8f0, #cbd5e0);
  z-index: 1;
  transition: all 0.3s ease;
}

.step-line.completed {
  background: linear-gradient(90deg, #10b981 0%, #059669 100%);
  box-shadow: 0 0 10px rgba(16, 185, 129, 0.5);
}

.step-indicator {
  position: relative;
  z-index: 2;
  margin-bottom: 1rem;
}

.step-circle {
  width: 56px;
  height: 56px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 1.1rem;
  transition: all 0.3s ease;
  background: #e2e8f0;
  color: #64748b;
  border: 3px solid #e2e8f0;
}

.step-indicator.active .step-circle,
.step-indicator.completed .step-circle {
  background: linear-gradient(135deg, #10b981 0%, #059669 100%);
  color: white;
  border-color: transparent;
  transform: scale(1.1);
  box-shadow: 
    0 12px 32px rgba(16, 185, 129, 0.35),
    0 6px 16px rgba(16, 185, 129, 0.2);
  animation: pulse 2s ease-in-out infinite;
}

.step-label {
  font-size: 0.95rem;
  font-weight: 600;
  color: #64748b;
  text-align: center;
}

.step-indicator.active + .step-label,
.step-indicator.completed + .step-label {
  color: #10b981;
  font-weight: 700;
}

@keyframes pulse {
  0%, 100% { box-shadow: 0 12px 32px rgba(16, 185, 129, 0.35), 0 6px 16px rgba(16, 185, 129, 0.2); }
  50% { box-shadow: 0 16px 40px rgba(16, 185, 129, 0.45), 0 8px 20px rgba(16, 185, 129, 0.3); }
}

/* Main Content */
.main-content {
  max-width: 1400px;
  margin: 0 auto;
  padding: 0 2rem 4rem;
  position: relative;
  z-index: 5;
}

/* Landing Section */
.landing-section {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 70vh;
}

.landing-card {
  background: rgba(248, 250, 252, 0.9);
  backdrop-filter: blur(20px);
  border-radius: 24px;
  padding: 4rem 3rem;
  text-align: center;
  box-shadow: 
    0 12px 40px rgba(16, 185, 129, 0.12),
    0 6px 20px rgba(0, 0, 0, 0.08),
    0 3px 10px rgba(16, 185, 129, 0.06),
    inset 0 1px 0 rgba(255, 255, 255, 0.9);
  border: 2px solid rgba(16, 185, 129, 0.08);
  max-width: 700px;
  width: 100%;
  position: relative;
  overflow: hidden;
}

.landing-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 4px;
  background: linear-gradient(90deg, #10b981 0%, #059669 100%);
}

.landing-icon {
  position: relative;
  width: 120px;
  height: 120px;
  margin: 0 auto 2rem;
}

.icon-bg {
  width: 100%;
  height: 100%;
  background: linear-gradient(135deg, #10b981 0%, #059669 50%, #047857 100%);
  border-radius: 24px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  position: relative;
  z-index: 2;
  animation: iconFloat 3s ease-in-out infinite;
}

.icon-glow {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 140px;
  height: 140px;
  background: radial-gradient(circle, rgba(16, 185, 129, 0.3) 0%, transparent 70%);
  border-radius: 50%;
  animation: glow 2s ease-in-out infinite alternate;
}

@keyframes iconFloat {
  0%, 100% { transform: translateY(0px); }
  50% { transform: translateY(-10px); }
}

@keyframes glow {
  0% { opacity: 0.5; transform: translate(-50%, -50%) scale(1); }
  100% { opacity: 1; transform: translate(-50%, -50%) scale(1.1); }
}

.landing-card h2 {
  font-size: 2.5rem;
  font-weight: 800;
  background: linear-gradient(135deg, #10b981 0%, #059669 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  margin-bottom: 1rem;
}

.landing-card p {
  font-size: 1.2rem;
  color: #64748b;
  margin-bottom: 2rem;
  line-height: 1.6;
}

.features-preview {
  display: flex;
  justify-content: center;
  gap: 2rem;
  margin-bottom: 2.5rem;
  flex-wrap: wrap;
}

.feature-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.5rem;
  padding: 1rem;
  background: rgba(16, 185, 129, 0.1);
  border-radius: 16px;
  border: 1px solid rgba(16, 185, 129, 0.2);
  transition: all 0.3s ease;
}

.feature-item:hover {
  transform: translateY(-5px);
  background: rgba(16, 185, 129, 0.15);
  box-shadow: 
    0 8px 25px rgba(16, 185, 129, 0.15),
    0 4px 12px rgba(16, 185, 129, 0.1);
}

.feature-icon {
  font-size: 2rem;
}

.create-quiz-btn {
  position: relative;
  padding: 1.25rem 2.5rem;
  background: 
    linear-gradient(135deg, #10b981 0%, #059669 50%, #047857 100%) !important;
  color: white !important;
  border: none !important;
  border-radius: 16px !important;
  font-weight: 700 !important;
  font-size: 1.1rem !important;
  cursor: pointer !important;
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1) !important;
  box-shadow: 
    0 10px 30px rgba(16, 185, 129, 0.35),
    0 5px 15px rgba(16, 185, 129, 0.2),
    inset 0 1px 0 rgba(255, 255, 255, 0.3) !important;
  overflow: hidden !important;
  letter-spacing: 0.025em !important;
  position: relative !important;
}

.create-quiz-btn:hover {
  background: 
    linear-gradient(135deg, #059669 0%, #047857 50%, #065f46 100%) !important;
  transform: translateY(-3px) scale(1.05) !important;
  box-shadow: 
    0 15px 40px rgba(16, 185, 129, 0.45),
    0 8px 20px rgba(16, 185, 129, 0.3),
    inset 0 1px 0 rgba(255, 255, 255, 0.4) !important;
}

/* Card Styles */
.content-card {
  background: rgba(248, 250, 252, 0.9);
  backdrop-filter: blur(20px);
  border-radius: 24px;
  padding: 3rem;
  box-shadow: 
    0 12px 40px rgba(16, 185, 129, 0.12),
    0 6px 20px rgba(0, 0, 0, 0.08),
    0 3px 10px rgba(16, 185, 129, 0.06),
    inset 0 1px 0 rgba(255, 255, 255, 0.9);
  border: 2px solid rgba(16, 185, 129, 0.08);
  margin-bottom: 2rem;
  position: relative;
  overflow: hidden;
}

.content-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 4px;
  background: linear-gradient(90deg, #10b981 0%, #059669 100%);
}

/* Section Headers */
.section-header {
  display: flex;
  align-items: center;
  gap: 1.5rem;
  margin-bottom: 3rem;
  padding-bottom: 1.5rem;
  border-bottom: 2px solid rgba(16, 185, 129, 0.1);
}

.section-icon {
  width: 56px;
  height: 56px;
  background: linear-gradient(135deg, #10b981 0%, #059669 100%);
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  box-shadow: 
    0 12px 32px rgba(16, 185, 129, 0.35),
    0 6px 16px rgba(16, 185, 129, 0.2);
}

.section-content {
  flex: 1;
}

.section-title {
  font-size: 2rem;
  font-weight: 700;
  color: #1f2937;
  margin: 0 0 0.5rem 0;
}

.section-subtitle {
  color: #64748b;
  font-size: 1.1rem;
  margin: 0;
}

.question-counter {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%);
  color: white;
  padding: 0.75rem 1.5rem;
  border-radius: 16px;
  font-weight: 700;
  font-size: 1.1rem;
  box-shadow: 
    0 8px 25px rgba(67, 233, 123, 0.3),
    0 4px 12px rgba(67, 233, 123, 0.2);
}

.counter-icon {
  font-size: 1.2rem;
}

/* Form Styles */
.form-section {
  margin-bottom: 2rem;
}

.form-grid {
  display: grid;
  grid-template-columns: 1fr 200px;
  gap: 2rem;
  margin-bottom: 2rem;
}

.form-group {
  margin-bottom: 1.5rem;
}

.form-label {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-weight: 600;
  color: #1f2937;
  margin-bottom: 0.75rem;
  font-size: 1rem;
}

.label-icon {
  font-size: 1.1rem;
}

.form-input {
  width: 100%;
  padding: 1rem 1.25rem;
  border: 2px solid #e2e8f0;
  border-radius: 16px;
  font-size: 1rem;
  transition: all 0.3s ease;
  background: rgba(255, 255, 255, 0.8);
  backdrop-filter: blur(10px);
}

.enhanced-input {
  border-color: rgba(16, 185, 129, 0.2);
  background: rgba(255, 255, 255, 0.9);
}

.enhanced-input:focus {
  outline: none;
  border-color: #10b981;
  box-shadow: 0 0 0 3px rgba(16, 185, 129, 0.15);
  background: rgba(255, 255, 255, 1);
}

.form-textarea {
  resize: vertical;
  min-height: 120px;
}

.form-select {
  appearance: none;
  background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' fill='none' viewBox='0 0 20 20'%3e%3cpath stroke='%2310b981' stroke-linecap='round' stroke-linejoin='round' stroke-width='1.5' d='m6 8 4 4 4-4'/%3e%3c/svg%3e");
  background-position: right 1rem center;
  background-repeat: no-repeat;
  background-size: 1.5em 1.5em;
  padding-right: 3rem;
}

/* Button Styles */
.btn {
  display: inline-flex;
  align-items: center;
  gap: 0.75rem;
  padding: 1rem 1.75rem;
  border-radius: 16px;
  font-weight: 600;
  font-size: 1rem;
  cursor: pointer;
  transition: all 0.3s ease;
  border: none;
  position: relative;
  overflow: hidden;
}

.btn-primary {
  background: linear-gradient(135deg, #10b981 0%, #059669 100%);
  color: white;
  box-shadow: 
    0 8px 25px rgba(16, 185, 129, 0.3),
    0 4px 12px rgba(16, 185, 129, 0.2);
}

.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 
    0 12px 35px rgba(16, 185, 129, 0.4),
    0 6px 18px rgba(16, 185, 129, 0.25);
}

.btn-secondary {
  background: rgba(255, 255, 255, 0.8);
  color: #64748b;
  border: 2px solid #e2e8f0;
  backdrop-filter: blur(10px);
}

.btn-secondary:hover {
  background: rgba(255, 255, 255, 1);
  color: #1f2937;
  border-color: #10b981;
  transform: translateY(-2px);
}

.btn-success {
  background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%);
  color: white;
  box-shadow: 0 4px 15px rgba(67, 233, 123, 0.3);
}

.btn-success:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(67, 233, 123, 0.4);
}

.btn-danger {
  background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
  color: white;
  box-shadow: 0 4px 15px rgba(245, 87, 108, 0.3);
}

.btn-danger:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(245, 87, 108, 0.4);
}

.btn-publish {
  background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
  color: white;
  padding: 1.25rem 2.5rem;
  font-size: 1.2rem;
  font-weight: 700;
  box-shadow: 0 8px 25px rgba(79, 172, 254, 0.4);
}

.btn-publish:hover {
  transform: translateY(-3px) scale(1.02);
  box-shadow: 0 12px 35px rgba(79, 172, 254, 0.6);
}

/* Question Cards */
.questions-container {
  display: flex;
  flex-direction: column;
  gap: 2rem;
  margin-bottom: 3rem;
}

.question-card {
  background: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(15px);
  border: 2px solid rgba(16, 185, 129, 0.1);
  border-radius: 24px;
  padding: 2rem;
  transition: all 0.3s ease;
}

.enhanced-card:hover {
  border-color: rgba(16, 185, 129, 0.3);
  box-shadow: 
    0 8px 30px rgba(16, 185, 129, 0.12),
    0 4px 15px rgba(16, 185, 129, 0.08);
  transform: translateY(-5px);
}

.question-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
  padding-bottom: 1rem;
  border-bottom: 1px solid rgba(16, 185, 129, 0.1);
}

.question-number {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.question-badge {
  width: 48px;
  height: 48px;
  background: linear-gradient(135deg, #10b981 0%, #059669 100%);
  color: white;
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 1.2rem;
  box-shadow: 
    0 8px 25px rgba(16, 185, 129, 0.3),
    0 4px 12px rgba(16, 185, 129, 0.2);
}

.question-title {
  font-size: 1.3rem;
  font-weight: 600;
  color: #1f2937;
  margin: 0;
}

.delete-btn {
  width: 44px;
  height: 44px;
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease;
}

.delete-btn:hover {
  transform: scale(1.1);
}

/* Options */
.options-container {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  margin-bottom: 1.5rem;
}

.option-item {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1rem;
  border: 2px solid #e2e8f0;
  border-radius: 16px;
  transition: all 0.3s ease;
  background: rgba(255, 255, 255, 0.8);
}

.enhanced-option:hover {
  border-color: rgba(16, 185, 129, 0.3);
  background: rgba(16, 185, 129, 0.05);
  transform: translateX(5px);
}

.option-radio {
  width: 20px;
  height: 20px;
  accent-color: #10b981;
}

.option-letter {
  width: 32px;
  height: 32px;
  background: linear-gradient(135deg, #10b981 0%, #059669 100%);
  color: white;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 0.9rem;
}

.option-input {
  flex: 1;
  border: none;
  background: transparent;
  font-size: 1rem;
  padding: 0.5rem;
  color: #1f2937;
}

.option-input:focus {
  outline: none;
}

.remove-option-btn {
  width: 36px;
  height: 36px;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease;
}

.remove-option-btn:hover {
  transform: scale(1.1);
}

.add-option-btn {
  align-self: flex-start;
  margin-top: 0.5rem;
}

/* True/False Options */
.tf-options {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.5rem;
  margin-top: 1rem;
}

.tf-option {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 2rem;
  border: 3px solid #e2e8f0;
  border-radius: 16px;
  cursor: pointer;
  transition: all 0.3s ease;
  background: rgba(255, 255, 255, 0.8);
}

.tf-option:hover {
  border-color: rgba(16, 185, 129, 0.3);
  background: rgba(16, 185, 129, 0.05);
  transform: translateY(-5px);
}

.tf-option.selected {
  border-color: #10b981;
  background: rgba(16, 185, 129, 0.1);
  box-shadow: 
    0 8px 25px rgba(16, 185, 129, 0.15),
    0 4px 12px rgba(16, 185, 129, 0.1);
}

.tf-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
}

.tf-icon {
  font-size: 3rem;
}

.tf-label {
  font-weight: 700;
  color: #1f2937;
  font-size: 1.2rem;
}

/* Add Question Card */
.add-question-card {
  border: 3px dashed rgba(16, 185, 129, 0.3);
  border-radius: 24px;
  padding: 3rem;
  text-align: center;
  cursor: pointer;
  transition: all 0.3s ease;
  background: rgba(16, 185, 129, 0.02);
}

.add-question-card:hover {
  border-color: rgba(16, 185, 129, 0.5);
  background: rgba(16, 185, 129, 0.05);
  transform: translateY(-5px);
}

.add-question-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
}

.add-question-icon {
  width: 80px;
  height: 80px;
  background: linear-gradient(135deg, #10b981 0%, #059669 100%);
  border-radius: 24px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  box-shadow: 
    0 8px 25px rgba(16, 185, 129, 0.15),
    0 4px 12px rgba(16, 185, 129, 0.1);
}

.add-question-content h3 {
  font-size: 1.5rem;
  font-weight: 700;
  color: #1f2937;
  margin: 0;
}

.add-question-content p {
  color: #64748b;
  margin: 0;
  font-size: 1.1rem;
}

/* Settings */
.settings-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
  margin-bottom: 3rem;
}

.setting-card {
  background: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(15px);
  border: 2px solid rgba(16, 185, 129, 0.1);
  border-radius: 24px;
  padding: 2rem;
  transition: all 0.3s ease;
}

.enhanced-setting:hover {
  border-color: rgba(16, 185, 129, 0.3);
  box-shadow: 
    0 8px 30px rgba(16, 185, 129, 0.12),
    0 4px 15px rgba(16, 185, 129, 0.08);
  transform: translateY(-5px);
}

.schedule-card {
  grid-column: 1 / -1;
}

.setting-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1.5rem;
}

.setting-info {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.setting-emoji {
  font-size: 2.5rem;
}

.setting-details h3 {
  font-size: 1.3rem;
  font-weight: 700;
  color: #1f2937;
  margin: 0 0 0.5rem 0;
}

.setting-details p {
  font-size: 1rem;
  color: #64748b;
  margin: 0;
}

.setting-content {
  margin-top: 1.5rem;
  padding-top: 1.5rem;
  border-top: 1px solid rgba(16, 185, 129, 0.1);
}

/* Toggle Switch */
.toggle-switch {
  position: relative;
  display: inline-block;
  width: 64px;
  height: 36px;
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
  background: #e2e8f0;
  border-radius: 34px;
  transition: all 0.3s ease;
}

.toggle-slider:before {
  position: absolute;
  content: "";
  height: 28px;
  width: 28px;
  left: 4px;
  bottom: 4px;
  background: white;
  border-radius: 50%;
  transition: all 0.3s ease;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
}

.toggle-switch input:checked + .toggle-slider {
  background: linear-gradient(135deg, #10b981 0%, #059669 100%);
  box-shadow: 
    0 8px 25px rgba(16, 185, 129, 0.15),
    0 4px 12px rgba(16, 185, 129, 0.1);
}

.toggle-switch input:checked + .toggle-slider:before {
  transform: translateX(28px);
}

/* Time Input */
.time-input-group {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.time-input {
  width: 100px;
}

.time-unit {
  font-weight: 600;
  color: #64748b;
}

/* Attempts Options */
.attempts-options {
  display: flex;
  gap: 1rem;
}

.attempt-option {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 1.5rem 1rem;
  border: 2px solid #e2e8f0;
  border-radius: 16px;
  cursor: pointer;
  transition: all 0.3s ease;
  background: rgba(255, 255, 255, 0.8);
}

.attempt-option:hover {
  border-color: rgba(16, 185, 129, 0.3);
  background: rgba(16, 185, 129, 0.05);
}

.attempt-option.selected {
  border-color: #10b981;
  background: rgba(16, 185, 129, 0.1);
  box-shadow: 
    0 8px 25px rgba(16, 185, 129, 0.15),
    0 4px 12px rgba(16, 185, 129, 0.1);
}

.attempt-number {
  font-size: 2rem;
  font-weight: 700;
  color: #1f2937;
  margin-bottom: 0.5rem;
}

.attempt-label {
  font-weight: 600;
  color: #64748b;
}

/* Schedule Grid */
.schedule-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2rem;
}

.form-label-small {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-weight: 600;
  color: #1f2937;
  margin-bottom: 0.75rem;
  font-size: 0.95rem;
}

/* Preview Section */
.preview-header {
  text-align: center;
  margin-bottom: 3rem;
  padding-bottom: 2rem;
  border-bottom: 2px solid rgba(16, 185, 129, 0.1);
}

.preview-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1.5rem;
  background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%);
  color: white;
  border-radius: 50px;
  font-weight: 700;
  font-size: 0.95rem;
  margin-bottom: 1.5rem;
  box-shadow: 
    0 8px 25px rgba(67, 233, 123, 0.3),
    0 4px 12px rgba(67, 233, 123, 0.2);
  animation: badge-pulse 2s ease-in-out infinite;
}

.badge-icon {
  font-size: 1.1rem;
}

@keyframes badge-pulse {
  0%, 100% { transform: scale(1); }
  50% { transform: scale(1.05); }
}

.preview-title {
  font-size: 2.5rem;
  font-weight: 800;
  background: linear-gradient(135deg, #10b981 0%, #059669 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  margin-bottom: 1rem;
}

.preview-description {
  color: #64748b;
  font-size: 1.2rem;
  margin-bottom: 2rem;
  line-height: 1.6;
}

.preview-stats {
  display: flex;
  justify-content: center;
  gap: 2rem;
  flex-wrap: wrap;
}

.stat-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 1.5rem 2rem;
  background: rgba(255, 255, 255, 0.8);
  border: 2px solid rgba(16, 185, 129, 0.1);
  border-radius: 24px;
  transition: all 0.3s ease;
  backdrop-filter: blur(15px);
}

.stat-card:hover {
  border-color: rgba(16, 185, 129, 0.3);
  transform: translateY(-5px);
  box-shadow: 
    0 8px 30px rgba(16, 185, 129, 0.12),
    0 4px 15px rgba(16, 185, 129, 0.08);
}

.stat-icon {
  font-size: 2rem;
  margin-bottom: 0.75rem;
}

.stat-value {
  font-size: 1.5rem;
  font-weight: 700;
  color: #1f2937;
  margin-bottom: 0.5rem;
}

.stat-label {
  font-weight: 600;
  color: #64748b;
  text-transform: uppercase;
  font-size: 0.85rem;
  letter-spacing: 0.5px;
}

/* Preview Questions */
.preview-questions {
  display: flex;
  flex-direction: column;
  gap: 2rem;
  margin-bottom: 3rem;
}

.preview-card {
  background: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(15px);
  border: 2px solid rgba(16, 185, 129, 0.1);
  border-radius: 24px;
  padding: 2rem;
  transition: all 0.3s ease;
}

.enhanced-preview:hover {
  border-color: rgba(16, 185, 129, 0.3);
  box-shadow: 
    0 8px 30px rgba(16, 185, 129, 0.12),
    0 4px 15px rgba(16, 185, 129, 0.08);
  transform: translateY(-5px);
}

.preview-question-header {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 1.5rem;
}

.preview-question-number {
  width: 48px;
  height: 48px;
  background: linear-gradient(135deg, #10b981 0%, #059669 100%);
  color: white;
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 1.2rem;
  box-shadow: 
    0 8px 25px rgba(16, 185, 129, 0.3),
    0 4px 12px rgba(16, 185, 129, 0.2);
}

.question-type-badge {
  padding: 0.5rem 1rem;
  border-radius: 16px;
  font-weight: 600;
  font-size: 0.85rem;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.question-type-badge.multiple_choice {
  background: rgba(16, 185, 129, 0.1);
  color: #10b981;
  border: 1px solid rgba(16, 185, 129, 0.2);
}

.question-type-badge.true_false {
  background: rgba(67, 233, 123, 0.1);
  color: #43e97b;
  border: 1px solid rgba(67, 233, 123, 0.2);
}

.question-type-badge.fill_blank {
  background: rgba(245, 87, 108, 0.1);
  color: #f5576c;
  border: 1px solid rgba(245, 87, 108, 0.2);
}

.preview-question-text {
  color: var(--primary-text-color);
  font-size: 1.2rem;
  font-weight: 600;
  margin: 0 0 1.5rem 0;
  line-height: 1.5;
}

.preview-options {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.preview-option {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1rem;
  background: rgba(248, 250, 252, 0.8);
  border: 1px solid #e2e8f0;
  border-radius: 16px;
  transition: all 0.3s ease;
}

.preview-option:hover {
  background: rgba(16, 185, 129, 0.05);
  border-color: rgba(16, 185, 129, 0.2);
}

.preview-option.correct-option {
  background: rgba(67, 233, 123, 0.1);
  border-color: rgba(67, 233, 123, 0.3);
  border-width: 2px;
}

.option-marker {
  width: 32px;
  height: 32px;
  background: linear-gradient(135deg, #10b981 0%, #059669 100%);
  color: white;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 0.9rem;
}

.option-text {
  flex: 1;
  font-size: 1rem;
  color: #1f2937;
}

.correct-mark {
  color: #43e97b;
  font-weight: 700;
  font-size: 1.5rem;
  animation: correct-bounce 0.5s ease-out;
}

@keyframes correct-bounce {
  0% { transform: scale(0); }
  50% { transform: scale(1.2); }
  100% { transform: scale(1); }
}

/* Fill Blank Preview */
.preview-fill-blank {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.fill-blank-input {
  max-width: 300px;
}

.correct-answer-display {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 1rem;
  background: rgba(67, 233, 123, 0.1);
  border: 1px solid rgba(67, 233, 123, 0.3);
  border-radius: 16px;
}

.correct-label {
  font-weight: 700;
  color: #43e97b;
}

.correct-text {
  color: var(--primary-text-color);
  font-weight: 600;
}

/* Action Buttons */
.action-buttons {
  display: flex;
  gap: 1.5rem;
  margin-top: 3rem;
  padding-top: 2rem;
  border-top: 2px solid rgba(16, 185, 129, 0.1);
}

/* Animations */
.slide-up {
  animation: slideUp 0.6s cubic-bezier(0.4, 0, 0.2, 1);
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

/* Utility Classes */
.hidden {
  display: none;
}

/* Responsive Design */
@media (max-width: 1200px) {
  .progress-container,
  .main-content {
    max-width: 100%;
    padding: 0 1.5rem;
  }
}

@media (max-width: 768px) {
  .create-quiz-page {
    padding: 1rem;
  }

  .section-header-card {
    padding: 2rem;
    margin-bottom: 1.5rem;
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

  .section-header-icon {
    width: 64px;
    height: 64px;
  }

  .section-header-title {
    font-size: 1.5rem;
  }

  .progress-card {
    padding: 1.5rem;
  }
  
  .progress-track {
    flex-direction: column;
    gap: 1.5rem;
  }
  
  .step-line {
    display: none;
  }
  
  .landing-card {
    padding: 2.5rem 1.5rem;
    margin: 1rem;
  }
  
  .content-card {
    padding: 2rem 1.5rem;
    margin: 1rem;
  }
  
  .features-preview {
    gap: 1rem;
  }
  
  .feature-item {
    padding: 0.75rem;
    min-width: 120px;
  }

  .form-grid {
    grid-template-columns: 1fr;
  }
  
  .schedule-grid {
    grid-template-columns: 1fr;
  }
  
  .settings-grid {
    grid-template-columns: 1fr;
  }
  
  .tf-options {
    grid-template-columns: 1fr;
  }
  
  .attempts-options {
    flex-direction: column;
  }
  
  .preview-stats {
    gap: 1rem;
  }
  
  .action-buttons {
    flex-direction: column;
  }

  .floating-shapes {
    display: none;
  }
}

@media (max-width: 480px) {
  .landing-card h2 {
    font-size: 2rem;
  }
  
  .section-title {
    font-size: 1.5rem;
  }
  
  .preview-title {
    font-size: 2rem;
  }

  .section-header-card {
    padding: 1.5rem;
  }

  .content-card {
    padding: 1.5rem;
  }

  .question-card {
    padding: 1.5rem;
  }
}

/* Accessibility improvements */
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}

.btn:focus-visible,
.form-input:focus-visible,
.toggle-switch:focus-visible {
  outline: 2px solid #10b981;
  outline-offset: 2px;
}

/* Dark Mode Styles */
.create-quiz-page.dark-mode {
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
  color: var(--secondary-text-color);
}

.dark-mode .section-header-description {
  color: var(--text-muted);
}

.dark-mode .progress-card {
  background: var(--bg-secondary);
  border: 1px solid var(--border-color);
}

.dark-mode .landing-card {
  background: var(--bg-secondary);
  border: 1px solid var(--border-color);
}

.dark-mode .landing-card h2 {
  background: linear-gradient(135deg, var(--accent-color) 0%, #4a9b87 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.dark-mode .landing-card p {
  color: var(--secondary-text-color);
}

.dark-mode .content-card {
  background: var(--bg-secondary);
  border: 1px solid var(--border-color);
}

.dark-mode .section-title {
  color: var(--primary-text-color);
}

.dark-mode .section-subtitle {
  color: var(--secondary-text-color);
}

.dark-mode .form-label {
  color: var(--primary-text-color);
}

.dark-mode .form-input {
  background: var(--input-bg);
  border-color: var(--input-border);
  color: var(--primary-text-color);
}

.dark-mode .form-input:focus {
  border-color: var(--accent-color);
  box-shadow: 0 0 0 3px rgba(95, 179, 160, 0.15);
}

.dark-mode .question-card {
  background: var(--bg-card);
  border: 1px solid var(--card-border-color);
}

.dark-mode .question-title {
  color: var(--primary-text-color);
}

.dark-mode .option-item {
  background: var(--bg-card);
  border-color: var(--border-color);
}

.dark-mode .option-input {
  color: var(--primary-text-color);
}

.dark-mode .tf-option {
  background: var(--bg-card);
  border-color: var(--border-color);
}

.dark-mode .tf-label {
  color: var(--primary-text-color);
}

.dark-mode .setting-card {
  background: var(--bg-card);
  border: 1px solid var(--card-border-color);
}

.dark-mode .setting-details h3 {
  color: var(--primary-text-color);
}

.dark-mode .setting-details p {
  color: var(--secondary-text-color);
}

.dark-mode .attempt-option {
  background: var(--bg-card);
  border-color: var(--border-color);
}

.dark-mode .attempt-number {
  color: var(--primary-text-color);
}

.dark-mode .attempt-label {
  color: var(--secondary-text-color);
}

.dark-mode .time-unit {
  color: var(--secondary-text-color);
}

.dark-mode .preview-title {
  background: linear-gradient(135deg, var(--accent-color) 0%, #4a9b87 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.dark-mode .preview-description {
  color: var(--secondary-text-color);
}

.dark-mode .stat-card {
  background: var(--bg-card);
  border: 1px solid var(--card-border-color);
}

.dark-mode .stat-value {
  color: var(--primary-text-color);
}

.dark-mode .stat-label {
  color: var(--secondary-text-color);
}

.dark-mode .preview-card {
  background: var(--bg-card);
  border: 1px solid var(--card-border-color);
}

.dark-mode .preview-question-text {
  color: var(--primary-text-color);
}

.dark-mode .preview-option {
  background: var(--bg-accent);
  border-color: var(--border-color);
}

.dark-mode .option-text {
  color: var(--primary-text-color);
}

.dark-mode .correct-text {
  color: var(--primary-text-color);
}


.create-quiz-page {
  padding: 2rem;
  max-width: 1400px;
  margin: 0 auto;
  background: var(--bg-primary, #f8fafc);
  min-height: 100vh;
  color: var(--primary-text-color, #1f2937);
  transition: all 0.3s ease;
}

.section-header-card {
  margin-bottom: 2rem;
  position: relative;
  overflow: hidden;
  background: rgba(248, 250, 252, 0.9);
  backdrop-filter: blur(20px);
  border-radius: 32px;
  padding: 3.5rem;
  border: 1px solid rgba(255, 255, 255, 0.8);
  min-height: 180px;
  box-shadow: 
    0 20px 40px rgba(0, 0, 0, 0.06),
    0 10px 20px rgba(0, 0, 0, 0.04),
    inset 0 1px 0 rgba(255, 255, 255, 0.8);
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.section-header-card:hover {
  transform: translateY(-4px) scale(1.005);
  box-shadow: 
    0 35px 70px rgba(16, 185, 129, 0.12),
    0 20px 40px rgba(0, 0, 0, 0.08),
    0 12px 24px rgba(16, 185, 129, 0.06),
    inset 0 1px 0 rgba(255, 255, 255, 0.95),
    inset 0 0 0 1px rgba(16, 185, 129, 0.1);
  border-color: rgba(16, 185, 129, 0.15);
}

.header-bg-decoration {
  position: absolute;
  top: -50%;
  right: -20%;
  width: 140%;
  height: 220%;
  background: 
    radial-gradient(ellipse 60% 40% at 70% 30%, rgba(16, 185, 129, 0.12) 0%, transparent 60%),
    radial-gradient(ellipse 40% 60% at 30% 70%, rgba(5, 150, 105, 0.08) 0%, transparent 50%),
    linear-gradient(135deg, rgba(16, 185, 129, 0.05) 0%, transparent 80%);
  z-index: 1;
  opacity: 0.8;
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
  gap: 2rem;
}

.section-header-icon {
  width: 88px;
  height: 88px;
  background: 
    linear-gradient(135deg, #10b981 0%, #059669 50%, #047857 100%),
    linear-gradient(225deg, rgba(255, 255, 255, 0.2) 0%, transparent 50%);
  border-radius: 28px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #fff;
  box-shadow: 
    0 12px 32px rgba(16, 185, 129, 0.35),
    0 6px 16px rgba(16, 185, 129, 0.2),
    inset 0 1px 0 rgba(255, 255, 255, 0.3),
    inset 0 -1px 0 rgba(0, 0, 0, 0.1);
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  position: relative;
  overflow: hidden;
}

.section-header-icon:hover {
  transform: translateY(-3px) scale(1.05);
  box-shadow: 
    0 16px 40px rgba(16, 185, 129, 0.4),
    0 8px 20px rgba(16, 185, 129, 0.25),
    inset 0 1px 0 rgba(255, 255, 255, 0.4),
    inset 0 -1px 0 rgba(0, 0, 0, 0.15);
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

.back-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  background: linear-gradient(135deg, rgba(255,255,255,0.7), rgba(248,250,252,0.7));
  border: 2px solid rgba(16,185,129,0.15);
  border-radius: 12px;
  padding: 0.7rem 1.4rem;
  color: #10b981;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  font-size: 0.95rem;
  position: relative;
  overflow: hidden;
  box-shadow: 0 2px 6px rgba(16, 185, 129, 0.06);
}

.back-btn:hover {
  background: linear-gradient(135deg, #f0fdf4, #dcfce7);
  border-color: #10b981;
  color: #065f46;
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(16, 185, 129, 0.15);
}

.spinner {
  width: 20px;
  height: 20px;
  border: 3px solid rgba(255, 255, 255, 0.3);
  border-top-color: white;
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

</style>
