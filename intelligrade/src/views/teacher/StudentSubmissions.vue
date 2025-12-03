<template>
  <div class="student-submissions">
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
        <!-- Center: Empty space -->
        <div class="navbar-center"></div>
        <!-- Right: User info -->
        <div class="navbar-right">
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
                
                <button @click="openLogoutModal" class="dropdown-item logout-btn">
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

    <!-- Main Content -->
    <main class="main-content">
      <!-- Page Header -->
      <div class="page-header">
        <div class="header-content">
          <div class="header-left">
            <button @click="goBack" class="back-btn">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                <path d="M20,11V13H8L13.5,18.5L12.08,19.92L4.16,12L12.08,4.08L13.5,5.5L8,11H20Z" />
              </svg>
              Back to Section
            </button>
            <div class="header-icon">
              <svg width="28" height="28" viewBox="0 0 24 24" fill="currentColor">
                <path d="M14,2H6A2,2 0 0,0 4,4V20A2,2 0 0,0 6,22H18A2,2 0 0,0 20,20V8L14,2M18,20H6V4H13V9H18V20Z"/>
              </svg>
            </div>
            <div>
              <h1 class="header-title">Student Submissions</h1>
              <p class="header-subtitle">{{ subjectName }} - {{ sectionName }}</p>
            </div>
          </div>
        </div>
      </div>

        <!-- Content Wrapper -->
        <div class="content-wrapper">
          <!-- Loading State -->
          <div v-if="loading" class="loading-container">
            <div class="loading-spinner"></div>
            <p>Loading submissions...</p>
          </div>

          <!-- Error State -->
          <div v-else-if="error" class="error-container">
            <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <circle cx="12" cy="12" r="10"/>
              <line x1="12" y1="8" x2="12" y2="12"/>
              <line x1="12" y1="16" x2="12.01" y2="16"/>
            </svg>
            <p>{{ error }}</p>
            <button @click="fetchSubmissions" class="retry-button">Retry</button>
          </div>

          <!-- Main Content -->
          <div v-else class="submissions-container">
            <!-- Filters Section -->
            <div class="filters-section">
              <!-- Search Bar -->
              <div class="search-container">
                <div class="search-input-container">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" class="search-icon">
                    <circle cx="11" cy="11" r="8" stroke="currentColor" stroke-width="2"/>
                    <path d="m21 21-4.35-4.35" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                  <input
                    v-model="searchQuery"
                    class="search-input"
                    type="text"
                    placeholder="Search by student name..."
                  />
                </div>
              </div>

              <!-- Filter Tabs -->
              <div class="filter-tabs">
                <button 
                  @click="filterType = 'all'"
                  :class="['filter-tab', { 'active': filterType === 'all' }]"
                >
                  <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
                    <polyline points="14 2 14 8 20 8"/>
                  </svg>
                  All Submissions
                  <span class="count">{{ submissions.length }}</span>
                </button>
                
                <button 
                  @click="filterType = 'quiz'"
                  :class="['filter-tab', 'quiz-tab', { 'active': filterType === 'quiz' }]"
                >
                  <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <circle cx="12" cy="12" r="10"/>
                    <path d="M12 6v6l4 2"/>
                  </svg>
                  Quizzes Only
                  <span class="count">{{ stats.totalQuizSubmissions }}</span>
                </button>
                
                <button 
                  @click="filterType = 'assignment'"
                  :class="['filter-tab', 'assignment-tab', { 'active': filterType === 'assignment' }]"
                >
                  <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
                    <polyline points="14 2 14 8 20 8"/>
                    <line x1="9" y1="15" x2="15" y2="15"/>
                  </svg>
                  Assignments Only
                  <span class="count">{{ stats.totalAssignmentSubmissions }}</span>
                </button>
              </div>

              <!-- Status Filter -->
              <div class="status-filter-container">
                <label class="filter-label">Filter by Status:</label>
                <select v-model="filterStatus" class="status-filter">
                  <option value="all">All Status</option>
                  <option value="submitted">Pending Review</option>
                  <option value="graded">Graded</option>
                  <option value="reviewed">Reviewed</option>
                  <option value="returned">Returned</option>
                </select>
              </div>
            </div>

                  <!-- Statistics Cards -->
            <div class="stats-grid">
              <div class="stat-card">
                <div class="stat-icon quiz">
                  <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
                    <polyline points="14 2 14 8 20 8"/>
                    <line x1="9" y1="15" x2="15" y2="15"/>
                  </svg>
                </div>
                <div class="stat-info">
                  <h3>{{ stats.totalQuizSubmissions }}</h3>
                  <p>Quiz Submissions</p>
                </div>
              </div>

              <div class="stat-card">
                <div class="stat-icon assignment">
                  <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
                    <polyline points="14 2 14 8 20 8"/>
                  </svg>
                </div>
                <div class="stat-info">
                  <h3>{{ stats.totalAssignmentSubmissions }}</h3>
                  <p>Assignment Submissions</p>
                </div>
              </div>

              <div class="stat-card">
                <div class="stat-icon pending">
                  <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <circle cx="12" cy="12" r="10"/>
                    <polyline points="12 6 12 12 16 14"/>
                  </svg>
                </div>
                <div class="stat-info">
                  <h3>{{ stats.pendingReview }}</h3>
                  <p>Pending Review</p>
                </div>
              </div>

              <div class="stat-card">
                <div class="stat-icon graded">
                  <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <polyline points="20 6 9 17 4 12"/>
                  </svg>
                </div>
                <div class="stat-info">
                  <h3>{{ stats.graded }}</h3>
                  <p>Graded</p>
                </div>
              </div>
            </div>

            <!-- Results Summary -->
            <div class="results-summary">
              <div class="results-text">
                <span class="results-count">{{ filteredSubmissions.length }}</span>
                <span class="results-label">
                  {{ filterType === 'quiz' ? 'quiz' : filterType === 'assignment' ? 'assignment' : '' }} 
                  {{ filteredSubmissions.length === 1 ? 'submission' : 'submissions' }}
                  {{ searchQuery ? `matching "${searchQuery}"` : '' }}
                </span>
              </div>
              <div v-if="filterType !== 'all'" class="active-filter">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <polygon points="22 3 2 3 10 12.46 10 19 14 21 14 12.46 22 3"/>
                </svg>
                Filtered by: {{ filterType === 'quiz' ? 'Quizzes Only' : 'Assignments Only' }}
              </div>
            </div>

            <!-- Submissions List -->
            <div class="submissions-list">
              <div v-if="filteredSubmissions.length === 0" class="empty-state">
                <svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
                  <polyline points="14 2 14 8 20 8"/>
                </svg>
                <h3>{{ getEmptyStateTitle() }}</h3>
                <p>{{ getEmptyStateMessage() }}</p>
                <button v-if="filterType !== 'all'" @click="filterType = 'all'" class="show-all-btn">
                  Show All Submissions
                </button>
              </div>

              <div v-else class="submissions-grid">
                <div 
                  v-for="submission in filteredSubmissions" 
                  :key="submission.id"
                  class="submission-card"
                  :class="submission.type"
                >
                  <!-- Student Info -->
                  <div class="submission-header">
                    <div class="student-info">
                      <div class="student-avatar">
                        {{ getInitials(submission.student_name) }}
                      </div>
                      <div>
                        <h3>{{ submission.student_name }}</h3>
                        <p class="student-id">{{ submission.student_number }}</p>
                      </div>
                    </div>
                    <span class="submission-type-badge" :class="submission.type">
                      {{ submission.type === 'quiz' ? 'Quiz' : 'Assignment' }}
                    </span>
                  </div>                  <!-- Submission Details -->
                  <div class="submission-body">
                    <h4 class="submission-title">{{ submission.title }}</h4>
                    
                    <div class="submission-meta">
                      <div class="meta-item">
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                          <circle cx="12" cy="12" r="10"/>
                          <polyline points="12 6 12 12 16 14"/>
                        </svg>
                        <span>{{ formatDate(submission.submitted_at) }}</span>
                      </div>

                      <div class="meta-item" v-if="submission.is_late">
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                          <circle cx="12" cy="12" r="10"/>
                          <line x1="12" y1="8" x2="12" y2="12"/>
                          <line x1="12" y1="16" x2="12.01" y2="16"/>
                        </svg>
                        <span class="late-indicator">Late Submission</span>
                      </div>
                    </div>

                    <!-- Score Display -->
                    <div class="score-section" v-if="submission.status === 'graded'">
                      <div class="score-display">
                        <span class="score">{{ submission.score }}</span>
                        <span class="max-score">/ {{ submission.max_score }}</span>
                      </div>
                      <div class="percentage" :class="getScoreClass(submission.percentage)">
                        {{ submission.percentage }}%
                      </div>
                    </div>

                    <div class="status-badge" v-else :class="submission.status">
                      {{ getStatusText(submission.status) }}
                    </div>
                  </div>                  <!-- Actions -->
                  <div class="submission-footer">
                    <button 
                      v-if="submission.type === 'quiz'"
                      @click="viewQuizDetails(submission)"
                      class="action-button view"
                    >
                      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/>
                        <circle cx="12" cy="12" r="3"/>
                      </svg>
                      View Details
                    </button>

                    <button 
                      v-if="submission.type === 'assignment'"
                      @click="viewAssignmentSubmission(submission)"
                      class="action-button view"
                    >
                      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/>
                        <circle cx="12" cy="12" r="3"/>
                      </svg>
                      View Submission
                    </button>

                    <button 
                      v-if="submission.type === 'assignment' && submission.status === 'submitted'"
                      @click="gradeAssignment(submission)"
                      class="action-button grade"
                    >
                      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"/>
                        <path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"/>
                      </svg>
                      Grade
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </main>
    </div>

    <!-- Grade Assignment Modal -->
    <div v-if="showGradeModal" class="modal-overlay" @click.self="closeGradeModal">
      <div class="modal-content grade-modal">
        <div class="modal-header">
          <h2>Grade Assignment</h2>
          <button @click="closeGradeModal" class="close-button">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <line x1="18" y1="6" x2="6" y2="18"/>
              <line x1="6" y1="6" x2="18" y2="18"/>
            </svg>
          </button>
        </div>

        <div class="modal-body">
          <div class="student-submission-info">
            <h3>{{ selectedSubmission?.student_name }}</h3>
            <p>{{ selectedSubmission?.title }}</p>
          </div>

          <div class="form-group">
            <label>Score (out of {{ selectedSubmission?.max_score }})</label>
            <input 
              type="number" 
              v-model.number="gradeForm.score" 
              :max="selectedSubmission?.max_score"
              min="0"
              class="form-input"
            />
          </div>

          <div class="form-group">
            <label>Feedback</label>
            <textarea 
              v-model="gradeForm.feedback" 
              rows="4"
              placeholder="Provide feedback to the student..."
              class="form-textarea"
            ></textarea>
          </div>
        </div>

        <div class="modal-footer">
          <button @click="closeGradeModal" class="button secondary">Cancel</button>
          <button @click="submitGrade" class="button primary" :disabled="submitting">
            {{ submitting ? 'Submitting...' : 'Submit Grade' }}
          </button>
        </div>
      </div>
    </div>

    <!-- Logout Confirmation Modal -->
    <div v-if="showLogoutModal" class="modal-overlay" @click.self="closeLogoutModal">
      <div class="modal-content logout-modal">
        <div class="modal-header">
          <h2>Confirm Logout</h2>
          <button @click="closeLogoutModal" class="close-button">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <line x1="18" y1="6" x2="6" y2="18"/>
              <line x1="6" y1="6" x2="18" y2="18"/>
            </svg>
          </button>
        </div>

        <div class="modal-body">
          <p>Are you sure you want to logout?</p>
        </div>

        <div class="modal-footer">
          <button @click="closeLogoutModal" class="button secondary">Cancel</button>
          <button @click="confirmLogout" class="button primary" :disabled="isLoggingOut">
            {{ isLoggingOut ? 'Logging out...' : 'Logout' }}
          </button>
        </div>
      </div>
    </div>

    <!-- View Assignment Submission Modal -->
    <div v-if="showViewSubmissionModal" class="modal-overlay" @click.self="closeViewSubmissionModal">
      <div class="modal-content view-submission-modal">
        <div class="modal-header">
          <h2>Assignment Submission Details</h2>
          <button @click="closeViewSubmissionModal" class="close-button">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <line x1="18" y1="6" x2="6" y2="18"/>
              <line x1="6" y1="6" x2="18" y2="18"/>
            </svg>
          </button>
        </div>

        <div class="modal-body" v-if="selectedSubmission">
          <!-- Student Info -->
          <div class="submission-detail-header">
            <div class="student-avatar-large">
              {{ getInitials(selectedSubmission.student_name) }}
            </div>
            <div>
              <h3>{{ selectedSubmission.student_name }}</h3>
              <p class="student-id">{{ selectedSubmission.student_number }}</p>
              <p class="submission-date">Submitted: {{ formatDate(selectedSubmission.submitted_at) }}</p>
            </div>
          </div>

          <!-- Assignment Title -->
          <div class="detail-section">
            <h4>Assignment</h4>
            <p class="assignment-title-large">{{ selectedSubmission.title }}</p>
          </div>

          <!-- Submission Status -->
          <div class="detail-section">
            <h4>Status</h4>
            <div class="status-info">
              <span class="status-badge" :class="selectedSubmission.status">
                {{ getStatusText(selectedSubmission.status) }}
              </span>
              <span v-if="selectedSubmission.is_late" class="late-badge">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <circle cx="12" cy="12" r="10"/>
                  <line x1="12" y1="8" x2="12" y2="12"/>
                  <line x1="12" y1="16" x2="12.01" y2="16"/>
                </svg>
                Late by {{ selectedSubmission.late_days }} day(s)
              </span>
            </div>
          </div>

          <!-- Score (if graded) -->
          <div class="detail-section" v-if="selectedSubmission.status === 'graded'">
            <h4>Score</h4>
            <div class="score-display-large">
              <span class="score">{{ selectedSubmission.score }}</span>
              <span class="max-score">/ {{ selectedSubmission.max_score }}</span>
              <span class="percentage" :class="getScoreClass(selectedSubmission.percentage)">
                {{ selectedSubmission.percentage }}%
              </span>
            </div>
          </div>

          <!-- Text Content -->
          <div class="detail-section" v-if="selectedSubmission.text_content">
            <h4>Text Submission</h4>
            <div class="text-content-box">
              {{ selectedSubmission.text_content }}
            </div>
          </div>

          <!-- File Attachments (Array) -->
          <div class="detail-section" v-if="selectedSubmission.attachments && selectedSubmission.attachments.length > 0">
            <h4>File Attachments ({{ selectedSubmission.attachments.length }})</h4>
            <div class="attachments-grid">
              <a 
                v-for="(attachment, index) in selectedSubmission.attachments" 
                :key="index"
                :href="getFileUrl(attachment)" 
                target="_blank" 
                :download="getFileName(attachment.name || attachment.url || attachment)"
                class="file-link"
                @click="handleFileClick(attachment, $event)"
              >
                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
                  <polyline points="14 2 14 8 20 8"/>
                </svg>
                <div class="file-info">
                  <span class="file-name">{{ getFileName(attachment.name || attachment.url || attachment) }}</span>
                  <span class="file-size" v-if="attachment.size">{{ formatFileSize(attachment.size) }}</span>
                </div>
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="download-icon">
                  <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/>
                  <polyline points="7 10 12 15 17 10"/>
                  <line x1="12" y1="15" x2="12" y2="3"/>
                </svg>
              </a>
            </div>
          </div>

          <!-- Single File URL (Legacy) -->
          <div class="detail-section" v-else-if="selectedSubmission.file_url">
            <h4>File Attachment</h4>
            <a 
              :href="getFileUrl(selectedSubmission.file_url)" 
              target="_blank" 
              :download="getFileName(selectedSubmission.file_url)"
              class="file-link"
              @click="handleFileClick(selectedSubmission.file_url, $event)"
            >
              <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
                <polyline points="14 2 14 8 20 8"/>
              </svg>
              <div class="file-info">
                <span class="file-name">{{ getFileName(selectedSubmission.file_url) }}</span>
              </div>
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="download-icon">
                <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/>
                <polyline points="7 10 12 15 17 10"/>
                <line x1="12" y1="15" x2="12" y2="3"/>
              </svg>
            </a>
          </div>

          <!-- Link Submission -->
          <div class="detail-section" v-if="selectedSubmission.link_url">
            <h4>Link Submission</h4>
            <a :href="selectedSubmission.link_url" target="_blank" class="file-link link-type">
              <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/>
                <path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/>
              </svg>
              <div class="file-info">
                <span class="file-name">{{ selectedSubmission.link_url }}</span>
              </div>
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="external-icon">
                <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/>
                <polyline points="15 3 21 3 21 9"/>
                <line x1="10" y1="14" x2="21" y2="3"/>
              </svg>
            </a>
          </div>

          <!-- Feedback (if graded) -->
          <div class="detail-section" v-if="selectedSubmission.feedback">
            <h4>Teacher Feedback</h4>
            <div class="feedback-box">
              {{ selectedSubmission.feedback }}
            </div>
          </div>
        </div>

        <div class="modal-footer">
          <button @click="closeViewSubmissionModal" class="button secondary">Close</button>
          <button 
            v-if="selectedSubmission?.status === 'submitted'"
            @click="gradeFromModal" 
            class="button primary"
          >
            Grade This Submission
          </button>
        </div>
      </div>
    </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted, onUnmounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { supabase } from '../../supabase.js';
