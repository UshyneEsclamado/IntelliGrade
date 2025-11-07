<template>
  <div class="analytics-container" :class="{ 'dark': isDarkMode }">
    <!-- Simple Header -->
    <div class="header-card">
      <div class="header-content">
        <div class="header-left">
          <div class="header-icon">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="currentColor">
              <path d="M22,21H2V3H4V19H6V10H10V19H12V6H16V19H18V14H22V21Z" />
            </svg>
          </div>
          <div>
            <h1 class="header-title">Student Analytics</h1>
            <p class="header-subtitle">Monitor and analyze student performance</p>
          </div>
        </div>
        
        <div class="header-actions">
          <select v-model="selectedSection" @change="filterBySection" class="section-filter">
            <option value="">All Sections</option>
            <option v-for="section in sections" :key="section.id" :value="section.id">
              {{ section.name }} - {{ section.subject_name }}
            </option>
          </select>
          <button @click="exportData" class="grade-btn export-btn">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" style="margin-right:8px;vertical-align:middle;">
              <path d="M14,2H6A2,2 0 0,0 4,4V20A2,2 0 0,0 6,22H18A2,2 0 0,0 20,20V8L14,2M18,20H6V4H13V9H18V20Z" fill="currentColor"/>
            </svg>
            <span style="vertical-align:middle;">Export Data</span>
          </button>
        </div>
      </div>
    </div>

    <!-- Loading Overlay -->
    <div v-if="loading" class="loading-overlay">
      <div class="loading-content">
        <div class="loading-spinner-container">
          <div class="loading-spinner"></div>
        </div>
        <p class="loading-text">Loading analytics...</p>
      </div>
    </div>

    <!-- Stats Cards -->
    <div v-else class="stats-grid">
      <div class="stat-card">
        <div class="stat-icon stat-average">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
            <path d="M16,6L18.29,8.29L13.41,13.17L9.41,9.17L2,16.59L3.41,18L9.41,12L13.41,16L19.71,9.71L22,12V6H16Z" />
          </svg>
        </div>
        <div>
          <div class="stat-number">{{ overallStats.averageScore }}%</div>
          <div class="stat-label">Overall Average</div>
        </div>
      </div>

      <div class="stat-card">
        <div class="stat-icon stat-students">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
            <path d="M12,5.5A3.5,3.5 0 0,1 15.5,9A3.5,3.5 0 0,1 12,12.5A3.5,3.5 0 0,1 8.5,9A3.5,3.5 0 0,1 12,5.5M5,8C5.56,8 6.08,8.15 6.53,8.42C6.38,9.85 6.8,11.27 7.66,12.38C7.16,13.34 6.16,14 5,14A3,3 0 0,1 2,11A3,3 0 0,1 5,8M19,8A3,3 0 0,1 22,11A3,3 0 0,1 19,14C17.84,14 16.84,13.34 16.34,12.38C17.2,11.27 17.62,9.85 17.47,8.42C17.92,8.15 18.44,8 19,8M5.5,18.25C5.5,16.18 8.41,14.5 12,14.5C15.59,14.5 18.5,16.18 18.5,18.25V20H5.5V18.25M0,20V18.5C0,17.11 1.89,15.94 4.45,15.6C3.86,16.28 3.5,17.22 3.5,18.25V20H0M24,20H20.5V18.25C20.5,17.22 20.14,16.28 19.55,15.6C22.11,15.94 24,17.11 24,18.5V20Z" />
          </svg>
        </div>
        <div>
          <div class="stat-number">{{ overallStats.totalStudents }}</div>
          <div class="stat-label">Total Students</div>
        </div>
      </div>

      <div class="stat-card">
        <div class="stat-icon stat-assessments">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
            <path d="M19,3H5C3.9,3 3,3.9 3,5V19C3,20.1 3.9,21 5,21H19C20.1,21 21,20.1 21,19V5C21,3.9 20.1,3 19,3M9,17H7V10H9V17M13,17H11V7H13V17M17,17H15V13H17V17Z" />
          </svg>
        </div>
        <div>
          <div class="stat-number">{{ overallStats.totalQuizzes }}</div>
          <div class="stat-label">Quizzes Created</div>
        </div>
      </div>
    </div>

    <!-- Content Grid -->
    <div v-if="!loading" class="content-grid">
      <!-- Quiz Performance -->
      <div class="content-card">
        <div class="card-header">
          <h3>Quiz Performance Summary</h3>
          <p class="card-desc">Average scores across all quizzes</p>
        </div>
        <div class="chart-placeholder">
          <div v-if="quizPerformanceData.length > 0" class="performance-list">
            <div v-for="quiz in quizPerformanceData" :key="quiz.quiz_id" class="performance-item">
              <div class="quiz-info">
                <div class="quiz-title">{{ quiz.quiz_title }}</div>
                <div class="quiz-meta">{{ quiz.total_attempts }} attempts • {{ quiz.students_attempted }} students</div>
              </div>
              <div class="quiz-score">
                <span :class="['score-badge', getScoreClass(quiz.average_score)]">
                  {{ quiz.average_score }}%
                </span>
              </div>
            </div>
          </div>
          <div v-else class="empty-state">
            No quiz data available yet. Students need to take quizzes first.
          </div>
        </div>
      </div>

      <!-- Student Distribution -->
      <div class="content-card">
        <div class="card-header">
          <h3>Student Performance Distribution</h3>
          <p class="card-desc">Count of students by performance level</p>
        </div>
        <div class="chart-placeholder">
          <div v-if="performanceDistribution" class="distribution-list">
            <div class="dist-item">
              <span class="dist-label excellent">Excellent (90+)</span>
              <span class="dist-count">{{ performanceDistribution.excellent }}</span>
            </div>
            <div class="dist-item">
              <span class="dist-label good">Good (80-89)</span>
              <span class="dist-count">{{ performanceDistribution.good }}</span>
            </div>
            <div class="dist-item">
              <span class="dist-label satisfactory">Satisfactory (75-79)</span>
              <span class="dist-count">{{ performanceDistribution.satisfactory }}</span>
            </div>
            <div class="dist-item">
              <span class="dist-label warning">Needs Help (<75)</span>
              <span class="dist-count">{{ performanceDistribution.needsHelp }}</span>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Student Performance Table -->
    <div v-if="!loading" class="content-card">
      <div class="card-header">
        <h3>Student Performance Overview</h3>
        <p class="card-desc">Quiz results and performance data for each student</p>
        <div class="table-controls">
          <input 
            v-model="searchQuery" 
            type="text" 
            placeholder="Search students..."
            class="search-input"
          >
          <select v-model="sortBy" @change="sortStudents" class="sort-select">
            <option value="name">Sort by Name</option>
            <option value="average">Sort by Average Score</option>
            <option value="quizzes">Sort by Quizzes Taken</option>
          </select>
        </div>
      </div>

      <div class="table-wrapper">
        <table class="performance-table">
          <thead>
            <tr>
              <th>Student</th>
              <th>Section</th>
              <th>Subject</th>
              <th>Quizzes Taken</th>
              <th>Average Score</th>
              <th>Best Score</th>
              <th>Status</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="student in filteredStudents" :key="student.student_id" class="student-row">
              <td class="student-cell">
                <div class="student-info">
                  <div class="student-avatar">
                    <div class="avatar-placeholder">
                      {{ getInitials(student.student_name) }}
                    </div>
                  </div>
                  <div>
                    <div class="student-name">{{ student.student_name }}</div>
                    <div class="student-id">ID: {{ student.student_number }}</div>
                  </div>
                </div>
              </td>
              <td>{{ student.section_name }}</td>
              <td>{{ student.subject_name }}</td>
              <td>{{ student.quizzes_attempted }}</td>
              <td>{{ student.average_score || 0 }}%</td>
              <td>
                <span :class="['score-badge', getScoreClass(student.best_score || 0)]">
                  {{ student.best_score || 0 }}%
                </span>
              </td>
              <td>
                <span :class="['status-badge', getStatusClass(student.average_score || 0)]">
                  {{ student.performance_status }}
                </span>
              </td>
              <td class="actions-cell">
                <button @click="viewStudentDetails(student)" class="action-btn view-btn" title="View Details">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M12,9A3,3 0 0,0 9,12A3,3 0 0,0 12,15A3,3 0 0,0 15,12A3,3 0 0,0 12,9M12,17A5,5 0 0,1 7,12A5,5 0 0,1 12,7A5,5 0 0,1 17,12A5,5 0 0,1 12,17M12,4.5C7,4.5 2.73,7.61 1,12C2.73,16.39 7,19.5 12,19.5C17,19.5 21.27,16.39 23,12C21.27,7.61 17,4.5 12,4.5Z" />
                  </svg>
                </button>
              </td>
            </tr>
            <tr v-if="filteredStudents.length === 0">
              <td colspan="8" style="text-align: center; padding: 2rem; color: #999;">
                {{ studentData.length === 0 ? 'No student data yet. Students need to take quizzes first.' : 'No students match your search.' }}
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- Pagination -->
      <div class="pagination">
        <button 
          @click="currentPage = Math.max(1, currentPage - 1)"
          :disabled="currentPage === 1"
          class="page-btn"
        >
          Previous
        </button>
        <span class="page-info">
          Page {{ currentPage }} of {{ totalPages }}
        </span>
        <button 
          @click="currentPage = Math.min(totalPages, currentPage + 1)"
          :disabled="currentPage === totalPages"
          class="page-btn"
        >
          Next
        </button>
      </div>
    </div>

    <!-- Student Detail Modal -->
    <div v-if="selectedStudent" class="modal-overlay" @click.self="selectedStudent = null">
      <div class="modal student-detail-modal">
        <div class="modal-header">
          <h3>{{ selectedStudent.student_name }} - Quiz Results</h3>
          <button @click="selectedStudent = null" class="close-btn">✕</button>
        </div>
        
        <div class="modal-content">
          <div class="student-summary">
            <div class="summary-stat">
              <h4>{{ selectedStudent.average_score || 0 }}%</h4>
              <p>Average Score</p>
            </div>
            <div class="summary-stat">
              <h4>{{ selectedStudent.total_quiz_attempts }}</h4>
              <p>Total Attempts</p>
            </div>
            <div class="summary-stat">
              <h4>{{ selectedStudent.best_score || 0 }}%</h4>
              <p>Best Score</p>
            </div>
          </div>

          <div class="quiz-history">
            <h4>Quiz Attempts</h4>
            <div v-if="studentQuizResults.length > 0" class="history-list">
              <div v-for="result in studentQuizResults" :key="result.attempt_id" class="history-item">
                <div class="quiz-info">
                  <h5>{{ result.quiz_title }}</h5>
                  <p>Attempt {{ result.attempt_number }} • {{ formatDate(result.submitted_at) }}</p>
                </div>
                <div class="quiz-score">
                  <span :class="['score-badge', getScoreClass(result.percentage)]">
                    {{ Math.round(result.percentage) }}%
                  </span>
                </div>
              </div>
            </div>
            <div v-else class="empty-state">
              No quiz attempts yet
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { ref, onMounted, computed, onUnmounted } from 'vue'
import { supabase } from '../../supabase.js'
import { useDarkMode } from '../../composables/useDarkMode.js'

