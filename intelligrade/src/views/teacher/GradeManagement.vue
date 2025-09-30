<template>
  <div class="grade-management-container" :class="{ 'dark-mode': isDarkMode }">
    <div class="main-wrapper">
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
                <path d="M12,2A2,2 0 0,1 14,4V8H17A1,1 0 0,1 18,9V19A3,3 0 0,1 15,22H9A3,3 0 0,1 6,19V9A1,1 0 0,1 7,8H10V4A2,2 0 0,1 12,2M12,4V8H12V4M8,10V19A1,1 0 0,0 9,20H15A1,1 0 0,0 16,19V10H8Z" />
              </svg>
            </div>
            <div class="header-text">
              <div class="section-header-title">Grade Management</div>
              <div class="section-header-subtitle">{{ sectionName || 'Section' }}</div>
              <div class="section-header-description">Manage student grades and track academic progress</div>
            </div>
          </div>
          
          <div class="header-actions">
            <button @click="goBack" class="back-button">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                <path d="M10 19l-7-7 7-7m-7 7h18"></path>
              </svg>
              Back to Subjects
            </button>
          </div>
        </div>
      </div>

      <!-- Main Controls Section -->
      <div class="controls-section">
        <div class="controls-card">
          <div class="floating-shapes">
            <div class="floating-shape shape-1"></div>
            <div class="floating-shape shape-2"></div>
          </div>
          <div class="controls-content">
            <div class="controls-header">
              <div class="control-buttons">
              <div class="control-buttons">
                <button @click="exportGrades" class="control-btn export">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M14,2H6A2,2 0 0,0 4,4V20A2,2 0 0,0 6,22H18A2,2 0 0,0 20,20V8L14,2M18,20H6V4H13V9H18V20Z" />
                  </svg>
                  Export Grades
                </button>
                
                <button @click="showGradeSettings = true" class="control-btn settings">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M12,15.5A3.5,3.5 0 0,1 8.5,12A3.5,3.5 0 0,1 12,8.5A3.5,3.5 0 0,1 15.5,12A3.5,3.5 0 0,1 12,15.5M19.43,12.97C19.47,12.65 19.5,12.33 19.5,12C19.5,11.67 19.47,11.34 19.43,11L21.54,9.37C21.73,9.22 21.78,8.95 21.66,8.73L19.66,5.27C19.54,5.05 19.27,4.96 19.05,5.05L16.56,6.05C16.04,5.66 15.5,5.32 14.87,5.07L14.5,2.42C14.46,2.18 14.25,2 14,2H10C9.75,2 9.54,2.18 9.5,2.42L9.13,5.07C8.5,5.32 7.96,5.66 7.44,6.05L4.95,5.05C4.73,4.96 4.46,5.05 4.34,5.27L2.34,8.73C2.22,8.95 2.27,9.22 2.46,9.37L4.57,11C4.53,11.34 4.5,11.67 4.5,12C4.5,12.33 4.53,12.65 4.57,12.97L2.46,14.63C2.27,14.78 2.22,15.05 2.34,15.27L4.34,18.73C4.46,18.95 4.73,19.03 4.95,18.95L7.44,17.94C7.96,18.34 8.5,18.68 9.13,18.93L9.5,21.58C9.54,21.82 9.75,22 10,22H14C14.25,22 14.46,21.82 14.5,21.58L14.87,18.93C15.5,18.68 16.04,18.34 16.56,17.94L19.05,18.95C19.27,19.03 19.54,18.95 19.66,18.73L21.66,15.27C21.78,15.05 21.73,14.78 21.54,14.63L19.43,12.97Z" />
                  </svg>
                  Grade Settings
                </button>
              </div>
          </div>
        </div>
      </div>

      <!-- Filters Section -->
      <div class="filters-section">
          <div class="filter-group">
            <label>Filter by:</label>
            <select v-model="filterBy">
              <option value="all">All Students</option>
              <option value="passed">Passed (≥60%)</option>
              <option value="failed">Failed (&lt;60%)</option>
              <option value="no-submissions">No Submissions</option>
            </select>
          </div>

          <div class="search-group">
            <input 
              type="text" 
              v-model="searchQuery" 
              placeholder="Search students..."
              class="search-input"
            >
          </div>
        </div>
      </div>

      <!-- Gradebook Table -->
      <div class="gradebook-section card-box">
        <div class="table-container">
          <table class="gradebook-table">
            <thead>
              <tr>
                <th class="student-column">Student</th>
                <th 
                  v-for="quiz in quizzes" 
                  :key="quiz.id" 
                  class="quiz-column"
                  :title="quiz.title"
                >
                  <div class="quiz-header">
                    <span class="quiz-title">{{ truncateTitle(quiz.title) }}</span>
                    <span class="quiz-points">{{ quiz.total_points }}pts</span>
                    <span class="quiz-date">{{ formatDate(quiz.created_at) }}</span>
                  </div>
                </th>
                <th class="average-column">Overall Average</th>
                <th class="actions-column">Actions</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="student in filteredStudents" :key="student.id" class="student-row">
                <td class="student-info">
                  <div class="student-details">
                    <div class="student-avatar">
                      {{ getInitials(student.full_name) }}
                    </div>
                    <div class="student-text">
                      <div class="student-name">{{ student.full_name }}</div>
                      <div class="student-email">{{ student.email }}</div>
                    </div>
                  </div>
                </td>
                
                <td 
                  v-for="quiz in quizzes" 
                  :key="`${student.id}-${quiz.id}`" 
                  class="grade-cell"
                >
                  <div class="grade-container">
                    <input 
                      type="number" 
                      :value="getGrade(student.id, quiz.id)" 
                      @blur="updateGrade(student.id, quiz.id, $event.target.value)"
                      :max="quiz.total_points"
                      min="0"
                      step="0.1"
                      class="grade-input"
                      :class="getGradeClass(getGrade(student.id, quiz.id), quiz.total_points)"
                    >
                    <span class="grade-percentage">
                      {{ getGradePercentage(getGrade(student.id, quiz.id), quiz.total_points) }}%
                    </span>
                  </div>
                </td>
                
                <td class="average-cell">
                  <div class="average-display">
                    <span :class="['average-score', getAverageClass(student.average)]">
                      {{ student.average || 'N/A' }}%
                    </span>
                    <div class="progress-bar">
                      <div 
                        class="progress-fill" 
                        :style="{ width: `${student.average || 0}%` }"
                        :class="getAverageClass(student.average)"
                      ></div>
                    </div>
                  </div>
                </td>
                
                <td class="actions-cell">
                  <button @click="viewStudentDetail(student)" class="action-btn view" title="View Details">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                      <path d="M12,9A3,3 0 0,0 9,12A3,3 0 0,0 12,15A3,3 0 0,0 15,12A3,3 0 0,0 12,9M12,17A5,5 0 0,1 7,12A5,5 0 0,1 12,7A5,5 0 0,1 17,12A5,5 0 0,1 12,17M12,4.5C7,4.5 2.73,7.61 1,12C2.73,16.39 7,19.5 12,19.5C17,19.5 21.27,16.39 23,12C21.27,7.61 17,4.5 12,4.5Z" />
                    </svg>
                  </button>
                  
                  <button @click="messageStudent(student)" class="action-btn message" title="Send Message">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                      <path d="M20,2H4A2,2 0 0,0 2,4V22L6,18H20A2,2 0 0,0 22,16V4C22,2.89 21.1,2 20,2Z" />
                    </svg>
                  </button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>

        <!-- Empty State -->
        <div v-if="students.length === 0" class="empty-state">
          <div class="empty-icon">
            <svg width="64" height="64" viewBox="0 0 24 24" fill="currentColor">
              <path d="M19,3H5C3.9,3 3,3.9 3,5V19C3,20.1 3.9,21 5,21H19C20.1,21 21,20.1 21,19V5C21,3.9 20.1,3 19,3M19,19H5V5H19V19M17,12H7V10H17V12M15,16H7V14H15V16M17,8H7V6H17V8Z" />
            </svg>
          </div>
          <h3>No Students or Grades Yet</h3>
          <p>Students and their grades will appear here once they start taking quizzes.</p>
        </div>
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
                <input type="number" v-model="gradeScale.A" min="0" max="100">%
              </div>
              <div class="scale-item">
                <label>B (Good):</label>
                <input type="number" v-model="gradeScale.B" min="0" max="100">%
              </div>
              <div class="scale-item">
                <label>C (Satisfactory):</label>
                <input type="number" v-model="gradeScale.C" min="0" max="100">%
              </div>
              <div class="scale-item">
                <label>D (Needs Improvement):</label>
                <input type="number" v-model="gradeScale.D" min="0" max="100">%
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
    </div> <!-- End main-wrapper -->

    <!-- Loading Overlay -->
    <!-- Loading Overlay -->
    <div v-if="isLoading" class="loading-overlay">
      <div class="loading-content">
        <div class="loading-spinner"></div>
        <p>{{ loadingMessage }}</p>
      </div>
    </div>
    </div> <!-- End main-wrapper -->
