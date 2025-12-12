<template>
  <div class="grade-management-page">
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
        
        <!-- Center: Breadcrumb Navigation -->
        <div class="navbar-center">
          <div class="page-breadcrumb">
            <button @click="goBack" class="breadcrumb-back">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                <path d="M20,11V13H8L13.5,18.5L12.08,19.92L4.16,12L12.08,4.08L13.5,5.5L8,11H20Z"/>
              </svg>
            </button>
            <span class="breadcrumb-item">Subjects</span>
            <span class="breadcrumb-separator">></span>
            <span class="breadcrumb-item">{{ subject?.name || 'Subject' }}</span>
            <span class="breadcrumb-separator">></span>
            <span class="breadcrumb-current">Grade Management</span>
          </div>
        </div>
        
        <!-- Right: Actions and User Profile -->
        <div class="navbar-right">
          <button @click="showGradeSettings = true" class="action-btn secondary">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
              <path d="M12,15.5A3.5,3.5 0 0,1 8.5,12A3.5,3.5 0 0,1 12,8.5A3.5,3.5 0 0,1 15.5,12A3.5,3.5 0 0,1 12,15.5M19.43,12.97C19.47,12.65 19.5,12.33 19.5,12C19.5,11.67 19.47,11.34 19.43,11L21.54,9.37C21.73,9.22 21.78,8.95 21.66,8.73L19.66,5.27C19.54,5.05 19.27,4.96 19.05,5.05L16.56,6.05C16.04,5.66 15.5,5.32 14.87,5.07L14.5,2.42C14.46,2.18 14.25,2 14,2H10C9.75,2 9.54,2.18 9.5,2.42L9.13,5.07C8.5,5.32 7.96,5.66 7.44,6.05L4.95,5.05C4.73,4.96 4.46,5.05 4.34,5.27L2.34,8.73C2.22,8.95 2.27,9.22 2.46,9.37L4.57,11C4.53,11.34 4.5,11.67 4.5,12C4.5,12.33 4.53,12.65 4.57,12.97L2.46,14.63C2.27,14.78 2.22,15.05 2.34,15.27L4.34,18.73C4.46,18.95 4.73,19.03 4.95,18.95L7.44,17.94C7.96,18.34 8.5,18.68 9.13,18.93L9.5,21.58C9.54,21.82 9.75,22 10,22H14C14.25,22 14.46,21.82 14.5,21.58L14.87,18.93C15.5,18.68 16.04,18.34 16.56,17.94L19.05,18.95C19.27,19.03 19.54,18.95 19.66,18.73L21.66,15.27C21.78,15.05 21.73,14.78 21.54,14.63L19.43,12.97Z"/>
            </svg>
            Grade Settings
          </button>

          <button 
            @click="exportGrades" 
            :disabled="students.length === 0"
            class="export-btn"
          >
            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
              <path d="M14,2H6A2,2 0 0,0 4,4V20A2,2 0 0,0 6,22H18A2,2 0 0,0 20,20V8L14,2M18,20H6V4H13V9H18V20Z" />
            </svg>
            Export Grades
          </button>
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



    <!-- Main Content Area -->
    <main class="main-content">
      <!-- Scroll to Top Button -->
      <button v-if="showScrollTop" @click="scrollToTop" class="scroll-to-top">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
          <path d="M7 14l5-5 5 5z"/>
        </svg>
      </button>
      
      <!-- Main Content Container -->
      <div class="main-container">
        <!-- Grade Management Header -->
        <div class="section-header">
          <div class="header-content">
            <div class="header-left">
              <div class="header-icon">
                <svg width="32" height="32" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M14,2H6A2,2 0 0,0 4,4V20A2,2 0 0,0 6,22H18A2,2 0 0,0 20,20V8L14,2M18,20H6V4H13V9H18V20Z" />
                </svg>
              </div>
              <div class="header-info">
                <h1 class="section-title">Grade Management</h1>
                <p class="section-subtitle">{{ subject?.name }}<span v-if="section?.name"> - {{ section?.name }}</span></p>
              </div>
            </div>
            
            <div class="header-actions">
              <button @click="exportGrades" class="action-btn secondary" :disabled="students.length === 0">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M14,2H6A2,2 0 0,0 4,4V20A2,2 0 0,0 6,22H18A2,2 0 0,0 20,20V8L14,2M18,20H6V4H13V9H18V20Z" />
                </svg>
                Export Grades
              </button>
              <button @click="goBack" class="action-btn primary">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M20,11V13H8L13.5,18.5L12.08,19.92L4.16,12L12.08,4.08L13.5,5.5L8,11H20Z" />
                </svg>
                Back to Section
              </button>
            </div>
          </div>
        </div>
      </div>
      <!-- Controls -->
      <div class="controls-card">
      <div class="controls-header">
        <h2 class="controls-title">Grade Controls</h2>
      </div>
      <div class="controls-content">
        <div class="filters">
          <select v-model="selectedAssessmentType" @change="filterByAssessmentType" class="filter-select">
            <option value="all">All Assessments ({{ assessments.length }})</option>
            <option value="quiz">Quizzes Only ({{ quizzes.length }})</option>
            <option value="assignment">Assignments Only ({{ assignments.length }})</option>
          </select>
          <select v-model="selectedAssessment" @change="filterByAssessment" class="filter-select">
            <option value="">All {{ selectedAssessmentType === 'all' ? 'Assessments' : selectedAssessmentType === 'quiz' ? 'Quizzes' : 'Assignments' }}</option>
            <option v-for="assessment in displayedAssessments" :key="assessment.id" :value="assessment.id">
              {{ assessment.title }} ({{ assessment.type === 'quiz' ? 'Quiz' : 'Assignment' }})
            </option>
          </select>
          <select v-model="viewMode" @change="changeViewMode" class="filter-select">
            <option value="edit">Edit Mode</option>
            <option value="view">View Only</option>
          </select>
        </div>
        <button @click="exportGrades" class="secondary-btn" :disabled="students.length === 0">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
            <path d="M14,2H6A2,2 0 0,0 4,4V20A2,2 0 0,0 6,22H18A2,2 0 0,0 20,20V8L14,2M18,20H6V4H13V9H18V20Z" />
          </svg>
          Export Grades
        </button>
        <button @click="showGradeSettings = true" class="primary-btn">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
            <path d="M12,15.5A3.5,3.5 0 0,1 8.5,12A3.5,3.5 0 0,1 12,8.5A3.5,3.5 0 0,1 15.5,12A3.5,3.5 0 0,1 12,15.5M19.43,12.97C19.47,12.65 19.5,12.33 19.5,12C19.5,11.67 19.47,11.34 19.43,11.03L21.54,9.37C21.73,9.22 21.78,8.95 21.66,8.73L19.66,5.27C19.54,5.05 19.27,4.96 19.05,5.05L16.56,6.05C16.04,5.66 15.5,5.32 14.87,5.07L14.5,2.42C14.46,2.18 14.25,2 14,2H10C9.75,2 9.54,2.18 9.5,2.42L9.13,5.07C8.5,5.32 7.96,5.66 7.44,6.05L4.95,5.05C4.73,4.96 4.46,5.05 4.34,5.27L2.34,8.73C2.22,8.95 2.27,9.22 2.46,9.37L4.57,11.03C4.53,11.34 4.5,11.67 4.5,12C4.5,12.33 4.53,12.65 4.57,12.97L2.46,14.63C2.27,14.78 2.22,15.05 2.34,15.27L4.34,18.73C4.46,18.95 4.73,19.03 4.95,18.95L7.44,17.94C7.96,18.34 8.5,18.68 9.13,18.93L9.5,21.58C9.54,21.82 9.75,22 10,22H14C14.25,22 14.46,21.82 14.5,21.58L14.87,18.93C15.5,18.68 16.04,18.34 16.56,17.94L19.05,18.95C19.27,19.03 19.54,18.95 19.66,18.73L21.66,15.27C21.78,15.05 21.73,14.78 21.54,14.63L19.43,12.97Z" />
          </svg>
          Grade Settings
        </button>
      </div>
    </div>

    <!-- Grade Table -->
    <div class="table-container">
      <div class="table-header">
        <h2 class="table-title">
          Student Grades ({{ students.length }} Students)
          <span class="assessment-count">
            - {{ displayedAssessments.length }} {{ selectedAssessmentType === 'all' ? 'Assessments' : selectedAssessmentType === 'quiz' ? 'Quizzes' : 'Assignments' }}
          </span>
        </h2>
      </div>

      <div v-if="filteredStudents.length > 0" class="table-wrapper">
        <!-- Debug info -->
        <div v-if="assessments.length === 0" class="assessment-debug" style="padding: 1rem; background: #fef3c7; margin-bottom: 1rem; border-radius: 8px; color: #92400e;">
          <p><strong>No assessments found for this section.</strong></p>
          <p>Make sure you have published quizzes and assignments for this subject and section.</p>
        </div>
        
        <!-- Scrollable table container -->
        <div class="scrollable-table-container">
          <table class="grade-table">
            <thead>
              <tr>
                <th class="student-column sticky-column">
                  <div class="column-header">
                    <span>Student</span>
                  </div>
                </th>
                <th v-for="assessment in displayedAssessments" :key="assessment.id" class="assessment-column" :class="assessment.type + '-column'">
                  <div class="column-header assessment-header">
                    <div class="assessment-title">{{ assessment.title }}</div>
                    <div class="assessment-meta">
                      <span class="assessment-type" :class="assessment.type">
                        {{ assessment.type === 'quiz' ? 'Quiz' : 'Assignment' }}
                      </span>
                      <span class="assessment-points">({{ assessment.total_points || 100 }} pts)</span>
                    </div>
                    <div v-if="assessment.due_date" class="assessment-due">
                      Due: {{ formatDate(assessment.due_date) }}
                    </div>
                  </div>
                </th>
                <th v-if="assessments.length === 0" class="no-assessments-column">
                  <div class="column-header">
                    <span>No Assessments</span>
                    <small>Publish assessments to see grades</small>
                  </div>
                </th>
                <th class="average-column sticky-column">
                  <div class="column-header">
                    <span>Average</span>
                    <small>Overall Grade</small>
                  </div>
                </th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="student in filteredStudents" :key="student.id" class="student-row">
                <td class="student-column sticky-column">
                  <div class="student-info">
                    <div class="student-avatar">
                      {{ getInitials(student.first_name, student.last_name) }}
                    </div>
                    <div class="student-details">
                      <div class="student-name">{{ student.first_name }} {{ student.last_name }}</div>
                      <div class="student-email">{{ student.email }}</div>
                    </div>
                  </div>
                </td>
                <td v-for="assessment in displayedAssessments" :key="assessment.id" class="assessment-column" :class="assessment.type + '-column'">
                  <div class="grade-cell">
                    <input
                      v-if="viewMode === 'edit'"
                      :value="getGradeValue(student.id, assessment.id)"
                      @input="updateGrade(student.id, assessment.id, $event, assessment.type)"
                      @blur="saveGradeToDatabase(student.id, assessment.id, assessment.type)"
                      type="number"
                      :min="0"
                      :max="assessment.total_points || 100"
                      class="grade-input"
                      :placeholder="`0/${assessment.total_points || 100}`"
                    />
                    <div v-else class="grade-display" :class="getGradeClass(getGradeValue(student.id, assessment.id), assessment.total_points || 100)">
                      <span class="grade-score">{{ getGradeValue(student.id, assessment.id) }}</span>
                      <span class="grade-separator">/</span>
                      <span class="grade-total">{{ assessment.total_points || 100 }}</span>
                      <div class="grade-percentage">
                        {{ formatGrade(getGradeValue(student.id, assessment.id), assessment.total_points || 100) }}
                      </div>
                    </div>
                  </div>
                </td>
                <td v-if="assessments.length === 0" class="no-assessments-column">
                  <div class="no-assessment-message">
                    <span>No assessments</span>
                  </div>
                </td>
                <td class="average-column sticky-column">
                  <div class="average-cell">
                    <div class="average-display" :class="getAverageClass(student.average)">
                      <span class="average-percentage">{{ student.average !== null ? Math.round(student.average) + '%' : 'N/A' }}</span>
                      <small class="average-label" v-if="student.average !== null && student.average > 0">{{ getLetterGrade(student.average) }}</small>
                      <small class="average-label" v-else>No Grades</small>
                    </div>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <div v-else class="empty-state">
        <svg width="64" height="64" viewBox="0 0 24 24" fill="currentColor" style="opacity: 0.3; margin-bottom: 1rem;">
          <path d="M12,3L1,9L12,15L21,10.09V17H23V9M5,13.18V17.18L12,21L19,17.18V13.18L12,17L5,13.18Z" />
        </svg>
        <h3>No Students Found</h3>
        <p>No students are enrolled in this section yet.</p>
      </div>
    </div>

    <!-- Grade Settings Modal -->
    <div v-if="showGradeSettings" class="modal-overlay" @click="showGradeSettings = false">
      <div class="modal-content" @click.stop>
        <div class="modal-header">
          <h2>Grade Settings</h2>
          <button @click="showGradeSettings = false" class="close-btn">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
              <path d="M19,6.41L17.59,5L12,10.59L6.41,5L5,6.41L10.59,12L5,17.59L6.41,19L12,13.41L17.59,19L19,17.59L13.41,12L19,6.41Z" />
            </svg>
          </button>
        </div>

        <div class="modal-body">
          <div class="setting-group">
            <h3>Grading Scale</h3>
            <div class="grade-scale">
              <div class="scale-item">
                <label>A (Excellent):</label>
                <input type="number" v-model.number="gradeScale.A" min="0" max="100">%
              </div>
              <div class="scale-item">
                <label>B (Good):</label>
                <input type="number" v-model.number="gradeScale.B" min="0" max="100">%
              </div>
              <div class="scale-item">
                <label>C (Satisfactory):</label>
                <input type="number" v-model.number="gradeScale.C" min="0" max="100">%
              </div>
              <div class="scale-item">
                <label>D (Needs Improvement):</label>
                <input type="number" v-model.number="gradeScale.D" min="0" max="100">%
              </div>
            </div>
          </div>

          <div class="setting-group">
            <h3>Grade Display Options</h3>
            <div class="option-item">
              <label>
                <input type="checkbox" v-model="displayOptions.showPercentages">
                Show percentages
              </label>
            </div>
            <div class="option-item">
              <label>
                <input type="checkbox" v-model="displayOptions.showLetterGrades">
                Show letter grades
              </label>
            </div>
            <div class="option-item">
              <label>
                <input type="checkbox" v-model="displayOptions.roundToWhole">
                Round to whole numbers
              </label>
            </div>
          </div>

          <div class="modal-actions">
            <button @click="showGradeSettings = false" class="cancel-btn">Cancel</button>
            <button @click="saveGradeSettings" class="save-btn">Save Settings</button>
          </div>
        </div>
      </div>
    </div>

    <!-- Loading Overlay -->
    <div v-if="isLoading" class="loading-overlay">
      <div class="loading-content">
        <div class="loading-spinner"></div>
        <p>{{ loadingMessage }}</p>
      </div>
    </div>

    <!-- Success Toast -->
    <transition name="toast">
      <div v-if="showToast" class="toast" :class="toastType">
        {{ toastMessage }}
      </div>
      </transition>

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
    </main>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted, computed, watch } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { supabase } from '../../supabase'