interface Section {
  id: string
  name: string
  subject_name: string
}

interface StudentData {
  student_id: string
  student_name: string
  student_number: string
  student_email: string
  grade_level: number
  section_id: string
  section_name: string
  section_code: string
  subject_id: string
  subject_name: string
  teacher_id: string
  teacher_name: string
  total_quiz_attempts: number
  quizzes_attempted: number
  average_score: number
  best_score: number
  lowest_score: number
  last_quiz_date: string
  attempts_last_week: number
  performance_status: string
}

interface QuizPerformance {
  quiz_id: string
  quiz_title: string
  quiz_code: string
  section_id: string
  section_name: string
  subject_id: string
  subject_name: string
  teacher_id: string
  teacher_name: string
  total_attempts: number
  students_attempted: number
  average_score: number
  highest_score: number
  lowest_score: number
  count_excellent: number
  count_good: number
  count_satisfactory: number
  count_needs_help: number
}

interface QuizResult {
  attempt_id: string
  quiz_id: string
  quiz_title: string
  attempt_number: number
  percentage: number
  submitted_at: string
}

export default {
  name: 'AnalyticsView',
  setup() {
    const { isDarkMode, initDarkMode } = useDarkMode()
    
    const sections = ref<Section[]>([])
    const studentData = ref<StudentData[]>([])
    const quizPerformanceData = ref<QuizPerformance[]>([])
    const selectedSection = ref('')
    const searchQuery = ref('')
    const sortBy = ref('name')
    const currentPage = ref(1)
    const itemsPerPage = 10
    const loading = ref(false)
    const selectedStudent = ref<StudentData | null>(null)
    const studentQuizResults = ref<QuizResult[]>([])
    const teacherId = ref<string>('')
    
    // Real-time subscription channels
    let quizAttemptsSubscription: any = null
    let quizzesSubscription: any = null
    let enrollmentsSubscription: any = null

    // Computed properties
    const overallStats = computed(() => {
      let students = studentData.value
      if (selectedSection.value) {
        students = students.filter(s => s.section_id === selectedSection.value)
      }

      const totalStudents = students.length
      
      // Count unique quizzes from quiz performance data
      let quizzes = quizPerformanceData.value
      if (selectedSection.value) {
        quizzes = quizzes.filter(q => q.section_id === selectedSection.value)
      }
      const totalQuizzes = quizzes.length
      
      // Calculate average score from students who have taken quizzes
      const studentsWithScores = students.filter(s => s.average_score > 0)
      const averageScore = studentsWithScores.length > 0 
        ? Math.round(studentsWithScores.reduce((sum, s) => sum + s.average_score, 0) / studentsWithScores.length)
        : 0

      return {
        totalStudents,
        totalQuizzes,
        averageScore
      }
    })

    const performanceDistribution = computed(() => {
      let students = studentData.value
      if (selectedSection.value) {
        students = students.filter(s => s.section_id === selectedSection.value)
      }

      // Only count students who have taken at least one quiz
      const studentsWithScores = students.filter(s => s.average_score > 0)

      return {
        excellent: studentsWithScores.filter(s => s.average_score >= 90).length,
        good: studentsWithScores.filter(s => s.average_score >= 80 && s.average_score < 90).length,
        satisfactory: studentsWithScores.filter(s => s.average_score >= 75 && s.average_score < 80).length,
        needsHelp: studentsWithScores.filter(s => s.average_score < 75).length
      }
    })

    const filteredStudents = computed(() => {
      let filtered = studentData.value

      // Filter by section
      if (selectedSection.value) {
        filtered = filtered.filter(s => s.section_id === selectedSection.value)
      }

      // Filter by search query
      if (searchQuery.value) {
        const query = searchQuery.value.toLowerCase()
        filtered = filtered.filter(s => 
          s.student_name.toLowerCase().includes(query) ||
          s.student_number.toLowerCase().includes(query) ||
          s.student_email.toLowerCase().includes(query)
        )
      }

      // Sort students
      filtered.sort((a, b) => {
        switch (sortBy.value) {
          case 'average':
            return (b.average_score || 0) - (a.average_score || 0)
          case 'quizzes':
            return b.quizzes_attempted - a.quizzes_attempted
          default: // 'name'
            return a.student_name.localeCompare(b.student_name)
        }
      })

      // Paginate
      const start = (currentPage.value - 1) * itemsPerPage
      return filtered.slice(start, start + itemsPerPage)
    })

    const totalPages = computed(() => {
      let filtered = studentData.value
      
      if (selectedSection.value) {
        filtered = filtered.filter(s => s.section_id === selectedSection.value)
      }
      
      if (searchQuery.value) {
        const query = searchQuery.value.toLowerCase()
        filtered = filtered.filter(s => 
          s.student_name.toLowerCase().includes(query) ||
          s.student_number.toLowerCase().includes(query)
        )
      }
      
      return Math.ceil(filtered.length / itemsPerPage) || 1
    })

    // Get current teacher ID
    const getCurrentTeacherId = async () => {
      try {
        const { data: { session }, error: sessionError } = await supabase.auth.getSession()
        
        if (sessionError || !session?.user) {
          console.error('No session found')
          return null
        }

        const { data: profile, error: profileError } = await supabase
          .from('profiles')
          .select('id, role')
          .eq('auth_user_id', session.user.id)
          .single()

        if (profileError || !profile || profile.role !== 'teacher') {
          console.error('Teacher profile not found')
          return null
        }

        const { data: teacher, error: teacherError } = await supabase
          .from('teachers')
          .select('id')
          .eq('profile_id', profile.id)
          .single()

        if (teacherError || !teacher) {
          console.error('Teacher not found')
          return null
        }

        return teacher.id
      } catch (error) {
        console.error('Error getting teacher ID:', error)
        return null
      }
    }

    // Fetch student performance data with manual calculation
    const fetchStudentPerformanceData = async (currentTeacherId: string) => {
      try {
        console.log('Fetching student performance data...')
        
        // Get all enrolled students in teacher's sections
        const { data: enrollments, error: enrollError } = await supabase
          .from('enrollments')
          .select(`
            student_id,
            section_id,
            subject_id,
            students!inner (
              id,
              student_id,
              full_name,
              email,
              grade_level
            ),
            sections!inner (
              id,
              name,
              section_code,
              subjects!inner (
                id,
                name,
                teacher_id,
                teachers!inner (
                  id,
                  full_name
                )
              )
            )
          `)
          .eq('status', 'active')
          .eq('sections.subjects.teacher_id', currentTeacherId)

        if (enrollError) throw enrollError

        if (!enrollments || enrollments.length === 0) {
          console.log('No enrollments found')
          studentData.value = []
          return
        }

        // Get all quiz attempts for these students
        const studentIds = enrollments.map((e: any) => e.student_id)
        
        const { data: attempts, error: attemptsError } = await supabase
          .from('quiz_attempts')
          .select(`
            id,
            student_id,
            quiz_id,
            percentage,
            submitted_at,
            attempt_number,
            status,
            quizzes!inner (
              id,
              title,
              section_id
            )
          `)
          .in('student_id', studentIds)
          .in('status', ['submitted', 'graded'])

        if (attemptsError) throw attemptsError

        console.log('Found attempts:', attempts?.length || 0)

        // Calculate stats for each student
        const studentStats = enrollments.map((enrollment: any) => {
          const student = enrollment.students
          const section = enrollment.sections
          const subject = section.subjects
          const teacher = subject.teachers

          // Get all attempts for this student in this teacher's sections
          const studentAttempts = (attempts || []).filter((a: any) => 
            a.student_id === student.id &&
            enrollments.some((e: any) => 
              e.student_id === student.id && 
              e.section_id === a.quizzes.section_id
            )
          )

          // Calculate statistics
          const totalAttempts = studentAttempts.length
          const uniqueQuizzes = new Set(studentAttempts.map((a: any) => a.quiz_id)).size
          
          let averageScore = 0
          let bestScore = 0
          let lowestScore = 0
          let lastQuizDate = ''
          let performanceStatus = 'No Data'

          if (totalAttempts > 0) {
            const scores = studentAttempts.map((a: any) => a.percentage || 0)
            averageScore = Math.round(scores.reduce((sum, score) => sum + score, 0) / scores.length)
            bestScore = Math.max(...scores)
            lowestScore = Math.min(...scores)
            
            // Get most recent attempt date
            const sortedAttempts = studentAttempts.sort((a: any, b: any) => 
              new Date(b.submitted_at).getTime() - new Date(a.submitted_at).getTime()
            )
            lastQuizDate = sortedAttempts[0]?.submitted_at || ''

            // Determine performance status
            if (averageScore >= 90) performanceStatus = 'Excellent'
            else if (averageScore >= 80) performanceStatus = 'Good'
            else if (averageScore >= 75) performanceStatus = 'Satisfactory'
            else performanceStatus = 'Needs Help'
          }

          // Count attempts in last week
          const oneWeekAgo = new Date()
          oneWeekAgo.setDate(oneWeekAgo.getDate() - 7)
          const attemptsLastWeek = studentAttempts.filter((a: any) => 
            new Date(a.submitted_at) >= oneWeekAgo
          ).length

          return {
            student_id: student.id,
            student_name: student.full_name,
            student_number: student.student_id,
            student_email: student.email,
            grade_level: student.grade_level,
            section_id: section.id,
            section_name: section.name,
            section_code: section.section_code,
            subject_id: subject.id,
            subject_name: subject.name,
            teacher_id: teacher.id,
            teacher_name: teacher.full_name,
            total_quiz_attempts: totalAttempts,
            quizzes_attempted: uniqueQuizzes,
            average_score: averageScore,
            best_score: bestScore,
            lowest_score: lowestScore,
            last_quiz_date: lastQuizDate,
            attempts_last_week: attemptsLastWeek,
            performance_status: performanceStatus
          }
        })

        studentData.value = studentStats
        console.log('Student data updated:', studentStats.length, 'students')

      } catch (error) {
        console.error('Error fetching student performance:', error)
        studentData.value = []
      }
    }

    // Fetch quiz performance data with manual calculation
    const fetchQuizPerformanceData = async (currentTeacherId: string) => {
      try {
        console.log('Fetching quiz performance data...')

        // Get all quizzes for this teacher
        const { data: quizzes, error: quizzesError } = await supabase
          .from('quizzes')
          .select(`
            id,
            title,
            quiz_code,
            section_id,
            sections!inner (
              id,
              name,
              subject_id,
              subjects!inner (
                id,
                name,
                teacher_id,
                teachers!inner (
                  id,
                  full_name
                )
              )
            )
          `)
          .eq('sections.subjects.teacher_id', currentTeacherId)

        if (quizzesError) throw quizzesError

        if (!quizzes || quizzes.length === 0) {
          console.log('No quizzes found')
          quizPerformanceData.value = []
          return
        }

        // Get all attempts for these quizzes
        const quizIds = quizzes.map((q: any) => q.id)
        
        const { data: attempts, error: attemptsError } = await supabase
          .from('quiz_attempts')
          .select('id, quiz_id, student_id, percentage, status')
          .in('quiz_id', quizIds)
          .in('status', ['submitted', 'graded'])

        if (attemptsError) throw attemptsError

        console.log('Found quiz attempts:', attempts?.length || 0)

        // Calculate stats for each quiz
        const quizStats = quizzes.map((quiz: any) => {
          const section = quiz.sections
          const subject = section.subjects
          const teacher = subject.teachers

          // Get all attempts for this quiz
          const quizAttempts = (attempts || []).filter((a: any) => a.quiz_id === quiz.id)
          
          const totalAttempts = quizAttempts.length
          const uniqueStudents = new Set(quizAttempts.map((a: any) => a.student_id)).size

          let averageScore = 0
          let highestScore = 0
          let lowestScore = 0
          let countExcellent = 0
          let countGood = 0
          let countSatisfactory = 0
          let countNeedsHelp = 0

          if (totalAttempts > 0) {
            const scores = quizAttempts.map((a: any) => a.percentage || 0)
            averageScore = Math.round(scores.reduce((sum, score) => sum + score, 0) / scores.length)
            highestScore = Math.max(...scores)
            lowestScore = Math.min(...scores)

            // Count by performance level
            scores.forEach(score => {
              if (score >= 90) countExcellent++
              else if (score >= 80) countGood++
              else if (score >= 75) countSatisfactory++
              else countNeedsHelp++
            })
          }

          return {
            quiz_id: quiz.id,
            quiz_title: quiz.title,
            quiz_code: quiz.quiz_code,
            section_id: section.id,
            section_name: section.name,
            subject_id: subject.id,
            subject_name: subject.name,
            teacher_id: teacher.id,
            teacher_name: teacher.full_name,
            total_attempts: totalAttempts,
            students_attempted: uniqueStudents,
            average_score: averageScore,
            highest_score: highestScore,
            lowest_score: lowestScore,
            count_excellent: countExcellent,
            count_good: countGood,
            count_satisfactory: countSatisfactory,
            count_needs_help: countNeedsHelp
          }
        })

        quizPerformanceData.value = quizStats
        console.log('Quiz performance data updated:', quizStats.length, 'quizzes')

      } catch (error) {
        console.error('Error fetching quiz performance:', error)
        quizPerformanceData.value = []
      }
    }

    // Fetch all analytics data
    const fetchData = async () => {
      loading.value = true
      try {
        const currentTeacherId = await getCurrentTeacherId()
        if (!currentTeacherId) {
          console.error('Could not get teacher ID')
          loading.value = false
          return
        }

        teacherId.value = currentTeacherId
        console.log('Teacher ID:', currentTeacherId)

        // Fetch both student and quiz performance data
        await Promise.all([
          fetchStudentPerformanceData(currentTeacherId),
          fetchQuizPerformanceData(currentTeacherId)
        ])

        // Build unique sections list for filter
        const uniqueSections = new Map()
        studentData.value.forEach(s => {
          if (!uniqueSections.has(s.section_id)) {
            uniqueSections.set(s.section_id, {
              id: s.section_id,
              name: s.section_name,
              subject_name: s.subject_name
            })
          }
        })
        sections.value = Array.from(uniqueSections.values())

        console.log('Data loaded successfully:', {
          students: studentData.value.length,
          quizzes: quizPerformanceData.value.length,
          sections: sections.value.length
        })

      } catch (error) {
        console.error('Error fetching analytics data:', error)
      } finally {
        loading.value = false
      }
    }

    // Setup real-time subscriptions
    const setupRealtimeSubscriptions = async () => {
      if (!teacherId.value) return

      console.log('Setting up real-time subscriptions...')

      // Subscribe to quiz attempts changes
      quizAttemptsSubscription = supabase
        .channel('quiz_attempts_changes')
        .on(
          'postgres_changes',
          {
            event: '*',
            schema: 'public',
            table: 'quiz_attempts'
          },
          async (payload) => {
            console.log('Quiz attempt changed:', payload)
            // Refresh data when attempts are created, updated, or deleted
            await fetchStudentPerformanceData(teacherId.value)
            await fetchQuizPerformanceData(teacherId.value)
          }
        )
        .subscribe()

      // Subscribe to quizzes changes
      quizzesSubscription = supabase
        .channel('quizzes_changes')
        .on(
          'postgres_changes',
          {
            event: '*',
            schema: 'public',
            table: 'quizzes'
          },
          async (payload) => {
            console.log('Quiz changed:', payload)
            // Refresh quiz performance data
            await fetchQuizPerformanceData(teacherId.value)
          }
        )
        .subscribe()

      // Subscribe to enrollments changes
      enrollmentsSubscription = supabase
        .channel('enrollments_changes')
        .on(
          'postgres_changes',
          {
            event: '*',
            schema: 'public',
            table: 'enrollments'
          },
          async (payload) => {
            console.log('Enrollment changed:', payload)
            // Refresh student data
            await fetchStudentPerformanceData(teacherId.value)
          }
        )
        .subscribe()

      console.log('Real-time subscriptions active')
    }

    // Cleanup subscriptions
    const cleanupSubscriptions = () => {
      if (quizAttemptsSubscription) {
        supabase.removeChannel(quizAttemptsSubscription)
        quizAttemptsSubscription = null
      }
      if (quizzesSubscription) {
        supabase.removeChannel(quizzesSubscription)
        quizzesSubscription = null
      }
      if (enrollmentsSubscription) {
        supabase.removeChannel(enrollmentsSubscription)
        enrollmentsSubscription = null
      }
      console.log('Real-time subscriptions cleaned up')
    }

    // View student details
    const viewStudentDetails = async (student: StudentData) => {
      selectedStudent.value = student

      try {
        // Fetch individual quiz attempts for this student
        const { data: attempts, error } = await supabase
          .from('quiz_attempts')
          .select(`
            id,
            quiz_id,
            attempt_number,
            percentage,
            submitted_at,
            quizzes (
              title
            )
          `)
          .eq('student_id', student.student_id)
          .in('status', ['submitted', 'graded'])
          .order('submitted_at', { ascending: false })

        if (error) throw error

        if (attempts) {
          studentQuizResults.value = attempts.map((a: any) => ({
            attempt_id: a.id,
            quiz_id: a.quiz_id,
            quiz_title: a.quizzes?.title || `Quiz ${a.quiz_id.slice(0, 8)}`,
            attempt_number: a.attempt_number,
            percentage: a.percentage || 0,
            submitted_at: a.submitted_at
          }))
        }
      } catch (error) {
        console.error('Error fetching student details:', error)
        studentQuizResults.value = []
      }
    }

    // Filter by section
    const filterBySection = () => {
      currentPage.value = 1
    }

    // Sort students
    const sortStudents = () => {
      currentPage.value = 1
    }

    // Export data to CSV
    const exportData = () => {
      const headers = ['Student Name', 'ID', 'Section', 'Subject', 'Average Score', 'Best Score', 'Quizzes Taken', 'Status']
      const csvData = studentData.value.map(student => [
        student.student_name,
        student.student_number,
        student.section_name,
        student.subject_name,
        student.average_score || 0,
        student.best_score || 0,
        student.quizzes_attempted,
        student.performance_status
      ])

      const csvContent = [headers, ...csvData]
        .map(row => row.map(field => `"${field}"`).join(','))
        .join('\n')

      const blob = new Blob([csvContent], { type: 'text/csv' })
      const url = window.URL.createObjectURL(blob)
      const link = document.createElement('a')
      link.href = url
      link.download = `student_analytics_${new Date().toISOString().split('T')[0]}.csv`
      link.click()
      window.URL.revokeObjectURL(url)
    }

    // Helper functions
    const getInitials = (name: string) => {
      return name.split(' ').map(n => n[0]).join('').toUpperCase().slice(0, 2)
    }

    const getScoreClass = (score: number) => {
      if (score >= 90) return 'excellent'
      if (score >= 80) return 'good'
      if (score >= 75) return 'satisfactory'
      return 'needs-improvement'
    }

    const getStatusClass = (score: number) => {
      if (score >= 90) return 'excellent'
      if (score >= 80) return 'good'
      if (score >= 75) return 'satisfactory'
      return 'warning'
    }

    const formatDate = (dateString: string) => {
      if (!dateString) return 'N/A'
      return new Date(dateString).toLocaleDateString('en-US', {
        year: 'numeric',
        month: 'short',
        day: 'numeric'
      })
    }

    // Lifecycle
    onMounted(async () => {
      initDarkMode()
      await fetchData()
      await setupRealtimeSubscriptions()
    })

    onUnmounted(() => {
      cleanupSubscriptions()
    })

    return {
      isDarkMode,
      sections,
      studentData,
      quizPerformanceData,
      selectedSection,
      searchQuery,
      sortBy,
      currentPage,
      itemsPerPage,
      loading,
      selectedStudent,
      studentQuizResults,
      overallStats,
      performanceDistribution,
      filteredStudents,
      totalPages,
      fetchData,
      filterBySection,
      sortStudents,
      viewStudentDetails,
      exportData,
      getInitials,
      getScoreClass,
      getStatusClass,
      formatDate
    }
  }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.analytics-container {
  min-height: 100vh;
  background: #FBFFE4;
  padding: 1.5rem;
  font-family: 'Inter', sans-serif;
}
.dark .analytics-container {
  background: #181c20;
}

/* Header */
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
  flex-wrap: wrap;
}