import { useTeacherAuth } from '../../composables/useTeacherAuth.js';

const route = useRoute();
const router = useRouter();

// Authentication
const { teacherInfo, isAuthenticated } = useTeacherAuth();

// State
const loading = ref(true);
const error = ref('');
const submissions = ref<any[]>([]);
const filterType = ref('all');
const filterStatus = ref('all');
const searchQuery = ref('');
const showGradeModal = ref(false);
const showViewSubmissionModal = ref(false);
const selectedSubmission = ref<any>(null);
const submitting = ref(false);

// User profile states
const showProfileDropdown = ref(false);
const fullName = ref('Teacher');
const showLogoutModal = ref(false);
const isLoggingOut = ref(false);
const isAuthReady = ref(false);

const gradeForm = ref({
  score: 0,
  feedback: ''
});

// Route params
const subjectId = route.params.subjectId as string;
const sectionId = route.params.sectionId as string;
const subjectName = route.query.subject as string;
const sectionName = route.query.section as string;

// ============================================================
// WAIT FOR AUTH TO BE READY
// ============================================================
const waitForAuth = async (maxAttempts = 50, intervalMs = 100) => {
  return new Promise((resolve, reject) => {
    let attempts = 0
    
    // Check immediately first
    if (teacherInfo.value?.id) {
      isAuthReady.value = true
      console.log('✅ Auth already ready:', teacherInfo.value.id)
      resolve(true)
      return
    }
    
    const checkAuth = setInterval(() => {
      attempts++
      
      // Check if teacher info is available and has an ID
      if (teacherInfo.value?.id) {
        clearInterval(checkAuth)
        isAuthReady.value = true
        console.log('✅ Auth ready after', attempts, 'attempts:', teacherInfo.value.id)
        resolve(true)
        return
      }
      
      // Timeout after max attempts (5 seconds)
      if (attempts >= maxAttempts) {
        clearInterval(checkAuth)
        console.warn('⚠️ Auth timeout after', attempts, 'attempts')
        // Don't reject - just resolve anyway to prevent logout
        isAuthReady.value = false
        resolve(false)
      }
    }, intervalMs)
  })
}

