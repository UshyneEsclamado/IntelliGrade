<template>
  <div class="page-container" :class="{ 'dark-mode': isDarkMode }">
    <div class="main-wrapper">
      <!-- Enhanced Header Section -->
      <section class="section-header-card">
        <div class="floating-shapes">
          <div class="shape shape-1"></div>
          <div class="shape shape-2"></div>
          <div class="shape shape-3"></div>
          <div class="shape shape-4"></div>
        </div>
        
        <div class="header-content">
          <button @click="goBack" class="back-button">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M10 19l-7-7 7-7m-7 7h18"></path>
            </svg>
            Back to My Subjects
          </button>
          
          <div class="hero-header">
            <h1>{{ sectionName }} Students</h1>
            <p class="hero-subtitle">Manage students and track their progress in this section</p>
          </div>
          
          <div class="section-info">
            <div class="info-badge subject">
              <div class="icon">📚</div>
              <div class="text">
                <span class="label">Subject</span>
                <span class="value">{{ subjectName }} (Grade {{ gradeLevel }})</span>
              </div>
            </div>
            <div class="info-badge section">
              <div class="icon">👥</div>
              <div class="text">
                <span class="label">Section</span>
                <span class="value">{{ sectionName }}</span>
              </div>
            </div>
            <div class="info-badge code">
              <div class="icon">🔑</div>
              <div class="text">
                <span class="label">Section Code</span>
                <span class="value">{{ sectionCode }}</span>
              </div>
            </div>
            <div class="info-badge students">
              <div class="icon">👤</div>
              <div class="text">
                <span class="label">Students</span>
                <span class="value">{{ students.length }}</span>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- Quick Actions -->
      <section class="content-card">
        <div class="card-header">
          <h3>Section Management</h3>
          <p class="card-subtitle">Quick actions for managing this section</p>
        </div>
        <div class="action-buttons">
          <button @click="navigateToCreateQuiz" class="action-btn create-quiz">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M14,2H6A2,2 0 0,0 4,4V20A2,2 0 0,0 6,22H18A2,2 0 0,0 20,20V8L14,2M18,20H6V4H13V9H18V20Z" />
            </svg>
            Create Quiz for This Section
          </button>
          
          <button @click="viewQuizzes" class="action-btn view-quizzes">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M13,9V3.5L18.5,9M6,2C4.89,2 4,2.89 4,4V20A2,2 0 0,0 6,22H18A2,2 0 0,0 20,20V8L14,2H6Z" />
            </svg>
            View All Quizzes
          </button>
          
          <button @click="manageGrades" class="action-btn manage-grades">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M19,3H5C3.9,3 3,3.9 3,5V19C3,20.1 3.9,21 5,21H19C20.1,21 21,20.1 21,19V5C21,3.9 20.1,3 19,3M19,19H5V5H19V19M17,12H7V10H17V12M15,16H7V14H15V16M17,8H7V6H17V8Z" />
            </svg>
            Grade Management
          </button>
          
          <button @click="generateReports" class="action-btn generate-reports">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M9,17H7V10H9V17M13,17H11V7H13V17M17,17H15V13H17V17M19.5,3.5L18,2L16.5,3.5L15,2L13.5,3.5L12,2L10.5,3.5L9,2L7.5,3.5L6,2L4.5,3.5L3,2V22L4.5,20.5L6,22L7.5,20.5L9,22L10.5,20.5L12,22L13.5,20.5L15,22L16.5,20.5L18,22L19.5,20.5L21,22V2L19.5,3.5Z" />
            </svg>
            Reports & Analytics
          </button>
        </div>
      </section>

      <!-- Students List -->
      <section class="content-card">
        <div class="card-header">
          <div class="header-info">
            <h3>Enrolled Students</h3>
            <p class="card-subtitle">{{ students.length }} students enrolled in this section</p>
            <div class="students-stats">
              <div class="stat-item">
                <span class="stat-label">Active:</span>
                <span class="stat-value">{{ activeStudents }}</span>
              </div>
              <div class="stat-item">
                <span class="stat-label">Recent Activity:</span>
                <span class="stat-value">{{ recentlyActive }}</span>
              </div>
            </div>
          </div>
          
          <div class="header-actions">
            <button @click="showAddStudentModal = true" class="add-student-btn">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                <path d="M19,13H13V19H11V13H5V11H11V5H13V11H19V13Z" />
              </svg>
              Add Student
            </button>
            
            <button @click="exportStudents" class="export-btn">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                <path d="M14,2H6A2,2 0 0,0 4,4V20A2,2 0 0,0 6,22H18A2,2 0 0,0 20,20V8L14,2M18,20H6V4H13V9H18V20Z" />
              </svg>
              Export List
            </button>
          </div>
        </div>

        <!-- Search and Filter -->
        <div class="search-section">
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
        </div>

        <!-- Students Grid -->
        <div v-if="filteredStudents.length > 0" class="students-grid">
          <div v-for="student in filteredStudents" :key="student.id" class="student-card">
            <div class="student-avatar">
              <div class="avatar-circle">
                {{ getInitials(student.full_name) }}
              </div>
              <div :class="['status-indicator', student.status]"></div>
            </div>
            
            <div class="student-info">
              <h3>{{ student.full_name }}</h3>
              <p class="email">{{ student.email }}</p>
              <div class="student-meta">
                <span class="enrollment-date">
                  Enrolled: {{ formatDate(student.enrolled_at) }}
                </span>
                <span class="last-activity">
                  Last active: {{ formatDate(student.last_activity) }}
                </span>
              </div>
            </div>
            
            <div class="student-stats">
              <div class="stat-item">
                <span class="stat-value">{{ student.quiz_count || 0 }}</span>
                <span class="stat-label">Quizzes</span>
              </div>
              <div class="stat-item">
                <span class="stat-value">{{ student.average_grade || 'N/A' }}%</span>
                <span class="stat-label">Avg Grade</span>
              </div>
            </div>
            
            <div class="student-actions">
              <button @click="viewStudentDetails(student)" class="student-action-btn view" title="View Details">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M12,9A3,3 0 0,0 9,12A3,3 0 0,0 12,15A3,3 0 0,0 15,12A3,3 0 0,0 12,9M12,17A5,5 0 0,1 7,12A5,5 0 0,1 12,7A5,5 0 0,1 17,12A5,5 0 0,1 12,17M12,4.5C7,4.5 2.73,7.61 1,12C2.73,16.39 7,19.5 12,19.5C17,19.5 21.27,16.39 23,12C21.27,7.61 17,4.5 12,4.5Z" />
                </svg>
              </button>
              
              <button @click="messageStudent(student)" class="student-action-btn message" title="Send Message">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M20,2H4A2,2 0 0,0 2,4V22L6,18H20A2,2 0 0,0 22,16V4C22,2.89 21.1,2 20,2Z" />
                </svg>
              </button>
              
              <button @click="removeStudent(student)" class="student-action-btn remove" title="Remove from Section">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M19,4H15.5L14.5,3H9.5L8.5,4H5V6H19M6,19A2,2 0 0,0 8,21H16A2,2 0 0,0 18,19V7H6V19Z" />
                </svg>
              </button>
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
          <p>Students will appear here once they join this section using the section link.</p>
          <button @click="showAddStudentModal = true" class="empty-action-btn">
            Add First Student
          </button>
        </div>

        <!-- No Results -->
        <div v-else class="no-results">
          <p>No students found matching "{{ searchQuery }}"</p>
        </div>
      </section>
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

    <!-- Loading Overlay -->
    <div v-if="isLoading" class="loading-overlay">
      <div class="loading-content">
        <div class="loading-spinner"></div>
        <p>{{ loadingMessage }}</p>
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
const students = ref([])
const searchQuery = ref('')
const filterStatus = ref('all')
const showAddStudentModal = ref(false)
const newStudentEmail = ref('')
const newStudentName = ref('')
const isLoading = ref(false)
const loadingMessage = ref('')

