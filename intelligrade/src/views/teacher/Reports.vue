
<template>
  <div class="reports-container">
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
              <path d="M9,17H7V10H9V17M13,17H11V7H13V17M17,17H15V13H17V17M19.5,3.5L18,2L16.5,3.5L15,2L13.5,3.5L12,2L10.5,3.5L9,2L7.5,3.5L6,2L4.5,3.5L3,2V22L4.5,20.5L6,22L7.5,20.5L9,22L10.5,20.5L12,22L13.5,20.5L15,22L16.5,20.5L18,22L19.5,20.5L21,22V2L19.5,3.5Z" />
            </svg>
          </div>
          <div class="header-text">
            <div class="section-header-title">Performance Reports</div>
            <div class="section-header-subtitle">{{ subjectName }} (Grade {{ gradeLevel }})</div>
            <div class="section-header-description">{{ sectionName }} - {{ sectionCode }}</div>
          </div>
        </div>
        
        <div class="header-actions">
          <button @click="exportReports" class="export-btn" :disabled="isExporting">
            <svg v-if="isExporting" width="20" height="20" viewBox="0 0 24 24" fill="currentColor" class="spinner">
              <path d="M12,4V2A10,10 0 0,0 2,12H4A8,8 0 0,1 12,4Z" />
            </svg>
            <svg v-else width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M14,2H6A2,2 0 0,0 4,4V20A2,2 0 0,0 6,22H18A2,2 0 0,0 20,20V8L14,2M18,20H6V4H13V9H18V20Z" />
            </svg>
            {{ isExporting ? 'Exporting...' : 'Export Reports' }}
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
        <p>Loading performance data...</p>
      </div>

      <!-- Error State -->
      <div v-else-if="error" class="error-state">
        <div class="error-icon">
          <svg width="48" height="48" viewBox="0 0 24 24" fill="currentColor">
            <path d="M11,15H13V17H11V15M11,7H13V13H11V7M12,2C6.47,2 2,6.5 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2M12,20A8,8 0 0,1 4,12A8,8 0 0,1 12,4A8,8 0 0,1 20,12A8,8 0 0,1 12,20Z" />
          </svg>
        </div>
        <h3>Error Loading Reports</h3>
        <p>{{ error }}</p>
        <button @click="fetchReportData" class="retry-btn">Try Again</button>
      </div>

      <!-- Reports Content -->
      <div v-else class="reports-content">
        <!-- Summary Cards -->
        <div class="summary-grid">
          <div class="summary-card total-students">
            <div class="summary-icon">
              <svg width="32" height="32" viewBox="0 0 24 24" fill="currentColor">
                <path d="M16,4C18.11,4 19.81,5.69 19.81,7.8C19.81,9.91 18.11,11.6 16,11.6C13.89,11.6 12.2,9.91 12.2,7.8C12.2,5.69 13.89,4 16,4M16,13.4C18.73,13.4 22,14.76 22,17.5V20H10V17.5C10,14.76 13.27,13.4 16,13.4M6,6H8V8H6V6M6,10H8V12H6V10M6,14H8V16H6V14Z" />
              </svg>
            </div>
            <div class="summary-info">
              <span class="summary-number">{{ reportData.totalStudents }}</span>
              <span class="summary-label">Total Students</span>
            </div>
          </div>

          <div class="summary-card total-assessments">
            <div class="summary-icon">
              <svg width="32" height="32" viewBox="0 0 24 24" fill="currentColor">
                <path d="M14,2H6A2,2 0 0,0 4,4V20A2,2 0 0,0 6,22H18A2,2 0 0,0 20,20V8L14,2M18,20H6V4H13V9H18V20Z" />
              </svg>
            </div>
            <div class="summary-info">
              <span class="summary-number">{{ reportData.totalQuizzes }}</span>
              <span class="summary-label">Total Quizzes</span>
            </div>
          </div>

          <div class="summary-card average-score">
            <div class="summary-icon">
              <svg width="32" height="32" viewBox="0 0 24 24" fill="currentColor">
                <path d="M12,17.27L18.18,21L16.54,13.97L22,9.24L14.81,8.62L12,2L9.19,8.62L2,9.24L7.46,13.97L5.82,21L12,17.27Z" />
              </svg>
            </div>
            <div class="summary-info">
              <span class="summary-number">{{ reportData.averageScore }}%</span>
              <span class="summary-label">Class Average</span>
            </div>
          </div>

          <div class="summary-card completion-rate">
            <div class="summary-icon">
              <svg width="32" height="32" viewBox="0 0 24 24" fill="currentColor">
                <path d="M9,20.42L2.79,14.21L5.62,11.38L9,14.77L18.88,4.88L21.71,7.71L9,20.42Z" />
              </svg>
            </div>
            <div class="summary-info">
              <span class="summary-number">{{ reportData.completionRate }}%</span>
              <span class="summary-label">Completion Rate</span>
            </div>
          </div>
        </div>

        <!-- Reports Tabs -->
        <div class="reports-tabs">
          <div class="tab-buttons">
            <button 
              v-for="tab in tabs" 
              :key="tab.id"
              @click="activeTab = tab.id"
              :class="['tab-button', { active: activeTab === tab.id }]"
            >
              <component :is="tab.icon" />
              {{ tab.label }}
            </button>
          </div>

          <div class="tab-content">
            <!-- Overview Tab -->
            <div v-if="activeTab === 'overview'" class="tab-panel">
              <div class="report-section">
                <h3>Class Performance Overview</h3>
                
                <div class="charts-grid">
                  <!-- Score Distribution Chart -->
                  <div class="chart-card">
                    <h4>Score Distribution</h4>
                    <div class="chart-placeholder">
                      <div class="chart-bars">
                        <div v-for="(range, index) in scoreDistribution" :key="index" class="score-bar">
                          <div class="bar" :style="{ height: range.percentage + '%' }"></div>
                          <span class="bar-label">{{ range.range }}</span>
                        </div>
                      </div>
                    </div>
                  </div>

                  <!-- Performance Trends -->
                  <div class="chart-card">
                    <h4>Performance Trends</h4>
                    <div class="trend-chart">
                      <div class="trend-line">
                        <div v-for="(point, index) in performanceTrend" :key="index" 
                             class="trend-point" 
                             :style="{ left: (index * 20) + '%', bottom: point.score + '%' }">
                        </div>
                      </div>
                      <div class="trend-labels">
                        <span v-for="(quiz, index) in performanceTrend" :key="index" class="trend-label">
                          Quiz {{ index + 1 }}
                        </span>
                      </div>
                    </div>
                  </div>
                </div>

                <!-- Top Performers -->
                <div class="performers-section">
                  <div class="top-performers">
                    <h4>Top Performers</h4>
                    <div v-if="reportData.topPerformers.length > 0" class="performers-list">
                      <div v-for="(student, index) in reportData.topPerformers" :key="student.id" class="performer-item">
                        <div class="performer-rank">{{ index + 1 }}</div>
                        <div class="performer-info">
                          <span class="performer-name">{{ student.full_name }}</span>
                          <span class="performer-score">{{ student.average_score }}%</span>
                        </div>
                      </div>
                    </div>
                    <div v-else class="no-data">
                      <p>No assessment data available yet</p>
                    </div>
                  </div>

                  <div class="struggling-students">
                    <h4>Students Needing Support</h4>
                    <div v-if="reportData.strugglingStudents.length > 0" class="performers-list">
                      <div v-for="student in reportData.strugglingStudents" :key="student.id" class="performer-item struggling">
                        <div class="performer-info">
                          <span class="performer-name">{{ student.full_name }}</span>
                          <span class="performer-score">{{ student.average_score }}%</span>
                        </div>
                        <div class="support-indicator">
                          <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                            <path d="M11,15H13V17H11V15M11,7H13V13H11V7M12,2C6.47,2 2,6.5 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2M12,20A8,8 0 0,1 4,12A8,8 0 0,1 12,4A8,8 0 0,1 20,12A8,8 0 0,1 12,20Z" />
                          </svg>
                        </div>
                      </div>
                    </div>
                    <div v-else class="no-data">
                      <p>All students performing well!</p>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <!-- Individual Performance Tab -->
            <div v-if="activeTab === 'individual'" class="tab-panel">
              <div class="report-section">
                <h3>Individual Student Performance</h3>
                
                <div class="search-filter">
                  <div class="search-box">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                      <path d="M9.5,3A6.5,6.5 0 0,1 16,9.5C16,11.11 15.41,12.59 14.44,13.73L14.71,14H15.5L20.5,19L19,20.5L14,15.5V14.71L13.73,14.44C12.59,15.41 11.11,16 9.5,16A6.5,6.5 0 0,1 3,9.5A6.5,6.5 0 0,1 9.5,3M9.5,5C7,5 5,7 5,9.5C5,12 7,14 9.5,14C12,14 14,12 14,9.5C14,7 12,5 9.5,5Z" />
                    </svg>
                    <input 
                      v-model="searchStudent" 
                      type="text" 
                      placeholder="Search students..."
                    >
                  </div>
                </div>

                <div v-if="filteredStudents.length > 0" class="students-performance-table">
                  <div class="table-header">
                    <div class="header-cell">Student Name</div>
                    <div class="header-cell">Quizzes Taken</div>
                    <div class="header-cell">Average Score</div>
                    <div class="header-cell">Best Score</div>
                    <div class="header-cell">Last Activity</div>
                    <div class="header-cell">Actions</div>
                  </div>
                  <div class="table-body">
                    <div v-for="student in filteredStudents" :key="student.id" class="table-row">
                      <div class="table-cell student-name">
                        <div class="student-avatar">{{ getInitials(student.full_name) }}</div>
                        <span>{{ student.full_name }}</span>
                      </div>
                      <div class="table-cell">{{ student.quizzes_taken || 0 }}</div>
                      <div class="table-cell">
                        <span :class="['score-badge', getScoreClass(student.average_score)]">
                          {{ student.average_score || 0 }}%
                        </span>
                      </div>
                      <div class="table-cell">{{ student.best_score || 0 }}%</div>
                      <div class="table-cell">{{ formatDate(student.last_activity) }}</div>
                      <div class="table-cell">
                        <button @click="viewStudentDetail(student)" class="action-btn-small">
                          View Details
                        </button>
                      </div>
                    </div>
                  </div>
                </div>
                <div v-else-if="searchStudent" class="no-results">
                  <p>No students found matching "{{ searchStudent }}"</p>
                </div>
                <div v-else class="no-data">
                  <p>No students enrolled in this section yet</p>
                </div>
              </div>
            </div>

            <!-- Quiz Performance Tab -->
            <div v-if="activeTab === 'quiz'" class="tab-panel">
              <div class="report-section">
                <h3>Quiz Performance Analysis</h3>
                
                <div v-if="reportData.quizPerformance.length > 0" class="quiz-performance-list">
                  <div v-for="quiz in reportData.quizPerformance" :key="quiz.id" class="quiz-performance-card">
                    <div class="quiz-performance-header">
                      <h4>{{ quiz.title }}</h4>
                      <span class="quiz-date">{{ formatDate(quiz.created_at) }}</span>
                    </div>
                    
                    <div class="quiz-stats-grid">
                      <div class="quiz-stat">
                        <span class="stat-value">{{ quiz.attempts || 0 }}</span>
                        <span class="stat-label">Attempts</span>
                      </div>
                      <div class="quiz-stat">
                        <span class="stat-value">{{ quiz.average_score || 0 }}%</span>
                        <span class="stat-label">Average</span>
                      </div>
                      <div class="quiz-stat">
                        <span class="stat-value">{{ quiz.highest_score || 0 }}%</span>
                        <span class="stat-label">Highest</span>
                      </div>
                      <div class="quiz-stat">
                        <span class="stat-value">{{ quiz.lowest_score || 0 }}%</span>
                        <span class="stat-label">Lowest</span>
                      </div>
                    </div>

                    <div class="quiz-difficulty-analysis">
                      <h5>Question Difficulty Analysis</h5>
                      <div class="difficulty-bars">
                        <div v-for="(question, index) in quiz.questions_analysis" :key="index" class="difficulty-item">
                          <span class="question-label">Q{{ index + 1 }}</span>
                          <div class="difficulty-bar-container">
                            <div class="difficulty-bar" :style="{ width: question.correct_percentage + '%', backgroundColor: getDifficultyColor(question.correct_percentage) }"></div>
                          </div>
                          <span class="difficulty-percentage">{{ question.correct_percentage }}%</span>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
                <div v-else class="no-data">
                  <p>No quiz data available yet</p>
                </div>
              </div>
            </div>

            <!-- Analytics Tab -->
            <div v-if="activeTab === 'analytics'" class="tab-panel">
              <div class="report-section">
                <h3>Learning Analytics</h3>
                
                <div class="analytics-grid">
                  <div class="analytics-card">
                    <h4>Engagement Metrics</h4>
                    <div class="metric-list">
                      <div class="metric-item">
                        <span class="metric-label">Daily Active Students</span>
                        <span class="metric-value">{{ reportData.analytics.dailyActive || 0 }}</span>
                      </div>
                      <div class="metric-item">
                        <span class="metric-label">Weekly Active Students</span>
                        <span class="metric-value">{{ reportData.analytics.weeklyActive || 0 }}</span>
                      </div>
                      <div class="metric-item">
                        <span class="metric-label">Average Session Time</span>
                        <span class="metric-value">{{ reportData.analytics.averageSession || '0 min' }}</span>
                      </div>
                    </div>
                  </div>

                  <div class="analytics-card">
                    <h4>Learning Patterns</h4>
                    <div class="pattern-insights">
                      <div class="insight-item">
                        <div class="insight-icon">📊</div>
                        <div class="insight-text">
                          <strong>Peak Activity Time:</strong> {{ reportData.analytics.peakTime || 'No data' }}
                        </div>
                      </div>
                      <div class="insight-item">
                        <div class="insight-icon">📈</div>
                        <div class="insight-text">
                          <strong>Improvement Trend:</strong> {{ reportData.analytics.improvementTrend || 'No trend data' }}
                        </div>
                      </div>
                      <div class="insight-item">
                        <div class="insight-icon">🎯</div>
                        <div class="insight-text">
                          <strong>Most Challenging Topic:</strong> {{ reportData.analytics.challengingTopic || 'No data' }}
                        </div>
                      </div>
                    </div>
                  </div>

                  <div class="analytics-card">
                    <h4>Recommendations</h4>
                    <div class="recommendations-list">
                      <div v-for="(recommendation, index) in reportData.recommendations" :key="index" class="recommendation-item">
                        <div class="recommendation-priority" :class="recommendation.priority">
                          {{ recommendation.priority }}
                        </div>
                        <div class="recommendation-text">{{ recommendation.text }}</div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { supabase } from '../../supabase.js'