// Computed
const stats = computed(() => {
  const quizSubmissions = submissions.value.filter(s => s.type === 'quiz').length;
  const assignmentSubmissions = submissions.value.filter(s => s.type === 'assignment').length;
  const pending = submissions.value.filter(s => s.status === 'submitted').length;
  const graded = submissions.value.filter(s => ['graded', 'reviewed', 'returned'].includes(s.status)).length;

  return {
    totalQuizSubmissions: quizSubmissions,
    totalAssignmentSubmissions: assignmentSubmissions,
    pendingReview: pending,
    graded: graded
  };
});

const filteredSubmissions = computed(() => {
  let filtered = submissions.value;

  // Filter by type
  if (filterType.value !== 'all') {
    filtered = filtered.filter(s => s.type === filterType.value);
  }

  // Filter by status
  if (filterStatus.value !== 'all') {
    filtered = filtered.filter(s => s.status === filterStatus.value);
  }

  // Search by student name
  if (searchQuery.value) {
    filtered = filtered.filter(s => 
      s.student_name.toLowerCase().includes(searchQuery.value.toLowerCase())
    );
  }

  return filtered;
});

// Methods
const fetchSubmissions = async () => {
  try {
    loading.value = true;
    error.value = '';

    console.log('=== FETCHING SUBMISSIONS ===');
    console.log('Section ID:', sectionId);
    console.log('Subject ID:', subjectId);

    // ============================================
    // FETCH QUIZ SUBMISSIONS
    // ============================================
    let quizData: any[] = [];
    let quizzesMap = new Map();
    
    // Get published quizzes for this section and subject
    const { data: sectionQuizzes, error: sectionQuizzesError } = await supabase
      .from('quizzes')
      .select('id, title')
      .eq('section_id', sectionId)
      .eq('subject_id', subjectId)
      .eq('status', 'published');

    if (sectionQuizzesError) {
      console.error('Error fetching quizzes:', sectionQuizzesError);
    } else {
      console.log('Published quizzes found:', sectionQuizzes?.length || 0, sectionQuizzes);
      quizzesMap = new Map(sectionQuizzes?.map(q => [q.id, q]) || []);
    }

    if (sectionQuizzes && sectionQuizzes.length > 0) {
      const quizIds = sectionQuizzes.map(q => q.id);
      
      // Fetch quiz attempts for these quizzes with submitted or graded status
      const { data: quizSubmissions, error: quizError } = await supabase
        .from('quiz_attempts')
        .select('*')
        .in('quiz_id', quizIds)
        .in('status', ['submitted', 'graded', 'reviewed']);

      if (quizError) {
        console.error('Error fetching quiz attempts:', quizError);
      } else {
        console.log('Quiz attempts found:', quizSubmissions?.length || 0, quizSubmissions);
        quizData = quizSubmissions || [];
      }
    }

    // ============================================
    // FETCH ASSIGNMENT SUBMISSIONS
    // ============================================
    let assignmentData: any[] = [];
    let assignmentsMap = new Map();
    
    // Get published assignments for this section and subject
    const { data: sectionAssignments, error: sectionAssignmentsError } = await supabase
      .from('assignments')
      .select('id, title, total_points, status, due_date, allow_late_submission')
      .eq('section_id', sectionId)
      .eq('subject_id', subjectId)
      .eq('status', 'published');

    if (sectionAssignmentsError) {
      console.error('Error fetching assignments:', sectionAssignmentsError);
    } else {
      console.log('Published assignments found:', sectionAssignments?.length || 0, sectionAssignments);
      assignmentsMap = new Map(sectionAssignments?.map(a => [a.id, a]) || []);
    }

    if (sectionAssignments && sectionAssignments.length > 0) {
      const assignmentIds = sectionAssignments.map(a => a.id);
      console.log('Looking for submissions with assignment IDs:', assignmentIds);
      
      // Fetch assignment submissions for these assignments
      // Include all statuses except 'draft'
      const { data: assignmentSubmissions, error: assignmentError } = await supabase
        .from('assignment_submissions')
        .select('*')
        .in('assignment_id', assignmentIds)
        .neq('status', 'draft');

      if (assignmentError) {
        console.error('Error fetching assignment submissions:', assignmentError);
      } else {
        console.log('Assignment submissions found:', assignmentSubmissions?.length || 0, assignmentSubmissions);
        assignmentData = assignmentSubmissions || [];
      }
    }

    // ============================================
    // GET STUDENT DETAILS
    // ============================================
    const allStudentIds = [
      ...new Set([
        ...(quizData?.map(q => q.student_id) || []),
        ...(assignmentData?.map(a => a.student_id) || [])
      ])
    ];

    console.log('Unique student IDs:', allStudentIds.length, allStudentIds);

    if (allStudentIds.length === 0) {
      console.log('No student submissions found');
      submissions.value = [];
      loading.value = false;
      return;
    }

    // Fetch student details
    const { data: studentsData, error: studentsError } = await supabase
      .from('students')
      .select('id, full_name, student_id')
      .in('id', allStudentIds);

    if (studentsError) {
      console.error('Error fetching students:', studentsError);
      throw studentsError;
    }

    console.log('Students found:', studentsData?.length || 0, studentsData);

    // Create student lookup map
    const studentsMap = new Map(studentsData?.map(s => [s.id, s]) || []);

    // ============================================
    // FORMAT QUIZ SUBMISSIONS
    // ============================================
    const formattedQuizzes = (quizData || [])
      .map((quiz: any) => {
        const student = studentsMap.get(quiz.student_id);
        const quizInfo = quizzesMap.get(quiz.quiz_id);
        
        if (!student || !quizInfo) {
          console.warn('Missing data for quiz submission:', quiz.id);
          return null;
        }
        
        return {
          id: quiz.id,
          type: 'quiz',
          quiz_id: quiz.quiz_id,
          student_id: quiz.student_id,
          student_name: student.full_name,
          student_number: student.student_id,
          title: quizInfo.title,
          submitted_at: quiz.submitted_at || quiz.created_at,
          score: quiz.total_score || 0,
          max_score: quiz.max_score || 0,
          percentage: quiz.percentage || 0,
          status: quiz.status,
          is_late: false,
          late_days: 0
        };
      })
      .filter(Boolean);

    console.log('Formatted quiz submissions:', formattedQuizzes.length, formattedQuizzes);

    // ============================================
    // FORMAT ASSIGNMENT SUBMISSIONS
    // ============================================
    const formattedAssignments = (assignmentData || [])
      .map((assignment: any) => {
        const student = studentsMap.get(assignment.student_id);
        const assignmentInfo = assignmentsMap.get(assignment.assignment_id);
        
        if (!student || !assignmentInfo) {
          console.warn('Missing data for assignment submission:', assignment.id);
          return null;
        }
        
        const score = assignment.score || 0;
        const maxScore = assignmentInfo.total_points || 100;
        const percentage = maxScore > 0 ? ((score / maxScore) * 100).toFixed(2) : '0';
        
        // Parse attachments if it's a string
        let attachments = assignment.attachments;
        if (typeof attachments === 'string') {
          try {
            attachments = JSON.parse(attachments);
          } catch (e) {
            console.warn('Failed to parse attachments:', e);
            attachments = [];
          }
        }
        
        // Ensure attachments is an array
        if (!Array.isArray(attachments)) {
          attachments = attachments ? [attachments] : [];
        }
        
        console.log('Assignment submission attachments:', {
          id: assignment.id,
          student: student.full_name,
          attachments: attachments,
          file_url: assignment.file_url,
          link_url: assignment.link_url
        });
        
        return {
          id: assignment.id,
          type: 'assignment',
          assignment_id: assignment.assignment_id,
          student_id: assignment.student_id,
          student_name: student.full_name,
          student_number: student.student_id,
          title: assignmentInfo.title,
          submitted_at: assignment.submitted_at || assignment.created_at,
          score: score,
          max_score: maxScore,
          percentage: percentage,
          status: assignment.status,
          is_late: assignment.is_late || false,
          late_days: assignment.late_days || 0,
          feedback: assignment.feedback || '',
          text_content: assignment.text_content,
          file_url: assignment.file_url,
          link_url: assignment.link_url,
          attachments: attachments
        };
      })
      .filter(Boolean);

    console.log('Formatted assignment submissions:', formattedAssignments.length, formattedAssignments);

    // ============================================
    // COMBINE AND SORT
    // ============================================
    submissions.value = [...formattedQuizzes, ...formattedAssignments]
      .sort((a, b) => {
        const dateA = new Date(a.submitted_at).getTime();
        const dateB = new Date(b.submitted_at).getTime();
        return dateB - dateA;
      });

    console.log('=== FINAL RESULTS ===');
    console.log('Total submissions:', submissions.value.length);
    console.log('Quiz submissions:', submissions.value.filter(s => s.type === 'quiz').length);
    console.log('Assignment submissions:', submissions.value.filter(s => s.type === 'assignment').length);
    console.log('All submissions:', submissions.value);

  } catch (err: any) {
    console.error('Error fetching submissions:', err);
    error.value = err.message || 'Failed to load submissions';
  } finally {
    loading.value = false;
  }
};