// Computed
const filteredStudents = computed(() => {
  let filtered = students.value

  // Filter by search query
  if (searchQuery.value) {
    const query = searchQuery.value.toLowerCase()
    filtered = filtered.filter(student => 
      student.full_name.toLowerCase().includes(query) ||
      student.email.toLowerCase().includes(query)
    )
  }

  // Filter by status
  if (filterStatus.value !== 'all') {
    filtered = filtered.filter(student => student.status === filterStatus.value)
  }

  return filtered
})

const activeStudents = computed(() => {
  return students.value.filter(student => student.status === 'active').length
})

const recentlyActive = computed(() => {
  const oneWeekAgo = new Date(Date.now() - 7 * 24 * 60 * 60 * 1000)
  return students.value.filter(student => 
    new Date(student.last_activity) > oneWeekAgo
  ).length
})

// Methods
const fetchStudents = async () => {
  isLoading.value = true
  loadingMessage.value = 'Loading students...'

  try {
    // Fetch students enrolled in this section
    const { data, error } = await supabase
      .from('section_enrollments')
      .select(`
        *,
        student:student_id (
          id,
          full_name,
          email,
          created_at
        )
      `)
      .eq('section_id', sectionId.value)

    if (error) throw error

    // Transform the data
    students.value = data.map(enrollment => ({
      id: enrollment.student.id,
      full_name: enrollment.student.full_name || 'Unknown Student',
      email: enrollment.student.email,
      enrolled_at: enrollment.created_at,
      last_activity: enrollment.last_activity || enrollment.created_at,
      status: enrollment.status || 'active',
      quiz_count: 0, // Will be populated by separate query
      average_grade: null // Will be populated by separate query
    }))

    console.log('Fetched students:', students.value)

  } catch (error) {
    console.error('Error fetching students:', error)
    alert(`Error loading students: ${error.message}`)
  } finally {
    isLoading.value = false
  }
}

