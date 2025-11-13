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
          Back to Section
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
            <option value="">All Quizzes ({{ quizzes.length }})</option>
            <option v-for="quiz in quizzes" :key="quiz.id" :value="quiz.id">
              {{ quiz.title }}
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
        <h2 class="table-title">Student Grades ({{ students.length }} Students)</h2>
      </div>

      <div v-if="filteredStudents.length > 0" class="table-wrapper">
        <!-- Debug info -->
        <div v-if="quizzes.length === 0" class="quiz-debug" style="padding: 1rem; background: #fef3c7; margin-bottom: 1rem; border-radius: 8px; color: #92400e;">
          <p><strong>No quizzes found for this section.</strong></p>
          <p>Make sure you have published quizzes for this subject and section.</p>
        </div>
        
        <table class="grade-table">
          <thead>
            <tr>
              <th class="student-column">
                <div class="column-header">
                  <span>Student</span>
                </div>
              </th>
              <th v-for="quiz in displayedQuizzes" :key="quiz.id" class="quiz-column">
                <div class="column-header quiz-header">
                  <span class="quiz-title">{{ quiz.title }}</span>
                  <small class="quiz-points">({{ quiz.total_points || 100 }} pts)</small>
                </div>
              </th>
              <th v-if="quizzes.length === 0" class="no-quizzes-column">
                <div class="column-header">
                  <span>No Quizzes</span>
                  <small>Publish quizzes to see grades</small>
                </div>
              </th>
              <th class="average-column">
                <div class="column-header">
                  <span>Average</span>
                  <small>Overall Grade</small>
                </div>
              </th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="student in filteredStudents" :key="student.id" class="student-row">
              <td class="student-column">
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
              <td v-for="quiz in displayedQuizzes" :key="quiz.id" class="quiz-column">
                <div class="grade-cell">
                  <input
                    v-if="viewMode === 'edit'"
                    :value="getGradeValue(student.id, quiz.id)"
                    @input="updateGrade(student.id, quiz.id, $event)"
                    @blur="saveGradeToDatabase(student.id, quiz.id)"
                    type="number"
                    :min="0"
                    :max="quiz.total_points || 100"
                    class="grade-input"
                    :placeholder="`0/${quiz.total_points || 100}`"
                  />
                  <div v-else class="grade-display" :class="getGradeClass(getGradeValue(student.id, quiz.id), quiz.total_points || 100)">
                    <span class="grade-score">{{ getGradeValue(student.id, quiz.id) }}</span>
                    <span class="grade-separator">/</span>
                    <span class="grade-total">{{ quiz.total_points || 100 }}</span>
                    <div class="grade-percentage">
                      {{ formatGrade(getGradeValue(student.id, quiz.id), quiz.total_points || 100) }}
                    </div>
                  </div>
                </div>
              </td>
              <td v-if="quizzes.length === 0" class="no-quizzes-column">
                <div class="no-quiz-message">
                  <span>No quizzes</span>
                </div>
              </td>
              <td class="average-column">
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
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, computed, watch } from 'vue'
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

interface Quiz {
  id: string
  title: string
  total_points: number
  created_at: string
  status?: string
}

interface QuizResult {
  id: string
  quiz_id: string
  student_id: string
  best_score: number
  best_percentage: number
}

const { isDarkMode, initDarkMode } = useDarkMode()
const router = useRouter()
const route = useRoute()

const students = ref<Student[]>([])
const quizzes = ref<Quiz[]>([])
const grades = ref<Record<string, Record<string, number>>>({})
const quizResults = ref<QuizResult[]>([])
const subject = ref<any>(null)
const section = ref<any>(null)
const subjectId = ref(route.params.subjectId as string)
const sectionId = ref(route.params.sectionId as string)

const isLoading = ref(false)
const loadingMessage = ref('')
const viewMode = ref('edit')
const selectedQuiz = ref('')
const showGradeSettings = ref(false)
const showToast = ref(false)
const toastMessage = ref('')
const toastType = ref('success')

const gradeScale = ref({ A: 90, B: 80, C: 70, D: 60 })
const displayOptions = ref({ showPercentages: true, showLetterGrades: false, roundToWhole: true })

const filteredStudents = computed(() => [...students.value])
const displayedQuizzes = computed(() => selectedQuiz.value ? quizzes.value.filter(q => q.id === selectedQuiz.value) : quizzes.value)

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

const updateGrade = (studentId: string, quizId: string, event: Event) => {
  const target = event.target as HTMLInputElement
  const newGrade = Number(target.value)
  
  if (!grades.value[studentId]) grades.value[studentId] = {}
  grades.value[studentId][quizId] = newGrade
  calculateStudentAverage(studentId)
}