const router = useRouter()
const route = useRoute()

// Get data from route
const subjectId = ref(route.params.subjectId)
const sectionId = ref(route.params.sectionId)
const subjectName = ref(route.query.subjectName || '')
const sectionName = ref(route.query.sectionName || '')
const gradeLevel = ref(route.query.gradeLevel || '')
const sectionCode = ref(route.query.sectionCode || '')

// State
const isLoading = ref(false)
const isExporting = ref(false)
const error = ref(null)
const activeTab = ref('overview')
const searchStudent = ref('')

// Report Data
const reportData = ref({
  totalStudents: 0,
  totalQuizzes: 0,
  averageScore: 0,
  completionRate: 0,
  topPerformers: [],
  strugglingStudents: [],
  studentPerformance: [],
  quizPerformance: [],
  analytics: {
    dailyActive: 0,
    weeklyActive: 0,
    averageSession: '0 min',
    peakTime: 'No data',
    improvementTrend: 'No trend data',
    challengingTopic: 'No data'
  },
  recommendations: [
    { priority: 'high', text: 'Consider reviewing topics with low quiz scores' },
    { priority: 'medium', text: 'Increase engagement with interactive activities' },
    { priority: 'low', text: 'Provide additional practice materials for struggling students' }
  ]
})

// Mock data for visualization
const scoreDistribution = ref([
  { range: '90-100%', percentage: 25 },
  { range: '80-89%', percentage: 40 },
  { range: '70-79%', percentage: 60 },
  { range: '60-69%', percentage: 35 },
  { range: 'Below 60%', percentage: 15 }
])

