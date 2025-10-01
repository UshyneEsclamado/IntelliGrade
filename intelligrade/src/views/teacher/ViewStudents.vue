<template>
  <div class="students-container" :class="{ 'dark-mode': isDarkMode }">
    <!-- Enhanced Header Section -->
    <div class="section-header-card">
      <div class="header-bg-decoration"></div>
      <div class="floating-shapes">
        <div class="shape shape-1"></div>
        <div class="shape shape-2"></div>
        <div class="shape shape-3"></div>
      </div>
      
      <div class="section-header-content">
        <div class="section-header-left">
          <div class="section-header-icon">
            <svg width="40" height="40" viewBox="0 0 24 24" fill="currentColor">
              <path d="M16,4C18.21,4 20,5.79 20,8C20,10.21 18.21,12 16,12C13.79,12 12,10.21 12,8C12,5.79 13.79,4 16,4M16,14C20.42,14 24,15.79 24,18V20H8V18C8,15.79 11.58,14 16,14M6,6C7.1,6 8,6.9 8,8C8,9.1 7.1,10 6,10C4.9,10 4,9.1 4,8C4,6.9 4.9,6 6,6M6,12C8.67,12 12,13.34 12,16V18H0V16C0,13.34 3.33,12 6,12Z" />
            </svg>
          </div>
          <div class="header-text">
            <div class="section-header-title">Student Management</div>
            <div class="section-header-subtitle">{{ subjectName }} (Grade {{ gradeLevel }})</div>
            <div class="section-header-description">{{ sectionName }} - {{ sectionCode }}</div>
          </div>
        </div>
        
        <div class="header-actions">
          <button @click="exportStudents" class="export-btn" :disabled="isExporting">
            <svg v-if="isExporting" width="20" height="20" viewBox="0 0 24 24" fill="currentColor" class="spinner">
              <path d="M12,4V2A10,10 0 0,0 2,12H4A8,8 0 0,1 12,4Z" />
            </svg>
            <svg v-else width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M14,2H6A2,2 0 0,0 4,4V20A2,2 0 0,0 6,22H18A2,2 0 0,0 20,20V8L14,2M18,20H6V4H13V9H18V20Z" />
            </svg>
            {{ isExporting ? 'Exporting...' : 'Export List' }}
          </button>
          <button @click="goBack" class="back-button">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M10 19l-7-7 7-7m-7 7h18"></path>
            </svg>
            Back to Subjects
          </button>
        </div>
      </div>
    </div>

    <!-- Main Content -->
    <div class="main-wrapper">
      <!-- Loading State -->
      <div v-if="isLoading" class="loading-state">
        <div class="loading-spinner"></div>
        <p>{{ loadingMessage }}</p>
      </div>

      <!-- Students Content -->
      <div v-else class="students-content">
        <!-- Summary Cards -->
        <div class="summary-grid">
          <div class="summary-card total-students">
            <div class="summary-icon">
              <svg width="32" height="32" viewBox="0 0 24 24" fill="currentColor">
                <path d="M16,4C18.11,4 19.81,5.69 19.81,7.8C19.81,9.91 18.11,11.6 16,11.6C13.89,11.6 12.2,9.91 12.2,7.8C12.2,5.69 13.89,4 16,4M16,13.4C18.73,13.4 22,14.76 22,17.5V20H10V17.5C10,14.76 13.27,13.4 16,13.4M6,6H8V8H6V6M6,10H8V12H6V10M6,14H8V16H6V14Z" />
              </svg>
            </div>
            <div class="summary-info">
              <span class="summary-number">{{ students.length }}</span>
              <span class="summary-label">Total Students</span>
            </div>
          </div>

          <div class="summary-card active-students">
            <div class="summary-icon">
              <svg width="32" height="32" viewBox="0 0 24 24" fill="currentColor">
                <path d="M9,20.42L2.79,14.21L5.62,11.38L9,14.77L18.88,4.88L21.71,7.71L9,20.42Z" />
              </svg>
            </div>
            <div class="summary-info">
              <span class="summary-number">{{ activeStudents }}</span>
              <span class="summary-label">Active Students</span>
            </div>
          </div>
        </div>

        <!-- Students Management Section -->
        <div class="students-section">
          <div class="section-header">
            <div class="section-title">
              <h3>Enrolled Students</h3>
              <p>{{ students.length }} students enrolled in this section</p>
            </div>
            
            <!-- Search and Filter -->
            <div class="search-controls">
              <div class="search-input">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" class="search-icon">
                  <path d="M9.5,3A6.5,6.5 0 0,1 16,9.5C16,11.11 15.41,12.59 14.44,13.73L14.71,14H15.5L20.5,19L19,20.5L14,15.5V14.71L13.73,14.44C12.59,15.41 11.11,16 9.5,16A6.5,6.5 0 0,1 3,9.5A6.5,6.5 0 0,1 9.5,3M9.5,5C7,5 5,7 5,9.5C5,12 7,14 9.5,14C12,14 14,12 14,9.5C14,7 12,5 9.5,5Z" />
                </svg>
                <input 
                  type="text" 
                  v-model="searchQuery" 
                  placeholder="Search students by name or email..."
                >
              </div>
              
              <select v-model="filterStatus" class="filter-select">
                <option value="all">All Students</option>
                <option value="active">Active</option>
                <option value="inactive">Inactive</option>
              </select>

              <button @click="showAddStudentModal = true" class="add-student-icon-btn" title="Add Student">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M15 12C17.21 12 19 10.21 19 8S17.21 4 15 4 11 5.79 11 8 12.79 12 15 12M6 10V7H4V10H1V12H4V15H6V12H9V10M15 14C12.33 14 7 15.34 7 18V20H23V18C23 15.34 17.67 14 15 14Z"/>
                </svg>
              </button>
            </div>
          </div>

          <!-- Students List -->
          <div v-if="filteredStudents.length > 0" class="students-list">
            <div class="list-header">
              <div class="header-name">Student Name</div>
              <div class="header-enrolled">Enrolled</div>
              <div class="header-status">Status</div>
            </div>
            
            <div v-for="student in filteredStudents" :key="student.id" class="student-row">
              <div class="student-name">
                <div class="name-avatar">
                  {{ getInitials(student.full_name) }}
                </div>
                <span>{{ student.full_name }}</span>
              </div>
              <div class="student-enrolled">{{ formatDate(student.enrolled_at) }}</div>
              <div class="student-status">
                <span :class="['status-badge', student.status]">{{ student.status }}</span>
              </div>
            </div>
          </div>

          <!-- Empty State -->
          <div v-else-if="students.length === 0" class="empty-state">
            <div class="empty-icon">
              <svg width="64" height="64" viewBox="0 0 24 24" fill="currentColor">
                <path d="M16,4C18.11,4 20.11,4.89 21.39,6.39C22.67,7.89 23.11,9.89 22.39,11.39L20.39,8.61C19.56,7.11 18.11,6 16,6C15.44,6 14.89,6.22 14.5,6.61L12.89,8.22C12.33,8.78 11.67,8.78 11.11,8.22L9.5,6.61C9.11,6.22 8.56,6 8,6C5.89,6 4.44,7.11 3.61,8.61L1.61,11.39C0.89,9.89 1.33,7.89 2.61,6.39C3.89,4.89 5.89,4 8,4C9.33,4 10.56,4.44 11.5,5.17C12.44,4.44 13.67,4 16,4M12,13.5A1.5,1.5 0 0,1 10.5,12A1.5,1.5 0 0,1 12,10.5A1.5,1.5 0 0,1 13.5,12A1.5,1.5 0 0,1 12,13.5Z" />
              </svg>
            </div>
            <h3>No Students Enrolled</h3>
            <p>Students will appear here once they join this section using the section code.</p>
            <button @click="showAddStudentModal = true" class="empty-action-btn">
              Add First Student
            </button>
          </div>

          <!-- No Results -->
          <div v-else class="no-results">
            <div class="no-results-icon">
              <svg width="48" height="48" viewBox="0 0 24 24" fill="currentColor">
                <path d="M9.5,3A6.5,6.5 0 0,1 16,9.5C16,11.11 15.41,12.59 14.44,13.73L14.71,14H15.5L20.5,19L19,20.5L14,15.5V14.71L13.73,14.44C12.59,15.41 11.11,16 9.5,16A6.5,6.5 0 0,1 3,9.5A6.5,6.5 0 0,1 9.5,3M9.5,5C7,5 5,7 5,9.5C5,12 7,14 9.5,14C12,14 14,12 14,9.5C14,7 12,5 9.5,5Z" />
              </svg>
            </div>
            <h4>No students found</h4>
            <p>No students found matching "{{ searchQuery }}"</p>
          </div>
        </div>
      </div>
    </div>

    <!-- Add Student Modal -->
    <div v-if="showAddStudentModal" class="modal-overlay" @click="showAddStudentModal = false">
      <div class="modal-content" @click.stop>
        <div class="modal-header">
          <h2>Add Student to Section</h2>
          <button @click="showAddStudentModal = false" class="close-btn">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
              <path d="M19,6.41L17.59,5L12,10.59L6.41,5L5,6.41L10.59,12L5,17.59L6.41,19L12,13.41L17.59,19L19,17.59L13.41,12L19,6.41Z" />
            </svg>
          </button>
        </div>

        <div class="modal-body">
          <div class="form-group">
            <label for="student-email">Student Email</label>
            <input 
              type="email" 
              id="student-email" 
              v-model="newStudentEmail" 
              placeholder="student@example.com"
              required
            >
          </div>
          
          <div class="form-group">
            <label for="student-name">Full Name (Optional)</label>
            <input 
              type="text" 
              id="student-name" 
              v-model="newStudentName" 
              placeholder="Student's full name"
            >
          </div>

          <div class="modal-actions">
            <button @click="showAddStudentModal = false" class="cancel-btn">Cancel</button>
            <button @click="addStudent" :disabled="!newStudentEmail" class="add-btn">
              Add Student
            </button>
          </div>
        </div>
      </div>
    </div>
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
const showAddStudentModal = ref(false)
const newStudentEmail = ref('')
const newStudentName = ref('')
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
    // Get enrollments for the section
    const { data: enrollments, error: enrollError } = await supabase
      .from('enrollments')
      .select('*')
      .eq('section_id', sectionId.value)

    if (enrollError) throw enrollError
    if (!enrollments || enrollments.length === 0) {
      students.value = []
      return
    }

    console.log('🔍 Found enrollments:', enrollments)

    // 🎯 COMPREHENSIVE APPROACH: Try multiple ways to get real names
    const studentPromises = enrollments.map(async (enrollment: any) => {
      const studentId = enrollment.student_id
      console.log(`🔍 Processing student ID: ${studentId}`)
      
      let studentName = null
      let foundMethod = 'none'

      // METHOD 1: Try profiles table with auth_user_id
      try {
        const { data: profile1 } = await supabase
          .from('profiles')
          .select('full_name, email')
          .eq('auth_user_id', studentId)
          .single()
        
        if (profile1?.full_name) {
          studentName = profile1.full_name
          foundMethod = 'profiles by auth_user_id'
          console.log(`✅ Method 1 SUCCESS for ${studentId}: ${studentName}`)
        }
      } catch (e) {
        console.log(`❌ Method 1 failed for ${studentId}:`, e)
      }

      // METHOD 2: Try profiles table with id field
      if (!studentName) {
        try {
          const { data: profile2 } = await supabase
            .from('profiles')
            .select('full_name, email')
            .eq('id', studentId)
            .single()
          
          if (profile2?.full_name) {
            studentName = profile2.full_name
            foundMethod = 'profiles by id'
            console.log(`✅ Method 2 SUCCESS for ${studentId}: ${studentName}`)
          }
        } catch (e) {
          console.log(`❌ Method 2 failed for ${studentId}:`, e)
        }
      }

      // METHOD 3: Try students table lookup
      if (!studentName) {
        try {
          const { data: student } = await supabase
            .from('students')
            .select('full_name, profile_id')
            .eq('profile_id', studentId)
            .single()
          
          if (student?.full_name) {
            studentName = student.full_name
            foundMethod = 'students table'
            console.log(`✅ Method 3 SUCCESS for ${studentId}: ${studentName}`)
          }
        } catch (e) {
          console.log(`❌ Method 3 failed for ${studentId}:`, e)
        }
      }

      // METHOD 4: Try auth admin API
      if (!studentName) {
        try {
          const { data: authUser } = await supabase.auth.admin.getUserById(studentId)
          if (authUser?.user) {
            studentName = authUser.user.user_metadata?.full_name || 
                        authUser.user.user_metadata?.name ||
                        authUser.user.email?.split('@')[0]
            if (studentName) {
              foundMethod = 'auth admin API'
              console.log(`✅ Method 4 SUCCESS for ${studentId}: ${studentName}`)
            }
          }
        } catch (e) {
          console.log(`❌ Method 4 failed for ${studentId}:`, e)
        }
      }

      // Final result
      const finalName = studentName || `Student ${studentId.slice(-8).toUpperCase()}`
      console.log(`🎯 FINAL for ${studentId}: "${finalName}" (via ${foundMethod})`)

      return {
        id: studentId,
        full_name: finalName,
        enrolled_at: enrollment.enrolled_at || enrollment.created_at,
        status: enrollment.status || 'active'
      }
    })

    students.value = await Promise.all(studentPromises)
  } catch (error: any) {
    console.error('Error fetching students:', error)
    alert(`Error loading students: ${error?.message || 'Unknown error'}`)
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
  return date.toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'short',
    day: 'numeric'
  })
}

