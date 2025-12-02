<template>
  <div class="dashboard-container" :class="{ 'dark': isDarkMode }">
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

    <!-- Sidebar Navigation - Custom Tooltip Labels on Hover -->
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
        <router-link to="/teacher/subjects" class="sidebar-item rounded-bg" :class="{ 'active': $route.path.includes('/teacher/subjects') }">
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
      <button v-if="showScrollTop" @click="scrollToTop" class="scroll-to-top">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
          <path d="M7 14l5-5 5 5z"/>
        </svg>
      </button>

      <!-- Unified Gradebook Header -->
      <div class="gradebook-header">
        <div class="header-content">
          <div class="header-left">
            <div class="header-icon">
              <svg width="28" height="28" viewBox="0 0 24 24" fill="currentColor">
                <path d="M14,2H6A2,2 0 0,0 4,4V20A2,2 0 0,0 6,22H18A2,2 0 0,0 20,20V8L14,2M18,20H6V4H13V9H18V20Z" />
              </svg>
            </div>
            <div>
              <h1 class="header-title">Class Record</h1>
              <p class="header-subtitle">All-in-One Gradebook • Excel-style Layout</p>
            </div>
          </div>
          <div class="header-actions">
            <!-- Section Selector -->
            <div class="section-selector">
              <label for="section-select">Section:</label>
              <select id="section-select" v-model="selectedSectionId" @change="onSectionChange" class="section-select">
                <option value="">Choose a Section</option>
                <optgroup v-for="subject in subjects" :key="subject.id" :label="subject.name">
                  <option v-for="section in subject.sections" :key="section.id" :value="section.id">
                    {{ section.name }} ({{ subject.name }})
                  </option>
                </optgroup>
              </select>
            </div>
            <button @click="refreshData" class="refresh-btn grade-btn" :disabled="loading">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" :class="{ 'spinning': loading }">
                <path d="M17.65,6.35C16.2,4.9 14.21,4 12,4A8,8 0 0,0 4,12A8,8 0 0,0 12,20C15.73,20 18.84,17.45 19.73,14H17.65C16.83,16.33 14.61,18 12,18A6,6 0 0,1 6,12A6,6 0 0,1 12,6C13.66,6 15.14,6.69 16.22,7.78L13,11H20V4L17.65,6.35Z" />
              </svg>
              Refresh
            </button>
          </div>
        </div>
      </div>

      <!-- Loading State -->
      <div v-if="loading && !selectedSectionId" class="loading-container">
        <div class="spinner-large"></div>
        <p>Loading sections...</p>
      </div>

      <!-- Error State -->
      <div v-else-if="error" class="error-container">
        <svg width="48" height="48" viewBox="0 0 24 24" fill="currentColor">
          <path d="M12,2C17.53,2 22,6.47 22,12C22,17.53 17.53,22 12,22C6.47,22 2,17.53 2,12C2,6.47 6.47,2 12,2M15.59,7L12,10.59L8.41,7L7,8.41L10.59,12L7,15.59L8.41,17L12,13.41L15.59,17L17,15.59L13.41,12L17,8.41L15.59,7Z" />
        </svg>
        <h3>Error Loading Data</h3>
        <p>{{ error }}</p>
        <button @click="refreshData" class="grade-btn">Retry</button>
      </div>

      <!-- No Section Selected State -->
      <div v-else-if="!selectedSectionId" class="no-section-state">
        <div class="empty-icon">
          <svg width="64" height="64" viewBox="0 0 24 24" fill="currentColor">
            <path d="M19,3H5C3.89,3 3,3.89 3,5V19A2,2 0 0,0 5,21H19A2,2 0 0,0 21,19V5C21,3.89 20.1,3 19,3M7,7H9V9H7V7M7,11H9V13H7V11M7,15H9V17H7V15M11,7H17V9H11V7M11,11H17V13H11V11M11,15H17V17H11V15Z" />
          </svg>
        </div>
        <h3>Select a Section</h3>
        <p>Choose a section from the dropdown above to view the class record</p>
      </div>

      <!-- Excel-Style Gradebook -->
      <div v-else class="gradebook-main">
        <!-- Mini Analytics Panel -->
        <div class="analytics-panel">
          <div class="analytics-header">
            <h3>{{ currentSectionInfo.name }} Analytics</h3>
            <div class="header-actions">
              <span class="student-count">{{ students.length }} Students</span>
              <button @click="exportToExcel" class="export-btn grade-btn" :disabled="!students.length">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M14,2H6A2,2 0 0,0 4,4V20A2,2 0 0,0 6,22H18A2,2 0 0,0 20,20V8L14,2M18,20H6V4H13V9H18V20Z" />
                </svg>
                Export to Excel
              </button>
            </div>
          </div>
          <div class="analytics-stats">
            <div class="stat-mini">
              <div class="stat-icon">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M16,6L18.29,8.29L13.41,13.17L9.41,9.17L2,16.59L3.41,18L9.41,12L13.41,16L19.71,9.71L22,12V6H16Z" />
                </svg>
              </div>
              <div class="stat-content">
                <div class="stat-value">{{ analyticsData.averageScore }}%</div>
                <div class="stat-label">Avg Score</div>
              </div>
            </div>
            <div class="stat-mini">
              <div class="stat-icon">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M7,10L12,15L17,10H7Z" />
                </svg>
              </div>
              <div class="stat-content">
                <div class="stat-value">{{ analyticsData.highestScore }}%</div>
                <div class="stat-label">Highest</div>
              </div>
            </div>
            <div class="stat-mini">
              <div class="stat-icon">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M7,14L12,9L17,14H7Z" />
                </svg>
              </div>
              <div class="stat-content">
                <div class="stat-value">{{ analyticsData.lowestScore }}%</div>
                <div class="stat-label">Lowest</div>
              </div>
            </div>
            <div class="stat-mini">
              <div class="stat-icon">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M9,10V12H7V10H9M13,10V12H11V10H13M17,10V12H15V10H17M19,3A2,2 0 0,1 21,5V19A2,2 0 0,1 19,21H5C3.89,21 3,20.1 3,19V5A2,2 0 0,1 5,3H6V1H8V3H16V1H18V3H19M19,19V8H5V19H19M9,14V16H7V14H9M13,14V16H11V14H13M17,14V16H15V14H17Z" />
                </svg>
              </div>
              <div class="stat-content">
                <div class="stat-value">{{ analyticsData.submissionRate }}%</div>
                <div class="stat-label">Submitted</div>
              </div>
            </div>
          </div>
        </div>

        <!-- Excel-Style Gradebook Table -->
        <div class="gradebook-container">
          <div class="gradebook-scroll">
            <table class="gradebook-table">
              <thead class="gradebook-header">
                <tr>
                  <th class="student-column sticky-col">
                    <div class="header-content">
                      <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                        <path d="M12,5.5A3.5,3.5 0 0,1 15.5,9A3.5,3.5 0 0,1 12,12.5A3.5,3.5 0 0,1 8.5,9A3.5,3.5 0 0,1 12,5.5M5,8C5.56,8 6.08,8.15 6.53,8.42C6.38,9.85 6.8,11.27 7.66,12.38C7.16,13.34 6.16,14 5,14A3,3 0 0,1 2,11A3,3 0 0,1 5,8M19,8A3,3 0 0,1 22,11A3,3 0 0,1 19,14C17.84,14 16.84,13.34 16.34,12.38C17.2,11.27 17.62,9.85 17.47,8.42C17.92,8.15 18.44,8 19,8Z" />
                      </svg>
                      Student
                    </div>
                  </th>
                  <th v-for="assessment in assessments" :key="assessment.id" class="assessment-column">
                    <div class="header-content">
                      <div class="assessment-title">{{ assessment.title }}</div>
                      <div class="assessment-info">
                        <span class="assessment-type">{{ getAssessmentTypeLabel(assessment.type) }}</span>
                        <span class="assessment-points">{{ assessment.max_score }}pts</span>
                      </div>
                    </div>
                  </th>
                  <th class="total-column">
                    <div class="header-content">
                      <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                        <path d="M19,3H5C3.89,3 3,3.89 3,5V19A2,2 0 0,0 5,21H19A2,2 0 0,0 21,19V5C21,3.89 20.1,3 19,3M7,7H17V9H7V7M7,11H17V13H7V11M7,15H17V17H7V15Z" />
                      </svg>
                      Total
                    </div>
                  </th>
                </tr>
              </thead>
              <tbody class="gradebook-body">
                <template v-for="student in students" :key="student.id">
                  <!-- Main Student Row -->
                  <tr class="student-row" :class="{ 'expanded': expandedStudent === student.id }">
                    <td class="student-cell sticky-col" @click="toggleStudentHistory(student.id)">
                      <div class="student-info">
                        <div class="student-avatar">{{ getInitials(student.full_name) }}</div>
                        <div class="student-details">
                          <div class="student-name">{{ student.full_name }}</div>
                          <div class="student-id">{{ student.student_id || 'N/A' }}</div>
                        </div>
                        <button class="expand-btn" :class="{ 'rotated': expandedStudent === student.id }">
                          <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                            <path d="M8.59,16.58L13.17,12L8.59,7.41L10,6L16,12L10,18L8.59,16.58Z" />
                          </svg>
                        </button>
                      </div>
                    </td>
                    <td v-for="assessment in assessments" :key="assessment.id" class="score-cell">
                      <div class="score-input-wrapper">
                        <input 
                          v-if="assessment.type === 'manual'"
                          type="number"
                          :value="getStudentScore(student.id, assessment.id)"
                          @input="updateManualScore(student.id, assessment.id, $event.target.value)"
                          @blur="saveManualScore(student.id, assessment.id)"
                          class="score-input manual"
                          :max="assessment.max_score"
                          min="0"
                          step="0.5"
                          placeholder="--"
                        />
                        <div v-else class="score-display auto" :class="getScoreClass(getStudentPercentage(student.id, assessment.id))">
                          <span class="score-value">{{ getStudentScore(student.id, assessment.id) || '--' }}</span>
                          <span v-if="getStudentScore(student.id, assessment.id)" class="score-max">/ {{ assessment.max_score }}</span>
                        </div>
                        <div v-if="hasSubmissionPending(student.id, assessment.id)" class="pending-indicator" title="Pending Review">
                          <svg width="12" height="12" viewBox="0 0 24 24" fill="currentColor">
                            <path d="M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2M16.2,16.2L11,13V7H12.5V12.2L17,14.9L16.2,16.2Z" />
                          </svg>
                        </div>
                      </div>
                    </td>
                    <td class="total-cell">
                      <div class="total-score" :class="getScoreClass(getStudentTotalPercentage(student.id))">
                        <span class="total-value">{{ getStudentTotal(student.id) }}</span>
                        <span class="total-max">/ {{ getTotalMaxScore() }}</span>
                        <div class="total-percentage">{{ getStudentTotalPercentage(student.id) }}%</div>
                      </div>
                    </td>
                  </tr>
                  
                  <!-- Expandable Student History Row -->
                  <tr v-if="expandedStudent === student.id" class="student-history-row">
                    <td colspan="100%" class="history-cell">
                      <div class="student-history-panel">
                        <div class="history-header">
                          <h4>{{ student.full_name }} - Detailed History</h4>
                        </div>
                        <div class="history-content">
                          <div v-for="assessment in assessments" :key="assessment.id" class="history-item">
                            <div class="history-assessment">
                              <div class="assessment-name">{{ assessment.title }}</div>
                              <div class="assessment-details">
                                <span class="score-info">
                                  Score: {{ getStudentScore(student.id, assessment.id) || 'Not taken' }}
                                  <span v-if="getStudentScore(student.id, assessment.id)">/ {{ assessment.max_score }}</span>
                                </span>
                                <span v-if="getStudentScore(student.id, assessment.id)" class="percentage-info">
                                  ({{ getStudentPercentage(student.id, assessment.id) }}%)
                                </span>
                              </div>
                              <div v-if="hasSubmissionPending(student.id, assessment.id)" class="status-pending">
                                <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor">
                                  <path d="M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2M16.2,16.2L11,13V7H12.5V12.2L17,14.9L16.2,16.2Z" />
                                </svg>
                                Pending Review
                              </div>
                              <button v-if="hasSubmissionToGrade(student.id, assessment.id)" 
                                @click="reviewStudentSubmission(student.id, assessment.id)"
                                class="review-btn">
                                Grade Submission
                              </button>
                            </div>
                          </div>
                        </div>
                      </div>
                    </td>
                  </tr>
                </template>
              </tbody>
            </table>
          </div>
        </div>
      </div>


    <!-- Review/Grade Modal -->
    <div v-if="showReviewModal" class="modal-overlay" @click="closeReviewModal">
      <div class="review-modal" @click.stop>
        <div class="modal-header">
          <div>
            <h3>{{ modalMode === 'view' ? 'View Submission' : 'Grade Submission' }}</h3>
            <p class="modal-subtitle" v-if="selectedSubmission">
              {{ selectedSubmission.student_name }} - {{ selectedSubmission.quiz_title }}
            </p>
          </div>
          <button @click="closeReviewModal" class="modal-close">
            <i class="fas fa-times"></i>
          </button>
        </div>

        <div class="modal-content">
          <div v-if="loadingQuestions" class="loading-questions">
            <div class="spinner-small"></div>
            <p>Loading questions...</p>
          </div>

          <div v-else-if="reviewQuestions.length === 0" class="no-questions">
            <p>No questions found for this quiz.</p>
          </div>

          <div v-else class="submission-review">
            <div class="review-summary">
              <div class="summary-stat">
                <span class="stat-label">Score</span>
                <span class="stat-value">{{ calculateReviewScore() }}/{{ maxReviewScore }}</span>
              </div>
              <div class="summary-stat">
                <span class="stat-label">Percentage</span>
                <span class="stat-value">{{ calculateReviewPercentage() }}%</span>
              </div>
              <div class="summary-stat">
                <span class="stat-label">Correct</span>
                <span class="stat-value">{{ correctAnswerCount }}/{{ reviewQuestions.length }}</span>
              </div>
            </div>

            <div class="questions-review">
              <div v-for="(question, index) in reviewQuestions" :key="question.id" class="question-review-item">
                <div class="question-header">
                  <div class="question-number">Q{{ index + 1 }}</div>
                  <div class="question-result" :class="question.is_correct ? 'correct' : 'incorrect'">
                    {{ question.is_correct ? '✓ Correct' : '✗ Incorrect' }}
                  </div>
                  <div class="question-points" v-if="modalMode === 'grade'">
                    <input 
                      v-model.number="question.manualPoints"
                      type="number"
                      :max="question.points"
                      min="0"
                      step="0.5"
                      class="points-input"
                      @input="updateQuestionPoints(question)"
                    /> / {{ question.points }} pts
                  </div>
                  <div class="question-points" v-else>
                    {{ question.points_earned }} / {{ question.points }} pts
                  </div>
                </div>

                <div class="question-text">{{ question.question_text }}</div>

                <!-- Multiple Choice -->
                <div v-if="question.question_type === 'multiple_choice'" class="answer-section">
                  <div class="answer-key-label">
                    <strong>Answer Key:</strong> {{ getCorrectOptionLabel(question) }}
                  </div>
                  <div class="answer-key-label">
                    <strong>Student's Answer:</strong> 
                    <span v-if="question.selected_option_id">{{ getStudentOptionLabel(question) }}</span>
                    <span v-else-if="question.answer_text">{{ question.answer_text }}</span>
                    <span v-else style="color: #ef4444;">
                      No answer provided
                    </span>
                  </div>
                  <div class="options-grid">
                    <div 
                      v-for="option in question.options" 
                      :key="option.id" 
                      class="option-item"
                      :class="{
                        'selected': question.selected_option_id === option.id,
                        'correct': option.is_correct,
                        'incorrect': question.selected_option_id === option.id && !option.is_correct
                      }"
                    >
                      <div class="option-letter">{{ String.fromCharCode(65 + (option.option_number - 1)) }}</div>
                      <div class="option-content">
                        <div class="option-text">{{ option.option_text }}</div>
                        <div v-if="option.is_correct" class="correct-tag">✓ Correct Answer</div>
                        <div v-if="question.selected_option_id === option.id" class="selected-tag">Student's Answer</div>
                      </div>
                    </div>
                  </div>
                </div>

                <!-- True/False -->
                <div v-else-if="question.question_type === 'true_false'" class="answer-section">
                  <div class="answer-key-label">
                    <strong>Answer Key:</strong> {{ question.correct_answer }}
                  </div>
                  <div class="answer-key-label">
                    <strong>Student's Answer:</strong> 
                    <span v-if="question.answer_text" :class="question.is_correct ? 'text-green-600' : 'text-red-600'">
                      {{ question.answer_text }}
                    </span>
                    <span v-else style="color: #ef4444;">No answer provided</span>
                  </div>
                  <div class="true-false-options">
                    <div class="tf-option" :class="{ 
                      'student-selected': question.answer_text === 'true', 
                      'correct-answer': question.correct_answer === 'true',
                      'wrong-answer': question.answer_text === 'true' && question.correct_answer !== 'true'
                    }">
                      <strong>True</strong>
                      <span v-if="question.correct_answer === 'true'" class="correct-tag">✓ Correct</span>
                      <span v-if="question.answer_text === 'true'" class="selected-tag">Student's Answer</span>
                    </div>
                    <div class="tf-option" :class="{ 
                      'student-selected': question.answer_text === 'false', 
                      'correct-answer': question.correct_answer === 'false',
                      'wrong-answer': question.answer_text === 'false' && question.correct_answer !== 'false'
                    }">
                      <strong>False</strong>
                      <span v-if="question.correct_answer === 'false'" class="correct-tag">✓ Correct</span>
                      <span v-if="question.answer_text === 'false'" class="selected-tag">Student's Answer</span>
                    </div>
                  </div>
                </div>

                <!-- Fill in the Blank -->
                <div v-else-if="question.question_type === 'fill_blank'" class="answer-section">
                  <div class="fill-blank-answers">
                    <div class="answer-key-box">
                      <div class="answer-label">Answer Key:</div>
                      <div class="answer-text correct">
                        {{ question.correct_answer }}
                      </div>
                    </div>
                    <div class="student-answer-box">
                      <div class="answer-label">Student's Answer:</div>
                      <div class="answer-text" :class="question.is_correct ? 'correct' : 'incorrect'">
                        {{ question.answer_text || 'No answer' }}
                      </div>
                    </div>
                  </div>
                </div>

                <!-- Teacher Comment -->
                <div class="teacher-comment-section" v-if="modalMode === 'grade'">
                  <textarea 
                    v-model="question.teacherComment"
                    class="comment-input"
                    placeholder="Add feedback for this question..."
                    rows="2"
                  ></textarea>
                </div>
                <div class="teacher-comment-section" v-else-if="question.teacher_comment">
                  <div class="comment-display">
                    <strong>Teacher's Feedback:</strong>
                    <p>{{ question.teacher_comment }}</p>
                  </div>
                </div>
              </div>
            </div>

            <!-- Overall Feedback -->
            <div class="overall-feedback-section" v-if="modalMode === 'grade'">
              <h4>Overall Feedback</h4>
              <textarea 
                v-model="reviewFeedback" 
                class="feedback-textarea"
                placeholder="Add overall feedback for the student..."
                rows="3"
              ></textarea>
            </div>
            <div class="overall-feedback-section" v-else-if="selectedSubmission?.teacher_feedback">
              <h4>Overall Feedback</h4>
              <div class="feedback-display">
                <p>{{ selectedSubmission.teacher_feedback }}</p>
              </div>
            </div>
          </div>
        </div>

        <div class="modal-actions">
          <button @click="closeReviewModal" class="btn-modal cancel">Close</button>
          <button v-if="modalMode === 'grade'" @click="saveGrade" class="btn-modal primary" :disabled="savingGrade">
            {{ savingGrade ? 'Saving...' : 'Save Grade' }}
          </button>
        </div>
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

