<template>
  <div class="dashboard-container">
    <!-- Top Navigation Bar -->
    <nav class="top-navbar">
      <div class="navbar-content">
        <!-- Left: Logo and Brand -->
        <div class="navbar-left">
          <div class="brand-logo">
            <img src="@/assets/LOGO WAY BG.png" alt="DigiCheck" class="logo-img" />
            <span class="brand-name">DigiCheck</span>
          </div>
        </div>
        <!-- Center: Empty space for clean look -->
        <div class="navbar-center">
        </div>
        
        <!-- Right: User Profile -->
        <div class="navbar-right">
          <!-- Notification Bell -->
          <div class="notif-wrapper">
            <button class="nav-icon-btn rounded-bg" aria-label="Notifications">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                <path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"></path>
                <path d="M13.73 21a2 2 0 0 1-3.46 0"></path>
              </svg>
            </button>
          </div>
          
          <!-- User Profile -->
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
        
        <div class="sidebar-divider"></div>
        
        <router-link to="/teacher/settings" class="sidebar-item rounded-bg">
          <div class="sidebar-icon">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
              <circle cx="12" cy="7" r="4"></circle>
            </svg>
          </div>
          <span class="sidebar-tooltip">Profile & Settings</span>
        </router-link>
        
        <button @click="logout" class="sidebar-item sidebar-logout rounded-bg">
          <div class="sidebar-icon">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"></path>
              <polyline points="16 17 21 12 16 7"></polyline>
              <line x1="21" y1="12" x2="9" y2="12"></line>
            </svg>
          </div>
          <span class="sidebar-tooltip">Logout</span>
        </button>
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
            <h1>Edit Assessment</h1>
            <p>{{ assessmentTitle || 'Loading...' }}</p>
          </div>
        </div>
        <div class="header-right">
          <button @click="saveAssessment" :disabled="isSaving" class="create-subject-btn">
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

      <!-- Assessment Type Selector -->
      <div class="content-wrapper">
        <div v-if="!assessmentType" class="assessment-type-selector">
          <div class="selector-card">
            <div class="selector-header">
              <div class="selector-icon">
                <svg width="48" height="48" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M12,2A10,10 0 0,1 22,12A10,10 0 0,1 12,22A10,10 0 0,1 2,12A10,10 0 0,1 12,2M12,4A8,8 0 0,0 4,12A8,8 0 0,0 12,20A8,8 0 0,0 20,12A8,8 0 0,0 12,4M11,16.5L6.5,12L7.91,10.59L11,13.67L16.59,8.09L18,9.5L11,16.5Z" />
                </svg>
              </div>
              <h2>Choose Assessment Type</h2>
              <p>Select what type of assessment you want to edit</p>
            </div>
            
            <div class="type-options">
              <button @click="selectAssessmentType('quiz')" class="type-option-btn quiz-option">
                <div class="option-icon">
                  <svg width="32" height="32" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M9,5V9H21V7.5L22.5,6L21,4.5L19.5,6L18,4.5L16.5,6L18,7.5V9H15V5H9M9,19V15H15V19H9M21,15V13.5L19.5,12L18,13.5V15H21Z" />
                  </svg>
                </div>
                <h3>Edit Quiz</h3>
                <p>Multiple choice, True/False, Fill-in-blank questions</p>
              </button>
              
              <button @click="selectAssessmentType('assignment')" class="type-option-btn assignment-option">
                <div class="option-icon">
                  <svg width="32" height="32" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M14,2H6A2,2 0 0,0 4,4V20A2,2 0 0,0 6,22H18A2,2 0 0,0 20,20V8L14,2M18,20H6V4H13V9H18V20Z" />
                  </svg>
                </div>
                <h3>Edit Assignment</h3>
                <p>Essays, Projects, Research tasks, File submissions</p>
              </button>
            </div>
          </div>
        </div>

        <!-- Quiz Editor -->
        <div v-if="assessmentType === 'quiz' && !isLoading && !error">
          <!-- Quiz Settings Card -->
          <div class="form-card">
            <div class="card-header">
              <h3>Quiz Settings</h3>
            </div>
            <div class="card-body">
              <div class="form-group">
                <label for="quiz-title">Quiz Title *</label>
                <input 
                  type="text" 
                  id="quiz-title" 
                  v-model="quiz.title" 
                  placeholder="Enter quiz title"
                  required
                />
              </div>

              <div class="form-group">
                <label for="quiz-description">Description</label>
                <textarea 
                  id="quiz-description" 
                  v-model="quiz.description" 
                  placeholder="Enter quiz description (optional)"
                  rows="3"
                ></textarea>
              </div>

              <div class="form-row">
                <div class="form-group">
                  <label for="quiz-status">Status</label>
                  <select id="quiz-status" v-model="quiz.status">
                    <option value="draft">Draft</option>
                    <option value="published">Published</option>
                    <option value="archived">Archived</option>
                  </select>
                </div>

                <div class="form-group">
                  <label for="quiz-attempts">Attempts Allowed *</label>
                  <input 
                    type="number" 
                    id="quiz-attempts" 
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
                  <label for="quiz-timeLimit">Time Limit (minutes) *</label>
                  <input 
                    type="number" 
                    id="quiz-timeLimit" 
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
                  <label for="quiz-startDate">Start Date</label>
                  <input 
                    type="datetime-local" 
                    id="quiz-startDate" 
                    v-model="quiz.start_date" 
                  />
                </div>

                <div class="form-group">
                  <label for="quiz-endDate">End Date</label>
                  <input 
                    type="datetime-local" 
                    id="quiz-endDate" 
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
        </div>

        <!-- Assignment Editor -->
        <div v-if="assessmentType === 'assignment' && !isLoading && !error">
          <!-- Assignment Settings Card -->
          <div class="form-card">
            <div class="card-header">
              <h3>Assignment Settings</h3>
            </div>
            <div class="card-body">
              <div class="form-group">
                <label for="assignment-title">Assignment Title *</label>
                <input 
                  type="text" 
                  id="assignment-title" 
                  v-model="assignment.title" 
                  placeholder="Enter assignment title"
                  required
                />
              </div>

              <div class="form-group">
                <label for="assignment-description">Description / Instructions</label>
                <textarea 
                  id="assignment-description" 
                  v-model="assignment.description" 
                  placeholder="Provide detailed instructions for the assignment..."
                  rows="4"
                ></textarea>
              </div>

              <div class="form-row">
                <div class="form-group">
                  <label for="assignment-points">Total Points *</label>
                  <input 
                    type="number" 
                    id="assignment-points" 
                    v-model.number="assignment.total_points" 
                    min="1"
                    placeholder="100"
                    required
                  />
                </div>

                <div class="form-group">
                  <label for="assignment-dueDate">Due Date *</label>
                  <input 
                    type="datetime-local" 
                    id="assignment-dueDate" 
                    v-model="assignment.due_date" 
                    required
                  />
                </div>
              </div>

              <div class="form-row">
                <div class="form-group">
                  <label for="assignment-type">Assignment Type *</label>
                  <select id="assignment-type" v-model="assignment.assignment_type" required>
                    <option value="">Select assignment type</option>
                    <option value="homework">Homework</option>
                    <option value="project">Project</option>
                    <option value="essay">Essay</option>
                    <option value="presentation">Presentation</option>
                    <option value="research">Research Paper</option>
                    <option value="lab">Lab Work</option>
                    <option value="other">Other</option>
                  </select>
                </div>

                <div class="form-group">
                  <label for="assignment-submission">Submission Type *</label>
                  <select id="assignment-submission" v-model="assignment.submission_type" required>
                    <option value="">Select submission type</option>
                    <option value="file_upload">File Upload</option>
                    <option value="text_entry">Text Entry</option>
                    <option value="link">External Link</option>
                    <option value="physical">Physical Submission</option>
                  </select>
                </div>
              </div>

              <div class="settings-section">
                <h4>Additional Settings</h4>
                
                <div class="checkbox-group">
                  <label>
                    <input type="checkbox" v-model="assignment.allow_late_submission" />
                    <span>Allow late submissions</span>
                  </label>
                </div>

                <div v-if="assignment.allow_late_submission" class="form-group indent">
                  <label for="assignment-penalty">Late Penalty (%)</label>
                  <input 
                    type="number" 
                    id="assignment-penalty" 
                    v-model.number="assignment.late_penalty" 
                    min="0"
                    max="100"
                    placeholder="10"
                  />
                </div>

                <div class="checkbox-group">
                  <label>
                    <input type="checkbox" v-model="assignment.require_plagiarism_check" />
                    <span>Require plagiarism check</span>
                  </label>
                </div>

                <div class="checkbox-group">
                  <label>
                    <input type="checkbox" v-model="assignment.publish_immediately" />
                    <span>Published</span>
                  </label>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Loading State -->
        <div v-if="isLoading" class="loading-state">
          <div class="loading-spinner"></div>
          <p>Loading assessment...</p>
        </div>

        <!-- Error State -->
        <div v-if="error" class="empty-state">
          <div class="empty-icon">
            <svg width="64" height="64" viewBox="0 0 24 24" fill="currentColor">
              <path d="M11,15H13V17H11V15M11,7H13V13H11V7M12,2C6.47,2 2,6.5 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2M12,20A8,8 0 0,1 4,12A8,8 0 0,1 12,4A8,8 0 0,1 20,12A8,8 0 0,1 12,20Z" />
            </svg>
          </div>
          <h3 class="empty-title">Error Loading Assessment</h3>
          <p class="empty-desc">{{ error }}</p>
          <button @click="loadAssessment" class="create-quiz-btn">Try Again</button>
        </div>

        <!-- Save Button (Bottom) -->
        <div v-if="assessmentType" class="form-actions">
          <button @click="goBack" class="cancel-btn">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M10 19l-7-7 7-7m-7 7h18"></path>
            </svg>
            Cancel
          </button>
          <button @click="saveAssessment" :disabled="isSaving" class="save-btn-large">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M15,9H5V5H15M12,19A3,3 0 0,1 9,16A3,3 0 0,1 12,13A3,3 0 0,1 15,16A3,3 0 0,1 12,19M17,3H5C3.89,3 3,3.9 3,5V19A2,2 0 0,0 5,21H19A2,2 0 0,0 21,19V7L17,3Z" />
            </svg>
            {{ isSaving ? 'Saving Changes...' : 'Save All Changes' }}
          </button>
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

