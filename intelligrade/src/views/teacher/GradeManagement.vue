<template>
  <div class="grade-management-page" :class="{ 'dark': isDarkMode }">
    <!-- Header -->
    <div class="header-card">
      <div class="header-content">
        <div class="header-left">
          <div class="header-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
              <path d="M14,2H6A2,2 0 0,0 4,4V20A2,2 0 0,0 6,22H18A2,2 0 0,0 20,20V8L14,2M18,20H6V4H13V9H18V20Z" />
            </svg>
          </div>
          <div class="header-info">
            <h1 class="header-title">Grade Management</h1>
            <p class="header-subtitle">{{ subject?.name }} - {{ section?.name }}</p>
          </div>
        </div>
        <button @click="goBack" class="back-btn">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
            <path d="M20,11V13H8L13.5,18.5L12.08,19.92L4.16,12L12.08,4.08L13.5,5.5L8,11H20Z" />
          </svg>
          Back to Students
        </button>
      </div>
    </div>

    <!-- Controls -->
    <div class="controls-card">
      <div class="controls-header">
        <h2 class="controls-title">Grade Controls</h2>
      </div>
      <div class="controls-content">
        <div class="filters">
          <select v-model="selectedQuiz" @change="filterByQuiz" class="filter-select">
            <option value="">All Quizzes</option>
            <option v-for="quiz in quizzes" :key="quiz.id" :value="quiz.id">
              {{ quiz.title }}
            </option>
          </select>
          <select v-model="viewMode" @change="changeViewMode" class="filter-select">
            <option value="edit">Edit Mode</option>
            <option value="view">View Only</option>
          </select>
        </div>
        <button @click="exportGrades" class="secondary-btn">
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
        <h2 class="table-title">Student Grades</h2>
      </div>

      <div v-if="filteredStudents.length > 0">
        <table class="grade-table">
          <thead>
            <tr>
              <th>Student</th>
              <th v-for="quiz in quizzes" :key="quiz.id" class="quiz-column">
                {{ quiz.title }}
                <br>
                <small>({{ quiz.total_points }} pts)</small>
              </th>
              <th class="average-column">Average</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="student in filteredStudents" :key="student.id">
              <td>
                <div class="student-info">
                  <div class="student-avatar">
                    {{ student.first_name?.charAt(0) || 'S' }}{{ student.last_name?.charAt(0) || 'T' }}
                  </div>
                  <div class="student-details">
                    <div class="student-name">{{ student.first_name }} {{ student.last_name }}</div>
                  </div>
                </div>
              </td>
              <td v-for="quiz in quizzes" :key="quiz.id" class="quiz-column">
                <input
                  v-if="viewMode === 'edit'"
                  :value="getGradeValue(student.id, quiz.id)"
                  @input="updateGrade(student.id, quiz.id, $event)"
                  type="number"
                  :min="0"
                  :max="quiz.total_points"
                  class="grade-input"
                  :placeholder="`/${quiz.total_points}`"
                />
                <div v-else class="grade-display" :class="getGradeClass(getGradeValue(student.id, quiz.id), quiz.total_points)">
                  {{ getGradePercentage(getGradeValue(student.id, quiz.id), quiz.total_points) }}%
                </div>
              </td>
              <td class="average-column">
                <div class="average-display" :class="getAverageClass(student.average)">
                  {{ student.average ? Math.round(student.average) + '%' : 'N/A' }}
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <div v-else class="empty-state">
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
import { supabase } from '../../supabase'
import { useDarkMode } from '../../composables/useDarkMode.js'

// Interfaces
interface Enrollment {
  student_id: string
  students: {
    id: string
    first_name: string
    last_name: string
    email: string
  }[]
}

// Dark mode
const { isDarkMode, initDarkMode } = useDarkMode()

const router = useRouter()
const route = useRoute()

// Data
const students = ref([])
const quizzes = ref([])
const grades = ref({})
const subject = ref(null)
const section = ref(null)
const subjectId = ref(route.params.subjectId)
const sectionId = ref(route.params.sectionId)

// UI State
const isLoading = ref(false)
const loadingMessage = ref('')
const viewMode = ref('edit')
const selectedQuiz = ref('')
const showGradeSettings = ref(false)

