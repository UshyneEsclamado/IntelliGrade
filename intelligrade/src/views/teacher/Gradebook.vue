<template>
  <div class="analytics-container" :class="{ 'dark': isDarkMode }">
    <!-- Top Navigation Bar (Same as Dashboard) -->
    <nav class="top-navbar">
      <div class="navbar-content">
        <!-- Left: Logo and Brand -->
        <div class="navbar-left">
          <div class="brand-logo">
            <img src="@/assets/LOGO WAY BG.png" alt="IntelliGrade" class="logo-img" />
            <span class="brand-name">IntelliGrade</span>
          </div>
        </div>
        
        <!-- Center: Navigation Links -->
        <div class="navbar-center">
          <router-link to="/teacher/dashboard" class="nav-item">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M10,20V14H14V20H19V12H22L12,3L2,12H5V20H10Z" />
            </svg>
            <span>Dashboard</span>
          </router-link>
          
          <router-link to="/teacher/subjects" class="nav-item">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M12,3L1,9L12,15L21,10.09V17H23V9M5,13.18V17.18L12,21L19,17.18V13.18L12,17L5,13.18Z"/>
            </svg>
            <span>Classes</span>
          </router-link>
          
          <router-link to="/teacher/gradebook" class="nav-item active">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M19,3H14.82C14.4,1.84 13.3,1 12,1C10.7,1 9.6,1.84 9.18,3H5A2,2 0 0,0 3,5V19A2,2 0 0,0 5,21H19A2,2 0 0,0 21,19V5A2,2 0 0,0 19,3M12,3A1,1 0 0,1 13,4A1,1 0 0,1 12,5A1,1 0 0,1 11,4A1,1 0 0,1 12,3Z" />
            </svg>
            <span>Gradebook</span>
          </router-link>
          
          <router-link to="/teacher/analytics" class="nav-item">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M22,21H2V3H4V19H6V10H10V19H12V6H16V19H18V14H22V21Z" />
            </svg>
            <span>Analytics</span>
          </router-link>
          
          <router-link to="/teacher/messages" class="nav-item">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>
            </svg>
            <span>Messages</span>
          </router-link>
          
          <router-link to="/teacher/upload-assessment" class="nav-item">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M9,16V10H5L12,3L19,10H15V16H9M5,20V18H19V20H5Z" />
            </svg>
            <span>Upload</span>
          </router-link>
        </div>
        
        <!-- Right: Search and Actions -->
        <div class="navbar-right">
          <div class="search-box">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <circle cx="11" cy="11" r="8"></circle>
              <path d="M21 21L16.65 16.65"></path>
            </svg>
            <input 
              v-model="searchQuery" 
              type="text" 
              placeholder="Search..."
            >
          </div>
          <button @click="refreshData" class="export-btn refresh-btn" :disabled="loading">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" :class="{ 'spinning': loading }">
              <polyline points="23 4 23 10 17 10"></polyline>
              <polyline points="1 20 1 14 7 14"></polyline>
              <path d="M20.49 9A9 9 0 0 0 5.64 5.64L1 10m22 4l-4.64 4.36A9 9 0 0 1 3.51 15"></path>
            </svg>
            <span>Refresh</span>
          </button>
        </div>
      </div>
    </nav>

    <!-- Main Content Area -->
    <main class="main-content">
      <!-- Page Header -->
      <div class="page-header">
        <div class="header-content">
          <div class="header-left">
            <div class="header-icon">
              <svg width="28" height="28" viewBox="0 0 24 24" fill="currentColor">
                <path d="M14,2H6A2,2 0 0,0 4,4V20A2,2 0 0,0 6,22H18A2,2 0 0,0 20,20V8L14,2M18,20H6V4H13V9H18V20Z" />
              </svg>
            </div>
            <div>
              <h1 class="header-title">Gradebook</h1>
              <p class="header-subtitle">Review and grade quiz submissions</p>
            </div>
          </div>
        </div>
      </div>

      <!-- Content Area -->

    <!-- Subject Filter Buttons -->
    <div v-if="!selectedSubject && !selectedSection" class="subject-filters">
      <div class="filter-header">
        <h3 class="filter-title">Filter by Subject</h3>
        <span class="filter-subtitle">Choose a subject type to filter courses</span>
      </div>
      <div class="filter-buttons">
        <button 
          @click="selectedSubjectFilter = ''" 
          class="filter-btn modern" 
          :class="{ 'active': selectedSubjectFilter === '' }"
        >
          <div class="filter-icon">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor">
              <path d="M9,5V9H21V5M9,19H21V15H9M9,14H21V10H9M4,9H8L6,7L4,9M4,19H8L6,17L4,19M4,14H8L6,12L4,14Z" />
            </svg>
          </div>
          <span class="filter-text">All Subjects</span>
        </button>
        <button 
          v-for="filterType in availableSubjectTypes" 
          :key="filterType.name"
          @click="selectedSubjectFilter = filterType.name" 
          class="filter-btn modern" 
          :class="{ 'active': selectedSubjectFilter === filterType.name }"
          :style="{ '--filter-color': filterType.color }"
        >
          <div class="filter-icon" v-html="filterType.icon"></div>
          <span class="filter-text">{{ filterType.name }}</span>
        </button>
      </div>
    </div>

    <!-- Breadcrumb Navigation -->
    <div class="breadcrumb-nav" v-if="selectedSubject || selectedSection">
      <button @click="resetToSubjects" class="breadcrumb-btn">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
          <path d="M12,2A3,3 0 0,1 15,5V11A3,3 0 0,1 12,14A3,3 0 0,1 9,11V5A3,3 0 0,1 12,2M19,12V19A3,3 0 0,1 16,22H8A3,3 0 0,1 5,19V12A3,3 0 0,1 8,9H16A3,3 0 0,1 19,12Z" />
        </svg>
        Subjects
      </button>
      <span v-if="selectedSubject" class="breadcrumb-separator">/</span>
      <button v-if="selectedSubject" @click="resetToSections" class="breadcrumb-btn">
        {{ selectedSubject.name }}
      </button>
      <span v-if="selectedSection" class="breadcrumb-separator">/</span>
      <span v-if="selectedSection" class="breadcrumb-current">
        {{ selectedSection.name }}
      </span>
    </div>

    <!-- Loading State -->
    <div v-if="loading" class="loading-container">
      <div class="spinner-large"></div>
      <p>Loading...</p>
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

    <!-- Main Content -->
    <div v-else class="main-content">
      <!-- LEVEL 1: Subject Selection -->
      <div v-if="!selectedSubject" class="content-card modern">
        <div class="card-header enhanced">
          <div class="card-title-section">
            <h3>My Subjects</h3>
            <p class="card-desc">Choose a subject to view sections and manage submissions</p>
          </div>
          <div class="card-stats">
            <div class="stat-item">
              <span class="stat-number">{{ filteredSubjects.length }}</span>
              <span class="stat-label">Subjects</span>
            </div>
          </div>
        </div>
        
        <div class="subjects-grid modern">
          <div 
            v-for="subject in filteredSubjects" 
            :key="subject.id"
            class="subject-card modern"
            @click="selectSubject(subject)"
          >
            <div class="subject-icon modern" :style="{ background: getSubjectIconColor(subject.name) }">
              <div v-html="getSubjectIconSvg(subject.name)"></div>
            </div>
            <div class="subject-info">
              <h4>{{ subject.name }}</h4>
              <p class="subject-grade">Grade {{ subject.grade_level }}</p>
              <div class="subject-stats">
                <span class="stat-item">
                  <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M12,5.5A3.5,3.5 0 0,1 15.5,9A3.5,3.5 0 0,1 12,12.5A3.5,3.5 0 0,1 8.5,9A3.5,3.5 0 0,1 12,5.5M5,8C5.56,8 6.08,8.15 6.53,8.42C6.38,9.85 6.8,11.27 7.66,12.38C7.16,13.34 6.16,14 5,14A3,3 0 0,1 2,11A3,3 0 0,1 5,8M19,8A3,3 0 0,1 22,11A3,3 0 0,1 19,14C17.84,14 16.84,13.34 16.34,12.38C17.2,11.27 17.62,9.85 17.47,8.42C17.92,8.15 18.44,8 19,8M5.5,18.25C5.5,16.18 8.41,14.5 12,14.5C15.59,14.5 18.5,16.18 18.5,18.25V20H5.5V18.25M0,20V18.5C0,17.11 1.89,15.94 4.45,15.6C3.86,16.28 3.5,17.22 3.5,18.25V20H0M24,20H20.5V18.25C20.5,17.22 20.14,16.28 19.55,15.6C22.11,15.94 24,17.11 24,18.5V20Z" />
                  </svg>
                  {{ subject.section_count }} Sections
                </span>
                <span class="stat-item pending" v-if="subject.pending_count > 0">
                  <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2M16.2,16.2L11,13V7H12.5V12.2L17,14.9L16.2,16.2Z" />
                  </svg>
                  {{ subject.pending_count }} Pending
                </span>
              </div>
            </div>
            <div class="card-arrow modern">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                <path d="M8.59,16.58L13.17,12L8.59,7.41L10,6L16,12L10,18L8.59,16.58Z" />
              </svg>
            </div>
          </div>

          <div v-if="filteredSubjects.length === 0" class="empty-state modern">
            <div class="empty-icon">
              <svg width="48" height="48" viewBox="0 0 24 24" fill="currentColor">
                <path d="M19 3H5C3.9 3 3 3.9 3 5V19C3.9 19 5 18.1 5 17V9H19C20.1 9 21 8.1 21 7V5C21 3.9 20.1 3 19 3Z" />
              </svg>
            </div>
            <h3>No subjects found</h3>
            <p>You don't have any subjects assigned yet.</p>
          </div>
        </div>
      </div>

      <!-- LEVEL 2: Section Selection -->
      <div v-else-if="selectedSubject && !selectedSection" class="content-card modern">
        <div class="card-header enhanced">
          <div class="card-title-section">
            <h3>📝 {{ selectedSubject.name }} Sections</h3>
            <p class="card-desc">Choose a section to view quiz submissions and manage grades</p>
          </div>
          <div class="card-stats">
            <div class="stat-item">
              <span class="stat-number">{{ filteredSections.length }}</span>
              <span class="stat-label">Sections</span>
            </div>
            <div class="stat-item">
              <span class="stat-number">{{ filteredSections.reduce((sum, s) => sum + (s.quiz_count || 0), 0) }}</span>
              <span class="stat-label">Quizzes</span>
            </div>
          </div>
        </div>
        
        <div class="sections-grid enhanced">
          <div 
            v-for="section in filteredSections" 
            :key="section.id"
            class="section-card modern"
            @click="selectSection(section)"
          >
            <div class="section-icon modern">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                <path d="M12,5.5A3.5,3.5 0 0,1 15.5,9A3.5,3.5 0 0,1 12,12.5A3.5,3.5 0 0,1 8.5,9A3.5,3.5 0 0,1 12,5.5M5,8C5.56,8 6.08,8.15 6.53,8.42C6.38,9.85 6.8,11.27 7.66,12.38C7.16,13.34 6.16,14 5,14A3,3 0 0,1 2,11A3,3 0 0,1 5,8M19,8A3,3 0 0,1 22,11A3,3 0 0,1 19,14C17.84,14 16.84,13.34 16.34,12.38C17.2,11.27 17.62,9.85 17.47,8.42C17.92,8.15 18.44,8 19,8M5.5,18.25C5.5,16.18 8.41,14.5 12,14.5C15.59,14.5 18.5,16.18 18.5,18.25V20H5.5V18.25M0,20V18.5C0,17.11 1.89,15.94 4.45,15.6C3.86,16.28 3.5,17.22 3.5,18.25V20H0M24,20H20.5V18.25C20.5,17.22 20.14,16.28 19.55,15.6C22.11,15.94 24,17.11 24,18.5V20Z" />
              </svg>
            </div>
            <div class="section-info enhanced">
              <h4>{{ section.name }}</h4>
              <p class="section-code">{{ section.section_code }}</p>
              <div class="section-stats enhanced">
                <span class="stat-item modern">
                  <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M14,2H6A2,2 0 0,0 4,4V20A2,2 0 0,0 6,22H18A2,2 0 0,0 20,20V8L14,2M18,20H6V4H13V9H18V20Z" />
                  </svg>
                  {{ section.quiz_count }} Quizzes
                </span>
                <span class="stat-item modern pending" v-if="section.pending_count > 0">
                  <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2M16.2,16.2L11,13V7H12.5V12.2L17,14.9L16.2,16.2Z" />
                  </svg>
                  {{ section.pending_count }} Pending
                </span>
              </div>
            </div>
            <div class="card-arrow modern">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                <path d="M8.59,16.58L13.17,12L8.59,7.41L10,6L16,12L10,18L8.59,16.58Z" />
              </svg>
            </div>
          </div>

          <div v-if="filteredSections.length === 0" class="empty-state modern">
            <div class="empty-icon">
              <svg width="48" height="48" viewBox="0 0 24 24" fill="currentColor">
                <path d="M12,5.5A3.5,3.5 0 0,1 15.5,9A3.5,3.5 0 0,1 12,12.5A3.5,3.5 0 0,1 8.5,9A3.5,3.5 0 0,1 12,5.5M5,8C5.56,8 6.08,8.15 6.53,8.42C6.38,9.85 6.8,11.27 7.66,12.38C7.16,13.34 6.16,14 5,14A3,3 0 0,1 2,11A3,3 0 0,1 5,8M19,8A3,3 0 0,1 22,11A3,3 0 0,1 19,14C17.84,14 16.84,13.34 16.34,12.38C17.2,11.27 17.62,9.85 17.47,8.42C17.92,8.15 18.44,8 19,8M5.5,18.25C5.5,16.18 8.41,14.5 12,14.5C15.59,14.5 18.5,16.18 18.5,18.25V20H5.5V18.25M0,20V18.5C0,17.11 1.89,15.94 4.45,15.6C3.86,16.28 3.5,17.22 3.5,18.25V20H0M24,20H20.5V18.25C20.5,17.22 20.14,16.28 19.55,15.6C22.11,15.94 24,17.11 24,18.5V20Z" />
              </svg>
            </div>
            <div class="empty-content">
              <h3>No sections found</h3>
              <p>No sections available for this subject.</p>
            </div>
          </div>
        </div>
      </div>

      <!-- LEVEL 3: Submissions Table -->
      <div v-else-if="selectedSection" class="submissions-view">
        <!-- Stats Cards -->
        <div class="stats-grid">
          <div class="stat-card">
            <div class="stat-icon pending">
              <i class="fas fa-clock"></i>
            </div>
            <div class="stat-info">
              <h3>{{ sectionStats.pendingReview }}</h3>
              <p>Pending Review</p>
            </div>
          </div>
          <div class="stat-card">
            <div class="stat-icon graded">
              <i class="fas fa-check-circle"></i>
            </div>
            <div class="stat-info">
              <h3>{{ sectionStats.graded }}</h3>
              <p>Graded</p>
            </div>
          </div>
          <div class="stat-card">
            <div class="stat-icon total">
              <i class="fas fa-clipboard-list"></i>
            </div>
            <div class="stat-info">
              <h3>{{ sectionStats.total }}</h3>
              <p>Total Submissions</p>
            </div>
          </div>
          <div class="stat-card">
            <div class="stat-icon average">
              <i class="fas fa-chart-line"></i>
            </div>
            <div class="stat-info">
              <h3>{{ sectionStats.averageScore }}%</h3>
              <p>Average Score</p>
            </div>
          </div>
        </div>

        <!-- Filters -->
        <div class="submissions-filters">
          <select v-model="selectedStatus" class="filter-select">
            <option value="">All Status</option>
            <option value="submitted">Pending Review</option>
            <option value="graded">Graded</option>
          </select>
        </div>

        <!-- Submissions Table -->
        <div class="submissions-section">
          <div v-if="filteredSubmissions.length === 0" class="empty-state">
            <i class="fas fa-clipboard-list"></i>
            <h3>No submissions found</h3>
            <p>There are no quiz submissions for this section yet.</p>
          </div>

          <div v-else class="submissions-table-container">
            <table class="submissions-table">
              <thead>
                <tr>
                  <th @click="sortBy('student_name')" class="sortable">
                    Student Name
                    <i class="fas fa-sort" :class="getSortIcon('student_name')"></i>
                  </th>
                  <th @click="sortBy('quiz_title')" class="sortable">
                    Quiz
                    <i class="fas fa-sort" :class="getSortIcon('quiz_title')"></i>
                  </th>
                  <th @click="sortBy('submitted_at')" class="sortable">
                    Submitted
                    <i class="fas fa-sort" :class="getSortIcon('submitted_at')"></i>
                  </th>
                  <th @click="sortBy('percentage')" class="sortable">
                    Score
                    <i class="fas fa-sort" :class="getSortIcon('percentage')"></i>
                  </th>
                  <th>Status</th>
                  <th>Actions</th>
                </tr>
              </thead>
              <tbody>
                <tr 
                  v-for="submission in paginatedSubmissions" 
                  :key="submission.id"
                >
                  <td>
                    <div class="student-info">
                      <div class="student-avatar">
                        {{ getInitials(submission.student_name) }}
                      </div>
                      <div>
                        <div class="student-name">{{ submission.student_name }}</div>
                        <div class="student-email">{{ submission.student_email }}</div>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="quiz-info">
                      <div class="quiz-title">{{ submission.quiz_title }}</div>
                      <div class="quiz-code">{{ submission.quiz_code }}</div>
                    </div>
                  </td>
                  <td>
                    <div class="date-info">
                      <div class="date">{{ formatDate(submission.submitted_at) }}</div>
                      <div class="time">{{ formatTime(submission.submitted_at) }}</div>
                    </div>
                  </td>
                  <td>
                    <div class="score-display">
                      <div class="score-percentage" :class="getScoreClass(submission.percentage)">
                        {{ submission.percentage }}%
                      </div>
                      <div class="score-fraction">
                        {{ submission.total_score }}/{{ submission.max_score }}
                      </div>
                    </div>
                  </td>
                  <td>
                    <span class="status-badge" :class="submission.status">
                      {{ getStatusText(submission.status) }}
                    </span>
                  </td>
                  <td>
                    <div class="action-buttons">
                      <button 
                        @click="reviewSubmission(submission)" 
                        class="btn-action review"
                        title="Review & Grade"
                      >
                        <i class="fas fa-edit"></i>
                      </button>
                      <button 
                        @click="viewSubmission(submission)" 
                        class="btn-action view"
                        title="View Details"
                      >
                        <i class="fas fa-eye"></i>
                      </button>
                    </div>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>

          <!-- Pagination -->
          <div v-if="totalPages > 1" class="pagination">
            <button 
              @click="currentPage--" 
              :disabled="currentPage === 1"
              class="pagination-btn"
            >
              <i class="fas fa-chevron-left"></i>
            </button>
            <span class="pagination-info">
              Page {{ currentPage }} of {{ totalPages }}
            </span>
            <button 
              @click="currentPage++" 
              :disabled="currentPage === totalPages"
              class="pagination-btn"
            >
              <i class="fas fa-chevron-right"></i>
            </button>
          </div>
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
                      <div class="option-letter">{{ String.fromCharCode(65 + option.option_number - 1) }}</div>
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
  </div>