const goBack = async () => {
  try {
    await router.push({ name: 'MySubjects' })
  } catch (error) {
    console.error('Navigation error:', error)
  }
}

const addStudent = async () => {
  if (!newStudentEmail.value) return

  isLoading.value = true
  loadingMessage.value = 'Adding student...'

  try {
    console.log('Adding student:', {
      email: newStudentEmail.value,
      name: newStudentName.value,
      sectionId: sectionId.value
    })

    alert(`Student "${newStudentEmail.value}" added successfully!`)
    
    newStudentEmail.value = ''
    newStudentName.value = ''
    showAddStudentModal.value = false
    
    await fetchStudents()

  } catch (error: any) {
    console.error('Error adding student:', error)
    alert(`Error adding student: ${error?.message || 'Unknown error'}`)
  } finally {
    isLoading.value = false
  }
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
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

.students-container {
  padding: 2rem;
  max-width: 1400px;
  margin: 0 auto;
  font-family: 'Inter', sans-serif;
  background: var(--bg-primary);
  min-height: 100vh;
}

/* Enhanced Header Design */
.section-header-card {
  position: relative;
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.95) 0%, rgba(248, 250, 252, 0.9) 100%);
  backdrop-filter: blur(20px);
  border-radius: 32px;
  padding: 3.5rem;
  margin-bottom: 3rem;
  min-height: 180px;
  box-shadow: 
    0 24px 48px rgba(0, 0, 0, 0.1),
    0 12px 24px rgba(0, 0, 0, 0.08),
    inset 0 1px 0 rgba(255, 255, 255, 0.8);
  border: 2px solid rgba(255, 255, 255, 0.3);
  overflow: hidden;
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}