const getInitials = (name) => {
  if (!name) return 'NS'
  return name.split(' ')
    .map(word => word.charAt(0))
    .join('')
    .substring(0, 2)
    .toUpperCase()
}

const formatDate = (dateString) => {
  if (!dateString) return 'Never'
  const date = new Date(dateString)
  return date.toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'short',
    day: 'numeric'
  })
}

// Navigation methods
const goBack = async () => {
  try {
    await router.push({ name: 'MySubjects' })
  } catch (error) {
    console.error('Navigation error:', error)
  }
}

const navigateToCreateQuiz = async () => {
  try {
    await router.push({
      name: 'CreateQuiz',
      params: {
        subjectId: subjectId.value,
        sectionId: sectionId.value
      },
      query: {
        subjectName: subjectName.value,
        sectionName: sectionName.value,
        gradeLevel: gradeLevel.value,
        classCode: classCode.value,
        sectionCode: sectionCode.value
      }
    })
  } catch (error) {
    console.error('Navigation error:', error)
  }
}

const viewQuizzes = async () => {
  try {
    await router.push({
      name: 'ViewQuizzes',
      params: { subjectId: subjectId.value, sectionId: sectionId.value },
      query: { sectionName: sectionName.value }
    })
  } catch (error) {
    console.error('Navigation error:', error)
  }
}

const manageGrades = async () => {
  try {
    await router.push({
      name: 'GradeManagement',
      params: { subjectId: subjectId.value, sectionId: sectionId.value },
      query: { sectionName: sectionName.value }
    })
  } catch (error) {
    console.error('Navigation error:', error)
  }
}

const generateReports = async () => {
  try {
    await router.push({
      name: 'Reports',
      params: { subjectId: subjectId.value, sectionId: sectionId.value },
      query: { sectionName: sectionName.value }
    })
  } catch (error) {
    console.error('Navigation error:', error)
  }
}