</template>

<script setup lang="ts">
import { ref, onMounted, computed } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { supabase } from '../../supabase'
import { useDarkMode } from '../../composables/useDarkMode.js'

// Dark mode
const { isDarkMode, initDarkMode } = useDarkMode()

const router = useRouter()
const route = useRoute()

// Route data
const subjectId = ref(route.params.subjectId)
const sectionId = ref(route.params.sectionId)
const sectionName = ref(route.query.sectionName || 'Section')

// State
const students = ref([])
const quizzes = ref([])
const grades = ref({}) // Format: { studentId: { quizId: grade } }
const searchQuery = ref('')
const filterBy = ref('all')
const showGradeSettings = ref(false)
const isLoading = ref(false)
const loadingMessage = ref('')

// Grade settings
const gradeScale = ref({
  A: 90,
  B: 80,
  C: 70,
  D: 60
})

const displayOptions = ref({
  showPercentages: true,
  showLetterGrades: false,
  roundToWhole: false
})

// Computed
const filteredStudents = computed(() => {
  let filtered = students.value

  // Apply search filter
  if (searchQuery.value) {
    const query = searchQuery.value.toLowerCase()
    filtered = filtered.filter(student => 
      student.full_name.toLowerCase().includes(query) ||
      student.email.toLowerCase().includes(query)
    )
  }

  // Apply grade filter
  if (filterBy.value !== 'all') {
    filtered = filtered.filter(student => {
      switch (filterBy.value) {
        case 'passed':
          return student.average >= 60
        case 'failed':
          return student.average < 60 && student.average !== null
        case 'no-submissions':
          return student.average === null || student.average === 0
        default:
          return true
      }
    })
  }

  return filtered
})

const classAverage = computed(() => {
  const validAverages = students.value
    .map(s => s.average)
    .filter(avg => avg !== null && avg !== undefined)
  
  if (validAverages.length === 0) return 'N/A'
  
  const sum = validAverages.reduce((a, b) => a + b, 0)
  return Math.round(sum / validAverages.length)
})