import { useDarkMode } from '../../composables/useDarkMode.js'

interface Student {
  id: string
  first_name: string
  last_name: string
  email: string
  average: number | null
}

interface Assessment {
  id: string
  title: string
  total_points: number
  created_at: string
  status?: string
  type: 'quiz' | 'assignment'
  due_date?: string
}

interface AssessmentResult {
  id: string
  assessment_id: string
  student_id: string
  best_score: number
  best_percentage: number
  type: 'quiz' | 'assignment'
}

// Initialize composables
const { initDarkMode } = useDarkMode()
const router = useRouter()
const route = useRoute()

// User and authentication state
const fullName = ref('Teacher')
const isLoadingName = ref(false)
const userId = ref(null)
const teacherId = ref(null)

// UI state
const notifications = ref([])
const showNotifDropdown = ref(false)
const showProfileDropdown = ref(false)
const showScrollTop = ref(false)
const showLogoutModal = ref(false)
const isLoggingOut = ref(false)

// Grade management state
const students = ref<Student[]>([])
const assessments = ref<Assessment[]>([])
const quizzes = ref<Assessment[]>([])
const assignments = ref<Assessment[]>([])
const grades = ref<Record<string, Record<string, number>>>({})
const assessmentResults = ref<AssessmentResult[]>([])
const subject = ref<any>(null)
const section = ref<any>(null)
const subjectId = ref(route.params.subjectId as string)
const sectionId = ref(route.params.sectionId as string)