const formatDate = (dateString: string) => {
  if (!dateString) return 'N/A';
  const date = new Date(dateString);
  return date.toLocaleDateString('en-US', {
    month: 'short',
    day: 'numeric',
    year: 'numeric',
    hour: '2-digit',
    minute: '2-digit'
  });
};

const getInitials = (name: string) => {
  if (!name) return '?';
  return name
    .split(' ')
    .map(n => n[0])
    .join('')
    .toUpperCase()
    .slice(0, 2);
};

const getStatusText = (status: string) => {
  const statusMap: Record<string, string> = {
    submitted: 'Pending Review',
    graded: 'Graded',
    reviewed: 'Reviewed',
    returned: 'Returned',
    in_progress: 'In Progress',
    draft: 'Draft'
  };
  return statusMap[status] || status;
};

const getScoreClass = (percentage: number | string) => {
  const pct = typeof percentage === 'string' ? parseFloat(percentage) : percentage;
  if (pct >= 90) return 'excellent';
  if (pct >= 80) return 'good';
  if (pct >= 70) return 'fair';
  return 'poor';
};

const viewQuizDetails = (submission: any) => {
  router.push({
    name: 'QuizResults',
    params: {
      quizId: submission.quiz_id,
      attemptId: submission.id
    }
  });
};

const viewAssignmentSubmission = (submission: any) => {
  // Open modal to show assignment submission details
  selectedSubmission.value = submission;
  showViewSubmissionModal.value = true;
};

const gradeAssignment = (submission: any) => {
  selectedSubmission.value = submission;
  gradeForm.value.score = submission.score || 0;
  gradeForm.value.feedback = submission.feedback || '';
  showGradeModal.value = true;
};

const closeGradeModal = () => {
  showGradeModal.value = false;
  selectedSubmission.value = null;
  gradeForm.value.score = 0;
  gradeForm.value.feedback = '';
};

const closeViewSubmissionModal = () => {
  showViewSubmissionModal.value = false;
  selectedSubmission.value = null;
};

const gradeFromModal = () => {
  if (selectedSubmission.value) {
    closeViewSubmissionModal();
    gradeAssignment(selectedSubmission.value);
  }
};

const handleFileClick = (attachment: any, event: Event) => {
  const url = getFileUrl(attachment);
  console.log('📥 Opening file:', {
    attachment: attachment,
    generatedUrl: url,
    fileName: getFileName(attachment.name || attachment.url || attachment)
  });
  
  // If URL is empty or invalid, prevent default and show error
  if (!url || url === '' || url === 'undefined') {
    event.preventDefault();
    alert('Unable to access file. The file URL is missing or invalid.');
    console.error('❌ Invalid file URL:', attachment);
  }
};

const submitGrade = async () => {
  try {
    submitting.value = true;

    if (!selectedSubmission.value) {
      throw new Error('No submission selected');
    }

    // Validate score
    if (gradeForm.value.score < 0 || gradeForm.value.score > selectedSubmission.value.max_score) {
      throw new Error(`Score must be between 0 and ${selectedSubmission.value.max_score}`);
    }

    // Calculate percentage
    const percentage = ((gradeForm.value.score / selectedSubmission.value.max_score) * 100).toFixed(2);

    console.log('📝 Submitting grade:', {
      submissionId: selectedSubmission.value.id,
      score: gradeForm.value.score,
      maxScore: selectedSubmission.value.max_score,
      percentage: percentage,
      feedback: gradeForm.value.feedback
    });

    // Use teacherInfo from composable (already loaded)
    if (!teacherInfo.value?.id) {
      throw new Error('Teacher information not available');
    }

    const teacherId = teacherInfo.value.id;
    console.log('✅ Using teacher ID:', teacherId);

    // Update the assignment submission with ALL required fields
    const { data: updateData, error: updateError } = await supabase
      .from('assignment_submissions')
      .update({
        score: Number(gradeForm.value.score),
        feedback: gradeForm.value.feedback || null,
        status: 'graded',
        graded_by: teacherId,
        graded_at: new Date().toISOString(),
        updated_at: new Date().toISOString()
      })
      .eq('id', selectedSubmission.value.id)
      .select();

    if (updateError) {
      console.error('❌ Update error:', updateError);
      throw new Error(`Database error: ${updateError.message}`);
    }

    if (!updateData || updateData.length === 0) {
      console.error('❌ No data returned from update');
      throw new Error('Failed to update submission - no data returned');
    }

    console.log('✅ Grade saved successfully:', updateData[0]);

    // Update local data with the actual database response
    const index = submissions.value.findIndex(s => s.id === selectedSubmission.value.id);
    if (index !== -1) {
      submissions.value[index] = {
        ...submissions.value[index],
        score: Number(gradeForm.value.score),
        status: 'graded',
        percentage: percentage,
        feedback: gradeForm.value.feedback
      };
      console.log('✅ Local data updated:', submissions.value[index]);
    }

    closeGradeModal();
    alert('Grade submitted successfully!');

    // Optionally refresh the data from server to ensure sync
    await fetchSubmissions();

  } catch (err: any) {
    console.error('💥 Error submitting grade:', err);
    alert('Failed to submit grade: ' + err.message);
  } finally {
    submitting.value = false;
  }
};