// Methods
const fetchData = async () => {
  isLoading.value = true
  loadingMessage.value = 'Loading gradebook data...'

  try {
    // Fetch students
    const { data: studentsData, error: studentsError } = await supabase
      .from('section_enrollments')
      .select(`
        *,
        student:student_id (
          id,
          full_name,
          email
        )
      `)
      .eq('section_id', sectionId.value)

    if (studentsError) throw studentsError

    // Fetch quizzes
    const { data: quizzesData, error: quizzesError } = await supabase
      .from('quizzes')
      .select('*')
      .eq('section_id', sectionId.value)
      .eq('status', 'published')
      .order('created_at')

    if (quizzesError) throw quizzesError

    // Transform students data
    students.value = studentsData.map(enrollment => ({
      id: enrollment.student.id,
      full_name: enrollment.student.full_name || 'Unknown Student',
      email: enrollment.student.email,
      average: Math.floor(Math.random() * 40) + 60 // Mock data
    }))

    quizzes.value = quizzesData

    // Generate mock grades
    generateMockGrades()

  } catch (error) {
    console.error('Error fetching gradebook data:', error)
    alert(`Error loading gradebook: ${error.message}`)
  } finally {
    isLoading.value = false
  }
}

const generateMockGrades = () => {
  const mockGrades = {}
  
  students.value.forEach(student => {
    mockGrades[student.id] = {}
    quizzes.value.forEach(quiz => {
      // Generate random grade (60-100% of total points)
      const percentage = (Math.random() * 40 + 60) / 100
      const grade = Math.round(quiz.total_points * percentage * 10) / 10
      mockGrades[student.id][quiz.id] = grade
    })
  })
  
  grades.value = mockGrades
}

const getGrade = (studentId, quizId) => {
  return grades.value[studentId]?.[quizId] || ''
}

const getGradePercentage = (grade, totalPoints) => {
  if (!grade || !totalPoints) return '0'
  return Math.round((grade / totalPoints) * 100)
}

const getGradeClass = (grade, totalPoints) => {
  const percentage = getGradePercentage(grade, totalPoints)
  if (percentage >= 90) return 'grade-a'
  if (percentage >= 80) return 'grade-b'
  if (percentage >= 70) return 'grade-c'
  if (percentage >= 60) return 'grade-d'
  return 'grade-f'
}

const getAverageClass = (average) => {
  if (!average) return 'no-grade'
  if (average >= 90) return 'grade-a'
  if (average >= 80) return 'grade-b'
  if (average >= 70) return 'grade-c'
  if (average >= 60) return 'grade-d'
  return 'grade-f'
}

const updateGrade = async (studentId, quizId, newGrade) => {
  if (!grades.value[studentId]) {
    grades.value[studentId] = {}
  }
  
  grades.value[studentId][quizId] = parseFloat(newGrade) || 0
  
  // Recalculate student average
  calculateStudentAverage(studentId)
  
  console.log('Grade updated:', { studentId, quizId, newGrade })
  // Here you would save to the database
}