// New filter state
const selectedAssessmentType = ref('all') // 'all', 'quiz', 'assignment'
const selectedAssessment = ref('')

const isLoading = ref(false)
const loadingMessage = ref('')
const viewMode = ref('edit')
const showGradeSettings = ref(false)
const showToast = ref(false)
const toastMessage = ref('')
const toastType = ref('success')

const gradeScale = ref({ A: 90, B: 80, C: 70, D: 60 })
const displayOptions = ref({ showPercentages: true, showLetterGrades: false, roundToWhole: true })

const filteredStudents = computed(() => [...students.value])

const displayedAssessments = computed(() => {
  let filtered = assessments.value
  
  // Filter by type
  if (selectedAssessmentType.value === 'quiz') {
    filtered = assessments.value.filter(a => a.type === 'quiz')
  } else if (selectedAssessmentType.value === 'assignment') {
    filtered = assessments.value.filter(a => a.type === 'assignment')
  }
  
  // Filter by specific assessment
  if (selectedAssessment.value) {
    filtered = filtered.filter(a => a.id === selectedAssessment.value)
  }
  
  return filtered
})

// Computed for legacy compatibility
const displayedQuizzes = computed(() => displayedAssessments.value)

// Methods for UI interactions
const toggleNotifDropdown = () => {
  showNotifDropdown.value = !showNotifDropdown.value
  if (showNotifDropdown.value) {
    showProfileDropdown.value = false
  }
}

const toggleProfileDropdown = () => {
  showProfileDropdown.value = !showProfileDropdown.value
  if (showProfileDropdown.value) {
    showNotifDropdown.value = false
  }
}

const scrollToTop = () => {
  window.scrollTo({ top: 0, behavior: 'smooth' })
}

// Handle scroll to show/hide scroll-to-top button
const handleScroll = () => {
  showScrollTop.value = window.pageYOffset > 300
}

// Load teacher profile
const loadTeacherProfile = async () => {
  try {
    isLoadingName.value = true
    console.log('🔍 Loading teacher profile...')
    
    const { data: { user }, error: userError } = await supabase.auth.getUser()
    if (userError || !user) {
      console.error('❌ No user found:', userError)
      return false
    }
    
    userId.value = user.id
    console.log('✅ User ID:', user.id)
    
    // Get profile
    const { data: profile, error: profileError } = await supabase
      .from('profiles')
      .select('id, full_name, role')
      .eq('auth_user_id', user.id)
      .single()
    
    if (profileError || !profile) {
      console.error('❌ Profile error:', profileError)
      return false
    }
    
    console.log('✅ Profile found:', profile)
    
    // Get teacher data
    const { data: teacher, error: teacherError } = await supabase
      .from('teachers')
      .select('id, full_name')
      .eq('profile_id', profile.id)
      .single()
    
    if (teacherError || !teacher) {
      console.error('❌ Teacher error:', teacherError)
      return false
    }
    
    teacherId.value = teacher.id
    fullName.value = teacher.full_name || profile.full_name || 'Teacher'
    
    console.log('✅ Teacher loaded:', { id: teacher.id, name: fullName.value })
    return true
    
  } catch (err) {
    console.error('❌ Error loading profile:', err)
    return false
  } finally {
    isLoadingName.value = false
  }
}

// Load notifications
const loadNotifications = async () => {
  if (!teacherId.value) {
    console.warn('⚠️ No teacher ID, cannot load notifications')
    return
  }
  
  try {
    console.log('🔔 Loading notifications for teacher:', teacherId.value)
    
    // Get recent quiz submissions (last 24 hours)
    const yesterday = new Date()
    yesterday.setDate(yesterday.getDate() - 1)
    const yesterdayISO = yesterday.toISOString()
    
    const { data: recentSubmissions, error: submissionsError } = await supabase
      .from('quiz_attempts')
      .select(`
        id,
        submitted_at,
        student_id,
        quiz_id,
        quizzes!inner(title, teacher_id),
        students!inner(full_name)
      `)
      .eq('quizzes.teacher_id', teacherId.value)
      .eq('status', 'submitted')
      .gte('submitted_at', yesterdayISO)
      .order('submitted_at', { ascending: false })
    
    if (submissionsError) {
      console.error('❌ Error loading submissions:', submissionsError)
      return
    }
    
    // Convert submissions to notifications
    const submissionNotifications = (recentSubmissions || []).map(submission => ({
      id: `submission-${submission.id}`,
      title: `New Quiz Submission`,
      body: `${submission.students.full_name} submitted "${submission.quizzes.title}"`,
      date: new Date(submission.submitted_at).toLocaleDateString(),
      type: 'submission'
    }))
    
    notifications.value = submissionNotifications
    
    console.log('✅ Loaded', notifications.value.length, 'notifications')
    
  } catch (err) {
    console.error('❌ Error loading notifications:', err)
  }
}

const handleNotificationClick = (notif) => {
  console.log('Notification clicked:', notif)
  // Handle notification click if needed
}

// Logout functionality
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

const getInitials = (firstName: string, lastName: string): string => {
  const first = firstName?.charAt(0)?.toUpperCase() || 'S'
  const last = lastName?.charAt(0)?.toUpperCase() || 'T'
  return first + last
}

const getGradeValue = (studentId: string, quizId: string): number => grades.value[studentId]?.[quizId] || 0

const formatGrade = (grade: number, totalPoints: number): string => {
  if (!grade || !totalPoints) return '0%'
  const percentage = (grade / totalPoints) * 100
  
  if (displayOptions.value.showLetterGrades) {
    const letter = getLetterGrade(percentage)
    if (displayOptions.value.showPercentages) return `${Math.round(percentage)}% (${letter})`
    return letter
  }
  
  return displayOptions.value.roundToWhole ? `${Math.round(percentage)}%` : `${percentage.toFixed(1)}%`
}

const getLetterGrade = (percentage: number): string => {
  if (percentage >= gradeScale.value.A) return 'A'
  if (percentage >= gradeScale.value.B) return 'B'
  if (percentage >= gradeScale.value.C) return 'C'
  if (percentage >= gradeScale.value.D) return 'D'
  return 'F'
}

const getGradeClass = (grade: number, totalPoints: number): string => {
  if (!grade || !totalPoints) return 'grade-f'
  const percentage = (grade / totalPoints) * 100
  if (percentage >= 90) return 'grade-a'
  if (percentage >= 80) return 'grade-b'
  if (percentage >= 70) return 'grade-c'
  if (percentage >= 60) return 'grade-d'
  return 'grade-f'
}

const getAverageClass = (average: number | null): string => {
  if (!average) return ''
  if (average >= 90) return 'grade-a'
  if (average >= 80) return 'grade-b'
  if (average >= 70) return 'grade-c'
  if (average >= 60) return 'grade-d'
  return 'grade-f'
}

const updateGrade = (studentId: string, assessmentId: string, event: Event, assessmentType?: string) => {
  const target = event.target as HTMLInputElement
  const newGrade = Number(target.value)
  
  if (!grades.value[studentId]) grades.value[studentId] = {}
  grades.value[studentId][assessmentId] = newGrade
  calculateStudentAverage(studentId)
}