const goBack = () => {
  router.back();
};

const getEmptyStateTitle = () => {
  if (filterType.value === 'quiz') return 'No Quiz Submissions';
  if (filterType.value === 'assignment') return 'No Assignment Submissions';
  return 'No Submissions Found';
};

const getEmptyStateMessage = () => {
  if (submissions.value.length === 0) {
    return 'Students haven\'t submitted any work for this section yet.';
  }
  
  if (filterType.value === 'quiz') {
    return 'No quiz submissions match your current filters.';
  }
  if (filterType.value === 'assignment') {
    return 'No assignment submissions match your current filters.';
  }
  
  if (searchQuery.value) {
    return `No submissions found for "${searchQuery.value}".`;
  }
  
  return 'No student submissions match your current filters.';
};

const getFileName = (urlOrPath: string) => {
  if (!urlOrPath) return 'File';
  
  // If it's an object with a name property
  if (typeof urlOrPath === 'object' && urlOrPath.name) {
    return urlOrPath.name;
  }
  
  // Extract filename from URL or path
  const parts = urlOrPath.split('/');
  const filename = parts[parts.length - 1];
  
  // Decode URL encoding
  try {
    return decodeURIComponent(filename);
  } catch {
    return filename;
  }
};

const formatFileSize = (bytes: number) => {
  if (!bytes) return '';
  
  const sizes = ['Bytes', 'KB', 'MB', 'GB'];
  const i = Math.floor(Math.log(bytes) / Math.log(1024));
  return Math.round(bytes / Math.pow(1024, i) * 100) / 100 + ' ' + sizes[i];
};

const getFileUrl = (attachment: any) => {
  console.log('🔍 Processing attachment:', attachment);
  
  // If attachment is a string, it might be a path or URL
  if (typeof attachment === 'string') {
    // If it's already a full URL, return it
    if (attachment.startsWith('http://') || attachment.startsWith('https://')) {
      console.log('✅ Already a full URL:', attachment);
      return attachment;
    }
    
    // If it's a storage path, generate public URL
    if (attachment.includes('/')) {
      try {
        const { data } = supabase.storage
          .from('assignment-attachments')
          .getPublicUrl(attachment);
        
        console.log('📎 Generated public URL for path:', attachment, '→', data.publicUrl);
        return data.publicUrl;
      } catch (error) {
        console.warn('⚠️ Failed to generate public URL:', error);
        return attachment;
      }
    }
    
    return attachment;
  }
  
  // If attachment is an object with url property that's already a full URL
  if (attachment?.url) {
    if (attachment.url.startsWith('http://') || attachment.url.startsWith('https://')) {
      console.log('✅ Object with full URL:', attachment.url);
      return attachment.url;
    }
    
    // If url is a path, generate public URL
    if (attachment.url.includes('/')) {
      try {
        const { data } = supabase.storage
          .from('assignment-attachments')
          .getPublicUrl(attachment.url);
        
        console.log('📎 Generated public URL for object.url:', attachment.url, '→', data.publicUrl);
        return data.publicUrl;
      } catch (error) {
        console.warn('⚠️ Failed to generate public URL:', error);
        return attachment.url;
      }
    }
    
    return attachment.url;
  }
  
  // If attachment has path property
  if (attachment?.path) {
    try {
      const { data } = supabase.storage
        .from('assignment-attachments')
        .getPublicUrl(attachment.path);
      
      console.log('📎 Generated public URL for object.path:', attachment.path, '→', data.publicUrl);
      return data.publicUrl;
    } catch (error) {
      console.warn('⚠️ Failed to generate public URL:', error);
      return attachment.path;
    }
  }
  
  console.warn('⚠️ Could not extract URL from attachment:', attachment);
  return '';
};

// Profile dropdown toggle
const toggleProfileDropdown = () => {
  showProfileDropdown.value = !showProfileDropdown.value;
};

// Logout modal functions
const openLogoutModal = () => {
  showLogoutModal.value = true;
  showProfileDropdown.value = false;
};

const closeLogoutModal = () => {
  showLogoutModal.value = false;
  isLoggingOut.value = false;
};

const confirmLogout = async () => {
  console.log('🚪 Logout confirmed - starting process...');
  isLoggingOut.value = true;
  showLogoutModal.value = false;
  
  // Clear any local state
  localStorage.removeItem('teacherInfo');
  sessionStorage.clear();
  
  // Sign out from Supabase
  supabase.auth.signOut().catch(err => console.log('Signout error:', err));
  
  // Immediate redirect - no waiting!
  setTimeout(() => {
    window.location.assign('/login');
  }, 100);
  
  console.log('✅ Logout initiated');
};

const logout = () => {
  openLogoutModal();
};

// Click outside handler
const handleClickOutside = (event: any) => {
  const target = event.target as HTMLElement;
  if (!target.closest('.user-profile-wrapper')) {
    showProfileDropdown.value = false;
  }
};

// Lifecycle
onMounted(async () => {
  console.log('StudentSubmissions mounted with params:', {
    subjectId,
    sectionId,
    subjectName,
    sectionName
  });
  
  // Set up click handler
  document.addEventListener('click', handleClickOutside);
  
  // Validate route params first
  if (!sectionId) {
    error.value = 'Section ID is missing';
    loading.value = false;
    return;
  }

  if (!subjectId) {
    error.value = 'Subject ID is missing';
    loading.value = false;
    return;
  }
  
  try {
    console.log('� Initializing authentication...');
    
    // Wait for teacherInfo to be fully loaded with retry logic
    try {
      await waitForAuth(30, 200); // Wait up to 6 seconds
      
      // Load teacher name using the teacherInfo.value.id
      try {
        const { data: teacher, error: teacherError } = await supabase
          .from('teachers')
          .select('full_name')
          .eq('id', teacherInfo.value.id)
          .single();
          
        if (!teacherError && teacher) {
          fullName.value = teacher.full_name || 'Teacher';
          console.log('✅ Teacher loaded:', { id: teacherInfo.value.id, name: fullName.value });
        } else {
          console.warn('⚠️ Teacher not found:', teacherError);
          fullName.value = 'Teacher';
        }
      } catch (err) {
        console.warn('⚠️ Failed to load teacher name:', err);
        fullName.value = 'Teacher';
      }
      
      // Fetch submissions only after auth is confirmed ready
      console.log('📚 Fetching submissions...');
      await fetchSubmissions();
      
    } catch (authError) {
      console.error('❌ Auth timeout:', authError);
      
      // Still try to fetch if we have any auth info
      if (teacherInfo.value?.id) {
        console.log('⚠️ Attempting to fetch with partial auth...');
        fullName.value = 'Teacher';
        await fetchSubmissions();
      } else {
        // Don't redirect to login - just show error and keep page loaded
        error.value = 'Could not verify authentication. Please reload the page.';
        fullName.value = 'Teacher';
        loading.value = false;
      }
    }
    
  } catch (err) {
    console.error('❌ Component mount error:', err);
    error.value = 'Failed to initialize page. Please reload.';
    loading.value = false;
    
    // Try to continue if we have auth
    if (teacherInfo.value?.id) {
      console.log('⚠️ Attempting recovery...');
      isAuthReady.value = true;
      await fetchSubmissions();
    }
  }
});