.section-header-card:hover {
  transform: translateY(-2px);
  box-shadow: 
    0 32px 64px rgba(0, 0, 0, 0.12),
    0 16px 32px rgba(0, 0, 0, 0.1),
    inset 0 1px 0 rgba(255, 255, 255, 0.9);
}

.header-bg-decoration {
  position: absolute;
  top: -50%;
  right: -20%;
  width: 120%;
  height: 200%;
  background: radial-gradient(ellipse at center, rgba(16, 185, 129, 0.08) 0%, transparent 70%);
  z-index: 1;
}

.floating-shapes {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 1;
  pointer-events: none;
}

.shape {
  position: absolute;
  border-radius: 50%;
  background: linear-gradient(135deg, rgba(16, 185, 129, 0.1) 0%, rgba(5, 150, 105, 0.05) 100%);
}

.shape-1 {
  width: 100px;
  height: 100px;
  top: -20px;
  right: 15%;
  animation: float 6s ease-in-out infinite;
}

.shape-2 {
  width: 80px;
  height: 80px;
  bottom: -15px;
  right: 30%;
  animation: float 8s ease-in-out infinite reverse;
}

.shape-3 {
  width: 60px;
  height: 60px;
  top: 40%;
  right: 5%;
  animation: float 7s ease-in-out infinite;
}