const saveGradeToDatabase = async (studentId: string, assessmentId: string, assessmentType: string) => {
  const grade = getGradeValue(studentId, assessmentId)
  const assessment = assessments.value.find(a => a.id === assessmentId)
  if (!assessment) return
  
  try {
    const percentage = (grade / assessment.total_points) * 100
    
    if (assessmentType === 'quiz') {
      // Save to quiz_results table
      const { error } = await supabase.from('quiz_results').upsert({
        quiz_id: assessmentId,
        student_id: studentId,
        best_score: grade,
        best_percentage: percentage,
        status: 'graded',
        finalized: true,
        visible_to_student: true,
        updated_at: new Date().toISOString()
      }, { onConflict: 'quiz_id,student_id' })
      
      if (error) throw error
    } else if (assessmentType === 'assignment') {
      // Save to assignment_submissions table
      const { error } = await supabase.from('assignment_submissions').upsert({
        assignment_id: assessmentId,
        student_id: studentId,
        score: grade,
        status: 'graded',
        graded_by: teacherId.value,
        graded_at: new Date().toISOString(),
        updated_at: new Date().toISOString()
      }, { onConflict: 'assignment_id,student_id' })
      
      if (error) throw error
    }
    
    showToastMessage('Grade saved successfully!', 'success')
  } catch (error) {
    console.error('Error saving grade:', error)
    showToastMessage('Failed to save grade. Please try again.', 'error')
  }
}

const calculateStudentAverage = (studentId: string) => {
  const studentGrades = grades.value[studentId]
  if (!studentGrades) return

  const gradeValues = Object.entries(studentGrades).map(([assessmentId, grade]) => {
    const assessment = assessments.value.find(a => a.id === assessmentId)
    return assessment ? (Number(grade) / assessment.total_points) * 100 : 0
  }).filter(val => val > 0)

  if (gradeValues.length > 0) {
    const average = gradeValues.reduce((a, b) => a + b, 0) / gradeValues.length
    const student = students.value.find(s => s.id === studentId)
    if (student) student.average = average
  }
}

const filterByAssessmentType = () => {
  console.log('Filtering by assessment type:', selectedAssessmentType.value)
  selectedAssessment.value = '' // Reset specific assessment filter
}

const filterByAssessment = () => {
  console.log('Filtering by assessment:', selectedAssessment.value)
}

const changeViewMode = () => {
  console.log('View mode changed to:', viewMode.value)
}

// Add date formatting function
const formatDate = (dateString: string) => {
  if (!dateString) return 'N/A'
  const date = new Date(dateString)
  return date.toLocaleDateString('en-US', {
    month: 'short',
    day: 'numeric',
    year: 'numeric'
  })
}

const saveGradeSettings = () => {
  showGradeSettings.value = false
  showToastMessage('Grade settings saved successfully!', 'success')
}

const showToastMessage = (message: string, type: string = 'success') => {
  toastMessage.value = message
  toastType.value = type
  showToast.value = true
  setTimeout(() => showToast.value = false, 3000)
}

const fetchData = async () => {
  isLoading.value = true
  loadingMessage.value = 'Loading grade data...'
  
  try {
    const [subjectRes, sectionRes] = await Promise.all([
      supabase.from('subjects').select('*').eq('id', subjectId.value).single(),
      supabase.from('sections').select('*').eq('id', sectionId.value).single()
    ])
    
    subject.value = subjectRes.data
    section.value = sectionRes.data
    
    const { data: enrollmentsData, error: enrollError } = await supabase
      .from('enrollments').select('student_id, students(id, full_name, email)')
      .eq('section_id', sectionId.value).eq('status', 'active')
    
    if (enrollError) throw enrollError
    
    students.value = enrollmentsData?.map((enrollment: any) => {
      const studentData = enrollment.students
      const fullName = studentData.full_name || ''
      const nameParts = fullName.split(' ')
      
      return {
        id: studentData.id,
        first_name: nameParts[0] || 'Unknown',
        last_name: nameParts.slice(1).join(' ') || 'Student',
        email: studentData.email || '',
        average: null
      }
    }) || []
    
    // Fetch quizzes
    const { data: quizzesData, error: quizzesError } = await supabase
      .from('quizzes').select('id, title, created_at, status')
      .eq('subject_id', subjectId.value).eq('section_id', sectionId.value)
      .eq('status', 'published').order('created_at', { ascending: true })
    
    if (quizzesError) throw quizzesError
    
    const quizzesWithPoints: Assessment[] = []
    for (const quiz of quizzesData || []) {
      const { data: questionsData } = await supabase
        .from('quiz_questions').select('points').eq('quiz_id', quiz.id)
      
      const totalPoints = questionsData?.reduce((sum, q) => sum + (q.points || 0), 0) || 100
      
      quizzesWithPoints.push({
        id: quiz.id,
        title: quiz.title,
        created_at: quiz.created_at,
        status: quiz.status,
        total_points: totalPoints,
        type: 'quiz'
      })
    }
    
    // Fetch assignments
    const { data: assignmentsData, error: assignmentsError } = await supabase
      .from('assignments').select('id, title, total_points, created_at, status, due_date')
      .eq('subject_id', subjectId.value).eq('section_id', sectionId.value)
      .eq('status', 'published').order('created_at', { ascending: true })
    
    if (assignmentsError) throw assignmentsError
    
    const assignmentsWithType: Assessment[] = (assignmentsData || []).map(assignment => ({
      id: assignment.id,
      title: assignment.title,
      created_at: assignment.created_at,
      status: assignment.status,
      total_points: assignment.total_points || 100,
      type: 'assignment' as const,
      due_date: assignment.due_date
    }))
    
    // Combine and set data
    quizzes.value = quizzesWithPoints
    assignments.value = assignmentsWithType
    assessments.value = [...quizzesWithPoints, ...assignmentsWithType].sort((a, b) => 
      new Date(a.created_at).getTime() - new Date(b.created_at).getTime()
    )
    
    // Load grades for both quizzes and assignments
    if (assessments.value.length > 0 && students.value.length > 0) {
      grades.value = {}
      assessmentResults.value = []
      
      // Load quiz results
      if (quizzesWithPoints.length > 0) {
        const { data: quizResultsData, error: quizResultsError } = await supabase
          .from('quiz_results').select('*')
          .in('quiz_id', quizzesWithPoints.map(q => q.id))
          .in('student_id', students.value.map(s => s.id))
        
        if (quizResultsError) throw quizResultsError
        
        quizResultsData?.forEach((result: any) => {
          if (!grades.value[result.student_id]) grades.value[result.student_id] = {}
          grades.value[result.student_id][result.quiz_id] = result.best_score || 0
          
          assessmentResults.value.push({
            id: result.id,
            assessment_id: result.quiz_id,
            student_id: result.student_id,
            best_score: result.best_score || 0,
            best_percentage: result.best_percentage || 0,
            type: 'quiz'
          })
        })
      }
      
      // Load assignment submissions
      if (assignmentsWithType.length > 0) {
        const { data: assignmentSubmissions, error: assignmentSubmissionsError } = await supabase
          .from('assignment_submissions').select('*')
          .in('assignment_id', assignmentsWithType.map(a => a.id))
          .in('student_id', students.value.map(s => s.id))
          .eq('status', 'graded')
        
        if (assignmentSubmissionsError) throw assignmentSubmissionsError
        
        assignmentSubmissions?.forEach((submission: any) => {
          if (!grades.value[submission.student_id]) grades.value[submission.student_id] = {}
          grades.value[submission.student_id][submission.assignment_id] = submission.score || 0
          
          // Calculate percentage for assignment
          const assignment = assignmentsWithType.find(a => a.id === submission.assignment_id)
          const percentage = assignment ? (submission.score / assignment.total_points) * 100 : 0
          
          assessmentResults.value.push({
            id: submission.id,
            assessment_id: submission.assignment_id,
            student_id: submission.student_id,
            best_score: submission.score || 0,
            best_percentage: percentage,
            type: 'assignment'
          })
        })
      }
    }
    
    students.value.forEach(student => calculateStudentAverage(student.id))
  } catch (error) {
    console.error('Error fetching data:', error)
    showToastMessage('Failed to load grade data. Please try again.', 'error')
  } finally {
    isLoading.value = false
  }
}

const goBack = () => {
  router.push('/teacher/subjects')
}