// Get quiz/assignment ID and route params from query
const assessmentId = ref(route.params.quizId) // Can be quiz_id or assignment_id
const subjectId = ref(route.query.subjectId)
const sectionId = ref(route.query.sectionId)
const subjectName = ref(route.query.subjectName)
const sectionName = ref(route.query.sectionName)
const gradeLevel = ref(route.query.gradeLevel)
const sectionCode = ref(route.query.sectionCode)

// State
const assessmentType = ref(null) // 'quiz' or 'assignment'
const assessmentTitle = ref('')

// Quiz state
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

// Assignment state
const assignment = ref({
  title: '',
  description: '',
  assignment_type: '',
  submission_type: '',
  total_points: 100,
  due_date: null,
  allow_late_submission: false,
  late_penalty: 0,
  require_plagiarism_check: false,
  publish_immediately: false,
  status: 'draft'
})

const isLoading = ref(false)
const isSaving = ref(false)
const error = ref(null)
const fullName = ref('Teacher')

// TIMEZONE UTILITY FUNCTIONS
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
    const localDate = new Date(phDateString);
    const phOffset = -8 * 60;
    const localOffset = localDate.getTimezoneOffset();
    const offsetDiff = localOffset - phOffset;
    const utcTime = new Date(localDate.getTime() + (offsetDiff * 60 * 1000));
    
    console.log('🕐 Converting PH to UTC:');
    console.log('  Input PH time:', phDateString);
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