onUnmounted(() => {
  document.removeEventListener('click', handleClickOutside);
});
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

/* ===============================================
   MODERN UI SYSTEM - CONSISTENT WITH MYSUBJECTS
   =============================================== */

/* Reset and Base */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.student-submissions {
  min-height: 100vh;
  width: 100vw;
  background: #f8fafc;
  font-family: 'Inter', sans-serif;
  overflow-x: hidden;
}

.dark .student-submissions {
  background: #0f172a;
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
  color: white;
  opacity: 0.7;
  transition: transform 0.2s;
}

.user-profile:hover .dropdown-arrow {
  opacity: 1;
}

/* Profile Dropdown */
.profile-dropdown {
  position: absolute;
  top: calc(100% + 0.5rem);
  right: 0;
  background: white;
  border-radius: 12px;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.15);
  min-width: 260px;
  z-index: 1000;
  overflow: hidden;
  animation: slideDown 0.2s ease;
}

.dark .profile-dropdown {
  background: #1e293b;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4);
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

.dropdown-header {
  padding: 1.5rem;
  background: linear-gradient(135deg, #3D8D7A, #2d6a5a);
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
  color: white;
  font-size: 1rem;
  font-weight: 600;
  margin: 0 0 0.25rem 0;
}

.profile-details p {
  color: rgba(255, 255, 255, 0.9);
  font-size: 0.875rem;
  margin: 0;
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
  color: #374151;
  text-decoration: none;
  transition: all 0.2s;
  cursor: pointer;
  border: none;
  background: none;
  width: 100%;
  font-size: 0.9rem;
  font-weight: 500;
}

.dark .dropdown-item {
  color: #e2e8f0;
}

.dropdown-item:hover {
  background: #f3f4f6;
}

.dark .dropdown-item:hover {
  background: #334155;
}

.dropdown-item svg {
  color: #6b7280;
}

.dark .dropdown-item svg {
  color: #94a3b8;
}

.dropdown-item:hover svg {
  color: #3D8D7A;
}

.dropdown-divider {
  height: 1px;
  background: #e5e7eb;
  margin: 0.5rem 0;
}

.dark .dropdown-divider {
  background: #334155;
}

.logout-btn {
  color: #dc2626;
}

.dark .logout-btn {
  color: #ef4444;
}

.logout-btn:hover {
  background: #fee2e2;
}

.dark .logout-btn:hover {
  background: rgba(239, 68, 68, 0.1);
}

.logout-btn svg {
  color: #dc2626;
}

.dark .logout-btn svg {
  color: #ef4444;
}

/* Rounded semi-transparent backgrounds */
.rounded-bg {
  background: rgba(255,255,255,0.13);
  border-radius: 16px;
  transition: background 0.2s;
}

.rounded-bg:hover {
  background: rgba(255,255,255,0.22);
}

/* Main Content */
.main-content {
  margin-top: 64px;
  padding: 1.5rem;
  width: 100%;
  height: calc(100vh - 64px);
  position: relative;
  overflow-y: auto;
  overflow-x: hidden;
  scroll-behavior: smooth;
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

.dark .page-header {
  background: #1e293b;
  border-color: #334155;
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

.back-btn {
  background: #3D8D7A;
  border: none;
  padding: 1rem 1.5rem;
  border-radius: 12px;
  color: white;
  font-weight: 600;
  font-size: 1rem;
  cursor: pointer;
  transition: all 0.2s ease;
  display: flex;
  align-items: center;
  gap: 0.75rem;
  box-shadow: 0 2px 8px rgba(61, 141, 122, 0.2);
}

.back-btn:hover {
  background: #2d6a5a;
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(61, 141, 122, 0.3);
}

.back-btn svg {
  width: 24px;
  height: 24px;
}

.dark .back-btn {
  background: #3D8D7A;
  color: white;
}

.dark .back-btn:hover {
  background: #2d6a5a;
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

.dark .header-title {
  color: #f1f5f9;
}

.header-subtitle {
  font-size: 0.95rem;
  color: #64748b;
}

.dark .header-subtitle {
  color: #94a3b8;
}

.loading-container,
.error-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 4rem 2rem;
  color: #6b7280;
}

.loading-spinner {
  width: 48px;
  height: 48px;
  border: 4px solid #e5e7eb;
  border-top-color: #3D8D7A;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

.error-container svg {
  color: #ef4444;
  margin-bottom: 1rem;
}

.retry-button {
  margin-top: 1rem;
  padding: 0.5rem 1.5rem;
  background: #3D8D7A;
  color: white;
  border: none;
  border-radius: 0.375rem;
  cursor: pointer;
  transition: all 0.2s ease;
}

.retry-button:hover {
  background: #2d6a5a;
}

.submissions-container {
  max-width: 1400px;
  margin: 0 auto;
  padding: 2rem;
}

.filters-section {
  background: white;
  padding: 1.5rem;
  border-radius: 0.75rem;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
  margin-bottom: 2rem;
}

.filter-group {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.filter-group label {
  font-size: 0.875rem;
  font-weight: 500;
  color: #374151;
}

.filter-select,
.search-input {
  padding: 0.625rem;
  border: 1px solid #d1d5db;
  border-radius: 0.375rem;
  font-size: 0.875rem;
  transition: border-color 0.2s;
}

.filter-select:focus,
.search-input:focus {
  outline: none;
  border-color: #3b82f6;
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
}

.content-wrapper {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
}

.submissions-container {
  max-width: 1400px;
  margin: 0 auto;
  padding: 0;
  height: 100%;
  overflow-y: auto;
}

.filters-section {
  background: white;
  padding: 1.5rem;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
  margin-bottom: 2rem;
  border: 1px solid #e2e8f0;
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.dark .filters-section {
  background: #1e293b;
  border-color: #334155;
}

.search-container {
  width: 100%;
}

.filter-tabs {
  display: flex;
  gap: 0.5rem;
  flex-wrap: wrap;
}

.filter-tab {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1.25rem;
  border: 2px solid #e5e7eb;
  border-radius: 12px;
  background: white;
  color: #6b7280;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s ease;
  font-size: 0.875rem;
}

.filter-tab:hover {
  border-color: #d1d5db;
  background: #f9fafb;
}

.filter-tab.active {
  border-color: #3D8D7A;
  background: #3D8D7A;
  color: white;
}

.filter-tab.quiz-tab.active {
  border-color: #3b82f6;
  background: #3b82f6;
}

.filter-tab.assignment-tab.active {
  border-color: #f59e0b;
  background: #f59e0b;
}

.filter-tab .count {
  background: rgba(255, 255, 255, 0.2);
  padding: 0.25rem 0.5rem;
  border-radius: 6px;
  font-size: 0.75rem;
  font-weight: 600;
}

.filter-tab:not(.active) .count {
  background: #e5e7eb;
  color: #6b7280;
}

.status-filter-container {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.filter-label {
  font-size: 0.875rem;
  font-weight: 500;
  color: #374151;
  white-space: nowrap;
}

.dark .filter-label {
  color: #e2e8f0;
}

.dark .filter-tab {
  background: #1e293b;
  border-color: #334155;
  color: #94a3b8;
}

.dark .filter-tab:hover {
  background: #334155;
  border-color: #475569;
}

.dark .filter-tab.active {
  color: white;
}

.results-summary {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 1.5rem;
  background: #f8fafc;
  border-radius: 12px;
  margin-bottom: 1rem;
  border: 1px solid #e2e8f0;
}

.dark .results-summary {
  background: #0f172a;
  border-color: #1e293b;
}

.results-text {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.results-count {
  font-size: 1.125rem;
  font-weight: 700;
  color: #3D8D7A;
}

.results-label {
  font-size: 0.875rem;
  color: #6b7280;
}

.dark .results-label {
  color: #94a3b8;
}

.active-filter {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.875rem;
  color: #6b7280;
  background: white;
  padding: 0.5rem 0.75rem;
  border-radius: 8px;
  border: 1px solid #e5e7eb;
}

.dark .active-filter {
  background: #1e293b;
  border-color: #334155;
  color: #94a3b8;
}

.search-input-container {
  position: relative;
  flex: 1;
}

.search-icon {
  position: absolute;
  left: 1rem;
  top: 50%;
  transform: translateY(-50%);
  color: #6b7280;
}

.search-input {
  width: 100%;
  padding: 0.75rem 1rem 0.75rem 3rem;
  border: 1px solid #e5e7eb;
  border-radius: 12px;
  font-size: 1rem;
  background: white;
  transition: all 0.2s ease;
}
.search-input:focus {
  outline: none;
  border-color: #3D8D7A;
  box-shadow: 0 0 0 3px rgba(61, 141, 122, 0.1);
}
.dark .search-input {
  background: #1e293b;
  border-color: #334155;
  color: #e2e8f0;
}

.status-filter {
  padding: 0.75rem 1rem;
  border: 1px solid #e5e7eb;
  border-radius: 12px;
  background: white;
  min-width: 180px;
  font-size: 0.875rem;
  cursor: pointer;
  transition: all 0.2s ease;
}

.status-filter:focus {
  outline: none;
  border-color: #3D8D7A;
  box-shadow: 0 0 0 3px rgba(61, 141, 122, 0.1);
}

.dark .status-filter {
  background: #1e293b;
  border-color: #334155;
  color: #e2e8f0;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
  margin-bottom: 2rem;
}

.stat-card {
  background: white;
  padding: 1.5rem;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
  display: flex;
  align-items: center;
  gap: 1rem;
  border: 1px solid #e2e8f0;
}

.dark .stat-card {
  background: #1e293b;
  border-color: #334155;
}

.stat-icon {
  width: 48px;
  height: 48px;
  border-radius: 0.75rem;
  display: flex;
  align-items: center;
  justify-content: center;
}

.stat-icon.quiz {
  background: linear-gradient(135deg, #dbeafe, #bfdbfe);
  color: #3b82f6;
}

.stat-icon.assignment {
  background: linear-gradient(135deg, #fef3c7, #fde68a);
  color: #f59e0b;
}

.stat-icon.pending {
  background: linear-gradient(135deg, #fce7f3, #fbcfe8);
  color: #ec4899;
}

.stat-icon.graded {
  background: linear-gradient(135deg, #d1fae5, #a7f3d0);
  color: #10b981;
}

.stat-info h3 {
  font-size: 1.875rem;
  font-weight: 700;
  color: #111827;
  margin: 0;
}

.dark .stat-info h3 {
  color: #f1f5f9;
}

.stat-info p {
  color: #6b7280;
  font-size: 0.875rem;
  margin: 0;
}

.dark .stat-info p {
  color: #94a3b8;
}

.submissions-list {
  background: white;
  padding: 1.5rem;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
  border: 1px solid #e2e8f0;
  max-height: 70vh;
  overflow-y: auto;
  scrollbar-width: thin;
  scrollbar-color: #cbd5e1 #f1f5f9;
}

.dark .submissions-list {
  background: #1e293b;
  border-color: #334155;
}

.submissions-list::-webkit-scrollbar {
  width: 6px;
}

.submissions-list::-webkit-scrollbar-track {
  background: #f1f5f9;
  border-radius: 3px;
}

.submissions-list::-webkit-scrollbar-thumb {
  background: #cbd5e1;
  border-radius: 3px;
}

.submissions-list::-webkit-scrollbar-thumb:hover {
  background: #94a3b8;
}

.empty-state {
  text-align: center;
  padding: 4rem 2rem;
  color: #6b7280;
}

.empty-state svg {
  color: #d1d5db;
  margin-bottom: 1rem;
}

.empty-state h3 {
  font-size: 1.25rem;
  font-weight: 600;
  color: #374151;
  margin: 0.5rem 0;
}

.dark .empty-state h3 {
  color: #f1f5f9;
}

.empty-state p {
  color: #6b7280;
  margin-bottom: 1.5rem;
}

.dark .empty-state p {
  color: #94a3b8;
}

.show-all-btn {
  background: #3D8D7A;
  color: white;
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 8px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s ease;
}

.show-all-btn:hover {
  background: #2d6a5a;
  transform: translateY(-1px);
}

.submissions-grid {
  display: grid;
  gap: 1.5rem;
}

.submission-card {
  border: 1px solid #e5e7eb;
  border-radius: 16px;
  padding: 1.5rem;
  transition: all 0.2s;
  background: white;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
}

.submission-card:hover {
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
  transform: translateY(-2px);
  border-color: #3D8D7A;
}

.dark .submission-card {
  background: #1e293b;
  border-color: #334155;
}

.dark .submission-card:hover {
  border-color: #3D8D7A;
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3);
}

.submission-card.quiz {
  border-left: 4px solid #3b82f6;
}

.submission-card.assignment {
  border-left: 4px solid #f59e0b;
}

.submission-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
  padding-bottom: 1rem;
  border-bottom: 1px solid #e5e7eb;
}

.student-info {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.student-avatar {
  width: 48px;
  height: 48px;
  border-radius: 50%;
  background: linear-gradient(135deg, #3D8D7A 0%, #2d6a5a 100%);
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 600;
  font-size: 1rem;
}

.student-info h3 {
  font-size: 1rem;
  font-weight: 600;
  color: #111827;
  margin: 0;
}

.dark .student-info h3 {
  color: #f1f5f9;
}

.student-id {
  font-size: 0.875rem;
  color: #6b7280;
  margin: 0.25rem 0 0 0;
}

.dark .student-id {
  color: #94a3b8;
}

.submission-type-badge {
  padding: 0.375rem 0.75rem;
  border-radius: 9999px;
  font-size: 0.75rem;
  font-weight: 500;
}

.submission-type-badge.quiz {
  background: #dbeafe;
  color: #1e40af;
}

.submission-type-badge.assignment {
  background: #fef3c7;
  color: #92400e;
}

.submission-body {
  margin-bottom: 1rem;
}

.submission-title {
  font-size: 1.125rem;
  font-weight: 600;
  color: #111827;
  margin: 0 0 1rem 0;
}

.submission-meta {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
  margin-bottom: 1rem;
}

.meta-item {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.875rem;
  color: #6b7280;
}

.late-indicator {
  color: #dc2626;
  font-weight: 500;
}

.score-section {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1rem;
  background: #f9fafb;
  border-radius: 0.5rem;
}

.score-display {
  font-size: 1.5rem;
  font-weight: 700;
  color: #111827;
}

.max-score {
  color: #6b7280;
  font-size: 1.25rem;
}

.percentage {
  padding: 0.5rem 1rem;
  border-radius: 9999px;
  font-weight: 600;
  font-size: 0.875rem;
}

.percentage.excellent {
  background: #d1fae5;
  color: #065f46;
}

.percentage.good {
  background: #dbeafe;
  color: #1e40af;
}

.percentage.fair {
  background: #fef3c7;
  color: #92400e;
}

.percentage.poor {
  background: #fee2e2;
  color: #991b1b;
}

.status-badge {
  display: inline-block;
  padding: 0.5rem 1rem;
  border-radius: 9999px;
  font-size: 0.875rem;
  font-weight: 500;
}

.status-badge.submitted {
  background: #fef3c7;
  color: #92400e;
}

.status-badge.graded {
  background: #d1fae5;
  color: #065f46;
}

.submission-footer {
  display: flex;
  gap: 0.75rem;
  padding-top: 1rem;
  border-top: 1px solid #e5e7eb;
}

.action-button {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  padding: 0.625rem 1rem;
  border: none;
  border-radius: 0.375rem;
  font-size: 0.875rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s;
}

.action-button.view {
  background: #eff6ff;
  color: #1e40af;
}

.action-button.view:hover {
  background: #dbeafe;
}

.action-button.grade {
  background: #3D8D7A;
  color: white;
}

.action-button.grade:hover {
  background: #2d6a5a;
}

/* Modal Styles */
.modal-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 50;
  padding: 1rem;
}

.modal-content {
  background: white;
  border-radius: 0.75rem;
  max-width: 600px;
  width: 100%;
  max-height: 90vh;
  overflow-y: auto;
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.5rem;
  border-bottom: 1px solid #e5e7eb;
}

.modal-header h2 {
  font-size: 1.5rem;
  font-weight: 700;
  color: #111827;
  margin: 0;
}

.close-button {
  background: none;
  border: none;
  cursor: pointer;
  color: #6b7280;
  padding: 0.5rem;
  border-radius: 0.375rem;
  transition: all 0.2s;
}

.close-button:hover {
  background: #f3f4f6;
  color: #374151;
}

.modal-body {
  padding: 1.5rem;
}

.student-submission-info {
  margin-bottom: 1.5rem;
  padding: 1rem;
  background: #f9fafb;
  border-radius: 0.5rem;
}

.student-submission-info h3 {
  font-size: 1.125rem;
  font-weight: 600;
  color: #111827;
  margin: 0 0 0.25rem 0;
}

.student-submission-info p {
  color: #6b7280;
  margin: 0;
}

.form-group {
  margin-bottom: 1.5rem;
}

.form-group label {
  display: block;
  font-size: 0.875rem;
  font-weight: 500;
  color: #374151;
  margin-bottom: 0.5rem;
}

.form-input,
.form-textarea {
  width: 100%;
  padding: 0.625rem;
  border: 1px solid #d1d5db;
  border-radius: 0.375rem;
  font-size: 0.875rem;
  transition: border-color 0.2s;
}

.form-input:focus,
.form-textarea:focus {
  outline: none;
  border-color: #3D8D7A;
  box-shadow: 0 0 0 3px rgba(61, 141, 122, 0.1);
}

.modal-footer {
  display: flex;
  justify-content: flex-end;
  gap: 0.75rem;
  padding: 1.5rem;
  border-top: 1px solid #e5e7eb;
}

.button {
  padding: 0.625rem 1.5rem;
  border: none;
  border-radius: 0.375rem;
  font-size: 0.875rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s;
}

.button.secondary {
  background: #f3f4f6;
  color: #374151;
}

.button.secondary:hover {
  background: #e5e7eb;
}

.button.primary {
  background: #3D8D7A;
  color: white;
}

.button.primary:hover {
  background: #2d6a5a;
}

.button.primary:disabled {
  background: #9ca3af;
  cursor: not-allowed;
}

/* Responsive Design */
@media (max-width: 768px) {
  .page-header {
    padding: 1rem;
  }

  .submissions-container {
    padding: 1rem;
  }

  .filters-section {
    padding: 1rem;
    gap: 1rem;
  }

  .filter-tabs {
    flex-direction: column;
    gap: 0.75rem;
  }

  .filter-tab {
    width: 100%;
    justify-content: center;
    padding: 1rem;
  }

  .status-filter-container {
    flex-direction: column;
    align-items: flex-start;
    gap: 0.5rem;
  }

  .status-filter {
    width: 100%;
  }

  .stats-grid {
    grid-template-columns: 1fr;
  }

  .submission-footer {
    flex-direction: column;
  }

  .action-button {
    width: 100%;
  }
  
  .header-content {
    flex-direction: column;
    align-items: flex-start;
  }
  
  .header-left {
    width: 100%;
  }
  
  .main-content {
    padding: 1rem;
  }

  .submissions-list {
    max-height: 60vh;
    padding: 1rem;
  }

  .results-summary {
    flex-direction: column;
    align-items: flex-start;
    gap: 0.75rem;
    padding: 1rem;
  }

  .active-filter {
    font-size: 0.8rem;
  }
}

@media (max-width: 480px) {
  .filter-tab {
    font-size: 0.8rem;
    padding: 0.875rem;
  }

  .filter-tab svg {
    width: 16px;
    height: 16px;
  }

  .stats-grid {
    grid-template-columns: 1fr;
    gap: 1rem;
  }

  .stat-card {
    padding: 1rem;
  }

  .submissions-list {
    max-height: 50vh;
  }
}

/* View Submission Modal Styles */
.view-submission-modal {
  max-width: 800px;
}

.submission-detail-header {
  display: flex;
  align-items: center;
  gap: 1.5rem;
  padding: 1.5rem;
  background: linear-gradient(135deg, #3D8D7A, #2d6a5a);
  border-radius: 12px;
  margin-bottom: 1.5rem;
  color: white;
}

.student-avatar-large {
  width: 64px;
  height: 64px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.2);
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 1.5rem;
  color: white;
}

.submission-detail-header h3 {
  font-size: 1.5rem;
  font-weight: 700;
  color: white;
  margin: 0 0 0.25rem 0;
}

.submission-detail-header .student-id {
  font-size: 0.875rem;
  color: rgba(255, 255, 255, 0.9);
  margin: 0.25rem 0;
}

.submission-detail-header .submission-date {
  font-size: 0.875rem;
  color: rgba(255, 255, 255, 0.8);
  margin: 0.25rem 0 0 0;
}

.detail-section {
  margin-bottom: 1.5rem;
  padding-bottom: 1.5rem;
  border-bottom: 1px solid #e5e7eb;
}

.detail-section:last-child {
  border-bottom: none;
  margin-bottom: 0;
  padding-bottom: 0;
}

.detail-section h4 {
  font-size: 0.875rem;
  font-weight: 600;
  color: #6b7280;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin: 0 0 0.75rem 0;
}

.assignment-title-large {
  font-size: 1.25rem;
  font-weight: 600;
  color: #111827;
  margin: 0;
}

.dark .assignment-title-large {
  color: #f1f5f9;
}

.status-info {
  display: flex;
  align-items: center;
  gap: 1rem;
  flex-wrap: wrap;
}

.late-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem 1rem;
  background: #fee2e2;
  color: #991b1b;
  border-radius: 8px;
  font-size: 0.875rem;
  font-weight: 500;
}

.score-display-large {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1.5rem;
  background: #f9fafb;
  border-radius: 12px;
}

.dark .score-display-large {
  background: #0f172a;
}

.score-display-large .score {
  font-size: 2.5rem;
  font-weight: 700;
  color: #3D8D7A;
}

.score-display-large .max-score {
  font-size: 1.5rem;
  color: #6b7280;
}

.score-display-large .percentage {
  margin-left: auto;
  font-size: 1.25rem;
}

.text-content-box {
  padding: 1.5rem;
  background: #f9fafb;
  border-radius: 12px;
  border: 1px solid #e5e7eb;
  white-space: pre-wrap;
  word-break: break-word;
  color: #374151;
  line-height: 1.6;
  max-height: 300px;
  overflow-y: auto;
}

.dark .text-content-box {
  background: #0f172a;
  border-color: #1e293b;
  color: #e2e8f0;
}

.file-link {
  display: inline-flex;
  align-items: center;
  gap: 0.75rem;
  padding: 1rem 1.5rem;
  background: #eff6ff;
  border: 1px solid #dbeafe;
  border-radius: 12px;
  color: #1e40af;
  text-decoration: none;
  font-weight: 500;
  transition: all 0.2s ease;
  width: 100%;
}

.file-link:hover {
  background: #dbeafe;
  border-color: #bfdbfe;
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(59, 130, 246, 0.2);
}

.file-link.link-type {
  background: #f0fdf4;
  border-color: #bbf7d0;
  color: #166534;
}

.file-link.link-type:hover {
  background: #dcfce7;
  border-color: #86efac;
}

.file-info {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
  flex: 1;
  min-width: 0;
}

.file-name {
  font-weight: 500;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.file-size {
  font-size: 0.75rem;
  opacity: 0.7;
}

.download-icon,
.external-icon {
  flex-shrink: 0;
  opacity: 0.6;
}

.file-link:hover .download-icon,
.file-link:hover .external-icon {
  opacity: 1;
}

.attachments-grid {
  display: grid;
  gap: 0.75rem;
}

.dark .file-link {
  background: rgba(59, 130, 246, 0.1);
  border-color: rgba(59, 130, 246, 0.2);
  color: #60a5fa;
}

.dark .file-link:hover {
  background: rgba(59, 130, 246, 0.15);
  border-color: rgba(59, 130, 246, 0.3);
}

.feedback-box {
  padding: 1.5rem;
  background: #fef3c7;
  border: 1px solid #fde68a;
  border-radius: 12px;
  color: #92400e;
  line-height: 1.6;
  white-space: pre-wrap;
  word-break: break-word;
}

.dark .feedback-box {
  background: rgba(254, 243, 199, 0.1);
  border-color: rgba(253, 230, 138, 0.2);
  color: #fbbf24;
}
</style>