const exportGrades = () => {
  if (students.value.length === 0) {
    showToastMessage('No data to export', 'error')
    return
  }
  
  try {
    // Create headers with assessment names and types
    const assessmentHeaders = displayedAssessments.value.map(a => `${a.title} (${a.type === 'quiz' ? 'Quiz' : 'Assignment'})`)
    let csv = 'Student Name,Email,' + assessmentHeaders.join(',') + ',Average\n'
    
    students.value.forEach(student => {
      csv += `"${student.first_name} ${student.last_name}","${student.email}",`
      displayedAssessments.value.forEach(assessment => {
        const grade = getGradeValue(student.id, assessment.id)
        const percentage = assessment.total_points ? Math.round((grade / assessment.total_points) * 100) : 0
        csv += `${percentage}%,`
      })
      csv += `${student.average ? Math.round(student.average) + '%' : 'N/A'}\n`
    })
    
    const blob = new Blob([csv], { type: 'text/csv' })
    const url = window.URL.createObjectURL(blob)
    const a = document.createElement('a')
    a.href = url
    a.download = `${subject.value?.name}_${section.value?.name}_grades.csv`
    document.body.appendChild(a)
    a.click()
    document.body.removeChild(a)
    window.URL.revokeObjectURL(url)
    
    showToastMessage('Grades exported successfully!', 'success')
  } catch (error) {
    console.error('Error exporting grades:', error)
    showToastMessage('Failed to export grades', 'error')
  }
}

watch(() => grades.value, () => {
  students.value.forEach(student => calculateStudentAverage(student.id))
}, { deep: true })

onMounted(async () => {
  initDarkMode()
  
  // Add scroll event listener
  window.addEventListener('scroll', handleScroll)
  
  // Load teacher profile first
  await loadTeacherProfile()
  
  // Load notifications
  await loadNotifications()
  
  await fetchData()
})