// Grade Settings
const gradeScale = ref({
  A: 90,
  B: 80,
  C: 70,
  D: 60
})

const displayOptions = ref({
  showPercentages: true,
  showLetterGrades: false,
  roundToWhole: true
})

// Computed
const filteredStudents = computed(() => {
  const filtered = [...students.value]
  
  if (selectedQuiz.value) {
    // Filter logic for specific quiz if needed
  }
  
  return filtered
})

// Functions
const getGradePercentage = (grade: number, totalPoints: number): string => {
  if (!grade || !totalPoints) return '0'
  return Math.round((grade / totalPoints) * 100).toString()
}

const getGradeClass = (grade: number, totalPoints: number): string => {
  const percentage = Number(getGradePercentage(grade, totalPoints))
  if (percentage >= 90) return 'grade-a'
  if (percentage >= 80) return 'grade-b'
  if (percentage >= 70) return 'grade-c'
  if (percentage >= 60) return 'grade-d'
  return 'grade-f'
}

const getAverageClass = (average: number): string => {
  if (!average) return ''
  if (average >= 90) return 'grade-a'
  if (average >= 80) return 'grade-b'
  if (average >= 70) return 'grade-c'
  if (average >= 60) return 'grade-d'
  return 'grade-f'
}

const getGradeValue = (studentId: string, quizId: string): number => {
  return grades.value[studentId]?.[quizId] || 0
}

const updateGrade = async (studentId: string, quizId: string, event: Event) => {
  const target = event.target as HTMLInputElement
  const newGrade = Number(target.value)
  
  if (!grades.value[studentId]) {
    grades.value[studentId] = {}
  }
  
  grades.value[studentId][quizId] = newGrade
  
  // Save to database
  await saveGrade(studentId, quizId, newGrade)
  
  // Recalculate student average
  calculateStudentAverage(studentId)
}

const saveGrade = async (studentId: string, quizId: string, grade: number) => {
  try {
    const { error } = await supabase
      .from('quiz_results')
      .upsert({
        student_id: studentId,
        quiz_id: quizId,
        score: grade,
        updated_at: new Date()
      })
    
    if (error) throw error
  } catch (error) {
    console.error('Error saving grade:', error)
    alert('Failed to save grade. Please try again.')
  }
}

const calculateStudentAverage = (studentId: string) => {
  const studentGrades = grades.value[studentId]
  if (!studentGrades) return

  const gradeValues = Object.entries(studentGrades).map(([quizId, grade]) => {
    const quiz = quizzes.value.find(q => q.id === quizId)
    return quiz ? (Number(grade) / quiz.total_points) * 100 : 0
  })

  if (gradeValues.length > 0) {
    const average = gradeValues.reduce((a, b) => a + b, 0) / gradeValues.length
    const student = students.value.find(s => s.id === studentId)
    if (student) {
      student.average = average
    }
  }
}

const filterByQuiz = () => {
  // Filter implementation if needed
  console.log('Filtering by quiz:', selectedQuiz.value)
}

const changeViewMode = () => {
  console.log('View mode changed to:', viewMode.value)
}

const saveGradeSettings = () => {
  console.log('Saving grade settings:', { gradeScale: gradeScale.value, displayOptions: displayOptions.value })
  showGradeSettings.value = false
  alert('Grade settings saved successfully!')
}