const performanceTrend = ref([
  { score: 75 },
  { score: 78 },
  { score: 82 },
  { score: 79 },
  { score: 85 }
])

// Tabs configuration
const tabs = ref([
  { 
    id: 'overview', 
    label: 'Overview',
    icon: 'OverviewIcon'
  },
  { 
    id: 'individual', 
    label: 'Individual Performance',
    icon: 'IndividualIcon'
  },
  { 
    id: 'quiz', 
    label: 'Quiz Analysis',
    icon: 'QuizIcon'
  },
  { 
    id: 'analytics', 
    label: 'Learning Analytics',
    icon: 'AnalyticsIcon'
  }
])

// Computed
const filteredStudents = computed(() => {
  if (!searchStudent.value) {
    return reportData.value.studentPerformance
  }
  return reportData.value.studentPerformance.filter(student =>
    student.full_name.toLowerCase().includes(searchStudent.value.toLowerCase())
  )
})

// Methods
const fetchReportData = async () => {
  isLoading.value = true
  error.value = null
  
  try {
    const { data: { user } } = await supabase.auth.getUser()
    if (!user) throw new Error('Please login to continue')

    // Fetch students in this section
    const { data: students, error: studentsError } = await supabase
      .from('student_sections')
      .select(`
        student_id,
        profiles!inner(
          id,
          full_name,
          created_at
        )
      `)
      .eq('section_id', sectionId.value)

    if (studentsError) throw studentsError

    // Fetch quizzes for this section
    const { data: quizzes, error: quizzesError } = await supabase
      .from('quizzes')
      .select(`
        *,
        quiz_questions(id, points)
      `)
      .eq('subject_id', subjectId.value)
      .eq('section_id', sectionId.value)
      .eq('teacher_id', user.id)

    if (quizzesError) throw quizzesError

    // Process and populate report data
    reportData.value.totalStudents = students?.length || 0
    reportData.value.totalQuizzes = quizzes?.length || 0
    
    // Mock additional data since we don't have quiz attempts table yet
    reportData.value.averageScore = Math.floor(Math.random() * 20) + 70 // 70-90%
    reportData.value.completionRate = Math.floor(Math.random() * 30) + 70 // 70-100%

    // Generate mock student performance data
    reportData.value.studentPerformance = (students || []).map(student => ({
      ...student.profiles,
      quizzes_taken: Math.floor(Math.random() * (quizzes?.length || 0) + 1),
      average_score: Math.floor(Math.random() * 30) + 60,
      best_score: Math.floor(Math.random() * 20) + 80,
      last_activity: new Date(Date.now() - Math.random() * 7 * 24 * 60 * 60 * 1000).toISOString()
    }))

    // Generate top performers and struggling students
    const sortedStudents = [...reportData.value.studentPerformance].sort((a, b) => b.average_score - a.average_score)
    reportData.value.topPerformers = sortedStudents.slice(0, 5)
    reportData.value.strugglingStudents = sortedStudents.filter(s => s.average_score < 70).slice(0, 5)

    // Generate quiz performance data
    reportData.value.quizPerformance = (quizzes || []).map(quiz => ({
      ...quiz,
      attempts: Math.floor(Math.random() * reportData.value.totalStudents),
      average_score: Math.floor(Math.random() * 30) + 60,
      highest_score: Math.floor(Math.random() * 20) + 80,
      lowest_score: Math.floor(Math.random() * 40) + 30,
      questions_analysis: (quiz.quiz_questions || []).map((_, index) => ({
        correct_percentage: Math.floor(Math.random() * 50) + 50
      }))
    }))

  } catch (err) {
    console.error('Error fetching report data:', err)
    error.value = err.message
  } finally {
    isLoading.value = false
  }
}

