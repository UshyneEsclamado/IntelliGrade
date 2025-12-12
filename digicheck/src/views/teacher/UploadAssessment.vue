<template>
  <div class="dashboard-container" :class="{ 'dark': isDarkMode }">
    <!-- Top Navigation Bar (Clean) -->
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
        
        <!-- Right: User Profile and Notifications -->
        <div class="navbar-right">
          <!-- Notification Bell -->
          <div class="notif-wrapper">
            <button class="nav-icon-btn rounded-bg" @click="toggleNotifDropdown" aria-label="Notifications">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                <path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"></path>
                <path d="M13.73 21a2 2 0 0 1-3.46 0"></path>
              </svg>
              <span v-if="notifications.length" class="notification-badge">{{ notifications.length }}</span>
            </button>
            
            <!-- Notification Dropdown -->
            <div v-if="showNotifDropdown" class="notification-dropdown">
              <div class="dropdown-header">
                <h3>Notifications</h3>
              </div>
              <div class="notification-list">
                <div v-if="notifications.length === 0" class="no-notifications">
                  No new notifications
                </div>
                <div v-for="notif in notifications" :key="notif.id" class="notification-item" @click="handleNotificationClick(notif)">
                  <div class="notif-content">
                    <h4>{{ notif.title }}</h4>
                    <p>{{ notif.body }}</p>
                    <span class="notif-time">{{ notif.date }}</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
          
          <!-- User Profile -->
          <div class="user-profile-wrapper">
            <div class="user-profile rounded-bg" @click="toggleProfileDropdown">
              <div class="user-avatar">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
                  <circle cx="12" cy="7" r="4"></circle>
                </svg>
              </div>
              <span class="user-name">{{ fullName }}</span>
              <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" class="dropdown-arrow">
                <path d="M7 10l5 5 5-5z"/>
              </svg>
            </div>
            
            <!-- Profile Dropdown -->
            <div v-if="showProfileDropdown" class="profile-dropdown">
              <div class="dropdown-header">
                <div class="profile-info">
                  <div class="profile-avatar">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                      <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
                      <circle cx="12" cy="7" r="4"></circle>
                    </svg>
                  </div>
                  <div class="profile-details">
                    <h4>{{ fullName }}</h4>
                    <p>Teacher</p>
                  </div>
                </div>
              </div>
              
              <div class="dropdown-menu">
                <router-link to="/teacher/settings" class="dropdown-item">
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M12 2C13.1 2 14 2.9 14 4C14 5.1 13.1 6 12 6C10.9 6 10 5.1 10 4C10 2.9 10.9 2 12 2ZM21 9V7L15 1V3H9V1L3 7V9H5V20A2 2 0 0 0 7 22H17A2 2 0 0 0 19 20V9H21M17 20H7V9H10V12H14V9H17V20Z"/>
                  </svg>
                  <span>Profile & Settings</span>
                </router-link>
                
                <div class="dropdown-divider"></div>
                
                <button @click="logout" class="dropdown-item logout-btn">
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M16 17V14H9V10H16V7L21 12L16 17M14 2A2 2 0 0 1 16 4V6H14V4H5V20H14V18H16V20A2 2 0 0 1 14 22H5A2 2 0 0 1 3 20V4A2 2 0 0 1 5 2H14Z"/>
                  </svg>
                  <span>Logout</span>
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </nav>

    <!-- Sidebar Navigation -->
    <aside class="sidebar" style="background:#3D8D7A; border-right:none;">
      <nav class="sidebar-nav">
        <router-link to="/teacher/dashboard" class="sidebar-item rounded-bg" :class="{ 'active': $route.path === '/teacher/dashboard' }">
          <div class="sidebar-icon">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M10 20v-6h4v6m5-8h3L12 3 2 12h3v8h5v-6h4v6h5v-8z" />
            </svg>
          </div>
          <span class="sidebar-tooltip">Dashboard</span>
        </router-link>
        <router-link to="/teacher/subjects" class="sidebar-item rounded-bg" :class="{ 'active': $route.path === '/teacher/subjects' }">
          <div class="sidebar-icon">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <rect x="3" y="7" width="18" height="13" rx="2" />
              <path d="M3 7l9-4 9 4" />
            </svg>
          </div>
          <span class="sidebar-tooltip">Classes</span>
        </router-link>
        <router-link to="/teacher/gradebook" class="sidebar-item rounded-bg" :class="{ 'active': $route.path === '/teacher/gradebook' }">
          <div class="sidebar-icon">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <rect x="4" y="4" width="16" height="16" rx="2" />
              <path d="M8 2v4M16 2v4" />
            </svg>
          </div>
          <span class="sidebar-tooltip">Gradebook</span>
        </router-link>
        <router-link to="/teacher/upload-assessment" class="sidebar-item rounded-bg" :class="{ 'active': $route.path === '/teacher/upload-assessment' }">
          <div class="sidebar-icon">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M12 19V6M5 12l7-7 7 7" />
              <rect x="5" y="19" width="14" height="2" rx="1" />
            </svg>
          </div>
          <span class="sidebar-tooltip">Upload Assessment</span>
        </router-link>
        <router-link to="/teacher/analytics" class="sidebar-item rounded-bg" :class="{ 'active': $route.path === '/teacher/analytics' }">
          <div class="sidebar-icon">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <rect x="3" y="12" width="4" height="8" />
              <rect x="10" y="8" width="4" height="12" />
              <rect x="17" y="4" width="4" height="16" />
            </svg>
          </div>
          <span class="sidebar-tooltip">Analytics</span>
        </router-link>
        <router-link to="/teacher/messages" class="sidebar-item rounded-bg" :class="{ 'active': $route.path === '/teacher/messages' }">
          <div class="sidebar-icon">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <rect x="3" y="5" width="18" height="14" rx="2" />
              <path d="M3 5l9 7 9-7" />
            </svg>
          </div>
          <span class="sidebar-tooltip">Messages</span>
        </router-link>
      </nav>
    </aside>

    <!-- Main Content Area -->
    <main class="main-content">
      <!-- Scroll to Top Button -->
      <button v-if="showScrollTop" @click="scrollToTop" class="scroll-to-top-btn">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#3D8D7A" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <circle cx="12" cy="12" r="10" fill="#fff"/>
          <path d="M12 16V8" stroke="#3D8D7A" stroke-width="2"/>
          <path d="M8 12l4-4 4 4" stroke="#3D8D7A" stroke-width="2"/>
        </svg>
      </button>
      
      <!-- Page Header -->
      <div class="page-header">
        <div class="header-content">
          <div class="header-left">
            <div class="header-icon">
              <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
                <polyline points="14,2 14,8 20,8"></polyline>
                <line x1="16" y1="13" x2="8" y2="13"></line>
                <line x1="16" y1="17" x2="8" y2="17"></line>
                <polyline points="10,9 9,9 8,9"></polyline>
              </svg>
            </div>
            <div>
              <h1 class="header-title">Assessment Checker</h1>
              <p class="header-subtitle">Upload student assessments for instant AI-powered scoring</p>
            </div>
          </div>
        </div>
      </div>

      <!-- Content Grid -->
      <div class="content-grid">
        
        <!-- Loading Overlay -->
        <div v-if="isLoading" class="loading-overlay">
          <div class="loader"></div>
          <p>{{ loadingMessage }}</p>
          <div v-if="processingSteps.length > 0" class="processing-steps">
            <div v-for="(step, index) in processingSteps" :key="index" 
                 class="processing-step" :class="{ 'completed': step.completed, 'active': step.active }">
              <span class="step-icon">
                <span v-if="step.completed" class="icon-completed">✓</span>
                <span v-else-if="step.active" class="icon-active">⟳</span>
                <span v-else class="icon-pending">○</span>
              </span>
              <span class="step-text">{{ step.text }}</span>
            </div>
          </div>
        </div>

        <!-- Assessment Configuration Card -->
        <div class="content-card">
          <div class="card-header">
            <div class="card-title-wrapper">
              <div class="card-icon">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M9 11H5a2 2 0 0 0-2 2v7a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7a2 2 0 0 0-2-2h-4"></path>
                  <path d="M9 11V9a3 3 0 0 1 6 0v2"></path>
                </svg>
              </div>
              <div>
                <h2>Assessment Configuration</h2>
                <p>Set up your assessment parameters and scoring system</p>
              </div>
            </div>
          </div>
          <div class="card-body">
            <div class="form-row">
              <div class="form-group">
                <label for="subject">Subject *</label>
                <input v-model="subject" id="subject" type="text" class="form-control"
                  placeholder="e.g., Mathematics, Science" required />
              </div>

              <div class="form-group">
                <label for="assessment-title">Assessment Title *</label>
                <input v-model="assessmentTitle" id="assessment-title" type="text" class="form-control"
                  placeholder="e.g., Chapter 5 Quiz" required />
              </div>
            </div>

            <div class="form-row">
              <div class="form-group">
                <label for="num-questions">Number of Questions *</label>
                <input v-model="numQuestions" id="num-questions" type="number" class="form-control" 
                  min="1" max="100" placeholder="10" required @input="updateQuestionsList" />
              </div>

              <div class="form-group">
                <label for="scoring-method">Scoring Method *</label>
                <select v-model="scoringMethod" id="scoring-method" class="form-control" @change="handleScoringMethodChange">
                  <option value="uniform">Uniform Points (All questions same points)</option>
                  <option value="individual">Individual Points (Set points per question)</option>
                </select>
              </div>
            </div>

            <div v-if="scoringMethod === 'uniform'" class="form-row">
              <div class="form-group">
                <label for="points-per-question">Points Per Question *</label>
                <input v-model="pointsPerQuestion" id="points-per-question" type="number" class="form-control" 
                  min="1" placeholder="5" required @input="calculateTotalPoints" />
              </div>
            </div>

            <div v-if="scoringMethod === 'individual' && numQuestions > 0" class="individual-points-section">
              <div class="points-header">
                <h4>Set Points for Each Question</h4>
                <div class="quick-assign-buttons">
                  <button type="button" @click="assignAllPoints(1)" class="quick-btn">All 1pt</button>
                  <button type="button" @click="assignAllPoints(2)" class="quick-btn">All 2pts</button>
                  <button type="button" @click="assignAllPoints(5)" class="quick-btn">All 5pts</button>
                  <button type="button" @click="setCustomPattern" class="quick-btn">Custom Pattern</button>
                </div>
              </div>
              <div class="points-grid">
                <div v-for="(question, index) in questionsList" :key="index" class="point-assignment-item" 
                     :class="{ highlighted: question.points > 1 }">
                  <label class="point-label">Q{{ index + 1 }}</label>
                  <input v-model="question.points" type="number" class="point-input" 
                         min="1" max="100" placeholder="1" @input="calculateTotalPoints" />
                  <span class="point-unit">{{ question.points == 1 ? 'pt' : 'pts' }}</span>
                </div>
              </div>
              <div class="points-summary">
                <p><strong>Total Questions:</strong> {{ numQuestions }}</p>
                <p><strong>Point Distribution:</strong> 
                  <span v-for="(count, points) in pointDistribution" :key="points" class="dist-item">
                    {{ count }} × {{ points }}pt{{ points > 1 ? 's' : '' }}
                  </span>
                </p>
              </div>
            </div>

            <div class="form-group">
              <label class="calculated-total">
                Total Points: <strong>{{ totalPoints }}</strong>
              </label>
            </div>
          </div>
        </div>

        <!-- Answer Key Setup -->
        <div class="content-card">
          <div class="card-header">
            <div class="card-title-wrapper">
              <div class="card-icon">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M9 12l2 2 4-4"></path>
                  <path d="M21 12c-1 0-3-1-3-3s2-3 3-3 3 1 3 3-2 3-3 3"></path>
                  <path d="M3 12c1 0 3-1 3-3s-2-3-3-3-3 1-3 3 2 3 3 3"></path>
                  <path d="M12 3v18"></path>
                </svg>
              </div>
              <div>
                <h2>Answer Key Setup</h2>
                <p>Provide the correct answers for automatic scoring</p>
              </div>
            </div>
          </div>
          <div class="card-body">
            <div class="answer-key-tabs">
              <button type="button" class="tab-button" :class="{ active: answerKeyMethod === 'upload' }" 
                      @click="answerKeyMethod = 'upload'">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" style="vertical-align:middle;margin-right:4px;">
                  <path d="M19.35 10.04C18.67 6.59 15.64 4 12 4 9.11 4 6.6 5.64 5.35 8.04 2.34 8.36 0 10.91 0 14c0 3.31 2.69 6 6 6h13c2.76 0 5-2.24 5-5 0-2.64-2.05-4.78-4.65-4.96zM14 13v4h-4v-4H7l5-5 5 5h-3z"/>
                </svg> Upload Answer Key
              </button>
              <button type="button" class="tab-button" :class="{ active: answerKeyMethod === 'manual' }" 
                      @click="answerKeyMethod = 'manual'">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" style="vertical-align:middle;margin-right:4px;">
                  <path d="M3 17.25V21h3.75L17.81 9.94l-3.75-3.75L3 17.25zM20.71 7.04c.39-.39.39-1.02 0-1.41l-2.34-2.34a.9959.9959 0 0 0-1.41 0l-1.83 1.83 3.75 3.75 1.83-1.83z"/>
                </svg> Manual Input
              </button>
            </div>

            <!-- Upload Answer Key -->
            <div v-if="answerKeyMethod === 'upload'" class="answer-key-section">
              <div class="file-upload-area" :class="{ 'drag-over': isAnswerKeyDragOver }" 
                   @dragover.prevent="handleAnswerKeyDragOver" 
                   @dragleave.prevent="handleAnswerKeyDragLeave" 
                   @drop.prevent="handleAnswerKeyDrop" 
                   @click="($refs.answerKeyInput as HTMLInputElement)?.click()">
                <input type="file" @change="handleAnswerKeyUpload" class="file-input"
                  accept=".txt,.docx,.pdf,.jpg,.jpeg,.png" ref="answerKeyInput" />
                <div class="upload-content">
                  <svg class="upload-icon" fill="currentColor" viewBox="0 0 24 24" width="48" height="48">
                    <path d="M19.35 10.04C18.67 6.59 15.64 4 12 4 9.11 4 6.6 5.64 5.35 8.04 2.34 8.36 0 10.91 0 14c0 3.31 2.69 6 6 6h13c2.76 0 5-2.24 5-5 0-2.64-2.05-4.78-4.65-4.96zM14 13v4h-4v-4H7l5-5 5 5h-3z" />
                  </svg>
                  <p v-if="!answerKeyFile">
                    Drop answer key file here or <span class="upload-link">browse</span>
                  </p>
                  <p v-else class="file-selected">
                    🔑 {{ answerKeyFile.name }} ({{ formatFileSize(answerKeyFile.size) }})
                  </p>
                  <small>Answer key with correct answers (TXT, DOCX, PDF, Images)</small>
                </div>
              </div>
            </div>

            <!-- Manual Answer Key Input -->
            <div v-if="answerKeyMethod === 'manual'" class="answer-key-section">
              <div class="manual-input-tabs">
                <button type="button" class="input-tab" :class="{ active: manualInputMethod === 'individual' }" 
                        @click="manualInputMethod = 'individual'">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" style="vertical-align:middle;margin-right:4px;">
                    <path d="M3 17.25V21h3.75L17.81 9.94l-3.75-3.75L3 17.25zM20.71 7.04c.39-.39.39-1.02 0-1.41l-2.34-2.34a.9959.9959 0 0 0-1.41 0l-1.83 1.83 3.75 3.75 1.83-1.83z"/>
                  </svg> Individual Questions
                </button>
                <button type="button" class="input-tab" :class="{ active: manualInputMethod === 'bulk' }" 
                        @click="manualInputMethod = 'bulk'">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" style="vertical-align:middle;margin-right:4px;">
                    <path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm0 16H5V5h14v14z"/>
                  </svg> Bulk Text Input
                </button>
              </div>

              <!-- Individual Question Input -->
              <div v-if="manualInputMethod === 'individual'" class="manual-answers-container">
                <div v-if="numQuestions > 0" class="questions-list">
                  <div v-for="(question, index) in questionsList" :key="index" class="question-item-input">
                    <div class="question-header">
                      <span class="question-number">Q{{ index + 1 }}</span>
                      <select v-model="question.type" class="question-type-select">
                        <option value="multiple-choice">Multiple Choice</option>
                        <option value="true-false">True/False</option>
                      </select>
                    </div>
                    
                    <div v-if="question.type === 'multiple-choice'" class="answer-options">
                      <label>Correct Answer:</label>
                      <select v-model="question.correctAnswer" class="form-control">
                        <option value="">Select correct answer...</option>
                        <option value="A">A</option>
                        <option value="B">B</option>
                        <option value="C">C</option>
                        <option value="D">D</option>
                        <option value="E">E</option>
                      </select>
                    </div>
                    
                    <div v-if="question.type === 'true-false'" class="answer-options">
                      <label>Correct Answer:</label>
                      <select v-model="question.correctAnswer" class="form-control">
                        <option value="">Select correct answer...</option>
                        <option value="True">True</option>
                        <option value="False">False</option>
                      </select>
                    </div>
                  </div>
                </div>
                <div v-else class="no-questions-message">
                  <p>⚠️ Please set the number of questions first in the Assessment Configuration section above.</p>
                </div>
              </div>

              <!-- Bulk Text Input -->
              <div v-if="manualInputMethod === 'bulk'" class="bulk-input-container">
                <div class="bulk-input-header">
                  <h4>
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" style="vertical-align:middle;margin-right:4px;">
                      <path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm0 16H5V5h14v14z"/>
                    </svg> Bulk Answer Key Input
                  </h4>
                  <p>Enter your answer key in any format. The system will automatically detect the pattern.</p>
                  <div class="format-examples">
                    <div class="example-tabs">
                      <button v-for="(example, key) in bulkExamples" :key="key" 
                              @click="activeBulkExample = key" 
                              class="example-tab" :class="{ active: activeBulkExample === key }">
                        {{ example.name }}
                      </button>
                    </div>
                    <div class="example-content">
                      <small>{{ bulkExamples[activeBulkExample].description }}</small>
                      <pre class="example-code">{{ bulkExamples[activeBulkExample].content }}</pre>
                      <button @click="loadExample(activeBulkExample)" class="load-example-btn">
                        <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor" style="vertical-align:middle;margin-right:2px;">
                          <path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm0 16H5V5h14v14z"/>
                        </svg> Use This Example
                      </button>
                    </div>
                  </div>
                </div>
                
                <textarea v-model="bulkAnswerText" 
                          class="bulk-input-textarea" 
                          placeholder="Enter your answer key here in any format..."
                          rows="12"
                          @input="parseBulkInput">
                </textarea>
                
                <div v-if="bulkParsedQuestions.length > 0" class="bulk-preview">
                  <h4>
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" style="vertical-align:middle;margin-right:4px;">
                      <path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm0 16H5V5h14v14z"/>
                    </svg> Detected Questions ({{ bulkParsedQuestions.length }})
                  </h4>
                  <div class="bulk-preview-grid">
                    <div v-for="(question, index) in bulkParsedQuestions" :key="index" 
                         class="bulk-preview-item" :class="question.type">
                      <span class="preview-q-num">Q{{ question.id }}</span>
                      <span class="preview-answer">{{ question.answer }}</span>
                      <span class="preview-type">{{ question.type }}</span>
                    </div>
                  </div>
                  <button @click="applyBulkAnswers" class="apply-bulk-btn">
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor" style="vertical-align:middle;margin-right:2px;">
                      <path d="M9 16.2l-3.5-3.5 1.41-1.41L9 13.38l7.09-7.09 1.41 1.41z"/>
                    </svg> Apply These Answers ({{ bulkParsedQuestions.length }} questions)
                  </button>
                </div>
              </div>
            </div>

            <!-- Answer Key Preview -->
            <div v-if="hasAnswerKey" class="answer-key-preview">
              <h4>Answer Key Preview</h4>
              <div class="preview-grid">
                <div v-for="(answer, index) in answerKeyPreview" :key="index" class="answer-preview-item">
                  <span class="q-num">Q{{ index + 1 }}</span>
                  <span class="q-answer" :class="answer.type">{{ answer.answer }}</span>
                  <span class="q-type">{{ answer.type }}</span>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Student Assessment Upload -->
        <div class="content-card">
          <div class="card-header">
            <div class="card-title-wrapper">
              <div class="card-icon">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path>
                  <polyline points="17,8 12,3 7,8"></polyline>
                  <line x1="12" y1="3" x2="12" y2="15"></line>
                </svg>
              </div>
              <div>
                <h2>Student Assessment Upload</h2>
                <p>Upload a student's completed assessment for automatic scoring</p>
              </div>
            </div>
          </div>
          <div class="card-body">
            <div class="form-row">
              <div class="form-group">
                <label for="student-name">Student Name (Optional)</label>
                <input v-model="studentName" id="student-name" type="text" class="form-control"
                  placeholder="Will auto-detect from file if available" />
                <small class="form-hint">💡 Leave blank if the student name is already in the assessment file</small>
              </div>

              <div class="form-group">
                <label for="assessment-type">Assessment Type</label>
                <select v-model="selectedTemplate" id="assessment-type" class="form-control" required>
                  <option value="">Select assessment type...</option>
                  <option value="multiple-choice">Multiple Choice Questions Only</option>
                  <option value="true-false">True/False Questions Only</option>
                  <option value="mixed">Mixed Format (MCQ + True/False)</option>
                </select>
              </div>
            </div>

            <!-- Upload File Section -->
            <div class="file-upload-area" :class="{ 'drag-over': isDragOver }" @dragover.prevent="handleDragOver"
              @dragleave.prevent="handleDragLeave" @drop.prevent="handleDrop" @click="($refs.fileInput as HTMLInputElement)?.click()">
              <input type="file" id="file-upload" @change="handleFileUpload" class="file-input"
                accept=".txt,.docx,.pdf,.jpg,.jpeg,.png" ref="fileInput" />
              <div class="upload-content">
                <svg class="upload-icon" fill="currentColor" viewBox="0 0 24 24" width="48" height="48">
                  <path
                    d="M19.35 10.04C18.67 6.59 15.64 4 12 4 9.11 4 6.6 5.64 5.35 8.04 2.34 8.36 0 10.91 0 14c0 3.31 2.69 6 6 6h13c2.76 0 5-2.24 5-5 0-2.64-2.05-4.78-4.65-4.96zM14 13v4h-4v-4H7l5-5 5 5h-3z" />
                </svg>
                <p v-if="!assessmentFile">
                  Drop student's assessment here or <span class="upload-link">browse</span>
                </p>
                <p v-else class="file-selected">
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" style="vertical-align:middle;margin-right:4px;">
                    <path d="M6 2a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8l-6-6H6zm7 7V3.5L18.5 9H13z"/>
                  </svg>
                  {{ assessmentFile.name }} ({{ formatFileSize(assessmentFile.size) }})
                </p>
                <small>Supported: TXT, DOCX, PDF, Images (JPG, PNG)</small>
              </div>
            </div>

            <!-- Detected Questions from Upload (if questionnaire only) -->
            <div v-if="detectedQuestions.length > 0" class="detected-questions">
              <h4>📋 Detected Questions - Please Set Correct Answers</h4>
              <p class="detection-note">We detected {{ detectedQuestions.length }} questions. Please select the correct answers below:</p>
              
              <div class="detected-questions-list">
                <div v-for="(question, index) in detectedQuestions" :key="index" class="detected-question-item">
                  <div class="question-content">
                    <div class="question-text">
                      <span class="q-number">Q{{ index + 1 }}.</span>
                      <span class="q-text">{{ question.text }}</span>
                    </div>
                    
                    <div v-if="question.options && question.options.length > 0" class="question-options">
                      <div class="option-selection">
                        <label>Select Correct Answer:</label>
                        <div class="options-grid">
                          <label v-for="(option, optIndex) in question.options" :key="optIndex" 
                                 class="option-item" :class="{ selected: question.correctAnswer === option.letter }">
                            <input type="radio" :name="`question_${index}`" 
                                   :value="option.letter" v-model="question.correctAnswer" />
                            <span class="option-letter">{{ option.letter }}.</span>
                            <span class="option-text">{{ option.text }}</span>
                          </label>
                        </div>
                      </div>
                    </div>
                    
                    <div v-else class="true-false-selection">
                      <label>Select Correct Answer:</label>
                      <div class="tf-options">
                        <label class="tf-option" :class="{ selected: question.correctAnswer === 'True' }">
                          <input type="radio" :name="`question_${index}`" value="True" v-model="question.correctAnswer" />
                          <span>True</span>
                        </label>
                        <label class="tf-option" :class="{ selected: question.correctAnswer === 'False' }">
                          <input type="radio" :name="`question_${index}`" value="False" v-model="question.correctAnswer" />
                          <span>False</span>
                        </label>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              
              <div class="answer-key-actions">
                <button @click="autoGenerateAnswerKey" class="btn-secondary">
                  <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor" style="vertical-align:middle;margin-right:2px;">
                    <circle cx="12" cy="12" r="10"/><path d="M8 12l2 2 4-4"/>
                  </svg> Auto-Generate Sample Answers
                </button>
                <button @click="saveDetectedAnswerKey" class="btn-primary" :disabled="!allQuestionsAnswered">
                  <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor" style="vertical-align:middle;margin-right:2px;">
                    <path d="M9 16.2l-3.5-3.5 1.41-1.41L9 13.38l7.09-7.09 1.41 1.41z"/>
                  </svg> Save Answer Key ({{ answeredQuestionsCount }}/{{ detectedQuestions.length }})
                </button>
              </div>
            </div>
          </div>
        </div>

        <!-- Results Display -->
        <div v-if="gradingResults" class="card results-card">
          <div class="card-header">
            <h2>AI Grading Results</h2>
            <p>Automated analysis completed for {{ gradingResults.studentName }}'s assessment</p>
          </div>
          <div class="card-body">
            
            <!-- ⭐ Feedback Type Indicator Banner -->
            <div v-if="feedbackTypeMessage" class="feedback-type-banner" 
                 :style="{ background: feedbackTypeMessage.bgColor, color: feedbackTypeMessage.textColor }">
              <div class="banner-content">
                <span class="banner-icon">{{ feedbackTypeMessage.icon }}</span>
                <div class="banner-text">
                  <h4>{{ feedbackTypeMessage.title }}</h4>
                  <p>{{ feedbackTypeMessage.description }}</p>
                </div>
                <span v-if="feedbackTypeMessage.type === 'rule-based'" class="banner-badge">Fallback Mode</span>
              </div>
            </div>
            
            <!-- Score Overview -->
            <div class="score-overview">
              <div class="score-circle" :class="getScoreClass(gradingResults.percentage)">
                <div class="score-value">{{ gradingResults.percentage }}%</div>
                <div class="score-label">Overall Score</div>
              </div>
              <div class="score-details">
                <div class="detail-item">
                  <span class="detail-label">Student:</span>
                  <span class="detail-value">{{ gradingResults.studentName }}</span>
                </div>
                <div class="detail-item">
                  <span class="detail-label">Assessment:</span>
                  <span class="detail-value">{{ gradingResults.assessmentTitle }}</span>
                </div>
                <div class="detail-item">
                  <span class="detail-label">Points Earned:</span>
                  <span class="detail-value">{{ gradingResults.pointsEarned }} / {{ gradingResults.totalPoints }}</span>
                </div>
                <div class="detail-item">
                  <span class="detail-label">Letter Grade:</span>
                  <span class="detail-value grade-letter" :class="getGradeClass(gradingResults.percentage)">
                    {{ getLetterGrade(gradingResults.percentage) }}
                  </span>
                </div>
              </div>
            </div>

            <!-- AI Feedback -->
            <div v-if="gradingResults.feedback" class="ai-feedback">
              <h3>AI-Generated Feedback</h3>
              
              <div class="feedback-section">
                <h4><span class="feedback-icon">💪</span> Strengths Identified</h4>
                <ul class="feedback-list strengths">
                  <li v-for="strength in gradingResults.feedback.strengths" :key="strength">{{ strength }}</li>
                </ul>
              </div>

              <div class="feedback-section">
                <h4><span class="feedback-icon">🎯</span> Areas for Improvement</h4>
                <ul class="feedback-list weaknesses">
                  <li v-for="weakness in gradingResults.feedback.weaknesses" :key="weakness">{{ weakness }}</li>
                </ul>
              </div>

              <div class="feedback-section">
                <h4><span class="feedback-icon">📚</span> Recommendations</h4>
                <ul class="feedback-list recommendations">
                  <li v-for="rec in gradingResults.feedback.recommendations" :key="rec">{{ rec }}</li>
                </ul>
              </div>

              <div v-if="gradingResults.feedback.detailedAnalysis" class="detailed-analysis">
                <h4><span class="feedback-icon">🔍</span> Detailed Analysis</h4>
                <p>{{ gradingResults.feedback.detailedAnalysis }}</p>
              </div>
            </div>

            <!-- Question-by-Question Breakdown -->
            <div v-if="gradingResults.questionBreakdown" class="question-breakdown">
              <h3>Question-by-Question Analysis</h3>
              <div class="breakdown-list">
                <div v-for="(question, index) in gradingResults.questionBreakdown" :key="index" 
                     class="question-item" :class="{ 'correct': question.isCorrect, 'incorrect': !question.isCorrect }">
                  <div class="question-header">
                    <span class="question-number">Q{{ index + 1 }}</span>
                    <span class="question-status">{{ question.isCorrect ? '✅ Correct' : '❌ Incorrect' }}</span>
                    <span class="question-points">{{ question.pointsEarned }}/{{ question.pointsPossible }} pts</span>
                  </div>
                  <div v-if="question.feedback" class="question-feedback">
                    <p>{{ question.feedback }}</p>
                  </div>
                </div>
              </div>
            </div>

            <!-- Action Buttons -->
            <div class="results-actions">
              <button @click="downloadReport" class="btn-secondary">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor" style="vertical-align:middle;margin-right:2px;">
                  <path d="M6 2a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8l-6-6H6zm7 7V3.5L18.5 9H13z"/>
                </svg> Download Report
              </button>
              <button @click="viewAllAssessments" class="btn-primary">
                  View All Assessments
              </button>
              <button @click="resetForm" class="btn-secondary">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor" style="vertical-align:middle;margin-right:2px;">
                  <path d="M12 2v2m0 16v2m8-10h2M2 12H0m16.24-7.76l1.42-1.42M4.34 19.66l-1.42 1.42M19.66 19.66l1.42 1.42M4.34 4.34L2.92 2.92"/>
                </svg> Check Another Assessment
              </button>
            </div>
          </div>
        </div>

        <!-- Error -->
        <div v-if="error" class="error-message">
          <div class="error-content">
            <strong>Error:</strong> 
            <pre class="error-text">{{ error }}</pre>
          </div>
          
          <!-- Quick Fix Suggestions -->
          <div v-if="error.includes('questions but no student answers')" class="error-suggestions">
            <h4>💡 Quick Fix Suggestions:</h4>
            <div class="suggestion-buttons">
              <button @click="moveFileToAnswerKey" class="suggestion-btn" v-if="assessmentFile">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor" style="vertical-align:middle;margin-right:2px;">
                  <path d="M19.35 10.04C18.67 6.59 15.64 4 12 4 9.11 4 6.6 5.64 5.35 8.04 2.34 8.36 0 10.91 0 14c0 3.31 2.69 6 6 6h13c2.76 0 5-2.24 5-5 0-2.64-2.05-4.78-4.65-4.96zM14 13v4h-4v-4H7l5-5 5 5h-3z"/>
                </svg> Use This File as Answer Key
              </button>
              <button @click="clearFileAndShowExample" class="suggestion-btn">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor" style="vertical-align:middle;margin-right:2px;">
                  <path d="M3 17.25V21h3.75L17.81 9.94l-3.75-3.75L3 17.25zM20.71 7.04c.39-.39.39-1.02 0-1.41l-2.34-2.34a.9959.9959 0 0 0-1.41 0l-1.83 1.83 3.75 3.75 1.83-1.83z"/>
                </svg> Show Example of Student Response File
              </button>
              <button @click="clearErrorAndContinue" class="suggestion-btn">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor" style="vertical-align:middle;margin-right:2px;">
                  <path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"/>
                </svg> Clear Error & Continue
              </button>
            </div>
          </div>
        </div>

        <!-- Action Buttons -->
        <div class="action-buttons">
          <button @click="clearForm" class="btn-secondary">Clear Form</button>
          <button @click="submitAssessment" class="btn-submit" :disabled="!canSubmit || isLoading">
            <span v-if="isLoading">Processing...</span>
            <span v-else>
              <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" style="vertical-align:middle;margin-right:4px;">
                <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8zm0-14c-3.31 0-6 2.69-6 6s2.69 6 6 6 6-2.69 6-6-2.69-6-6-6zm0 10c-2.21 0-4-1.79-4-4s1.79-4 4-4 4 1.79 4-4 4z"/>
              </svg> Start AI Grading
            </span>
          </button>
        </div>
      </div>
    </main>

    <!-- Logout Confirmation Modal -->
    <div v-if="showLogoutModal" class="modal-overlay" @click="closeLogoutModal">
      <div class="modal-content logout-modal" @click.stop>
        <div class="modal-header logout-header">
          <h3>Confirm Logout</h3>
        </div>
        <div class="modal-body">
          <div class="logout-icon">
            <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"/>
              <polyline points="16 17 21 12 16 7"/>
              <line x1="21" y1="12" x2="9" y2="12"/>
            </svg>
          </div>
          <p class="logout-message">Are you sure you want to logout?</p>
          <p class="logout-submessage">You will be redirected to the login page.</p>
        </div>
        <div class="modal-footer logout-footer">
          <button @click="closeLogoutModal" class="btn-cancel" :disabled="isLoggingOut">Cancel</button>
          <button @click="confirmLogout" class="btn-logout" :disabled="isLoggingOut">
            <span v-if="!isLoggingOut">Logout</span>
            <span v-else class="loading-text">
              <div class="logout-spinner"></div>
              Redirecting...
            </span>
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, watch, nextTick, onMounted } from "vue";
import { useRouter } from "vue-router";
import { supabase } from '@/supabase.js';
import { useDarkMode } from "../../composables/useDarkMode.js";
import { useTeacherAuth } from "../../composables/useTeacherAuth.js";
import { API_URL } from '@/api.js'