</template>

<script setup>
import { ref, computed, watch, onMounted } from 'vue'
import { supabase } from '@/supabase.js'
import { useDarkMode } from '@/composables/useDarkMode.js'

const { isDarkMode } = useDarkMode()

const loading = ref(true)
const loadingQuestions = ref(false)
const savingGrade = ref(false)
const error = ref(null)
const searchQuery = ref('')
const teacherId = ref(null)

const subjects = ref([])
const selectedSubject = ref(null)
const sections = ref([])
const selectedSection = ref(null)
const submissions = ref([])

const selectedStatus = ref('')
const currentPage = ref(1)
const itemsPerPage = ref(10)
const sortField = ref('submitted_at')
const sortDirection = ref('desc')

const showReviewModal = ref(false)
const selectedSubmission = ref(null)
const reviewQuestions = ref([])
const reviewFeedback = ref('')
const modalMode = ref('view')

const selectedSubjectFilter = ref('')

const sectionStats = computed(() => {
  const pending = submissions.value.filter(s => s.status === 'submitted').length
  const graded = submissions.value.filter(s => s.status === 'graded').length
  const total = submissions.value.length
  const averageScore = total > 0 
    ? Math.round(submissions.value.reduce((sum, s) => sum + (s.percentage || 0), 0) / total)
    : 0
  return { pendingReview: pending, graded, total, averageScore }
})