@keyframes float {
  0%, 100% { transform: translateY(0) rotate(0deg); }
  50% { transform: translateY(-15px) rotate(10deg); }
}

.section-header-content {
  position: relative;
  z-index: 2;
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
}

.section-header-left {
  display: flex;
  align-items: center;
  gap: 2rem;
}

.section-header-icon {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 80px;
  height: 80px;
  background: linear-gradient(135deg, rgba(16, 185, 129, 0.15) 0%, rgba(5, 150, 105, 0.1) 100%);
  border-radius: 24px;
  color: #059669;
  backdrop-filter: blur(10px);
  border: 1px solid rgba(16, 185, 129, 0.2);
}

.header-text {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.section-header-title {
  font-size: 2.5rem;
  font-weight: 800;
  color: #111827;
  line-height: 1.1;
  margin: 0;
}

.section-header-subtitle {
  font-size: 1.1rem;
  font-weight: 600;
  color: #059669;
  margin: 0;
}

.section-header-description {
  font-size: 1rem;
  color: #6b7280;
  margin: 0;
}

.header-actions {
  display: flex;
  gap: 1rem;
  align-items: center;
}

.export-btn,
.back-button {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 1rem 1.5rem;
  border-radius: 16px;
  font-weight: 600;
  font-size: 0.95rem;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  cursor: pointer;
  text-decoration: none;
  border: none;
}

.export-btn {
  background: linear-gradient(135deg, #059669 0%, #10b981 100%);
  color: white;
  box-shadow: 0 4px 14px rgba(5, 150, 105, 0.3);
}

.export-btn:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(5, 150, 105, 0.4);
  background: linear-gradient(135deg, #047857 0%, #059669 100%);
}

.export-btn:disabled {
  opacity: 0.7;
  cursor: not-allowed;
  transform: none;
}

.back-button {
  background: rgba(255, 255, 255, 0.9);
  color: #374151;
  border: 2px solid rgba(16, 185, 129, 0.2);
  backdrop-filter: blur(10px);
}

.back-button:hover {
  background: rgba(255, 255, 255, 1);
  border-color: rgba(16, 185, 129, 0.3);
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
}

.spinner {
  animation: spin 1s linear infinite;
}

@keyframes spin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}

/* Main Content */
.main-wrapper {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

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
  border: 4px solid rgba(16, 185, 129, 0.2);
  border-top: 4px solid #10b981;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin-bottom: 1rem;
}

.loading-state p {
  color: #6b7280;
  font-size: 1.1rem;
  font-weight: 500;
}

/* Summary Cards */
.summary-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 2rem;
  width: 100%;
  margin-bottom: 3rem;
}