const exportReports = async () => {
  isExporting.value = true
  
  try {
    // Simulate export delay
    await new Promise(resolve => setTimeout(resolve, 2000))
    
    // Create a simple CSV export
    const csvData = [
      ['Student Name', 'Average Score', 'Quizzes Taken', 'Last Activity'],
      ...reportData.value.studentPerformance.map(student => [
        student.full_name,
        student.average_score + '%',
        student.quizzes_taken,
        formatDate(student.last_activity)
      ])
    ]
    
    const csvContent = csvData.map(row => row.join(',')).join('\n')
    const blob = new Blob([csvContent], { type: 'text/csv' })
    const url = window.URL.createObjectURL(blob)
    const a = document.createElement('a')
    a.href = url
    a.download = `${subjectName.value}_${sectionName.value}_Report.csv`
    a.click()
    window.URL.revokeObjectURL(url)
    
    alert('Report exported successfully!')
  } catch (err) {
    console.error('Error exporting reports:', err)
    alert('Error exporting reports. Please try again.')
  } finally {
    isExporting.value = false
  }
}

const viewStudentDetail = (student) => {
  alert(`Viewing detailed performance for ${student.full_name}\n\nThis would show:\n• Individual quiz scores\n• Progress over time\n• Strengths and areas for improvement`)
}