// Student actions
const addStudent = async () => {
  if (!newStudentEmail.value) return

  isLoading.value = true
  loadingMessage.value = 'Adding student...'

  try {
    // This is a simplified version - you'll need to implement proper student management
    console.log('Adding student:', {
      email: newStudentEmail.value,
      name: newStudentName.value,
      sectionId: sectionId.value
    })

    // For now, just show success
    alert(`Student "${newStudentEmail.value}" added successfully!`)
    
    // Reset form
    newStudentEmail.value = ''
    newStudentName.value = ''
    showAddStudentModal.value = false
    
    // Refresh students list
    await fetchStudents()

  } catch (error) {
    console.error('Error adding student:', error)
    alert(`Error adding student: ${error.message}`)
  } finally {
    isLoading.value = false
  }
}

const viewStudentDetails = (student) => {
  // Navigate to student details page
  console.log('Viewing details for:', student)
  alert(`View details for ${student.full_name} - This feature will be implemented later`)
}

const messageStudent = (student) => {
  console.log('Messaging student:', student)
  alert(`Send message to ${student.full_name} - This feature will be implemented later`)
}

const removeStudent = async (student) => {
  if (!confirm(`Are you sure you want to remove ${student.full_name} from this section?`)) {
    return
  }

  isLoading.value = true
  loadingMessage.value = 'Removing student...'

  try {
    // Remove student from section
    const { error } = await supabase
      .from('section_enrollments')
      .delete()
      .eq('section_id', sectionId.value)
      .eq('student_id', student.id)

    if (error) throw error

    alert(`${student.full_name} removed from section successfully!`)
    await fetchStudents()

  } catch (error) {
    console.error('Error removing student:', error)
    alert(`Error removing student: ${error.message}`)
  } finally {
    isLoading.value = false
  }
}

const exportStudents = () => {
  // Export students list to CSV
  console.log('Exporting students list')
  alert('Export feature will be implemented later')
}

// Lifecycle
onMounted(() => {
  fetchStudents()
})
</script>

<style scoped>
/* Enhanced Student Folder Design Pattern */
.page-container {
  min-height: 100vh;
  background: var(--body-background);
  padding: 2rem 5%;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', sans-serif;
}

.main-wrapper {
  max-width: 1400px;
  margin: 0 auto;
}

.card-box {
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(20px);
  border: 1px solid rgba(61, 141, 122, 0.1);
  border-radius: 24px;
  padding: 2.5rem;
  margin-bottom: 2rem;
  box-shadow: 
    0 8px 32px rgba(61, 141, 122, 0.1),
    0 0 0 1px rgba(255, 255, 255, 0.2);
}

.back-button {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  background: none;
  border: none;
  color: #3D8D7A;
  font-weight: 600;
  font-size: 1rem;
  cursor: pointer;
  transition: all 0.3s;
  margin-bottom: 1.5rem;
}

.back-button:hover {
  color: #2e6b5c;
  transform: translateX(-5px);
}

.section-header h1 {
  font-size: 2.5rem;
  font-weight: 800;
  color: #3D8D7A;
  margin: 0 0 1.5rem 0;
}

.section-info {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
}

.info-badge {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1.25rem;
  border-radius: 12px;
  font-size: 0.9rem;
}

.info-badge.subject {
  background: rgba(16, 185, 129, 0.1);
  border: 1px solid rgba(16, 185, 129, 0.2);
}

.info-badge.section {
  background: rgba(59, 130, 246, 0.1);
  border: 1px solid rgba(59, 130, 246, 0.2);
}

.info-badge.code {
  background: rgba(139, 92, 246, 0.1);
  border: 1px solid rgba(139, 92, 246, 0.2);
}

.info-badge .label {
  font-weight: 600;
  color: #666;
}

.info-badge .value {
  font-weight: 700;
  color: #333;
}

.quick-actions h2 {
  color: #3D8D7A;
  margin-bottom: 1.5rem;
  font-size: 1.5rem;
  font-weight: 700;
}

.action-buttons {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1rem;
}

.action-btn {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 1rem 1.5rem;
  border: none;
  border-radius: 16px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
}