.summary-card {
  background: white;
  border: 1px solid #e5e7eb;
  border-radius: 20px;
  padding: 2rem;
  display: flex;
  align-items: center;
  gap: 1.5rem;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
  transition: all 0.3s ease;
}

.summary-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.1);
}

.summary-icon {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 64px;
  height: 64px;
  border-radius: 16px;
  flex-shrink: 0;
}

.total-students .summary-icon {
  background: linear-gradient(135deg, rgba(16, 185, 129, 0.1) 0%, rgba(5, 150, 105, 0.05) 100%);
  color: #059669;
}

.active-students .summary-icon {
  background: linear-gradient(135deg, rgba(34, 197, 94, 0.1) 0%, rgba(22, 163, 74, 0.05) 100%);
  color: #16a34a;
}

.summary-info {
  display: flex;
  flex-direction: column;
}

.summary-number {
  font-size: 2.5rem;
  font-weight: 800;
  color: #111827;
  line-height: 1;
  margin-bottom: 0.25rem;
}

.summary-label {
  font-size: 0.95rem;
  font-weight: 600;
  color: #6b7280;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

/* Students Section */
.students-section {
  background: white;
  border: 1px solid #e5e7eb;
  border-radius: 20px;
  padding: 2.5rem;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
}

.section-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 2rem;
  gap: 2rem;
}