const correctAnswerCount = computed(() => {
  return reviewQuestions.value.filter(q => q.is_correct).length
})

const maxReviewScore = computed(() => {
  return reviewQuestions.value.reduce((sum, q) => sum + (q.points || 1), 0)
})

const availableSubjectTypes = computed(() => {
  const types = new Set()
  subjects.value.forEach(subject => {
    types.add(subject.name)
  })
  
  return Array.from(types).map(type => ({
    name: type,
    color: getSubjectIconColor(type),
    icon: getSubjectIconSvg(type)
  }))
})

const filteredSubjects = computed(() => {
  let filtered = subjects.value
  
  if (selectedSubjectFilter.value) {
    filtered = filtered.filter(subject => subject.name === selectedSubjectFilter.value)
  }
  
  if (searchQuery.value) {
    const query = searchQuery.value.toLowerCase()
    filtered = filtered.filter(s => 
      s.name.toLowerCase().includes(query) || 
      s.grade_level.toString().includes(query)
    )
  }
  
  return filtered
})

const filteredSections = computed(() => {
  if (!searchQuery.value) return sections.value
  const query = searchQuery.value.toLowerCase()
  return sections.value.filter(s => 
    s.name.toLowerCase().includes(query) || 
    s.section_code.toLowerCase().includes(query)
  )
})

