<template>
  <div class="dashboard-container">
    <!-- Top Navigation Bar (Facebook-style) -->
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
          <router-link to="/teacher/dashboard" class="nav-item active">
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
          
          <router-link to="/teacher/gradebook" class="nav-item">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M19,3H14.82C14.4,1.84 13.3,1 12,1C10.7,1 9.6,1.84 9.18,3H5A2,2 0 0,0 3,5V19A2,2 0 0,0 5,21H19A2,2 0 0,0 21,19V5A2,2 0 0,0 19,3M12,3A1,1 0 0,1 13,4A1,1 0 0,1 12,5A1,1 0 0,1 11,4A1,1 0 0,1 12,3Z" />
            </svg>
            <span>Gradebook</span>
          </router-link>
          
          <router-link to="/teacher/upload-assessment" class="nav-item">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M9,16V10H5L12,3L19,10H15V16H9M5,20V18H19V20H5Z" />
            </svg>
            <span>Upload</span>
          </router-link>
        </div>
        
        <!-- Right: User Profile and Notifications -->
        <div class="navbar-right">
          <!-- Notification Bell -->
          <div class="notif-wrapper">
            <button class="nav-icon-btn" @click="toggleNotifDropdown" aria-label="Notifications">
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
                <div v-for="notif in notifications" :key="notif.id" class="notification-item">
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
            <div class="user-profile" @click="toggleProfileDropdown">
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
                <router-link to="/teacher/profile" class="dropdown-item">
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M12 2C13.1 2 14 2.9 14 4C14 5.1 13.1 6 12 6C10.9 6 10 5.1 10 4C10 2.9 10.9 2 12 2ZM21 9V7L15 1V3H9V1L3 7V9H5V20A2 2 0 0 0 7 22H17A2 2 0 0 0 19 20V9H21M17 20H7V9H10V12H14V9H17V20Z"/>
                  </svg>
                  <span>View Profile</span>
                </router-link>
                
                <router-link to="/teacher/settings" class="dropdown-item">
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M12,15.5A3.5,3.5 0 0,1 8.5,12A3.5,3.5 0 0,1 12,8.5A3.5,3.5 0 0,1 15.5,12A3.5,3.5 0 0,1 12,15.5M19.43,12.97C19.47,12.65 19.5,12.33 19.5,12C19.5,11.67 19.47,11.34 19.43,11L21.54,9.37C21.73,9.22 21.78,8.95 21.66,8.73L19.66,5.27C19.54,5.05 19.27,4.96 19.05,5.05L16.56,6.05C16.04,5.66 15.5,5.32 14.87,5.07L14.5,2.42C14.46,2.18 14.25,2 14,2H10C9.75,2 9.54,2.18 9.5,2.42L9.13,5.07C8.5,5.32 7.96,5.66 7.44,6.05L4.95,5.05C4.73,4.96 4.46,5.05 4.34,5.27L2.34,8.73C2.22,8.95 2.27,9.22 2.46,9.37L4.57,11C4.53,11.34 4.5,11.67 4.5,12C4.5,12.33 4.53,12.65 4.57,12.97L2.46,14.63C2.27,14.78 2.22,15.05 2.34,15.27L4.34,18.73C4.46,18.95 4.73,19.03 4.95,18.95L7.44,17.94C7.96,18.34 8.5,18.68 9.13,18.93L9.5,21.58C9.54,21.82 9.75,22 10,22H14C14.25,22 14.46,21.82 14.5,21.58L14.87,18.93C15.5,18.68 16.04,18.34 16.56,17.94L19.05,18.95C19.27,19.03 19.54,18.95 19.66,18.73L21.66,15.27C21.78,15.05 21.73,14.78 21.54,14.63L19.43,12.97Z"/>
                  </svg>
                  <span>Settings</span>
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
      
      <!-- Welcome Header -->
      <div class="welcome-header">
        <div class="welcome-content">
          <h1 class="welcome-title">
            <span v-if="!isLoadingName">Welcome back, {{ fullName }}!</span>
            <span v-else>Welcome back, Loading...</span>
          </h1>
          <p class="welcome-subtitle">Here's what's happening with your classes today</p>
        </div>
        <div class="quick-actions">
          <router-link to="/teacher/subjects" class="quick-action-btn primary">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor">
              <path d="M14,2H6A2,2 0 0,0 4,4V20A2,2 0 0,0 6,22H18A2,2 0 0,0 20,20V8L14,2M18,20H6V4H13V9H18V20Z" />
            </svg>
            <span>Create Quiz</span>
          </router-link>
          <router-link to="/teacher/upload-assessment" class="quick-action-btn secondary">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor">
              <path d="M9,16V10H5L12,3L19,10H15V16H9M5,20V18H19V20H5Z" />
            </svg>
            <span>Upload File</span>
          </router-link>
        </div>
      </div>

      <!-- Stats Dashboard -->
      <div class="stats-section">
        <div class="stats-grid">
          <div class="stat-card">
            <div class="stat-icon subjects">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path>
                <circle cx="9" cy="7" r="4"></circle>
                <path d="M23 21v-2a4 4 0 0 0-3-3.87"></path>
                <path d="M16 3.13a4 4 0 0 1 0 7.75"></path>
              </svg>
            </div>
            <div class="stat-info">
              <div class="stat-number">{{ totalClasses }}</div>
              <div class="stat-label">Active Subjects</div>
            </div>
          </div>

          <div class="stat-card">
            <div class="stat-icon students">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                <path d="M16 17v2H2v-2s0-4 7-4 7 4 7 4m-3.5-9.5A3.5 3.5 0 1 0 9 11a3.5 3.5 0 0 0 3.5-3.5m3.44 5.5A5.32 5.32 0 0 1 18 17v2h4v-2s0-3.63-6.06-4M15 4a3.39 3.39 0 0 0-1.93.59 5 5 0 0 1 0 5.82A3.39 3.39 0 0 0 15 11a3.5 3.5 0 0 0 0-7z"/>
              </svg>
            </div>
            <div class="stat-info">
              <div class="stat-number">{{ totalStudents }}</div>
              <div class="stat-label">Total Students</div>
            </div>
          </div>

          <div class="stat-card">
            <div class="stat-icon graded">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                <path d="M22 11.08V12a10 10 0 1 1-5.93-8.66"></path>
                <path d="M22 4L12 14.01l-3-3"></path>
              </svg>
            </div>
            <div class="stat-info">
              <div class="stat-number">{{ gradedToday }}</div>
              <div class="stat-label">Graded Today</div>
            </div>
          </div>

          <div class="stat-card">
            <div class="stat-icon pending">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                <circle cx="12" cy="12" r="10"></circle>
                <polyline points="12,6 12,12 16,14"></polyline>
              </svg>
            </div>
            <div class="stat-info">
              <div class="stat-number">{{ pendingReviews }}</div>
              <div class="stat-label">Pending Reviews</div>
            </div>
          </div>
        </div>
      </div>

      <!-- Content Grid -->
      <div class="content-section">
        <div class="content-grid">
          <!-- Assessments to Grade -->
          <div class="content-card large">
            <div class="card-header">
              <div class="card-title-section">
                <h3>Assessments to Grade</h3>
                <p class="card-description">Review pending student submissions</p>
              </div>
              <div class="card-actions">
                <button class="refresh-btn">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M17.65,6.35C16.2,4.9 14.21,4 12,4A8,8 0 0,0 4,12A8,8 0 0,0 12,20C15.73,20 18.84,17.45 19.73,14H17.65C16.83,16.33 14.61,18 12,18A6,6 0 0,1 6,12A6,6 0 0,1 12,6C13.66,6 15.14,6.69 16.22,7.78L13,11H20V4L17.65,6.35Z" />
                  </svg>
                </button>
              </div>
            </div>
            <div class="assessment-grid">
              <div v-if="assessmentsToGrade.length === 0" class="empty-state">
                <svg width="48" height="48" viewBox="0 0 24 24" fill="currentColor" opacity="0.3">
                  <path d="M19 3H14.82C14.4 1.84 13.3 1 12 1S9.6 1.84 9.18 3H5C3.9 3 3 3.9 3 5V19C3 20.1 3.9 21 5 21H19C20.1 21 21 20.1 21 19V5C21 3.9 20.1 3 19 3Z"/>
                </svg>
                <h4>All caught up!</h4>
                <p>No assessments need grading right now</p>
              </div>
              <div v-for="assessment in assessmentsToGrade" :key="assessment.id" class="assessment-card">
                <div class="assessment-header">
                  <h4>{{ assessment.title }}</h4>
                  <span class="assessment-badge">{{ assessment.studentsSubmitted }} submissions</span>
                </div>
                <p class="assessment-class">{{ assessment.className }}</p>
                <div class="assessment-footer">
                  <div class="progress-info">
                    <div class="progress-bar">
                      <div class="progress-fill" :style="{ width: (assessment.studentsSubmitted / assessment.totalStudents * 100) + '%' }"></div>
                    </div>
                    <span class="progress-text">{{ assessment.studentsSubmitted }} / {{ assessment.totalStudents }} submitted</span>
                  </div>
                  <button @click="gradeAssessment(assessment)" class="grade-assessment-btn">
                    Grade
                  </button>
                </div>
              </div>
            </div>
          </div>

          <!-- Quick Actions -->
          <div class="content-card small">
            <div class="card-header">
              <div class="card-title-section">
                <h3>Quick Actions</h3>
                <p class="card-description">Common tasks</p>
              </div>
            </div>
            
            <!-- Analytics & Messages - Compact Buttons -->
            <div class="compact-actions">
              <button @click="toggleAnalytics" class="compact-btn analytics">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M22,21H2V3H4V19H6V10H10V19H12V6H16V19H18V14H22V21Z"/>
                </svg>
                <span>Analytics</span>
              </button>
              <button @click="toggleMessages" class="compact-btn messages">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M20,2H4A2,2 0 0,0 2,4V22L6,18H20A2,2 0 0,0 22,16V4A2,2 0 0,0 20,2M6,9H18V11H6M6,5H18V7H6M6,13H15V15H6"/>
                </svg>
                <span>Messages</span>
              </button>
            </div>
            <div class="action-grid">
              <router-link to="/teacher/subjects" class="action-item">
                <div class="action-icon">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M12,3L1,9L12,15L21,10.09V17H23V9M5,13.18V17.18L12,21L19,17.18V13.18L12,17L5,13.18Z"/>
                  </svg>
                </div>
                <div class="action-content">
                  <h4>Manage Classes</h4>
                  <p>View and edit your subjects</p>
                </div>
              </router-link>
              
              <router-link to="/teacher/gradebook" class="action-item">
                <div class="action-icon">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M19,3H14.82C14.4,1.84 13.3,1 12,1C10.7,1 9.6,1.84 9.18,3H5A2,2 0 0,0 3,5V19A2,2 0 0,0 5,21H19A2,2 0 0,0 21,19V5A2,2 0 0,0 19,3M12,3A1,1 0 0,1 13,4A1,1 0 0,1 12,5A1,1 0 0,1 11,4A1,1 0 0,1 12,3Z" />
                  </svg>
                </div>
                <div class="action-content">
                  <h4>Gradebook</h4>
                  <p>Review student grades</p>
                </div>
              </router-link>
              
              <router-link to="/teacher/upload-assessment" class="action-item">
                <div class="action-icon">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M9,16V10H5L12,3L19,10H15V16H9M5,20V18H19V20H5Z" />
                  </svg>
                </div>
                <div class="action-content">
                  <h4>Upload Assessment</h4>
                  <p>Add new materials</p>
                </div>
              </router-link>
              
              <router-link to="/teacher/subjects" class="action-item">
                <div class="action-icon">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M14,2H6A2,2 0 0,0 4,4V20A2,2 0 0,0 6,22H18A2,2 0 0,0 20,20V8L14,2M18,20H6V4H13V9H18V20Z" />
                  </svg>
                </div>
                <div class="action-content">
                  <h4>Create Quiz</h4>
                  <p>Build new assessments</p>
                </div>
              </router-link>
            </div>
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
import { ref, onMounted, computed } from 'vue'
import { useRouter } from 'vue-router'
import { supabase } from '../../supabase.js'

