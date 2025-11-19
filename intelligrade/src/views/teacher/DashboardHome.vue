<template>
  <div class="dashboard-container">
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
                <button class="refresh-btn" @click="refreshAssessments">
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
const isLoggingOut = ref(false)
const isLoadingName = ref(false)
const totalClasses = ref(0)
const totalStudents = ref(0)
const gradedToday = ref(0)
const pendingReviews = ref(0)
const assessmentsToGrade = ref([])
const teacherId = ref(null)
const userId = ref(null)
const sidebarExpanded = ref(false)
const showLogoutModal = ref(false)

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

const toggleSidebar = () => {
  sidebarExpanded.value = !sidebarExpanded.value
}

// Handle scroll to show/hide scroll-to-top button
const handleScroll = () => {
  showScrollTop.value = window.pageYOffset > 300
}

// Logout confirmation modal
const openLogoutModal = () => {
  showLogoutModal.value = true
}

const closeLogoutModal = () => {
  showLogoutModal.value = false
}

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

const refreshAssessments = async () => {
  console.log('🔄 Refreshing assessments...')
  await loadDashboardStats()
  await loadNotifications()
}

const gradeAssessment = (assessment) => {
  console.log('Grading assessment:', assessment)
  // Navigate to gradebook with the specific assessment
  router.push({
    path: '/teacher/gradebook',
    query: {
      assessmentId: assessment.id,
      sectionId: assessment.sectionId,
      subjectId: assessment.subjectId
    }
  })
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
      .limit(10)
    
    if (!submissionsError && recentSubmissions) {
      const submissionNotifications = recentSubmissions.map(submission => ({
        id: `submission-${submission.id}`,
        title: 'New Quiz Submission',
        body: `${submission.students.full_name} submitted "${submission.quizzes.title}"`,
        date: new Date(submission.submitted_at).toLocaleString(),
        type: 'submission'
      }))
      
      notifications.value = [...submissionNotifications]
      console.log('✅ Loaded', submissionNotifications.length, 'submission notifications')
    }
    
    // Get recent messages from students using your existing schema
    try {
      const { data: recentMessages, error: messagesError } = await supabase
        .from('messages')
        .select(`
          id, 
          message_text, 
          sent_at,
          sender_id,
          students!sender_id(full_name)
        `)
        .eq('recipient_id', teacherId.value)
        .eq('message_type', 'direct')
        .not('message_reads.reader_id', 'eq', teacherId.value)
        .order('sent_at', { ascending: false })
        .limit(5)
      
      if (!messagesError && recentMessages) {
        const messageNotifications = recentMessages.map(message => ({
          id: `message-${message.id}`,
          title: 'New Message',
          body: `${message.students?.full_name || 'Student'}: ${message.message_text.substring(0, 50)}...`,
          date: new Date(message.sent_at).toLocaleString(),
          type: 'message'
        }))
        
        notifications.value = [...notifications.value, ...messageNotifications]
        console.log('✅ Loaded', messageNotifications.length, 'message notifications')
      }
    } catch (msgError) {
      console.log('ℹ️ Messages table not configured or no messages:', msgError.message)
      // Don't throw error if messages table doesn't have data yet
    }
    
  } catch (error) {
    console.error('❌ Error loading notifications:', error)
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
    await loadNotifications()
    
    // Auto-refresh every 30 seconds
    const statsIntervalId = setInterval(() => {
      loadDashboardStats()
    }, 30000)
    
    // Refresh notifications every 15 seconds
    const notifIntervalId = setInterval(() => {
      loadNotifications()
    }, 15000)
    
    // Add scroll listener for scroll-to-top button
    window.addEventListener('scroll', handleScroll)
    
    // Set up real-time subscription for quiz submissions
    const quizSubscription = supabase
      .channel('quiz_attempts_channel')
      .on('postgres_changes', {
        event: 'INSERT',
        schema: 'public',
        table: 'quiz_attempts',
        filter: `status=eq.submitted`
      }, (payload) => {
        console.log('🆕 New quiz submission:', payload)
        loadNotifications() // Refresh notifications when new submission
        loadDashboardStats() // Refresh stats
      })
      .subscribe()
    
    // Set up real-time subscription for messages using your schema
    const messageSubscription = supabase
      .channel('messages_channel')
      .on('postgres_changes', {
        event: 'INSERT',
        schema: 'public',
        table: 'messages',
        filter: `recipient_id=eq.${teacherId.value}`
      }, (payload) => {
        console.log('💬 New message received:', payload)
        loadNotifications() // Refresh notifications when new message
      })
      .subscribe()
    
    // Cleanup on unmount
    return () => {
      clearInterval(statsIntervalId)
      clearInterval(notifIntervalId)
      window.removeEventListener('scroll', handleScroll)
      quizSubscription.unsubscribe()
      messageSubscription.unsubscribe()
    }
  }
})

// Notification click handler
const handleNotificationClick = async (notification) => {
  console.log('📱 Clicked notification:', notification)
  
  if (notification.type === 'submission') {
    // Navigate to gradebook for quiz submissions
    router.push('/teacher/gradebook')
  } else if (notification.type === 'message') {
    // Navigate to messages for message notifications
    router.push('/teacher/messages')
    
    // Mark message as read using your schema
    try {
      const messageId = notification.id.replace('message-', '')
      
      // Use the mark_message_read function from your schema
      await supabase.rpc('mark_message_read', {
        p_message_id: messageId,
        p_reader_id: teacherId.value
      })
      
      // Refresh notifications to update count
      await loadNotifications()
    } catch (error) {
      console.error('❌ Error marking message as read:', error)
    }
  }
  
  // Close notification dropdown
  showNotifDropdown.value = false
}
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
/* Main Content - Better Spacing */
.main-content {
  margin-top: 64px;
  margin-left: 80px;
  padding: 1.5rem;
  width: calc(100% - 80px);
  min-height: calc(100vh - 64px);
  position: relative;
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

/* Compact Action Buttons */
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

/* Logout Modal */
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
</style>