const filteredSubmissions = computed(() => {
  let filtered = submissions.value

  if (searchQuery.value) {
    const query = searchQuery.value.toLowerCase()
    filtered = filtered.filter(submission => 
      submission.student_name.toLowerCase().includes(query) ||
      submission.quiz_title.toLowerCase().includes(query) ||
      submission.student_email.toLowerCase().includes(query)
    )
  }

  if (selectedStatus.value) {
    filtered = filtered.filter(submission => 
      submission.status === selectedStatus.value
    )
  }

  filtered.sort((a, b) => {
    let aValue = a[sortField.value]
    let bValue = b[sortField.value]

    if (sortField.value === 'submitted_at') {
      aValue = new Date(aValue)
      bValue = new Date(bValue)
    }

    if (aValue < bValue) {
      return sortDirection.value === 'asc' ? -1 : 1
    }
    if (aValue > bValue) {
      return sortDirection.value === 'asc' ? 1 : -1
    }
    return 0
  })

  return filtered
})

const paginatedSubmissions = computed(() => {
  const start = (currentPage.value - 1) * itemsPerPage.value
  const end = start + itemsPerPage.value
  return filteredSubmissions.value.slice(start, end)
})

const totalPages = computed(() => {
  return Math.ceil(filteredSubmissions.value.length / itemsPerPage.value)
})

