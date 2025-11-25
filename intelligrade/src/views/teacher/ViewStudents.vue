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
      <!-- Page Header -->
      <div class="page-header">
        <div class="header-content">
          <div class="header-left">
            <div class="header-icon">
              <svg width="32" height="32" viewBox="0 0 24 24" fill="currentColor">
                <path d="M16,4C18.21,4 20,5.79 20,8C20,10.21 18.21,12 16,12C13.79,12 12,10.21 12,8C12,5.79 13.79,4 16,4M16,14C20.42,14 24,15.79 24,18V20H8V18C8,15.79 11.58,14 16,14M6,6C7.1,6 8,6.9 8,8C8,9.1 7.1,10 6,10C4.9,10 4,9.1 4,8C4,6.9 4.9,6 6,6M6,12C8.67,12 12,13.34 12,16V18H0V16C0,13.34 3.33,12 6,12Z" />
              </svg>
            </div>
            <div>
              <h1 class="header-title">Student Management</h1>
              <p class="header-subtitle">{{ subjectName }} (Grade {{ gradeLevel }}) - {{ sectionName }} ({{ sectionCode }})</p>
            </div>
          </div>
        </div>
      </div>

      <!-- Content Area -->

    <!-- Main Content -->
    <div class="main-content-wrapper">
      <button v-if="showScrollTop" @click="scrollToTop" class="scroll-to-top">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
          <path d="M7 14l5-5 5 5z"/>
        </svg>
      </button>
      <div v-if="isLoading" class="loading-state">
        <div class="loading-spinner"></div>
        <p>{{ loadingMessage }}</p>
      </div>
      <div v-else>
        <!-- Simple Summary Cards -->
        <div class="stats-grid">
          <div class="stat-card">
            <div class="stat-icon stat-classes">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                <path d="M16,4C18.21,4 20,5.79 20,8C20,10.21 18.21,12 16,12C13.79,12 12,10.21 12,8C12,5.79 13.79,4 16,4M16,14C20.42,14 24,15.79 24,18V20H8V18C8,15.79 11.58,14 16,14M6,6C7.1,6 8,6.9 8,8C8,9.1 7.1,10 6,10C4.9,10 4,9.1 4,8C4,6.9 4.9,6 6,6M6,12C8.67,12 12,13.34 12,16V18H0V16C0,13.34 3.33,12 6,12Z" />
              </svg>
            </div>
            <div>
              <div class="stat-number">{{ students.length }}</div>
              <div class="stat-label">Total Students</div>
            </div>
          </div>
          <div class="stat-card">
            <div class="stat-icon stat-graded">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                <path d="M9,20.42L2.79,14.21L5.62,11.38L9,14.77L18.88,4.88L21.71,7.71L9,20.42Z" />
              </svg>
            </div>
            <div>
              <div class="stat-number">{{ activeStudents }}</div>
              <div class="stat-label">Active Students</div>
            </div>
          </div>
        </div>

        <!-- Students List Card -->
        <div class="content-card">
          <div class="card-header">
            <h3>Enrolled Students</h3>
            <p class="card-desc">{{ students.length }} students enrolled in this section</p>
          </div>
          <div class="search-controls">
            <input type="text" v-model="searchQuery" placeholder="Search students by name or email..." class="search-input-simple" />
            <select v-model="filterStatus" class="filter-select-simple">
              <option value="all">All Students</option>
              <option value="active">Active</option>
              <option value="inactive">Inactive</option>
            </select>
          </div>
          <div v-if="filteredStudents.length > 0" class="students-list-simple">
            <div class="students-list-header">
              <span>Name</span>
              <span>Status</span>
              <span>Enrolled</span>
            </div>
            <div v-for="student in filteredStudents" :key="student.id" class="students-list-row">
              <span>{{ student.full_name }}</span>
              <span :class="['status-badge', student.status]">{{ student.status }}</span>
              <span>{{ formatDate(student.enrolled_at) }}</span>
            </div>
          </div>
          <div v-else-if="students.length === 0" class="empty-state">
            <div class="empty-icon">
              <svg width="48" height="48" fill="none" viewBox="0 0 24 24">
                <path fill="currentColor" d="M16,4C18.21,4 20,5.79 20,8C20,10.21 18.21,12 16,12C13.79,12 12,10.21 12,8C12,5.79 13.79,4 16,4M16,14C20.42,14 24,15.79 24,18V20H8V18C8,15.79 11.58,14 16,14M6,6C7.1,6 8,6.9 8,8C8,9.1 7.1,10 6,10C4.9,10 4,9.1 4,8C4,6.9 4.9,6 6,6M6,12C8.67,12 12,13.34 12,16V18H0V16C0,13.34 3.33,12 6,12Z" />
              </svg>
            </div>
            <div class="empty-title">No Students Enrolled</div>
            <div class="empty-desc">This section doesn't have any students enrolled yet.</div>
          </div>
          <div v-else class="no-results">
            <p>No students found matching "{{ searchQuery }}"</p>
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