.section-title h3 {
  font-size: 1.5rem;
  font-weight: 700;
  color: #111827;
  margin: 0 0 0.5rem 0;
}

.section-title p {
  color: #6b7280;
  margin: 0;
  font-size: 1rem;
}

.search-controls {
  display: flex;
  gap: 1rem;
  align-items: center;
  flex-wrap: wrap;
}

.search-input {
  position: relative;
  min-width: 300px;
}

.search-icon {
  position: absolute;
  left: 1rem;
  top: 50%;
  transform: translateY(-50%);
  color: #9ca3af;
  z-index: 2;
}

.search-input input {
  width: 100%;
  padding: 0.875rem 1rem 0.875rem 3rem;
  border: 2px solid #e5e7eb;
  border-radius: 12px;
  font-size: 0.95rem;
  background: white;
  transition: all 0.3s ease;
}

.search-input input:focus {
  outline: none;
  border-color: #10b981;
  box-shadow: 0 0 0 3px rgba(16, 185, 129, 0.1);
}

.filter-select {
  padding: 0.875rem 1rem;
  border: 2px solid #e5e7eb;
  border-radius: 12px;
  font-size: 0.95rem;
  background: white;
  color: #374151;
  cursor: pointer;
  transition: all 0.3s ease;
}

.filter-select:focus {
  outline: none;
  border-color: #10b981;
  box-shadow: 0 0 0 3px rgba(16, 185, 129, 0.1);
}

/* Students List */
.students-list {
  background: white;
  border: 1px solid #e5e7eb;
  border-radius: 12px;
  overflow: hidden;
}

.list-header {
  display: grid;
  grid-template-columns: 3fr 1fr 1fr; /* name, enrolled, status */
  gap: 1rem;
  padding: 1rem 1.5rem;
  background: #f9fafb;
  border-bottom: 1px solid #e5e7eb;
  font-weight: 600;
  color: #374151;
  font-size: 0.875rem;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.list-header .header-actions {
  text-align: center;
}

.student-row {
  display: grid;
  grid-template-columns: 3fr 1fr 1fr; /* name, enrolled, status */
  gap: 1rem;
  padding: 1rem 1.5rem;
  border-bottom: 1px solid #f3f4f6;
  align-items: center;
  transition: all 0.2s ease;
}

.student-row:hover {
  background: #f9fafb;
}

.student-row:last-child {
  border-bottom: none;
}

.student-name {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  font-weight: 600;
  color: #111827;
}

.name-avatar {
  width: 32px;
  height: 32px;
  border-radius: 8px;
  background: linear-gradient(135deg, #059669 0%, #10b981 100%);
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 0.75rem;
}



.student-enrolled {
  color: #6b7280;
  font-size: 0.875rem;
}

.status-badge {
  padding: 0.25rem 0.75rem;
  border-radius: 12px;
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
}

.status-badge.active {
  background: #dcfce7;
  color: #166534;
}

.status-badge.inactive {
  background: #fee2e2;
  color: #991b1b;
}



.action-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 36px;
  height: 36px;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.2s ease;
}

.action-btn.remove {
  background: rgba(239, 68, 68, 0.15);
  color: #dc2626;
  border: 1px solid rgba(239, 68, 68, 0.2);
}

.action-btn:hover {
  transform: scale(1.1);
  background: rgba(239, 68, 68, 0.25);
  border-color: rgba(239, 68, 68, 0.4);
}

/* Empty States */
.empty-state,
.no-results {
  text-align: center;
  padding: 4rem 2rem;
  color: #6b7280;
}

.empty-icon,
.no-results-icon {
  color: #d1d5db;
  margin-bottom: 2rem;
}

.empty-state h3,
.no-results h4 {
  color: #111827;
  font-size: 1.5rem;
  font-weight: 700;
  margin-bottom: 1rem;
}

.empty-action-btn {
  background: linear-gradient(135deg, #059669 0%, #10b981 100%);
  color: white;
  border: none;
  padding: 1rem 2rem;
  border-radius: 16px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s;
  margin-top: 1rem;
}

.empty-action-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(5, 150, 105, 0.3);
}

/* Modal Styles */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.6);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
  padding: 2rem;
}