// Detect assessment type and load data
const loadAssessment = async () => {
  isLoading.value = true
  error.value = null
  
  try {
    console.log('Loading assessment:', assessmentId.value)
    
    // First, try to load as quiz
    const { data: quizData, error: quizError } = await supabase
      .from('quizzes')
      .select('*')
      .eq('id', assessmentId.value)
      .single()
    
    if (quizData && !quizError) {
      // It's a quiz
      assessmentType.value = 'quiz'
      assessmentTitle.value = quizData.title
      await loadQuiz()
      return
    }
    
    // If not a quiz, try to load as assignment
    const { data: assignmentData, error: assignmentError } = await supabase
      .from('assignments')
      .select('*')
      .eq('id', assessmentId.value)
      .single()
    
    if (assignmentData && !assignmentError) {
      // It's an assignment
      assessmentType.value = 'assignment'
      assessmentTitle.value = assignmentData.title
      await loadAssignment()
      return
    }
    
    // Neither found
    throw new Error('Assessment not found')
    
  } catch (err) {
    console.error('Error detecting assessment type:', err)
    error.value = err.message
  } finally {
    isLoading.value = false
  }
}

// Load quiz data
const loadQuiz = async () => {
  try {
    console.log('Loading quiz:', assessmentId.value)
    
    const { data: quizData, error: quizError } = await supabase
      .from('quizzes')
      .select('*')
      .eq('id', assessmentId.value)
      .single()
    
    if (quizError) throw quizError
    
    console.log('Quiz data loaded:', quizData)
    
    quiz.value = {
      ...quizData,
      start_date: quizData.start_date ? convertUTCtoPHForInput(quizData.start_date) : null,
      end_date: quizData.end_date ? convertUTCtoPHForInput(quizData.end_date) : null
    }
    
    // Fetch questions
    console.log('Loading questions for quiz:', assessmentId.value)
    const { data: questionsData, error: questionsError } = await supabase
      .from('quiz_questions')
      .select('*')
      .eq('quiz_id', assessmentId.value)
      .order('question_number')
    
    if (questionsError) throw questionsError
    
    console.log('✅ Questions loaded:', questionsData?.length || 0)
    
    // Load options and answers for each question
    for (const question of questionsData || []) {
      if (question.question_type === 'multiple_choice') {
        const { data: options, error: optionsError } = await supabase
          .from('question_options')
          .select('*')
          .eq('question_id', question.id)
          .order('option_number')
        
        if (optionsError) throw optionsError
        question.options = options || []
      } else {
        const { data: answer, error: answerError } = await supabase
          .from('question_answers')
          .select('*')
          .eq('question_id', question.id)
          .single()
        
        if (!answerError && answer) {
          question.answer = answer
        } else {
          question.answer = {
            correct_answer: question.question_type === 'true_false' ? 'true' : '',
            case_sensitive: false
          }
        }
      }
    }
    
    questions.value = questionsData || []
    console.log('All quiz data loaded successfully')
    
  } catch (err) {
    console.error('Error loading quiz:', err)
    throw err
  }
}