const fetchData = async () => {
  isLoading.value = true
  loadingMessage.value = 'Loading grade data...'
  
  try {
    // Fetch subject and section info
    const { data: subjectData } = await supabase
      .from('subjects')
      .select('*')
      .eq('id', subjectId.value)
      .single()
    
    const { data: sectionData } = await supabase
      .from('sections')
      .select('*')
      .eq('id', sectionId.value)
      .single()
    
    subject.value = subjectData
    section.value = sectionData
    
    // Fetch students in this section
    const { data: studentsData } = await supabase
      .from('section_enrollments')
      .select(`
        student_id,
        students (
          id,
          first_name,
          last_name,
          email
        )
      `)
      .eq('section_id', sectionId.value)
    
    students.value = studentsData?.map((enrollment: Enrollment) => ({
      id: enrollment.students[0].id,
      first_name: enrollment.students[0].first_name,
      last_name: enrollment.students[0].last_name,
      email: enrollment.students[0].email,
      average: null
    })) || []
    
    // Fetch quizzes for this subject/section
    const { data: quizzesData } = await supabase
      .from('quizzes')
      .select('*')
      .eq('subject_id', subjectId.value)
      .eq('section_id', sectionId.value)
    
    quizzes.value = quizzesData || []
    
    // Fetch existing grades
    const { data: gradesData } = await supabase
      .from('quiz_results')
      .select('*')
      .in('quiz_id', quizzes.value.map(q => q.id))
      .in('student_id', students.value.map(s => s.id))
    
    // Organize grades by student and quiz
    grades.value = {}
    gradesData?.forEach(result => {
      if (!grades.value[result.student_id]) {
        grades.value[result.student_id] = {}
      }
      grades.value[result.student_id][result.quiz_id] = result.score
    })
    
    // Calculate averages for each student
    students.value.forEach(student => {
      calculateStudentAverage(student.id)
    })
    
  } catch (error) {
    console.error('Error fetching data:', error)
    alert('Failed to load grade data. Please try again.')
  } finally {
    isLoading.value = false
  }
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

onMounted(async () => {
  initDarkMode()
  await fetchData()
})
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.grade-management-page {
  min-height: 100vh;
  background: #FBFFE4;
  padding: 1.5rem;
  font-family: 'Inter', sans-serif;
}
.dark .grade-management-page {
  background: #181c20;
}

/* Header */
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

.back-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem 1.25rem;
  border-radius: 8px;
  font-weight: 500;
  font-size: 0.875rem;
  transition: all 0.2s;
  cursor: pointer;
  text-decoration: none;
  outline: none;
  border: 2px solid #3D8D7A;
  background: #3D8D7A;
  color: white;
  box-shadow: 0 2px 8px rgba(61, 141, 122, 0.10);
}
.back-btn:hover {
  background: #A3D1C6;
  color: #23272b;
  border-color: #3D8D7A;
  box-shadow: 0 4px 16px rgba(61, 141, 122, 0.18);
}
.dark .back-btn {
  background: #3D8D7A;
  color: white;
  border-color: #A3D1C6;
}
.dark .back-btn:hover {
  background: #A3D1C6;
  color: #23272b;
  border-color: #3D8D7A;
}

/* Controls */
.controls-card {
  background: white;
  border-radius: 16px;
  padding: 1.5rem;
  margin-bottom: 1.5rem;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
}
.dark .controls-card {
  background: #23272b;
  border: 1px solid #3D8D7A;
  box-shadow: 0 2px 8px rgba(0,0,0,0.25);
}

.controls-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 1rem;
}

.controls-title {
  font-size: 1.125rem;
  font-weight: 600;
  color: #1f2937;
}
.dark .controls-title {
  color: #A3D1C6;
}

.controls-content {
  display: grid;
  grid-template-columns: 1fr auto auto;
  gap: 1rem;
  align-items: center;
}

.filters {
  display: flex;
  gap: 1rem;
  align-items: center;
}

.filter-select {
  padding: 0.5rem 1rem;
  border: 1px solid #d1d5db;
  border-radius: 8px;
  background: white;
  color: #374151;
  font-size: 0.875rem;
  outline: none;
  transition: all 0.2s;
  min-width: 150px;
}
.filter-select:focus {
  border-color: #3D8D7A;
  box-shadow: 0 0 0 3px rgba(61, 141, 122, 0.1);
}
.dark .filter-select {
  background: #374151;
  border-color: #4b5563;
  color: #e5e7eb;
}
.dark .filter-select:focus {
  border-color: #A3D1C6;
  box-shadow: 0 0 0 3px rgba(163, 209, 198, 0.1);
}

.primary-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1.5rem;
  background: #3D8D7A;
  color: white;
  border: none;
  border-radius: 8px;
  font-weight: 500;
  font-size: 0.875rem;
  cursor: pointer;
  transition: all 0.2s;
  text-decoration: none;
}
.primary-btn:hover {
  background: #B3D8A8;
  color: #1f2937;
}
.dark .primary-btn {
  background: #3D8D7A;
  color: white;
}
.dark .primary-btn:hover {
  background: #A3D1C6;
  color: #1f2937;
}