const saveGradeToDatabase = async (studentId: string, quizId: string) => {
  const grade = getGradeValue(studentId, quizId)
  const quiz = quizzes.value.find(q => q.id === quizId)
  if (!quiz) return
  
  try {
    const percentage = (grade / quiz.total_points) * 100
    const { error } = await supabase.from('quiz_results').upsert({
      quiz_id: quizId,
      student_id: studentId,
      best_score: grade,
      best_percentage: percentage,
      status: 'graded',
      finalized: true,
      visible_to_student: true,
      updated_at: new Date().toISOString()
    }, { onConflict: 'quiz_id,student_id' })
    
    if (error) throw error
    showToastMessage('Grade saved successfully!', 'success')
  } catch (error) {
    console.error('Error saving grade:', error)
    showToastMessage('Failed to save grade. Please try again.', 'error')
  }
}

const calculateStudentAverage = (studentId: string) => {
  const studentGrades = grades.value[studentId]
  if (!studentGrades) return

  const gradeValues = Object.entries(studentGrades).map(([quizId, grade]) => {
    const quiz = quizzes.value.find(q => q.id === quizId)
    return quiz ? (Number(grade) / quiz.total_points) * 100 : 0
  }).filter(val => val > 0)

  if (gradeValues.length > 0) {
    const average = gradeValues.reduce((a, b) => a + b, 0) / gradeValues.length
    const student = students.value.find(s => s.id === studentId)
    if (student) student.average = average
  }
}

const filterByQuiz = () => {
  console.log('Filtering by quiz:', selectedQuiz.value)
}

const changeViewMode = () => {
  console.log('View mode changed to:', viewMode.value)
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
    
    const { data: quizzesData, error: quizzesError } = await supabase
      .from('quizzes').select('id, title, created_at, status')
      .eq('subject_id', subjectId.value).eq('section_id', sectionId.value)
      .eq('status', 'published').order('created_at', { ascending: true })
    
    if (quizzesError) throw quizzesError
    
    const quizzesWithPoints: Quiz[] = []
    for (const quiz of quizzesData || []) {
      const { data: questionsData } = await supabase
        .from('quiz_questions').select('points').eq('quiz_id', quiz.id)
      
      const totalPoints = questionsData?.reduce((sum, q) => sum + (q.points || 0), 0) || 100
      
      quizzesWithPoints.push({
        id: quiz.id,
        title: quiz.title,
        created_at: quiz.created_at,
        status: quiz.status,
        total_points: totalPoints
      })
    }
    
    quizzes.value = quizzesWithPoints
    
    if (quizzes.value.length > 0 && students.value.length > 0) {
      const { data: resultsData, error: resultsError } = await supabase
        .from('quiz_results').select('*')
        .in('quiz_id', quizzes.value.map(q => q.id))
        .in('student_id', students.value.map(s => s.id))
      
      if (resultsError) throw resultsError
      
      quizResults.value = resultsData || []
      grades.value = {}
      resultsData?.forEach((result: QuizResult) => {
        if (!grades.value[result.student_id]) grades.value[result.student_id] = {}
        grades.value[result.student_id][result.quiz_id] = result.best_score || 0
      })
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
  router.push({ 
    name: 'ViewStudents', 
    params: { subjectId: subjectId.value, sectionId: sectionId.value } 
  })
}

const exportGrades = () => {
  if (students.value.length === 0) {
    showToastMessage('No data to export', 'error')
    return
  }
  
  try {
    let csv = 'Student Name,Email,' + quizzes.value.map(q => q.title).join(',') + ',Average\n'
    
    students.value.forEach(student => {
      csv += `"${student.first_name} ${student.last_name}","${student.email}",`
      quizzes.value.forEach(quiz => {
        const grade = getGradeValue(student.id, quiz.id)
        const percentage = quiz.total_points ? Math.round((grade / quiz.total_points) * 100) : 0
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
  await fetchData()
})
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

* { margin: 0; padding: 0; box-sizing: border-box; }

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

.table-wrapper { overflow-x: auto; }
.grade-table { width: 100%; border-collapse: collapse; min-width: 800px; }

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

/* Responsive */
@media (max-width: 1024px) {
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
  .grade-management-page {
    padding: 1rem;
  }
  
  .header-content {
    flex-direction: column;
    gap: 1rem;
    align-items: flex-start;
  }
  
  .back-btn {
    width: 100%;
    justify-content: center;
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

</style>