const router = useRouter();
const { isDarkMode } = useDarkMode();
const { teacherInfo, isAuthenticated } = useTeacherAuth();

// ==================== NAVBAR & AUTH ====================
const showNotifDropdown = ref(false);
const showProfileDropdown = ref(false);
const notifications = ref([]);
const fullName = ref('');
const nameLoading = ref(true);
const showScrollTop = ref(false);
const teacherId = ref(null);

// ==================== LOGOUT MODAL ====================
const showLogoutModal = ref(false);
const isLoggingOut = ref(false);

// ==================== LOADING & ERROR ====================
const isLoading = ref(false);
const loadingMessage = ref("Processing...");
const isDragOver = ref(false);
const isAnswerKeyDragOver = ref(false);
const error = ref("");
const processingSteps = ref([]);

// ==================== STUDENT & ASSESSMENT INFO ====================
const studentName = ref("");
const assessmentTitle = ref("");
const subject = ref("");
const numQuestions = ref(10);
const pointsPerQuestion = ref(5);
const scoringMethod = ref("uniform");
const totalPoints = ref(50);
const selectedTemplate = ref("");
const assessmentFile = ref(null);

// ==================== ANSWER KEY MANAGEMENT ====================
const answerKeyMethod = ref("upload");
const answerKeyFile = ref(null);
const questionsList = ref([]);
const detectedQuestions = ref([]);