onUnmounted(() => {
  // Remove scroll event listener
  window.removeEventListener('scroll', handleScroll)
})
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.grade-management-page {
  min-height: 100vh;
  height: 100vh;
  width: 100vw;
  background: #f8fafc;
  font-family: 'Inter', sans-serif;
  overflow: hidden;
  display: flex;
  flex-direction: column;
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

/* Sidebar Divider */
.sidebar-divider {
  height: 1px;
  background: rgba(255, 255, 255, 0.2);
  margin: 8px 12px;
}

/* Sidebar Logout Button */
.sidebar-logout {
  background: transparent;
  border: none;
  cursor: pointer;
  padding: 0;
  margin: 0;
  display: flex;
  align-items: center;
  justify-content: center;
}

.sidebar-logout:hover {
  background: rgba(255, 255, 255, 0.1);
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
  gap: 0.75rem;
  color: white;
  font-weight: 700;
  text-decoration: none;
  transition: opacity 0.2s;
}

.brand-logo:hover {
  opacity: 0.9;
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

/* Breadcrumb Navigation */
.page-breadcrumb {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  color: rgba(255, 255, 255, 0.9);
  font-size: 0.9rem;
  font-weight: 500;
}

.breadcrumb-back {
  background: rgba(255, 255, 255, 0.15);
  border: none;
  border-radius: 50%;
  width: 32px;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  cursor: pointer;
  transition: all 0.2s;
}

.breadcrumb-back:hover {
  background: rgba(255, 255, 255, 0.25);
  transform: translateX(-2px);
}

.breadcrumb-item {
  color: rgba(255, 255, 255, 0.8);
  transition: color 0.2s;
}

.breadcrumb-item:hover {
  color: white;
}

.breadcrumb-separator {
  color: rgba(255, 255, 255, 0.6);
  margin: 0 0.25rem;
}

.breadcrumb-current {
  color: white;
  font-weight: 600;
}

/* Action Buttons */
.action-btn {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1.25rem;
  border-radius: 8px;
  font-weight: 500;
  font-size: 0.875rem;
  cursor: pointer;
  transition: all 0.2s;
  border: none;
  text-decoration: none;
}

.action-btn.secondary {
  background: rgba(255, 255, 255, 0.15);
  color: white;
  border: 1px solid rgba(255, 255, 255, 0.2);
}

.action-btn.secondary:hover {
  background: rgba(255, 255, 255, 0.25);
  border-color: rgba(255, 255, 255, 0.3);
  transform: translateY(-1px);
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

.export-btn:hover:not(:disabled) {
  background: rgba(255, 255, 255, 0.25);
  border-color: rgba(255, 255, 255, 0.3);
  transform: translateY(-1px);
}

.export-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
  transform: none;
}

/* User Profile and Notifications */
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

.notification-badge {
  position: absolute;
  top: 6px;
  right: 6px;
  background: #ef4444;
  color: white;
  font-size: 0.7rem;
  font-weight: 600;
  padding: 0.125rem 0.375rem;
  border-radius: 10px;
  min-width: 18px;
  text-align: center;
  line-height: 1;
}

.notif-wrapper {
  position: relative;
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

.dropdown-header {
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

/* Rounded semi-transparent backgrounds for sidebar and navbar icons/buttons */
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
  height: calc(100vh - 64px);
  width: 100vw;
  overflow-y: auto;
  overflow-x: hidden;
  position: relative;
}

/* Custom Scrollbar for Main Content */
.main-content::-webkit-scrollbar {
  width: 10px;
}

.main-content::-webkit-scrollbar-track {
  background: #e2e8f0;
  border-radius: 5px;
  margin: 4px;
}

.main-content::-webkit-scrollbar-thumb {
  background: #94a3b8;
  border-radius: 5px;
  border: 1px solid #e2e8f0;
  transition: all 0.2s;
}

.main-content::-webkit-scrollbar-thumb:hover {
  background: #64748b;
  border-color: #cbd5e1;
}

.dark .main-content::-webkit-scrollbar-track {
  background: #334155;
}

.dark .main-content::-webkit-scrollbar-thumb {
  background: #64748b;
}

.dark .main-content::-webkit-scrollbar-thumb:hover {
  background: #94a3b8;
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
  transition: all 0.2s;
  z-index: 900;
}

.scroll-to-top:hover {
  background: #2d6a5a;
  transform: translateY(-2px);
  box-shadow: 0 6px 16px rgba(61, 141, 122, 0.4);
}

/* Main Container */
.main-container {
  width: 100%;
  max-width: 100%;
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
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
  letter-spacing: -0.025em;
}

.header-subtitle {
  font-size: 0.95rem;
  color: #64748b;
  margin: 0;
  font-weight: 500;
}

.header-actions {
  display: flex;
  gap: 1rem;
}

.action-btn {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1.5rem;
  border-radius: 10px;
  font-weight: 600;
  font-size: 0.875rem;
  text-decoration: none;
  transition: all 0.2s ease;
  border: none;
  cursor: pointer;
}

.action-btn.primary {
  background: #10b981;
  color: white;
  border: 1px solid #10b981;
}

.action-btn.primary:hover {
  background: #059669;
  border-color: #047857;
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(16, 185, 129, 0.25);
}

.action-btn.secondary {
  background: #f1f5f9;
  color: #475569;
  border: 1px solid #e2e8f0;
}

.action-btn.secondary:hover {
  background: #e2e8f0;
  color: #1e293b;
  transform: translateY(-1px);
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

.export-btn:hover:not(:disabled) {
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

.grade-management-page { min-height: 100vh; background: #FBFFE4; padding: 1.5rem; font-family: 'Inter', sans-serif; }
.dark .grade-management-page { background: #181c20; }

/* Header Card - Matching MySubjects Style */
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

.header-content { display: flex; align-items: center; justify-content: space-between; }
.header-left { display: flex; align-items: center; gap: 1rem; }
.header-icon { width: 56px; height: 56px; background: #3D8D7A; border-radius: 12px; display: flex; align-items: center; justify-content: center; color: white; }
.header-title { font-size: 1.5rem; font-weight: 700; color: #1f2937; margin-bottom: 0.25rem; }
.dark .header-title { color: #A3D1C6; }
.header-subtitle { font-size: 0.875rem; color: #6b7280; }
.dark .header-subtitle { color: #A3D1C6; }

.back-btn { 
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
.back-btn:hover {
  background: #A3D1C6;
  color: #23272b;
  border-color: #20c997;
  transform: translateY(-1px);
}
.dark .back-btn {
  background: #20c997;
  color: #181c20;
  border: 1px solid #A3D1C6;
}
.dark .back-btn:hover {
  background: #A3D1C6;
  color: #23272b;
  border-color: #20c997;
}

/* Section Header Styles - Match DashboardHome */
.section-header {
  margin-bottom: 1.5rem;
}

.section-header .header-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: white;
  padding: 1.5rem 2rem;
  border-radius: 16px;
  border: 1px solid #e2e8f0;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
}

.section-header .header-left {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.section-header .header-icon {
  width: 56px;
  height: 56px;
  background: linear-gradient(135deg, #3D8D7A, #2d6a5a);
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
}

.section-title {
  font-size: 1.75rem;
  font-weight: 700;
  color: #1e293b;
  margin-bottom: 0.25rem;
  letter-spacing: -0.025em;
}

.section-subtitle {
  font-size: 0.95rem;
  color: #64748b;
  margin: 0;
  font-weight: 500;
}

.header-actions {
  display: flex;
  gap: 1rem;
}

.action-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1.25rem;
  border-radius: 12px;
  border: none;
  font-size: 0.9rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
  text-decoration: none;
}

.action-btn.primary {
  background: #3D8D7A;
  color: white;
}

.action-btn.primary:hover {
  background: #2d6a5a;
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(61, 141, 122, 0.3);
}

.action-btn.secondary {
  background: #f8fafc;
  color: #64748b;
  border: 1px solid #e2e8f0;
}

.action-btn.secondary:hover {
  background: white;
  border-color: #cbd5e1;
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.controls-card { 
  background: white; 
  border: 1.5px solid #e5e7eb;
  border-radius: 16px; 
  padding: 1.5rem; 
  margin-bottom: 1.5rem; 
  box-shadow: 0 2px 8px rgba(0,0,0,0.04);
  transition: all 0.18s ease;
}
.dark .controls-card { 
  background: #23272b; 
  border: 1.5px solid #374151; 
  box-shadow: 0 2px 8px rgba(32, 201, 151, 0.13);
}

.controls-title { 
  font-size: 1.25rem; 
  font-weight: 700; 
  color: #1f2937; 
  margin-bottom: 1rem; 
  line-height: 1.3;
}
.dark .controls-title { 
  color: #f9fafb; 
}

.controls-content { display: grid; grid-template-columns: 1fr auto auto; gap: 1rem; align-items: center; }
.filters { display: flex; gap: 1rem; align-items: center; }

.filter-select { 
  background: #f8f9fa;
  border: 2px solid #e5e7eb;
  border-radius: 10px;
  padding: 0.75rem 1rem;
  font-size: 0.875rem;
  font-family: 'Inter', sans-serif;
  color: #1f2937;
  transition: all 0.2s;
  min-width: 150px;
  cursor: pointer;
  outline: none;
}
.filter-select:focus { 
  border-color: #10b981; 
  box-shadow: 0 0 0 3px rgba(16, 185, 129, 0.1); 
}
.dark .filter-select { 
  background: #374151; 
  border-color: #4b5563; 
  color: #f3f4f6; 
}
.dark .filter-select:focus {
  border-color: #10b981;
  box-shadow: 0 0 0 3px rgba(16, 185, 129, 0.1);
}

.primary-btn, .secondary-btn { 
  display: flex; 
  align-items: center; 
  gap: 0.5rem; 
  padding: 0.5rem 1.25rem; 
  border-radius: 8px; 
  font-weight: 500; 
  font-size: 0.875rem; 
  cursor: pointer; 
  transition: all 0.2s; 
  border: 1px solid transparent;
  outline: none;
}

.primary-btn { 
  background: #20c997; 
  color: #181c20;
  border-color: #A3D1C6;
}
.primary-btn:hover { 
  background: #A3D1C6; 
  color: #23272b;
  border-color: #20c997;
  transform: translateY(-1px);
}
.dark .primary-btn {
  background: #20c997;
  color: #181c20;
  border-color: #A3D1C6;
}
.dark .primary-btn:hover {
  background: #A3D1C6;
  color: #23272b;
  border-color: #20c997;
}

.secondary-btn { 
  background: white; 
  color: #374151; 
  border: 1px solid #d1d5db; 
}
.secondary-btn:hover:not(:disabled) { 
  background: #B3D8A8; 
  border-color: #3D8D7A; 
  color: #1f2937;
  transform: translateY(-1px);
}
.secondary-btn:disabled { 
  opacity: 0.5; 
  cursor: not-allowed; 
}
.dark .secondary-btn { 
  background: #374151; 
  color: #e5e7eb; 
  border-color: #4b5563; 
}
.dark .secondary-btn:hover:not(:disabled) {
  background: #3D8D7A;
  border-color: #A3D1C6;
  color: white;
}

.table-container { 
  background: #fff;
  border: 1.5px solid #e5e7eb;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.04);
  padding: 0;
  margin-bottom: 1rem;
  transition: all 0.18s ease;
  overflow: hidden;
}
.dark .table-container { 
  background: #23272b; 
  border: 1.5px solid #374151; 
  box-shadow: 0 2px 8px rgba(32, 201, 151, 0.13);
}

.table-header { 
  background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
  padding: 1.5rem; 
  border-bottom: 1px solid #e2e8f0;
}
.dark .table-header { 
  background: #1f2937; 
  border-bottom: 1px solid #374151;
}
.table-title { 
  font-size: 1.25rem; 
  font-weight: 700; 
  color: #1f2937; 
  margin: 0;
  line-height: 1.3;
}
.dark .table-title { 
  color: #f9fafb; 
}

.table-wrapper { 
  overflow-x: auto; 
  max-width: 100%;
}

/* Custom scrollbar for table wrapper */
.table-wrapper::-webkit-scrollbar {
  height: 6px;
}

.table-wrapper::-webkit-scrollbar-track {
  background: #f1f5f9;
  border-radius: 3px;
}

.table-wrapper::-webkit-scrollbar-thumb {
  background: #cbd5e1;
  border-radius: 3px;
  transition: background 0.2s;
}

.table-wrapper::-webkit-scrollbar-thumb:hover {
  background: #94a3b8;
}

.dark .table-wrapper::-webkit-scrollbar-track {
  background: #334155;
}

.dark .table-wrapper::-webkit-scrollbar-thumb {
  background: #64748b;
}

.dark .table-wrapper::-webkit-scrollbar-thumb:hover {
  background: #94a3b8;
}
.grade-table { width: 100%; border-collapse: collapse; min-width: 1200px; }

/* Table Styling */
.grade-table thead tr {
  background: linear-gradient(135deg, #3D8D7A 0%, #20c997 100%);
  border-bottom: 2px solid #A3D1C6;
}
.dark .grade-table thead tr {
  background: linear-gradient(135deg, #20c997 0%, #3D8D7A 100%);
  border-bottom-color: #A3D1C6;
}

.grade-table th {
  padding: 1rem;
  text-align: center;
  font-weight: 600;
  color: #ffffff;
  font-size: 0.875rem;
  border-right: 1px solid rgba(255, 255, 255, 0.2);
}
.grade-table th:last-child {
  border-right: none;
}
.dark .grade-table th {
  color: #ffffff;
}

.column-header {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.25rem;
}

.quiz-header {
  min-height: 60px;
  justify-content: center;
}

.quiz-title {
  font-size: 0.875rem;
  font-weight: 600;
  line-height: 1.2;
}

.quiz-points {
  font-size: 0.75rem;
  opacity: 0.8;
  font-weight: 400;
}

.grade-table tbody tr {
  border-bottom: 1px solid #e5e7eb;
  transition: background-color 0.2s;
}
.grade-table tbody tr:hover {
  background: rgba(61, 141, 122, 0.02);
}
.dark .grade-table tbody tr:hover {
  background: rgba(32, 201, 151, 0.05);
}
.dark .grade-table tbody tr {
  border-bottom-color: #374151;
}

.grade-table td {
  padding: 1rem;
  color: #374151;
  border-right: 1px solid #f3f4f6;
  vertical-align: middle;
}
.grade-table td:last-child {
  border-right: none;
}
.dark .grade-table td {
  color: #e5e7eb;
  border-right-color: #374151;
}

.student-column {
  min-width: 280px;
  width: 280px;
  text-align: left;
}

.quiz-column {
  min-width: 140px;
  text-align: center;
  padding: 0.75rem;
}

.average-column {
  min-width: 120px;
  text-align: center;
}

/* Grade Cell Styling */
.grade-cell {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.25rem;
}

.grade-display {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.25rem;
  padding: 0.75rem 0.5rem;
  border-radius: 8px;
  min-width: 80px;
  transition: all 0.2s;
}

.grade-score {
  font-size: 1.1rem;
  font-weight: 700;
}

.grade-separator {
  margin: 0 0.25rem;
  font-weight: 500;
  opacity: 0.7;
}

.grade-total {
  font-weight: 500;
  opacity: 0.8;
}

.grade-percentage {
  font-size: 0.75rem;
  font-weight: 600;
  margin-top: 0.25rem;
  padding: 0.25rem 0.5rem;
  background: rgba(255, 255, 255, 0.2);
  border-radius: 12px;
}

/* Average Cell Styling */
.average-cell {
  display: flex;
  justify-content: center;
}

.average-display {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.25rem;
  padding: 0.75rem 1rem;
  border-radius: 8px;
  min-width: 80px;
  transition: all 0.2s;
}

.average-percentage {
  font-size: 1.25rem;
  font-weight: 700;
}

.average-label {
  font-size: 0.75rem;
  font-weight: 600;
  opacity: 0.8;
}

/* Student Info Styling */
.student-info {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 0.5rem;
}

.student-avatar {
  width: 48px;
  height: 48px;
  border-radius: 12px;
  background: linear-gradient(135deg, #3D8D7A, #20c997);
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 0.875rem;
  flex-shrink: 0;
  box-shadow: 0 2px 8px rgba(61, 141, 122, 0.2);
}

.student-details {
  display: flex;
  flex-direction: column;
  min-width: 0;
  flex: 1;
}

.student-name {
  font-weight: 600;
  color: #1f2937;
  font-size: 0.875rem;
  line-height: 1.4;
  margin-bottom: 0.25rem;
}
.dark .student-name {
  color: #e5e7eb;
}

.student-email {
  font-size: 0.75rem;
  color: #6b7280;
  line-height: 1.2;
}
.dark .student-email {
  color: #9ca3af;
}

/* Grade Input Styling */
.grade-input {
  width: 100%;
  max-width: 100px;
  padding: 0.75rem 0.5rem;
  border: 2px solid #e5e7eb;
  border-radius: 8px;
  font-size: 0.875rem;
  text-align: center;
  outline: none;
  transition: all 0.2s;
  background: #f8f9fa;
  font-weight: 500;
}
.grade-input:focus {
  border-color: #10b981;
  box-shadow: 0 0 0 3px rgba(16, 185, 129, 0.1);
  background: white;
}
.dark .grade-input {
  background: #374151;
  border-color: #4b5563;
  color: #e5e7eb;
}
.dark .grade-input:focus {
  border-color: #10b981;
  box-shadow: 0 0 0 3px rgba(16, 185, 129, 0.1);
  background: #4b5563;
}

/* No Quizzes Styling */
.no-quizzes-column {
  min-width: 200px;
  text-align: center;
}

.no-quiz-message {
  color: #6b7280;
  font-style: italic;
  padding: 1rem;
}
.dark .no-quiz-message {
  color: #9ca3af;
}

.quiz-debug {
  background: #fef3c7;
  padding: 1rem;
  margin-bottom: 1rem;
  border-radius: 8px;
  color: #92400e;
  border: 1px solid #fed7aa;
}
.dark .quiz-debug {
  background: rgba(251, 146, 60, 0.1);
  color: #fed7aa;
  border-color: rgba(251, 146, 60, 0.3);
}

/* Grade Display Classes */
.grade-a {
  background: #dcfce7;
  color: #166534;
}
.dark .grade-a {
  background: rgba(34, 197, 94, 0.2);
  color: #86efac;
}

.grade-b {
  background: #dbeafe;
  color: #1e40af;
}
.dark .grade-b {
  background: rgba(59, 130, 246, 0.2);
  color: #93c5fd;
}

.grade-c {
  background: #fef3c7;
  color: #92400e;
}
.dark .grade-c {
  background: rgba(251, 146, 60, 0.2);
  color: #fed7aa;
}

.grade-d {
  background: #fee2e2;
  color: #7f1d1d;
}
.dark .grade-d {
  background: rgba(239, 68, 68, 0.2);
  color: #fca5a5;
}

.grade-f {
  background: #fecaca;
  color: #7f1d1d;
}
.dark .grade-f {
  background: rgba(220, 38, 38, 0.2);
  color: #fca5a5;
}

/* Empty State */
.empty-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 3rem;
  color: #9ca3af;
}
.dark .empty-state {
  color: #6b7280;
}

.empty-state h3 {
  font-size: 1.125rem;
  margin-bottom: 0.5rem;
  color: #374151;
}
.dark .empty-state h3 {
  color: #e5e7eb;
}

/* Modal */
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

.modal-content {
  background: white;
  border-radius: 16px;
  box-shadow: 0 20px 25px rgba(0, 0, 0, 0.15);
  max-width: 500px;
  width: 100%;
  max-height: 90vh;
  overflow-y: auto;
}
.dark .modal-content {
  background: #23272b;
  border: 1px solid #3D8D7A;
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

.modal-header h2 {
  font-size: 1.25rem;
  font-weight: 700;
  color: #1f2937;
}
.dark .modal-header h2 {
  color: #A3D1C6;
}

.close-btn {
  background: none;
  border: none;
  cursor: pointer;
  padding: 0.5rem;
  color: #6b7280;
  transition: color 0.2s;
}
.close-btn:hover {
  color: #1f2937;
}
.dark .close-btn:hover {
  color: #e5e7eb;
}

.modal-body {
  padding: 1.5rem;
}

.setting-group {
  margin-bottom: 1.5rem;
}

.setting-group h3 {
  font-size: 0.95rem;
  font-weight: 600;
  margin-bottom: 1rem;
  color: #1f2937;
}
.dark .setting-group h3 {
  color: #A3D1C6;
}

.grade-scale {
  display: grid;
  gap: 0.75rem;
}

.scale-item {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.scale-item label {
  min-width: 150px;
  color: #374151;
  font-size: 0.875rem;
  font-weight: 500;
}
.dark .scale-item label {
  color: #e5e7eb;
}

.scale-item input {
  width: 80px;
  padding: 0.5rem;
  border: 1px solid #d1d5db;
  border-radius: 6px;
  font-size: 0.875rem;
  text-align: center;
  outline: none;
}
.scale-item input:focus {
  border-color: #3D8D7A;
  box-shadow: 0 0 0 3px rgba(61, 141, 122, 0.1);
}
.dark .scale-item input {
  background: #374151;
  border-color: #4b5563;
  color: #e5e7eb;
}

.option-item {
  display: flex;
  align-items: center;
  margin-bottom: 0.75rem;
}

.option-item input[type="checkbox"] {
  width: 18px;
  height: 18px;
  margin-right: 0.75rem;
  cursor: pointer;
  accent-color: #3D8D7A;
}

.option-item label {
  display: flex;
  align-items: center;
  cursor: pointer;
  font-size: 0.875rem;
  color: #374151;
}
.dark .option-item label {
  color: #e5e7eb;
}

.modal-actions {
  display: flex;
  gap: 1rem;
  margin-top: 1.5rem;
  padding-top: 1.5rem;
  border-top: 1px solid #e5e7eb;
}
.dark .modal-actions {
  border-top-color: #3D8D7A;
}

.cancel-btn, .save-btn {
  flex: 1;
  padding: 0.75rem;
  border-radius: 8px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s;
  border: none;
  font-size: 0.875rem;
}

.cancel-btn {
  background: #e5e7eb;
  color: #374151;
}
.cancel-btn:hover {
  background: #d1d5db;
}
.dark .cancel-btn {
  background: #374151;
  color: #e5e7eb;
}
.dark .cancel-btn:hover {
  background: #4b5563;
}

.save-btn {
  background: #3D8D7A;
  color: white;
}
.save-btn:hover {
  background: #2a6257;
}

/* Loading Overlay */
.loading-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.7);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 999;
}

.loading-content {
  text-align: center;
  color: white;
}

.loading-spinner {
  width: 40px;
  height: 40px;
  border: 4px solid rgba(255, 255, 255, 0.3);
  border-top-color: white;
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
  margin: 0 auto 1rem;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

.loading-content p {
  font-size: 0.95rem;
  margin-top: 0.5rem;
}

/* Toast Notification */
.toast {
  position: fixed;
  bottom: 2rem;
  right: 2rem;
  padding: 1rem 1.5rem;
  border-radius: 8px;
  font-weight: 500;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  z-index: 1001;
  max-width: 400px;
}

.toast.success {
  background: #dcfce7;
  color: #166534;
  border: 1px solid #86efac;
}

.toast.error {
  background: #fee2e2;
  color: #7f1d1d;
  border: 1px solid #fca5a5;
}

.toast-enter-active, .toast-leave-active {
  transition: all 0.3s ease;
}

.toast-enter-from {
  transform: translateX(400px);
  opacity: 0;
}

.toast-leave-to {
  transform: translateX(400px);
  opacity: 0;
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
  
  .controls-content {
    grid-template-columns: 1fr;
  }
  
  .filters {
    flex-wrap: wrap;
  }
  
  .student-column {
    min-width: 200px;
    width: 200px;
  }
  
  .quiz-column {
    min-width: 100px;
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
  
  .header-content {
    flex-direction: column;
    gap: 1rem;
    align-items: flex-start;
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
  
  .table-wrapper {
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
  }
  
  .student-column {
    min-width: 180px;
  }
  
  .quiz-column {
    min-width: 90px;
    font-size: 0.75rem;
    padding: 0.75rem 0.5rem;
  }
  
  .grade-input, .grade-display {
    padding: 0.4rem 0.25rem;
    font-size: 0.75rem;
  }
  
  .modal-content {
    margin: 0 1rem;
  }
  
  .toast {
    bottom: 1rem;
    right: 1rem;
    left: 1rem;
    max-width: none;
  }
}

@media (max-width: 480px) {
  .header-icon {
    width: 48px;
    height: 48px;
  }
  
  .header-title {
    font-size: 1.25rem;
  }
  
  .controls-title {
    font-size: 1rem;
  }
  
  .filter-select {
    min-width: 120px;
  }
  
  .student-avatar {
    width: 36px;
    height: 36px;
    font-size: 0.75rem;
  }
  
  .student-column {
    min-width: 150px;
  }
  
  .quiz-column {
    min-width: 80px;
  }
  
  .modal-body {
    padding: 1rem;
  }
  
  .scale-item {
    flex-direction: column;
    align-items: flex-start;
  }
  
  .scale-item label {
    min-width: auto;
    margin-bottom: 0.25rem;
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

/* Enhanced Scrollable Table Styles */
.scrollable-table-container {
  overflow: auto;
  max-height: calc(100vh - 280px);
  max-width: 100%;
  scrollbar-width: thin;
  scrollbar-color: #94a3b8 #e2e8f0;
  position: relative;
  border-radius: 12px;
  border: 1px solid #e2e8f0;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
  background: white;
}

.scrollable-table-container::-webkit-scrollbar {
  width: 12px;
  height: 12px;
}

.scrollable-table-container::-webkit-scrollbar-track {
  background: #e2e8f0;
  border-radius: 6px;
  margin: 4px;
}

.scrollable-table-container::-webkit-scrollbar-thumb {
  background: #94a3b8;
  border-radius: 6px;
  border: 2px solid #e2e8f0;
  transition: all 0.2s;
}

.scrollable-table-container::-webkit-scrollbar-thumb:hover {
  background: #64748b;
  border-color: #cbd5e1;
}

.scrollable-table-container::-webkit-scrollbar-corner {
  background: #f1f5f9;
}

.dark .scrollable-table-container {
  scrollbar-color: #64748b #334155;
}

.dark .scrollable-table-container::-webkit-scrollbar-track {
  background: #374151;
  border-radius: 6px;
  margin: 4px;
}

.dark .scrollable-table-container::-webkit-scrollbar-thumb {
  background: #64748b;
  border-radius: 6px;
  border: 2px solid #374151;
  transition: all 0.2s;
}

.dark .scrollable-table-container::-webkit-scrollbar-thumb:hover {
  background: #94a3b8;
  border-color: #4b5563;
}

.dark .scrollable-table-container::-webkit-scrollbar-corner {
  background: #334155;
}

/* Sticky columns for better scrolling experience */
.sticky-column {
  position: sticky;
  background: white;
  z-index: 2;
}

.dark .sticky-column {
  background: #23272b;
}

.student-column.sticky-column {
  left: 0;
  box-shadow: 2px 0 4px rgba(0, 0, 0, 0.1);
}

.average-column.sticky-column {
  right: 0;
  box-shadow: -2px 0 4px rgba(0, 0, 0, 0.1);
}

.dark .student-column.sticky-column,
.dark .average-column.sticky-column {
  box-shadow: 2px 0 4px rgba(0, 0, 0, 0.3);
}

/* Assessment column styling for different types */
.assessment-column.quiz-column {
  background: rgba(59, 130, 246, 0.02);
}

.assessment-column.assignment-column {
  background: rgba(245, 158, 11, 0.02);
}

.dark .assessment-column.quiz-column {
  background: rgba(59, 130, 246, 0.05);
}

.dark .assessment-column.assignment-column {
  background: rgba(245, 158, 11, 0.05);
}

/* Assessment header styling */
.assessment-header {
  min-height: 80px;
  justify-content: center;
  text-align: center;
}

.assessment-title {
  font-size: 0.875rem;
  font-weight: 600;
  line-height: 1.2;
  margin-bottom: 0.5rem;
}

.assessment-meta {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.25rem;
}

.assessment-type {
  padding: 0.25rem 0.5rem;
  border-radius: 12px;
  font-size: 0.7rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.assessment-type.quiz {
  background: #dbeafe;
  color: #1e40af;
}

.assessment-type.assignment {
  background: #fef3c7;
  color: #92400e;
}

.dark .assessment-type.quiz {
  background: rgba(59, 130, 246, 0.2);
  color: #93c5fd;
}

.dark .assessment-type.assignment {
  background: rgba(245, 158, 11, 0.2);
  color: #fcd34d;
}

.assessment-points {
  font-size: 0.75rem;
  opacity: 0.8;
  font-weight: 400;
}

.assessment-due {
  font-size: 0.7rem;
  opacity: 0.7;
  font-style: italic;
  margin-top: 0.25rem;
}

.assessment-count {
  font-weight: 500;
  opacity: 0.8;
  font-size: 0.9rem;
}

/* No assessments styling */
.no-assessments-column {
  min-width: 200px;
  text-align: center;
}

.no-assessment-message {
  color: #6b7280;
  font-style: italic;
  padding: 1rem;
}

.dark .no-assessment-message {
  color: #9ca3af;
}

.assessment-debug {
  background: #fef3c7;
  padding: 1rem;
  margin-bottom: 1rem;
  border-radius: 8px;
  color: #92400e;
  border: 1px solid #fed7aa;
}

.dark .assessment-debug {
  background: rgba(251, 146, 60, 0.1);
  color: #fed7aa;
  border-color: rgba(251, 146, 60, 0.3);
}

/* Mobile responsiveness for scrollable table */
@media (max-width: 768px) {
  .scrollable-table-container {
    max-height: 60vh;
  }
  
  .assessment-header {
    min-height: 70px;
  }
  
  .assessment-title {
    font-size: 0.8rem;
  }
  
  .assessment-type {
    font-size: 0.65rem;
    padding: 0.2rem 0.4rem;
  }
  
  .assessment-points {
    font-size: 0.7rem;
  }
}

</style>