// Load assignment data
const loadAssignment = async () => {
  try {
    console.log('Loading assignment:', assessmentId.value)
    
    const { data: assignmentData, error: assignmentError } = await supabase
      .from('assignments')
      .select('*')
      .eq('id', assessmentId.value)
      .single()
    
    if (assignmentError) throw assignmentError
    
    console.log('Assignment data loaded:', assignmentData)
    
    assignment.value = {
      ...assignmentData,
      due_date: assignmentData.due_date ? convertUTCtoPHForInput(assignmentData.due_date) : null,
      publish_immediately: assignmentData.status === 'published'
    }
    
    console.log('Assignment loaded successfully')
    
  } catch (err) {
    console.error('Error loading assignment:', err)
    throw err
  }
}

// Select assessment type (for new assessments)
const selectAssessmentType = (type) => {
  assessmentType.value = type
  console.log('Assessment type selected:', type)
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

// Save assessment
const saveAssessment = async () => {
  if (assessmentType.value === 'quiz') {
    await saveQuiz()
  } else if (assessmentType.value === 'assignment') {
    await saveAssignmentData()
  }
}

// Save quiz
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
    console.log('Updating quiz settings...')
    
    const startDateUTC = convertPHTimeToUTC(quiz.value.start_date);
    const endDateUTC = convertPHTimeToUTC(quiz.value.end_date);
    
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
      .eq('id', assessmentId.value)
    
    if (quizError) throw quizError
    
    console.log('Quiz settings updated')
    
    // Get existing questions
    const { data: existingQuestions, error: fetchError } = await supabase
      .from('quiz_questions')
      .select('id')
      .eq('quiz_id', assessmentId.value)
    
    if (fetchError) throw fetchError
    
    // Delete old questions
    if (existingQuestions && existingQuestions.length > 0) {
      console.log(`Deleting ${existingQuestions.length} existing questions...`)
      const questionIds = existingQuestions.map(q => q.id)
      
      const { error: deleteError } = await supabase
        .from('quiz_questions')
        .delete()
        .in('id', questionIds)
      
      if (deleteError) throw deleteError
      console.log('Old questions deleted')
    }
    
    // Insert new questions
    console.log(`Inserting ${questions.value.length} new questions...`)
    
    for (let i = 0; i < questions.value.length; i++) {
      const question = questions.value[i]
      console.log(`Processing question ${i + 1}...`)
      
      const { data: insertedQuestion, error: questionError } = await supabase
        .from('quiz_questions')
        .insert({
          quiz_id: assessmentId.value,
          question_number: question.question_number,
          question_type: question.question_type,
          question_text: question.question_text,
          points: question.points
        })
        .select()
        .single()
      
      if (questionError) throw new Error(`Failed to save question ${i + 1}: ${questionError.message}`)
      
      console.log(`Question ${i + 1} inserted:`, insertedQuestion.id)
      
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
        
        if (optionsError) throw new Error(`Failed to save options for question ${i + 1}: ${optionsError.message}`)
        
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
        
        if (answerError) throw new Error(`Failed to save answer for question ${i + 1}: ${answerError.message}`)
        
        console.log(`Answer inserted for question ${i + 1}`)
      }
    }
    
    console.log('All questions saved successfully!')
    
    // Show success message
    if (confirm('✅ Quiz updated successfully! Click OK to go back.')) {
      goBack()
    }
    
  } catch (err) {
    console.error('❌ Error saving quiz:', err)
    alert(`❌ Error saving quiz: ${err.message || 'Unknown error occurred'}`)
  } finally {
    isSaving.value = false
  }
}