.secondary-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1.5rem;
  background: white;
  color: #374151;
  border: 1px solid #d1d5db;
  border-radius: 8px;
  font-weight: 500;
  font-size: 0.875rem;
  cursor: pointer;
  transition: all 0.2s;
  text-decoration: none;
}
.secondary-btn:hover {
  background: #B3D8A8;
  border-color: #3D8D7A;
  color: #1f2937;
}
.dark .secondary-btn {
  background: #374151;
  color: #e5e7eb;
  border-color: #4b5563;
}
.dark .secondary-btn:hover {
  background: #A3D1C6;
  border-color: #3D8D7A;
  color: #1f2937;
}

/* Table */
.table-container {
  background: white;
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
}
.dark .table-container {
  background: #23272b;
  border: 1px solid #3D8D7A;
  box-shadow: 0 2px 8px rgba(0,0,0,0.25);
}

.table-header {
  background: #B3D8A8;
  padding: 1rem 1.5rem;
  border-bottom: 1px solid #e5e7eb;
}
.dark .table-header {
  background: #3D8D7A;
  border-bottom-color: #4b5563;
}

.table-title {
  font-size: 1.125rem;
  font-weight: 600;
  color: #1f2937;
}
.dark .table-title {
  color: white;
}

.grade-table {
  width: 100%;
  border-collapse: collapse;
}

.grade-table th,
.grade-table td {
  padding: 1rem;
  text-align: left;
  border-bottom: 1px solid #e5e7eb;
}
.dark .grade-table th,
.dark .grade-table td {
  border-bottom-color: #374151;
}

.grade-table th {
  background: #FBFFE4;
  font-weight: 600;
  color: #374151;
  font-size: 0.875rem;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}
.dark .grade-table th {
  background: #374151;
  color: #A3D1C6;
}

.grade-table td {
  color: #6b7280;
  font-size: 0.875rem;
}
.dark .grade-table td {
  color: #d1d5db;
}