// Initialize router
const router = useRouter()

// Local state
const notifications = ref([])
const showNotifDropdown = ref(false)
const showProfileDropdown = ref(false)
const showAnalytics = ref(false)
const showMessages = ref(false)
const showAnalyticsLabel = ref(false)
const showMessagesLabel = ref(false)
const showScrollTop = ref(false)
const fullName = ref('Teacher')
const isLoadingName = ref(false)
const totalClasses = ref(0)
const totalStudents = ref(0)
const gradedToday = ref(0)
const pendingReviews = ref(0)
const assessmentsToGrade = ref([])
const teacherId = ref(null)
const userId = ref(null)

// Methods
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

const toggleAnalytics = () => {
  // Navigate to the actual Analytics page
  window.location.href = '/teacher/analytics'
  // Alternative router navigation (if you have access to router):
  // this.$router.push('/teacher/analytics')
}

const toggleMessages = () => {
  // Navigate to the actual Messages page
  window.location.href = '/teacher/messages'
  // Alternative router navigation (if you have access to router):
  // this.$router.push('/teacher/messages')
}

const scrollToTop = () => {
  window.scrollTo({ top: 0, behavior: 'smooth' })
}

// Handle scroll to show/hide scroll-to-top button
const handleScroll = () => {
  showScrollTop.value = window.pageYOffset > 300
}