.section-filter {
  padding: 0.75rem 1rem;
  border: 1px solid #A3D1C6;
  border-radius: 8px;
  background: white;
  color: #3D8D7A;
  font-size: 0.875rem;
  font-weight: 500;
}
.dark .section-filter {
  background: #23272b;
  border-color: #3D8D7A;
  color: #A3D1C6;
}

  .export-btn {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    background: #20c997;
    color: #181c20;
    border: 1px solid #A3D1C6;
    padding: 0.5rem 1.25rem;
    border-radius: 8px;
    font-size: 0.875rem;
    font-weight: 500;
    cursor: pointer;
    transition: all 0.2s;
    box-shadow: none;
  }
  .dark .export-btn {
    background: #20c997;
    color: #181c20;
    border: 1px solid #A3D1C6;
  }
  .export-btn:hover {
    background: #A3D1C6;
    color: #23272b;
    border-color: #20c997;
    transform: translateY(-1px);
  }
  .dark .export-btn:hover {
    background: #A3D1C6;
    color: #23272b;
    border-color: #20c997;
  }
  .export-btn svg {
    margin-right: 8px;
    color: #3D8D7A;
  }

/* Stats Grid */
.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
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
  border: 1px solid #20c997;
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

.stat-average { background: #3D8D7A; }
.stat-students { background: #B3D8A8; }
.stat-assessments { background: #A3D1C6; }
.stat-help { background: #f59e0b; }

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

/* Content Grid */
.content-grid {
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: 1.5rem;
  margin-bottom: 1.5rem;
}

.content-card {
  background: white;
  border-radius: 12px;
  padding: 1.5rem;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
  display: flex;
  flex-direction: column;
}
.dark .content-card {
  background: #23272b;
  border: 1px solid #20c997;
  box-shadow: 0 2px 8px rgba(0,0,0,0.25);
}

.card-header {
  margin-bottom: 1.25rem;
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  flex-wrap: wrap;
  gap: 1rem;
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

.table-controls {
  display: flex;
  gap: 1rem;
  align-items: center;
  flex-wrap: wrap;
}

.search-input,
.sort-select {
  padding: 0.5rem 0.75rem;
  border: 1px solid #A3D1C6;
  border-radius: 6px;
  background: white;
  color: #3D8D7A;
  font-size: 0.875rem;
}
.dark .search-input,
.dark .sort-select {
  background: #23272b;
  border-color: #3D8D7A;
  color: #A3D1C6;
}

.chart-controls {
  display: flex;
  gap: 0.5rem;
  margin-bottom: 1rem;
  flex-wrap: wrap;
}

.period-btn {
  padding: 0.5rem 1rem;
  border: 1px solid #A3D1C6;
  background: white;
  color: #3D8D7A;
  border-radius: 6px;
  cursor: pointer;
  font-size: 0.875rem;
  transition: all 0.2s;
}
.dark .period-btn {
  background: #23272b;
  border-color: #3D8D7A;
  color: #A3D1C6;
}

.period-btn.active,
.period-btn:hover {
  background: #3D8D7A;
  color: white;
  border-color: #3D8D7A;
}

.chart-placeholder {
  min-height: 200px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #FBFFE4;
  border-radius: 8px;
  color: #6b7280;
}
.dark .chart-placeholder {
  background: #181c20;
  color: #A3D1C6;
}

/* Table */
.table-wrapper {
  overflow-x: auto;
  margin-bottom: 1rem;
}

.performance-table {
  width: 100%;
  border-collapse: collapse;
}

.performance-table th,
.performance-table td {
  padding: 0.75rem;
  text-align: left;
  border-bottom: 1px solid #e5e7eb;
}
.dark .performance-table th,
.dark .performance-table td {
  border-bottom-color: #374151;
}

.performance-table th {
  background: #FBFFE4;
  font-weight: 600;
  color: #3D8D7A;
  font-size: 0.875rem;
}
.dark .performance-table th {
  background: #181c20;
  color: #A3D1C6;
}

.student-info {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.student-avatar {
  width: 2rem;
  height: 2rem;
  border-radius: 50%;
  overflow: hidden;
}

.student-avatar img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.avatar-placeholder {
  width: 100%;
  height: 100%;
  background: #3D8D7A;
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 600;
  font-size: 0.75rem;
}

.student-name {
  font-weight: 500;
  color: #1f2937;
  font-size: 0.875rem;
}
.dark .student-name {
  color: #A3D1C6;
}

.student-id {
  font-size: 0.75rem;
  color: #6b7280;
}
.dark .student-id {
  color: #9ca3af;
}

.score-badge,
.improvement-badge,
.status-badge {
  padding: 0.25rem 0.5rem;
  border-radius: 4px;
  font-size: 0.75rem;
  font-weight: 500;
}

.score-badge.excellent,
.status-badge.excellent {
  background: #dcfce7;
  color: #166534;
}

.score-badge.good,
.status-badge.good {
  background: #dbeafe;
  color: #1e40af;
}

.score-badge.satisfactory,
.status-badge.satisfactory {
  background: #fef3c7;
  color: #92400e;
}

.score-badge.needs-improvement,
.status-badge.warning {
  background: #fee2e2;
  color: #dc2626;
}

.improvement-badge.positive {
  background: #dcfce7;
  color: #166534;
}

.improvement-badge.negative {
  background: #fee2e2;
  color: #dc2626;
}

.actions-cell {
  width: 120px;
}

.action-btn {
  width: 2rem;
  height: 2rem;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  margin-right: 0.25rem;
  transition: all 0.2s;
}

.view-btn {
  background: #FBFFE4;
  color: #3D8D7A;
}

.view-btn:hover {
  background: #A3D1C6;
}

.edit-btn {
  background: #B3D8A8;
  color: #1f2937;
}

.edit-btn:hover {
  background: #A3D1C6;
}

.warning-btn {
  background: #fef3c7;
  color: #d97706;
}

.warning-btn:hover {
  background: #fde68a;
}

.pagination {
  padding: 1rem 0;
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-top: 1px solid #e5e7eb;
}
.dark .pagination {
  border-top-color: #374151;
}

.page-btn {
  padding: 0.5rem 1rem;
  border: 1px solid #A3D1C6;
  background: white;
  color: #3D8D7A;
  border-radius: 6px;
  cursor: pointer;
  font-weight: 500;
  transition: all 0.2s;
}
.dark .page-btn {
  background: #23272b;
  border-color: #3D8D7A;
  color: #A3D1C6;
}

.page-btn:hover:not(:disabled) {
  background: #A3D1C6;
  color: white;
}

.page-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.page-info {
  color: #6b7280;
  font-size: 0.875rem;
}
.dark .page-info {
  color: #A3D1C6;
}

/* Modals */
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

.modal {
  background: white;
  border-radius: 12px;
  max-width: 500px;
  width: 90%;
  max-height: 90vh;
  overflow-y: auto;
}
.dark .modal {
  background: #23272b;
  border: 1px solid #20c997;
}

.student-detail-modal {
  max-width: 600px;
}

.modal-header {
  padding: 1.5rem;
  border-bottom: 1px solid #e5e7eb;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.dark .modal-header {
  border-bottom-color: #374151;
}

.modal-header h3 {
  margin: 0;
  color: #1f2937;
}
.dark .modal-header h3 {
  color: #A3D1C6;
}

.close-btn {
  background: none;
  border: none;
  font-size: 1.25rem;
  cursor: pointer;
  color: #6b7280;
  width: 2rem;
  height: 2rem;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 6px;
  transition: all 0.2s;
}
.dark .close-btn {
  color: #A3D1C6;
}

.close-btn:hover {
  background: #f3f4f6;
}
.dark .close-btn:hover {
  background: #374151;
}

.modal-content {
  padding: 1.5rem;
}

.student-summary {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1rem;
  margin-bottom: 2rem;
}

.summary-stat {
  text-align: center;
  padding: 1rem;
  background: #FBFFE4;
  border-radius: 8px;
}
.dark .summary-stat {
  background: #181c20;
}

.summary-stat h4 {
  font-size: 1.5rem;
  font-weight: bold;
  color: #3D8D7A;
  margin: 0;
}
.dark .summary-stat h4 {
  color: #A3D1C6;
}

.summary-stat p {
  color: #6b7280;
  font-size: 0.875rem;
  margin: 0.25rem 0 0 0;
}
.dark .summary-stat p {
  color: #A3D1C6;
}

.assessment-history h4 {
  color: #1f2937;
  margin: 0 0 1rem 0;
}
.dark .assessment-history h4 {
  color: #A3D1C6;
}

.history-list {
  max-height: 200px;
  overflow-y: auto;
}

.history-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.75rem;
  border: 1px solid #e5e7eb;
  border-radius: 8px;
  margin-bottom: 0.5rem;
}
.dark .history-item {
  border-color: #374151;
}

.assessment-info h5 {
  font-weight: 500;
  color: #1f2937;
  margin: 0;
}
.dark .assessment-info h5 {
  color: #A3D1C6;
}

.assessment-info p {
  color: #6b7280;
  font-size: 0.75rem;
  margin: 0.25rem 0 0 0;
}
.dark .assessment-info p {
  color: #A3D1C6;
}

.remediation-notes {
  margin-top: 1.5rem;
}

.remediation-notes h4 {
  color: #1f2937;
  margin: 0 0 1rem 0;
}
.dark .remediation-notes h4 {
  color: #A3D1C6;
}

.notes-textarea {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid #A3D1C6;
  border-radius: 8px;
  resize: vertical;
  font-family: inherit;
  background: white;
  color: #1f2937;
}
.dark .notes-textarea {
  background: #23272b;
  border-color: #3D8D7A;
  color: #A3D1C6;
}

.save-notes-btn {
  background: #3D8D7A;
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 6px;
  cursor: pointer;
  font-weight: 500;
  margin-top: 0.5rem;
  transition: all 0.2s;
}

.save-notes-btn:hover {
  background: #2c6b5c;
}

.modal-form {
  padding: 1.5rem;
}

.form-group {
  margin-bottom: 1rem;
}

.form-group label {
  display: block;
  font-weight: 500;
  color: #374151;
  margin-bottom: 0.5rem;
}
.dark .form-group label {
  color: #A3D1C6;
}

.form-group input,
.form-group select,
.form-group textarea {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid #A3D1C6;
  border-radius: 8px;
  font-size: 0.875rem;
  background: white;
  color: #1f2937;
}
.dark .form-group input,
.dark .form-group select,
.dark .form-group textarea {
  background: #23272b;
  border-color: #3D8D7A;
  color: #A3D1C6;
}

.form-group input:focus,
.form-group select:focus,
.form-group textarea:focus {
  outline: none;
  border-color: #3D8D7A;
}

.modal-actions {
  display: flex;
  gap: 0.75rem;
  justify-content: flex-end;
  margin-top: 1.5rem;
}

.cancel-btn {
  padding: 0.75rem 1.5rem;
  border: 1px solid #A3D1C6;
  background: white;
  color: #3D8D7A;
  border-radius: 8px;
  cursor: pointer;
  font-weight: 500;
  transition: all 0.2s;
}
.dark .cancel-btn {
  background: #23272b;
  border-color: #3D8D7A;
  color: #A3D1C6;
}

.cancel-btn:hover {
  background: #FBFFE4;
}
.dark .cancel-btn:hover {
  background: #181c20;
}

.submit-btn {
  padding: 0.75rem 1.5rem;
  background: #3D8D7A;
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  font-weight: 500;
  transition: all 0.2s;
}

.submit-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.submit-btn:hover:not(:disabled) {
  background: #2c6b5c;
  transform: translateY(-1px);
}

@media (max-width: 1024px) {
  .content-grid {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 768px) {
  .analytics-container {
    padding: 1rem;
  }
  
  .header-content {
    flex-direction: column;
    align-items: stretch;
  }
  
  .header-actions {
    flex-direction: column;
    gap: 0.5rem;
  }
  
  .stats-grid {
    grid-template-columns: 1fr;
  }
  
  .card-header {
    flex-direction: column;
    align-items: stretch;
  }
  
  .table-controls {
    flex-direction: column;
    gap: 0.5rem;
  }
  
  .search-input {
    width: 100%;
  }
  
  .table-wrapper {
    font-size: 0.875rem;
  }
  
  .performance-table th,
  .performance-table td {
    padding: 0.5rem;
  }
  
  .student-summary {
    grid-template-columns: 1fr;
  }
}

/* New styles for quiz performance list */
.performance-list {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.performance-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
  background: #FBFFE4;
  border-radius: 8px;
  border-left: 4px solid #3D8D7A;
}

.dark .performance-item {
  background: #181c20;
  border-left-color: #20c997;
}

.quiz-info {
  flex: 1;
}

.quiz-title {
  font-weight: 600;
  color: #1f2937;
  margin-bottom: 0.25rem;
}

.dark .quiz-title {
  color: #A3D1C6;
}

.quiz-meta {
  font-size: 0.813rem;
  color: #6b7280;
}

.dark .quiz-meta {
  color: #9ca3af;
}

.quiz-score {
  margin-left: 1rem;
}

/* Distribution list styles */
.distribution-list {
  display: grid;
  gap: 1rem;
}

.dist-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
  background: #FBFFE4;
  border-radius: 8px;
}

.dark .dist-item {
  background: #181c20;
}

.dist-label {
  padding: 0.25rem 0.75rem;
  border-radius: 4px;
  font-size: 0.875rem;
  font-weight: 500;
}

.dist-label.excellent {
  background: #dcfce7;
  color: #166534;
}

.dist-label.good {
  background: #dbeafe;
  color: #1e40af;
}

.dist-label.satisfactory {
  background: #fef3c7;
  color: #92400e;
}

.dist-label.warning {
  background: #fee2e2;
  color: #dc2626;
}

.dist-count {
  font-size: 1.5rem;
  font-weight: 700;
  color: #3D8D7A;
  margin-left: 1rem;
}

.dark .dist-count {
  color: #A3D1C6;
}

.empty-state {
  padding: 2rem;
  text-align: center;
  color: #6b7280;
}

.dark .empty-state {
  color: #9ca3af;
}

.history-list {
  max-height: 300px;
  overflow-y: auto;
}

.history-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
  border: 1px solid #e5e7eb;
  border-radius: 8px;
  margin-bottom: 0.5rem;
}

.dark .history-item {
  border-color: #374151;
}

.quiz-info h5 {
  font-weight: 600;
  color: #1f2937;
  margin: 0;
  margin-bottom: 0.25rem;
}

.dark .quiz-info h5 {
  color: #A3D1C6;
}

.quiz-info p {
  font-size: 0.75rem;
  color: #6b7280;
  margin: 0;
}

.dark .quiz-info p {
  color: #9ca3af;
}

/* Enhanced Loading Overlay - Matches MessagesPage */
.loading-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(251, 255, 228, 0.95);
  backdrop-filter: blur(8px);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 9999;
  animation: fadeIn 0.3s ease;
}

@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

.dark .loading-overlay {
  background: rgba(24, 28, 32, 0.95);
}

.loading-content {
  background: white;
  padding: 3rem 4rem;
  border-radius: 20px;
  text-align: center;
  box-shadow: 0 20px 60px rgba(61, 141, 122, 0.15);
  border: 2px solid #a3d1c6;
  animation: slideUp 0.4s ease;
}

@keyframes slideUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.dark .loading-content {
  background: #23272b;
  border-color: #374151;
}

.loading-spinner-container {
  position: relative;
  width: 80px;
  height: 80px;
  margin: 0 auto 1.5rem;
}

.loading-spinner {
  width: 80px;
  height: 80px;
  border: 5px solid rgba(61, 141, 122, 0.1);
  border-left: 5px solid #3d8d7a;
  border-top: 5px solid #20c997;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin: 0 auto;
  box-shadow: 0 0 20px rgba(61, 141, 122, 0.1);
}

@keyframes spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

.dark .loading-spinner {
  border: 5px solid rgba(32, 201, 151, 0.1);
  border-left: 5px solid #20c997;
  border-top: 5px solid #18a577;
  box-shadow: 0 0 20px rgba(32, 201, 151, 0.1);
}

.loading-text {
  font-size: 1.125rem;
  font-weight: 600;
  color: #1f2937;
  margin: 0;
  letter-spacing: 0.025em;
}

.dark .loading-text {
  color: #A3D1C6;
}
</style>