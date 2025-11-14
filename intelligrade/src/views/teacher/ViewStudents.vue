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
          
          <router-link to="/teacher/subjects" class="nav-item active">
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
        
        <!-- Right: Actions -->
        <div class="navbar-right">
          <button @click="exportStudents" class="export-btn" :disabled="isExporting">
            <svg v-if="isExporting" width="16" height="16" viewBox="0 0 24 24" fill="currentColor" class="spinner">
              <path d="M12,4V2A10,10 0 0,0 2,12H4A8,8 0 0,1 12,4Z" />
            </svg>
            <svg v-else width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
              <path d="M14,2H6A2,2 0 0,0 4,4V20A2,2 0 0,0 6,22H18A2,2 0 0,0 20,20V8L14,2M18,20H6V4H13V9H18V20Z" />
            </svg>
            <span>{{ isExporting ? 'Exporting...' : 'Export List' }}</span>
          </button>
          <button @click="goBack" class="export-btn">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
              <path d="M20,11V13H8L13.5,18.5L12.08,19.92L4.16,12L12.08,4.08L13.5,5.5L8,11H20Z" />
            </svg>
            <span>Back to Section</span>
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
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, computed } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { supabase } from '../../supabase.js'
import { useDarkMode } from '../../composables/useDarkMode.js'

// Dark mode
const { isDarkMode, initDarkMode } = useDarkMode()

const router = useRouter()
const route = useRoute()

// Route data
const subjectId = ref(route.params.subjectId)
const sectionId = ref(route.params.sectionId)
const subjectName = ref(route.query.subjectName || '')
const sectionName = ref(route.query.sectionName || '')
const gradeLevel = ref(route.query.gradeLevel || '')
const classCode = ref(route.query.classCode || '')
const sectionCode = ref(route.query.sectionCode || '')

// State
const students = ref<any[]>([])
const searchQuery = ref('')
const filterStatus = ref('all')
const isLoading = ref(false)
const isExporting = ref(false)
const loadingMessage = ref('')

// Computed
const filteredStudents = computed(() => {
  let filtered = students.value

  // Filter by search query
  if (searchQuery.value) {
    const query = searchQuery.value.toLowerCase()
    filtered = filtered.filter((student: any) => 
      student.full_name.toLowerCase().includes(query) ||
      student.email.toLowerCase().includes(query)
    )
  }

  // Filter by status
  if (filterStatus.value !== 'all') {
    filtered = filtered.filter((student: any) => student.status === filterStatus.value)
  }

  return filtered
})

const activeStudents = computed(() => {
  return students.value.filter((student: any) => student.status === 'active').length
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
      const studentData = studentsData?.find(s => s.id === enrollment.student_id)
      
      return {
        id: enrollment.student_id,
        full_name: studentData?.full_name || `Student ${enrollment.student_id.slice(-8)}`,
        email: studentData?.email || 'No email',
        enrolled_at: enrollment.enrolled_at || enrollment.created_at,
        status: enrollment.status || 'active',
        enrollment_id: enrollment.id,
        grade_level: studentData?.grade_level || 'N/A'
      }
    })

    console.log('✅ Final students data:', students.value)

  } catch (error: any) {
    console.error('Error fetching students:', error)
    alert(`Error loading students: ${error?.message || 'Unknown error'}`)
    students.value = []
  } finally {
    isLoading.value = false
  }
}

const getInitials = (name: string) => {
  if (!name) return 'NS'
  return name.split(' ')
    .map((word: string) => word.charAt(0))
    .join('')
    .substring(0, 2)
    .toUpperCase()
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

const removeStudent = async (student: any) => {
  if (!confirm(`Are you sure you want to remove ${student.full_name} from this section?`)) {
    return
  }

  isLoading.value = true
  loadingMessage.value = 'Removing student...'

  try {
    const { error } = await supabase
      .from('enrollments')
      .delete()
      .eq('section_id', sectionId.value)
      .eq('student_id', student.id)

    if (error) throw error

    alert(`${student.full_name} removed from section successfully!`)
    await fetchStudents()

  } catch (error: any) {
    console.error('Error removing student:', error)
    alert(`Error removing student: ${error?.message || 'Unknown error'}`)
  } finally {
    isLoading.value = false
  }
}

const exportStudents = async () => {
  isExporting.value = true
  
  try {
    let csvContent = `Subject: ${subjectName.value} (Grade ${gradeLevel.value})\n`
    csvContent += `Section: ${sectionName.value} (${sectionCode.value})\n`
    csvContent += `Total Students: ${students.value.length}\n\n`
    csvContent += `Student ID,Full Name,Email,Status,Enrollment Date,Last Activity,Quiz Count,Average Grade\n`
    
    students.value.forEach((student: any) => {
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
  } catch (error: any) {
    console.error('Error exporting students:', error)
    alert('Error exporting students list. Please try again.')
  } finally {
    isExporting.value = false
  }
}

onMounted(() => {
  fetchStudents()
})
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

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
  
  .navbar-center {
    gap: 0.25rem;
  }
  
  .nav-item {
    padding: 0.5rem 1rem;
    font-size: 0.7rem;
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
  }
  
  .page-header {
    padding: 1rem;
    margin-bottom: 1.5rem;
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
}
</style>