// Save assignment
const saveAssignmentData = async () => {
  console.log('Starting save assignment process...')
  
  // Validation
  if (!assignment.value.title.trim()) {
    alert('Please enter an assignment title')
    return
  }
  
  if (!assignment.value.assignment_type) {
    alert('Please select an assignment type')
    return
  }
  
  if (!assignment.value.submission_type) {
    alert('Please select a submission type')
    return
  }
  
  if (!assignment.value.due_date) {
    alert('Please set a due date')
    return
  }
  
  if (!assignment.value.total_points || assignment.value.total_points < 1) {
    alert('Please enter valid total points')
    return
  }
  
  isSaving.value = true
  
  try {
    console.log('Updating assignment...')
    
    const dueDateUTC = convertPHTimeToUTC(assignment.value.due_date);
    
    const { error: assignmentError } = await supabase
      .from('assignments')
      .update({
        title: assignment.value.title,
        description: assignment.value.description,
        assignment_type: assignment.value.assignment_type,
        submission_type: assignment.value.submission_type,
        total_points: assignment.value.total_points,
        due_date: dueDateUTC,
        allow_late_submission: assignment.value.allow_late_submission,
        late_penalty: assignment.value.allow_late_submission ? assignment.value.late_penalty : 0,
        require_plagiarism_check: assignment.value.require_plagiarism_check,
        status: assignment.value.publish_immediately ? 'published' : 'draft',
        updated_at: new Date().toISOString()
      })
      .eq('id', assessmentId.value)
    
    if (assignmentError) throw assignmentError
    
    console.log('Assignment updated successfully!')
    
    // Show success message
    if (confirm('✅ Assignment updated successfully! Click OK to go back.')) {
      goBack()
    }
    
  } catch (err) {
    console.error('❌ Error saving assignment:', err)
    alert(`❌ Error saving assignment: ${err.message || 'Unknown error occurred'}`)
  } finally {
    isSaving.value = false
  }
}

const goBack = () => {
  console.log('Navigating back')
  // Use router.go(-1) to go back to previous page
  router.go(-1)
  
  // Alternative: If you want to navigate to a specific route
  // router.push({
  //   path: `/teacher/subjects/${subjectId.value}/sections/${sectionId.value}/quizzes`
  // })
}

const logout = () => {
  // Implement logout logic
  console.log('Logout clicked')
}

// Lifecycle
onMounted(async () => {
  console.log('EditQuiz component mounted')
  initDarkMode()
  
  try {
    await initializeAuth()
    
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
      }
    }
  } catch (err) {
    console.warn('⚠️ Auth initialization warning:', err)
  }
  
  if (!assessmentId.value) {
    console.error('❌ Assessment ID is missing')
    error.value = 'Assessment ID is missing'
    return
  }
  
  await loadAssessment()
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

/* Notification Bell */
.notif-wrapper {
  position: relative;
}

.nav-icon-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 40px;
  height: 40px;
  background: rgba(255, 255, 255, 0.1);
  border: none;
  border-radius: 50%;
  color: white;
  cursor: pointer;
  transition: all 0.2s;
}

.nav-icon-btn:hover {
  background: rgba(255, 255, 255, 0.2);
}

/* Sidebar Divider */
.sidebar-divider {
  width: 48px;
  height: 1px;
  background: rgba(255, 255, 255, 0.2);
  margin: 0.75rem 0;
}

.sidebar-logout {
  background: transparent;
  border: none;
  color: white;
}

.sidebar-logout:hover {
  background: rgba(239, 68, 68, 0.2);
}

/* Content Wrapper */
.content-wrapper {
  margin-top: 2rem;
}

/* Assessment Type Selector */
.assessment-type-selector {
  display: flex;
  justify-content: center;
  padding: 2rem 0;
}

.selector-card {
  background: white;
  border-radius: 20px;
  border: 1.5px solid #e5e7eb;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.06);
  padding: 2.5rem;
  max-width: 800px;
  width: 100%;
}