// ==================== MANUAL INPUT MANAGEMENT ====================
const manualInputMethod = ref("individual");
const bulkAnswerText = ref("");
const bulkParsedQuestions = ref([]);
const activeBulkExample = ref("tf_end");

// ==================== BULK EXAMPLES ====================
const bulkExamples = ref({
  tf_start: {
    name: "T/F Start",
    description: "True/False answers at the beginning of each line",
    content: `T 1. The earth orbits the sun.
F 2. Fish can live without water.
T 3. Plants need sunlight to grow.`
  },
  tf_end: {
    name: "T/F End", 
    description: "True/False answers at the end of each line",
    content: `1. The sky is blue. T
2. Humans can breathe underwater. F
3. Fire is hot. T`
  },
  mc_start: {
    name: "MC Start",
    description: "Multiple choice answers at the beginning",
    content: `B 1. What is the capital of Japan?
A 2. Which is a fruit?
C 3. What color is grass?`
  },
  mc_answer: {
    name: "MC Answer",
    description: "Multiple choice with Answer: keyword",
    content: `1. What is the largest planet?
Answer: C

2. What color is the sun?  
Answer: C`
  },
  simple: {
    name: "Simple",
    description: "Just the answers in order",
    content: `1. A
2. B
3. T
4. F
5. C`
  },
  mixed: {
    name: "Mixed",
    description: "Mixed format with sections",
    content: `True or False
1. The Earth is round. T
2. Water boils at 100°C. T

Multiple Choice  
1. What is 2+2? B
2. What is 3+3? C`
  }
});

// ==================== RESULTS ====================
const gradingResults = ref(null);

// ==================== COMPUTED PROPERTIES ====================

const canSubmit = computed(() => {
  const hasBasicInfo = subject.value && 
                      assessmentTitle.value &&
                      numQuestions.value &&
                      pointsPerQuestion.value &&
                      selectedTemplate.value && 
                      assessmentFile.value &&
                      !isLoading.value;
  
  const hasAnswerKeyData = questionsList.value.length > 0 && 
                          questionsList.value.some(q => q.correctAnswer);
  
  const hasAnswerKeyFile = !!answerKeyFile.value;
  
  const hasAnswerKeySetup = hasAnswerKeyData || hasAnswerKeyFile;
  
  console.log('🔍 canSubmit Debug:', {
    subject: !!subject.value,
    assessmentTitle: !!assessmentTitle.value,
    numQuestions: !!numQuestions.value,
    pointsPerQuestion: !!pointsPerQuestion.value,
    selectedTemplate: !!selectedTemplate.value,
    assessmentFile: !!assessmentFile.value,
    isLoading: isLoading.value,
    questionsCount: questionsList.value.length,
    questionsWithAnswers: questionsList.value.filter(q => q.correctAnswer).length,
    canSubmit: hasBasicInfo && hasAnswerKeySetup
  });
  
  return hasBasicInfo && hasAnswerKeySetup;
});

const hasAnswerKey = computed(() => {
  if (answerKeyMethod.value === 'upload') {
    const hasFile = !!answerKeyFile.value;
    const hasQuestions = questionsList.value.length > 0;
    const hasAnswers = questionsList.value.some(q => q.correctAnswer);
    return hasFile || (hasQuestions && hasAnswers);
  } else if (answerKeyMethod.value === 'manual') {
    const hasQuestions = questionsList.value.length > 0;
    const hasAnswers = questionsList.value.some(q => q.correctAnswer);
    return hasQuestions && hasAnswers;
  }
  return false;
});

const answerKeyPreview = computed(() => {
  return questionsList.value
    .filter(q => q.correctAnswer)
    .map((q) => ({
      answer: q.correctAnswer || '',
      type: q.type || 'multiple-choice'
    }));
});

const allQuestionsAnswered = computed(() => {
  return detectedQuestions.value.length > 0 && 
         detectedQuestions.value.every(q => q.correctAnswer);
});

const answeredQuestionsCount = computed(() => {
  return detectedQuestions.value.filter(q => q.correctAnswer).length;
});

const pointDistribution = computed(() => {
  const distribution = {};
  questionsList.value.forEach(q => {
    const points = parseInt(q.points) || 1;
    distribution[points] = (distribution[points] || 0) + 1;
  });
  return distribution;
});

const feedbackTypeMessage = computed(() => {
  if (!gradingResults.value) return null;
  
  const aiUsed = gradingResults.value.aiUsed;
  
  if (aiUsed) {
    return {
      type: 'ai',
      icon: '🤖',
      title: 'AI-Powered Feedback',
      description: 'Generated using advanced AI analysis',
      bgColor: 'linear-gradient(135deg, #3b82f6, #2563eb)',
      textColor: 'white'
    };
  } else {
    return {
      type: 'rule-based',
      icon: '📊',
      title: 'Rule-Based Feedback',
      description: 'Generated using intelligent rule-based analysis',
      bgColor: 'linear-gradient(135deg, #f59e0b, #d97706)',
      textColor: 'white'
    };
  }
});

// ==================== WATCHERS ====================

watch(questionsList, (newVal) => {
  console.log('👀 questionsList CHANGED:', {
    length: newVal.length,
    withAnswers: newVal.filter(q => q.correctAnswer).length,
    data: JSON.stringify(newVal, null, 2)
  });
}, { deep: true });

// ==================== QUESTION MANAGEMENT ====================

const updateQuestionsList = () => {
  const count = parseInt(String(numQuestions.value)) || 0;
  const newList = Array.from({ length: count }, (_, index) => ({
    id: index + 1,
    type: 'multiple-choice',
    correctAnswer: '',
    points: parseInt(String(pointsPerQuestion.value)) || 1
  }));
  questionsList.value = newList;
  calculateTotalPoints();
  console.log('📋 Updated questions list:', newList);
};

const handleScoringMethodChange = () => {
  if (scoringMethod.value === 'uniform') {
    questionsList.value.forEach(q => {
      q.points = parseInt(String(pointsPerQuestion.value)) || 1;
    });
  }
  calculateTotalPoints();
};

const calculateTotalPoints = () => {
  if (scoringMethod.value === 'uniform') {
    const questions = parseInt(String(numQuestions.value)) || 0;
    const points = parseInt(String(pointsPerQuestion.value)) || 0;
    totalPoints.value = questions * points;
  } else {
    totalPoints.value = questionsList.value.reduce((sum, q) => sum + (parseInt(q.points) || 0), 0);
  }
  console.log('📊 Total Points Calculated:', totalPoints.value);
};

const assignAllPoints = (points) => {
  questionsList.value.forEach(q => {
    q.points = points;
  });
  calculateTotalPoints();
};

const setCustomPattern = () => {
  const pattern = prompt(`Set custom point pattern. Examples:
  
1. "1-9:1,10:5" = Questions 1-9 get 1 point, Question 10 gets 5 points
2. "1-5:2,6-10:3" = Questions 1-5 get 2 points, Questions 6-10 get 3 points
3. "all:1,10:5" = All questions get 1 point except Question 10 gets 5 points

Enter pattern:`);
  
  if (pattern) {
    try {
      applyCustomPattern(pattern);
      calculateTotalPoints();
    } catch (err) {
      console.error('Error applying pattern:', err);
      alert("Invalid pattern format. Please use format like '1-9:1,10:5'");
    }
  }
};

const applyCustomPattern = (pattern) => {
  const parts = pattern.split(',');
  
  parts.forEach(part => {
    const [range, points] = part.split(':');
    const pointValue = parseInt(points);
    
    if (range.trim() === 'all') {
      questionsList.value.forEach(q => {
        q.points = pointValue;
      });
    } else if (range.includes('-')) {
      const [start, end] = range.split('-').map(n => parseInt(n.trim()));
      for (let i = start - 1; i < end && i < questionsList.value.length; i++) {
        questionsList.value[i].points = pointValue;
      }
    } else {
      const questionNum = parseInt(range.trim());
      if (questionNum > 0 && questionNum <= questionsList.value.length) {
        questionsList.value[questionNum - 1].points = pointValue;
      }
    }
  });
};

// ==================== ANSWER KEY FILE HANDLING ====================

const handleAnswerKeyDragOver = () => {
  isAnswerKeyDragOver.value = true;
};

const handleAnswerKeyDragLeave = () => {
  isAnswerKeyDragOver.value = false;
};

const handleAnswerKeyDrop = (event) => {
  const file = event.dataTransfer.files[0];
  if (file) {
    answerKeyFile.value = file;
    processAnswerKeyFile(file);
    error.value = "";
  }
  isAnswerKeyDragOver.value = false;
};

const handleAnswerKeyUpload = (event) => {
  const file = event.target.files[0];
  if (file) {
    answerKeyFile.value = file;
    processAnswerKeyFile(file);
    error.value = "";
  }
};

const processAnswerKeyFile = async (file) => {
  isLoading.value = true;
  loadingMessage.value = "Processing answer key...";
  
  try {
    const formData = new FormData();
    formData.append('file', file);
    
    const response = await fetch(`${API_URL}/api/assessments/process-answer-key`, {
  method: 'POST',
  body: formData
})

    if (!response.ok) {
      if (response.status === 0 || !response.status) {
        throw new Error('Backend server is not running. Please start the backend server at http://localhost:8000');
      }
      const errorText = await response.text();
      throw new Error(`Server error: ${response.status} - ${errorText}`);
    }

    const result = await response.json();
    
    if (result.questions && result.questions.length > 0) {
      const newQuestions = result.questions.map((q) => ({
        id: q.id,
        type: q.type || 'multiple-choice',
        correctAnswer: q.answer || q.correctAnswer || '',
        points: q.points || parseInt(String(pointsPerQuestion.value)) || 1
      }));
      
      questionsList.value = [];
      await nextTick();
      questionsList.value = newQuestions;
      await nextTick();
      
      numQuestions.value = result.questions.length;
      calculateTotalPoints();
      error.value = "";
      
      const mcqCount = newQuestions.filter(q => q.type === 'multiple-choice').length;
      const tfCount = newQuestions.filter(q => q.type === 'true-false').length;
      
      alert(`✅ Successfully processed ${result.questions.length} questions!\n\n📊 Breakdown:\n- Multiple Choice: ${mcqCount}\n- True/False: ${tfCount}\n\nFormat: ${result.format_detected || 'flexible'}\n\n✨ Answer key preview should now be visible!`);
    } else {
      throw new Error("No questions found in the uploaded answer key file");
    }
  } catch (err) {
    console.error('❌ Error processing answer key:', err);
    if (err.message.includes('Failed to fetch') || err.message.includes('Backend server')) {
      error.value = "🚫 Backend server is not running!\n\nPlease start the backend server:\n1. Open terminal in backend folder\n2. Run: uvicorn main:app --reload\n3. Server should start at http://localhost:8000";
    } else {
      error.value = "Failed to process answer key: " + err.message;
    }
  } finally {
    isLoading.value = false;
  }
};

// ==================== STUDENT ASSESSMENT FILE HANDLING ====================