<script setup lang="ts">
import { ref, onMounted, computed, onUnmounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { supabase } from '../../Supabase.js'
import { useDarkMode } from '../../composables/useDarkMode.js'
import { useTeacherAuth } from '../../composables/useTeacherAuth.js'

// Dark mode
const { isDarkMode } = useDarkMode()

// Teacher authentication
const { teacherProfile } = useTeacherAuth()
const fullName = computed(() => teacherProfile.value?.full_name || 'Teacher')

const router = useRouter()
const route = useRoute()

// Route data
const subjectId = ref(route.params.subjectId)
const sectionId = ref(route.params.sectionId)
const subjectName = ref(route.query.subjectName || '')
const sectionName = ref(route.query.sectionName || '')
const gradeLevel = ref(route.query.gradeLevel || '')
const sectionCode = ref(route.query.sectionCode || '')

// State
interface Student {
  id: string;
  full_name: string;
  email: string;
  enrolled_at: string;
  status: string;
  enrollment_id: string;
  grade_level: string;
  last_activity?: string;
  quiz_count?: number;
  average_grade?: number;
}
const students = ref<Student[]>([])
const searchQuery = ref('')
const filterStatus = ref('all')
const isLoading = ref(false)
const isExporting = ref(false)
const loadingMessage = ref('')
const showProfileDropdown = ref(false)
const showNotifDropdown = ref(false)
interface Notification {
  id: string;
  title: string;
  body: string;
  date: string;
}
const notifications = ref<Notification[]>([])

// Logout modal states
const showLogoutModal = ref(false)
const isLoggingOut = ref(false)

// Scroll to Top Button State
const showScrollTop = ref(false)
const handleScroll = () => {
  showScrollTop.value = window.scrollY > 200
}
const scrollToTop = () => {
  window.scrollTo({ top: 0, behavior: 'smooth' })
}

// Profile dropdown functions
const toggleProfileDropdown = () => {
  showProfileDropdown.value = !showProfileDropdown.value
  if (showProfileDropdown.value) {
    showNotifDropdown.value = false
  }
}

const toggleNotifDropdown = () => {
  showNotifDropdown.value = !showNotifDropdown.value
  if (showNotifDropdown.value) {
    showProfileDropdown.value = false
  }
}

const handleNotificationClick = (notification: Notification) => {
  console.log('Notification clicked:', notification)
  // Handle notification click logic here
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

// Computed
const filteredStudents = computed(() => {
  let filtered = students.value

  // Filter by search query
  if (searchQuery.value) {
    const query = searchQuery.value.toLowerCase()
    filtered = filtered.filter((student: Student) => 
      student.full_name.toLowerCase().includes(query) ||
      student.email.toLowerCase().includes(query)
    )
  }

  // Filter by status
  if (filterStatus.value !== 'all') {
    filtered = filtered.filter((student: Student) => student.status === filterStatus.value)
  }

  return filtered
})

const activeStudents = computed(() => {
  return students.value.filter((student: Student) => student.status === 'active').length
})

// Methods
const fetchStudents = async () => {
  isLoading.value = true
  loadingMessage.value = 'Loading students...'

  try {
    console.log('🔍 Fetching students for section:', sectionId.value)

    // Get enrollments for this section
    const { data: enrollmentsData, error: enrollError } = await supabase
      .from('enrollments')
      .select('*')
      .eq('section_id', sectionId.value)
      .eq('status', 'active')

    if (enrollError) {
      console.error('Error fetching enrollments:', enrollError)
      throw enrollError
    }

    console.log('✅ Enrollments found:', enrollmentsData)

    if (!enrollmentsData || enrollmentsData.length === 0) {
      students.value = []
      return
    }

    // Get student IDs from enrollments
    const studentIds = enrollmentsData.map(enrollment => enrollment.student_id)

    // Fetch students details
    const { data: studentsData, error: studentsError } = await supabase
      .from('students')
      .select('*')
      .in('id', studentIds)
      .eq('is_active', true)

    if (studentsError) {
      console.error('Error fetching students:', studentsError)
      throw studentsError
    }

    console.log('✅ Students data found:', studentsData)

    // Combine enrollment and student data
    students.value = enrollmentsData.map((enrollment: any) => {
      const studentData = studentsData?.find((s: any) => s.id === enrollment.student_id)
      
      return {
        id: enrollment.student_id,
        full_name: studentData?.full_name || `Student ${enrollment.student_id.slice(-8)}`,
        email: studentData?.email || 'No email',
        enrolled_at: enrollment.enrolled_at || enrollment.created_at,
        status: enrollment.status || 'active',
        enrollment_id: enrollment.id,
        grade_level: studentData?.grade_level || 'N/A'
      } as Student
    })

    console.log('✅ Final students data:', students.value)

  } catch (error) {
    console.error('Error fetching students:', error)
    alert(`Error loading students: ${error instanceof Error ? error.message : 'Unknown error'}`)
    students.value = []
  } finally {
    isLoading.value = false
  }
}

const formatDate = (dateString: string) => {
  if (!dateString) return 'Never'
  const date = new Date(dateString)
  // Use compact but accurate date format
  return date.toLocaleDateString('en-US', {
    month: 'short',
    day: 'numeric',
    year: 'numeric'
  })
}

const goBack = async () => {
  // Go back to MySubjects.vue and set viewMode to 'section-detail' with correct params
  router.push({
    name: 'MySubjects',
    params: {
      subjectId: subjectId.value,
      sectionId: sectionId.value
    },
    query: {
      viewMode: 'section-detail',
      subjectName: subjectName.value,
      sectionName: sectionName.value,
      gradeLevel: gradeLevel.value,
      sectionCode: sectionCode.value
    }
  });
}

const exportStudents = async () => {
  isExporting.value = true
  
  try {
    let csvContent = `Subject: ${subjectName.value} (Grade ${gradeLevel.value})\n`
    csvContent += `Section: ${sectionName.value} (${sectionCode.value})\n`
    csvContent += `Total Students: ${students.value.length}\n\n`
    csvContent += `Student ID,Full Name,Email,Status,Enrollment Date,Last Activity,Quiz Count,Average Grade\n`
    
    students.value.forEach((student: Student) => {
      csvContent += `"${student.id}","${student.full_name}","${student.email}","${student.status}","${formatDate(student.enrolled_at)}","${formatDate(student.last_activity)}","${student.quiz_count || 0}","${student.average_grade || 'N/A'}%"\n`
    })
    
    const blob = new Blob([csvContent], { type: 'text/csv' })
    const url = window.URL.createObjectURL(blob)
    const a = document.createElement('a')
    a.href = url
    a.download = `${subjectName.value}_${sectionName.value}_Students.csv`
    document.body.appendChild(a)
    a.click()
    document.body.removeChild(a)
    window.URL.revokeObjectURL(url)
    
    console.log('Exported students list successfully')
  } catch (error) {
    console.error('Error exporting students:', error)
    alert('Error exporting students list. Please try again.')
  } finally {
    isExporting.value = false
  }
}

onMounted(() => {
  fetchStudents()
  window.addEventListener('scroll', handleScroll)
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
})
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&800&display=swap');

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
  height: calc(100vh - 64px);
  position: relative;
  background: #f8fafc;
  overflow-y: auto;
  overflow-x: hidden;
  scroll-behavior: smooth;
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

.spinner {
  animation: spin 0.8s linear infinite;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
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

.spinner {
  animation: spin 0.8s linear infinite;
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

.students-home-container {
  min-height: 100vh;
  background: #FBFFE4;
  padding: 1.5rem;
  font-family: 'Inter', sans-serif;
}
.dark .students-home-container {
  background: #181c20;
}

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

.header-content {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.header-left {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.user-icon {
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
  font-weight: 700;
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
}

/* Header Action Button - Matching MySubjects create-quiz-btn */
.header-action-btn {
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
.header-action-btn:disabled {
  opacity: 0.7;
  cursor: not-allowed;
}
.header-action-btn:hover:not(:disabled) {
  background: #A3D1C6;
  color: #23272b;
  border-color: #20c997;
  transform: translateY(-1px);
}
.dark .header-action-btn {
  background: #20c997;
  color: #181c20;
  border: 1px solid #A3D1C6;
}
.dark .header-action-btn:hover:not(:disabled) {
  background: #A3D1C6;
  color: #23272b;
  border-color: #20c997;
}

.main-content-wrapper {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

/* Stats Grid - Matching MySubjects */
.stats-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1rem;
  margin-bottom: 1.5rem;
}

.stat-card {
  background: white;
  border: 1.5px solid #e5e7eb;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.04);
  padding: 1.25rem;
  display: flex;
  align-items: center;
  gap: 1rem;
  transition: all 0.18s ease;
}

.dark .stat-card {
  background: #23272b;
  border: 1.5px solid #374151;
  box-shadow: 0 2px 8px rgba(32, 201, 151, 0.13);
}

.stat-card:hover {
  box-shadow: 0 8px 24px rgba(16, 185, 129, 0.12);
  border-color: #10b981;
  background: #f8fdfa;
  transform: translateY(-2px);
}

.dark .stat-card:hover {
  border-color: #20c997;
  box-shadow: 0 8px 24px rgba(16, 185, 129, 0.18);
  background: #23272b;
}

.stat-icon {
  width: 48px;
  height: 48px;
  border-radius: 14px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  flex-shrink: 0;
  transition: transform 0.2s ease;
}

.stat-classes { 
  background: linear-gradient(135deg, #3D8D7A, #20c997);
  box-shadow: 0 4px 12px rgba(61, 141, 122, 0.3);
}
.stat-graded { 
  background: linear-gradient(135deg, #10b981, #059669);
  box-shadow: 0 4px 12px rgba(16, 185, 129, 0.3);
}

.stat-number {
  font-size: 1.875rem;
  font-weight: 700;
  color: #1f2937;
  line-height: 1;
}
.dark .stat-number {
  color: #f9fafb;
}

.stat-label {
  font-size: 0.875rem;
  color: #6b7280;
  margin-top: 0.25rem;
  font-weight: 500;
}
.dark .stat-label {
  color: #9ca3af;
}

/* Content Card - Matching MySubjects */
.content-card {
  background: #fff;
  border: 1.5px solid #e5e7eb;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.04);
  padding: 0;
  margin-bottom: 1rem;
  transition: all 0.18s ease;
  overflow: hidden;
}

.dark .content-card {
  background: #23272b;
  border: 1.5px solid #374151;
  box-shadow: 0 2px 8px rgba(32, 201, 151, 0.13);
}

.card-header {
  padding: 1.5rem 1.5rem 1rem 1.5rem;
  background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
  border-bottom: 1px solid #e2e8f0;
}

.dark .card-header {
  background: #1f2937;
  border-bottom: 1px solid #374151;
}

.card-header h3 {
  font-size: 1.25rem;
  font-weight: 700;
  color: #1f2937;
  margin: 0 0 0.25rem 0;
  line-height: 1.3;
}
.dark .card-header h3 {
  color: #f9fafb;
}

.card-desc {
  font-size: 0.95rem;
  color: #10b981;
  font-weight: 600;
  margin: 0;
}
.dark .card-desc {
  color: #34d399;
}

/* Search Controls - Enhanced */
.search-controls {
  display: flex;
  gap: 1rem;
  align-items: center;
  padding: 1.5rem;
  background: #fff;
}

.dark .search-controls {
  background: #23272b;
}

.search-input-simple {
  flex: 1;
  background: #f8f9fa;
  border: 2px solid #e5e7eb;
  border-radius: 10px;
  padding: 0.75rem 1rem;
  font-size: 0.875rem;
  font-family: 'Inter', sans-serif;
  color: #1f2937;
  transition: all 0.2s;
}

.search-input-simple:focus {
  outline: none;
  border-color: #10b981;
  box-shadow: 0 0 0 3px rgba(16, 185, 129, 0.1);
}

.dark .search-input-simple {
  background: #374151;
  border-color: #4b5563;
  color: #f3f4f6;
}

.dark .search-input-simple:focus {
  border-color: #10b981;
  box-shadow: 0 0 0 3px rgba(16, 185, 129, 0.1);
}

.filter-select-simple {
  background: #f8f9fa;
  border: 2px solid #e5e7eb;
  border-radius: 10px;
  padding: 0.75rem 1rem;
  font-size: 0.875rem;
  font-family: 'Inter', sans-serif;
  color: #1f2937;
  transition: all 0.2s;
  min-width: 150px;
}

.filter-select-simple:focus {
  outline: none;
  border-color: #10b981;
  box-shadow: 0 0 0 3px rgba(16, 185, 129, 0.1);
}

.dark .filter-select-simple {
  background: #374151;
  border-color: #4b5563;
  color: #f3f4f6;
}

.dark .filter-select-simple:focus {
  border-color: #10b981;
  box-shadow: 0 0 0 3px rgba(16, 185, 129, 0.1);
}

/* Students List - Enhanced Design */
.students-list-simple {
  display: flex;
  flex-direction: column;
  background: #fff;
}

.dark .students-list-simple {
  background: #23272b;
}

.students-list-header {
  display: grid;
  grid-template-columns: 2fr 120px 180px; /* Name 2fr, Status 120px, Date 180px for full date */
  gap: 1rem;
  font-size: 0.75rem;
  font-weight: 600;
  color: #ffffff;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  padding: 1rem 1.5rem;
  background: linear-gradient(135deg, #3D8D7A 0%, #20c997 100%);
  border-bottom: 1px solid #A3D1C6;
}

.dark .students-list-header {
  background: linear-gradient(135deg, #20c997 0%, #3D8D7A 100%);
  border-bottom-color: #A3D1C6;
  color: #ffffff;
}

.students-list-row {
  display: grid;
  grid-template-columns: 2fr 120px 180px; /* Match header grid exactly */
  gap: 1rem;
  align-items: center;
  padding: 1rem 1.5rem;
  border-bottom: 1px solid #f3f4f6;
  font-size: 0.875rem;
  color: #1f2937;
  transition: all 0.2s ease;
}

.students-list-row:hover {
  background: linear-gradient(135deg, #f8fdfa 0%, #f1f5f9 100%);
}

.students-list-row:last-child {
  border-bottom: none;
}

.dark .students-list-row {
  color: #f3f4f6;
  border-bottom-color: #374151;
}

.dark .students-list-row:hover {
  background: #374151;
}

/* Remove text overflow restrictions for date column */
.students-list-row span:last-child,
.students-list-header span:last-child {
  font-size: 0.875rem;
  white-space: nowrap;
  text-align: left;
}

/* Status Badge - Enhanced */
.status-badge {
  padding: 0.375rem 0.75rem;
  border-radius: 12px;
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.025em;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-width: 80px;
  transition: all 0.2s ease;
}

.status-badge.active {
  background: linear-gradient(135deg, #d1fae5, #a7f3d0);
  color: #065f46;
  border: 1px solid #10b981;
  box-shadow: 0 2px 4px rgba(16, 185, 129, 0.1);
}

.status-badge.inactive {
  background: linear-gradient(135deg, #fee2e2, #fecaca);
  color: #991b1b;
  border: 1px solid #ef4444;
  box-shadow: 0 2px 4px rgba(239, 68, 68, 0.1);
}

/* Empty State - Matching MySubjects */
.empty-state {
  background: white;
  border-radius: 16px;
  padding: 2.5rem 1.5rem;
  margin: 2rem auto;
  max-width: 480px;
  box-shadow: 0 1px 3px rgba(0,0,0,0.07);
  text-align: center;
  color: #1f2937;
}
.dark .empty-state {
  background: #23272b;
  color: #A3D1C6;
  border: 1px solid #20c997;
}

.empty-icon {
  margin-bottom: 1rem;
  color: #3D8D7A;
}
.dark .empty-icon {
  color: #A3D1C6;
}

.empty-title {
  font-size: 1.25rem;
  font-weight: 700;
  margin-bottom: 0.5rem;
}

.empty-desc {
  font-size: 0.95rem;
  color: #6b7280;
  margin-bottom: 1.5rem;
}

.dark .empty-desc {
  color: #9ca3af;
}

.no-results {
  text-align: center;
  color: #6b7280;
  padding: 2rem;
  font-size: 0.875rem;
}

.dark .no-results {
  color: #9ca3af;
}

/* Loading State */
.loading-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 3rem;
  text-align: center;
}

.loading-spinner {
  width: 40px;
  height: 40px;
  border: 4px solid rgba(61, 141, 122, 0.1);
  border-left: 4px solid #3D8D7A;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin-bottom: 1rem;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.loading-state p {
  color: #6b7280;
  font-size: 0.875rem;
  font-weight: 500;
}

.dark .loading-state p {
  color: #9ca3af;
}

/* Spinner for buttons */
.spinner {
  animation: spin 0.8s linear infinite;
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
}

@media (max-width: 768px) {
  .header-content {
    flex-direction: column;
    gap: 1rem;
    align-items: stretch;
  }
  
  .header-actions {
    flex-direction: column;
    gap: 0.5rem;
  }
  
  .stats-grid {
    grid-template-columns: 1fr;
  }
  
  .search-controls {
    flex-direction: column;
    align-items: stretch;
  }
  
  .students-list-header,
  .students-list-row {
    grid-template-columns: 1fr auto;
    gap: 0.5rem;
  }
  
  .students-list-header span:last-child,
  .students-list-row span:last-child {
    display: none;
  }
  
  .main-content {
    padding: 1rem;
    margin-left: 0;
  }
  
  .sidebar {
    transform: translateX(-100%);
  }
  
  .page-header {
    padding: 1rem;
    margin-bottom: 1.5rem;
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
</style>