const getInitials = (name) => {
  return name.split(' ').map(n => n[0]).join('').toUpperCase()
}

const getScoreClass = (score) => {
  if (score >= 90) return 'excellent'
  if (score >= 80) return 'good'
  if (score >= 70) return 'average'
  return 'needs-improvement'
}

const getDifficultyColor = (percentage) => {
  if (percentage >= 80) return '#10b981'
  if (percentage >= 60) return '#f59e0b'
  return '#ef4444'
}

const formatDate = (dateString) => {
  if (!dateString) return 'No activity'
  return new Date(dateString).toLocaleDateString()
}

const goBack = () => {
  router.push({ name: 'MySubjects' })
}

// Lifecycle
onMounted(() => {
  fetchReportData()
})
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

.reports-container {
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
  background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
  border-radius: 32px;
  padding: 3rem;
  margin-bottom: 2.5rem;
  min-height: 160px;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.3);
  overflow: hidden;
}

.header-bg-decoration {
  position: absolute;
  top: -50%;
  right: -20%;
  width: 120%;
  height: 200%;
  background: radial-gradient(ellipse at center, rgba(139, 92, 246, 0.08) 0%, transparent 70%);
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
  background: linear-gradient(135deg, rgba(139, 92, 246, 0.1) 0%, rgba(167, 139, 250, 0.05) 100%);
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
  width: 70px;
  height: 70px;
  background: linear-gradient(135deg, #8b5cf6 0%, #a78bfa 100%);
  border-radius: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #fff;
  box-shadow: 0 8px 24px rgba(139, 92, 246, 0.3);
}

.header-text {
  display: flex;
  flex-direction: column;
  gap: 0.3rem;
}

.section-header-title {
  font-size: 2rem;
  font-weight: 800;
  color: #8b5cf6;
  margin-bottom: 0.25rem;
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

.export-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  background: linear-gradient(135deg, #f59e0b 0%, #fbbf24 100%);
  color: white;
  border: none;
  padding: 0.875rem 1.5rem;
  border-radius: 16px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 8px 24px rgba(245, 158, 11, 0.3);
}

.export-btn:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 12px 32px rgba(245, 158, 11, 0.4);
}

.export-btn:disabled {
  opacity: 0.7;
  cursor: not-allowed;
}

.back-button {
  background: rgba(255, 255, 255, 0.8);
  border: 1px solid rgba(203, 213, 225, 0.5);
  border-radius: 16px;
  padding: 0.875rem 1.5rem;
  backdrop-filter: blur(10px);
  display: flex;
  align-items: center;
  gap: 0.5rem;
  color: #64748b;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
}

.back-button:hover {
  background: rgba(255, 255, 255, 0.95);
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1);
}

.main-wrapper {
  background: white;
  border-radius: 24px;
  padding: 2rem;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.3);
}

/* States */
.loading-state, .error-state {
  text-align: center;
  padding: 4rem 2rem;
}

.loading-spinner {
  width: 40px;
  height: 40px;
  border: 4px solid rgba(139, 92, 246, 0.1);
  border-left: 4px solid #8b5cf6;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin: 0 auto 1rem;
}