const handleFileUpload = (event) => {
  const file = event.target.files[0];
  if (file) {
    assessmentFile.value = file;
    error.value = "";
  }
};

const handleDragOver = () => {
  isDragOver.value = true;
};

const handleDragLeave = () => {
  isDragOver.value = false;
};

const handleDrop = (event) => {
  const file = event.dataTransfer.files[0];
  if (file) {
    assessmentFile.value = file;
    error.value = "";
  }
  isDragOver.value = false;
};

const autoGenerateAnswerKey = () => {
  detectedQuestions.value.forEach(question => {
    if (question.type === 'true-false') {
      question.correctAnswer = Math.random() > 0.5 ? 'True' : 'False';
    } else {
      const options = ['A', 'B', 'C', 'D', 'E'];
      const availableOptions = question.options?.map(opt => opt.letter) || options.slice(0, 4);
      question.correctAnswer = availableOptions[Math.floor(Math.random() * availableOptions.length)];
    }
  });
};

const saveDetectedAnswerKey = () => {
  if (!allQuestionsAnswered.value) {
    error.value = "Please answer all questions before saving the answer key.";
    return;
  }
  
  questionsList.value = detectedQuestions.value.map((q, index) => ({
    id: index + 1,
    type: q.type,
    correctAnswer: q.correctAnswer,
    points: parseInt(String(pointsPerQuestion.value)) || 1
  }));
  
  numQuestions.value = detectedQuestions.value.length;
  calculateTotalPoints();
  detectedQuestions.value = [];
  answerKeyMethod.value = 'manual';
  
  console.log('✅ Answer key saved:', questionsList.value);
  alert("Answer key saved successfully! You can now proceed with grading.");
};

const formatFileSize = (size) => {
  if (size < 1024) return size + " bytes";
  else if (size < 1048576) return (size / 1024).toFixed(1) + " KB";
  else return (size / 1048576).toFixed(1) + " MB";
};

// ==================== PROCESSING STEPS ====================

const setupProcessingSteps = () => {
  processingSteps.value = [
    { text: "Uploading files to server", completed: false, active: true },
    { text: "Parsing assessment content", completed: false, active: false },
    { text: "Comparing with answer key", completed: false, active: false },
    { text: "Generating AI feedback", completed: false, active: false },
    { text: "Calculating final scores", completed: false, active: false },
    { text: "Saving to database", completed: false, active: false }
  ];
};

const updateProcessingStep = (stepIndex) => {
  if (stepIndex > 0) {
    processingSteps.value[stepIndex - 1].completed = true;
    processingSteps.value[stepIndex - 1].active = false;
  }
  if (stepIndex < processingSteps.value.length) {
    processingSteps.value[stepIndex].active = true;
  }
};

// ==================== MAIN SUBMIT FUNCTION ====================

const submitAssessment = async () => {
  if (!subject.value || !assessmentTitle.value || !numQuestions.value || !pointsPerQuestion.value || !selectedTemplate.value || !assessmentFile.value) {
    error.value = "Please fill in all required fields and upload a file.";
    return;
  }

  if (!hasAnswerKey.value) {
    error.value = "Answer key is required! Please provide an answer key before proceeding.";
    return;
  }

  isLoading.value = true;
  error.value = "";
  gradingResults.value = null;
  setupProcessingSteps();

  try {
    loadingMessage.value = "Uploading files to server...";
    updateProcessingStep(0);

    const formData = new FormData();
    formData.append('file', assessmentFile.value);
    formData.append('student_name', studentName.value || 'Anonymous');
    formData.append('assessment_title', assessmentTitle.value);
    formData.append('subject', subject.value);
    formData.append('num_questions', numQuestions.value.toString());
    formData.append('total_points', totalPoints.value.toString());
    formData.append('points_per_question', pointsPerQuestion.value.toString());
    formData.append('assessment_type', selectedTemplate.value);
    formData.append('use_ai_feedback', 'true');
    
    const answerKeyData = questionsList.value.map((q, index) => ({
      id: index + 1,
      type: q.type,
      correctAnswer: q.correctAnswer,
      points: parseInt(String(q.points)) || 1
    }));
    
    console.log('📤 Sending Answer Key Data:', answerKeyData);
    console.log('📊 Total Points:', totalPoints.value);
    
    formData.append('answer_key_data', JSON.stringify(answerKeyData));
    formData.append('scoring_method', scoringMethod.value);

    updateProcessingStep(1);
    loadingMessage.value = "Parsing assessment content...";
    await new Promise(resolve => setTimeout(resolve, 500));

    const response = await fetch('http://localhost:8000/api/assessments/check-with-answer-key', {
      method: 'POST',
      body: formData
    });

    if (!response.ok) {
      const errorText = await response.text();
      throw new Error(`Upload failed: ${response.status} - ${errorText}`);
    }

    const result = await response.json();

    updateProcessingStep(2);
    loadingMessage.value = "Comparing answers with answer key...";
    await new Promise(resolve => setTimeout(resolve, 800));

    updateProcessingStep(3);
    loadingMessage.value = "Generating AI-powered feedback...";
    await new Promise(resolve => setTimeout(resolve, 1500));

    updateProcessingStep(4);
    loadingMessage.value = "Calculating final scores...";
    await new Promise(resolve => setTimeout(resolve, 500));

    updateProcessingStep(5);
    loadingMessage.value = "Saving results to database...";
    await new Promise(resolve => setTimeout(resolve, 800));

    if (result.success && result.results) {
      gradingResults.value = {
        ...result.results,
        feedbackType: result.results.feedbackType || (result.results.aiUsed ? 'ai' : 'rule-based'),
        aiError: result.results.aiError || null,
        totalPoints: totalPoints.value,
        scoringMethod: scoringMethod.value
      };
      
      processingSteps.value.forEach(step => {
        step.completed = true;
        step.active = false;
      });

      setTimeout(() => {
        const aiUsed = result.results.aiUsed ? '✅ WITH AI-POWERED FEEDBACK' : '⚠️ WITHOUT AI';
        const dbSaved = result.results.databaseSaved ? '✅ SAVED TO DATABASE' : '⚠️ NOT SAVED';
        
        alert(`✅ Assessment checked successfully!\n\n${aiUsed}\n${dbSaved}\n\nScore: ${result.results.percentage}%\nPoints: ${result.results.pointsEarned}/${result.results.totalPoints}\nProcessing Time: ${result.processing_time}s`);
      }, 500);
    } else {
      throw new Error("Invalid response from server");
    }

  } catch (err) {
    console.error('Assessment processing error:', err);
    error.value = "Failed to process assessment: " + err.message;
  } finally {
    isLoading.value = false;
  }
};

// ==================== SCORE & GRADE UTILITIES ====================

const getScoreClass = (percentage) => {
  if (percentage >= 90) return "excellent";
  if (percentage >= 80) return "good";
  if (percentage >= 70) return "average";
  if (percentage >= 60) return "below-average";
  return "poor";
};

const getLetterGrade = (percentage) => {
  if (percentage >= 90) return "A";
  if (percentage >= 80) return "B";
  if (percentage >= 70) return "C";
  if (percentage >= 60) return "D";
  return "F";
};

const getGradeClass = (percentage) => {
  if (percentage >= 80) return "grade-a";
  if (percentage >= 70) return "grade-b";
  if (percentage >= 60) return "grade-c";
  return "grade-f";
};

// ==================== DOWNLOAD & EXPORT ====================