// Logout confirmation modal
const showLogoutModal = ref(false)

const openLogoutModal = () => {
  showLogoutModal.value = true
}

const closeLogoutModal = () => {
  showLogoutModal.value = false
}

const isLoggingOut = ref(false)

const confirmLogout = () => {
  isLoggingOut.value = true
  
  console.log('🚪 Logging out...')
  
  // Clear storage immediately
  localStorage.clear()
  sessionStorage.clear()
  
  // Sign out from Supabase (don't wait for response)
  supabase.auth.signOut({ scope: 'local' })
  
  console.log('✅ Logout successful')
  
  // Force immediate redirect - most reliable method
  window.location.replace('/login')
}

const logout = () => {
  openLogoutModal()
}

const gradeAssessment = (assessment) => {
  console.log('Grading assessment:', assessment)
  // TODO: Implement grade assessment functionality
}

// Load teacher profile
const loadTeacherProfile = async () => {
  try {
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
    
  } catch (error) {
    console.error('❌ Error loading profile:', error)
    return false
  }
}

// Load dashboard stats
const loadDashboardStats = async () => {
  if (!teacherId.value) {
    console.warn('⚠️ No teacher ID, cannot load stats')
    return
  }
  
  try {
    console.log('📊 Loading dashboard stats for teacher:', teacherId.value)
    
    // Get total classes (subjects)
    const { data: subjects, error: subjectsError } = await supabase
      .from('subjects')
      .select('id')
      .eq('teacher_id', teacherId.value)
      .eq('is_active', true)
    
    if (!subjectsError && subjects) {
      totalClasses.value = subjects.length
      console.log('📚 Total subjects:', subjects.length)
    }
    
    // Get total students across all sections taught by this teacher
    // First, get all sections for this teacher's subjects
    const { data: teacherSections, error: sectionsError } = await supabase
      .from('sections')
      .select(`
        id,
        subject_id,
        subjects!inner(teacher_id)
      `)
      .eq('subjects.teacher_id', teacherId.value)
    
    if (!sectionsError && teacherSections && teacherSections.length > 0) {
      console.log('📋 Found sections:', teacherSections.length)
      
      // Get unique student count across all sections
      const sectionIds = teacherSections.map(s => s.id)
      
      const { data: enrollments, error: enrollError } = await supabase
        .from('enrollments')
        .select('student_id')
        .in('section_id', sectionIds)
        .eq('status', 'active')
      
      if (!enrollError && enrollments) {
        // Count unique students (in case a student is in multiple sections)
        const uniqueStudents = new Set(enrollments.map(e => e.student_id))
        totalStudents.value = uniqueStudents.size
        console.log('👥 Total unique students:', uniqueStudents.size)
        console.log('� Total enrollments:', enrollments.length)
      } else {
        console.error('❌ Enrollment error:', enrollError)
      }
    } else {
      console.log('⚠️ No sections found for teacher')
      if (sectionsError) console.error('❌ Sections error:', sectionsError)
    }
    
    // Get graded today
    const today = new Date()
    today.setHours(0, 0, 0, 0)
    const todayISO = today.toISOString()
    
    const { data: graded, error: gradedError } = await supabase
      .from('quiz_attempts')
      .select('id, quiz_id!inner(teacher_id)')
      .eq('quiz_id.teacher_id', teacherId.value)
      .eq('status', 'graded')
      .gte('graded_at', todayISO)
    
    if (!gradedError && graded) {
      gradedToday.value = graded.length
      console.log('✅ Graded today:', graded.length)
    }
    
    // Get pending assessments
    const { data: quizzes, error: quizzesError } = await supabase
      .from('quizzes')
      .select(`
        id,
        title,
        subject_id,
        section_id,
        subjects!inner(name),
        sections!inner(name)
      `)
      .eq('teacher_id', teacherId.value)
      .eq('status', 'published')
    
    if (!quizzesError && quizzes) {
      const assessmentsWithSubmissions = []
      
      for (const quiz of quizzes) {
        // Get submitted attempts
        const { data: attempts } = await supabase
          .from('quiz_attempts')
          .select('id, student_id')
          .eq('quiz_id', quiz.id)
          .eq('status', 'submitted')
        
        if (attempts && attempts.length > 0) {
          // Get total students in section
          const { data: enrollments } = await supabase
            .from('enrollments')
            .select('student_id')
            .eq('section_id', quiz.section_id)
            .eq('status', 'active')
          
          assessmentsWithSubmissions.push({
            id: quiz.id,
            title: quiz.title,
            className: `${quiz.subjects.name} - ${quiz.sections.name}`,
            studentsSubmitted: attempts.length,
            totalStudents: enrollments?.length || 0,
            sectionId: quiz.section_id,
            subjectId: quiz.subject_id
          })
        }
      }
      
      assessmentsToGrade.value = assessmentsWithSubmissions
      pendingReviews.value = assessmentsWithSubmissions.length
      
      console.log('📝 Assessments to grade:', assessmentsWithSubmissions.length)
    }
    
    console.log('✅ Dashboard stats loaded successfully')
    
  } catch (error) {
    console.error('❌ Error loading dashboard stats:', error)
  }
}