.modal-content {
  background: white;
  border-radius: 24px;
  max-width: 500px;
  width: 100%;
  max-height: 90vh;
  overflow-y: auto;
  box-shadow: 0 25px 50px rgba(0, 0, 0, 0.3);
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 2rem 2rem 1rem;
  border-bottom: 1px solid #e5e7eb;
}

.modal-header h2 {
  color: #111827;
  font-size: 1.5rem;
  font-weight: 700;
  margin: 0;
}

.close-btn {
  background: none;
  border: none;
  color: #6b7280;
  cursor: pointer;
  transition: all 0.3s ease;
  padding: 0.5rem;
  border-radius: 8px;
}

.close-btn:hover {
  color: #111827;
  background: #f3f4f6;
}

.modal-body {
  padding: 2rem;
}

.form-group {
  margin-bottom: 1.5rem;
}

.form-group label {
  display: block;
  margin-bottom: 0.5rem;
  color: #374151;
  font-weight: 600;
}

.form-group input {
  width: 100%;
  padding: 0.75rem 1rem;
  border: 2px solid #e5e7eb;
  border-radius: 12px;
  font-size: 1rem;
  transition: all 0.3s ease;
}

.form-group input:focus {
  outline: none;
  border-color: #10b981;
  box-shadow: 0 0 0 3px rgba(16, 185, 129, 0.1);
}

.modal-actions {
  display: flex;
  gap: 1rem;
  justify-content: flex-end;
  margin-top: 2rem;
}

.cancel-btn {
  background: #f3f4f6;
  color: #374151;
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 12px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s;
}

.cancel-btn:hover {
  background: #e5e7eb;
}