const downloadReport = () => {
  const reportData = {
    student: studentName.value,
    assessment: assessmentTitle.value,
    subject: subject.value,
    score: gradingResults.value.percentage,
    pointsEarned: gradingResults.value.pointsEarned,
    totalPoints: gradingResults.value.totalPoints,
    feedback: gradingResults.value.feedback,
    aiPowered: gradingResults.value.aiUsed,
    feedbackType: gradingResults.value.feedbackType,
    scoringMethod: scoringMethod.value
  };
  
  const blob = new Blob([JSON.stringify(reportData, null, 2)], { type: 'application/json' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = `${studentName.value}_${assessmentTitle.value}_report.json`;
  a.click();
  URL.revokeObjectURL(url);
};

// ==================== FORM RESET ====================

const resetForm = () => {
  console.log('🔄 Resetting form...');
  
  studentName.value = "";
  assessmentTitle.value = "";
  subject.value = "";
  numQuestions.value = 10;
  pointsPerQuestion.value = 5;
  totalPoints.value = 50;
  selectedTemplate.value = "";
  assessmentFile.value = null;
  answerKeyFile.value = null;
  questionsList.value = [];
  gradingResults.value = null;
  error.value = "";
  processingSteps.value = [];
  manualInputMethod.value = "individual";
  bulkAnswerText.value = "";
  bulkParsedQuestions.value = [];
  detectedQuestions.value = [];
  answerKeyMethod.value = "upload";
  
  console.log('✅ Form reset complete');
  
  // Reload teacher name after form clear
  loadTeacherName();
};

const clearForm = () => {
  resetForm();
};

const viewAllAssessments = () => {
  router.push('/teacher/assessment-history');
};

const moveFileToAnswerKey = () => {
  if (assessmentFile.value) {
    answerKeyFile.value = assessmentFile.value;
    answerKeyMethod.value = 'upload';
    processAnswerKeyFile(assessmentFile.value);
    assessmentFile.value = null;
    error.value = "";
    alert("✅ File moved to Answer Key section!\n\nNow please upload the student's completed assessment.");
  }
};

const clearFileAndShowExample = () => {
  assessmentFile.value = null;
  error.value = "";
  
  alert(`📝 Example Student Response Formats:

FORMAT 1 - Complete:
Student: John Smith
1. A
2. True
3. B

FORMAT 2 - Simple:
A
True
B
False

✅ Both formats work!`);
};

const clearErrorAndContinue = () => {
  error.value = "";
};

// ==================== BULK INPUT HANDLING ====================

const loadExample = (exampleKey) => {
  bulkAnswerText.value = bulkExamples.value[exampleKey].content;
  parseBulkInput();
};

const parseBulkInput = async () => {
  if (!bulkAnswerText.value.trim()) {
    bulkParsedQuestions.value = [];
    return;
  }

  try {
    const formData = new FormData();
    const blob = new Blob([bulkAnswerText.value], { type: 'text/plain' });
    formData.append('file', blob, 'bulk_answers.txt');

    const response = await fetch('http://localhost:8000/api/assessments/process-answer-key', {
      method: 'POST',
      body: formData
    });

    if (response.ok) {
      const result = await response.json();
      if (result.questions && result.questions.length > 0) {
        bulkParsedQuestions.value = result.questions.map(q => ({
          id: q.id,
          answer: q.answer || q.correctAnswer,
          type: q.type,
          text: q.text
        }));
        console.log('✅ Parsed bulk answers:', bulkParsedQuestions.value);
      } else {
        bulkParsedQuestions.value = [];
      }
    }
  } catch (err) {
    console.error('❌ Error parsing bulk input:', err);
    bulkParsedQuestions.value = [];
  }
};

const applyBulkAnswers = async () => {
  if (bulkParsedQuestions.value.length === 0) {
    alert("No questions to apply!");
    return;
  }

  console.log('📋 Applying bulk answers:', bulkParsedQuestions.value);

  const newList = bulkParsedQuestions.value.map((q) => ({
    id: q.id,
    type: q.type,
    correctAnswer: q.answer,
    points: parseInt(String(pointsPerQuestion.value)) || 1
  }));

  console.log('📝 New question list:', newList);

  questionsList.value = [];
  await nextTick();
  questionsList.value = newList;
  await nextTick();

  numQuestions.value = bulkParsedQuestions.value.length;
  calculateTotalPoints();
  manualInputMethod.value = 'individual';
  bulkAnswerText.value = "";
  bulkParsedQuestions.value = [];

  console.log('✅ Applied! questionsList is now:', questionsList.value);
  alert(`✅ Successfully applied ${newList.length} answers!\n\n📊 The "Start Grading" button should now be enabled!`);
};

// ==================== NAVBAR & DROPDOWN ====================

const toggleNotifDropdown = () => {
  showNotifDropdown.value = !showNotifDropdown.value;
  showProfileDropdown.value = false;
};

const toggleProfileDropdown = () => {
  showProfileDropdown.value = !showProfileDropdown.value;
  showNotifDropdown.value = false;
};

const handleNotificationClick = (notif) => {
  console.log('Notification clicked:', notif);
};

// ==================== LOGOUT ====================

const openLogoutModal = () => {
  showLogoutModal.value = true;
};

const closeLogoutModal = () => {
  showLogoutModal.value = false;
};

const confirmLogout = () => {
  localStorage.clear();
  sessionStorage.clear();
  supabase.auth.signOut().catch(err => console.log('Signout error:', err));
  
  // Immediate redirect - no waiting!
  setTimeout(() => {
    window.location.assign('/login');
  }, 100);
};

const logout = () => {
  openLogoutModal();
};

const scrollToTop = () => {
  window.scrollTo({ top: 0, behavior: 'smooth' });
};

// ==================== LOAD TEACHER NAME ====================

const loadTeacherName = async () => {
  nameLoading.value = true;
  console.log('👤 Loading teacher name...');
  
  try {
    if (teacherInfo.value?.id) {
      const { data: teacher, error } = await supabase
        .from('teachers')
        .select('full_name')
        .eq('id', teacherInfo.value.id)
        .single();
        
      if (!error && teacher) {
        fullName.value = teacher.full_name || 'Teacher';
        console.log('✅ Teacher name loaded:', fullName.value);
      } else {
        console.warn('❌ Failed to fetch teacher:', error);
        fullName.value = 'Teacher';
      }
    } else {
      console.warn('⚠️ teacherInfo not available');
      fullName.value = 'Teacher';
    }
  } catch (err) {
    console.error('❌ Error loading teacher name:', err);
    fullName.value = 'Teacher';
  } finally {
    nameLoading.value = false;
  }
};

// ==================== LIFECYCLE ====================

onMounted(async () => {
  console.log('🚀 Component mounted');
  
  // Load teacher name on mount
  await loadTeacherName();
  
  // Setup scroll listener
  const handleScroll = () => {
    showScrollTop.value = window.scrollY > 300;
  };
  window.addEventListener('scroll', handleScroll);

  return () => {
    window.removeEventListener('scroll', handleScroll);
  };
});

// ⭐ Watch for teacherInfo changes - Updates name in real-time
watch(
  () => teacherInfo.value,
  async (newTeacherInfo) => {
    if (newTeacherInfo?.id) {
      console.log('👀 teacherInfo changed, reloading name...');
      await loadTeacherName();
    }
  },
  { deep: true }
);

// ⭐ Also watch for isAuthenticated changes
watch(
  () => isAuthenticated.value,
  async (newAuth) => {
    if (newAuth) {
      console.log('✅ Authentication changed to true, reloading name...');
      await loadTeacherName();
    }
  }
);
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
/* Scroll-to-top floating button */
.scroll-to-top-btn {
  position: fixed;
  bottom: 32px;
  right: 32px;
  z-index: 1000;
  background: none;
  border: none;
  outline: none;
  cursor: pointer;
  box-shadow: 0 2px 8px rgba(61, 141, 122, 0.12);
  border-radius: 50%;
  transition: box-shadow 0.2s;
}
.scroll-to-top-btn:hover {
  box-shadow: 0 4px 16px rgba(61, 141, 122, 0.18);
}

  /* Base Styles */
  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }

  /* Dashboard container setup */
  .dashboard-container {
    display: flex;
    flex-direction: row;
    width: 100vw;
    height: 100vh;
    min-height: 100vh;
    background: #f8fafc;
    font-family: 'Inter', sans-serif;
    overflow: hidden;
  }
  .dark .dashboard-container {
    background: #0f172a;
  }

  /* Sidebar Navigation */
  .sidebar {
    position: fixed;
    top: 64px;
    left: 0;
    width: 80px;
    height: calc(100vh - 64px);
    background: #3D8D7A;
    border-right: none;
    z-index: 900;
    box-shadow: 2px 0 10px rgba(0, 0, 0, 0.05);
    overflow: visible;
  }

  .sidebar-nav {
    padding: 2rem 0.5rem 1rem 0.5rem;
  }

  .sidebar-item {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 56px;
    width: 56px;
    margin: 8px 0;
    border-radius: 12px;
    transition: background 0.2s, box-shadow 0.2s;
    cursor: pointer;
    position: relative;
    text-decoration: none;
  }

  .sidebar-item:hover {
    background: rgba(255,255,255,0.22);
    box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  }

  .sidebar-item.active {
    border: 2px solid #fff;
    background: rgba(255, 255, 255, 0.13);
    box-sizing: border-box;
  }

  .rounded-bg {
    background: rgba(255,255,255,0.13);
    border-radius: 16px;
    transition: background 0.2s;
  }
  .rounded-bg:hover {
    background: rgba(255,255,255,0.22);
  }

  .sidebar-icon svg {
    display: block;
  }

  .sidebar-tooltip {
    position: absolute;
    left: 60px;
    top: 50%;
    transform: translateY(-50%);
    background: #fff;
    color: #3D8D7A;
    padding: 4px 12px;
    border-radius: 6px;
    font-size: 14px;
    font-family: 'Inter', sans-serif;
    white-space: nowrap;
    box-shadow: 0 2px 8px rgba(0,0,0,0.08);
    opacity: 0;
    pointer-events: none;
    transition: opacity 0.2s;
    z-index: 10;
  }

  .sidebar-item:hover .sidebar-tooltip {
    opacity: 1;
    pointer-events: auto;
  }

/* Top Navigation Bar (Greenish Theme) */
.top-navbar {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  height: 64px;
  background: linear-gradient(135deg, #3D8D7A, #2d6a5a);
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  z-index: 1000;
  box-shadow: 0 4px 20px rgba(61, 141, 122, 0.3);
}

.navbar-content {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 100%;
  max-width: 1400px;
  margin: 0 auto;
  padding: 0 1.5rem;
}

.navbar-left {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.brand-logo {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  color: white;
  font-weight: 700;
  text-decoration: none;
}

.logo-img {
  width: 36px;
  height: 36px;
  object-fit: contain;
  filter: brightness(0) invert(1);
}

.brand-name {
  font-size: 1.4rem;
  font-weight: 800;
  color: white;
  letter-spacing: -0.5px;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
}

.navbar-center {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  flex: 1;
  justify-content: center;
  max-width: 600px;
}

.navbar-right {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.nav-icon-btn {
  width: 44px;
  height: 44px;
  background: rgba(255, 255, 255, 0.15);
  border: none;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.2s ease;
  color: rgba(255, 255, 255, 0.9);
  position: relative;
}

.nav-icon-btn:hover {
  background: rgba(255, 255, 255, 0.25);
  color: white;
}

.user-profile-wrapper {
  position: relative;
}

.user-profile {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.5rem 0.75rem;
  border-radius: 12px;
  transition: background 0.2s;
  cursor: pointer;
}

.user-profile:hover {
  background: rgba(255, 255, 255, 0.1);
}

.user-avatar {
  width: 36px;
  height: 36px;
  background: rgba(255, 255, 255, 0.2);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
}

.user-name {
  font-size: 0.9rem;
  font-weight: 600;
  color: white;
}

.dropdown-arrow {
  color: rgba(255, 255, 255, 0.8);
  transition: transform 0.2s;
}

.user-profile:hover .dropdown-arrow {
  transform: rotate(180deg);
}

/* Rounded semi-transparent backgrounds for sidebar and navbar icons/buttons */
.rounded-bg {
  background: rgba(255,255,255,0.13);
  border-radius: 16px;
  transition: background 0.2s;
}
.rounded-bg:hover {
  background: rgba(255,255,255,0.22);
}

/* Notification dropdown styles */
.notif-wrapper {
  position: relative;
}

.notification-badge {
  position: absolute;
  top: -2px;
  right: -2px;
  background: #ef4444;
  color: white;
  border-radius: 50%;
  width: 18px;
  height: 18px;
  font-size: 0.75rem;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 2px solid #3D8D7A;
}

.notification-dropdown {
  position: absolute;
  top: 55px;
  right: 0;
  width: 360px;
  max-height: 480px;
  background: white;
  border-radius: 16px;
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15);
  overflow: hidden;
  z-index: 1001;
  border: 1px solid #e2e8f0;
}

.dropdown-header {
  padding: 1.25rem 1.5rem;
  border-bottom: 1px solid #e2e8f0;
  background: #fafafa;
}

.dropdown-header h3 {
  font-size: 1.1rem;
  font-weight: 600;
  color: #1e293b;
}

.notification-list {
  max-height: 400px;
  overflow-y: auto;
}

.no-notifications {
  padding: 3rem 1.5rem;
  text-align: center;
  color: #94a3b8;
  font-size: 0.9rem;
}

.notification-item {
  padding: 1rem 1.5rem;
  border-bottom: 1px solid #f1f5f9;
  transition: background 0.2s;
  cursor: pointer;
}

.notification-item:hover {
  background: #f8fafc;
}

.notification-item:last-child {
  border-bottom: none;
}

.notif-content h4 {
  font-size: 0.9rem;
  font-weight: 600;
  color: #1e293b;
  margin-bottom: 0.25rem;
}

.notif-content p {
  font-size: 0.8rem;
  color: #64748b;
  margin-bottom: 0.5rem;
}

.notif-time {
  font-size: 0.75rem;
  color: #94a3b8;
}

.profile-dropdown {
  position: absolute;
  top: 55px;
  right: 0;
  width: 280px;
  background: white;
  border-radius: 16px;
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15);
  overflow: hidden;
  z-index: 1001;
  border: 1px solid #e2e8f0;
}

.profile-dropdown .dropdown-header {
  padding: 1.5rem;
  background: linear-gradient(135deg, #3D8D7A, #2d6a5a);
  color: white;
}

.profile-info {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.profile-avatar {
  width: 48px;
  height: 48px;
  background: rgba(255, 255, 255, 0.2);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
}

.profile-details h4 {
  font-size: 1rem;
  font-weight: 600;
  margin-bottom: 0.25rem;
}

.profile-details p {
  font-size: 0.85rem;
  opacity: 0.9;
}

.dropdown-menu {
  padding: 0.5rem;
}

.dropdown-item {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.75rem 1rem;
  border-radius: 8px;
  text-decoration: none;
  color: #1e293b;
  font-size: 0.9rem;
  font-weight: 500;
  transition: all 0.2s;
  cursor: pointer;
  border: none;
  background: none;
  width: 100%;
}

.dropdown-item:hover {
  background: #f1f5f9;
  color: #3D8D7A;
}

.dropdown-item svg {
  color: #64748b;
  transition: color 0.2s;
}

.dropdown-item:hover svg {
  color: #3D8D7A;
}

.dropdown-divider {
  height: 1px;
  background: #e2e8f0;
  margin: 0.5rem 0;
}

.logout-btn {
  color: #ef4444 !important;
}

.logout-btn:hover {
  background: #fef2f2 !important;
  color: #dc2626 !important;
}

.logout-btn svg {
  color: #ef4444 !important;
}

.logout-btn:hover svg {
  color: #dc2626 !important;
}

/* Sidebar Navigation */
.sidebar {
  position: fixed;
  top: 64px;
  left: 0;
  width: 80px;
  height: calc(100vh - 64px);
  background: #3D8D7A;
  border-right: none;
  z-index: 900;
  box-shadow: 2px 0 10px rgba(0, 0, 0, 0.05);
  overflow: visible;
}

.sidebar-nav {
  padding: 2rem 0.5rem 1rem 0.5rem;
}

.sidebar-item {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 56px;
  width: 56px;
  margin: 8px 0;
  border-radius: 12px;
  transition: background 0.2s, box-shadow 0.2s;
  cursor: pointer;
  position: relative;
}

.sidebar-item:hover {
  background: rgba(255,255,255,0.22);
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
}

.sidebar-item.active {
  background: rgba(255,255,255,0.15);
  border: 2px solid #fff;
}

.rounded-bg {
  background: rgba(255,255,255,0.13);
  border-radius: 16px;
  transition: background 0.2s;
}
.rounded-bg:hover {
  background: rgba(255,255,255,0.22);
}
.sidebar-icon svg {
  display: block;
}

.sidebar-tooltip {
  position: absolute;
  left: 60px;
  top: 50%;
  transform: translateY(-50%);
  background: #fff;
  color: #3D8D7A;
  padding: 4px 12px;
  border-radius: 6px;
  font-size: 14px;
  font-family: Inter, sans-serif;
  white-space: nowrap;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.2s;
  z-index: 10;
}

.sidebar-item:hover .sidebar-tooltip {
  opacity: 1;
  pointer-events: auto;
}
  .export-btn {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    background: rgba(255, 255, 255, 0.15);
    color: white;
    border: 1px solid rgba(255, 255, 255, 0.2);
    padding: 0.75rem 1.25rem;
    border-radius: 8px;
    font-size: 0.875rem;
    font-weight: 500;
    cursor: pointer;
    transition: all 0.2s;
  }

  .export-btn:hover {
    background: rgba(255, 255, 255, 0.25);
    border-color: rgba(255, 255, 255, 0.3);
    transform: translateY(-1px);
  }

  .export-btn:disabled {
    opacity: 0.5;
    cursor: not-allowed;
    transform: none;
  }

  /* Main Content */
  .main-content {
  flex: 1;
  display: flex;
  flex-direction: column;
  position: relative;
  width: calc(100% - 80px);
  margin-left: 80px;
  margin-top: 64px;
  padding: 32px 40px 40px 40px;
  min-height: calc(100vh - 64px);
  max-height: calc(100vh - 64px);
  overflow-y: auto;
  overflow-x: hidden;
  scroll-behavior: smooth;
  background: #f8fafc;
  padding-bottom: 2rem;
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

  /* Page Header */
  .page-header {
    background: white;
    border-radius: 16px;
    padding: 1.5rem 2rem;
    margin-bottom: 1.5rem;
    border: 1px solid #e2e8f0;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
  }

  .header-content {
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 1rem;
  }

  .header-left {
    display: flex;
    align-items: center;
    gap: 1rem;
  }

  .header-icon {
    width: 56px;
    height: 56px;
    background: linear-gradient(135deg, #3D8D7A, #2d6a5a);
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
  }

  .header-title {
    font-size: 1.75rem;
    font-weight: 700;
    color: #1e293b;
    margin-bottom: 0.25rem;
  }

  .header-subtitle {
    font-size: 0.95rem;
    color: #64748b;
  }

  /* Base Container */
  .home-container {
    min-height: 100vh;
    background: #FBFFE4;
    font-family: 'Inter', sans-serif;
    padding: 1.5rem;
    max-width: 1200px;
    margin: 0 auto;
  }

  .dark .home-container {
    background: #181c20;
  }

  /* Uniform Header Section */
  .header-card {
    background: white;
    border-radius: 16px;
    padding: 1.5rem 2.5rem;
    margin-bottom: 1.5rem;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
    border: 2px solid #A3D1C6;
    width: 100%;
  }

  .dark .header-card {
    background: #23272b;
    border: 2px solid #20c997;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.3);
  }

  .header-content {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .header-left {
    display: flex;
    align-items: center;
    gap: 1rem;
  }

  .user-icon {
    width: 60px;
    height: 60px;
    background: linear-gradient(135deg, #20c997, #17a085);
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    flex-shrink: 0;
  }

.header-title {
  font-size: 1.5rem;
  font-weight: 800;
  color: #1f2937;
  margin-bottom: 0.25rem;
}

  .dark .header-title {
    color: #e2e8f0;
  }

  .header-subtitle {
    font-size: 0.875rem;
    color: #6b7280;
  }

  .dark .header-subtitle {
    color: #a0aec0;
  }

  /* Content Grid */
  .content-grid {
    display: grid;
    gap: 1.5rem;
    grid-template-columns: 1fr;
  }

  .content-card {
    background: white;
    border-radius: 20px;
    padding: 0;
    box-shadow: 0 4px 20px rgba(32, 201, 151, 0.08);
    border: 2px solid rgba(163, 209, 198, 0.3);
    transition: all 0.3s ease;
    margin-bottom: 32px;
    overflow: hidden;
  }

  .dark .content-card {
    background: #23272b;
    border-color: rgba(32, 201, 151, 0.3);
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
  }

  .content-card:hover {
    box-shadow: 0 8px 25px rgba(32, 201, 151, 0.15);
    border-color: rgba(32, 201, 151, 0.6);
    transform: translateY(-2px);
  }

  .dark .content-card:hover {
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.5);
    border-color: rgba(32, 201, 151, 0.6);
  }

  .section-header-left {
    display: flex;
    align-items: center;
    gap: 1rem;
  }

  .section-header-icon {
    width: 56px;
    height: 56px;
    background: linear-gradient(135deg, #A3D1C6 0%, #87C5B8 100%);
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    box-shadow: 0 4px 12px rgba(163, 209, 198, 0.3);
  }
  .dark .section-header-icon {
    background: linear-gradient(135deg, #20c997 0%, #17a085 100%);
  }

  .section-header-title {
    font-size: 1.5rem;
    font-weight: 500;
    color: #2c3e50;
    margin-bottom: 0.25rem;
  }
  .dark .section-header-title {
    color: #ffffff;
  }

  .section-header-sub {
    font-size: 1rem;
    color: #6c757d;
    font-weight: 400;
  }
  .dark .section-header-sub {
    color: #adb5bd;
  }

  /* Header Card */
  .header-card {
    background: white;
    border-radius: 20px;
    padding: 2rem;
    margin-bottom: 2rem;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
  }

  .dark .header-card {
    background: #2a2d33;
  }

  .header-content {
    display: flex;
    align-items: center;
    gap: 1rem;
  }

  .header-left {
    display: flex;
    align-items: center;
    gap: 1rem;
  }

  .user-icon {
    background: #B3D8A8;
    color: #3D8D7A;
    padding: 0.75rem;
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .dark .user-icon {
    background: #3D8D7A;
    color: #B3D8A8;
  }

  .header-title {
    font-size: 1.75rem;
    font-weight: 700;
    color: #3D8D7A;
    margin: 0;
  }

  .dark .header-title {
    color: #B3D8A8;
  }

  .header-subtitle {
    color: #6b7280;
    margin: 0;
    font-size: 0.95rem;
  }

  .dark .header-subtitle {
    color: #9ca3af;
  }

  /* Cards */
  .card {
    background: white;
    border-radius: 20px;
    margin-bottom: 2rem;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
    overflow: hidden;
  }

  .dark .card {
    background: #2a2d33;
  }

  /* Enhanced Card Headers */
  .card-header {
    padding: 1.25rem 1.5rem 1rem 1.5rem;
    border-bottom: 2px solid rgba(163, 209, 198, 0.15);
    margin-bottom: 0;
    background: linear-gradient(135deg, rgba(32, 201, 151, 0.05), rgba(163, 209, 198, 0.05));
  }

  .dark .card-header {
    border-bottom: 2px solid rgba(32, 201, 151, 0.2);
    background: linear-gradient(135deg, rgba(32, 201, 151, 0.08), rgba(163, 209, 198, 0.08));
  }

  .card-title-wrapper {
    display: flex;
    align-items: center;
    gap: 0.75rem;
  }

  .card-icon {
    width: 48px;
    height: 48px;
    background: #3D8D7A;
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #fff;
    flex-shrink: 0;
    box-shadow: 0 2px 8px rgba(61, 141, 122, 0.08);
  }

  .card-header h2 {
    margin: 0 0 0.25rem 0;
    font-size: 1.3rem;
    font-weight: 700;
    color: #2d3748;
    background: linear-gradient(135deg, #20c997, #17a085);
    background-clip: text;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }

  .dark .card-header h2 {
    color: #e2e8f0;
    background: linear-gradient(135deg, #20c997, #17a085);
    background-clip: text;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }

  .card-header p {
    margin: 0;
    font-size: 0.85rem;
    color: #718096;
    font-weight: 500;
  }

  .dark .card-header p {
    color: #a0aec0;
  }

  .card-body {
    padding: 1.5rem;
  }

  /* Enhanced Forms */
  .form-row {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1.5rem;
    margin-bottom: 1rem;
  }

  .form-group {
    margin-bottom: 1.5rem;
  }

  .form-group label {
    display: block;
    margin-bottom: 0.5rem;
    font-weight: 600;
    font-size: 0.9rem;
    color: #4a5568;
    position: relative;
  }

  .dark .form-group label {
    color: #e2e8f0;
  }

  .form-control {
    width: 100%;
    padding: 0.75rem 1rem;
    border: 2px solid rgba(163, 209, 198, 0.3);
    border-radius: 12px;
    font-size: 0.9rem;
    background: rgba(255, 255, 255, 0.8);
    color: #2d3748;
    transition: all 0.3s ease;
    backdrop-filter: blur(10px);
    box-shadow: 0 2px 6px rgba(32, 201, 151, 0.05);
  }

  .dark .form-control {
    border-color: rgba(32, 201, 151, 0.3);
    background: rgba(45, 55, 72, 0.8);
    color: #e2e8f0;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  }

  .form-control:focus {
    border-color: #20c997;
    box-shadow: 0 0 0 4px rgba(32, 201, 151, 0.15);
    outline: none;
    transform: translateY(-1px);
  }

  .dark .form-control:focus {
    border-color: #20c997;
    box-shadow: 0 0 0 4px rgba(32, 201, 151, 0.15);
  }

  /* Enhanced Upload Areas */
  .file-upload-area {
    border: 3px dashed rgba(32, 201, 151, 0.4);
    border-radius: 16px;
    padding: 2rem 1.5rem;
    text-align: center;
    background: linear-gradient(135deg, rgba(32, 201, 151, 0.05), rgba(163, 209, 198, 0.05));
    transition: all 0.4s ease;
    cursor: pointer;
    margin: 1.5rem 0;
    position: relative;
    overflow: hidden;
  }

  .file-upload-area::before {
    content: '';
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: radial-gradient(circle, rgba(32, 201, 151, 0.1) 0%, transparent 50%);
    opacity: 0;
    transition: opacity 0.4s ease;
  }

  .dark .file-upload-area {
    border-color: rgba(32, 201, 151, 0.5);
    background: linear-gradient(135deg, rgba(32, 201, 151, 0.08), rgba(163, 209, 198, 0.08));
  }

  .file-upload-area:hover, 
  .file-upload-area.drag-over {
    border-color: #20c997;
    background: linear-gradient(135deg, rgba(32, 201, 151, 0.12), rgba(163, 209, 198, 0.12));
    transform: translateY(-4px);
    box-shadow: 0 8px 25px rgba(32, 201, 151, 0.25);
  }

  .file-upload-area:hover::before,
  .file-upload-area.drag-over::before {
    opacity: 1;
  }

  .dark .file-upload-area:hover, 
  .dark .file-upload-area.drag-over {
    border-color: #20c997;
    background: linear-gradient(135deg, rgba(32, 201, 151, 0.15), rgba(163, 209, 198, 0.15));
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.4);
  }

  .upload-content {
    position: relative;
    z-index: 1;
  }

  .file-input { 
    display: none; 
  }

  .upload-icon { 
    color: #20c997; 
    margin-bottom: 1rem;
    filter: drop-shadow(0 3px 6px rgba(32, 201, 151, 0.3));
    animation: float 3s ease-in-out infinite;
  }

  @keyframes float {
    0%, 100% { transform: translateY(0px); }
    50% { transform: translateY(-10px); }
  }

  .dark .upload-icon {
    color: #20c997;
  }

  .upload-link { 
    color: #20c997; 
    font-weight: 700;
    text-decoration: underline;
    text-decoration-color: transparent;
    transition: text-decoration-color 0.3s ease;
  }

  .upload-link:hover {
    text-decoration-color: #20c997;
  }

  .dark .upload-link {
    color: #20c997;
  }

  .file-selected { 
    color: #20c997; 
    font-weight: 600;
    background: rgba(32, 201, 151, 0.1);
    padding: 0.75rem;
    border-radius: 10px;
    display: inline-block;
    margin-top: 0.75rem;
  }

  .dark .file-selected {
    color: #20c997;
    background: rgba(32, 201, 151, 0.15);
  }

  /* Template Guide */
  .template-guide {
    margin-top: 1.5rem;
    padding: 1rem;
    border-left: 4px solid #87CBB9;
    background: rgba(135,203,185,0.1);
    border-radius: 8px;
  }
  .format-example pre {
    margin: 0;
    padding: 1rem;
    background: white;
    border-radius: 6px;
    border: 1px solid #E0E7EE;
    font-family: monospace;
    font-size: 0.85rem;
    color: #555;
  }

  /* Preview */
  .preview-meta {
    display: flex;
    align-items: center;
    gap: 1rem;
    margin-bottom: 1rem;
  }
  .badge {
    background: #B3D8A8;
    color: #2c3e50;
    padding: 0.3rem 0.8rem;
    border-radius: 20px;
    font-size: 0.8rem;
    font-weight: 600;
  }
  .preview-text {
    background: #F7F9F7;
    padding: 1rem;
    border-radius: 8px;
    border: 1px solid #E0E7EE;
    max-height: 250px;
    overflow-y: auto;
  }

  /* Enhanced Buttons */
  .action-buttons {
    display: flex;
    gap: 1rem;
    justify-content: flex-end;
    margin: 1.5rem 0 0 0;
    padding: 1.5rem 1.5rem;
    border-top: 2px solid rgba(163, 209, 198, 0.15);
    background: linear-gradient(135deg, rgba(32, 201, 151, 0.02), rgba(163, 209, 198, 0.02));
  }

  .dark .action-buttons {
    border-top: 2px solid rgba(32, 201, 151, 0.2);
    background: linear-gradient(135deg, rgba(32, 201, 151, 0.05), rgba(163, 209, 198, 0.05));
  }

  .btn-submit, 
  .btn-secondary, 
  .btn-primary {
    padding: 0.75rem 1.5rem;
    border-radius: 12px;
    font-weight: 700;
    font-size: 0.9rem;
    border: none;
    cursor: pointer;
    transition: all 0.3s ease;
    display: flex;
    align-items: center;
    gap: 0.5rem;
    position: relative;
    overflow: hidden;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }

  .btn-submit,
  .btn-primary {
    background: linear-gradient(135deg, #20c997, #17a085);
    color: white;
    box-shadow: 0 4px 15px rgba(32, 201, 151, 0.3);
  }

  .btn-submit::before,
  .btn-primary::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.3), transparent);
    transition: left 0.6s ease;
  }

  .btn-submit:hover:not(:disabled),
  .btn-primary:hover:not(:disabled) {
    background: linear-gradient(135deg, #17a085, #138f75);
    box-shadow: 0 8px 25px rgba(32, 201, 151, 0.4);
    transform: translateY(-3px);
  }

  .btn-submit:hover::before,
  .btn-primary:hover::before {
    left: 100%;
  }

  .btn-submit:disabled,
  .btn-primary:disabled {
    background: #cbd5e0;
    cursor: not-allowed;
    box-shadow: none;
    transform: none;
    opacity: 0.6;
  }

  .btn-secondary {
    background: white;
    color: #4a5568;
    border: 2px solid rgba(163, 209, 198, 0.4);
    box-shadow: 0 4px 15px rgba(163, 209, 198, 0.2);
  }

  .btn-secondary:hover { 
    background: rgba(32, 201, 151, 0.05);
    border-color: #20c997;
    transform: translateY(-3px);
    box-shadow: 0 8px 25px rgba(163, 209, 198, 0.3);
  }

  .dark .btn-secondary {
    background: #2d3748;
    color: #e2e8f0;
    border: 2px solid rgba(32, 201, 151, 0.3);
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
  }

  .dark .btn-secondary:hover {
    background: rgba(32, 201, 151, 0.1);
    border-color: #20c997;
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.4);
  }

  /* Error */
  .error-message {
    background: #fff5f5;
    color: #c53030;
    padding: 1.5rem;
    border-radius: 12px;
    border: 1px solid #fed7d7;
    margin-bottom: 1.5rem;
    box-shadow: 0 4px 12px rgba(239, 68, 68, 0.1);
  }

  .error-content {
    margin-bottom: 1rem;
  }

  .error-text {
    white-space: pre-wrap;
    font-family: inherit;
    margin: 0.5rem 0 0 0;
    font-size: 0.95rem;
    line-height: 1.5;
  }

  .error-suggestions {
    border-top: 1px solid rgba(239, 68, 68, 0.2);
    padding-top: 1rem;
  }

  .error-suggestions h4 {
    margin: 0 0 1rem 0;
    color: #2d3748;
    font-size: 1rem;
    font-weight: 600;
  }

  .suggestion-buttons {
    display: flex;
    gap: 0.75rem;
    flex-wrap: wrap;
  }

  .suggestion-btn {
    padding: 0.75rem 1rem;
    background: linear-gradient(135deg, #3D8D7A, #4CAF50);
    color: white;
    border: none;
    border-radius: 8px;
    font-size: 0.85rem;
    font-weight: 500;
    cursor: pointer;
    transition: all 0.3s ease;
    box-shadow: 0 2px 8px rgba(61, 141, 122, 0.3);
  }

  .suggestion-btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(61, 141, 122, 0.4);
    background: linear-gradient(135deg, #317c6b, #45a049);
  }

  .suggestion-btn:active {
    transform: translateY(0);
  }

  /* Loading Overlay */
  .loading-overlay {
    position: fixed;
    top: 0; 
    left: 0;
    width: 100%; 
    height: 100%;
    background: rgba(251, 255, 228, 0.9);
    backdrop-filter: blur(6px);
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    z-index: 1000;
  }

  .dark .loading-overlay {
    background: rgba(24, 28, 32, 0.9);
  }

  .loader {
    width: 50px; 
    height: 50px;
    border: 5px solid #B3D8A8;
    border-top: 5px solid #3D8D7A;
    border-radius: 50%;
    animation: spin 1s linear infinite;
    margin-bottom: 1rem;
  }

  .dark .loader {
    border: 5px solid #3D8D7A;
    border-top: 5px solid #B3D8A8;
  }

  @keyframes spin { 
    to { transform: rotate(360deg); } 
  }

  /* Processing Steps */
  .processing-steps {
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
    margin-top: 1rem;
    padding: 1rem;
    background: white;
    border-radius: 12px;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
  }

  .dark .processing-steps {
    background: #2a2d33;
  }

  .processing-step {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    padding: 0.75rem;
    border-radius: 8px;
    background: #f8f9fa;
  }

  .dark .processing-step {
    background: #1a1e23;
  }

  .processing-step.active {
    background: rgba(61, 141, 122, 0.1);
    border-left: 4px solid #3D8D7A;
  }

  .dark .processing-step.active {
    background: rgba(179, 216, 168, 0.1);
    border-left: 4px solid #B3D8A8;
  }

  .processing-step.completed {
    background: rgba(179, 216, 168, 0.2);
    color: #3D8D7A;
  }

  .dark .processing-step.completed {
    background: rgba(61, 141, 122, 0.2);
    color: #B3D8A8;
  }

  .step-icon .icon-completed {
    color: #3D8D7A;
    font-weight: bold;
  }

  .dark .step-icon .icon-completed {
    color: #B3D8A8;
  }

  .step-icon .icon-active {
    color: #3D8D7A;
    animation: rotate 1s linear infinite;
  }

  .dark .step-icon .icon-active {
    color: #B3D8A8;
  }

  @keyframes rotate {
    to { transform: rotate(360deg); }
  }

  .step-icon .icon-pending {
    color: #6b7280;
  }

  .step-text {
    color: #333;
    font-size: 0.9rem;
  }

  .dark .step-text {
    color: #e1e5e9;
  }

  /* Answer Key Tabs */
  .answer-key-tabs {
    display: flex;
    gap: 0.5rem;
    margin-bottom: 1.5rem;
  }

  .tab-button {
    padding: 0.75rem 1.5rem;
    border: 2px solid #E0E7EE;
    background: rgba(255, 255, 255, 0.8);
    color: #666;
    border-radius: 10px;
    cursor: pointer;
    font-weight: 500;
    transition: all 0.3s ease;
  }

  .tab-button.active {
    border-color: #3D8D7A;
    background: #3D8D7A;
    color: white;
  }

  .tab-button:hover:not(.active) {
    border-color: #87CBB9;
    background: rgba(135, 203, 185, 0.1);
  }

  /* Answer Key Section */
  .answer-key-section {
    margin-top: 1rem;
  }

  .manual-answers-container {
    background: rgba(250, 252, 254, 0.8);
    border: 1px solid #E0E7EE;
    border-radius: 12px;
    padding: 1.5rem;
  }

  .questions-list {
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }

  .question-item-input {
    background: white;
    border: 1px solid #E0E7EE;
    border-radius: 10px;
    padding: 1rem;
    transition: all 0.3s ease;
  }

  .question-item-input:hover {
    border-color: #3D8D7A;
    box-shadow: 0 2px 8px rgba(61, 141, 122, 0.1);
  }

  .question-header {
    display: flex;
    align-items: center;
    gap: 1rem;
    margin-bottom: 1rem;
  }

  .question-number {
    background: #3D8D7A;
    color: white;
    padding: 0.5rem 0.75rem;
    border-radius: 6px;
    font-weight: 600;
    min-width: 60px;
    text-align: center;
  }

  .question-type-select {
    padding: 0.5rem;
    border: 1px solid #E0E7EE;
    border-radius: 6px;
    background: white;
    font-size: 0.9rem;
  }

  .answer-options {
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
  }

  .answer-options label {
    font-weight: 500;
    color: #555;
  }

  .no-questions-message {
    text-align: center;
    padding: 2rem;
    color: #666;
    font-style: italic;
  }

  /* Answer Key Preview */
  .answer-key-preview {
    margin-top: 1.5rem;
    padding: 1rem;
    background: rgba(179, 216, 168, 0.1);
    border: 1px solid rgba(179, 216, 168, 0.3);
    border-radius: 10px;
  }

  .answer-key-preview h4 {
    margin-bottom: 1rem;
    color: #333;
    font-size: 1.1rem;
  }

  .preview-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(120px, 1fr));
    gap: 0.75rem;
  }

  .answer-preview-item {
    background: white;
    border: 1px solid #E0E7EE;
    border-radius: 8px;
    padding: 0.75rem;
    text-align: center;
    display: flex;
    flex-direction: column;
    gap: 0.25rem;
  }

  .q-num {
    font-weight: 600;
    color: #3D8D7A;
    font-size: 0.9rem;
  }

  .q-answer {
    font-weight: 700;
    font-size: 1.1rem;
    color: #333;
  }

  .q-answer.multiple-choice {
    color: #3b82f6;
  }

  .q-answer.true-false {
    color: #f59e0b;
  }

  .q-type {
    font-size: 0.75rem;
    color: #666;
    text-transform: uppercase;
  }

  /* Detected Questions */
  .detected-questions {
    margin-top: 1.5rem;
    padding: 1.5rem;
    background: rgba(59, 130, 246, 0.05);
    border: 2px solid rgba(59, 130, 246, 0.2);
    border-radius: 12px;
  }

  .detected-questions h4 {
    margin-bottom: 0.5rem;
    color: #1e40af;
    font-size: 1.2rem;
  }

  .detection-note {
    margin-bottom: 1.5rem;
    color: #475569;
    font-style: italic;
  }

  .detected-questions-list {
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
    margin-bottom: 1.5rem;
  }

  .detected-question-item {
    background: white;
    border: 1px solid #E0E7EE;
    border-radius: 10px;
    padding: 1.5rem;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
  }

  .question-content {
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }

  .question-text {
    display: flex;
    gap: 0.75rem;
    align-items: flex-start;
  }

  .q-number {
    background: #3D8D7A;
    color: white;
    padding: 0.25rem 0.75rem;
    border-radius: 6px;
    font-weight: 600;
    flex-shrink: 0;
  }

  .q-text {
    flex: 1;
    line-height: 1.5;
    color: #333;
  }

  .question-options {
    margin-top: 1rem;
  }

  .option-selection label {
    font-weight: 500;
    margin-bottom: 0.75rem;
    display: block;
    color: #555;
  }

  .options-grid {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
  }

  .option-item {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    padding: 0.75rem;
    border: 1px solid #E0E7EE;
    border-radius: 8px;
    cursor: pointer;
    transition: all 0.3s ease;
  }

  .option-item:hover {
    border-color: #3D8D7A;
    background: rgba(61, 141, 122, 0.05);
  }

  .option-item.selected {
    border-color: #3D8D7A;
    background: rgba(61, 141, 122, 0.1);
  }

  .option-item input[type="radio"] {
    margin: 0;
    accent-color: #3D8D7A;
  }

  .option-letter {
    font-weight: 600;
    color: #3D8D7A;
    min-width: 20px;
  }

  .option-text {
    flex: 1;
    color: #333;
  }

  .true-false-selection {
    margin-top: 1rem;
  }

  .true-false-selection label {
    font-weight: 500;
    margin-bottom: 0.75rem;
    display: block;
    color: #555;
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
    border: 1px solid #E0E7EE;
    border-radius: 8px;
    cursor: pointer;
    transition: all 0.3s ease;
    background: white;
  }

  .tf-option:hover {
    border-color: #3D8D7A;
    background: rgba(61, 141, 122, 0.05);
  }

  .tf-option.selected {
    border-color: #3D8D7A;
    background: rgba(61, 141, 122, 0.1);
  }

  .tf-option input[type="radio"] {
    margin: 0;
    accent-color: #3D8D7A;
  }

  .tf-option span {
    font-weight: 500;
    color: #333;
  }

  .answer-key-actions {
    display: flex;
    gap: 1rem;
    justify-content: center;
    padding-top: 1.5rem;
    border-top: 1px solid rgba(0, 0, 0, 0.1);
  }

  .dark .answer-key-actions {
    border-top: 1px solid rgba(179, 216, 168, 0.1);
  }

  .calculated-total {
    display: block;
    padding: 1rem;
    background: rgba(179, 216, 168, 0.1);
    border: 1px solid rgba(179, 216, 168, 0.3);
    border-radius: 8px;
    text-align: center;
    font-size: 1.1rem;
    color: #333;
  }

  .calculated-total strong {
    color: #3D8D7A;
    font-size: 1.2rem;
  }

  /* Individual Points Section */
  .individual-points-section {
    margin-top: 1.5rem;
    padding: 1.5rem;
    background: rgba(179, 216, 168, 0.1);
    border: 1px solid rgba(179, 216, 168, 0.3);
    border-radius: 10px;
  }

  .points-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 1.5rem;
  }

  .points-header h4 {
    margin: 0;
    color: #333;
    font-size: 1.1rem;
  }

  .quick-assign-buttons {
    display: flex;
    gap: 0.5rem;
  }

  .quick-btn {
    padding: 0.5rem 1rem;
    background: #3D8D7A;
    color: white;
    border: none;
    border-radius: 6px;
    font-size: 0.8rem;
    cursor: pointer;
    transition: all 0.3s ease;
  }

  .quick-btn:hover {
    background: #317c6b;
    transform: translateY(-1px);
  }

  .points-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(140px, 1fr));
    gap: 1rem;
    margin-bottom: 1.5rem;
  }

  .point-assignment-item {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    background: white;
    padding: 0.75rem;
    border-radius: 8px;
    border: 1px solid #E0E7EE;
    transition: all 0.3s ease;
  }

  .point-assignment-item.highlighted {
    border-color: #3D8D7A;
    background: rgba(61, 141, 122, 0.05);
    box-shadow: 0 2px 4px rgba(61, 141, 122, 0.1);
  }

  .point-label {
    font-weight: 600;
    color: #3D8D7A;
    min-width: 30px;
    font-size: 0.9rem;
  }

  .point-input {
    flex: 1;
    padding: 0.25rem 0.5rem;
    border: 1px solid #E0E7EE;
    border-radius: 4px;
    text-align: center;
    font-weight: 600;
  }

  .point-input:focus {
    border-color: #3D8D7A;
    outline: none;
  }

  .point-unit {
    font-size: 0.8rem;
    color: #666;
    font-weight: 500;
  }

  .points-summary {
    background: rgba(255, 255, 255, 0.8);
    padding: 1rem;
    border-radius: 8px;
    border: 1px solid rgba(61, 141, 122, 0.2);
  }

  .points-summary p {
    margin: 0.5rem 0;
    color: #333;
  }

  .dist-item {
    background: #3D8D7A;
    color: white;
    padding: 0.25rem 0.5rem;
    border-radius: 4px;
    font-size: 0.8rem;
    margin-right: 0.5rem;
    display: inline-block;
  }

  /* Processing Steps */
  .processing-steps {
    margin-top: 1.5rem;
    padding: 1rem;
    background: rgba(255, 255, 255, 0.1);
    border-radius: 12px;
    max-width: 400px;
  }

  .processing-step {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    padding: 0.5rem 0;
    color: #666;
    transition: all 0.3s ease;
  }

  .processing-step.active {
    color: #3D8D7A;
    font-weight: 600;
  }

  .processing-step.completed {
    color: #22c55e;
  }

  .step-icon {
    font-size: 1.1rem;
    width: 20px;
    text-align: center;
  }

  /* AI Features */
  .ai-features {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1rem;
    margin-top: 1rem;
  }

  .feature-item {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    padding: 0.75rem;
    background: rgba(179, 216, 168, 0.1);
    border-radius: 8px;
    border: 1px solid rgba(179, 216, 168, 0.3);
  }

  .feature-icon {
    font-size: 1.2rem;
    flex-shrink: 0;
  }

  /* AI Settings Grid */
  .ai-settings-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1.5rem;
    margin-bottom: 2rem;
  }

  .setting-card {
    background: rgba(250, 252, 254, 0.8);
    border: 1px solid #E0E7EE;
    border-radius: 12px;
    padding: 1.5rem;
    transition: all 0.3s ease;
  }

  .setting-card:hover {
    border-color: #3D8D7A;
    box-shadow: 0 4px 12px rgba(61, 141, 122, 0.1);
  }

  .setting-header {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    margin-bottom: 1rem;
  }

  .setting-icon {
    font-size: 1.5rem;
  }

  .setting-header h3 {
    margin: 0;
    font-size: 1.1rem;
    font-weight: 600;
    color: #333;
  }

  /* Checkbox Group */
  .checkbox-group {
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }

  .checkbox-item {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    cursor: pointer;
    padding: 0.75rem;
    border-radius: 8px;
    transition: all 0.3s ease;
  }

  .checkbox-item:hover {
    background: rgba(61, 141, 122, 0.05);
  }

  .checkbox-item input[type="checkbox"] {
    width: 18px;
    height: 18px;
    accent-color: #3D8D7A;
  }

  .checkbox-text {
    font-size: 0.95rem;
    color: #555;
    font-weight: 500;
  }

  /* Form Hints */
  .form-hint {
    font-size: 0.8rem;
    color: var(--gray-500);
    margin-top: 0.25rem;
    font-style: italic;
  }

  /* Results Card */
  .results-card {
    border: 2px solid #22c55e;
    background: linear-gradient(135deg, rgba(34, 197, 94, 0.05) 0%, rgba(179, 216, 168, 0.05) 100%);
  }

  /* Score Overview */
  .score-overview {
    display: flex;
    align-items: center;
    gap: 2rem;
    margin-bottom: 2rem;
    padding: 1.5rem;
    background: rgba(255, 255, 255, 0.6);
    border-radius: 12px;
  }

  .score-circle {
    width: 120px;
    height: 120px;
    border-radius: 50%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    border: 4px solid;
    position: relative;
  }

  .score-circle.excellent { border-color: #22c55e; background: rgba(34, 197, 94, 0.1); }
  .score-circle.good { border-color: #3b82f6; background: rgba(59, 130, 246, 0.1); }
  .score-circle.average { border-color: #f59e0b; background: rgba(245, 158, 11, 0.1); }
  .score-circle.below-average { border-color: #ef4444; background: rgba(239, 68, 68, 0.1); }
  .score-circle.poor { border-color: #dc2626; background: rgba(220, 38, 38, 0.1); }

  .score-value {
    font-size: 2rem;
    font-weight: 700;
    color: #333;
  }

  .score-label {
    font-size: 0.85rem;
    color: #666;
    margin-top: 0.25rem;
  }

  .score-details {
    flex: 1;
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }

  .detail-item {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0.75rem;
    background: rgba(255, 255, 255, 0.8);
    border-radius: 8px;
  }

  .detail-label {
    font-weight: 600;
    color: #555;
  }

  .detail-value {
    font-weight: 700;
    color: #333;
  }

  .grade-letter {
    padding: 0.25rem 0.75rem;
    border-radius: 6px;
    color: white;
    font-weight: 700;
  }

  .grade-letter.grade-a { background: #22c55e; }
  .grade-letter.grade-b { background: #3b82f6; }
  .grade-letter.grade-c { background: #f59e0b; }
  .grade-letter.grade-f { background: #ef4444; }

  /* AI Feedback */
  .ai-feedback {
    margin-bottom: 2rem;
  }

  .ai-feedback h3 {
    color: #333;
    margin-bottom: 1.5rem;
    font-size: 1.25rem;
    font-weight: 700;
  }

  .feedback-section {
    margin-bottom: 1.5rem;
    padding: 1rem;
    background: rgba(255, 255, 255, 0.6);
    border-radius: 10px;
  }

  .feedback-section h4 {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    margin-bottom: 0.75rem;
    font-size: 1.1rem;
    font-weight: 600;
    color: #333;
  }

  .feedback-icon {
    font-size: 1.2rem;
  }

  .feedback-list {
    margin: 0;
    padding-left: 1.5rem;
  }

  .feedback-list li {
    margin-bottom: 0.5rem;
    line-height: 1.5;
  }

  .feedback-list.strengths li {
    color: #166534;
  }

  .feedback-list.weaknesses li {
    color: #dc2626;
  }

  .feedback-list.recommendations li {
    color: #1d4ed8;
  }

  .detailed-analysis {
    padding: 1rem;
    background: rgba(179, 216, 168, 0.1);
    border-radius: 8px;
    border-left: 4px solid #3D8D7A;
  }

  .detailed-analysis h4 {
    margin-bottom: 0.75rem;
    color: #333;
  }

  .detailed-analysis p {
    line-height: 1.6;
    color: #555;
    margin: 0;
  }

  /* Question Breakdown */
  .question-breakdown {
    margin-bottom: 2rem;
  }

  .question-breakdown h3 {
    margin-bottom: 1rem;
    color: #333;
    font-size: 1.25rem;
    font-weight: 700;
  }

  .breakdown-list {
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }

  .question-item {
    padding: 1rem;
    border-radius: 10px;
    border: 2px solid;
    transition: all 0.3s ease;
  }

  .question-item.correct {
    border-color: #22c55e;
    background: rgba(34, 197, 94, 0.05);
  }

  .question-item.incorrect {
    border-color: #ef4444;
    background: rgba(239, 68, 68, 0.05);
  }

  .question-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 0.5rem;
  }

  .question-number {
    font-weight: 700;
    color: #333;
    background: rgba(255, 255, 255, 0.8);
    padding: 0.25rem 0.75rem;
    border-radius: 6px;
  }

  .question-status {
    font-weight: 600;
    flex: 1;
    text-align: center;
  }

  .question-points {
    font-weight: 600;
    color: #666;
  }

  .question-feedback {
    padding-top: 0.5rem;
    border-top: 1px solid rgba(0, 0, 0, 0.1);
  }

  .question-feedback p {
    margin: 0;
    color: #555;
    font-style: italic;
  }

  /* Results Actions */
  .results-actions {
    display: flex;
    gap: 1rem;
    justify-content: center;
    margin-top: 2rem;
    padding-top: 1.5rem;
    border-top: 1px solid rgba(0, 0, 0, 0.1);
  }

  @media (max-width: 768px) {
    .ai-settings-grid {
      grid-template-columns: 1fr;
    }
    
    .score-overview {
      flex-direction: column;
      text-align: center;
    }
    
    .results-actions {
      flex-direction: column;
    }
    
    .question-header {
      flex-direction: column;
      gap: 0.5rem;
      align-items: flex-start;
    }
  }

  /* Processing Steps */
  .processing-steps {
    margin-top: 1.5rem;
    padding: 1rem;
    background: rgba(255, 255, 255, 0.1);
    border-radius: 12px;
    max-width: 400px;
  }

  .processing-step {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    padding: 0.5rem 0;
    color: #666;
    transition: all 0.3s ease;
  }

  .processing-step.active {
    color: #3D8D7A;
    font-weight: 600;
  }

  .processing-step.completed {
    color: #22c55e;
  }

  .step-icon {
    font-size: 1.1rem;
    width: 20px;
    text-align: center;
  }

  /* AI Features */
  .ai-features {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1rem;
    margin-top: 1rem;
  }

  .feature-item {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    padding: 0.75rem;
    background: rgba(179, 216, 168, 0.1);
    border-radius: 8px;
    border: 1px solid rgba(179, 216, 168, 0.3);
  }

  .feature-icon {
    font-size: 1.2rem;
    flex-shrink: 0;
  }

  /* AI Settings Grid */
  .ai-settings-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1.5rem;
    margin-bottom: 2rem;
  }

  .setting-card {
    background: rgba(250, 252, 254, 0.8);
    border: 1px solid #E0E7EE;
    border-radius: 12px;
    padding: 1.5rem;
    transition: all 0.3s ease;
  }

  .setting-card:hover {
    border-color: #3D8D7A;
    box-shadow: 0 4px 12px rgba(61, 141, 122, 0.1);
  }

  .setting-header {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    margin-bottom: 1rem;
  }

  .setting-icon {
    font-size: 1.5rem;
  }

  .setting-header h3 {
    margin: 0;
    font-size: 1.1rem;
    font-weight: 600;
    color: #333;
  }

  /* Checkbox Group */
  .checkbox-group {
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }

  .checkbox-item {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    cursor: pointer;
    padding: 0.75rem;
    border-radius: 8px;
    transition: all 0.3s ease;
  }

  .checkbox-item:hover {
    background: rgba(61, 141, 122, 0.05);
  }

  .checkbox-item input[type="checkbox"] {
    width: 18px;
    height: 18px;
    accent-color: #3D8D7A;
  }

  .checkbox-text {
    font-size: 0.95rem;
    color: #555;
    font-weight: 500;
  }

  /* Form Hints */
  .form-hint {
    font-size: 0.8rem;
    color: var(--gray-500);
    margin-top: 0.25rem;
    font-style: italic;
  }

  /* Results Card */
  .results-card {
    border: 2px solid #22c55e;
    background: linear-gradient(135deg, rgba(34, 197, 94, 0.05) 0%, rgba(179, 216, 168, 0.05) 100%);
  }

  /* Score Overview */
  .score-overview {
    display: flex;
    align-items: center;
    gap: 2rem;
    margin-bottom: 2rem;
    padding: 1.5rem;
    background: rgba(255, 255, 255, 0.6);
    border-radius: 12px;
  }

  .score-circle {
    width: 120px;
    height: 120px;
    border-radius: 50%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    border: 4px solid;
    position: relative;
  }

  .score-circle.excellent { border-color: #22c55e; background: rgba(34, 197, 94, 0.1); }
  .score-circle.good { border-color: #3b82f6; background: rgba(59, 130, 246, 0.1); }
  .score-circle.average { border-color: #f59e0b; background: rgba(245, 158, 11, 0.1); }
  .score-circle.below-average { border-color: #ef4444; background: rgba(239, 68, 68, 0.1); }
  .score-circle.poor { border-color: #dc2626; background: rgba(220, 38, 38, 0.1); }

  .score-value {
    font-size: 2rem;
    font-weight: 700;
    color: #333;
  }

  .score-label {
    font-size: 0.85rem;
    color: #666;
    margin-top: 0.25rem;
  }

  .score-details {
    flex: 1;
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }

  .detail-item {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0.75rem;
    background: rgba(255, 255, 255, 0.8);
    border-radius: 8px;
  }

  .detail-label {
    font-weight: 600;
    color: #555;
  }

  .detail-value {
    font-weight: 700;
    color: #333;
  }

  .grade-letter {
    padding: 0.25rem 0.75rem;
    border-radius: 6px;
    color: white;
    font-weight: 700;
  }

  .grade-letter.grade-a { background: #22c55e; }
  .grade-letter.grade-b { background: #3b82f6; }
  .grade-letter.grade-c { background: #f59e0b; }
  .grade-letter.grade-f { background: #ef4444; }

  /* AI Feedback */
  .ai-feedback {
    margin-bottom: 2rem;
  }

  .ai-feedback h3 {
    color: #333;
    margin-bottom: 1.5rem;
    font-size: 1.25rem;
    font-weight: 700;
  }

  .feedback-section {
    margin-bottom: 1.5rem;
    padding: 1rem;
    background: rgba(255, 255, 255, 0.6);
    border-radius: 10px;
  }

  .feedback-section h4 {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    margin-bottom: 0.75rem;
    font-size: 1.1rem;
    font-weight: 600;
    color: #333;
  }

  .feedback-icon {
    font-size: 1.2rem;
  }

  .feedback-list {
    margin: 0;
    padding-left: 1.5rem;
  }

  .feedback-list li {
    margin-bottom: 0.5rem;
    line-height: 1.5;
  }

  .feedback-list.strengths li {
    color: #166534;
  }

  .feedback-list.weaknesses li {
    color: #dc2626;
  }

  .feedback-list.recommendations li {
    color: #1d4ed8;
  }

  .detailed-analysis {
    padding: 1rem;
    background: rgba(179, 216, 168, 0.1);
    border-radius: 8px;
    border-left: 4px solid #3D8D7A;
  }

  .detailed-analysis h4 {
    margin-bottom: 0.75rem;
    color: #333;
  }

  .detailed-analysis p {
    line-height: 1.6;
    color: #555;
    margin: 0;
  }

  /* Question Breakdown */
  .question-breakdown {
    margin-bottom: 2rem;
  }

  .question-breakdown h3 {
    margin-bottom: 1rem;
    color: #333;
    font-size: 1.25rem;
    font-weight: 700;
  }

  .breakdown-list {
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }

  .question-item {
    padding: 1rem;
    border-radius: 10px;
    border: 2px solid;
    transition: all 0.3s ease;
  }

  .question-item.correct {
    border-color: #22c55e;
    background: rgba(34, 197, 94, 0.05);
  }

  .question-item.incorrect {
    border-color: #ef4444;
    background: rgba(239, 68, 68, 0.05);
  }

  .question-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 0.5rem;
  }

  .question-number {
    font-weight: 700;
    color: #333;
    background: rgba(255, 255, 255, 0.8);
    padding: 0.25rem 0.75rem;
    border-radius: 6px;
  }

  .question-status {
    font-weight: 600;
    flex: 1;
    text-align: center;
  }

  .question-points {
    font-weight: 600;
    color: #666;
  }

  .question-feedback {
    padding-top: 0.5rem;
    border-top: 1px solid rgba(0, 0, 0, 0.1);
  }

  .question-feedback p {
    margin: 0;
    color: #555;
    font-style: italic;
  }

  /* Results Actions */
  .results-actions {
    display: flex;
    gap: 1rem;
    justify-content: center;
    margin-top: 2rem;
    padding-top: 1.5rem;
    border-top: 1px solid rgba(0, 0, 0, 0.1);
  }

  @media (max-width: 768px) {
    .ai-settings-grid {
      grid-template-columns: 1fr;
    }
    
    .score-overview {
      flex-direction: column;
      text-align: center;
    }
    
    .results-actions {
      flex-direction: column;
    }
    
    .question-header {
      flex-direction: column;
      gap: 0.5rem;
      align-items: flex-start;
    }
  }

  /* Manual Input Tabs */
  .manual-input-tabs {
    display: flex;
    gap: 0.5rem;
    margin-bottom: 1.5rem;
  }

  .input-tab {
    padding: 0.5rem 1rem;
    border: 1px solid #E0E7EE;
    background: rgba(255, 255, 255, 0.8);
    color: #666;
    border-radius: 8px;
    cursor: pointer;
    font-weight: 500;
    font-size: 0.9rem;
    transition: all 0.3s ease;
  }

  .input-tab.active {
    border-color: #3D8D7A;
    background: #3D8D7A;
    color: white;
  }

  .input-tab:hover:not(.active) {
    border-color: #87CBB9;
    background: rgba(135, 203, 185, 0.1);
  }

  /* Bulk Input Container */
  .bulk-input-container {
    background: rgba(250, 252, 254, 0.8);
    border: 1px solid #E0E7EE;
    border-radius: 12px;
    padding: 1.5rem;
  }

  .bulk-input-header h4 {
    margin: 0 0 0.5rem 0;
    color: #333;
    font-size: 1.1rem;
  }

  .bulk-input-header p {
    margin: 0 0 1rem 0;
    color: #666;
    font-size: 0.9rem;
  }

  .format-examples {
    background: rgba(255, 255, 255, 0.8);
    border: 1px solid #E0E7EE;
    border-radius: 8px;
    padding: 1rem;
    margin-bottom: 1rem;
  }

  .example-tabs {
    display: flex;
    gap: 0.5rem;
    margin-bottom: 1rem;
    flex-wrap: wrap;
  }

  .example-tab {
    padding: 0.4rem 0.8rem;
    border: 1px solid #E0E7EE;
    background: white;
    color: #666;
    border-radius: 6px;
    cursor: pointer;
    font-size: 0.8rem;
    transition: all 0.3s ease;
  }

  .example-tab.active {
    border-color: #3D8D7A;
    background: #3D8D7A;
    color: white;
  }

  .example-content {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
  }

  .example-code {
    background: #f8f9fa;
    border: 1px solid #e9ecef;
    border-radius: 4px;
    padding: 0.75rem;
    font-family: 'Monaco', 'Consolas', monospace;
    font-size: 0.8rem;
    color: #333;
    white-space: pre-wrap;
    margin: 0;
  }

  .load-example-btn {
    align-self: flex-start;
    padding: 0.4rem 0.8rem;
    background: #87CBB9;
    color: white;
    border: none;
    border-radius: 4px;
    font-size: 0.8rem;
    cursor: pointer;
    transition: all 0.3s ease;
  }

  .load-example-btn:hover {
    background: #3D8D7A;
    transform: translateY(-1px);
  }

  .bulk-input-textarea {
    width: 100%;
    padding: 1rem;
    border: 1px solid #E0E7EE;
    border-radius: 8px;
    font-family: 'Monaco', 'Consolas', monospace;
    font-size: 0.9rem;
    line-height: 1.4;
    resize: vertical;
    min-height: 300px;
    background: white;
    transition: border-color 0.3s ease;
  }

  .bulk-input-textarea:focus {
    border-color: #3D8D7A;
    outline: none;
    box-shadow: 0 0 0 3px rgba(61, 141, 122, 0.15);
  }

  .bulk-preview {
    margin-top: 1.5rem;
    padding: 1rem;
    background: rgba(179, 216, 168, 0.1);
    border: 1px solid rgba(179, 216, 168, 0.3);
    border-radius: 8px;
  }

  .bulk-preview h4 {
    margin: 0 0 1rem 0;
    color: #333;
    font-size: 1rem;
  }

  .bulk-preview-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(100px, 1fr));
    gap: 0.75rem;
    margin-bottom: 1rem;
  }

  .bulk-preview-item {
    background: white;
    border: 1px solid #E0E7EE;
    border-radius: 6px;
    padding: 0.5rem;
    text-align: center;
    display: flex;
    flex-direction: column;
    gap: 0.25rem;
    transition: all 0.3s ease;
  }

  .bulk-preview-item:hover {
    border-color: #3D8D7A;
    box-shadow: 0 2px 4px rgba(61, 141, 122, 0.1);
  }

  .bulk-preview-item.multiple-choice {
    border-left: 3px solid #3b82f6;
  }

  .bulk-preview-item.true-false {
    border-left: 3px solid #f59e0b;
  }

  .preview-q-num {
    font-weight: 600;
    color: #3D8D7A;
    font-size: 0.8rem;
  }

  .preview-answer {
    font-weight: 700;
    font-size: 1rem;
    color: #333;
  }

  .preview-type {
    font-size: 0.7rem;
    color: #666;
    text-transform: uppercase;
  }

  .apply-bulk-btn {
    background: #3D8D7A;
    color: white;
    padding: 0.75rem 1.5rem;
    border: none;
    border-radius: 8px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
    box-shadow: 0 4px 12px rgba(61, 141, 122, 0.3);
  }

  .apply-bulk-btn:hover {
    background: #317c6b;
    transform: translateY(-2px);
  }

  /* Responsive Design */
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
    .ai-settings-grid {
      grid-template-columns: 1fr;
    }
    
    .score-overview {
      flex-direction: column;
      text-align: center;
    }
    
    .results-actions {
      flex-direction: column;
    }
    
    .question-header {
      flex-direction: column;
      gap: 0.5rem;
      align-items: flex-start;
    }
    
    .main-content {
      padding: 1rem;
    }
    
    .page-header {
      padding: 1rem;
      margin-bottom: 1.5rem;
    }
    
    .header-content {
      flex-direction: column;
      align-items: stretch;
      gap: 1rem;
    }
    
    .navbar-content {
      padding: 0 0.5rem;
    }
    
    .brand-name {
      display: none;
    }
  }

  /* Logout Modal Styles */
  .modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(0, 0, 0, 0.5);
    backdrop-filter: blur(5px);
    z-index: 1000;
    display: flex;
    align-items: center;
    justify-content: center;
    animation: fadeIn 0.3s ease;
  }

  .logout-modal {
    max-width: 400px;
    border-radius: 16px;
    overflow: hidden;
    background: white;
    border: 2px solid #3D8D7A;
    animation: modalSlideIn 0.3s ease-out;
  }

  @keyframes modalSlideIn {
    from {
      opacity: 0;
      transform: translateY(-20px) scale(0.95);
    }
    to {
      opacity: 1;
      transform: translateY(0) scale(1);
    }
  }

  .logout-header {
    background: linear-gradient(135deg, #3D8D7A, #2d6a5a);
    color: white;
    padding: 1.5rem;
  }

  .logout-header h3 {
    font-size: 1.2rem;
    font-weight: 600;
    margin: 0;
  }

  .modal-body {
    padding: 2rem;
    text-align: center;
  }

  .logout-icon {
    display: flex;
    justify-content: center;
    margin-bottom: 1rem;
  }

  .logout-icon svg {
    color: #3D8D7A;
    animation: pulse 2s infinite;
  }

  @keyframes pulse {
    0%, 100% { transform: scale(1); }
    50% { transform: scale(1.05); }
  }

  .logout-message {
    font-size: 1rem;
    font-weight: 600;
    color: #1e293b;
    margin-bottom: 0.5rem;
  }

  .logout-submessage {
    font-size: 0.85rem;
    color: #64748b;
    margin-bottom: 0;
  }

  .logout-footer {
    display: flex;
    gap: 0.75rem;
    padding: 1.5rem 2rem;
    background: #f8fafc;
  }

  .btn-cancel {
    flex: 1;
    padding: 0.75rem 1rem;
    background: #f1f5f9;
    color: #64748b;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    font-size: 0.9rem;
    font-weight: 500;
    cursor: pointer;
    transition: all 0.2s;
  }

  .btn-cancel:hover {
    background: #e2e8f0;
    color: #1e293b;
  }

  .btn-logout {
    flex: 1;
    padding: 0.75rem 1rem;
    background: #ef4444;
    color: white;
    border: none;
    border-radius: 8px;
    font-size: 0.9rem;
    font-weight: 500;
    cursor: pointer;
    transition: all 0.2s;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0.5rem;
  }

  .btn-logout:hover {
    background: #dc2626;
    transform: translateY(-1px);
  }

  .btn-logout:disabled {
    opacity: 0.7;
    cursor: not-allowed;
    transform: none;
  }

  .logout-spinner {
    width: 16px;
    height: 16px;
    border: 2px solid rgba(255, 255, 255, 0.3);
    border-top: 2px solid white;
    border-radius: 50%;
    animation: spin 1s linear infinite;
  }

  @keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
  }

  .btn-logout .loading-text {
    display: flex;
    align-items: center;
    gap: 0.5rem;
  }

  @keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
  }

  /* ⭐ NEW: Feedback Type Banner Styles */
.feedback-type-banner {
  margin: -1.5rem -1.5rem 1.5rem -1.5rem;
  padding: 1.25rem 1.5rem;
  border-radius: 0;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
  animation: slideDown 0.4s ease-out;
  border-bottom: 3px solid rgba(255, 255, 255, 0.3);
}

@keyframes slideDown {
  from {
    opacity: 0;
    transform: translateY(-10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.banner-content {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.banner-icon {
  font-size: 2rem;
  animation: pulse 2s ease-in-out infinite;
}

@keyframes pulse {
  0%, 100% {
    transform: scale(1);
  }
  50% {
    transform: scale(1.1);
  }
}

.banner-text {
  flex: 1;
}

.banner-text h4 {
  margin: 0 0 0.25rem 0;
  font-size: 1.1rem;
  font-weight: 700;
  color: inherit;
}

.banner-text p {
  margin: 0;
  font-size: 0.85rem;
  opacity: 0.9;
  color: inherit;
}

.banner-badge {
  background: rgba(255, 255, 255, 0.25);
  padding: 0.4rem 0.8rem;
  border-radius: 20px;
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  border: 1px solid rgba(255, 255, 255, 0.3);
}

.dark .feedback-type-banner {
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.4);
}
  </style>