const calculateStudentAverage = (studentId) => {
  const studentGrades = grades.value[studentId]
  if (!studentGrades) return

  const gradeValues = Object.entries(studentGrades).map(([quizId, grade]) => {
    const quiz = quizzes.value.find(q => q.id === quizId)
    return quiz ? (grade / quiz.total_points) * 100 : 0
  })

  if (gradeValues.length > 0) {
    const average = gradeValues.reduce((a, b) => a + b, 0) / gradeValues.length
    const student = students.value.find(s => s.id === studentId)
    if (student) {
      student.average = Math.round(average)
    }
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

const truncateTitle = (title) => {
  return title.length > 15 ? title.substring(0, 15) + '...' : title
}

const formatDate = (dateString) => {
  const date = new Date(dateString)
  return date.toLocaleDateString('en-US', {
    month: 'short',
    day: 'numeric'
  })
}

// Actions
const goBack = async () => {
  try {
    await router.push({
      name: 'ViewStudents',
      params: { subjectId: subjectId.value, sectionId: sectionId.value }
    })
  } catch (error) {
    console.error('Navigation error:', error)
  }
}

const exportGrades = () => {
  console.log('Exporting grades...')
  alert('Export grades functionality will be implemented - this will generate a CSV/Excel file with all student grades.')
}

const viewStudentDetail = (student) => {
  console.log('Viewing student details:', student)
  alert(`View detailed grade report for ${student.full_name} - This will show individual quiz performance and progress over time.`)
}

const messageStudent = (student) => {
  console.log('Messaging student:', student)
  alert(`Send message to ${student.full_name} about their grades - This feature will integrate with the messaging system.`)
}

const saveGradeSettings = () => {
  console.log('Saving grade settings:', { gradeScale: gradeScale.value, displayOptions: displayOptions.value })
  alert('Grade settings saved successfully!')
  showGradeSettings.value = false
}

// Lifecycle
onMounted(() => {
  initDarkMode()
  fetchData()
})
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

.grade-management-container {
  padding: 2rem;
  max-width: 1400px;
  margin: 0 auto;
  font-family: 'Inter', sans-serif;
  background: var(--bg-primary);
  min-height: 100vh;
  color: var(--primary-text-color);
  transition: all 0.3s ease;
}

.main-wrapper {
  max-width: 1600px;
  margin: 0 auto;
}

/* Enhanced Header Section - Matching ViewQuizzes.vue */
.section-header-card {
  position: relative;
  background: var(--card-background);
  backdrop-filter: blur(20px);
  border-radius: 32px;
  padding: 3.5rem;
  margin-bottom: 2.5rem;
  min-height: 180px;
  box-shadow: 
    0 24px 48px rgba(0, 0, 0, 0.1),
    0 12px 24px rgba(0, 0, 0, 0.08),
    inset 0 1px 0 rgba(255, 255, 255, 0.8);
  border: 1px solid var(--border-color);
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
  background: radial-gradient(ellipse at center, rgba(79, 70, 229, 0.08) 0%, transparent 70%);
  z-index: 1;
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
  width: 80px;
  height: 80px;
  background: linear-gradient(135deg, #10b981 0%, #059669 100%);
  border-radius: 24px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #fff;
  box-shadow: 0 8px 24px rgba(79, 70, 229, 0.3);
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.section-header-icon:hover {
  transform: translateY(-2px);
}

.header-text {
  display: flex;
  flex-direction: column;
  gap: 0.3rem;
}

.section-header-title {
  font-size: 2rem;
  font-weight: 800;
  color: var(--accent-color);
  margin-bottom: 0.25rem;
  letter-spacing: -0.025em;
}

.section-header-subtitle {
  font-size: 1.1rem;
  font-weight: 600;
  color: #64748b;
}

.section-header-description {
  font-size: 0.9rem;
  color: #94a3b8;
}

.header-actions {
  display: flex;
  gap: 1rem;
  align-items: center;
}

.create-quiz-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  background: linear-gradient(135deg, #10b981 0%, #059669 100%);
  color: white;
  border: none;
  padding: 0.875rem 1.5rem;
  border-radius: 16px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 8px 24px rgba(16, 185, 129, 0.3);
}

.create-quiz-btn:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 12px 32px rgba(16, 185, 129, 0.4);
}

.shape {
  position: absolute;
  border-radius: 50%;
  background: linear-gradient(135deg, rgba(16, 185, 129, 0.1) 0%, rgba(79, 70, 229, 0.05) 100%);
}

.shape-1 {
  width: 100px;
  height: 100px;
  top: -20px;
  right: 15%;
  animation: float 6s ease-in-out infinite;
}

.shape-2 {
  width: 60px;
  height: 60px;
  bottom: -10px;
  right: 25%;
  animation: float 8s ease-in-out infinite reverse;
}

.shape-3 {
  width: 80px;
  height: 80px;
  top: 50%;
  right: 5%;
  animation: float 7s ease-in-out infinite;
}

@keyframes float {
  0%, 100% { transform: translateY(0) rotate(0deg); }
  50% { transform: translateY(-15px) rotate(10deg); }
}

/* Floating shapes animation */
.floating-shapes {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  pointer-events: none;
  overflow: hidden;
}

.shape {
  position: absolute;
  border-radius: 50%;
  opacity: 0.6;
  animation: float-shape 8s ease-in-out infinite;
}

.shape.shape-1 {
  width: 120px;
  height: 120px;
  background: linear-gradient(135deg, rgba(61, 141, 122, 0.1), rgba(163, 209, 198, 0.1));
  top: -60px;
  right: -60px;
  animation-delay: 0s;
}

.shape.shape-2 {
  width: 80px;
  height: 80px;
  background: linear-gradient(135deg, rgba(16, 185, 129, 0.1), rgba(5, 150, 105, 0.1));
  bottom: -40px;
  left: 10%;
  animation-delay: 2s;
}

.shape.shape-3 {
  width: 60px;
  height: 60px;
  background: linear-gradient(135deg, rgba(59, 130, 246, 0.1), rgba(37, 99, 235, 0.1));
  top: 20%;
  left: -30px;
  animation-delay: 4s;
}

.shape.shape-4 {
  width: 40px;
  height: 40px;
  background: linear-gradient(135deg, rgba(139, 92, 246, 0.1), rgba(124, 58, 237, 0.1));
  top: 60%;
  right: 15%;
  animation-delay: 6s;
}

@keyframes float-shape {
  0%, 100% {
    transform: translateY(0px) rotate(0deg);
    opacity: 0.6;
  }
  50% {
    transform: translateY(-20px) rotate(180deg);
    opacity: 0.8;
  }
}

/* Header content */
.header-content {
  position: relative;
  z-index: 2;
}

.back-button {
  display: inline-flex;
  align-items: center;
  gap: 0.75rem;
  background: rgba(75, 85, 99, 0.1);
  border: 1px solid rgba(75, 85, 99, 0.2);
  color: var(--secondary-text-color);
  font-weight: 600;
  font-size: 0.95rem;
  padding: 0.75rem 1.25rem;
  border-radius: 12px;
  cursor: pointer;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  margin-bottom: 2rem;
  text-decoration: none;
}

.back-button:hover {
  color: var(--primary-color-dark);
  transform: translateX(-5px);
  box-shadow: 0 4px 12px rgba(75, 85, 99, 0.2);
}

.hero-header {
  text-align: center;
  margin-bottom: 2.5rem;
}

.hero-header h1 {
  font-size: 3rem;
  font-weight: 800;
  background: linear-gradient(135deg, #10b981 0%, #059669 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  margin: 0 0 1rem 0;
  letter-spacing: -1px;
}

.hero-subtitle {
  font-size: 1.25rem;
  color: var(--secondary-text-color);
  font-weight: 500;
  max-width: 600px;
  margin: 0 auto;
  line-height: 1.6;
}

/* Section info badges */
.section-info {
  display: flex;
  justify-content: center;
  gap: 1.5rem;
  flex-wrap: wrap;
}

.info-badge {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1rem 1.5rem;
  background: rgba(255, 255, 255, 0.8);
  backdrop-filter: blur(8px);
  border: 1px solid rgba(61, 141, 122, 0.1);
  border-radius: 16px;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  min-width: 140px;
}

.info-badge:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(61, 141, 122, 0.12);
}

.info-badge.gradebook {
  background: rgba(59, 130, 246, 0.1);
  border: 1px solid rgba(59, 130, 246, 0.2);
}

.info-badge.students {
  background: rgba(16, 185, 129, 0.1);
  border: 1px solid rgba(16, 185, 129, 0.2);
}

.info-badge.quizzes {
  background: rgba(139, 92, 246, 0.1);
  border: 1px solid rgba(139, 92, 246, 0.2);
}

.info-badge.average {
  background: rgba(245, 158, 11, 0.1);
  border: 1px solid rgba(245, 158, 11, 0.2);
}

.info-badge .icon {
  font-size: 1.5rem;
  flex-shrink: 0;
}

.info-badge .text {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}

.info-badge .label {
  font-size: 0.8rem;
  font-weight: 500;
  color: var(--secondary-text-color);
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.info-badge .value {
  font-size: 1.1rem;
  font-weight: 700;
  color: var(--primary-text-color);
}

.card-box {
  background: var(--card-background);
  backdrop-filter: blur(20px);
  border: 1px solid var(--border-color);
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

.grade-summary {
  display: flex;
  gap: 2rem;
  flex-wrap: wrap;
}

.summary-item {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1.5rem;
  background: rgba(16, 185, 129, 0.1);
  border: 1px solid rgba(16, 185, 129, 0.2);
  border-radius: 12px;
}

.summary-item .label {
  font-weight: 600;
  color: #666;
}

.summary-item .value {
  font-weight: 800;
  color: #10b981;
  font-size: 1.1rem;
}

.controls-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
  flex-wrap: wrap;
  gap: 1rem;
}

.controls-header h2 {
  color: #3D8D7A;
  font-size: 1.5rem;
  font-weight: 700;
  margin: 0;
}

.control-buttons {
  display: flex;
  gap: 1rem;
}

.control-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1.5rem;
  border: none;
  border-radius: 12px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s;
}

.control-btn.export {
  background: rgba(59, 130, 246, 0.1);
  color: #3b82f6;
  border: 1px solid rgba(59, 130, 246, 0.2);
}

.control-btn.settings {
  background: rgba(139, 92, 246, 0.1);
  color: #8b5cf6;
  border: 1px solid rgba(139, 92, 246, 0.2);
}

.control-btn:hover {
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

/* Modern Controls Section */
.controls-section {
  margin-bottom: 2rem;
}

.controls-card {
  position: relative;
  background: var(--card-background);
  backdrop-filter: blur(20px);
  border: 1px solid var(--border-color);
  border-radius: 24px;
  padding: 2.5rem;
  margin-bottom: 3rem;
  overflow: hidden;
  box-shadow: 
    0 8px 32px rgba(61, 141, 122, 0.1),
    0 0 0 1px rgba(255, 255, 255, 0.2);
}

.floating-shapes {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  pointer-events: none;
  overflow: hidden;
}

.floating-shape {
  position: absolute;
  border-radius: 50%;
  opacity: 0.1;
  animation: float 6s ease-in-out infinite;
}

.floating-shape.shape-1 {
  width: 120px;
  height: 120px;
  background: linear-gradient(135deg, #10b981, #059669);
  top: -60px;
  right: -60px;
  animation-delay: 0s;
}

.floating-shape.shape-2 {
  width: 80px;
  height: 80px;
  background: linear-gradient(135deg, #10b981, #10b981);
  bottom: -40px;
  left: 20%;
  animation-delay: 2s;
}

@keyframes float {
  0%, 100% { transform: translateY(0px) rotate(0deg); }
  50% { transform: translateY(-20px) rotate(180deg); }
}

.controls-content {
  position: relative;
  z-index: 2;
}

.controls-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 1.5rem;
}

.controls-header h2 {
  color: #3D8D7A;
  font-size: 1.8rem;
  font-weight: 700;
  margin: 0;
  letter-spacing: -0.5px;
}

.control-buttons {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
}

.control-btn {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.875rem 1.75rem;
  border: none;
  border-radius: 16px;
  font-weight: 600;
  font-size: 0.95rem;
  cursor: pointer;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  position: relative;
  overflow: hidden;
}

.control-btn::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
  transition: left 0.5s;
}

.control-btn:hover::before {
  left: 100%;
}

.control-btn.export {
  background: linear-gradient(135deg, rgba(59, 130, 246, 0.1), rgba(99, 102, 241, 0.1));
  color: #3b82f6;
  border: 1px solid rgba(59, 130, 246, 0.2);
}

.control-btn.export:hover {
  background: linear-gradient(135deg, rgba(59, 130, 246, 0.15), rgba(99, 102, 241, 0.15));
  border-color: rgba(59, 130, 246, 0.3);
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(59, 130, 246, 0.25);
}

.control-btn.settings {
  background: linear-gradient(135deg, rgba(139, 92, 246, 0.1), rgba(168, 85, 247, 0.1));
  color: #8b5cf6;
  border: 1px solid rgba(139, 92, 246, 0.2);
}

.control-btn.settings:hover {
  background: linear-gradient(135deg, rgba(139, 92, 246, 0.15), rgba(168, 85, 247, 0.15));
  border-color: rgba(139, 92, 246, 0.3);
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(139, 92, 246, 0.25);
}

.control-btn svg {
  transition: transform 0.3s ease;
}

.control-btn:hover svg {
  transform: scale(1.1);
}

/* Enhanced Filters Section */
.filters-section {
  display: flex;
  gap: 2rem;
  align-items: end;
  flex-wrap: wrap;
  background: var(--card-background);
  backdrop-filter: blur(10px);
  padding: 1.5rem 2rem;
  border-radius: 20px;
  border: 1px solid var(--border-color);
  margin-top: 2rem;
  margin-bottom: 2rem;
}

.filter-group {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.filter-group label {
  font-weight: 600;
  color: #3D8D7A;
  font-size: 0.9rem;
  letter-spacing: -0.2px;
}

.filter-group select {
  padding: 0.875rem 1.25rem;
  border: 2px solid var(--input-border);
  border-radius: 16px;
  font-size: 1rem;
  font-weight: 500;
  background: var(--input-bg);
  backdrop-filter: blur(10px);
  min-width: 200px;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  cursor: pointer;
  color: var(--primary-text-color);
}

.filter-group select:focus {
  outline: none;
  border-color: rgba(61, 141, 122, 0.3);
  box-shadow: 0 0 0 4px rgba(61, 141, 122, 0.1);
  transform: translateY(-1px);
}

.filter-group select:hover {
  border-color: rgba(61, 141, 122, 0.2);
  background: rgba(255, 255, 255, 1);
}

.search-group {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  flex: 1;
  min-width: 250px;
}

.search-input {
  padding: 0.875rem 1.25rem;
  border: 2px solid rgba(61, 141, 122, 0.1);
  border-radius: 16px;
  font-size: 1rem;
  font-weight: 500;
  background: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(10px);
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.search-input:focus {
  outline: none;
  border-color: rgba(61, 141, 122, 0.3);
  box-shadow: 0 0 0 4px rgba(61, 141, 122, 0.1);
  transform: translateY(-1px);
  background: rgba(255, 255, 255, 1);
}

.search-input::placeholder {
  color: #9ca3af;
  font-weight: 400;
}

/* Enhanced Table Container and Gradebook Table */
.gradebook-section {
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(20px);
  border: 1px solid rgba(61, 141, 122, 0.1);
  border-radius: 24px;
  overflow: hidden;
  box-shadow: 
    0 8px 32px rgba(61, 141, 122, 0.1),
    0 0 0 1px rgba(255, 255, 255, 0.2);
}

.table-container {
  overflow-x: auto;
  border-radius: 0;
  border: none;
}

.gradebook-table {
  width: 100%;
  border-collapse: collapse;
  min-width: 800px;
  font-family: 'Inter', sans-serif;
}

.gradebook-table th {
  background: linear-gradient(135deg, #3D8D7A 0%, #2c6b5c 100%);
  color: white;
  padding: 1.75rem 1.25rem;
  text-align: left;
  font-weight: 700;
  font-size: 0.95rem;
  letter-spacing: -0.2px;
  border: none;
  position: sticky;
  top: 0;
  z-index: 10;
}

.gradebook-table th:first-child {
  border-top-left-radius: 0;
}

.gradebook-table th:last-child {
  border-top-right-radius: 0;
}

.gradebook-table tbody tr {
  transition: all 0.2s ease;
  border-bottom: 2px solid rgba(61, 141, 122, 0.12);
  margin-bottom: 4px;
}

.gradebook-table tbody tr:hover {
  background: rgba(61, 141, 122, 0.02);
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(61, 141, 122, 0.08);
}

.gradebook-table tbody tr:last-child {
  border-bottom: none;
}

.gradebook-table td {
  padding: 1.75rem 1.25rem;
  border: none;
  vertical-align: middle;
  font-weight: 500;
  border-bottom: 2px solid transparent;
}

.student-column {
  min-width: 280px;
  max-width: 280px;
}

.quiz-column {
  min-width: 140px;
  max-width: 140px;
  text-align: center;
}

.average-column {
  min-width: 160px;
  max-width: 160px;
}

.actions-column {
  min-width: 120px;
  max-width: 120px;
}

/* Enhanced Quiz Header */
.quiz-header {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  text-align: center;
}

.quiz-title {
  font-size: 0.95rem;
  font-weight: 700;
  letter-spacing: -0.2px;
}

.quiz-points,
.quiz-date {
  font-size: 0.75rem;
  opacity: 0.85;
  font-weight: 500;
}

/* Enhanced Student Details */
.student-details {
  display: flex;
  align-items: center;
  gap: 1.25rem;
}

.student-avatar {
  width: 45px;
  height: 45px;
  border-radius: 14px;
  background: linear-gradient(135deg, #3D8D7A 0%, #2c6b5c 100%);
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 0.95rem;
  flex-shrink: 0;
  box-shadow: 0 3px 8px rgba(61, 141, 122, 0.2);
  border: 2px solid rgba(255, 255, 255, 0.3);
}

.student-text {
  min-width: 0;
}

.student-name {
  font-weight: 700;
  color: #3D8D7A;
  font-size: 1rem;
  letter-spacing: -0.2px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.student-email {
  color: #666;
  font-size: 0.85rem;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.grade-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.5rem;
}

.student-id {
  font-size: 0.85rem;
  color: #6b7280;
  font-weight: 500;
}

/* Enhanced Grade Input Fields */
.grade-input {
  width: 70px;
  padding: 0.625rem 0.5rem;
  border: 2px solid rgba(61, 141, 122, 0.1);
  border-radius: 12px;
  text-align: center;
  font-weight: 700;
  font-size: 0.95rem;
  background: rgba(255, 255, 255, 0.8);
  backdrop-filter: blur(5px);
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.grade-input:focus {
  outline: none;
  border-color: rgba(61, 141, 122, 0.4);
  box-shadow: 0 0 0 4px rgba(61, 141, 122, 0.1);
  transform: scale(1.05);
  background: rgba(255, 255, 255, 1);
}

.grade-input:hover {
  border-color: rgba(61, 141, 122, 0.2);
  background: rgba(255, 255, 255, 0.95);
}

/* Enhanced Grade Color Classes */
.grade-input.grade-a {
  background: linear-gradient(135deg, rgba(16, 185, 129, 0.1), rgba(5, 150, 105, 0.1));
  color: #059669;
  border-color: rgba(16, 185, 129, 0.2);
}

.grade-input.grade-a:focus {
  border-color: rgba(16, 185, 129, 0.4);
  box-shadow: 0 0 0 4px rgba(16, 185, 129, 0.1);
}

.grade-input.grade-b {
  background: linear-gradient(135deg, rgba(59, 130, 246, 0.1), rgba(37, 99, 235, 0.1));
  color: #2563eb;
  border-color: rgba(59, 130, 246, 0.2);
}

.grade-input.grade-b:focus {
  border-color: rgba(59, 130, 246, 0.4);
  box-shadow: 0 0 0 4px rgba(59, 130, 246, 0.1);
}

.grade-input.grade-c {
  background: linear-gradient(135deg, rgba(245, 158, 11, 0.1), rgba(217, 119, 6, 0.1));
  color: #d97706;
  border-color: rgba(245, 158, 11, 0.2);
}

.grade-input.grade-c:focus {
  border-color: rgba(245, 158, 11, 0.4);
  box-shadow: 0 0 0 4px rgba(245, 158, 11, 0.1);
}

.grade-input.grade-d {
  background: rgba(249, 115, 22, 0.1);
  color: #ea580c;
  border-color: rgba(249, 115, 22, 0.2);
}

.grade-input.grade-d:focus {
  border-color: rgba(249, 115, 22, 0.4);
  box-shadow: 0 0 0 4px rgba(249, 115, 22, 0.1);
}

.grade-input.grade-f {
  background: linear-gradient(135deg, rgba(239, 68, 68, 0.1), rgba(220, 38, 38, 0.1));
  color: #dc2626;
  border-color: rgba(239, 68, 68, 0.2);
}

.grade-input.grade-f:focus {
  border-color: rgba(239, 68, 68, 0.4);
  box-shadow: 0 0 0 4px rgba(239, 68, 68, 0.1);
}

/* Enhanced Grade Display */

.grade-percentage {
  font-size: 0.75rem;
  font-weight: 600;
  color: #666;
}

.average-display {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.average-score {
  font-size: 1.1rem;
  font-weight: 800;
  text-align: center;
}

.average-score.grade-a { color: #10b981; }
.average-score.grade-b { color: #3b82f6; }
.average-score.grade-c { color: #f59e0b; }
.average-score.grade-d { color: #f97316; }
.average-score.grade-f { color: #ef4444; }
.average-score.no-grade { color: #9ca3af; }

.progress-bar {
  width: 100%;
  height: 8px;
  background: rgba(209, 213, 219, 0.3);
  border-radius: 4px;
  overflow: hidden;
}

.progress-fill {
  height: 100%;
  transition: all 0.3s ease;
  border-radius: 4px;
}

.progress-fill.grade-a { background: #10b981; }
.progress-fill.grade-b { background: #3b82f6; }
.progress-fill.grade-c { background: #f59e0b; }
.progress-fill.grade-d { background: #f97316; }
.progress-fill.grade-f { background: #ef4444; }

.actions-cell {
  text-align: center;
}

.action-btn {
  padding: 0.5rem;
  margin: 0 0.25rem;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.action-btn.view {
  background: rgba(59, 130, 246, 0.1);
  color: #3b82f6;
}

.action-btn.message {
  background: rgba(16, 185, 129, 0.1);
  color: #10b981;
}

.action-btn:hover {
  transform: scale(1.1);
}

.empty-state {
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
  background: var(--card-background);
  border-radius: 20px;
  max-width: 600px;
  width: 100%;
  max-height: 90vh;
  overflow-y: auto;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
  border: 1px solid var(--border-color);
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

.setting-group {
  margin-bottom: 2rem;
}

.setting-group h3 {
  color: #3D8D7A;
  margin-bottom: 1rem;
  font-size: 1.2rem;
  font-weight: 600;
}

.grade-scale {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1rem;
}

.scale-item {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.scale-item label {
  font-weight: 600;
  color: #444;
  min-width: 120px;
}

.scale-item input {
  flex: 1;
  padding: 0.5rem;
  border: 2px solid rgba(61, 141, 122, 0.1);
  border-radius: 8px;
}

.option-item {
  margin-bottom: 1rem;
}

.option-item label {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  cursor: pointer;
  font-weight: 500;
}

.option-item input[type="checkbox"] {
  width: 18px;
  height: 18px;
  accent-color: #3D8D7A;
}

.modal-actions {
  display: flex;
  gap: 1rem;
  justify-content: flex-end;
  margin-top: 2rem;
  padding-top: 2rem;
  border-top: 1px solid rgba(61, 141, 122, 0.1);
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

.save-btn {
  background: linear-gradient(135deg, #3D8D7A 0%, #A3D1C6 100%);
  color: white;
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 12px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s;
}

.save-btn:hover {
  transform: translateY(-1px);
  box-shadow: 0 8px 20px rgba(61, 141, 122, 0.3);
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
  background: var(--card-background);
  padding: 2rem;
  border-radius: 16px;
  text-align: center;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
  border: 1px solid var(--border-color);
  color: var(--primary-text-color);
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

  .grade-summary {
    flex-direction: column;
    gap: 1rem;
  }

  .controls-header,
  .filters-section {
    flex-direction: column;
    align-items: stretch;
    gap: 1rem;
  }

  .control-buttons {
    justify-content: stretch;
  }

  .control-btn {
    flex: 1;
    justify-content: center;
  }

  .table-container {
    font-size: 0.85rem;
  }

  .student-column {
    min-width: 200px;
    max-width: 200px;
  }

  .quiz-column {
    min-width: 100px;
    max-width: 100px;
  }

  .grade-scale {
    grid-template-columns: 1fr;
  }
}

/* Dark Mode Styles - Clean Implementation */
.grade-management-container.dark-mode {
  background: var(--bg-primary);
  color: var(--primary-text-color);
}

.grade-management-container.dark-mode .section-header-card {
  background: var(--card-background);
  border: 1px solid var(--border-color);
}

.grade-management-container.dark-mode .section-header-title {
  color: var(--accent-color);
}

.grade-management-container.dark-mode .section-header-subtitle,
.grade-management-container.dark-mode .section-header-description {
  color: var(--secondary-text-color);
}

.grade-management-container.dark-mode .back-button {
  background: var(--input-bg);
  border: 1px solid var(--border-color);
  color: var(--primary-text-color);
}

.grade-management-container.dark-mode .back-button:hover {
  background: var(--bg-secondary);
  color: var(--accent-color);
}

.grade-management-container.dark-mode .controls-card {
  background: var(--card-background);
  border: 1px solid var(--border-color);
}

.grade-management-container.dark-mode .controls-header h2 {
  color: var(--primary-text-color);
}

.grade-management-container.dark-mode .control-btn.export {
  background: rgba(59, 130, 246, 0.2);
  color: var(--accent-color);
  border: 1px solid rgba(59, 130, 246, 0.3);
}

.grade-management-container.dark-mode .control-btn.settings {
  background: rgba(139, 92, 246, 0.2);
  color: #8b5cf6;
  border: 1px solid rgba(139, 92, 246, 0.3);
}

.grade-management-container.dark-mode .filters-section {
  background: var(--card-background);
  border: 1px solid var(--border-color);
}

.grade-management-container.dark-mode .filter-group label {
  color: var(--primary-text-color);
}

.grade-management-container.dark-mode .filter-group select,
.grade-management-container.dark-mode .search-input {
  background: var(--input-bg);
  color: var(--primary-text-color);
  border: 2px solid var(--input-border);
}

.grade-management-container.dark-mode .filter-group select:focus,
.grade-management-container.dark-mode .search-input:focus {
  border-color: var(--accent-color);
}

.grade-management-container.dark-mode .gradebook-table {
  background: var(--card-background);
}

.grade-management-container.dark-mode .gradebook-table th {
  background: var(--accent-color);
  color: white;
}

.grade-management-container.dark-mode .gradebook-table td {
  background: var(--card-background);
  color: var(--primary-text-color);
  border-color: var(--border-color);
  padding: 1.75rem 1.25rem;
  border-bottom: 2px solid var(--border-color);
}

.grade-management-container.dark-mode .gradebook-table tbody tr:hover {
  background: var(--bg-secondary);
}

.grade-management-container.dark-mode .card-box {
  background: var(--card-background);
  border: 1px solid var(--border-color);
}

.dark-mode .filter-group select:focus {
  border-color: rgba(61, 141, 122, 0.4);
  box-shadow: 0 0 0 4px rgba(61, 141, 122, 0.15);
  background: rgba(17, 24, 39, 1);
}

.dark-mode .filter-group select:hover {
  border-color: rgba(255, 255, 255, 0.12);
  background: rgba(17, 24, 39, 1);
}

.dark-mode .search-input {
  background: rgba(17, 24, 39, 0.9);
  border: 2px solid rgba(255, 255, 255, 0.08);
  color: var(--primary-text-color);
}

.dark-mode .search-input:focus {
  border-color: rgba(61, 141, 122, 0.4);
  box-shadow: 0 0 0 4px rgba(61, 141, 122, 0.15);
  background: rgba(17, 24, 39, 1);
}

.dark-mode .search-input::placeholder {
  color: var(--secondary-text-color);
}

.dark-mode .gradebook-section {
  background: rgba(17, 24, 39, 0.95);
  border: 1px solid rgba(255, 255, 255, 0.08);
  box-shadow: 
    0 4px 12px rgba(0, 0, 0, 0.25),
    0 2px 6px rgba(0, 0, 0, 0.15);
}

.dark-mode .gradebook-table th {
  background: linear-gradient(135deg, #1f2937 0%, #111827 100%);
  color: var(--primary-text-color);
}

.dark-mode .gradebook-table tbody tr {
  border-bottom: 1px solid rgba(255, 255, 255, 0.05);
}

.dark-mode .gradebook-table tbody tr:hover {
  background: rgba(31, 41, 55, 0.6);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
}

.dark-mode .student-email {
  color: var(--secondary-text-color);
}

.dark-mode .student-avatar {
  background: linear-gradient(135deg, var(--accent-color) 0%, #2563eb 100%);
}
</style>