.dark .selector-card {
  background: #23272b;
  border-color: #374151;
}

.selector-header {
  text-align: center;
  margin-bottom: 2.5rem;
}

.selector-icon {
  display: flex;
  justify-content: center;
  margin-bottom: 1.5rem;
  color: #3D8D7A;
}

.dark .selector-icon {
  color: #A3D1C6;
}

.selector-header h2 {
  font-size: 1.75rem;
  font-weight: 700;
  color: #1e293b;
  margin-bottom: 0.5rem;
}

.dark .selector-header h2 {
  color: #f1f5f9;
}

.selector-header p {
  color: #64748b;
  font-size: 1rem;
}

.dark .selector-header p {
  color: #94a3b8;
}

/* Type Options */
.type-options {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1.5rem;
}

.type-option-btn {
  background: white;
  border: 2px solid #e2e8f0;
  border-radius: 16px;
  padding: 2rem 1.5rem;
  cursor: pointer;
  transition: all 0.3s ease;
  text-align: center;
}

.dark .type-option-btn {
  background: #1e2329;
  border-color: #374151;
}

.type-option-btn:hover {
  border-color: #3D8D7A;
  box-shadow: 0 8px 24px rgba(61, 141, 122, 0.15);
  transform: translateY(-4px);
}

.dark .type-option-btn:hover {
  border-color: #A3D1C6;
  box-shadow: 0 8px 24px rgba(163, 209, 198, 0.15);
}

.quiz-option:hover {
  background: linear-gradient(135deg, #f0fdfa 0%, #ecfdf5 100%);
}

.assignment-option:hover {
  background: linear-gradient(135deg, #fef3c7 0%, #fef9e7 100%);
}

.option-icon {
  width: 64px;
  height: 64px;
  margin: 0 auto 1rem;
  background: linear-gradient(135deg, #3D8D7A, #2d6a5a);
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
}

.dark .option-icon {
  background: linear-gradient(135deg, #A3D1C6, #20c997);
}

.assignment-option .option-icon {
  background: linear-gradient(135deg, #f59e0b, #d97706);
}

.type-option-btn h3 {
  font-size: 1.25rem;
  font-weight: 700;
  color: #1e293b;
  margin-bottom: 0.5rem;
}

.dark .type-option-btn h3 {
  color: #f1f5f9;
}

.type-option-btn p {
  color: #64748b;
  font-size: 0.875rem;
  line-height: 1.5;
}

.dark .type-option-btn p {
  color: #94a3b8;
}

/* Settings Section */
.settings-section {
  margin-top: 1.5rem;
  padding-top: 1.5rem;
  border-top: 1px solid #e2e8f0;
}

.dark .settings-section {
  border-top-color: #374151;
}

.settings-section h4 {
  font-size: 1rem;
  font-weight: 600;
  color: #374151;
  margin-bottom: 1rem;
}

.dark .settings-section h4 {
  color: #e5e7eb;
}

.indent {
  margin-left: 2rem;
}

/* Assignment Type Specific Styles */
#assignment-type,
#assignment-submission {
  appearance: none;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='12' viewBox='0 0 12 12'%3E%3Cpath fill='%236b7280' d='M6 9L1 4h10z'/%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-position: right 0.75rem center;
  background-size: 12px;
  padding-right: 2.5rem;
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

/* Responsive Design */
@media (max-width: 768px) {
  .type-options {
    grid-template-columns: 1fr;
  }
  
  .selector-card {
    padding: 1.5rem;
  }
  
  .type-option-btn {
    padding: 1.5rem 1rem;
  }
  
  .option-icon {
    width: 48px;
    height: 48px;
  }
  
  .indent {
    margin-left: 1rem;
  }
}

/* Main Content - FIXED: Added scroll and height constraints */
.main-content {
  padding: 2rem;
  max-width: 1400px;
  margin: 0 auto;
  max-height: calc(100vh - 64px);  /* NEW */
  overflow-y: auto;                 /* NEW */
  overflow-x: hidden;               /* NEW */
  scroll-behavior: smooth;          /* NEW */
}

/* Custom Scrollbar Styling - ADDED */
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

/* Firefox Scrollbar - ADDED */
* {
  scrollbar-width: thin;
  scrollbar-color: #3D8D7A #f1f5f9;
}

/* Dark mode scrollbar - ADDED */
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

/* Content Wrapper - ADDED */
.content-wrapper {
  margin-top: 2rem;
}
</style>