const getTeacherInfo = async () => {
  try {
    const { data: { session }, error: sessionError } = await supabase.auth.getSession()
    if (sessionError || !session) {
      error.value = 'Authentication error'
      return false
    }

    const { data: profile, error: profileError } = await supabase
      .from('profiles')
      .select('id, role')
      .eq('auth_user_id', session.user.id)
      .single()

    if (profileError || !profile || profile.role !== 'teacher') {
      error.value = 'Access denied - Teacher role required'
      return false
    }

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

const fetchSubjects = async () => {
  try {
    loading.value = true
    error.value = null

    const { data: subjectsData, error: subjectsError } = await supabase
      .from('subjects')
      .select('id, name, grade_level, description')
      .eq('teacher_id', teacherId.value)
      .eq('is_active', true)

    if (subjectsError) throw subjectsError

    const subjectsWithStats = await Promise.all(
      (subjectsData || []).map(async (subject) => {
        const { count: sectionCount } = await supabase
          .from('sections')
          .select('id', { count: 'exact', head: true })
          .eq('subject_id', subject.id)
          .eq('is_active', true)

        const { data: quizzes } = await supabase
          .from('quizzes')
          .select('id')
          .eq('subject_id', subject.id)

        const quizIds = quizzes?.map(q => q.id) || []
        
        let pendingCount = 0
        if (quizIds.length > 0) {
          const { count } = await supabase
            .from('quiz_attempts')
            .select('id', { count: 'exact', head: true })
            .in('quiz_id', quizIds)
            .eq('status', 'submitted')
            .not('submitted_at', 'is', null)

          pendingCount = count || 0
        }

        return {
          id: subject.id,
          name: subject.name,
          grade_level: subject.grade_level,
          description: subject.description || '',
          section_count: sectionCount || 0,
          pending_count: pendingCount
        }
      })
    )

    subjects.value = subjectsWithStats
  } catch (err) {
    console.error('Error fetching subjects:', err)
    error.value = `Failed to load subjects: ${err.message}`
  } finally {
    loading.value = false
  }
}

const selectSubject = async (subject) => {
  selectedSubject.value = subject
  await fetchSections(subject.id)
}

const fetchSections = async (subjectId) => {
  try {
    loading.value = true
    error.value = null

    const { data: sectionsData, error: sectionsError } = await supabase
      .from('sections')
      .select('id, name, section_code, max_students')
      .eq('subject_id', subjectId)
      .eq('is_active', true)

    if (sectionsError) throw sectionsError

    const sectionsWithStats = await Promise.all(
      (sectionsData || []).map(async (section) => {
        const { data: quizzes } = await supabase
          .from('quizzes')
          .select('id')
          .eq('section_id', section.id)

        const quizCount = quizzes?.length || 0
        const quizIds = quizzes?.map(q => q.id) || []
        
        let pendingCount = 0
        if (quizIds.length > 0) {
          const { count } = await supabase
            .from('quiz_attempts')
            .select('id', { count: 'exact', head: true })
            .in('quiz_id', quizIds)
            .eq('status', 'submitted')
            .not('submitted_at', 'is', null)

          pendingCount = count || 0
        }

        return {
          id: section.id,
          name: section.name,
          section_code: section.section_code,
          max_students: section.max_students,
          quiz_count: quizCount,
          pending_count: pendingCount
        }
      })
    )

    sections.value = sectionsWithStats
  } catch (err) {
    console.error('Error fetching sections:', err)
    error.value = `Failed to load sections: ${err.message}`
  } finally {
    loading.value = false
  }
}

const selectSection = async (section) => {
  selectedSection.value = section
  await fetchSubmissions(section.id)
}

const fetchSubmissions = async (sectionId) => {
  try {
    loading.value = true
    error.value = null

    const { data: quizzes, error: quizzesError } = await supabase
      .from('quizzes')
      .select('id, title, quiz_code')
      .eq('section_id', sectionId)

    if (quizzesError) throw quizzesError

    if (!quizzes || quizzes.length === 0) {
      submissions.value = []
      loading.value = false
      return
    }

    const quizIds = quizzes.map(q => q.id)

    const { data: attempts, error: attemptsError } = await supabase
      .from('quiz_attempts')
      .select('*')
      .in('quiz_id', quizIds)
      .order('submitted_at', { ascending: false })

    if (attemptsError) throw attemptsError

    const studentIds = [...new Set(attempts?.map(a => a.student_id) || [])]
    
    let studentsMap = {}
    if (studentIds.length > 0) {
      const { data: students } = await supabase
        .from('students')
        .select('id, full_name, email')
        .in('id', studentIds)

      students?.forEach(s => {
        studentsMap[s.id] = s
      })
    }

    const quizMap = {}
    quizzes.forEach(q => { quizMap[q.id] = q })

    submissions.value = (attempts || []).map(attempt => ({
      id: attempt.id,
      quiz_id: attempt.quiz_id,
      student_id: attempt.student_id,
      attempt_number: attempt.attempt_number,
      student_name: studentsMap[attempt.student_id]?.full_name || 'Unknown Student',
      student_email: studentsMap[attempt.student_id]?.email || '',
      quiz_title: quizMap[attempt.quiz_id]?.title || 'Unknown Quiz',
      quiz_code: quizMap[attempt.quiz_id]?.quiz_code || '',
      total_score: attempt.total_score || 0,
      max_score: attempt.max_score || 0,
      percentage: Math.round(attempt.percentage || 0),
      status: attempt.status || 'submitted',
      submitted_at: attempt.submitted_at,
      time_taken_minutes: attempt.time_taken_minutes,
      teacher_feedback: attempt.teacher_feedback
    }))

    console.log('Submissions loaded:', submissions.value.length)
  } catch (err) {
    console.error('Error fetching submissions:', err)
    error.value = `Failed to load submissions: ${err.message}`
  } finally {
    loading.value = false
  }
}

const resetToSubjects = () => {
  selectedSubject.value = null
  selectedSection.value = null
  sections.value = []
  submissions.value = []
  searchQuery.value = ''
}

const resetToSections = () => {
  selectedSection.value = null
  submissions.value = []
  searchQuery.value = ''
}

const refreshData = async () => {
  if (!selectedSubject.value && !selectedSection.value) {
    await fetchSubjects()
  } else if (selectedSubject.value && !selectedSection.value) {
    await fetchSections(selectedSubject.value.id)
  } else if (selectedSection.value) {
    await fetchSubmissions(selectedSection.value.id)
  }
}

const loadQuestionsAndAnswers = async (submission) => {
  try {
    loadingQuestions.value = true

    const { data: questions, error: questionsError } = await supabase
      .from('quiz_questions')
      .select('id, question_number, question_type, question_text, points')
      .eq('quiz_id', submission.quiz_id)
      .order('question_number')

    if (questionsError) throw questionsError

    if (!questions || questions.length === 0) {
      reviewQuestions.value = []
      return
    }

    const questionIds = questions.map(q => q.id)

    const { data: options } = await supabase
      .from('question_options')
      .select('*')
      .in('question_id', questionIds)
      .order('option_number')

    const { data: answers } = await supabase
      .from('question_answers')
      .select('*')
      .in('question_id', questionIds)

    const { data: studentAnswers } = await supabase
      .from('student_answers')
      .select('*')
      .eq('attempt_id', submission.id)

    const optionsMap = {}
    options?.forEach(opt => {
      if (!optionsMap[opt.question_id]) {
        optionsMap[opt.question_id] = []
      }
      optionsMap[opt.question_id].push(opt)
    })

    const answersMap = {}
    answers?.forEach(ans => {
      answersMap[ans.question_id] = ans
    })

    const studentAnswersMap = {}
    studentAnswers?.forEach(sa => {
      studentAnswersMap[sa.question_id] = sa
    })

    reviewQuestions.value = questions.map(q => {
      const studentAnswer = studentAnswersMap[q.id]
      const correctAnswer = answersMap[q.id]

      return {
        id: q.id,
        question_number: q.question_number,
        question_type: q.question_type,
        question_text: q.question_text,
        points: q.points || 1,
        options: optionsMap[q.id] || [],
        correct_answer: correctAnswer?.correct_answer || null,
        selected_option_id: studentAnswer?.selected_option_id || null,
        answer_text: studentAnswer?.answer_text || null,
        is_correct: studentAnswer?.is_correct || false,
        points_earned: studentAnswer?.points_earned || 0,
        teacher_comment: studentAnswer?.teacher_comment || '',
        manualPoints: studentAnswer?.points_earned || 0,
        teacherComment: studentAnswer?.teacher_comment || '',
        student_answer_id: studentAnswer?.id || null
      }
    })
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
  return get
SubjectIconSvg(type)
}

watch([searchQuery, selectedStatus], () => {
  currentPage.value = 1
})

onMounted(async () => {
  const success = await getTeacherInfo()
  if (success) {
    await fetchSubjects()
  } else {
    loading.value = false
  }
})
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

/* Reset and Hide Parent Layouts */
body, html {
  overflow-x: hidden !important;
}

/* Force hide any sidebar or layout from parent components */
.sidebar,
.dashboard-sidebar,
.navigation-sidebar,
.teacher-layout,
.dashboard-layout {
  display: none !important;
}

/* Ensure our container is on top */
.analytics-container {
  position: fixed !important;
  top: 0 !important;
  left: 0 !important;
  width: 100vw !important;
  height: 100vh !important;
  z-index: 999999 !important;
  background: #f8fafc !important;
  overflow-y: auto !important;
}

/* Top Navigation Bar (Same as Dashboard) */
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

.nav-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.25rem;
  padding: 0.75rem 1.5rem;
  border-radius: 12px;
  text-decoration: none;
  color: rgba(255, 255, 255, 0.8);
  transition: all 0.2s ease;
  position: relative;
  font-size: 0.75rem;
  font-weight: 500;
}

.nav-item:hover {
  background: rgba(255, 255, 255, 0.1);
  color: white;
}

.nav-item.active {
  color: white;
  background: rgba(255, 255, 255, 0.15);
}

.nav-item.active::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 60%;
  height: 3px;
  background: white;
  border-radius: 2px 2px 0 0;
}

.navbar-right {
  display: flex;
  align-items: center;
  gap: 1rem;
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

/* Main Content */
.main-content {
  margin-top: 64px;
  padding: 1.5rem;
  width: 100%;
  min-height: calc(100vh - 64px);
  position: relative;
  background: #f8fafc;
  padding-bottom: 2rem;
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

/* Enhanced Subject Filter Buttons */
.subject-filters {
  margin-bottom: 2rem;
  background: white;
  border-radius: 16px;
  padding: 1.5rem;
  border: 1px solid rgba(61, 141, 122, 0.1);
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
}
.dark .subject-filters {
  background: #23272b;
  border-color: #3D8D7A;
}

.filter-header {
  margin-bottom: 1.25rem;
  border-bottom: 1px solid rgba(61, 141, 122, 0.1);
  padding-bottom: 1rem;
}
.dark .filter-header {
  border-bottom-color: #3D8D7A;
}

.filter-title {
  font-size: 1.125rem;
  font-weight: 700;
  color: #1f2937;
  margin: 0 0 0.25rem 0;
}
.dark .filter-title {
  color: #A3D1C6;
}

.filter-subtitle {
  font-size: 0.875rem;
  color: #6b7280;
  margin: 0;
}
.dark .filter-subtitle {
  color: #9ca3af;
}

.filter-buttons {
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem;
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
  padding: 0.75rem 0;
  margin-bottom: 1rem;
}

.breadcrumb-btn {
  background: none;
  border: none;
  color: #3D8D7A;
  cursor: pointer;
  padding: 0.5rem 0.75rem;
  border-radius: 6px;
  font-size: 0.875rem;
  font-weight: 500;
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
  font-size: 0.875rem;
  padding: 0.5rem 0.75rem;
}
.dark .breadcrumb-current {
  color: #A3D1C6;
}

.breadcrumb-separator {
  color: #6b7280;
  font-size: 0.875rem;
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
  color: #fca5a5;
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
.main-content {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.content-card.modern {
  background: white;
  border-radius: 16px;
  padding: 0;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.06);
  border: 1px solid rgba(61, 141, 122, 0.08);
  overflow: hidden;
}
.dark .content-card.modern {
  background: #23272b;
  border: 1px solid rgba(163, 209, 198, 0.2);
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
}

.card-header.enhanced {
  padding: 2rem 2rem 1.5rem 2rem;
  background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
  border-bottom: 1px solid rgba(61, 141, 122, 0.1);
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
}
.dark .card-header.enhanced {
  background: linear-gradient(135deg, #374151 0%, #4b5563 100%);
  border-bottom-color: rgba(163, 209, 198, 0.2);
}

.card-title-section h3 {
  font-size: 1.5rem;
  font-weight: 700;
  color: #1f2937;
  margin: 0 0 0.5rem 0;
  background: linear-gradient(135deg, #3D8D7A, #059669);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}
.dark .card-title-section h3 {
  background: linear-gradient(135deg, #A3D1C6, #34d399);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.card-title-section .card-desc {
  font-size: 0.875rem;
  color: #6b7280;
  margin: 0;
}
.dark .card-title-section .card-desc {
  color: #9ca3af;
}

.card-stats {
  display: flex;
  gap: 1.5rem;
  align-items: center;
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

/* Stats Grid */
.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1rem;
  margin-bottom: 1.5rem;
}

.stat-card {
  background: white;
  border-radius: 12px;
  padding: 1.25rem;
  display: flex;
  align-items: center;
  gap: 1rem;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
  border: 1px solid rgba(61, 141, 122, 0.1);
}
.dark .stat-card {
  background: #23272b;
  border: 1px solid #3D8D7A;
  box-shadow: 0 2px 8px rgba(0,0,0,0.25);
}

.stat-icon {
  width: 48px;
  height: 48px;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  flex-shrink: 0;
}

.stat-icon.pending { background: #A3D1C6; }
.stat-icon.graded { background: #B3D8A8; }
.stat-icon.total { background: #3D8D7A; }
.stat-icon.average { background: linear-gradient(135deg, #3D8D7A, #A3D1C6); }

.stat-number {
  font-size: 1.75rem;
  font-weight: 700;
  color: #1f2937;
  line-height: 1;
}
.dark .stat-number {
  color: #A3D1C6;
}

.stat-label {
  font-size: 0.875rem;
  color: #6b7280;
  margin-top: 0.25rem;
  font-weight: 500;
}
.dark .stat-label {
  color: #A3D1C6;
}

/* Enhanced Subject and Section Cards */
.subjects-grid.modern {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(340px, 1fr));
  gap: 1.5rem;
  padding: 2rem;
}

.subjects-grid, .sections-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 1rem;
}

.subject-card.modern {
  background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
  border: 1.5px solid transparent;
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
}
.dark .subject-card.modern {
  background: linear-gradient(135deg, #1f2937 0%, #374151 100%);
  border-color: rgba(163, 209, 198, 0.2);
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
}
.dark .subject-icon.modern {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
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
  padding: 1rem;
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
  font-size: 0.875rem;
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
  gap: 0.75rem;
}

.student-avatar {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  background: #3D8D7A;
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 600;
  font-size: 0.75rem;
}

.student-name {
  font-weight: 500;
  color: #1f2937;
  font-size: 0.875rem;
}
.dark .student-name {
  color: #A3D1C6;
}

.student-email {
  font-size: 0.75rem;
  color: #6b7280;
}
.dark .student-email {
  color: #9ca3af;
}

.quiz-info {
  max-width: 180px;
}

.quiz-title {
  font-weight: 500;
  color: #1f2937;
  margin-bottom: 0.25rem;
  font-size: 0.875rem;
}
.dark .quiz-title {
  color: #A3D1C6;
}

.quiz-code {
  font-size: 0.7rem;
  color: #6b7280;
  font-family: 'Courier New', monospace;
  background: #B3D8A8;
  padding: 0.125rem 0.375rem;
  border-radius: 4px;
  display: inline-block;
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
}

.btn-action {
  width: 32px;
  height: 32px;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.2s;
}

.btn-action.review {
  background: #B3D8A8;
  color: #1f2937;
}

.btn-action.review:hover {
  background: #3D8D7A;
  color: white;
}

.btn-action.view {
  background: rgba(163, 209, 198, 0.3);
  color: #3D8D7A;
}

.btn-action.view:hover {
  background: #A3D1C6;
  color: #1f2937;
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
  grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
  gap: 1rem;
  padding: 1.25rem;
  background: #FBFFE4;
  border-radius: 8px;
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
  .sections-grid {
    grid-template-columns: 1fr;
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
  
  .search-box {
    min-width: 200px;
  }
}

/* Enhanced Sections */
.sections-grid.enhanced {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(340px, 1fr));
  gap: 1.5rem;
  padding: 2rem;
}

.section-card.modern {
  background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
  border: 1.5px solid transparent;
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
  background: linear-gradient(135deg, #6366f1, #8b5cf6);
  border-radius: 14px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  flex-shrink: 0;
  box-shadow: 0 4px 12px rgba(99, 102, 241, 0.3);
}
.dark .section-icon.modern {
  box-shadow: 0 4px 12px rgba(139, 92, 246, 0.3);
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
  padding: 3rem 2rem;
  text-align: center;
  background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
  border: 2px dashed rgba(107, 114, 128, 0.2);
  border-radius: 16px;
  grid-column: 1 / -1;
}
.dark .empty-state.modern {
  background: linear-gradient(135deg, #374151 0%, #4b5563 100%);
  border-color: rgba(163, 209, 198, 0.2);
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
</style>