<script setup>
import { ref, computed, watch, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { supabase } from '@/supabase.js'
import { useDarkMode } from '@/composables/useDarkMode.js'
import * as XLSX from 'xlsx'

const { isDarkMode } = useDarkMode()
const router = useRouter()

const loading = ref(true)
const loadingQuestions = ref(false)
const savingGrade = ref(false)
const error = ref(null)
const searchQuery = ref('')
const teacherId = ref(null)

// Data for unified gradebook
const subjects = ref([])
const selectedSectionId = ref('')
const currentSectionInfo = ref({})
const students = ref([])
const assessments = ref([])
const gradebookData = ref({}) // student_id -> assessment_id -> score
const submissions = ref([]) // For pending review tracking
const expandedStudent = ref(null)

const showReviewModal = ref(false)
const selectedSubmission = ref(null)
const reviewQuestions = ref([])
const reviewFeedback = ref('')
const modalMode = ref('view')

// Logout modal states
const showLogoutModal = ref(false)
const isLoggingOut = ref(false)

const selectedSubjectFilter = ref('')
const lastRefresh = ref(new Date())
const newSubmissionsCount = ref(0)

// Missing variables for pagination and filtering
const selectedStatus = ref('all')
const currentPage = ref(1)
const sortField = ref('')
const sortDirection = ref('asc')

// Navbar dropdown states
const showNotifDropdown = ref(false)
const showProfileDropdown = ref(false)
const notifications = ref([])
const fullName = ref('Teacher')
const showScrollTop = ref(false)

// Analytics data for the selected section
const analyticsData = computed(() => {
  if (!students.value.length || !assessments.value.length) {
    return {
      averageScore: 0,
      highestScore: 0,
      lowestScore: 0,
      submissionRate: 0
    }
  }

  const scores = []
  let totalSubmissions = 0
  let possibleSubmissions = students.value.length * assessments.value.length

  students.value.forEach(student => {
    assessments.value.forEach(assessment => {
      const score = getStudentScore(student.id, assessment.id)
      if (score !== null && score !== undefined && score !== '') {
        const percentage = (score / assessment.max_score) * 100
        scores.push(percentage)
        totalSubmissions++
      }
    })
  })

  const averageScore = scores.length > 0 ? Math.round(scores.reduce((sum, s) => sum + s, 0) / scores.length) : 0
  const highestScore = scores.length > 0 ? Math.round(Math.max(...scores)) : 0
  const lowestScore = scores.length > 0 ? Math.round(Math.min(...scores)) : 0
  const submissionRate = possibleSubmissions > 0 ? Math.round((totalSubmissions / possibleSubmissions) * 100) : 0

  return {
    averageScore,
    highestScore, 
    lowestScore,
    submissionRate
  }
})

const correctAnswerCount = computed(() => {
  return reviewQuestions.value.filter(q => q.is_correct).length
})

const maxReviewScore = computed(() => {
  return reviewQuestions.value.reduce((sum, q) => sum + (q.points || 1), 0)
})



const getTeacherInfo = async () => {
  try {
    const { data: { user }, error: userError } = await supabase.auth.getUser()
    if (userError || !user) {
      error.value = 'Authentication error'
      return false
    }

    // Get profile first
    const { data: profile, error: profileError } = await supabase
      .from('profiles')
      .select('id, role')
      .eq('auth_user_id', user.id)
      .eq('role', 'teacher')
      .single()

    if (profileError || !profile) {
      error.value = 'Access denied - Teacher role required'
      return false
    }

    // Get teacher data separately
    const { data: teacher, error: teacherError } = await supabase
      .from('teachers')
      .select('id')
      .eq('profile_id', profile.id)
      .single()

    if (teacherError || !teacher) {
      error.value = 'Teacher record not found'
      return false
    }

    teacherId.value = teacher.id
    return true
  } catch (err) {
    console.error('Error in getTeacherInfo:', err)
    error.value = err.message || 'An error occurred'
    return false
  }
}

// Fetch all subjects with their sections for the dropdown
const fetchSubjects = async () => {
  try {
    loading.value = true
    error.value = null

    console.log('🔄 Fetching subjects and sections for teacher:', teacherId.value)

    // Get subjects with sections
    const { data: subjectsData, error: subjectsError } = await supabase
      .from('subjects')
      .select(`
        id, 
        name, 
        grade_level,
        sections!inner(
          id,
          name,
          section_code,
          is_active
        )
      `)
      .eq('teacher_id', teacherId.value)
      .eq('is_active', true)
      .eq('sections.is_active', true)

    if (subjectsError) throw subjectsError

    console.log('📚 Found subjects with sections:', subjectsData?.length || 0)

    // Process the data for dropdown
    subjects.value = subjectsData?.map(subject => ({
      id: subject.id,
      name: subject.name,
      grade_level: subject.grade_level,
      sections: subject.sections || []
    })) || []

    console.log('✅ Processed subjects:', subjects.value)
  } catch (err) {
    console.error('❌ Error fetching subjects:', err)
    error.value = `Failed to load subjects: ${err.message}`
  } finally {
    loading.value = false
  }
}

// Handle section selection from dropdown
const onSectionChange = async () => {
  if (!selectedSectionId.value) {
    currentSectionInfo.value = {}
    students.value = []
    assessments.value = []
    gradebookData.value = {}
    return
  }

  try {
    loading.value = true
    error.value = null
    await fetchGradebookData(selectedSectionId.value)
  } catch (err) {
    console.error('❌ Error loading gradebook data:', err)
    error.value = `Failed to load gradebook data: ${err.message}`
  } finally {
    loading.value = false
  }
}

// Fetch complete gradebook data for a section
const fetchGradebookData = async (sectionId) => {
  console.log('🔄 Fetching gradebook data for section:', sectionId)

  // Get section info
  const { data: sectionInfo, error: sectionError } = await supabase
    .from('sections')
    .select(`
      id, name, section_code, subject_id,
      subjects(name, grade_level)
    `)
    .eq('id', sectionId)
    .single()

  if (sectionError) throw sectionError
  currentSectionInfo.value = sectionInfo

  // Get students in this section
  const { data: studentsData, error: studentsError } = await supabase
    .from('enrollments')
    .select(`
      student_id,
      students(id, full_name, email, student_id)
    `)
    .eq('section_id', sectionId)
    .eq('status', 'active')
    .eq('is_active', true)

  if (studentsError) throw studentsError
  students.value = studentsData?.map(enrollment => enrollment.students) || []

  // Get quizzes (auto-graded assessments) for this section
  const { data: quizzesData, error: quizzesError } = await supabase
    .from('quizzes')
    .select('id, title, max_score, created_at')
    .eq('section_id', sectionId)
    .eq('is_active', true)
    .order('created_at')

  if (quizzesError) throw quizzesError

  // Get manual assessments (for future expansion)
  // For now, we'll create some sample manual assessments
  const manualAssessments = [
    { id: 'manual_1', title: 'Assignment 1', type: 'manual', max_score: 50 },
    { id: 'manual_2', title: 'Activity 1', type: 'manual', max_score: 25 }
  ]

  // Combine all assessments
  const allAssessments = [
    ...(quizzesData?.map(quiz => ({
      id: quiz.id,
      title: quiz.title,
      type: 'auto',
      max_score: quiz.max_score,
      created_at: quiz.created_at
    })) || []),
    ...manualAssessments
  ]

  assessments.value = allAssessments

  // Get quiz attempts/results for gradebook
  if (quizzesData && quizzesData.length > 0) {
    const quizIds = quizzesData.map(q => q.id)
    const { data: attemptsData } = await supabase
      .from('quiz_attempts')
      .select('student_id, quiz_id, total_score, status, submitted_at')
      .in('quiz_id', quizIds)
      .in('student_id', students.value.map(s => s.id))
      .order('submitted_at', { ascending: false })

    // Process attempts into gradebook data structure
    const newGradebookData = {}
    students.value.forEach(student => {
      newGradebookData[student.id] = {}
    })

    attemptsData?.forEach(attempt => {
      // Only take the latest attempt for each student-quiz combination
      if (!newGradebookData[attempt.student_id][attempt.quiz_id]) {
        newGradebookData[attempt.student_id][attempt.quiz_id] = attempt.total_score
      }
    })

    gradebookData.value = newGradebookData
  }

  console.log('✅ Gradebook data loaded:', {
    section: sectionInfo.name,
    students: students.value.length,
    assessments: assessments.value.length
  })
}

// Gradebook helper functions
const getStudentScore = (studentId, assessmentId) => {
  return gradebookData.value[studentId]?.[assessmentId] || null
}

const getStudentPercentage = (studentId, assessmentId) => {
  const score = getStudentScore(studentId, assessmentId)
  const assessment = assessments.value.find(a => a.id === assessmentId)
  if (!score || !assessment) return 0
  return Math.round((score / assessment.max_score) * 100)
}

const getStudentTotal = (studentId) => {
  let total = 0
  assessments.value.forEach(assessment => {
    const score = getStudentScore(studentId, assessment.id)
    if (score) total += score
  })
  return total
}

const getTotalMaxScore = () => {
  return assessments.value.reduce((sum, assessment) => sum + assessment.max_score, 0)
}

const getStudentTotalPercentage = (studentId) => {
  const total = getStudentTotal(studentId)
  const maxTotal = getTotalMaxScore()
  if (maxTotal === 0) return 0
  return Math.round((total / maxTotal) * 100)
}

const getAssessmentTypeLabel = (type) => {
  return type === 'auto' ? 'Quiz' : 'Manual'
}

const hasSubmissionPending = (studentId, assessmentId) => {
  // Check if there's a pending submission for this student-assessment combination
  return submissions.value.some(s => 
    s.student_id === studentId && 
    s.quiz_id === assessmentId && 
    s.status === 'submitted'
  )
}

const hasSubmissionToGrade = (studentId, assessmentId) => {
  return hasSubmissionPending(studentId, assessmentId)
}

const toggleStudentHistory = (studentId) => {
  expandedStudent.value = expandedStudent.value === studentId ? null : studentId
}

const updateManualScore = (studentId, assessmentId, value) => {
  if (!gradebookData.value[studentId]) {
    gradebookData.value[studentId] = {}
  }
  gradebookData.value[studentId][assessmentId] = parseFloat(value) || null
}

const saveManualScore = async (studentId, assessmentId) => {
  // Implement saving manual scores to database
  // For now, just log it
  const score = getStudentScore(studentId, assessmentId)
  console.log('💾 Saving manual score:', { studentId, assessmentId, score })
}

const reviewStudentSubmission = async (studentId, assessmentId) => {
  // Find the submission to review
  const submission = submissions.value.find(s => 
    s.student_id === studentId && s.quiz_id === assessmentId
  )
  
  if (submission) {
    await reviewSubmission(submission)
  }
}

const refreshData = async () => {
  console.log('  Manual refresh triggered...')
  loading.value = true
  
  try {
    await fetchSubjects()
    
    if (selectedSectionId.value) {
      await fetchGradebookData(selectedSectionId.value)
    }
    
    console.log('✅ Manual refresh completed')
  } catch (error) {
    console.error('❌ Error during manual refresh:', error)
  } finally {
    loading.value = false
  }
}

const loadQuestionsAndAnswers = async (submission) => {
  try {
    loadingQuestions.value = true

    console.log('🔍 Loading questions for submission:', submission.id)
    console.log('📊 Submission details:', {
      id: submission.id,
      quiz_id: submission.quiz_id,
      student_id: submission.student_id,
      student_name: submission.student_name
    })

    // Get questions first
    const { data: questions, error: questionsError } = await supabase
      .from('quiz_questions')
      .select('id, question_number, question_type, question_text, points')
      .eq('quiz_id', submission.quiz_id)
      .order('question_number')

    if (questionsError) {
      console.error('❌ Questions error:', questionsError)
      throw questionsError
    }

    console.log('📝 Found questions:', questions?.length || 0, questions)

    if (!questions || questions.length === 0) {
      reviewQuestions.value = []
      return
    }

    const questionIds = questions.map(q => q.id)
    console.log('🔢 Question IDs:', questionIds)

    // Get question options first
    console.log('📋 Getting options for questions:', questionIds)
    const { data: optionsData, error: optionsError } = await supabase
      .from('question_options')
      .select('*')
      .in('question_id', questionIds)
      .order('option_number')

    if (optionsError) {
      console.error('❌ Options error:', optionsError)
      throw optionsError
    }

    // Get correct answers
    console.log('✅ Getting correct answers for questions')
    const { data: answersData, error: answersError } = await supabase
      .from('question_answers')
      .select('*')
      .in('question_id', questionIds)

    if (answersError) {
      console.error('❌ Answers error:', answersError)
      throw answersError
    }

    // Get student answers - simplified query
    console.log('👤 Getting student answers for attempt:', submission.id)
    const { data: studentAnswersData, error: studentAnswersError } = await supabase
      .from('student_answers')
      .select('*')
      .eq('attempt_id', submission.id)

    if (studentAnswersError) {
      console.error('❌ Student answers error:', studentAnswersError)
      throw studentAnswersError
    }

    // Create response objects for compatibility
    const optionsRes = { data: optionsData, error: optionsError }
    const answersRes = { data: answersData, error: answersError }
    const studentAnswersRes = { data: studentAnswersData, error: studentAnswersError }

    console.log('📋 Options data:', optionsRes.data?.length || 0, optionsRes.data)
    console.log('✅ Correct answers data:', answersRes.data?.length || 0, answersRes.data)
    console.log('👤 Student answers data:', studentAnswersRes.data?.length || 0, studentAnswersRes.data)

    if (optionsRes.error) console.error('Options error:', optionsRes.error)
    if (answersRes.error) console.error('Answers error:', answersRes.error)
    if (studentAnswersRes.error) console.error('Student answers error:', studentAnswersRes.error)

    // Enhanced debugging for student answers
    console.log('🔍 Student answers analysis:', {
      found: studentAnswersRes.data?.length || 0,
      attemptId: submission.id,
      questionIds: questionIds,
      studentAnswers: studentAnswersRes.data
    })

    // If no student answers found, try comprehensive search
    if (!studentAnswersRes.data || studentAnswersRes.data.length === 0) {
      console.log('🔍 No student answers found, trying multiple approaches...')
      
      // Try 1: Get all answers for this attempt (no filters)
      const { data: allAnswers, error: allError } = await supabase
        .from('student_answers')
        .select('*')
        .eq('attempt_id', submission.id)
      
      console.log('🔍 All answers for attempt:', allAnswers?.length || 0, allAnswers)
      
      // Try 2: Get answers by student and quiz combination
      const { data: studentQuizAnswers, error: sqError } = await supabase
        .from('student_answers')
        .select(`
          *,
          quiz_attempts!inner(quiz_id, student_id)
        `)
        .eq('quiz_attempts.quiz_id', submission.quiz_id)
        .eq('quiz_attempts.student_id', submission.student_id)
      
      console.log('🔍 Student-quiz answers:', studentQuizAnswers?.length || 0, studentQuizAnswers)
      
      // Use whichever approach found data
      if (allAnswers && allAnswers.length > 0) {
        studentAnswersRes.data = allAnswers
        console.log('🔄 Using all answers approach')
      } else if (studentQuizAnswers && studentQuizAnswers.length > 0) {
        studentAnswersRes.data = studentQuizAnswers
        console.log('🔄 Using student-quiz approach')
      }
    }

    // Additional debug: Try a completely raw query to see what's in the database
    console.log('  Raw debug query to check database...')
    const { data: debugAnswers, error: debugError } = await supabase
      .from('student_answers')
      .select('*')
      .eq('attempt_id', submission.id)
    
    console.log('🔍 Raw debug query result:', debugAnswers?.length || 0, debugAnswers)
    if (debugError) console.error('Debug query error:', debugError)

    // Create lookup maps with better validation
    const optionsMap = {}
    optionsRes.data?.forEach(opt => {
      if (!optionsMap[opt.question_id]) {
        optionsMap[opt.question_id] = []
      }
      optionsMap[opt.question_id].push(opt)
    })

    const answersMap = {}
    answersRes.data?.forEach(ans => {
      answersMap[ans.question_id] = ans
    })

    const studentAnswersMap = {}
    studentAnswersRes.data?.forEach(sa => {
      console.log('📝 Mapping student answer:', {
        id: sa.id,
        question_id: sa.question_id,
        selected_option_id: sa.selected_option_id,
        answer_text: sa.answer_text,
        attempt_id: sa.attempt_id
      })
      studentAnswersMap[sa.question_id] = sa
    })

    console.log('🗺️ Maps created:', {
      optionsMap: Object.keys(optionsMap).length,
      answersMap: Object.keys(answersMap).length,
      studentAnswersMap: Object.keys(studentAnswersMap).length,
      studentAnswerDetails: Object.entries(studentAnswersMap).map(([qId, answer]) => ({
        questionId: qId,
        hasSelectedOption: !!answer.selected_option_id,
        hasAnswerText: !!answer.answer_text,
        selectedOptionId: answer.selected_option_id,
        answerText: answer.answer_text
      }))
    })

    // Process the questions with enhanced logic
    reviewQuestions.value = questions.map(q => {
      const studentAnswer = studentAnswersMap[q.id] || {}
      const correctAnswer = answersMap[q.id]
      const questionOptions = optionsMap[q.id] || []

      console.log(`Processing Question ${q.question_number} (ID: ${q.id}):`, {
        studentAnswer: {
          id: studentAnswer.id,
          selected_option_id: studentAnswer.selected_option_id,
          answer_text: studentAnswer.answer_text,
          hasData: !!Object.keys(studentAnswer).length
        },
        correctAnswer,
        questionOptions: questionOptions.length,
        optionsList: questionOptions.map(opt => ({
          id: opt.id,
          number: opt.option_number,
          text: opt.option_text,
          correct: opt.is_correct
        })),
        type: q.question_type
      })

      // Determine if answer is correct based on question type
      let isCorrect = false
      let correctAnswerText = null

      if (q.question_type === 'multiple_choice') {
        // Find correct option
        const correctOption = questionOptions.find(opt => opt.is_correct)
        correctAnswerText = correctOption ? correctOption.option_text : 'No correct option found'
        
        console.log(`Multiple choice analysis:`, {
          correctOption,
          studentSelectedId: studentAnswer.selected_option_id,
          studentAnswerText: studentAnswer.answer_text,
          allOptions: questionOptions
        })

        // Check if student selected the correct option by ID
        if (correctOption && studentAnswer.selected_option_id === correctOption.id) {
          isCorrect = true
        }
        // Enhanced fallback logic for answer_text matching
        else if (studentAnswer.answer_text && questionOptions.length > 0) {
          const answerText = studentAnswer.answer_text.toString().toLowerCase().trim()
          
          console.log(`🔍 Trying to match answer_text: "${answerText}" for question ${q.id}`)
          
          // Method 1: Check if it's a number (like "1", "2", etc.)
          if (/^\d+$/.test(answerText)) {
            const optionNumber = parseInt(answerText)
            const selectedOption = questionOptions.find(opt => opt.option_number === optionNumber)
            if (selectedOption) {
              console.log(`✅ Matched by option number: ${optionNumber}`)
              if (selectedOption.is_correct) isCorrect = true
              studentAnswer.selected_option_id = selectedOption.id
            }
          }
          // Method 2: Check if it matches option text exactly
          else {
            const matchedOption = questionOptions.find(opt => 
              opt.option_text.toLowerCase().trim() === answerText
            )
            if (matchedOption) {
              console.log(`✅ Matched by option text: "${matchedOption.option_text}"`)
              if (matchedOption.is_correct) isCorrect = true
              studentAnswer.selected_option_id = matchedOption.id
            }
            // Method 3: Check if it matches option letter (A, B, C, etc.)
            else if (/^[a-zA-Z]$/.test(answerText)) {
              const letterIndex = answerText.toUpperCase().charCodeAt(0) - 65 + 1
              const letterOption = questionOptions.find(opt => opt.option_number === letterIndex)
              if (letterOption) {
                console.log(`✅ Matched by letter: ${answerText.toUpperCase()}`)
                if (letterOption.is_correct) isCorrect = true
                studentAnswer.selected_option_id = letterOption.id
              }
            }
          }
        }
        
        // If we still don't have a selected_option_id but have answer_text, use it for display
        if (!studentAnswer.selected_option_id && studentAnswer.answer_text) {
          console.log(`⚠️ Could not match answer_text "${studentAnswer.answer_text}" to any option`)
        }
      } else if (q.question_type === 'true_false') {
        correctAnswerText = correctAnswer?.correct_answer
        if (correctAnswerText && studentAnswer.answer_text) {
          isCorrect = studentAnswer.answer_text.toLowerCase() === correctAnswerText.toLowerCase()
        }
      } else if (q.question_type === 'fill_blank') {
        correctAnswerText = correctAnswer?.correct_answer
        if (correctAnswerText && studentAnswer.answer_text) {
          // Case-insensitive comparison, trimmed
          isCorrect = studentAnswer.answer_text.trim().toLowerCase() === correctAnswerText.trim().toLowerCase()
        }
      }

      const pointsEarned = isCorrect ? (q.points || 1) : 0

      console.log(`Question ${q.question_number} final result:`, {
        type: q.question_type,
        correct_answer: correctAnswerText,
        student_answer: studentAnswer.answer_text || studentAnswer.selected_option_id,
        selected_option_id: studentAnswer.selected_option_id,
        answer_text: studentAnswer.answer_text,
        is_correct: isCorrect,
        points_earned: pointsEarned,
        studentAnswerObject: studentAnswer
      })

      return {
        id: q.id,
        question_number: q.question_number,
        question_type: q.question_type,
        question_text: q.question_text,
        points: q.points || 1,
        options: questionOptions,
        correct_answer: correctAnswerText,
        selected_option_id: studentAnswer.selected_option_id || null,
        answer_text: studentAnswer.answer_text || null,
        is_correct: isCorrect,
        points_earned: pointsEarned,
        teacher_comment: studentAnswer.teacher_comment || '',
        manualPoints: pointsEarned,
        teacherComment: studentAnswer.teacher_comment || '',
        student_answer_id: studentAnswer.id || null
      }
    })

    console.log('✅ Questions processed:', reviewQuestions.value.length)
    console.log('📊 Review questions data:', reviewQuestions.value)
  } catch (err) {
    console.error('Error loading questions:', err)
    alert('Failed to load questions: ' + err.message)
  } finally {
    loadingQuestions.value = false
  }
}

const reviewSubmission = async (submission) => {
  modalMode.value = 'grade'
  selectedSubmission.value = submission
  reviewFeedback.value = submission.teacher_feedback || ''
  showReviewModal.value = true
  await loadQuestionsAndAnswers(submission)
}

const viewSubmission = async (submission) => {
  modalMode.value = 'view'
  selectedSubmission.value = submission
  reviewFeedback.value = submission.teacher_feedback || ''
  showReviewModal.value = true
  await loadQuestionsAndAnswers(submission)
}

const updateQuestionPoints = (question) => {
  if (question.manualPoints > question.points) {
    question.manualPoints = question.points
  }
  if (question.manualPoints < 0) {
    question.manualPoints = 0
  }
}

const calculateReviewScore = () => {
  if (modalMode.value === 'grade') {
    return reviewQuestions.value.reduce((sum, q) => sum + (parseFloat(q.manualPoints) || 0), 0)
  } else {
    return reviewQuestions.value.reduce((sum, q) => sum + (parseFloat(q.points_earned) || 0), 0)
  }
}

const calculateReviewPercentage = () => {
  if (maxReviewScore.value === 0) return 0
  return Math.round((calculateReviewScore() / maxReviewScore.value) * 100)
}

const closeReviewModal = () => {
  showReviewModal.value = false
  selectedSubmission.value = null
  reviewQuestions.value = []
  reviewFeedback.value = ''
  modalMode.value = 'view'
}

const getCorrectOptionLabel = (question) => {
  const correctOption = question.options.find(opt => opt.is_correct)
  if (correctOption) {
    return String.fromCharCode(65 + correctOption.option_number - 1)
  }
  return 'N/A'
}

const getStudentOptionLabel = (question) => {
  const selectedOption = question.options.find(opt => opt.id === question.selected_option_id)
  if (selectedOption) {
    return String.fromCharCode(65 + (selectedOption.option_number - 1))
  }
  
  // Enhanced fallback: if we have answer_text but no selected_option_id, try comprehensive matching
  if (question.answer_text && question.options.length > 0) {
    const answerText = question.answer_text.toString().toLowerCase().trim()
    
    // Method 1: Check if it's a number (like "1", "2", etc.)
    if (/^\d+$/.test(answerText)) {
      const optionNumber = parseInt(answerText)
      const matchedOption = question.options.find(opt => opt.option_number === optionNumber)
      if (matchedOption) {
        return String.fromCharCode(65 + (matchedOption.option_number - 1))
      }
    }
    
    // Method 2: Check if it's already a letter (A, B, C, etc.)
    if (/^[a-zA-Z]$/.test(answerText)) {
      return answerText.toUpperCase()
    }
    
    // Method 3: Try to match by option text
    const textMatchedOption = question.options.find(opt => 
      opt.option_text.toLowerCase().trim() === answerText
    )
    if (textMatchedOption) {
      return String.fromCharCode(65 + (textMatchedOption.option_number - 1))
    }
    
    // If no match found, show the raw answer with indication
    return `"${question.answer_text}"`
  }
  
  return 'No answer'
}

const saveGrade = async () => {
  try {
    if (!selectedSubmission.value) return

    savingGrade.value = true
    const finalScore = calculateReviewScore()
    const finalPercentage = calculateReviewPercentage()

    const { error: updateError } = await supabase
      .from('quiz_attempts')
      .update({
        total_score: finalScore,
        percentage: finalPercentage,
        status: 'graded',
        teacher_feedback: reviewFeedback.value,
        manually_reviewed: true,
        graded_by: teacherId.value,
        graded_at: new Date().toISOString()
      })
      .eq('id', selectedSubmission.value.id)

    if (updateError) throw updateError

    const answerUpdates = reviewQuestions.value
      .filter(q => q.student_answer_id)
      .map(q => ({
        id: q.student_answer_id,
        teacher_comment: q.teacherComment || null,
        points_earned: parseFloat(q.manualPoints) || 0
      }))

    if (answerUpdates.length > 0) {
      for (const update of answerUpdates) {
        await supabase
          .from('student_answers')
          .update({
            teacher_comment: update.teacher_comment,
            points_earned: update.points_earned
          })
          .eq('id', update.id)
      }
    }

    await supabase
      .from('quiz_results')
      .upsert({
        quiz_id: selectedSubmission.value.quiz_id,
        student_id: selectedSubmission.value.student_id,
        best_attempt_id: selectedSubmission.value.id,
        best_score: finalScore,
        best_percentage: finalPercentage,
        total_attempts: selectedSubmission.value.attempt_number,
        latest_attempt_date: selectedSubmission.value.submitted_at,
        status: 'graded',
        finalized: true,
        visible_to_student: true
      }, {
        onConflict: 'quiz_id,student_id',
        ignoreDuplicates: false
      })

    const index = submissions.value.findIndex(s => s.id === selectedSubmission.value.id)
    if (index !== -1) {
      submissions.value[index].status = 'graded'
      submissions.value[index].total_score = finalScore
      submissions.value[index].percentage = finalPercentage
      submissions.value[index].teacher_feedback = reviewFeedback.value
    }

    closeReviewModal()
    alert('Grade saved successfully!')
  } catch (err) {
    console.error('Error saving grade:', err)
    alert(`Error saving grade: ${err.message}`)
  } finally {
    savingGrade.value = false
  }
}

const sortBy = (field) => {
  if (sortField.value === field) {
    sortDirection.value = sortDirection.value === 'asc' ? 'desc' : 'asc'
  } else {
    sortField.value = field
    sortDirection.value = 'asc'
  }
}

const getSortIcon = (field) => {
  if (sortField.value !== field) return ''
  return sortDirection.value === 'asc' ? 'fa-sort-up' : 'fa-sort-down'
}

const getInitials = (name) => {
  if (!name) return '?'
  return name.split(' ').map(n => n[0]).join('').toUpperCase().substring(0, 2)
}

const formatDate = (dateString) => {
  if (!dateString) return 'N/A'
  return new Date(dateString).toLocaleDateString()
}

const formatTime = (dateString) => {
  if (!dateString) return 'N/A'
  return new Date(dateString).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
}

const getStatusText = (status) => {
  const map = {
    'in_progress': 'In Progress',
    'submitted': 'Pending Review',
    'graded': 'Graded',
    'reviewed': 'Reviewed'
  }
  return map[status] || status
}

const getScoreClass = (percentage) => {
  if (percentage >= 90) return 'excellent'
  if (percentage >= 80) return 'good'
  if (percentage >= 70) return 'average'
  return 'needs-improvement'
}

const getSubjectIconSvg = (subjectName) => {
  const name = subjectName.toLowerCase()
  
  if (name.includes('math') || name.includes('algebra') || name.includes('geometry') || name.includes('calculus')) {
    return '<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor"><path d="M19,3H5C3.89,3 3,3.89 3,5V19A2,2 0 0,0 5,21H19A2,2 0 0,0 21,19V5C21,3.89 20.1,3 19,3M7,7H9V9H7V7M7,11H9V13H7V11M7,15H9V17H7V15M11,7H17V9H11V7M11,11H17V13H11V11M11,15H17V17H11V15Z" /></svg>'
  }
  
  if (name.includes('english') || name.includes('literature') || name.includes('writing')) {
    return '<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor"><path d="M14,2H6A2,2 0 0,0 4,4V20A2,2 0 0,0 6,22H18A2,2 0 0,0 20,20V8L14,2M18,20H6V4H13V9H18V20Z" /></svg>'
  }
  
  if (name.includes('science') || name.includes('biology') || name.includes('chemistry') || name.includes('physics')) {
    return '<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor"><path d="M5,13H6.5L9.5,6H14.5L17.5,13H19L15.5,4H8.5L5,13M15,16A1,1 0 0,1 16,17A1,1 0 0,1 15,18A1,1 0 0,1 14,17A1,1 0 0,1 15,16M15,10A1,1 0 0,1 16,11A1,1 0 0,1 15,12A1,1 0 0,1 14,11A1,1 0 0,1 15,10Z" /></svg>'
  }
  
  if (name.includes('filipino') || name.includes('tagalog')) {
    return '<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor"><path d="M12.87,15.07L15.28,17.48L17.48,15.28L15.07,12.87L17.48,10.46L15.28,8.26L12.87,10.67L10.46,8.26L8.26,10.46L10.67,12.87L8.26,15.28L10.46,17.48L12.87,15.07M17.5,12A1.5,1.5 0 0,1 16,10.5A1.5,1.5 0 0,1 17.5,9A1.5,1.5 0 0,1 19,10.5A1.5,1.5 0 0,1 17.5,12M10,10.5C10,9.67 9.33,9 8.5,9C7.67,9 7,9.67 7,10.5C7,11.33 7.67,12 8.5,12C9.33,12 10,11.33 10,10.5M12,14C12,11.34 14.33,9.2 17.35,9.04C17.75,6.27 15.41,4 12.5,4C9.59,4 7.25,6.27 7.65,9.04C10.67,9.2 13,11.34 13,14H12Z" /></svg>'
  }
  
  if (name.includes('history') || name.includes('social')) {
    return '<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor"><path d="M13,3V9H21V3M13,21H21V11H13M3,21H11V15H3M3,13H11V3H3V13Z" /></svg>'
  }
  
  if (name.includes('art') || name.includes('music') || name.includes('creative')) {
    return '<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor"><path d="M12,3V13.55C11.41,13.21 10.73,13 10,13A4,4 0 0,0 6,17A4,4 0 0,0 10,21A4,4 0 0,0 14,17V7H18V3H12Z" /></svg>'
  }
  
  if (name.includes('pe') || name.includes('physical') || name.includes('sports')) {
    return '<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor"><path d="M6.5,2A7.5,7.5 0 0,1 14,9.5C14,10.87 13.61,12.14 12.94,13.22L19.07,19.36L17.66,20.78L11.5,14.63C10.42,15.28 9.17,15.67 7.83,15.67A7.67,7.67 0 0,1 0.17,8A7.5,7.5 0 0,1 6.5,2M6.5,4A5.5,5.5 0 0,0 1,9.5A5.5,5.5 0 0,0 6.5,15A5.5,5.5 0 0,0 12,9.5A5.5,5.5 0 0,0 6.5,4Z" /></svg>'
  }
  
  if (name.includes('computer') || name.includes('ict') || name.includes('programming') || name.includes('technology')) {
    return '<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor"><path d="M4,6H20V16H4M20,18A2,2 0 0,0 22,16V6C22,4.89 21.1,4 20,4H4C2.89,4 2,4.89 2,6V16A2,2 0 0,0 4,18H0V20H24V18H20Z" /></svg>'
  }
  
  return '<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor"><path d="M19 3H5C3.9 3 3 3.9 3 5V19C3.9 19 5 18.1 5 17V9H19C20.1 9 21 8.1 21 7V5C21 3.9 20.1 3 19 3Z" /></svg>'
}

const getSubjectIconColor = (subjectName) => {
  const name = subjectName.toLowerCase()
  
  if (name.includes('math') || name.includes('algebra') || name.includes('geometry') || name.includes('calculus')) {
    return '#2563eb'
  }
  
  if (name.includes('english') || name.includes('literature') || name.includes('writing')) {
    return '#dc2626'
  }
  
  if (name.includes('science') || name.includes('biology') || name.includes('chemistry') || name.includes('physics')) {
    return '#16a34a'
  }
  
  if (name.includes('filipino') || name.includes('tagalog')) {
    return '#ca8a04'
  }
  
  if (name.includes('history') || name.includes('social')) {
    return '#9333ea'
  }
  
  if (name.includes('art') || name.includes('music') || name.includes('creative')) {
    return '#ec4899'
  }
  
  if (name.includes('pe') || name.includes('physical') || name.includes('sports')) {
    return '#ea580c'
  }
  
  if (name.includes('computer') || name.includes('ict') || name.includes('programming') || name.includes('technology')) {
    return '#0891b2'
  }
  
  return '#3D8D7A'
}

const getSubjectTypeColor = (type) => {
  return getSubjectIconColor(type)
}

const getSubjectTypeIcon = (type) => {
  return getSubjectIconSvg(type)
}

// Navbar dropdown methods
const toggleNotifDropdown = () => {
  showNotifDropdown.value = !showNotifDropdown.value
  showProfileDropdown.value = false
}

const toggleProfileDropdown = () => {
  showProfileDropdown.value = !showProfileDropdown.value
  showNotifDropdown.value = false
}

const handleNotificationClick = (notif) => {
  console.log('Notification clicked:', notif)
}

// Logout confirmation modal functions
const openLogoutModal = () => {
  showLogoutModal.value = true
}

const closeLogoutModal = () => {
  showLogoutModal.value = false
}

const confirmLogout = () => {
  console.log('🚪 Logging out...')
  
  // Clear storage immediately
  localStorage.clear()
  sessionStorage.clear()
  
  // Sign out from Supabase (don't wait)
  supabase.auth.signOut().catch(err => console.log('Signout error:', err))
  
  // Immediate redirect - no waiting!
  setTimeout(() => {
    window.location.assign('/login')
  }, 100)
  
  console.log('✅ Logout initiated')
}

const logout = () => {
  openLogoutModal()
}

const scrollToTop = () => {
  window.scrollTo({ top: 0, behavior: 'smooth' })
}

// Excel Export Function
const exportToExcel = () => {
  if (!selectedSectionId.value || !students.value.length) {
    alert('Please select a section with students to export')
    return
  }

  // Prepare data for Excel export
  const exportData = []
  
  // Header row
  const headers = ['Student Name', 'Student ID']
  assessments.value.forEach(assessment => {
    headers.push(`${assessment.title} (${assessment.max_score}pts)`)
  })
  headers.push('Total', 'Percentage')
  exportData.push(headers)
  
  // Student data rows
  students.value.forEach(student => {
    const row = [student.full_name, student.student_id || 'N/A']
    
    // Assessment scores
    assessments.value.forEach(assessment => {
      const score = getStudentScore(student.id, assessment.id)
      row.push(score !== null ? score : '--')
    })
    
    // Total and percentage
    row.push(getStudentTotal(student.id))
    row.push(`${getStudentTotalPercentage(student.id)}%`)
    
    exportData.push(row)
  })
  
  // Create workbook and worksheet
  const wb = XLSX.utils.book_new()
  const ws = XLSX.utils.aoa_to_sheet(exportData)
  
  // Set column widths
  const colWidths = [
    { wch: 25 }, // Student Name
    { wch: 15 }, // Student ID
  ]
  assessments.value.forEach(() => {
    colWidths.push({ wch: 12 }) // Assessment columns
  })
  colWidths.push({ wch: 10 }, { wch: 12 }) // Total, Percentage
  
  ws['!cols'] = colWidths
  
  // Add worksheet to workbook
  const sheetName = `${currentSectionInfo.value.name || 'Gradebook'}_${new Date().toISOString().split('T')[0]}`
  XLSX.utils.book_append_sheet(wb, ws, sheetName)
  
  // Download file
  const fileName = `${currentSectionInfo.value.name || 'Gradebook'}_${new Date().toISOString().split('T')[0]}.xlsx`
  XLSX.writeFile(wb, fileName)
  
  console.log('✅ Gradebook exported to Excel:', fileName)
}

watch([searchQuery, selectedStatus], () => {
  currentPage.value = 1
})

onMounted(async () => {
  const success = await getTeacherInfo()
  if (success) {
    await fetchSubjects()
    
    // Load teacher name
    if (teacherId.value) {
      try {
        const { data: teacher, error } = await supabase
          .from('teachers')
          .select('full_name')
          .eq('id', teacherId.value)
          .single()
          
        if (!error && teacher) {
          fullName.value = teacher.full_name || 'Teacher'
          console.log('✅ Teacher loaded:', { id: teacherId.value, name: fullName.value })
        }
      } catch (err) {
        console.warn('Failed to load teacher name:', err)
      }
    }
    
    // Add scroll event listener for scroll-to-top button
    const handleScroll = () => {
      showScrollTop.value = window.scrollY > 300
    }
    window.addEventListener('scroll', handleScroll)
    
    // Set up real-time subscription for gradebook updates
    console.log('🔴 Setting up real-time subscriptions...')
    
    const subscription = supabase
      .channel('gradebook_realtime')
      .on('postgres_changes', {
        event: '*',
        schema: 'public',
        table: 'quiz_attempts'
      }, async (payload) => {
        console.log('🔄 Quiz attempt change detected:', payload.eventType)
        
        // Refresh gradebook data if viewing a section
        if (selectedSectionId.value) {
          await fetchGradebookData(selectedSectionId.value)
        }
      })
      .on('postgres_changes', {
        event: '*',
        schema: 'public',
        table: 'quizzes'
      }, async (payload) => {
        console.log('🔄 Quiz change detected:', payload.eventType)
        
        // Refresh gradebook data if viewing a section
        if (selectedSectionId.value) {
          await fetchGradebookData(selectedSectionId.value)
        }
      })
      .subscribe((status) => {
        console.log('📡 Subscription status:', status)
        if (status === 'SUBSCRIBED') {
          console.log('✅ Real-time subscriptions active!')
        }
      })
    
    // Cleanup on unmount
    return () => {
      console.log('🧹 Cleaning up subscriptions...')
      subscription.unsubscribe()
      window.removeEventListener('scroll', handleScroll)
    }
  } else {
    loading.value = false
  }
})
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

/* Reset and Hide Parent Layouts */
body, html {
  overflow-x: hidden !important;
}

.dashboard-container {
  display: flex;
  min-height: 100vh;
  background: #f8fafc;
  font-family: 'Inter', sans-serif;
}
.dark .dashboard-container {
  background: #0f172a;
}

/* Sidebar Navigation - Simple Outlined Icons Only, Single Color, Active Highlight */
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

.sidebar-item.active {
  background: rgba(255,255,255,0.15);
  border: 2px solid #fff;
}

.sidebar-item:hover {
  background: rgba(255,255,255,0.22);
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
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

/* Scroll to Top Button */
.scroll-to-top {
  position: fixed;
  bottom: 2rem;
  right: 2rem;
  width: 48px;
  height: 48px;
  background: #3D8D7A;
  color: white;
  border: none;
  border-radius: 50%;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 4px 12px rgba(61, 141, 122, 0.3);
  transition: all 0.2s ease;
  z-index: 1000;
}

.scroll-to-top:hover {
  background: #2d6a5a;
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(61, 141, 122, 0.4);
}

/* Main Content */
.main-content {
  margin-left: 80px;
  margin-top: 64px;
  padding: 1.5rem;
  width: calc(100% - 80px);
  min-height: calc(100vh - 64px);
  max-height: calc(100vh - 64px);
  overflow-y: auto;
  overflow-x: hidden;
  scroll-behavior: smooth;
  position: relative;
  background: #f8fafc;
  padding-bottom: 2rem;
}

/* Uniform Scrollbar */
.main-content::-webkit-scrollbar {
  width: 12px;
}

.main-content::-webkit-scrollbar-track {
  background: #f1f5f9;
  border-radius: 16px;
}

.main-content::-webkit-scrollbar-thumb {
  background: linear-gradient(135deg, #3D8D7A, #20c997);
  border-radius: 16px;
  border: 2px solid #f1f5f9;
  transition: all 0.3s ease;
}

.main-content::-webkit-scrollbar-thumb:hover {
  background: linear-gradient(135deg, #2a6e61, #1a9d7c);
  transform: scale(1.1);
}

.dark .main-content {
  background: #151821;
}

.dark .main-content::-webkit-scrollbar-track {
  background: #1e293b;
}

.dark .main-content::-webkit-scrollbar-thumb {
  border-color: #1e293b;
}

/* Content Wrapper */
.content-wrapper {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
  width: 100%;
  max-width: 1200px;
  margin: 0 auto;
}

/* Page Header */
.page-header {
  background: white;
  border-radius: 16px;
  padding: 1.5rem 2rem;
  margin-bottom: 1.5rem;
  border: 1px solid #e2e8f0;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
  transition: all 0.2s ease;
}

.page-header:hover {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
  border-color: #3D8D7A;
  transform: translateY(-1px);
}

.page-header {
  animation: fadeIn 0.5s ease-out;
}

.dark .page-header {
  background: #23272b;
  border: 1px solid #20c997;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.25);
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
  box-shadow: 0 2px 8px rgba(61, 141, 122, 0.2);
}

.header-title {
  font-size: 1.75rem;
  font-weight: 700;
  color: #1e293b;
  margin-bottom: 0.25rem;
  font-weight: 700;
  color: #1e293b;
  margin-bottom: 0.25rem;
}

.header-subtitle {
  font-size: 0.95rem;
  color: #64748b;
  font-size: 0.95rem;
  color: #64748b;
}

/* Search Box in Navbar */
.search-box {
  position: relative;
  min-width: 280px;
}

.search-box svg {
  position: absolute;
  left: 1rem;
  top: 50%;
  transform: translateY(-50%);
  color: rgba(255, 255, 255, 0.7);
}

.search-box input {
  width: 100%;
  padding: 0.75rem 1rem 0.75rem 2.5rem;
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 8px;
  font-size: 0.875rem;
  background: rgba(255, 255, 255, 0.1);
  color: white;
  transition: all 0.2s;
}

.search-box input::placeholder {
  color: rgba(255, 255, 255, 0.6);
}

.search-box input:focus {
  outline: none;
  border-color: rgba(255, 255, 255, 0.4);
  background: rgba(255, 255, 255, 0.2);
  box-shadow: 0 0 0 3px rgba(255, 255, 255, 0.1);
}

.gradebook-container {
  min-height: 100vh;
  background: #FBFFE4;
  padding: 1.5rem;
  font-family: 'Inter', sans-serif;
}
.dark .gradebook-container {
  background: #181c20;
}

/* Header */
.header-card {
  background: white;
  border: 1.5px solid #3D8D7A;
  border-radius: 16px;
  padding: 1.5rem;
  margin-bottom: 1.5rem;
  box-shadow: 0 2px 8px rgba(61, 141, 122, 0.1);
}
.dark .header-card {
  background: #23272b;
  border: 1.5px solid #A3D1C6;
  box-shadow: 0 2px 8px rgba(163, 209, 198, 0.1);
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
  background: #3D8D7A;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
}

.header-title {
  font-size: 1.5rem;
  font-weight: 800;
  color: #1f2937;
  margin-bottom: 0.25rem;
}
.dark .header-title {
  color: #A3D1C6;
}

.header-subtitle {
  font-size: 0.875rem;
  color: #6b7280;
}
.dark .header-subtitle {
  color: #A3D1C6;
}

.header-actions {
  display: flex;
  gap: 1rem;
  align-items: center;
  flex-wrap: wrap;
}

.search-box {
  position: relative;
  min-width: 280px;
}

.search-box svg {
  position: absolute;
  left: 1rem;
  top: 50%;
  transform: translateY(-50%);
  color: #64748b;
}

.search-box input {
  width: 100%;
  padding: 0.75rem 1rem 0.75rem 2.5rem;
  border: 1px solid #A3D1C6;
  border-radius: 8px;
  font-size: 0.875rem;
  background: white;
  transition: all 0.2s;
}
.dark .search-box input {
  background: #23272b;
  border-color: #3D8D7A;
  color: #A3D1C6;
}

.search-box input:focus {
  outline: none;
  border-color: #3D8D7A;
  box-shadow: 0 0 0 3px rgba(61, 141, 122, 0.1);
}

.grade-btn {
  background: #3D8D7A;
  color: white;
  border: none;
  border-radius: 8px;
  padding: 0.75rem 1rem;
  font-size: 0.875rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  box-shadow: 0 1px 3px rgba(0,0,0,0.1);
}

.grade-btn:hover:not(:disabled) {
  background: #2d6b5c;
  box-shadow: 0 2px 6px rgba(0,0,0,0.15);
  transform: translateY(-1px);
}

.grade-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
  transform: none;
}

.refresh-btn {
  min-width: auto;
}

.spinning {
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

@keyframes pulse {
  0%, 100% { 
    transform: scale(1);
    opacity: 0.3;
  }
  50% { 
    transform: scale(1.05);
    opacity: 0.1;
  }
}

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

@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

/* Enhanced Subject Filter Buttons */
.subject-filters {
  background: white;
  border-radius: 16px;
  padding: 2rem;
  border: 1px solid #e2e8f0;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
  margin-bottom: 1.5rem;
  transition: all 0.2s ease;
}

.subject-filters:hover {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
  border-color: #3D8D7A;
  transform: translateY(-1px);
}

.dark .subject-filters {
  background: #23272b;
  border: 1px solid #20c997;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.25);
}

.dark .subject-filters:hover {
  border-color: #34d399;
  box-shadow: 0 4px 12px rgba(32, 201, 151, 0.15);
}

.filter-header {
  border-bottom: 1px solid rgba(61, 141, 122, 0.1);
  padding-bottom: 1rem;
}
.dark .filter-header {
  border-bottom-color: #3D8D7A;
}

.filter-title {
  font-size: 1.5rem;
  font-weight: 700;
  color: #1f2937;
  margin: 0 0 0.5rem 0;
}
.dark .filter-title {
  color: #f3f4f6;
}

.filter-subtitle {
  font-size: 0.95rem;
  color: #6b7280;
  margin: 0;
  font-weight: 500;
  line-height: 1.5;
}
.dark .filter-subtitle {
  color: #9ca3af;
}

.filter-buttons {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1rem;
  margin-top: 1.5rem;
}

.filter-btn.modern {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.875rem 1.25rem;
  border: 2px solid #e5e7eb;
  background: white;
  border-radius: 12px;
  cursor: pointer;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  font-size: 0.875rem;
  font-weight: 600;
  color: #374151;
  position: relative;
  overflow: hidden;
}
.dark .filter-btn.modern {
  background: #374151;
  border-color: #4b5563;
  color: #d1d5db;
}

.filter-btn.modern:hover {
  background: #f9fafb;
  border-color: var(--filter-color, #3D8D7A);
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
}
.dark .filter-btn.modern:hover {
  background: #4b5563;
  border-color: var(--filter-color, #A3D1C6);
}

.filter-btn.modern.active {
  background: var(--filter-color, #3D8D7A);
  border-color: var(--filter-color, #3D8D7A);
  color: white;
  box-shadow: 0 4px 15px rgba(61, 141, 122, 0.3);
  transform: translateY(-1px);
}

.filter-icon {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 20px;
  height: 20px;
  flex-shrink: 0;
}

.filter-text {
  font-weight: 600;
}

/* All button special styling */
.filter-btn.modern:first-child {
  --filter-color: #3D8D7A;
}

/* Breadcrumb Navigation */
.breadcrumb-nav {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 1rem 1.5rem;
  margin-bottom: 1.5rem;
  background: white;
  border-radius: 12px;
  border: 1px solid #e2e8f0;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
  transition: all 0.2s ease;
}

.breadcrumb-nav:hover {
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.08);
  border-color: #3D8D7A;
}

.dark .breadcrumb-nav {
  background: #23272b;
  border: 1px solid #374151;
}

.dark .breadcrumb-nav:hover {
  border-color: #20c997;
}

.breadcrumb-btn {
  background: none;
  border: none;
  color: #3D8D7A;
  cursor: pointer;
  padding: 0.5rem 0.75rem;
  border-radius: 8px;
  font-weight: 600;
  transition: all 0.2s ease;
  font-size: 1rem;
  font-weight: 600;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  transition: all 0.2s;
}
.dark .breadcrumb-btn {
  color: #A3D1C6;
}

.breadcrumb-btn:hover {
  background: #B3D8A8;
  color: #1f2937;
}
.dark .breadcrumb-btn:hover {
  background: #3D8D7A;
  color: white;
}

.breadcrumb-current {
  color: #1f2937;
  font-weight: 600;
  font-size: 1rem;
  padding: 0.75rem 1rem;
}
.dark .breadcrumb-current {
  color: #A3D1C6;
}

.breadcrumb-separator {
  color: #6b7280;
  font-size: 1rem;
}
.dark .breadcrumb-separator {
  color: #A3D1C6;
}

/* Loading and Error States */
.loading-container, .error-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 400px;
  color: #6b7280;
}
.dark .loading-container {
  color: #A3D1C6;
}

.error-container {
  color: #dc2626;
  text-align: center;
  padding: 2rem;
}

.error-container svg {
  margin-bottom: 1rem;
    margin-bottom: -20rem; 
}

.error-container h3 {
  font-size: 1.25rem;
  margin-bottom: 0.5rem;
  color: #991b1b;
}

.spinner-large {
  width: 40px;
  height: 40px;
  border: 4px solid #B3D8A8;
  border-top: 4px solid #3D8D7A;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin-bottom: 1rem;
}

/* Enhanced Main Content */
.content-wrapper {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
  width: 100%;
}

.content-card.modern {
  margin-top: 0;
  background: white;
  border-radius: 16px;
  padding: 2rem;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
  border: 1px solid #e2e8f0;
  max-width: 1200px;
  width: 100%;
  margin: 0 auto 1.5rem auto;
  position: relative;
  box-sizing: border-box;
  min-height: 120px;
  transition: all 0.2s ease;
}

.content-card.modern:hover {
  box-shadow: 0 8px 24px rgba(61, 141, 122, 0.12);
  border-color: #3D8D7A;
  transform: translateY(-2px);
}

.content-card.modern {
  animation: slideUp 0.6s ease-out;
}

.dark .content-card.modern {
  background: #23272b;
  border: 1px solid #20c997;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.25);
}

.dark .content-card.modern:hover {
  box-shadow: 0 8px 24px rgba(32, 201, 151, 0.2);
  border-color: #34d399;
}

.card-header.enhanced {
  padding: 0;
  background: transparent;
  border-bottom: none;
  display: none;
}
/* Removed duplicated and misplaced CSS block causing errors */
.dark .card-title-section h3 {
  background: linear-gradient(135deg, #A3D1C6, #34d399);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.card-title-section .card-desc {
  margin-top: 0.5rem;
  color: #64748b;
  font-size: 1rem;
  font-weight: 400;
  letter-spacing: 0.01em;
  line-height: 1.5;
}

.card-stats .stat-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 1rem;
  background: white;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
  min-width: 80px;
}
.dark .card-stats .stat-item {
  background: #1f2937;
}

.card-stats .stat-number {
  font-size: 1.75rem;
  font-weight: 800;
  color: #3D8D7A;
  line-height: 1;
}
.dark .card-stats .stat-number {
  color: #A3D1C6;
}

.card-stats .stat-label {
  font-size: 0.75rem;
  color: #6b7280;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin-top: 0.25rem;
}
.dark .card-stats .stat-label {
  color: #9ca3af;
}

/* Enhanced Stats Grid */
.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 1rem;
  margin-bottom: 1.5rem;
  margin-top: 0.25rem;
}

/* Modern Stat Cards */
.stat-card.modern {
  background: linear-gradient(135deg, #ffffff 0%, #fefefe 100%);
  border-radius: 16px;
  padding: 1.5rem;
  display: flex;
  align-items: center;
  gap: 1rem;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.06);
  border: 1px solid rgba(255, 255, 255, 0.2);
  position: relative;
  overflow: hidden;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  backdrop-filter: blur(10px);
}

.dark .stat-card.modern {
  background: linear-gradient(135deg, #1f2937 0%, #374151 100%);
  border: 1px solid rgba(75, 85, 99, 0.3);
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
}

/* Hover Effects */
.stat-card.modern:hover {
  transform: translateY(-8px) scale(1.02);
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.15);
}

.dark .stat-card.modern:hover {
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.4);
}

/* Card Type Specific Styling */
.stat-card.modern.pending {
  border-left: 4px solid #f59e0b;
}

.stat-card.modern.pending:hover {
  box-shadow: 0 20px 60px rgba(245, 158, 11, 0.2);
}

/* Unified Gradebook Header */
.gradebook-header {
  background: white;
  border-radius: 16px;
  padding: 1.5rem 2rem;
  margin-bottom: 1.5rem;
  border: 1px solid #e2e8f0;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
  transition: all 0.2s ease;
}

.gradebook-header:hover {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
  border-color: #3D8D7A;
  transform: translateY(-1px);
}

.dark .gradebook-header {
  background: #23272b;
  border: 1px solid #20c997;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.25);
}

/* Section Selector */
.section-selector {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.section-selector label {
  font-size: 0.875rem;
  font-weight: 600;
  color: #1e293b;
  min-width: fit-content;
}

.dark .section-selector label {
  color: #f1f5f9;
}

.section-select {
  padding: 0.625rem 1rem;
  border: 2px solid #e2e8f0;
  border-radius: 8px;
  font-size: 0.875rem;
  font-weight: 500;
  background: white;
  color: #1e293b;
  min-width: 280px;
  transition: all 0.2s;
  cursor: pointer;
}

.section-select:hover {
  border-color: #3D8D7A;
}

.section-select:focus {
  outline: none;
  border-color: #3D8D7A;
  box-shadow: 0 0 0 3px rgba(61, 141, 122, 0.1);
}

.dark .section-select {
  background: #374151;
  border-color: #4b5563;
  color: #f1f5f9;
}

/* Loading and Empty States */
.loading-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 3rem;
  color: #64748b;
}

.spinner-large {
  width: 40px;
  height: 40px;
  border: 4px solid #e2e8f0;
  border-top: 4px solid #3D8D7A;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin-bottom: 1rem;
}

.error-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 3rem;
  color: #dc2626;
  text-align: center;
}

.no-section-state {
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

.no-section-state .empty-icon {
  margin-bottom: 1.5rem;
  color: #94a3b8;
}

.no-section-state h3 {
  font-size: 1.5rem;
  font-weight: 600;
  color: #1e293b;
  margin-bottom: 0.5rem;
}

.no-section-state p {
  color: #64748b;
  font-size: 1rem;
}

.dark .no-section-state {
  background: #23272b;
  border-color: #374151;
}

.dark .no-section-state h3 {
  color: #f1f5f9;
}

.dark .no-section-state p {
  color: #94a3b8;
}

/* Excel-Style Gradebook */
.gradebook-main {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

/* Mini Analytics Panel */
.analytics-panel {
  background: white;
  border-radius: 12px;
  padding: 1.5rem;
  border: 1px solid #e2e8f0;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
  margin-bottom: 1rem;
}

.analytics-header {
  display: flex;
  justify-content: between;
  align-items: center;
  margin-bottom: 1rem;
}

.analytics-header h3 {
  font-size: 1.125rem;
  font-weight: 600;
  color: #1e293b;
  margin: 0;
}

.student-count {
  font-size: 0.875rem;
  color: #64748b;
  background: #f1f5f9;
  padding: 0.25rem 0.75rem;
  border-radius: 12px;
  font-weight: 500;
}

.analytics-stats {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
  gap: 1rem;
}

.stat-mini {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 1rem;
  background: #f8fafc;
  border-radius: 8px;
  border: 1px solid #e2e8f0;
}

.stat-mini .stat-icon {
  width: 32px;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #3D8D7A;
  color: white;
  border-radius: 6px;
}

.stat-mini .stat-content {
  display: flex;
  flex-direction: column;
}

.stat-mini .stat-value {
  font-size: 1.25rem;
  font-weight: 700;
  color: #1e293b;
  line-height: 1;
}

.stat-mini .stat-label {
  font-size: 0.75rem;
  color: #64748b;
  font-weight: 500;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.dark .analytics-panel {
  background: #23272b;
  border-color: #374151;
}

.dark .analytics-header h3 {
  color: #f1f5f9;
}

.dark .student-count {
  background: #374151;
  color: #9ca3af;
}

.dark .stat-mini {
  background: #374151;
  border-color: #4b5563;
}

.dark .stat-mini .stat-value {
  color: #f1f5f9;
}

.dark .stat-mini .stat-label {
  color: #9ca3af;
}

/* Excel-Style Gradebook Table Container */
.gradebook-container {
  background: white;
  border-radius: 12px;
  border: 1px solid #e2e8f0;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
  overflow: hidden;
}

.gradebook-scroll {
  overflow: auto;
  max-height: 70vh;
}

.gradebook-table {
  width: 100%;
  border-collapse: separate;
  border-spacing: 0;
  font-size: 0.875rem;
}

/* Sticky Headers */
.gradebook-table thead th {
  position: sticky;
  top: 0;
  z-index: 10;
  background: #f8fafc;
  border-bottom: 2px solid #e2e8f0;
  padding: 1rem 0.75rem;
  text-align: left;
  font-weight: 600;
  color: #374151;
  white-space: nowrap;
}

.gradebook-table thead th.sticky-col {
  position: sticky;
  left: 0;
  z-index: 11;
  background: #f1f5f9;
  border-right: 2px solid #e2e8f0;
}

/* Table Headers */
.header-content {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}

.assessment-title {
  font-weight: 600;
  color: #1e293b;
  font-size: 0.875rem;
}

.assessment-info {
  display: flex;
  gap: 0.5rem;
  font-size: 0.75rem;
  color: #64748b;
}

.assessment-type {
  background: #3D8D7A;
  color: white;
  padding: 0.125rem 0.5rem;
  border-radius: 4px;
  font-weight: 500;
}

.assessment-points {
  font-weight: 500;
}

/* Student Rows */
.student-row {
  border-bottom: 1px solid #f1f5f9;
  transition: all 0.2s;
}

.student-row:hover {
  background: #f8fafc;
}

.student-row.expanded {
  background: #f0f9ff;
  border-color: #3D8D7A;
}

.student-cell {
  position: sticky;
  left: 0;
  z-index: 5;
  background: white;
  border-right: 1px solid #e2e8f0;
  padding: 0.75rem;
  min-width: 200px;
}

.student-row:hover .student-cell {
  background: #f8fafc;
}

.student-row.expanded .student-cell {
  background: #f0f9ff;
}

.student-info {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  cursor: pointer;
}

.student-avatar {
  width: 36px;
  height: 36px;
  background: #3D8D7A;
  color: white;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 600;
  font-size: 0.875rem;
}

.student-details {
  flex: 1;
  min-width: 0;
}

.student-name {
  font-weight: 600;
  color: #1e293b;
  font-size: 0.875rem;
}

.student-id {
  font-size: 0.75rem;
  color: #64748b;
}

.expand-btn {
  background: none;
  border: none;
  color: #64748b;
  cursor: pointer;
  padding: 0.25rem;
  border-radius: 4px;
  transition: all 0.2s;
}

.expand-btn:hover {
  background: #f1f5f9;
  color: #3D8D7A;
}

.expand-btn.rotated {
  transform: rotate(90deg);
  color: #3D8D7A;
}

/* Score Cells */
.score-cell {
  padding: 0.75rem;
  border-right: 1px solid #f1f5f9;
  text-align: center;
  position: relative;
}

.score-input-wrapper {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.25rem;
}

.score-input {
  width: 70px;
  padding: 0.375rem 0.5rem;
  border: 1px solid #d1d5db;
  border-radius: 4px;
  text-align: center;
  font-size: 0.875rem;
  font-weight: 500;
}

.score-input:focus {
  outline: none;
  border-color: #3D8D7A;
  box-shadow: 0 0 0 2px rgba(61, 141, 122, 0.1);
}

.score-input.manual {
  background: #fefce8;
  border-color: #facc15;
}

.score-display {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.125rem;
}

.score-value {
  font-weight: 600;
  font-size: 0.875rem;
}

.score-max {
  font-size: 0.75rem;
  color: #64748b;
}

.pending-indicator {
  position: absolute;
  top: 0.25rem;
  right: 0.25rem;
  color: #f59e0b;
  animation: pulse 2s infinite;
}

/* Score Color Classes */
.excellent .score-value { color: #059669; }
.good .score-value { color: #0891b2; }
.average .score-value { color: #d97706; }
.needs-improvement .score-value { color: #dc2626; }

/* Total Column */
.total-cell {
  padding: 0.75rem;
  text-align: center;
  background: #f8fafc;
  border-left: 2px solid #e2e8f0;
  font-weight: 600;
}

.total-score {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.25rem;
}

.total-value {
  font-size: 1rem;
  font-weight: 700;
}

.total-max {
  font-size: 0.75rem;
  color: #64748b;
}

.total-percentage {
  font-size: 0.75rem;
  font-weight: 600;
  padding: 0.125rem 0.5rem;
  border-radius: 12px;
  background: #f1f5f9;
  color: #64748b;
}

.total-score.excellent .total-percentage {
  background: #dcfce7;
  color: #059669;
}

.total-score.good .total-percentage {
  background: #cffafe;
  color: #0891b2;
}

.total-score.average .total-percentage {
  background: #fed7aa;
  color: #d97706;
}

.total-score.needs-improvement .total-percentage {
  background: #fecaca;
  color: #dc2626;
}

/* Student History Panel */
.student-history-row {
  background: #f0f9ff;
  border-bottom: 2px solid #3D8D7A;
}

.history-cell {
  padding: 0;
}

.student-history-panel {
  padding: 1.5rem;
  background: #f0f9ff;
  border-left: 4px solid #3D8D7A;
}

.history-header {
  margin-bottom: 1rem;
}

.history-header h4 {
  font-size: 1.125rem;
  font-weight: 600;
  color: #1e293b;
  margin: 0;
}

.history-content {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1rem;
}

.history-item {
  background: white;
  padding: 1rem;
  border-radius: 8px;
  border: 1px solid #e2e8f0;
}

.history-assessment {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.assessment-name {
  font-weight: 600;
  color: #1e293b;
  font-size: 0.875rem;
}

.assessment-details {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
  font-size: 0.8125rem;
}

.score-info {
  color: #374151;
  font-weight: 500;
}

.percentage-info {
  color: #64748b;
  font-style: italic;
}

.status-pending {
  display: flex;
  align-items: center;
  gap: 0.375rem;
  color: #f59e0b;
  font-size: 0.75rem;
  font-weight: 500;
}

.review-btn {
  background: #3D8D7A;
  color: white;
  border: none;
  padding: 0.5rem 0.75rem;
  border-radius: 6px;
  font-size: 0.75rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s;
  align-self: flex-start;
}

.review-btn:hover {
  background: #2d6a5a;
  transform: translateY(-1px);
}

/* Dark Mode for Gradebook */
.dark .gradebook-container {
  background: #23272b;
  border-color: #374151;
}

.dark .gradebook-table thead th {
  background: #374151;
  border-color: #4b5563;
  color: #f1f5f9;
}

.dark .gradebook-table thead th.sticky-col {
  background: #1f2937;
  border-color: #374151;
}

.dark .student-row {
  border-color: #374151;
}

.dark .student-row:hover {
  background: #374151;
}

.dark .student-row.expanded {
  background: #1e3a8a;
}

.dark .student-cell {
  background: #23272b;
  border-color: #374151;
}

.dark .student-row:hover .student-cell {
  background: #374151;
}

.dark .student-row.expanded .student-cell {
  background: #1e3a8a;
}

.dark .student-name {
  color: #f1f5f9;
}

.dark .student-id {
  color: #9ca3af;
}

.dark .score-cell {
  border-color: #374151;
}

.dark .score-input {
  background: #374151;
  border-color: #4b5563;
  color: #f1f5f9;
}

.dark .score-input.manual {
  background: #451a03;
  border-color: #92400e;
}

.dark .score-max {
  color: #9ca3af;
}

.dark .total-cell {
  background: #374151;
  border-color: #4b5563;
}

.dark .total-max {
  color: #9ca3af;
}

.dark .total-percentage {
  background: #4b5563;
  color: #9ca3af;
}

.dark .student-history-panel {
  background: #1e3a8a;
  border-color: #60a5fa;
}

.dark .history-header h4 {
  color: #f1f5f9;
}

.dark .history-item {
  background: #374151;
  border-color: #4b5563;
}

.dark .assessment-name {
  color: #f1f5f9;
}

.dark .score-info {
  color: #d1d5db;
}

.dark .percentage-info {
  color: #9ca3af;
}

/* Responsive Design */
@media (max-width: 768px) {
  .analytics-stats {
    grid-template-columns: repeat(2, 1fr);
  }
  
  .gradebook-scroll {
    max-height: 50vh;
  }
  
  .history-content {
    grid-template-columns: 1fr;
  }
  
  .section-selector {
    flex-direction: column;
    align-items: flex-start;
    gap: 0.5rem;
  }
  
  .section-select {
    min-width: 100%;
  }
  
  .header-actions {
    flex-direction: column;
    align-items: stretch;
    gap: 0.75rem;
  }
}

.stat-card.modern.graded {
  border-left: 4px solid #10b981;
}

.stat-card.modern.graded:hover {
  box-shadow: 0 20px 60px rgba(16, 185, 129, 0.2);
}

.stat-card.modern.total {
  border-left: 4px solid #3b82f6;
}

.stat-card.modern.total:hover {
  box-shadow: 0 20px 60px rgba(59, 130, 246, 0.2);
}

.stat-card.modern.average {
  border-left: 4px solid #8b5cf6;
}

.stat-card.modern.average:hover {
  box-shadow: 0 20px 60px rgba(139, 92, 246, 0.2);
}

/* Icon Wrapper with Animation */
.stat-icon-wrapper {
  position: relative;
}

.stat-icon {
  width: 48px;
  height: 48px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  flex-shrink: 0;
  position: relative;
  z-index: 2;
  transition: all 0.3s ease;
}

.stat-icon.pending { 
  background: linear-gradient(135deg, #f59e0b, #d97706);
  box-shadow: 0 8px 20px rgba(245, 158, 11, 0.3);
}

.stat-icon.graded { 
  background: linear-gradient(135deg, #10b981, #059669);
  box-shadow: 0 8px 20px rgba(16, 185, 129, 0.3);
}

.stat-icon.total { 
  background: linear-gradient(135deg, #3b82f6, #2563eb);
  box-shadow: 0 8px 20px rgba(59, 130, 246, 0.3);
}

.stat-icon.average { 
  background: linear-gradient(135deg, #8b5cf6, #7c3aed);
  box-shadow: 0 8px 20px rgba(139, 92, 246, 0.3);
}

/* Pulsing Animation Behind Icons */
.stat-pulse {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 48px;
  height: 48px;
  border-radius: 12px;
  opacity: 0.3;
  animation: pulse-animation 2s infinite;
}

.stat-pulse.pending {
  background: linear-gradient(135deg, #f59e0b, #d97706);
}

.stat-pulse.graded {
  background: linear-gradient(135deg, #10b981, #059669);
}

.stat-pulse.total {
  background: linear-gradient(135deg, #3b82f6, #2563eb);
}

.stat-pulse.average {
  background: linear-gradient(135deg, #8b5cf6, #7c3aed);
}

@keyframes pulse-animation {
  0% {
    transform: translate(-50%, -50%) scale(1);
    opacity: 0.3;
  }
  50% {
    transform: translate(-50%, -50%) scale(1.2);
    opacity: 0.1;
  }
  100% {
    transform: translate(-50%, -50%) scale(1);
    opacity: 0.3;
  }
}

/* Stat Content */
.stat-content {
  flex: 1;
  min-width: 0;
}

.stat-number {
  font-size: 1.75rem;
  font-weight: 700;
  color: #1f2937;
  line-height: 1;
  margin-bottom: 0.25rem;
  background: linear-gradient(135deg, #1f2937, #374151);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.dark .stat-number {
  background: linear-gradient(135deg, #f9fafb, #e5e7eb);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.stat-label {
  font-size: 0.875rem;
  color: #374151;
  font-weight: 600;
  margin-bottom: 0.125rem;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.dark .stat-label {
  color: #d1d5db;
}

.stat-description {
  font-size: 0.75rem;
  color: #6b7280;
  font-weight: 400;
  opacity: 0.8;
}

.dark .stat-description {
  color: #9ca3af;
}

/* Card Background Patterns */
.stat-card.modern::before {
  content: '';
  position: absolute;
  top: 0;
  right: 0;
  width: 100px;
  height: 100px;
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0.05));
  border-radius: 50%;
  transform: translate(30px, -30px);
  transition: all 0.3s ease;
}

.dark .stat-card.modern::before {
  background: linear-gradient(135deg, rgba(75, 85, 99, 0.2), rgba(55, 65, 81, 0.1));
}

.stat-card.modern:hover::before {
  transform: translate(20px, -20px) scale(1.2);
  opacity: 0.8;
}

/* Responsive Design */
@media (max-width: 768px) {
  .stats-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 0.75rem;
  }
  
  .stat-card.modern {
    padding: 1rem;
    gap: 0.75rem;
  }
  
  .stat-icon {
    width: 40px;
    height: 40px;
  }
  
  .stat-pulse {
    width: 40px;
    height: 40px;
  }
  
  .stat-number {
    font-size: 1.5rem;
  }
  
  .stat-label {
    font-size: 0.75rem;
  }
  
  .stat-description {
    font-size: 0.6875rem;
  }
}

@media (max-width: 480px) {
  .stats-grid {
    grid-template-columns: 1fr;
    gap: 0.75rem;
  }
  
  .stat-card.modern {
    flex-direction: row;
    text-align: left;
    padding: 1rem;
  }
  
  .stat-content {
    margin-top: 0;
  }
}

/* Enhanced Subject and Section Cards */
.subjects-grid.modern {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 1.5rem;
  padding: 1rem;
  margin-top: 1rem;
}

.subjects-grid, .sections-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 1rem;
}

.subject-card.modern {
  background: #ffffff;
  border: 1.5px solid #A3D1C6;
  border-radius: 16px;
  padding: 1.5rem;
  cursor: pointer;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  position: relative;
  overflow: hidden;
  display: flex;
  align-items: center;
  gap: 1rem;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.04);
  width: 100%;
  box-sizing: border-box;
}
.dark .subject-card.modern {
  background: #23272f;
  border-color: #20c997;
}

.subject-card.modern:before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(135deg, #3D8D7A, #059669);
  opacity: 0;
  transition: opacity 0.3s ease;
  border-radius: 16px;
}

.subject-card.modern:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 32px rgba(0, 0, 0, 0.12);
  border-color: rgba(61, 141, 122, 0.3);
}
.dark .subject-card.modern:hover {
  box-shadow: 0 12px 32px rgba(0, 0, 0, 0.4);
  border-color: rgba(163, 209, 198, 0.4);
}

.subject-card.modern:hover:before {
  opacity: 0.03;
}
.dark .subject-card.modern:hover:before {
  opacity: 0.08;
}

.subject-icon.modern {
  width: 56px;
  height: 56px;
  border-radius: 14px;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  flex-shrink: 0;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  background: #3D8D7A;
  color: #fff;
}
.dark .subject-icon.modern {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
  background: #20c997;
  color: #fff;
}

.subject-icon.modern svg,
.subject-icon.modern div {
  width: 28px;
  height: 28px;
  color: white;
  fill: white;
}

.subject-card, .section-card {
  background: #FBFFE4;
  border: 1px solid #A3D1C6;
  border-radius: 12px;
  padding: 1.25rem;
  cursor: pointer;
  transition: all 0.2s;
  display: flex;
  align-items: center;
  gap: 1rem;
}
.dark .subject-card, .dark .section-card {
  background: #23272b;
  border-color: #3D8D7A;
}

.subject-card:hover, .section-card:hover {
  background: white;
  border-color: #3D8D7A;
  box-shadow: 0 4px 12px rgba(61, 141, 122, 0.15);
  transform: translateY(-2px);
}
.dark .subject-card:hover, .dark .section-card:hover {
  background: #2a3038;
  border-color: #A3D1C6;
}

.subject-icon, .section-icon {
  width: 48px;
  height: 48px;
  border-radius: 10px;
  background: #3D8D7A;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  flex-shrink: 0;
}

.subject-info, .section-info {
  flex: 1;
}

.subject-info h4, .section-info h4 {
  font-size: 1.125rem;
  font-weight: 600;
  color: #1f2937;
  margin: 0 0 0.25rem 0;
}
.dark .subject-info h4, .dark .section-info h4 {
  color: #A3D1C6;
}

.subject-grade {
  color: #6b7280;
  font-size: 0.875rem;
  margin: 0 0 0.5rem 0;
}
.dark .subject-grade {
  color: #A3D1C6;
}

.section-code {
  background: #B3D8A8;
  color: #1f2937;
  border-radius: 6px;
  padding: 0.25rem 0.5rem;
  font-size: 0.75rem;
  font-weight: 600;
  display: inline-block;
  font-family: 'Courier New', monospace;
  margin: 0 0 0.5rem 0;
}
.dark .section-code {
  background: #3D8D7A;
  color: white;
}

.subject-stats, .section-stats {
  display: flex;
  gap: 0.75rem;
  flex-wrap: wrap;
}

.stat-item {
  display: flex;
  align-items: center;
  gap: 0.25rem;
  font-size: 0.75rem;
  color: #6b7280;
  font-weight: 500;
}
.dark .stat-item {
  color: #A3D1C6;
}

.stat-item.pending {
  color: #d97706;
}
.dark .stat-item.pending {
  color: #fbbf24;
}

.card-arrow {
  color: #A3D1C6;
  font-size: 1.25rem;
  transition: all 0.2s;
}

.subject-card:hover .card-arrow,
.section-card:hover .card-arrow {
  color: #3D8D7A;
  transform: translateX(2px);
}

.empty-state {
  padding: 3rem 2rem;
  text-align: center;
  color: #6b7280;
}
.dark .empty-state {
  color: #A3D1C6;
}

.empty-state svg {
  margin-bottom: 1rem;
  color: #A3D1C6;
}

.empty-state h3 {
  font-size: 1.125rem;
  margin-bottom: 0.5rem;
  color: #1f2937;
}
.dark .empty-state h3 {
  color: #A3D1C6;
}

/* Submissions Section */
.submissions-filters {
  display: flex;
  justify-content: flex-end;
  margin-bottom: 1rem;
}

.filter-select {
  padding: 0.5rem 0.75rem;
  border: 1px solid #A3D1C6;
  border-radius: 6px;
  background: white;
  font-size: 0.875rem;
  color: #1f2937;
}
.dark .filter-select {
  background: #23272b;
  border-color: #3D8D7A;
  color: #A3D1C6;
}

.submissions-table-container {
  overflow-x: auto;
  border-radius: 8px;
  border: 1px solid rgba(61, 141, 122, 0.1);
}
.dark .submissions-table-container {
  border-color: #3D8D7A;
}

.submissions-table {
  width: 100%;
  border-collapse: collapse;
  background: white;
}
.dark .submissions-table {
  background: #23272b;
}

.submissions-table th,
.submissions-table td {
  padding: 1.25rem 1rem;
  text-align: left;
  border-bottom: 1px solid rgba(61, 141, 122, 0.1);
}
.dark .submissions-table th,
.dark .submissions-table td {
  border-bottom-color: #3D8D7A;
}

.submissions-table th {
  background: #FBFFE4;
  font-weight: 600;
  color: #1f2937;
  font-size: 1rem;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}
.dark .submissions-table th {
  background: #1f2429;
  color: #A3D1C6;
}

.submissions-table th.sortable {
  cursor: pointer;
  user-select: none;
  transition: background 0.2s;
}

.submissions-table th.sortable:hover {
  background: #B3D8A8;
}
.dark .submissions-table th.sortable:hover {
  background: #2a3038;
}

.submissions-table th svg {
  margin-left: 0.5rem;
  opacity: 0.5;
}

/* Table Content Styles */
.student-info {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.student-avatar {
  width: 44px;
  height: 44px;
  border-radius: 50%;
  background: #3D8D7A;
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 600;
  font-size: 0.875rem;
  flex-shrink: 0;
}

.student-name {
  font-weight: 600;
  color: #1f2937;
  font-size: 1rem;
  line-height: 1.3;
}
.dark .student-name {
  color: #A3D1C6;
}

.student-email {
  font-size: 0.875rem;
  color: #6b7280;
  margin-top: 0.125rem;
}
.dark .student-email {
  color: #9ca3af;
}

.quiz-info {
  max-width: 200px;
}

.quiz-title {
  font-weight: 600;
  color: #1f2937;
  margin-bottom: 0.25rem;
  font-size: 1rem;
  line-height: 1.3;
}
.dark .quiz-title {
  color: #A3D1C6;
}

.quiz-code {
  font-size: 0.75rem;
  color: #6b7280;
  font-family: 'Courier New', monospace;
  background: #B3D8A8;
  padding: 0.25rem 0.5rem;
  border-radius: 6px;
  display: inline-block;
  font-weight: 500;
}
.dark .quiz-code {
  background: #3D8D7A;
  color: white;
}

.date-info {
  font-size: 0.75rem;
}

.date {
  color: #1f2937;
  font-weight: 500;
}
.dark .date {
  color: #A3D1C6;
}

.time {
  color: #6b7280;
}
.dark .time {
  color: #9ca3af;
}

.score-display {
  text-align: center;
}

.score-percentage {
  font-weight: 700;
  font-size: 1rem;
  margin-bottom: 0.25rem;
}

.score-percentage.excellent { color: #059669; }
.score-percentage.good { color: #3D8D7A; }
.score-percentage.average { color: #d97706; }
.score-percentage.needs-improvement { color: #dc2626; }

.score-fraction {
  font-size: 0.7rem;
  color: #6b7280;
}
.dark .score-fraction {
  color: #9ca3af;
}

.status-badge {
  padding: 0.25rem 0.625rem;
  border-radius: 12px;
  font-size: 0.7rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.025em;
}

.status-badge.submitted {
  background: rgba(163, 209, 198, 0.2);
  color: #1f2937;
}

.status-badge.graded {
  background: rgba(179, 216, 168, 0.3);
  color: #1f2937;
}

.status-badge.reviewed {
  background: rgba(61, 141, 122, 0.1);
  color: #3D8D7A;
}

/* Action Buttons */
.action-buttons {
  display: flex;
  gap: 0.5rem;
  flex-wrap: wrap;
}

.btn-action {
  border: none;
  border-radius: 8px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.025em;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

/* Old style for backward compatibility */
.btn-action:not(.modern) {
  width: 32px;
  height: 32px;
}

.btn-action:not(.modern).review {
  background: #B3D8A8;
  color: #1f2937;
}

.btn-action:not(.modern).review:hover {
  background: #3D8D7A;
  color: white;
}

.btn-action:not(.modern).view {
  background: rgba(163, 209, 198, 0.3);
  color: #3D8D7A;
}

.btn-action:not(.modern).view:hover {
  background: #A3D1C6;
  color: #1f2937;
}

/* Modern style with text labels */
.btn-action.modern {
  padding: 0.5rem 0.75rem;
  gap: 0.375rem;
  min-width: auto;
  white-space: nowrap;
}

.btn-action.modern svg {
  flex-shrink: 0;
}

.btn-action.modern span {
  font-size: 0.7rem;
  font-weight: 600;
}

.btn-action.modern.review {
  background: linear-gradient(135deg, #10b981, #059669);
  color: white;
  border: 1px solid transparent;
}

.btn-action.modern.review:hover {
  background: linear-gradient(135deg, #059669, #047857);
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(16, 185, 129, 0.3);
}

.btn-action.modern.view {
  background: linear-gradient(135deg, #3b82f6, #2563eb);
  color: white;
  border: 1px solid transparent;
}

.btn-action.modern.view:hover {
  background: linear-gradient(135deg, #2563eb, #1d4ed8);
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(59, 130, 246, 0.3);
}

.btn-action.modern:active {
  transform: translateY(0);
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

/* Dark mode support */
.dark .btn-action.modern.review {
  background: linear-gradient(135deg, #059669, #047857);
}

.dark .btn-action.modern.review:hover {
  background: linear-gradient(135deg, #047857, #065f46);
}

.dark .btn-action.modern.view {
  background: linear-gradient(135deg, #2563eb, #1d4ed8);
}

.dark .btn-action.modern.view:hover {
  background: linear-gradient(135deg, #1d4ed8, #1e40af);
}

/* Pagination */
.pagination {
  padding: 1.5rem;
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 1rem;
  border-top: 1px solid rgba(61, 141, 122, 0.1);
}
.dark .pagination {
  border-top-color: #3D8D7A;
}

.pagination-btn {
  width: 36px;
  height: 36px;
  border: 1px solid #A3D1C6;
  background: white;
  border-radius: 6px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.2s;
  color: #3D8D7A;
}
.dark .pagination-btn {
  background: #23272b;
  border-color: #3D8D7A;
  color: #A3D1C6;
}

.pagination-btn:hover:not(:disabled) {
  background: #B3D8A8;
  border-color: #3D8D7A;
  color: #1f2937;
}
.dark .pagination-btn:hover:not(:disabled) {
  background: #3D8D7A;
  color: white;
}

.pagination-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.pagination-info {
  color: #6b7280;
  font-size: 0.875rem;
  font-weight: 500;
}
.dark .pagination-info {
  color: #A3D1C6;
}

/* Modal Styles */
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
  padding: 1rem;
}

.review-modal {
  background: white;
  border-radius: 12px;
  width: 100%;
  max-width: 900px;
  max-height: 90vh;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  border: 1px solid #A3D1C6;
}
.dark .review-modal {
  background: #23272b;
  border-color: #3D8D7A;
}

.modal-header {
  padding: 1.5rem;
  border-bottom: 1px solid rgba(61, 141, 122, 0.1);
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: #FBFFE4;
}
.dark .modal-header {
  background: #1f2429;
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

.modal-subtitle {
  color: #6b7280;
  font-size: 0.875rem;
  margin: 0.25rem 0 0 0;
}
.dark .modal-subtitle {
  color: #A3D1C6;
}

.modal-close {
  width: 36px;
  height: 36px;
  border: none;
  background: none;
  cursor: pointer;
  border-radius: 6px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #6b7280;
  transition: all 0.2s;
}
.dark .modal-close {
  color: #A3D1C6;
}

.modal-close:hover {
  background: #B3D8A8;
  color: #1f2937;
}
.dark .modal-close:hover {
  background: #3D8D7A;
  color: white;
}

.modal-content {
  flex: 1;
  overflow-y: auto;
}

.loading-questions, .no-questions {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 3rem 2rem;
  color: #6b7280;
}
.dark .loading-questions, .dark .no-questions {
  color: #A3D1C6;
}

.spinner-small {
  width: 30px;
  height: 30px;
  border: 3px solid #B3D8A8;
  border-top: 3px solid #3D8D7A;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin-bottom: 1rem;
}

.submission-review {
  padding: 1.5rem;
}

.review-summary {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
  gap: 1.5rem;
  padding: 0.5rem 0;
  max-width: 100%;
  margin: 0 auto;
  margin-bottom: 1.5rem;
  border: 1px solid rgba(61, 141, 122, 0.1);
}
.dark .review-summary {
  background: #1f2429;
  border-color: #3D8D7A;
}

.summary-stat {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
}

.stat-label {
  font-size: 0.75rem;
  color: #6b7280;
  margin-bottom: 0.5rem;
  font-weight: 500;
}
.dark .stat-label {
  color: #A3D1C6;
}

.stat-value {
  font-size: 1.25rem;
  font-weight: 700;
  color: #1f2937;
}
.dark .stat-value {
  color: #A3D1C6;
}

/* Question Review Styles */
.questions-review {
  display: flex;
  flex-direction: column;
  gap: 1.25rem;
}

.question-review-item {
  border: 1px solid rgba(61, 141, 122, 0.1);
  border-radius: 8px;
  padding: 1.25rem;
  background: white;
}
.dark .question-review-item {
  background: #2a3038;
  border-color: #3D8D7A;
}

.question-header {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 1rem;
  flex-wrap: wrap;
}

.question-number {
  background: #3D8D7A;
  color: white;
  padding: 0.5rem 0.75rem;
  border-radius: 6px;
  font-weight: 600;
  font-size: 0.8rem;
}

.question-result {
  padding: 0.375rem 0.75rem;
  border-radius: 6px;
  font-weight: 600;
  font-size: 0.8rem;
}

.question-result.correct {
  background: rgba(179, 216, 168, 0.3);
  color: #1f2937;
}

.question-result.incorrect {
  background: rgba(248, 113, 113, 0.1);
  color: #dc2626;
}

.question-points {
  margin-left: auto;
  color: #6b7280;
  font-weight: 600;
  font-size: 0.875rem;
}
.dark .question-points {
  color: #A3D1C6;
}

.question-text {
  font-size: 1rem;
  color: #1f2937;
  margin-bottom: 1rem;
  line-height: 1.6;
}
.dark .question-text {
  color: #A3D1C6;
}

.answer-section {
  margin: 1rem 0;
}

.options-grid {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.option-item {
  display: flex;
  align-items: flex-start;
  gap: 0.75rem;
  padding: 1rem;
  border: 2px solid #e2e8f0;
  border-radius: 0.5rem;
  background: white;
}

.option-item.correct {
  border-color: #10b981;
  background: #ecfdf5;
}

.option-item.incorrect {
  border-color: #ef4444;
  background: #fef2f2;
}

.option-letter {
  min-width: 32px;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #f1f5f9;
  border-radius: 50%;
  font-weight: 700;
  color: #475569;
}

.option-item.correct .option-letter {
  background: #10b981;
  color: white;
}

.option-item.incorrect .option-letter {
  background: #ef4444;
  color: white;
}

.option-content {
  flex: 1;
}

.option-text {
  color: #1a202c;
  line-height: 1.5;
}

.true-false-options {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
}

.tf-option {
  padding: 1.5rem;
  border: 2px solid #e2e8f0;
  border-radius: 0.5rem;
  text-align: center;
  background: white;
}

.tf-option.student-selected {
  border-color: #3b82f6;
  background: #eff6ff;
}

.tf-option.correct-answer {
  border-color: #10b981;
  background: #ecfdf5;
}

.tf-option strong {
  display: block;
  font-size: 1.125rem;
  color: #1a202c;
}

.fill-blank-answers {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.student-answer-box, .correct-answer-box {
  padding: 1rem;
  border-radius: 0.5rem;
  border: 1px solid #e2e8f0;
}

.answer-label {
  font-size: 0.875rem;
  color: #64748b;
  margin-bottom: 0.5rem;
  font-weight: 600;
}

.answer-text {
  padding: 0.75rem;
  border-radius: 0.375rem;
  font-size: 1rem;
}

.answer-text.correct {
  background: #d1fae5;
  color: #065f46;
}

.answer-text.incorrect {
  background: #fee2e2;
  color: #991b1b;
}

.teacher-comment-section {
  margin-top: 1rem;
}

.comment-input {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid #e2e8f0;
  border-radius: 0.375rem;
  font-family: inherit;
  font-size: 0.875rem;
  resize: vertical;
}

.comment-input:focus {
  outline: none;
  border-color: #3b82f6;
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
}

.overall-feedback-section {
  margin-top: 1.5rem;
  padding-top: 1.5rem;
  border-top: 2px solid #e2e8f0;
}

.overall-feedback-section h4 {
  font-size: 1.125rem;
  color: #1a202c;
  margin-bottom: 0.75rem;
}

.feedback-textarea {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid #e2e8f0;
  border-radius: 0.375rem;
  font-family: inherit;
  font-size: 0.875rem;
  resize: vertical;
}

.feedback-textarea:focus {
  outline: none;
  border-color: #3b82f6;
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
}

.modal-actions {
  padding: 1.5rem;
  border-top: 1px solid rgba(61, 141, 122, 0.1);
  display: flex;
  justify-content: flex-end;
  gap: 1rem;
  background: #FBFFE4;
}
.dark .modal-actions {
  background: #1f2429;
  border-top-color: #3D8D7A;
}

.btn-modal {
  padding: 0.75rem 1.5rem;
  border: none;
  border-radius: 8px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
  font-size: 0.875rem;
}

.btn-modal.cancel {
  background: #f1f5f9;
  color: #6b7280;
  border: 1px solid #A3D1C6;
}
.dark .btn-modal.cancel {
  background: #23272b;
  color: #A3D1C6;
  border-color: #3D8D7A;
}

.btn-modal.cancel:hover {
  background: #B3D8A8;
  color: #1f2937;
}
.dark .btn-modal.cancel:hover {
  background: #3D8D7A;
  color: white;
}

.btn-modal.primary {
  background: #3D8D7A;
  color: white;
}

.btn-modal.primary:hover:not(:disabled) {
  background: #2d6b5c;
  box-shadow: 0 2px 6px rgba(61, 141, 122, 0.2);
}

.btn-modal:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

/* Points Input */
.points-input {
  width: 60px;
  padding: 0.375rem 0.5rem;
  border: 1px solid #A3D1C6;
  border-radius: 4px;
  text-align: center;
  font-weight: 600;
  font-size: 0.875rem;
  background: white;
}
.dark .points-input {
  background: #23272b;
  border-color: #3D8D7A;
  color: #A3D1C6;
}

.points-input:focus {
  outline: none;
  border-color: #3D8D7A;
  box-shadow: 0 0 0 3px rgba(61, 141, 122, 0.1);
}

/* Input and Textarea Styles */
.comment-input, .feedback-textarea {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid #A3D1C6;
  border-radius: 6px;
  font-family: inherit;
  font-size: 0.875rem;
  resize: vertical;
  background: white;
}
.dark .comment-input, .dark .feedback-textarea {
  background: #23272b;
  border-color: #3D8D7A;
  color: #A3D1C6;
}

.comment-input:focus, .feedback-textarea:focus {
  outline: none;
  border-color: #3D8D7A;
  box-shadow: 0 0 0 3px rgba(61, 141, 122, 0.1);
}

/* Answer Styles */
.answer-section {
  margin: 1rem 0;
}

.answer-key-label {
  font-weight: 600;
  color: #1f2937;
  margin-bottom: 0.75rem;
}
.dark .answer-key-label {
  color: #A3D1C6;
}

.options-grid {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.option-item {
  display: flex;
  align-items: flex-start;
  gap: 0.75rem;
  padding: 1rem;
  border: 2px solid #e5e7eb;
  border-radius: 8px;
  background: white;
}
.dark .option-item {
  background: #23272b;
  border-color: #374151;
}

.option-item.correct {
  border-color: #B3D8A8;
  background: rgba(179, 216, 168, 0.1);
}

.option-item.incorrect {
  border-color: #fca5a5;
  background: rgba(248, 113, 113, 0.1);
}

.option-item.selected {
  border-color: #3D8D7A;
}

.option-letter {
  min-width: 28px;
  height: 28px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #f1f5f9;
  border-radius: 50%;
  font-weight: 700;
  color: #475569;
  font-size: 0.875rem;
}

.option-item.correct .option-letter {
  background: #B3D8A8;
  color: #1f2937;
}

.option-item.incorrect .option-letter {
  background: #fca5a5;
  color: white;
}

.option-content {
  flex: 1;
}

.option-text {
  color: #1f2937;
  line-height: 1.5;
}
.dark .option-text {
  color: #A3D1C6;
}

.correct-tag, .selected-tag {
  font-size: 0.75rem;
  font-weight: 600;
  padding: 0.25rem 0.5rem;
  border-radius: 4px;
  margin-top: 0.5rem;
  display: inline-block;
}

.correct-tag {
  background: rgba(179, 216, 168, 0.2);
  color: #1f2937;
}

.selected-tag {
  background: rgba(61, 141, 122, 0.1);
  color: #3D8D7A;
}

/* True/False Options */
.true-false-options {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
}

.tf-option {
  padding: 1.25rem;
  border: 2px solid #e5e7eb;
  border-radius: 8px;
  text-align: center;
  background: white;
  transition: all 0.2s;
}
.dark .tf-option {
  background: #23272b;
  border-color: #374151;
}

.tf-option.student-selected {
  border-color: #3D8D7A;
  background: rgba(61, 141, 122, 0.05);
}

.tf-option.correct-answer {
  border-color: #B3D8A8;
  background: rgba(179, 216, 168, 0.1);
}

.tf-option.wrong-answer {
  border-color: #fca5a5;
  background: rgba(248, 113, 113, 0.1);
}

.tf-option strong {
  display: block;
  font-size: 1.125rem;
  color: #1f2937;
  margin-bottom: 0.5rem;
}
.dark .tf-option strong {
  color: #A3D1C6;
}

/* Fill in the Blank */
.fill-blank-answers {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.answer-key-box, .student-answer-box {
  padding: 1rem;
  border-radius: 8px;
  border: 1px solid #e5e7eb;
}
.dark .answer-key-box, .dark .student-answer-box {
  border-color: #374151;
}

.answer-label {
  font-size: 0.875rem;
  color: #6b7280;
  margin-bottom: 0.5rem;
  font-weight: 600;
}
.dark .answer-label {
  color: #A3D1C6;
}

.answer-text {
  padding: 0.75rem;
  border-radius: 6px;
  font-size: 1rem;
  font-weight: 500;
}

.answer-text.correct {
  background: rgba(179, 216, 168, 0.2);
  color: #1f2937;
}

.answer-text.incorrect {
  background: rgba(248, 113, 113, 0.1);
  color: #dc2626;
}

/* Teacher Comments */
.teacher-comment-section {
  margin-top: 1rem;
  padding-top: 1rem;
  border-top: 1px solid rgba(61, 141, 122, 0.1);
}
.dark .teacher-comment-section {
  border-top-color: #3D8D7A;
}

.overall-feedback-section {
  margin-top: 1.5rem;
  padding-top: 1.5rem;
  border-top: 2px solid rgba(61, 141, 122, 0.1);
}
.dark .overall-feedback-section {
  border-top-color: #3D8D7A;
}

.overall-feedback-section h4 {
  font-size: 1.125rem;
  color: #1f2937;
  margin-bottom: 0.75rem;
  font-weight: 600;
}
.dark .overall-feedback-section h4 {
  color: #A3D1C6;
}

.feedback-display {
  background: #FBFFE4;
  padding: 1rem;
  border-radius: 8px;
  border: 1px solid rgba(61, 141, 122, 0.1);
}
.dark .feedback-display {
  background: #1f2429;
  border-color: #3D8D7A;
}

.feedback-display p {
  color: #1f2937;
  line-height: 1.6;
  margin: 0;
}
.dark .feedback-display p {
  color: #A3D1C6;
}

.comment-display {
  background: rgba(61, 141, 122, 0.05);
  padding: 0.75rem;
  border-radius: 6px;
  margin-top: 0.5rem;
}
.dark .comment-display {
  background: rgba(61, 141, 122, 0.1);
}

.comment-display strong {
  color: #3D8D7A;
  font-weight: 600;
}
.dark .comment-display strong {
  color: #A3D1C6;
}

.comment-display p {
  margin: 0.5rem 0 0 0;
  color: #1f2937;
}
.dark .comment-display p {
  color: #A3D1C6;
}

/* Responsive Design */
@media (max-width: 768px) {
  .gradebook-container {
    padding: 1rem;
  }

  .header-content {
    flex-direction: column;
    align-items: stretch;
  }

  .search-box {
    min-width: auto;
  }

  .subjects-grid, .sections-grid {
    grid-template-columns: 1fr;
  }

  .stats-grid {
    grid-template-columns: 1fr;
  }

  .submissions-table {
    font-size: 0.8rem;
  }

  .review-summary {
    grid-template-columns: repeat(2, 1fr);
  }

  .modal-actions {
    flex-direction: column;
  }

  .btn-modal {
    width: 100%;
    max-width: 100%;
  }
}

/* Logout Modal Specific Styles */
.logout-modal {
  max-width: 400px;
  border-radius: 16px;
  overflow: hidden;
  background: white;
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15);
}

.dark .logout-modal {
  background: #23272b;
  border: 1px solid #374151;
}

.logout-header {
  background: linear-gradient(135deg, #dc2626, #b91c1c);
  color: white;
  padding: 1.5rem;
  border-bottom: none;
}

.logout-header h3 {
  color: white;
  margin: 0;
  font-size: 1.25rem;
  font-weight: 600;
}

.modal-body {
  padding: 2rem 1.5rem;
  text-align: center;
}

.logout-icon {
  color: #dc2626;
  margin-bottom: 1rem;
}

.logout-message {
  font-size: 1.125rem;
  font-weight: 600;
  color: #1f2937;
  margin-bottom: 0.5rem;
}

.dark .logout-message {
  color: #f1f5f9;
}

.logout-submessage {
  color: #64748b;
  font-size: 0.875rem;
}

.dark .logout-submessage {
  color: #9ca3af;
}

.logout-footer {
  padding: 1.5rem;
  background: #f8fafc;
  border-top: 1px solid #e2e8f0;
  display: flex;
  gap: 1rem;
  justify-content: flex-end;
}

.dark .logout-footer {
  background: #374151;
  border-color: #4b5563;
}

.btn-cancel {
  padding: 0.75rem 1.5rem;
  border: 1px solid #d1d5db;
  background: white;
  color: #374151;
  border-radius: 8px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
}

.dark .btn-cancel {
  background: #4b5563;
  border-color: #6b7280;
  color: #f1f5f9;
}

.btn-cancel:hover:not(:disabled) {
  background: #f3f4f6;
  border-color: #9ca3af;
}

.dark .btn-cancel:hover:not(:disabled) {
  background: #6b7280;
}

.btn-logout {
  padding: 0.75rem 1.5rem;
  background: linear-gradient(135deg, #dc2626, #b91c1c);
  color: white;
  border: none;
  border-radius: 8px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  min-width: 120px;
  justify-content: center;
}

.btn-logout:hover:not(:disabled) {
  background: linear-gradient(135deg, #b91c1c, #991b1b);
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(220, 38, 38, 0.3);
}

.btn-logout:disabled {
  opacity: 0.7;
  cursor: not-allowed;
  transform: none;
}

.loading-text {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.logout-spinner {
  width: 16px;
  height: 16px;
  border: 2px solid rgba(255, 255, 255, 0.3);
  border-top: 2px solid white;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

/* Final responsive adjustments */
@media (max-width: 480px) {
  .logout-footer {
    flex-direction: column;
  }
  
  .btn-cancel,
  .btn-logout {
    width: 100%;
  }
  
  .main-content {
    padding: 1rem;
  }
  
  .gradebook-header {
    padding: 1rem;
  }
  
  .header-actions {
    flex-direction: column;
    gap: 0.5rem;
  }
  
  .section-select {
    min-width: 100%;
  }
  
  .modal-actions {
    flex-direction: column;
  }

  .btn-modal {
    width: 100%;
    max-width: 100%;
  }
}

/* Breadcrumb Navigation */
.breadcrumb {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 1rem 0;
  margin-bottom: 1rem;
}

.breadcrumb-item {
  background: none;
  border: none;
  color: #64748b;
  cursor: pointer;
  padding: 0.5rem 0.75rem;
  border-radius: 0.375rem;
  font-size: 0.875rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  transition: all 0.2s;
}

.breadcrumb-item:hover {
  background: #f1f5f9;
  color: #3b82f6;
}

.breadcrumb-item.active {
  color: #1a202c;
  font-weight: 600;
  cursor: default;
}

.breadcrumb-item.active:hover {
  background: none;
}

.breadcrumb-separator {
  color: #cbd5e1;
}

/* Subject Cards */
.subjects-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 1.5rem;
}

.subject-card {
  background: white;
  border-radius: 0.75rem;
  padding: 1.5rem;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  cursor: pointer;
  transition: all 0.2s;
  display: flex;
  align-items: center;
  gap: 1rem;
}

.subject-card:hover {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  transform: translateY(-2px);
}

.subject-icon {
  width: 60px;
  height: 60px;
  border-radius: 0.75rem;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-size: 1.5rem;
  flex-shrink: 0;
}

.subject-info {
  flex: 1;
}

.subject-info h3 {
  font-size: 1.25rem;
  font-weight: 600;
  color: #1a202c;
  margin: 0 0 0.25rem 0;
}

.subject-info p {
  color: #64748b;
  font-size: 0.875rem;
  margin: 0 0 0.75rem 0;
  font-family: monospace;
}

.subject-stats {
  display: flex;
  gap: 0.5rem;
  flex-wrap: wrap;
}

.stat-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.375rem;
  padding: 0.25rem 0.625rem;
  background: #f1f5f9;
  border-radius: 0.375rem;
  font-size: 0.75rem;
  color: #475569;
  font-weight: 500;
}

.stat-badge.pending {
  background: #fef3c7;
  color: #92400e;
}

.stat-badge i {
  font-size: 0.625rem;
}

.card-arrow {
  color: #cbd5e1;
  font-size: 1.25rem;
}

/* Section Cards */
.sections-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 1.5rem;
}

.section-card {
  background: white;
  border-radius: 0.75rem;
  padding: 1.5rem;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  cursor: pointer;
  transition: all 0.2s;
  display: flex;
  align-items: center;
  gap: 1rem;
}

.section-card:hover {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  transform: translateY(-2px);
}

.section-icon {
  width: 60px;
  height: 60px;
  border-radius: 0.75rem;
  background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-size: 1.5rem;
  flex-shrink: 0;
}

.section-info {
  flex: 1;
}

.section-info h3 {
  font-size: 1.25rem;
  font-weight: 600;
  color: #1a202c;
  margin: 0 0 0.25rem 0;
}

.section-info p {
  color: #64748b;
  font-size: 0.875rem;
  margin: 0 0 0.75rem 0;
}

.section-stats {
  display: flex;
  gap: 0.5rem;
  flex-wrap: wrap;
}

/* Submissions View */
.submissions-view {
  animation: fadeIn 0.3s ease-in;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.submissions-filters {
  padding: 1rem 0;
  display: flex;
  justify-content: flex-end;
}

.stat-card .stat-icon.total {
  background: #6366f1;
}

/* Points Input in Modal */
.points-input {
  width: 60px;
  padding: 0.25rem 0.5rem;
  border: 1px solid #e2e8f0;
  border-radius: 0.25rem;
  text-align: center;
  font-weight: 600;
  font-size: 0.875rem;
}

.points-input:focus {
  outline: none;
  border-color: #3b82f6;
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
}

/* True/False styling updates */
.tf-option.wrong-answer {
  border-color: #ef4444;
  background: #fef2f2;
}

.tf-option.correct-answer.student-selected {
  border-color: #10b981;
  background: #ecfdf5;
}

/* Responsive adjustments */
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
  .subjects-grid,
  .sections-grid,
  .subjects-grid.modern,
  .sections-grid.enhanced {
    grid-template-columns: 1fr;
    gap: 1rem;
    padding: 0.5rem;
  }

  .breadcrumb {
    flex-wrap: wrap;
  }

  .subject-card,
  .section-card {
    padding: 1rem;
  }

  .subject-icon,
  .section-icon {
    width: 50px;
    height: 50px;
    font-size: 1.25rem;
  }
  
  .main-content {
    padding: 1rem;
    margin-left: 0;
    width: 100%;
  }
  
  .page-header {
    padding: 1rem;
  }
  
  .filter-buttons {
    grid-template-columns: 1fr;
    gap: 0.75rem;
  }
  
  .content-card.modern {
    padding: 1.5rem;
    margin: 0 0 1rem 0;
  }
  
  .filter-title {
    font-size: 1.25rem;
  }
  
  .header-title {
    font-size: 1.5rem;
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
  
  .search-box {
    min-width: 200px;
  }
}

/* Enhanced Sections */
.sections-grid.enhanced {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 1.5rem;
  padding: 1rem;
  margin-top: 1rem;
}

.section-card.modern {
  background: #fff;
  border-radius: 14px;
  padding: 1.25rem 1.5rem;
  margin-bottom: 0;
  box-shadow: 0 2px 8px rgba(61, 141, 122, 0.08);
  border: 1px solid #e2e8f0;
  cursor: pointer;
  transition: box-shadow 0.2s, border 0.2s, background 0.2s;
  position: relative;
  display: flex;
  align-items: center;
  gap: 1.25rem;
  width: 100%;
  box-sizing: border-box;
}
.dark .section-card.modern {
  background: linear-gradient(135deg, #1f2937 0%, #374151 100%);
  border-color: rgba(163, 209, 198, 0.2);
}

.section-card.modern:before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(135deg, #6366f1, #8b5cf6);
  opacity: 0;
  transition: opacity 0.3s ease;
  border-radius: 16px;
}

.section-card.modern:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 32px rgba(0, 0, 0, 0.12);
  border-color: rgba(99, 102, 241, 0.3);
}
.dark .section-card.modern:hover {
  box-shadow: 0 12px 32px rgba(0, 0, 0, 0.4);
  border-color: rgba(139, 92, 246, 0.4);
}

.section-card.modern:hover:before {
  opacity: 0.03;
}
.dark .section-card.modern:hover:before {
  opacity: 0.08;
}

.section-icon.modern {
  width: 56px;
  height: 56px;
  border-radius: 14px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.75rem;
  font-weight: 600;
  color: #fff;
  margin-right: 1.25rem;
  box-shadow: 0 2px 6px rgba(61, 141, 122, 0.12);
  background: linear-gradient(135deg, #3D8D7A 0%, #10b981 100%);
}
.dark .section-icon.modern {
  box-shadow: 0 4px 12px rgba(32, 201, 151, 0.3);
  background: linear-gradient(135deg, #059669 0%, #20c997 100%);
}

.section-info.enhanced {
  flex: 1;
  min-width: 0;
}

.section-info.enhanced h4 {
  font-size: 1.125rem;
  font-weight: 700;
  color: #1f2937;
  margin: 0 0 0.25rem 0;
  line-height: 1.3;
}
.dark .section-info.enhanced h4 {
  color: #f9fafb;
}

.section-stats.enhanced {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
}

.section-stats.enhanced .stat-item.modern {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.75rem;
  color: #6b7280;
  font-weight: 600;
  padding: 0.5rem 0.75rem;
  background: rgba(99, 102, 241, 0.08);
  border-radius: 8px;
  transition: all 0.2s ease;
}
.dark .section-stats.enhanced .stat-item.modern {
  color: #9ca3af;
  background: rgba(139, 92, 246, 0.15);
}

.section-stats.enhanced .stat-item.modern.pending {
  background: rgba(245, 101, 101, 0.1);
  color: #ef4444;
}
.dark .section-stats.enhanced .stat-item.modern.pending {
  background: rgba(245, 101, 101, 0.2);
  color: #fca5a5;
}

.empty-state.modern {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 4rem 2rem;
  text-align: center;
  background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
  border: 2px dashed #e2e8f0;
  border-radius: 16px;
  grid-column: 1 / -1;
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
}

.empty-state.modern:hover {
  border-color: #3D8D7A;
  background: linear-gradient(135deg, #f8fdfa 0%, #ecfdf5 100%);
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(61, 141, 122, 0.1);
}

.empty-state.modern:before {
  content: '';
  position: absolute;
  top: -50%;
  left: -50%;
  width: 200%;
  height: 200%;
  background: radial-gradient(circle, rgba(61, 141, 122, 0.03) 0%, transparent 70%);
  animation: pulse 4s ease-in-out infinite;
}

.dark .empty-state.modern {
  background: linear-gradient(135deg, #23272b 0%, #2a2f33 100%);
  border-color: #374151;
}

.dark .empty-state.modern:hover {
  border-color: #20c997;
  background: linear-gradient(135deg, #2a2f33 0%, #1f2937 100%);
}

.empty-icon {
  width: 80px;
  height: 80px;
  background: linear-gradient(135deg, #e5e7eb, #d1d5db);
  border-radius: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 1.5rem;
  color: #6b7280;
}
.dark .empty-icon {
  background: linear-gradient(135deg, #4b5563, #6b7280);
  color: #9ca3af;
}

.empty-content h3 {
  font-size: 1.25rem;
  font-weight: 700;
  color: #374151;
  margin: 0 0 0.5rem 0;
}
.dark .empty-content h3 {
  color: #d1d5db;
}

.empty-content p {
  font-size: 0.875rem;
  color: #6b7280;
  margin: 0;
}
.dark .empty-content p {
  color: #9ca3af;
}

.card-arrow.modern {
  color: #9ca3af;
  transition: all 0.3s ease;
  transform: translateX(0);
}
.dark .card-arrow.modern {
  color: #6b7280;
}

.subject-card.modern:hover .card-arrow.modern,
.section-card.modern:hover .card-arrow.modern {
  color: #3D8D7A;
  transform: translateX(4px);
}
.dark .subject-card.modern:hover .card-arrow.modern,
.dark .section-card.modern:hover .card-arrow.modern {
  color: #A3D1C6;
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
  background: #fff;
  border-radius: 14px;
  padding: 1.25rem 1.5rem;
  margin-bottom: 0;
  box-shadow: 0 2px 8px rgba(61, 141, 122, 0.08);
  border: 1px solid #e2e8f0;
  cursor: pointer;
  transition: box-shadow 0.2s, border 0.2s, background 0.2s;
  position: relative;
  display: flex;
  align-items: center;
  gap: 1.25rem;
  width: 100%;
  box-sizing: border-box;
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