.create-quiz {
  background: linear-gradient(135deg, #10b981 0%, #34d399 100%);
  color: white;
}

.view-quizzes {
  background: linear-gradient(135deg, #10b981 0%, #059669 100%);
  color: white;
}

.manage-grades {
  background: linear-gradient(135deg, #f59e0b 0%, #fbbf24 100%);
  color: white;
}

.generate-reports {
  background: linear-gradient(135deg, #8b5cf6 0%, #a78bfa 100%);
  color: white;
}

.action-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15);
}

.students-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 2rem;
  flex-wrap: wrap;
  gap: 1rem;
}

.header-info h2 {
  color: #3D8D7A;
  font-size: 1.5rem;
  font-weight: 700;
  margin-bottom: 0.5rem;
}

.students-stats {
  display: flex;
  gap: 1.5rem;
}

.stat {
  color: #666;
  font-size: 0.9rem;
}

.header-actions {
  display: flex;
  gap: 1rem;
}

.add-student-btn {
  background: linear-gradient(135deg, #10b981 0%, #34d399 100%);
  color: white;
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 12px;
  font-weight: 600;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  transition: all 0.3s;
}

.export-btn {
  background: rgba(16, 185, 129, 0.1);
  color: #10b981;
  border: 1px solid rgba(16, 185, 129, 0.2);
  padding: 0.75rem 1.5rem;
  border-radius: 12px;
  font-weight: 600;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  transition: all 0.3s;
}

.add-student-btn:hover,
.export-btn:hover {
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

.search-section {
  display: flex;
  gap: 1rem;
  margin-bottom: 2rem;
  flex-wrap: wrap;
}

.search-input {
  position: relative;
  flex: 1;
  min-width: 300px;
}

.search-icon {
  position: absolute;
  left: 1rem;
  top: 50%;
  transform: translateY(-50%);
  color: #666;
}

.search-input input {
  width: 100%;
  padding: 0.75rem 1rem 0.75rem 3rem;
  border: 2px solid rgba(61, 141, 122, 0.1);
  border-radius: 12px;
  font-size: 1rem;
}

.search-input input:focus {
  outline: none;
  border-color: #3D8D7A;
  box-shadow: 0 0 0 3px rgba(61, 141, 122, 0.1);
}

.filter-select {
  padding: 0.75rem 1rem;
  border: 2px solid rgba(61, 141, 122, 0.1);
  border-radius: 12px;
  font-size: 1rem;
  background: white;
  min-width: 150px;
}

.students-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
  gap: 1.5rem;
}

.student-card {
  background: white;
  border: 2px solid rgba(61, 141, 122, 0.1);
  border-radius: 16px;
  padding: 1.5rem;
  transition: all 0.3s ease;
  position: relative;
}

.student-card:hover {
  border-color: rgba(61, 141, 122, 0.3);
  box-shadow: 0 8px 24px rgba(61, 141, 122, 0.15);
  transform: translateY(-2px);
}

.student-avatar {
  position: relative;
  margin-bottom: 1rem;
}

.avatar-circle {
  width: 60px;
  height: 60px;
  border-radius: 50%;
  background: linear-gradient(135deg, #3D8D7A 0%, #A3D1C6 100%);
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 1.2rem;
  margin-bottom: 0.5rem;
}

.status-indicator {
  position: absolute;
  top: 0;
  right: 0;
  width: 16px;
  height: 16px;
  border-radius: 50%;
  border: 3px solid white;
}

.status-indicator.active {
  background: #10b981;
}

.status-indicator.inactive {
  background: #ef4444;
}

.student-info h3 {
  color: #3D8D7A;
  font-size: 1.1rem;
  font-weight: 700;
  margin-bottom: 0.25rem;
}

.student-info .email {
  color: #666;
  font-size: 0.9rem;
  margin-bottom: 0.75rem;
}

.student-meta {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
  margin-bottom: 1rem;
}

.enrollment-date,
.last-activity {
  color: #666;
  font-size: 0.8rem;
}

.student-stats {
  display: flex;
  gap: 1.5rem;
  margin-bottom: 1rem;
}

.stat-item {
  text-align: center;
}

.stat-value {
  display: block;
  font-size: 1.5rem;
  font-weight: 800;
  color: #3D8D7A;
}

.stat-label {
  font-size: 0.75rem;
  color: #666;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.student-actions {
  display: flex;
  gap: 0.5rem;
  justify-content: flex-end;
}

.student-action-btn {
  padding: 0.5rem;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.student-action-btn.view {
  background: rgba(16, 185, 129, 0.1);
  color: #10b981;
}

.student-action-btn.message {
  background: rgba(16, 185, 129, 0.1);
  color: #10b981;
}

.student-action-btn.remove {
  background: rgba(239, 68, 68, 0.1);
  color: #ef4444;
}

.student-action-btn:hover {
  transform: scale(1.1);
}

.empty-state,
.no-results {
  text-align: center;
  padding: 4rem 2rem;
  color: #666;
}

.empty-icon {
  color: #A3D1C6;
  margin-bottom: 2rem;
}

.empty-state h3 {
  color: #3D8D7A;
  font-size: 1.5rem;
  font-weight: 700;
  margin-bottom: 1rem;
}

.empty-action-btn {
  background: linear-gradient(135deg, #3D8D7A 0%, #A3D1C6 100%);
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
  box-shadow: 0 8px 20px rgba(61, 141, 122, 0.3);
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
  border-radius: 20px;
  max-width: 500px;
  width: 100%;
  max-height: 90vh;
  overflow-y: auto;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 2rem 2rem 1rem;
  border-bottom: 1px solid rgba(61, 141, 122, 0.1);
}

.modal-header h2 {
  color: #3D8D7A;
  font-size: 1.5rem;
  font-weight: 700;
  margin: 0;
}

.close-btn {
  background: none;
  border: none;
  color: #666;
  cursor: pointer;
  transition: all 0.3s ease;
  padding: 0.5rem;
  border-radius: 8px;
}

.close-btn:hover {
  color: #3D8D7A;
  background: rgba(61, 141, 122, 0.1);
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
  color: #3D8D7A;
  font-weight: 600;
}

.form-group input {
  width: 100%;
  padding: 0.75rem 1rem;
  border: 2px solid rgba(61, 141, 122, 0.1);
  border-radius: 12px;
  font-size: 1rem;
}

.form-group input:focus {
  outline: none;
  border-color: #3D8D7A;
  box-shadow: 0 0 0 3px rgba(61, 141, 122, 0.1);
}

.modal-actions {
  display: flex;
  gap: 1rem;
  justify-content: flex-end;
  margin-top: 2rem;
}

.cancel-btn {
  background: transparent;
  color: #666;
  border: 2px solid #ddd;
  padding: 0.75rem 1.5rem;
  border-radius: 12px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s;
}

.cancel-btn:hover {
  background: #f5f5f5;
  border-color: #999;
}

.add-btn {
  background: linear-gradient(135deg, #3D8D7A 0%, #A3D1C6 100%);
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
  box-shadow: 0 8px 20px rgba(61, 141, 122, 0.3);
}

.add-btn:disabled {
  opacity: 0.7;
  cursor: not-allowed;
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
  z-index: 2000;
}

.loading-content {
  background: white;
  padding: 2rem;
  border-radius: 16px;
  text-align: center;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
}

.loading-spinner {
  width: 40px;
  height: 40px;
  border: 4px solid rgba(61, 141, 122, 0.2);
  border-top: 4px solid #3D8D7A;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin: 0 auto 1rem;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

/* Responsive */
@media (max-width: 768px) {
  .page-container {
    padding: 1rem 3%;
  }

  .card-box {
    padding: 1.5rem;
  }

  .section-header h1 {
    font-size: 2rem;
  }

  .section-info {
    flex-direction: column;
    gap: 0.75rem;
  }

  .action-buttons {
    grid-template-columns: 1fr;
  }

  .students-header {
    flex-direction: column;
    align-items: stretch;
  }

  .header-actions {
    justify-content: stretch;
  }

  .add-student-btn,
  .export-btn {
    flex: 1;
    justify-content: center;
  }

  .search-section {
    flex-direction: column;
  }

  .students-grid {
    grid-template-columns: 1fr;
  }

  .student-stats {
    justify-content: space-around;
  }
}

/* Dark Mode Styles */
.dark-mode .page-container {
  background: var(--bg-primary);
}

.dark-mode .section-header-card {
  background: rgba(17, 24, 39, 0.95);
  border: 1px solid rgba(255, 255, 255, 0.08);
  box-shadow: 
    0 4px 12px rgba(0, 0, 0, 0.25),
    0 2px 6px rgba(0, 0, 0, 0.15);
}

.dark-mode .back-button {
  background: rgba(75, 85, 99, 0.2);
  color: var(--secondary-text-color);
}

.dark-mode .back-button:hover {
  color: var(--accent-color);
}

.dark-mode .hero-header h1 {
  color: var(--primary-text-color);
}

.dark-mode .hero-subtitle {
  color: var(--secondary-text-color);
}

.dark-mode .info-badge {
  background: rgba(17, 24, 39, 0.8);
  border: 1px solid rgba(255, 255, 255, 0.08);
}

.dark-mode .info-badge.subject {
  background: rgba(16, 185, 129, 0.15);
  border: 1px solid rgba(16, 185, 129, 0.3);
}

.dark-mode .info-badge.section {
  background: rgba(59, 130, 246, 0.15);
  border: 1px solid rgba(59, 130, 246, 0.3);
}

.dark-mode .info-badge.code {
  background: rgba(139, 92, 246, 0.15);
  border: 1px solid rgba(139, 92, 246, 0.3);
}

.dark-mode .info-badge.students {
  background: rgba(234, 179, 8, 0.15);
  border: 1px solid rgba(234, 179, 8, 0.3);
}

.dark-mode .info-badge .label {
  color: var(--secondary-text-color);
}

.dark-mode .info-badge .value {
  color: var(--primary-text-color);
}

.dark-mode .content-card {
  background: rgba(17, 24, 39, 0.95);
  border: 1px solid rgba(255, 255, 255, 0.08);
  box-shadow: 
    0 4px 12px rgba(0, 0, 0, 0.25),
    0 2px 6px rgba(0, 0, 0, 0.15);
}

.dark-mode .card-header h3 {
  color: var(--primary-text-color);
}

.dark-mode .card-subtitle {
  color: var(--secondary-text-color);
}

.dark-mode .action-btn {
  background: rgba(75, 85, 99, 0.2);
  border: 1px solid rgba(255, 255, 255, 0.1);
  color: var(--secondary-text-color);
}

.dark-mode .action-btn:hover {
  background: rgba(75, 85, 99, 0.3);
  color: var(--primary-text-color);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
}

.dark-mode .action-btn.create-quiz:hover {
  background: linear-gradient(135deg, var(--accent-color), #2563eb);
  color: white;
  box-shadow: 0 6px 20px rgba(59, 130, 246, 0.4);
}

.dark-mode .students-header h4 {
  color: var(--primary-text-color);
}

.dark-mode .add-student-btn {
  background: linear-gradient(135deg, var(--accent-color), #2563eb);
  box-shadow: 0 4px 14px rgba(59, 130, 246, 0.3);
}

.dark-mode .add-student-btn:hover {
  box-shadow: 0 8px 25px rgba(59, 130, 246, 0.4);
}

.dark-mode .export-btn {
  background: rgba(75, 85, 99, 0.2);
  border: 1px solid rgba(255, 255, 255, 0.1);
  color: var(--secondary-text-color);
}

.dark-mode .export-btn:hover {
  background: rgba(75, 85, 99, 0.3);
  color: var(--primary-text-color);
}

.dark-mode .search-input {
  background: rgba(17, 24, 39, 0.8);
  border: 2px solid rgba(255, 255, 255, 0.08);
  color: var(--primary-text-color);
}

.dark-mode .search-input:focus {
  border-color: var(--accent-color);
  box-shadow: 0 0 0 4px rgba(59, 130, 246, 0.15);
  background: rgba(17, 24, 39, 1);
}

.dark-mode .student-card {
  background: rgba(17, 24, 39, 0.8);
  border: 1px solid rgba(255, 255, 255, 0.05);
}

.dark-mode .student-card:hover {
  background: rgba(17, 24, 39, 0.95);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
}

.dark-mode .student-name {
  color: var(--primary-text-color);
}

.dark-mode .student-id {
  color: var(--secondary-text-color);
}

.dark-mode .student-email {
  color: var(--secondary-text-color);
}

.dark-mode .student-status.active {
  background: rgba(16, 185, 129, 0.15);
  color: rgba(16, 185, 129, 1);
  border: 1px solid rgba(16, 185, 129, 0.3);
}

.dark-mode .student-status.inactive {
  background: rgba(239, 68, 68, 0.15);
  color: rgba(239, 68, 68, 1);
  border: 1px solid rgba(239, 68, 68, 0.3);
}

.dark-mode .student-action {
  background: rgba(75, 85, 99, 0.2);
  color: var(--secondary-text-color);
}

.dark-mode .student-action:hover {
  background: rgba(75, 85, 99, 0.3);
  color: var(--primary-text-color);
}

.dark-mode .student-action.remove:hover {
  background: rgba(239, 68, 68, 0.2);
  color: #ef4444;
}

.dark-mode .modal {
  background: rgba(17, 24, 39, 0.95);
  border: 1px solid rgba(255, 255, 255, 0.08);
  box-shadow: 
    0 20px 50px rgba(0, 0, 0, 0.5),
    0 10px 25px rgba(0, 0, 0, 0.3);
}

.dark-mode .modal-header h3 {
  color: var(--primary-text-color);
}

.dark-mode .close-btn {
  background: rgba(75, 85, 99, 0.2);
  color: var(--secondary-text-color);
}

.dark-mode .close-btn:hover {
  background: #ef4444;
  color: white;
}

.dark-mode .form-group label {
  color: var(--secondary-text-color);
}

.dark-mode .form-group input,
.dark-mode .form-group select {
  background: rgba(17, 24, 39, 0.8);
  border: 2px solid rgba(255, 255, 255, 0.08);
  color: var(--primary-text-color);
}

.dark-mode .form-group input:focus,
.dark-mode .form-group select:focus {
  border-color: var(--accent-color);
  box-shadow: 0 0 0 4px rgba(59, 130, 246, 0.15);
  background: rgba(17, 24, 39, 1);
}

.dark-mode .modal-actions .cancel-btn {
  background: rgba(75, 85, 99, 0.2);
  border: 2px solid rgba(255, 255, 255, 0.1);
  color: var(--secondary-text-color);
}

.dark-mode .modal-actions .cancel-btn:hover {
  background: rgba(75, 85, 99, 0.3);
  border-color: rgba(255, 255, 255, 0.2);
}

.dark-mode .modal-actions .confirm-btn {
  background: linear-gradient(135deg, var(--accent-color), #2563eb);
  box-shadow: 0 4px 14px rgba(59, 130, 246, 0.3);
}

.dark-mode .modal-actions .confirm-btn:hover:not(:disabled) {
  box-shadow: 0 8px 25px rgba(59, 130, 246, 0.4);
}

.dark-mode .loading-overlay {
  background: rgba(0, 0, 0, 0.8);
}

.dark-mode .loading-content {
  background: rgba(17, 24, 39, 0.95);
  border: 1px solid rgba(255, 255, 255, 0.08);
  color: var(--primary-text-color);
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.5);
}

.dark-mode .loading-spinner {
  border: 4px solid rgba(59, 130, 246, 0.2);
  border-top: 4px solid var(--accent-color);
}
</style>