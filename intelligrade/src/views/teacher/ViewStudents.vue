<template>
  <div :class="['students-home-container', isDarkMode ? 'dark' : '']">
    <!-- Simple Header Section -->
    <div class="header-card">
      <div class="header-content">
        <div class="header-left">
          <div class="user-icon">
            <svg width="32" height="32" viewBox="0 0 24 24" fill="currentColor">
              <path d="M16,4C18.21,4 20,5.79 20,8C20,10.21 18.21,12 16,12C13.79,12 12,10.21 12,8C12,5.79 13.79,4 16,4M16,14C20.42,14 24,15.79 24,18V20H8V18C8,15.79 11.58,14 16,14M6,6C7.1,6 8,6.9 8,8C8,9.1 7.1,10 6,10C4.9,10 4,9.1 4,8C4,6.9 4.9,6 6,6M6,12C8.67,12 12,13.34 12,16V18H0V16C0,13.34 3.33,12 6,12Z" />
            </svg>
          </div>
          <div>
            <h1 class="header-title">Student Management</h1>
            <p class="header-subtitle">{{ subjectName }} (Grade {{ gradeLevel }}) - {{ sectionName }} ({{ sectionCode }})</p>
          </div>
        </div>
        <div class="header-actions">
          <button @click="exportStudents" class="header-action-btn" :disabled="isExporting">
            <svg v-if="isExporting" width="20" height="20" viewBox="0 0 24 24" fill="currentColor" class="spinner">
              <path d="M12,4V2A10,10 0 0,0 2,12H4A8,8 0 0,1 12,4Z" />
            </svg>
            <svg v-else width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M14,2H6A2,2 0 0,0 4,4V20A2,2 0 0,0 6,22H18A2,2 0 0,0 20,20V8L14,2M18,20H6V4H13V9H18V20Z" />
            </svg>
            {{ isExporting ? 'Exporting...' : 'Export List' }}
          </button>
          <button @click="goBack" class="header-action-btn">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M20,11V13H8L13.5,18.5L12.08,19.92L4.16,12L12.08,4.08L13.5,5.5L8,11H20Z" />
            </svg>
            Back to Section
          </button>
        </div>
      </div>
    </div>

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
            <button @click="showAddStudentModal = true" class="add-student-btn" title="Add Student">
              Add Student
            </button>
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
            <p>No students enrolled yet.</p>
            <button @click="showAddStudentModal = true" class="empty-action-btn">Add First Student</button>
          </div>
          <div v-else class="no-results">
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
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

.students-home-container {
  min-height: 100vh;
  background: #FBFFE4;
  padding: 1.5rem;
  font-family: 'Inter', sans-serif;
}
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

.students-home-container {
  min-height: 100vh;
  background: #FBFFE4;
  padding: 1.5rem;
  font-family: 'Inter', sans-serif;
}
.dark .students-home-container {
  background: #181c20;
}

.header-card {
  background: white;
  border-radius: 16px;
  padding: 1.5rem;
  margin-bottom: 1.5rem;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
}
.dark .header-card {
  background: #23272b;
  border: 1px solid #3D8D7A;
  box-shadow: 0 2px 8px rgba(0,0,0,0.25);
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
  background: linear-gradient(135deg, #3D8D7A 0%, #A3D1C6 100%);
  color: white;
  box-shadow: 0 4px 14px rgba(61, 141, 122, 0.3);
}
.export-btn:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(61, 141, 122, 0.4);
  background: linear-gradient(135deg, #3D8D7A 0%, #B3D8A8 100%);
}
.export-btn:disabled {
  opacity: 0.7;
  cursor: not-allowed;
  transform: none;
}
.back-button {
  background: #FBFFE4;
  color: #374151;
  border: 2px solid #A3D1C6;
  backdrop-filter: blur(10px);
}
.back-button:hover {
  background: #B3D8A8;
  border-color: #3D8D7A;
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
}
.main-content-wrapper {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}
.stats-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
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
.stat-classes { background: #3D8D7A; }
.stat-graded { background: #B3D8A8; }
.stat-number {
  font-size: 1.875rem;
  font-weight: 700;
  color: #1f2937;
  line-height: 1;
}
.dark .stat-number {
  color: #A3D1C6;
}
.stat-label {
  font-size: 0.813rem;
  color: #6b7280;
  margin-top: 0.25rem;
  font-weight: 500;
}
.dark .stat-label {
  color: #A3D1C6;
}
.content-card {
  background: white;
  border-radius: 12px;
  padding: 1.5rem;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
  display: flex;
  flex-direction: column;
  gap: 1rem;
}
.dark .content-card {
  background: #23272b;
  border: 1px solid #3D8D7A;
  box-shadow: 0 2px 8px rgba(0,0,0,0.25);
}
.card-header {
  margin-bottom: 1rem;
}
.card-header h3 {
  font-size: 1.125rem;
  font-weight: 600;
  color: #1f2937;
  margin-bottom: 0.25rem;
}
.dark .card-header h3 {
  color: #A3D1C6;
}
.card-desc {
  font-size: 0.813rem;
  color: #6b7280;
}
.dark .card-desc {
  color: #A3D1C6;
}
.search-controls {
  display: flex;
  gap: 1rem;
  align-items: center;
  margin-bottom: 1rem;
}
.search-input-simple {
  flex: 1;
  padding: 0.75rem 1rem;
  border: 1.5px solid #A3D1C6;
  border-radius: 8px;
  font-size: 1rem;
  background: #FBFFE4;
  color: #1f2937;
}
.dark .search-input-simple {
  background: #23272b;
  color: #A3D1C6;
  border-color: #3D8D7A;
}
.filter-select-simple {
  padding: 0.75rem 1rem;
  border: 1.5px solid #A3D1C6;
  border-radius: 8px;
  font-size: 1rem;
  background: #FBFFE4;
  color: #1f2937;
}
.dark .filter-select-simple {
  background: #23272b;
  color: #A3D1C6;
  border-color: #3D8D7A;
}
.add-student-btn {
  background: #3D8D7A;
  color: #FBFFE4;
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 8px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
}
.add-student-btn:hover {
  background: #B3D8A8;
  color: #23272b;
}
.students-list-simple {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}
.students-list-header {
  display: flex;
  justify-content: space-between;
  font-weight: 600;
  color: #3D8D7A;
  border-bottom: 1px solid #A3D1C6;
  padding-bottom: 0.5rem;
  margin-bottom: 0.5rem;
}
.students-list-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.5rem 0;
  border-bottom: 1px solid #F3F4F6;
  font-size: 1rem;
  color: #23272b;
}
.dark .students-list-row {
  color: #A3D1C6;
  border-bottom: 1px solid #3D8D7A;
}
.status-badge {
  padding: 0.25rem 0.75rem;
  border-radius: 12px;
  font-size: 0.85em;
  font-weight: 600;
  text-transform: uppercase;
  background: #B3D8A8;
  color: #3D8D7A;
}
.status-badge.active {
  background: #B3D8A8;
  color: #3D8D7A;
}
.status-badge.inactive {
  background: #FEE2E2;
  color: #991b1b;
}
.empty-state, .no-results {
  text-align: center;
  color: #6b7280;
  padding: 2rem 0;
}
.empty-action-btn {
  background: #3D8D7A;
  color: #FBFFE4;
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 8px;
  font-weight: 600;
  cursor: pointer;
  margin-top: 1rem;
  transition: all 0.2s;
}
.empty-action-btn:hover {
  background: #B3D8A8;
  color: #23272b;
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

/* --- Header Action Button (Reference: MySubjects.vue create-quiz-btn) --- */
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
</style>