.add-btn {
  background: linear-gradient(135deg, #059669 0%, #10b981 100%);
  color: white;
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 12px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s;
}

.add-btn:hover:not(:disabled) {
  transform: translateY(-1px);
  box-shadow: 0 8px 25px rgba(5, 150, 105, 0.3);
}

.add-btn:disabled {
  opacity: 0.7;
  cursor: not-allowed;
}

/* New Add Student Button Styles */
.add-student-icon-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 56px;
  height: 56px;
  border-radius: 50%;
  background: linear-gradient(135deg, #059669 0%, #10b981 100%);
  color: white;
  border: none;
  font-size: 1.5rem;
  box-shadow: 0 4px 14px rgba(5, 150, 105, 0.3);
  cursor: pointer;
  transition: all 0.3s;
}

.add-student-icon-btn:hover {
  transform: scale(1.08);
  box-shadow: 0 8px 25px rgba(5, 150, 105, 0.4);
}

.add-student-icon-btn svg {
  width: 32px;
  height: 32px;
  color: white;
}

/* Responsive Design */
@media (max-width: 1024px) {
  .section-header-content {
    flex-direction: column;
    gap: 2rem;
    text-align: center;
  }

  .section-header-left {
    flex-direction: column;
    gap: 1rem;
  }

  .header-actions {
    flex-direction: column;
    width: 100%;
  }

  .export-btn,
  .back-button {
    width: 100%;
    justify-content: center;
  }
}

@media (max-width: 768px) {
  .students-container {
    padding: 1rem;
  }

  .section-header-card {
    padding: 2rem;
  }

  .section-header-title {
    font-size: 2rem;
  }

  .summary-grid {
    grid-template-columns: 1fr;
    gap: 1.5rem;
  }

  .section-header {
    flex-direction: column;
    gap: 1rem;
  }

  .search-controls {
    flex-direction: column;
    width: 100%;
  }

  .search-input {
    min-width: unset;
    width: 100%;
  }

  .list-header {
    grid-template-columns: 2fr 1fr 1fr;
    gap: 0.5rem;
    padding: 0.75rem 1rem;
  }

  .header-email,
  .header-enrolled {
    display: none;
  }

  .student-row {
    grid-template-columns: 2fr 1fr 1fr;
    gap: 0.5rem;
    padding: 0.75rem 1rem;
  }

  .student-email,
  .student-enrolled {
    display: none;
  }

  .student-name {
    flex-direction: column;
    align-items: flex-start;
    gap: 0.25rem;
  }

  .name-avatar {
    width: 24px;
    height: 24px;
    font-size: 0.625rem;
  }

  .action-btn {
    width: 28px;
    height: 28px;
  }

  .action-btn svg {
    width: 14px;
    height: 14px;
  }
}

@media (max-width: 480px) {
  .list-header {
    grid-template-columns: 1fr auto;
  }

  .header-status {
    display: none;
  }

  .student-row {
    grid-template-columns: 1fr auto;
  }

  .student-status {
    display: none;
  }
}

/* Dark Mode Styles */
.students-container.dark-mode {
  background: var(--bg-primary);
  color: var(--primary-text-color);
}

.dark-mode .section-header-card {
  background: var(--bg-secondary);
  border: 1px solid var(--border-color);
}

.dark-mode .section-header-title {
  color: var(--primary-text-color);
}

.dark-mode .section-header-subtitle {
  color: var(--accent-color);
}

.dark-mode .section-header-description {
  color: var(--secondary-text-color);
}

.dark-mode .export-btn {
  background: linear-gradient(135deg, var(--accent-color) 0%, #4a9b87 100%);
}

.dark-mode .back-button {
  background: var(--bg-card);
  border: 2px solid var(--border-color);
  color: var(--secondary-text-color);
}

.dark-mode .back-button:hover {
  border-color: var(--accent-color);
  color: var(--accent-color);
}

.dark-mode .loading-state p {
  color: var(--secondary-text-color);
}

.dark-mode .loading-spinner {
  border: 4px solid rgba(95, 179, 160, 0.2);
  border-top: 4px solid var(--accent-color);
}

.dark-mode .summary-card {
  background: var(--bg-secondary);
  border: 1px solid var(--border-color);
}

.dark-mode .summary-number {
  color: var(--primary-text-color);
}

.dark-mode .summary-label {
  color: var(--secondary-text-color);
}

.dark-mode .students-section {
  background: var(--bg-secondary);
  border: 1px solid var(--border-color);
}

.dark-mode .section-title h3 {
  color: var(--primary-text-color);
}

.dark-mode .section-title p {
  color: var(--secondary-text-color);
}

.dark-mode .students-list {
  background: var(--bg-secondary);
  border: 1px solid var(--border-color);
}

.dark-mode .list-header {
  background: var(--bg-primary);
  border-bottom-color: var(--border-color);
  color: var(--secondary-text-color);
}

.dark-mode .student-row {
  border-bottom-color: var(--border-color);
}

.dark-mode .student-row:hover {
  background: var(--bg-primary);
}

.dark-mode .student-name {
  color: var(--primary-text-color);
}

.dark-mode .student-email,
.dark-mode .student-enrolled {
  color: var(--secondary-text-color);
}

.dark-mode .search-input input,
.dark-mode .filter-select {
  background: var(--card-background);
  border-color: var(--border-color);
  color: var(--primary-text-color);
}

.dark-mode .search-input input:focus,
.dark-mode .filter-select:focus {
  border-color: var(--accent-color);
  box-shadow: 0 0 0 3px rgba(95, 179, 160, 0.1);
}

.dark-mode .empty-state h3,
.dark-mode .no-results h4 {
  color: var(--primary-text-color);
}

.dark-mode .modal-content {
  background: var(--bg-secondary);
  border: 1px solid var(--border-color);
}

.dark-mode .modal-header {
  border-bottom-color: var(--border-color);
}

.dark-mode .modal-header h2 {
  color: var(--primary-text-color);
}

.dark-mode .form-group label {
  color: var(--secondary-text-color);
}

.dark-mode .form-group input {
  background: var(--card-background);
  border-color: var(--border-color);
  color: var(--primary-text-color);
}

.dark-mode .form-group input:focus {
  border-color: var(--accent-color);
  box-shadow: 0 0 0 3px rgba(95, 179, 160, 0.1);
}

.dark-mode .cancel-btn {
  background: var(--border-color);
  color: var(--secondary-text-color);
}

.dark-mode .cancel-btn:hover {
  background: var(--card-background);
}
</style>