.student-info {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.student-avatar {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background: #3D8D7A;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-weight: 600;
  font-size: 0.875rem;
}

.student-name {
  font-weight: 500;
  color: #1f2937;
}
.dark .student-name {
  color: #e5e7eb;
}

.grade-input {
  width: 80px;
  padding: 0.375rem 0.5rem;
  border: 1px solid #d1d5db;
  border-radius: 6px;
  text-align: center;
  font-size: 0.875rem;
  background: white;
  color: #374151;
}
.grade-input:focus {
  outline: none;
  border-color: #3D8D7A;
  box-shadow: 0 0 0 3px rgba(61, 141, 122, 0.1);
}
.dark .grade-input {
  background: #374151;
  border-color: #4b5563;
  color: #e5e7eb;
}
.dark .grade-input:focus {
  border-color: #A3D1C6;
  box-shadow: 0 0 0 3px rgba(163, 209, 198, 0.1);
}

.grade-display {
  padding: 0.25rem 0.75rem;
  border-radius: 12px;
  font-weight: 500;
  font-size: 0.875rem;
  text-align: center;
}

.grade-a { background: #dcfce7; color: #166534; }
.grade-b { background: #dbeafe; color: #1d4ed8; }
.grade-c { background: #fef3c7; color: #d97706; }
.grade-d { background: #fed7d7; color: #dc2626; }
.grade-f { background: #fee2e2; color: #dc2626; }

.dark .grade-a { background: #166534; color: #dcfce7; }
.dark .grade-b { background: #1d4ed8; color: #dbeafe; }
.dark .grade-c { background: #d97706; color: #fef3c7; }
.dark .grade-d { background: #dc2626; color: #fed7d7; }
.dark .grade-f { background: #dc2626; color: #fee2e2; }

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
}

.modal-content {
  background: white;
  border-radius: 16px;
  max-width: 500px;
  width: 90%;
  max-height: 80vh;
  overflow-y: auto;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
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
  border-bottom-color: #374151;
}

.modal-header h2 {
  font-size: 1.25rem;
  font-weight: 600;
  color: #1f2937;
}
.dark .modal-header h2 {
  color: #A3D1C6;
}

.close-btn {
  padding: 0.5rem;
  background: none;
  border: none;
  cursor: pointer;
  color: #6b7280;
  border-radius: 8px;
  transition: all 0.2s;
}
.close-btn:hover {
  background: #f3f4f6;
  color: #374151;
}
.dark .close-btn {
  color: #9ca3af;
}
.dark .close-btn:hover {
  background: #374151;
  color: #e5e7eb;
}

.modal-body {
  padding: 1.5rem;
}

.setting-group {
  margin-bottom: 2rem;
}

.setting-group h3 {
  font-size: 1rem;
  font-weight: 600;
  color: #1f2937;
  margin-bottom: 1rem;
}
.dark .setting-group h3 {
  color: #A3D1C6;
}

.grade-scale {
  display: grid;
  gap: 1rem;
}

.scale-item {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.scale-item label {
  min-width: 120px;
  font-weight: 500;
  color: #374151;
}
.dark .scale-item label {
  color: #d1d5db;
}

.scale-item input {
  width: 80px;
  padding: 0.5rem;
  border: 1px solid #d1d5db;
  border-radius: 6px;
  text-align: center;
  background: white;
  color: #374151;
}
.scale-item input:focus {
  outline: none;
  border-color: #3D8D7A;
  box-shadow: 0 0 0 3px rgba(61, 141, 122, 0.1);
}
.dark .scale-item input {
  background: #374151;
  border-color: #4b5563;
  color: #e5e7eb;
}
.dark .scale-item input:focus {
  border-color: #A3D1C6;
}

.option-item {
  margin-bottom: 0.75rem;
}

.option-item label {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  cursor: pointer;
  color: #374151;
}
.dark .option-item label {
  color: #d1d5db;
}

.modal-actions {
  display: flex;
  gap: 1rem;
  justify-content: flex-end;
  padding-top: 1rem;
  border-top: 1px solid #e5e7eb;
}
.dark .modal-actions {
  border-top-color: #374151;
}

.cancel-btn {
  padding: 0.75rem 1.5rem;
  background: white;
  color: #374151;
  border: 1px solid #d1d5db;
  border-radius: 8px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s;
}
.cancel-btn:hover {
  background: #f9fafb;
}
.dark .cancel-btn {
  background: #374151;
  color: #e5e7eb;
  border-color: #4b5563;
}
.dark .cancel-btn:hover {
  background: #4b5563;
}

.save-btn {
  padding: 0.75rem 1.5rem;
  background: #3D8D7A;
  color: white;
  border: none;
  border-radius: 8px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s;
}
.save-btn:hover {
  background: #B3D8A8;
  color: #1f2937;
}
.dark .save-btn:hover {
  background: #A3D1C6;
  color: #1f2937;
}

/* Loading */
.loading-overlay {
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
}

.loading-content {
  background: white;
  border-radius: 12px;
  padding: 2rem;
  text-align: center;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
}
.dark .loading-content {
  background: #23272b;
  border: 1px solid #3D8D7A;
}

.loading-spinner {
  width: 40px;
  height: 40px;
  border: 3px solid #e5e7eb;
  border-top: 3px solid #3D8D7A;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin: 0 auto 1rem;
}
.dark .loading-spinner {
  border-color: #374151;
  border-top-color: #A3D1C6;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.loading-content p {
  color: #6b7280;
  font-weight: 500;
}
.dark .loading-content p {
  color: #9ca3af;
}

/* Empty State */
.empty-state {
  text-align: center;
  padding: 3rem 1rem;
  color: #6b7280;
}
.dark .empty-state {
  color: #9ca3af;
}

.empty-state h3 {
  font-size: 1.125rem;
  font-weight: 600;
  margin-bottom: 0.5rem;
  color: #374151;
}
.dark .empty-state h3 {
  color: #d1d5db;
}

/* Responsive */
@media (max-width: 768px) {
  .grade-management-page {
    padding: 1rem;
  }
  
  .header-content {
    flex-direction: column;
    gap: 1rem;
    text-align: center;
  }
  
  .controls-content {
    grid-template-columns: 1fr;
    gap: 1rem;
  }
  
  .filters {
    flex-direction: column;
    width: 100%;
  }
  
  .filter-select {
    width: 100%;
  }
  
  .grade-table {
    font-size: 0.8rem;
  }
  
  .grade-table th,
  .grade-table td {
    padding: 0.75rem 0.5rem;
  }
  
  .modal-content {
    width: 95%;
    margin: 1rem;
  }
}
</style>