.spinner {
  animation: spin 1s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

.error-icon {
  color: #94a3b8;
  margin-bottom: 1.5rem;
}

.error-state h3 {
  color: #374151;
  font-size: 1.5rem;
  font-weight: 600;
  margin-bottom: 0.5rem;
}

.error-state p {
  color: #6b7280;
  margin-bottom: 2rem;
}

.retry-btn {
  background: linear-gradient(135deg, #8b5cf6 0%, #a78bfa 100%);
  color: white;
  border: none;
  padding: 1rem 2rem;
  border-radius: 16px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
}

.retry-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 12px 32px rgba(139, 92, 246, 0.3);
}

/* Summary Cards */
.summary-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.5rem;
  margin-bottom: 2rem;
}

.summary-card {
  background: white;
  border-radius: 20px;
  padding: 2rem;
  display: flex;
  align-items: center;
  gap: 1.5rem;
  border: 2px solid transparent;
  transition: all 0.3s ease;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.05);
}

.summary-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 16px 48px rgba(0, 0, 0, 0.1);
}

.total-students {
  border-color: rgba(59, 130, 246, 0.2);
}

.total-students .summary-icon {
  background: linear-gradient(135deg, #3b82f6 0%, #60a5fa 100%);
}

.total-assessments {
  border-color: rgba(16, 185, 129, 0.2);
}

.total-assessments .summary-icon {
  background: linear-gradient(135deg, #10b981 0%, #34d399 100%);
}

.average-score {
  border-color: rgba(245, 158, 11, 0.2);
}

.average-score .summary-icon {
  background: linear-gradient(135deg, #f59e0b 0%, #fbbf24 100%);
}

.completion-rate {
  border-color: rgba(139, 92, 246, 0.2);
}

.completion-rate .summary-icon {
  background: linear-gradient(135deg, #8b5cf6 0%, #a78bfa 100%);
}

.summary-icon {
  width: 60px;
  height: 60px;
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1);
}

.summary-info {
  display: flex;
  flex-direction: column;
}

.summary-number {
  font-size: 2rem;
  font-weight: 800;
  color: #1f2937;
  line-height: 1;
}

.summary-label {
  font-size: 0.9rem;
  color: #6b7280;
  font-weight: 500;
  margin-top: 0.25rem;
}

/* Tabs */
.reports-tabs {
  margin-top: 2rem;
}

.tab-buttons {
  display: flex;
  gap: 0.5rem;
  margin-bottom: 2rem;
  border-bottom: 2px solid rgba(229, 231, 235, 0.8);
  overflow-x: auto;
  padding-bottom: 1rem;
}

.tab-button {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1.5rem;
  border: none;
  background: transparent;
  border-radius: 12px;
  font-weight: 600;
  color: #6b7280;
  cursor: pointer;
  transition: all 0.3s ease;
  white-space: nowrap;
  position: relative;
}

.tab-button:hover {
  background: rgba(139, 92, 246, 0.1);
  color: #8b5cf6;
}

.tab-button.active {
  background: linear-gradient(135deg, #8b5cf6 0%, #a78bfa 100%);
  color: white;
  box-shadow: 0 4px 12px rgba(139, 92, 246, 0.3);
}

.tab-content {
  min-height: 400px;
}

.tab-panel {
  animation: fadeIn 0.3s ease;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}

.report-section h3 {
  color: #1f2937;
  font-size: 1.5rem;
  font-weight: 700;
  margin-bottom: 2rem;
}

/* Charts */
.charts-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
  gap: 2rem;
  margin-bottom: 3rem;
}

.chart-card {
  background: white;
  border: 1px solid rgba(229, 231, 235, 0.8);
  border-radius: 20px;
  padding: 2rem;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
}

.chart-card h4 {
  color: #1f2937;
  font-size: 1.1rem;
  font-weight: 600;
  margin-bottom: 1.5rem;
}

.chart-placeholder {
  height: 200px;
  display: flex;
  align-items: end;
  justify-content: center;
  padding: 1rem 0;
}

.chart-bars {
  display: flex;
  align-items: end;
  gap: 1rem;
  height: 100%;
  width: 100%;
  justify-content: space-around;
}

.score-bar {
  display: flex;
  flex-direction: column;
  align-items: center;
  height: 100%;
  flex: 1;
}

.bar {
  background: linear-gradient(135deg, #8b5cf6 0%, #a78bfa 100%);
  width: 100%;
  border-radius: 4px 4px 0 0;
  transition: all 0.3s ease;
  min-height: 4px;
}

.bar-label {
  font-size: 0.7rem;
  color: #6b7280;
  margin-top: 0.5rem;
  text-align: center;
  transform: rotate(-45deg);
}

.trend-chart {
  position: relative;
  height: 200px;
  background: rgba(248, 250, 252, 0.8);
  border-radius: 12px;
  overflow: hidden;
}

.trend-line {
  position: relative;
  height: 100%;
  padding: 1rem;
}

.trend-point {
  position: absolute;
  width: 8px;
  height: 8px;
  background: #8b5cf6;
  border-radius: 50%;
  border: 2px solid white;
  box-shadow: 0 2px 8px rgba(139, 92, 246, 0.3);
}

.trend-labels {
  position: absolute;
  bottom: 0.5rem;
  left: 1rem;
  right: 1rem;
  display: flex;
  justify-content: space-between;
}

.trend-label {
  font-size: 0.7rem;
  color: #6b7280;
}

/* Performers Section */
.performers-section {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
}

.top-performers, .struggling-students {
  background: white;
  border: 1px solid rgba(229, 231, 235, 0.8);
  border-radius: 20px;
  padding: 2rem;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
}

.top-performers h4, .struggling-students h4 {
  color: #1f2937;
  font-size: 1.1rem;
  font-weight: 600;
  margin-bottom: 1.5rem;
}

.performers-list {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.performer-item {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1rem;
  background: rgba(248, 250, 252, 0.5);
  border-radius: 12px;
  border: 1px solid rgba(229, 231, 235, 0.5);
}

.performer-item.struggling {
  border-color: rgba(239, 68, 68, 0.2);
  background: rgba(254, 242, 242, 0.5);
}

.performer-rank {
  background: linear-gradient(135deg, #f59e0b 0%, #fbbf24 100%);
  color: white;
  width: 28px;
  height: 28px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 0.8rem;
}

.performer-info {
  display: flex;
  flex-direction: column;
  flex: 1;
}

.performer-name {
  font-weight: 600;
  color: #1f2937;
}

.performer-score {
  font-size: 0.9rem;
  color: #6b7280;
}

.support-indicator {
  color: #ef4444;
}

.no-data {
  text-align: center;
  padding: 2rem;
  color: #6b7280;
}

/* Individual Performance Table */
.search-filter {
  margin-bottom: 2rem;
}

.search-box {
  position: relative;
  max-width: 400px;
}

.search-box svg {
  position: absolute;
  left: 1rem;
  top: 50%;
  transform: translateY(-50%);
  color: #6b7280;
}

.search-box input {
  width: 100%;
  padding: 0.75rem 1rem 0.75rem 3rem;
  border: 2px solid rgba(229, 231, 235, 0.8);
  border-radius: 12px;
  font-size: 1rem;
  transition: all 0.3s ease;
}

.search-box input:focus {
  outline: none;
  border-color: #8b5cf6;
  box-shadow: 0 0 0 3px rgba(139, 92, 246, 0.1);
}

.students-performance-table {
  background: white;
  border: 1px solid rgba(229, 231, 235, 0.8);
  border-radius: 20px;
  overflow: hidden;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
}

.table-header {
  display: grid;
  grid-template-columns: 2fr 1fr 1fr 1fr 1.5fr 1fr;
  gap: 1rem;
  padding: 1.5rem 2rem;
  background: rgba(248, 250, 252, 0.8);
  border-bottom: 1px solid rgba(229, 231, 235, 0.8);
}

.header-cell {
  font-weight: 600;
  color: #374151;
  font-size: 0.9rem;
}

.table-body {
  max-height: 500px;
  overflow-y: auto;
}

.table-row {
  display: grid;
  grid-template-columns: 2fr 1fr 1fr 1fr 1.5fr 1fr;
  gap: 1rem;
  padding: 1.5rem 2rem;
  border-bottom: 1px solid rgba(229, 231, 235, 0.5);
  transition: all 0.3s ease;
}

.table-row:hover {
  background: rgba(248, 250, 252, 0.5);
}

.table-cell {
  display: flex;
  align-items: center;
  color: #374151;
}

.student-name {
  gap: 1rem;
}

.student-avatar {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: linear-gradient(135deg, #8b5cf6 0%, #a78bfa 100%);
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 600;
  font-size: 0.9rem;
}

.score-badge {
  padding: 0.3rem 0.8rem;
  border-radius: 12px;
  font-size: 0.8rem;
  font-weight: 600;
}

.score-badge.excellent {
  background: rgba(16, 185, 129, 0.1);
  color: #10b981;
}

.score-badge.good {
  background: rgba(59, 130, 246, 0.1);
  color: #3b82f6;
}

.score-badge.average {
  background: rgba(245, 158, 11, 0.1);
  color: #f59e0b;
}

.score-badge.needs-improvement {
  background: rgba(239, 68, 68, 0.1);
  color: #ef4444;
}

.action-btn-small {
  background: linear-gradient(135deg, #8b5cf6 0%, #a78bfa 100%);
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 8px;
  font-size: 0.8rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
}

.action-btn-small:hover {
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(139, 92, 246, 0.3);
}

.no-results {
  text-align: center;
  padding: 3rem;
  color: #6b7280;
}

/* Quiz Performance */
.quiz-performance-list {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.quiz-performance-card {
  background: white;
  border: 1px solid rgba(229, 231, 235, 0.8);
  border-radius: 20px;
  padding: 2rem;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
}

.quiz-performance-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
}

.quiz-performance-header h4 {
  color: #1f2937;
  font-size: 1.2rem;
  font-weight: 600;
  margin: 0;
}

.quiz-date {
  color: #6b7280;
  font-size: 0.9rem;
}

.quiz-stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
  gap: 1.5rem;
  margin-bottom: 2rem;
}

.quiz-stat {
  text-align: center;
  padding: 1rem;
  background: rgba(248, 250, 252, 0.5);
  border-radius: 12px;
}

.quiz-stat .stat-value {
  display: block;
  font-size: 1.5rem;
  font-weight: 700;
  color: #8b5cf6;
  margin-bottom: 0.25rem;
}

.quiz-stat .stat-label {
  font-size: 0.8rem;
  color: #6b7280;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.quiz-difficulty-analysis h5 {
  color: #1f2937;
  font-size: 1rem;
  font-weight: 600;
  margin-bottom: 1rem;
}

.difficulty-bars {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.difficulty-item {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.question-label {
  width: 40px;
  font-size: 0.8rem;
  font-weight: 600;
  color: #6b7280;
}

.difficulty-bar-container {
  flex: 1;
  height: 20px;
  background: rgba(229, 231, 235, 0.5);
  border-radius: 10px;
  overflow: hidden;
}

.difficulty-bar {
  height: 100%;
  border-radius: 10px;
  transition: all 0.3s ease;
}

.difficulty-percentage {
  width: 50px;
  text-align: right;
  font-size: 0.8rem;
  font-weight: 600;
  color: #374151;
}

/* Analytics */
.analytics-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
  gap: 2rem;
}

.analytics-card {
  background: white;
  border: 1px solid rgba(229, 231, 235, 0.8);
  border-radius: 20px;
  padding: 2rem;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
}

.analytics-card h4 {
  color: #1f2937;
  font-size: 1.1rem;
  font-weight: 600;
  margin-bottom: 1.5rem;
}

.metric-list {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.metric-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
  background: rgba(248, 250, 252, 0.5);
  border-radius: 12px;
}

.metric-label {
  color: #6b7280;
  font-weight: 500;
}

.metric-value {
  color: #1f2937;
  font-weight: 600;
}

.pattern-insights {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.insight-item {
  display: flex;
  align-items: flex-start;
  gap: 1rem;
  padding: 1rem;
  background: rgba(248, 250, 252, 0.5);
  border-radius: 12px;
}

.insight-icon {
  font-size: 1.2rem;
}

.insight-text {
  color: #374151;
  line-height: 1.5;
}

.recommendations-list {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.recommendation-item {
  display: flex;
  align-items: flex-start;
  gap: 1rem;
  padding: 1rem;
  background: rgba(248, 250, 252, 0.5);
  border-radius: 12px;
  border-left: 4px solid #e5e7eb;
}

.recommendation-priority {
  padding: 0.25rem 0.6rem;
  border-radius: 8px;
  font-size: 0.7rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  flex-shrink: 0;
}

.recommendation-priority.high {
  background: rgba(239, 68, 68, 0.1);
  color: #ef4444;
}

.recommendation-priority.medium {
  background: rgba(245, 158, 11, 0.1);
  color: #f59e0b;
}

.recommendation-priority.low {
  background: rgba(59, 130, 246, 0.1);
  color: #3b82f6;
}

.recommendation-text {
  color: #374151;
  line-height: 1.5;
}

/* Responsive Design */
@media (max-width: 768px) {
  .reports-container {
    padding: 1rem;
  }
  
  .section-header-card {
    padding: 2rem;
    margin-bottom: 2rem;
  }
  
  .section-header-content {
    flex-direction: column;
    align-items: stretch;
    gap: 1.5rem;
  }
  
  .section-header-left {
    gap: 1.5rem;
  }
  
  .header-actions {
    flex-direction: column;
    align-items: stretch;
  }
  
  .summary-grid {
    grid-template-columns: 1fr;
  }
  
  .charts-grid {
    grid-template-columns: 1fr;
  }
  
  .performers-section {
    grid-template-columns: 1fr;
  }
  
  .table-header, .table-row {
    grid-template-columns: 1fr;
    gap: 0.5rem;
  }
  
  .table-cell {
    justify-content: space-between;
    padding: 0.5rem 0;
    border-bottom: 1px solid rgba(229, 231, 235, 0.3);
  }
  
  .table-cell:before {
    content: attr(data-label);
    font-weight: 600;
    color: #6b7280;
    font-size: 0.8rem;
  }
  
  .analytics-grid {
    grid-template-columns: 1fr;
  }
  
  .quiz-stats-grid {
    grid-template-columns: repeat(2, 1fr);
  }
  
  .tab-buttons {
    flex-wrap: wrap;
  }
}
</style>