// Lifecycle
onMounted(async () => {
  console.log('🚀 Dashboard mounting...')
  
  const profileLoaded = await loadTeacherProfile()
  
  if (profileLoaded) {
    await loadDashboardStats()
    
    // Auto-refresh every 30 seconds
    const intervalId = setInterval(() => {
      loadDashboardStats()
    }, 30000)
    
    // Add scroll listener for scroll-to-top button
    window.addEventListener('scroll', handleScroll)
    
    // Cleanup on unmount
    return () => {
      clearInterval(intervalId)
      window.removeEventListener('scroll', handleScroll)
    }
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

.dashboard-container {
  min-height: 100vh;
  width: 100vw;
  background: #f8fafc;
  font-family: 'Inter', sans-serif;
  overflow-x: hidden;
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

/* Main Content - Better Spacing */
.main-content {
  margin-top: 64px;
  padding: 1.5rem;
  width: 100%;
  min-height: calc(100vh - 64px);
  position: relative;
  max-width: 1400px;
  margin-left: auto;
  margin-right: auto;
}

/* Scroll to Top Button - Green Theme */
.scroll-to-top {
  position: fixed;
  right: 2rem;
  bottom: 2rem;
  width: 50px;
  height: 50px;
  background: linear-gradient(135deg, #3D8D7A, #2d6a5a);
  border: none;
  border-radius: 50%;
  color: white;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 4px 16px rgba(61, 141, 122, 0.3);
  transition: all 0.3s ease;
  z-index: 1001;
}

.scroll-to-top:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(61, 141, 122, 0.4);
}

/* Compact Action Buttons - Bigger Size */
.compact-actions {
  display: flex;
  gap: 0.75rem;
  margin-bottom: 1rem;
  padding-bottom: 1rem;
  border-bottom: 1px solid #f1f5f9;
}

.compact-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  padding: 0.75rem 1.25rem;
  border: none;
  border-radius: 10px;
  font-size: 0.85rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
  text-decoration: none;
  flex: 1;
  min-height: 44px;
}

.compact-btn.analytics {
  background: linear-gradient(135deg, #3D8D7A, #2d6a5a);
  color: white;
}

.compact-btn.analytics:hover {
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(61, 141, 122, 0.3);
}

.compact-btn.messages {
  background: linear-gradient(135deg, #06b6d4, #0891b2);
  color: white;
}

.compact-btn.messages:hover {
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(6, 182, 212, 0.3);
}

/* Floating Action Buttons - Removed (now using compact buttons) */



/* Modal Overlay */
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

/* Analytics Modal */
.analytics-modal {
  background: white;
  border-radius: 20px;
  width: 90%;
  max-width: 1200px;
  max-height: 80vh;
  overflow: hidden;
  animation: slideIn 0.3s ease;
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.2);
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.5rem 2rem;
  border-bottom: 1px solid #e2e8f0;
  background: linear-gradient(135deg, #3D8D7A, #2d6a5a);
  color: white;
}

.modal-header h2 {
  font-size: 1.5rem;
  font-weight: 700;
  margin: 0;
}

.close-btn {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  border: none;
  background: rgba(255, 255, 255, 0.2);
  color: white;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.2s;
}

.close-btn:hover {
  background: rgba(255, 255, 255, 0.3);
  transform: scale(1.1);
}

.modal-content {
  padding: 2rem;
  overflow-y: auto;
  max-height: calc(80vh - 80px);
}

.analytics-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
  gap: 1.5rem;
}

.analytics-card {
  background: #f8fafc;
  border-radius: 16px;
  padding: 1.5rem;
  border: 1px solid #e2e8f0;
  transition: all 0.3s ease;
}

.analytics-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
}

.analytics-card h3 {
  font-size: 1.2rem;
  font-weight: 600;
  color: #1e293b;
  margin-bottom: 1rem;
}

.chart-placeholder {
  margin: 1rem 0;
  text-align: center;
}

.progress-rings {
  display: flex;
  justify-content: space-around;
  gap: 1rem;
}

.ring-item {
  text-align: center;
}

.progress-ring {
  position: relative;
  display: inline-block;
}

.ring-text {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-weight: 700;
  color: #1e293b;
}

.activity-list {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.activity-item {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 0.75rem;
  background: white;
  border-radius: 12px;
  border: 1px solid #e2e8f0;
}

.activity-icon {
  font-size: 1.5rem;
}

.activity-text p {
  font-size: 0.9rem;
  color: #1e293b;
  margin: 0;
}

.activity-text span {
  font-size: 0.8rem;
  color: #64748b;
}

/* Messages Modal */
.messages-modal {
  background: white;
  border-radius: 20px;
  width: 90%;
  max-width: 1000px;
  height: 80vh;
  overflow: hidden;
  animation: slideIn 0.3s ease;
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.2);
}

.messages-modal .modal-header {
  background: linear-gradient(135deg, #06b6d4, #0891b2);
}

.messages-content {
  display: flex;
  height: calc(100% - 80px);
  padding: 0;
}

.messages-sidebar {
  width: 320px;
  border-right: 1px solid #e2e8f0;
  background: #f8fafc;
  display: flex;
  flex-direction: column;
}

.message-search {
  padding: 1rem;
  border-bottom: 1px solid #e2e8f0;
}

.search-input {
  width: 100%;
  padding: 0.75rem 1rem;
  border: 1px solid #e2e8f0;
  border-radius: 12px;
  font-size: 0.9rem;
  outline: none;
  transition: border-color 0.2s;
}

.search-input:focus {
  border-color: #06b6d4;
}

.message-list {
  flex: 1;
  overflow-y: auto;
  padding: 0.5rem;
}

.message-item {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 1rem;
  border-radius: 12px;
  cursor: pointer;
  transition: background 0.2s;
  position: relative;
}

.message-item:hover {
  background: rgba(6, 182, 212, 0.1);
}

.message-item.active {
  background: rgba(6, 182, 212, 0.15);
}

.message-avatar {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.2rem;
  background: #e2e8f0;
}

.message-info {
  flex: 1;
}

.message-info h4 {
  font-size: 0.9rem;
  font-weight: 600;
  color: #1e293b;
  margin: 0 0 0.25rem 0;
}

.message-info p {
  font-size: 0.8rem;
  color: #64748b;
  margin: 0 0 0.25rem 0;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.message-info span {
  font-size: 0.75rem;
  color: #94a3b8;
}

.message-unread {
  width: 20px;
  height: 20px;
  background: #06b6d4;
  color: white;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.75rem;
  font-weight: 600;
}

.message-chat {
  flex: 1;
  display: flex;
  flex-direction: column;
  background: white;
}

.chat-header {
  padding: 1rem 1.5rem;
  border-bottom: 1px solid #e2e8f0;
  background: #f8fafc;
}

.chat-user {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.chat-avatar {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.2rem;
  background: #e2e8f0;
}

.chat-info h4 {
  font-size: 1rem;
  font-weight: 600;
  color: #1e293b;
  margin: 0;
}

.chat-info span {
  font-size: 0.8rem;
  color: #64748b;
}

.chat-messages {
  flex: 1;
  padding: 1rem;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.chat-message {
  display: flex;
}

.chat-message.received {
  justify-content: flex-start;
}

.chat-message.sent {
  justify-content: flex-end;
}

.message-bubble {
  max-width: 70%;
  padding: 0.75rem 1rem;
  border-radius: 18px;
  position: relative;
}

.chat-message.received .message-bubble {
  background: #f1f5f9;
  color: #1e293b;
}

.chat-message.sent .message-bubble {
  background: #06b6d4;
  color: white;
}

.message-bubble p {
  margin: 0 0 0.5rem 0;
  font-size: 0.9rem;
  line-height: 1.4;
}

.message-time {
  font-size: 0.75rem;
  opacity: 0.7;
}

.chat-input {
  display: flex;
  gap: 0.75rem;
  padding: 1rem 1.5rem;
  border-top: 1px solid #e2e8f0;
  background: #f8fafc;
}

.message-input {
  flex: 1;
  padding: 0.75rem 1rem;
  border: 1px solid #e2e8f0;
  border-radius: 20px;
  font-size: 0.9rem;
  outline: none;
  transition: border-color 0.2s;
}

.message-input:focus {
  border-color: #06b6d4;
}

.send-btn {
  width: 44px;
  height: 44px;
  border-radius: 50%;
  border: none;
  background: #06b6d4;
  color: white;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.2s;
}

.send-btn:hover {
  background: #0891b2;
  transform: scale(1.05);
}

/* Animations */
@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

@keyframes slideIn {
  from {
    opacity: 0;
    transform: translateY(-20px) scale(0.95);
  }
  to {
    opacity: 1;
    transform: translateY(0) scale(1);
  }
}

/* Welcome Header - Better Arrangement */
.welcome-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1.5rem;
  background: white;
  padding: 1.5rem 2rem;
  border-radius: 16px;
  border: 1px solid #e2e8f0;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
}

.welcome-content h1 {
  font-size: 1.75rem;
  font-weight: 700;
  color: #1e293b;
  margin-bottom: 0.25rem;
}

.welcome-subtitle {
  font-size: 0.95rem;
  color: #64748b;
}

.quick-actions {
  display: flex;
  gap: 1rem;
}

.quick-action-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1.25rem;
  border-radius: 12px;
  text-decoration: none;
  font-size: 0.9rem;
  font-weight: 600;
  transition: all 0.2s ease;
  border: 2px solid transparent;
}

.quick-action-btn.primary {
  background: #3D8D7A;
  color: white;
}

.quick-action-btn.primary:hover {
  background: #2d6a5a;
  transform: translateY(-1px);
}

.quick-action-btn.secondary {
  background: #f1f5f9;
  color: #3D8D7A;
  border-color: #e2e8f0;
}

.quick-action-btn.secondary:hover {
  background: #e2e8f0;
  border-color: #3D8D7A;
}

/* Stats Section */
.stats-section {
  margin-bottom: 1.5rem;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1.25rem;
}

.stat-card {
  background: white;
  border-radius: 16px;
  padding: 1.5rem;
  display: flex;
  align-items: center;
  gap: 1rem;
  border: 1px solid #e2e8f0;
  transition: all 0.2s ease;
}

.stat-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
}

.stat-icon {
  width: 52px;
  height: 52px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  flex-shrink: 0;
}

.stat-icon.subjects { background: linear-gradient(135deg, #3D8D7A, #2d6a5a); }
.stat-icon.students { background: linear-gradient(135deg, #06b6d4, #0891b2); }
.stat-icon.graded { background: linear-gradient(135deg, #10b981, #059669); }
.stat-icon.pending { background: linear-gradient(135deg, #f59e0b, #d97706); }

.stat-info {
  flex: 1;
}

.stat-number {
  font-size: 2rem;
  font-weight: 800;
  color: #1e293b;
  line-height: 1;
  margin-bottom: 0.25rem;
}

.stat-label {
  font-size: 0.85rem;
  color: #64748b;
  font-weight: 500;
}

/* Content Section */
.content-section {
  margin-bottom: 2rem;
}

.content-grid {
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: 2rem;
}

.content-card {
  background: white;
  border-radius: 16px;
  padding: 1.5rem;
  border: 1px solid #e2e8f0;
  display: flex;
  flex-direction: column;
}

.content-card.large {
  min-height: 500px;
}

.content-card.small {
  min-height: 400px;
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 1.5rem;
  padding-bottom: 1rem;
  border-bottom: 1px solid #f1f5f9;
}

.card-title-section h3 {
  font-size: 1.25rem;
  font-weight: 700;
  color: #1e293b;
  margin-bottom: 0.25rem;
}

.card-description {
  font-size: 0.85rem;
  color: #64748b;
}

.card-actions {
  display: flex;
  gap: 0.5rem;
}

.refresh-btn {
  width: 36px;
  height: 36px;
  background: #f1f5f9;
  border: none;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.2s;
  color: #64748b;
}

.refresh-btn:hover {
  background: #e2e8f0;
  color: #3D8D7A;
}

/* Assessment Grid */
.assessment-grid {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  flex: 1;
  overflow-y: auto;
}

.empty-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  flex: 1;
  text-align: center;
  color: #94a3b8;
  gap: 1rem;
}

.empty-state h4 {
  font-size: 1.1rem;
  font-weight: 600;
  color: #64748b;
}

.empty-state p {
  font-size: 0.9rem;
}

.assessment-card {
  background: #f8fafc;
  border-radius: 12px;
  padding: 1.25rem;
  border: 1px solid #e2e8f0;
  transition: all 0.2s ease;
}

.assessment-card:hover {
  background: #f1f5f9;
  border-color: #3D8D7A;
}

.assessment-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 0.5rem;
}

.assessment-header h4 {
  font-size: 1rem;
  font-weight: 600;
  color: #1e293b;
}

.assessment-badge {
  background: #3D8D7A;
  color: white;
  padding: 0.25rem 0.75rem;
  border-radius: 12px;
  font-size: 0.75rem;
  font-weight: 500;
}

.assessment-class {
  font-size: 0.85rem;
  color: #64748b;
  margin-bottom: 1rem;
}

.assessment-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 1rem;
}

.progress-info {
  flex: 1;
}

.progress-bar {
  width: 100%;
  height: 6px;
  background: #e2e8f0;
  border-radius: 3px;
  overflow: hidden;
  margin-bottom: 0.5rem;
}

.progress-fill {
  height: 100%;
  background: #3D8D7A;
  border-radius: 3px;
  transition: width 0.3s ease;
}

.progress-text {
  font-size: 0.75rem;
  color: #64748b;
  font-weight: 500;
}

.grade-assessment-btn {
  background: #3D8D7A;
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 8px;
  font-size: 0.85rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s;
  flex-shrink: 0;
}

.grade-assessment-btn:hover {
  background: #2d6a5a;
  transform: translateY(-1px);
}

/* Action Grid */
.action-grid {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  flex: 1;
}

.action-item {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1rem;
  background: #f8fafc;
  border-radius: 12px;
  border: 1px solid #e2e8f0;
  text-decoration: none;
  transition: all 0.2s ease;
}

.action-item:hover {
  background: #f1f5f9;
  border-color: #3D8D7A;
  transform: translateY(-1px);
}

.action-icon {
  width: 40px;
  height: 40px;
  background: #3D8D7A;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  flex-shrink: 0;
}

.action-content {
  flex: 1;
}

.action-content h4 {
  font-size: 0.9rem;
  font-weight: 600;
  color: #1e293b;
  margin-bottom: 0.25rem;
}

.action-content p {
  font-size: 0.8rem;
  color: #64748b;
}

/* Dark mode support */
.dark .dashboard-container {
  background: #0f172a;
}

.dark .top-navbar {
  background: #1e293b;
  border-bottom-color: #334155;
}

.dark .brand-name,
.dark .nav-item.active {
  color: #A3D1C6;
}

.dark .nav-item {
  color: #94a3b8;
}

.dark .nav-item:hover {
  background: #334155;
  color: #A3D1C6;
}

.dark .welcome-header,
.dark .stat-card,
.dark .content-card {
  background: #1e293b;
  border-color: #334155;
}

.dark .welcome-content h1,
.dark .stat-number,
.dark .card-title-section h3,
.dark .assessment-header h4,
.dark .action-content h4 {
  color: #f1f5f9;
}

.dark .welcome-subtitle,
.dark .stat-label,
.dark .card-description,
.dark .assessment-class,
.dark .progress-text,
.dark .action-content p {
  color: #94a3b8;
}

/* Responsive Design */
@media (max-width: 1200px) {
  .main-content {
    padding: 1.5rem;
  }
  
  .stats-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 1rem;
  }
}

@media (max-width: 1024px) {
  .content-grid {
    grid-template-columns: 1fr;
    gap: 1.5rem;
  }
  
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
    padding: 1rem 0.5rem;
  }
  
  .welcome-header {
    flex-direction: column;
    align-items: stretch;
    gap: 1rem;
    margin: 0 0.5rem 1.5rem;
    padding: 1rem;
  }
  
  .quick-actions {
    justify-content: center;
    flex-wrap: wrap;
  }
  
  .stats-grid {
    grid-template-columns: 1fr;
    gap: 1rem;
    margin: 0 0.5rem;
  }
  
  .content-section {
    margin: 0 0.5rem 1.5rem;
  }
  
  .navbar-content {
    padding: 0 0.5rem;
  }
  
  .brand-name {
    display: none;
  }
  
  /* Mobile scroll-to-top button positioning */
  .scroll-to-top {
    right: 1rem;
    bottom: 1rem;
    width: 45px;
    height: 45px;
  }
  
  /* Mobile compact buttons - keep side by side but smaller */
  .compact-actions {
    gap: 0.5rem;
  }
  
  .compact-btn {
    font-size: 0.75rem;
    padding: 0.6rem 0.8rem;
    min-height: 40px;
  }
}

@media (max-width: 640px) {
  .dashboard-container {
    padding: 0;
  }
  
  .main-content {
    padding: 0.75rem 0.25rem;
  }
  
  .welcome-header {
    margin: 0 0.25rem 1rem;
    padding: 1rem 0.75rem;
  }
  
  .welcome-content h1 {
    font-size: 1.5rem;
  }
  
  .stats-grid {
    margin: 0 0.25rem;
    gap: 0.75rem;
  }
  
  .stat-card {
    padding: 1rem;
  }
  
  .stat-number {
    font-size: 1.75rem;
  }
  
  .content-section {
    margin: 0 0.25rem 0.75rem;
  }
  
  .content-card {
    padding: 1rem;
  }
  
  .assessment-footer {
    flex-direction: column;
    align-items: stretch;
    gap: 0.75rem;
  }
  
  .quick-action-btn {
    flex: 1;
    justify-content: center;
    padding: 0.5rem 0.75rem;
    font-size: 0.85rem;
  }
  
  .user-name {
    display: none;
  }
}

@media (max-width: 480px) {
  .main-content {
    padding: 0.5rem 0.125rem;
  }
  
  .welcome-header {
    margin: 0 0.125rem 0.75rem;
    padding: 0.75rem 0.5rem;
  }
  
  .welcome-content h1 {
    font-size: 1.25rem;
  }
  
  .welcome-subtitle {
    font-size: 0.85rem;
  }
  
  .stats-grid {
    margin: 0 0.125rem;
    gap: 0.5rem;
  }
  
  .stat-card {
    padding: 0.75rem;
    gap: 0.75rem;
  }
  
  .stat-icon {
    width: 44px;
    height: 44px;
  }
  
  .stat-number {
    font-size: 1.5rem;
  }
  
  .stat-label {
    font-size: 0.8rem;
  }
  
  .content-section {
    margin: 0 0.125rem 0.75rem;
  }
  
  .content-card {
    padding: 0.75rem;
  }
  
  .card-title-section h3 {
       font-size: 1.1rem;
  }
  
  .quick-action-btn {
    padding: 0.4rem 0.5rem;
    font-size: 0.8rem;
    gap: 0.4rem;
  }
  
  .quick-action-btn svg {
    width: 16px;
    height: 16px;
  }
  
  /* Smaller floating buttons for very small screens */
  .floating-actions {
    right: 0.5rem;
    bottom: 0.5rem;
    gap: 0.4rem;
  }
  
  .floating-btn {
    width: 40px;
    height: 40px;
  }
  
  .floating-btn svg {
    width: 16px;
    height: 16px;
  }
}

@media (max-width: 390px) {
  .main-content {
    padding: 0.25rem;
  }
  
  .welcome-header {
    margin: 0.125rem 0.125rem 0.5rem;
    padding: 0.5rem;
    border-radius: 12px;
  }
  
  .welcome-content h1 {
    font-size: 1.1rem;
    line-height: 1.3;
  }
  
  .welcome-subtitle {
    font-size: 0.8rem;
  }
  
  .quick-actions {
    gap: 0.5rem;
  }
  
  .quick-action-btn {
    padding: 0.35rem 0.4rem;
    font-size: 0.75rem;
    border-radius: 8px;
  }
  
  .quick-action-btn svg {
    width: 14px;
    height: 14px;
  }
  
  .stats-grid {
    margin: 0.125rem;
    gap: 0.5rem;
  }
  
  .stat-card {
    padding: 0.5rem;
    gap: 0.5rem;
    border-radius: 12px;
  }
  
  .stat-icon {
    width: 36px;
    height: 36px;
    border-radius: 8px;
  }
  
  .stat-icon svg {
    width: 18px;
    height: 18px;
  }
  
  .stat-number {
    font-size: 1.25rem;
  }
  
  .stat-label {
    font-size: 0.75rem;
  }
  
  .content-section {
    margin: 0.125rem 0.125rem 0.5rem;
  }
  
  .content-card {
    padding: 0.5rem;
    border-radius: 12px;
  }
  
  .card-header {
    margin-bottom: 1rem;
    padding-bottom: 0.75rem;
  }
  
  .card-title-section h3 {
    font-size: 1rem;
  }
  
  .card-description {
    font-size: 0.8rem;
  }
  
  .assessment-card {
    padding: 0.75rem;
    border-radius: 8px;
  }
  
  .assessment-header h4 {
    font-size: 0.9rem;
  }
  
  .assessment-badge {
    font-size: 0.7rem;
    padding: 0.2rem 0.5rem;
  }
  
  .action-item {
    padding: 0.75rem;
    border-radius: 8px;
  }
  
  .action-icon {
    width: 32px;
    height: 32px;
    border-radius: 6px;
  }
  
  .action-icon svg {
    width: 16px;
    height: 16px;
  }
  
  .action-content h4 {
    font-size: 0.85rem;
  }
  
  .action-content p {
    font-size: 0.75rem;
  }
  
  /* Navbar optimizations */
  .navbar-content {
    padding: 0 0.5rem;
  }
  
  .logo-img {
    width: 28px;
    height: 28px;
  }
  
  .brand-name {
    font-size: 1.1rem;
  }
  
  .user-avatar {
    width: 28px;
    height: 28px;
  }
  
  .nav-icon-btn {
    width: 36px;
    height: 36px;
  }
}

/* Landscape phone optimization */
@media (max-width: 896px) and (orientation: landscape) {
  .main-content {
    padding: 0.5rem;
  }
  
  .welcome-header {
    padding: 0.75rem 1rem;
    margin-bottom: 1rem;
  }
  
  .welcome-content h1 {
    font-size: 1.4rem;
  }
  
  .stats-grid {
    grid-template-columns: repeat(4, 1fr);
    gap: 0.75rem;
  }
}

/* Ultra-wide screen optimization */
@media (min-width: 1600px) {
  .navbar-content {
    max-width: 1600px;
  }
  
  .main-content {
    max-width: 1600px;
    margin: 64px auto 0;
    padding: 2.5rem;
  }
  
  .stats-grid {
    grid-template-columns: repeat(4, 1fr);
    gap: 2rem;
  }
  
  .content-grid {
    gap: 2.5rem;
  }
}

/* Print styles */
@media print {
  .top-navbar {
    display: none !important;
  }
  
  .main-content {
    margin-top: 0;
    padding: 1rem;
  }
  
  .dashboard-container {
    background: white;
  }
  
  .stat-card,
  .content-card,
  .welcome-header {
    box-shadow: none;
    border: 1px solid #ccc;
  }
}

/* Logout Confirmation Modal */
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
  text-align: center;
}

.logout-header h3 {
  margin: 0;
  font-size: 1.25rem;
  font-weight: 600;
}

.modal-body {
  padding: 2rem;
  text-align: center;
  background: #f8fafc;
}

.logout-icon {
  margin-bottom: 1rem;
}

.logout-icon svg {
  color: #3D8D7A;
  animation: pulse 2s infinite;
}

@keyframes pulse {
  0%, 100% { transform: scale(1); opacity: 1; }
  50% { transform: scale(1.1); opacity: 0.8; }
}

.logout-message {
  font-size: 1.1rem;
  font-weight: 600;
  color: #1f2937;
  margin-bottom: 0.5rem;
}

.logout-submessage {
  font-size: 0.9rem;
  color: #6b7280;
  margin: 0;
}

.logout-footer {
  padding: 1.5rem;
  display: flex;
  gap: 1rem;
  justify-content: center;
  border-top: 1px solid #e2e8f0;
  background: #f8fafc;
}

.btn-cancel {
  padding: 0.75rem 1.5rem;
  border: 2px solid #e2e8f0;
  background: white;
  color: #6b7280;
  border-radius: 8px;
  font-size: 0.9rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.btn-cancel:hover {
  border-color: #3D8D7A;
  color: #3D8D7A;
}

.btn-logout {
  padding: 0.75rem 1.5rem;
  border: none;
  background: #dc3545;
  color: white;
  border-radius: 8px;
  font-size: 0.9rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.btn-logout:hover {
  background: #c82333;
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(220, 53, 69, 0.3);
}

.btn-logout:disabled {
  background: #ccc;
  cursor: not-allowed;
  transform: none;
  opacity: 0.6;
}

.logout-spinner {
  width: 12px;
  height: 12px;
  border: 2px solid rgba(255, 255, 255, 0.3);
  border-top: 2px solid white;
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
  display: inline-block;
  margin-right: 0.5rem;
}

.btn-logout .loading-text {
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-size: 0.9rem;
}

/* High contrast mode support */
@media (prefers-contrast: high) {
  .nav-item.active::after {
    background: #000;
  }
  
  .stat-icon {
    border: 1px solid #000;
  }
}
</style>