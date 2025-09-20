<template>
  <div class="analytics-container">
    <!-- Header -->
    <div class="header-section">
      <div class="header-content">
        <h1 class="page-title">Student Analytics</h1>
        <p class="page-subtitle">Monitor and analyze student performance across all assessments</p>
      </div>
      <div class="header-actions">
        <select v-model="selectedSection" @change="filterBySection" class="section-filter">
          <option value="">All Sections</option>
          <option v-for="section in sections" :key="section.id" :value="section.id">
            {{ section.name }} - {{ section.subject }}
          </option>
        </select>
        <button @click="exportData" class="export-btn">
          <i class="fas fa-download"></i>
          Export Data
        </button>
      </div>
    </div>

    <!-- Overview Cards -->
    <div class="overview-grid">
      <div class="overview-card">
        <div class="card-icon">
          <i class="fas fa-chart-line"></i>
        </div>
        <div class="card-content">
          <h3>{{ overallStats.averageScore }}%</h3>
          <p>Overall Average</p>
          <span class="trend" :class="overallStats.trend > 0 ? 'positive' : 'negative'">
            <i :class="overallStats.trend > 0 ? 'fas fa-arrow-up' : 'fas fa-arrow-down'"></i>
            {{ Math.abs(overallStats.trend) }}% from last month
          </span>
        </div>
      </div>

      <div class="overview-card">
        <div class="card-icon">
          <i class="fas fa-users"></i>
        </div>
        <div class="card-content">
          <h3>{{ overallStats.totalStudents }}</h3>
          <p>Total Students</p>
          <span class="info">Across {{ sections.length }} sections</span>
        </div>
      </div>

      <div class="overview-card">
        <div class="card-icon">
          <i class="fas fa-clipboard-check"></i>
        </div>
        <div class="card-content">
          <h3>{{ overallStats.totalAssessments }}</h3>
          <p>Assessments Given</p>
          <span class="info">This academic year</span>
        </div>
      </div>

      <div class="overview-card">
        <div class="card-icon">
          <i class="fas fa-exclamation-triangle"></i>
        </div>
        <div class="card-content">
          <h3>{{ overallStats.studentsNeedingHelp }}</h3>
          <p>Need Remediation</p>
          <span class="warning">Below 75% average</span>
        </div>
      </div>
    </div>

    <!-- Performance Charts -->
    <div class="charts-section">
      <div class="chart-container">
        <h3>Performance Trends</h3>
        <div class="chart-controls">
          <button 
            v-for="period in timePeriods" 
            :key="period.value"
            @click="selectedTimePeriod = period.value"
            :class="['period-btn', { active: selectedTimePeriod === period.value }]"
          >
            {{ period.label }}
          </button>
        </div>
        <canvas ref="performanceChart"></canvas>
      </div>

      <div class="chart-container">
        <h3>Score Distribution</h3>
        <canvas ref="distributionChart"></canvas>
      </div>
    </div>

    <!-- Student Performance Table -->
    <div class="performance-table-section">
      <div class="table-header">
        <h3>Individual Student Performance</h3>
        <div class="table-controls">
          <input 
            v-model="searchQuery" 
            type="text" 
            placeholder="Search students..."
            class="search-input"
          >
          <select v-model="sortBy" @change="sortStudents" class="sort-select">
            <option value="name">Sort by Name</option>
            <option value="average">Sort by Average</option>
            <option value="latest">Sort by Latest Score</option>
            <option value="improvement">Sort by Improvement</option>
          </select>
        </div>
      </div>

      <div class="table-wrapper">
        <table class="performance-table">
          <thead>
            <tr>
              <th>Student</th>
              <th>Section</th>
              <th>Assessments Taken</th>
              <th>Average Score</th>
              <th>Latest Score</th>
              <th>Improvement</th>
              <th>Status</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="student in filteredStudents" :key="student.id" class="student-row">
              <td class="student-cell">
                <div class="student-info">
                  <div class="student-avatar">
                    <img v-if="student.avatar_url" :src="student.avatar_url" :alt="student.full_name">
                    <div v-else class="avatar-placeholder">
                      {{ getInitials(student.full_name) }}
                    </div>
                  </div>
                  <div>
                    <div class="student-name">{{ student.full_name }}</div>
                    <div class="student-id">ID: {{ student.student_id }}</div>
                  </div>
                </div>
              </td>
              <td>{{ student.section_name }}</td>
              <td>{{ student.assessments_count }}</td>
              <td>
                <div class="score-cell">
                  <span class="score-value">{{ student.average_score }}%</span>
                  <div class="score-bar">
                    <div 
                      class="score-fill" 
                      :style="{ width: student.average_score + '%' }"
                      :class="getScoreClass(student.average_score)"
                    ></div>
                  </div>
                </div>
              </td>
              <td>
                <span :class="['score-badge', getScoreClass(student.latest_score)]">
                  {{ student.latest_score }}%
                </span>
              </td>
              <td>
                <span :class="['improvement-badge', student.improvement >= 0 ? 'positive' : 'negative']">
                  <i :class="student.improvement >= 0 ? 'fas fa-arrow-up' : 'fas fa-arrow-down'"></i>
                  {{ Math.abs(student.improvement) }}%
                </span>
              </td>
              <td>
                <span :class="['status-badge', getStatusClass(student.average_score)]">
                  {{ getStatusText(student.average_score) }}
                </span>
              </td>
              <td class="actions-cell">
                <button @click="viewStudentDetails(student)" class="action-btn view-btn">
                  <i class="fas fa-eye"></i>
                </button>
                <button @click="updateScore(student)" class="action-btn edit-btn">
                  <i class="fas fa-edit"></i>
                </button>
                <button 
                  v-if="student.average_score < 75" 
                  @click="flagForRemediation(student)" 
                  class="action-btn warning-btn"
                >
                  <i class="fas fa-flag"></i>
                </button>
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
          <h3>{{ selectedStudent.full_name }} - Performance Details</h3>
          <button @click="selectedStudent = null" class="close-btn">
            <i class="fas fa-times"></i>
          </button>
        </div>
        
        <div class="modal-content">
          <div class="student-summary">
            <div class="summary-stat">
              <h4>{{ selectedStudent.average_score }}%</h4>
              <p>Average Score</p>
            </div>
            <div class="summary-stat">
              <h4>{{ selectedStudent.assessments_count }}</h4>
              <p>Assessments</p>
            </div>
            <div class="summary-stat">
              <h4>{{ selectedStudent.improvement }}%</h4>
              <p>Improvement</p>
            </div>
          </div>

          <div class="assessment-history">
            <h4>Assessment History</h4>
            <div class="history-list">
              <div v-for="assessment in selectedStudent.assessments" :key="assessment.id" class="history-item">
                <div class="assessment-info">
                  <h5>{{ assessment.title }}</h5>
                  <p>{{ formatDate(assessment.created_at) }}</p>
                </div>
                <div class="assessment-score">
                  <span :class="['score-badge', getScoreClass(assessment.score)]">
                    {{ assessment.score }}%
                  </span>
                </div>
              </div>
            </div>
          </div>

          <div class="remediation-notes">
            <h4>Notes & Comments</h4>
            <textarea 
              v-model="studentNotes" 
              rows="4" 
              placeholder="Add notes about this student's performance..."
              class="notes-textarea"
            ></textarea>
            <button @click="saveStudentNotes" class="save-notes-btn">
              Save Notes
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Update Score Modal -->
    <div v-if="showUpdateModal" class="modal-overlay" @click.self="showUpdateModal = false">
      <div class="modal">
        <div class="modal-header">
          <h3>Update Score</h3>
          <button @click="showUpdateModal = false" class="close-btn">
            <i class="fas fa-times"></i>
          </button>
        </div>
        
        <form @submit.prevent="saveScoreUpdate" class="modal-form">
          <div class="form-group">
            <label>Student: {{ updateStudent?.full_name }}</label>
          </div>
          
          <div class="form-group">
            <label>Assessment</label>
            <select v-model="scoreUpdate.assessment_id" required>
              <option v-for="assessment in updateStudent?.assessments" :key="assessment.id" :value="assessment.id">
                {{ assessment.title }}
              </option>
            </select>
          </div>
          
          <div class="form-group">
            <label>New Score (%)</label>
            <input v-model="scoreUpdate.score" type="number" min="0" max="100" required>
          </div>
          
          <div class="form-group">
            <label>Comment (Optional)</label>
            <textarea v-model="scoreUpdate.comment" rows="3"></textarea>
          </div>
          
          <div class="modal-actions">
            <button type="button" @click="showUpdateModal = false" class="cancel-btn">Cancel</button>
            <button type="submit" :disabled="loading" class="submit-btn">
              {{ loading ? 'Updating...' : 'Update Score' }}
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted, computed, nextTick } from 'vue'
import { supabase } from '../../supabase.js'

export default {
  name: 'AnalyticsView',
  setup() {
    const sections = ref([])
    const students = ref([])
    const assessments = ref([])
    const selectedSection = ref('')
    const selectedTimePeriod = ref('month')
    const searchQuery = ref('')
    const sortBy = ref('name')
    const currentPage = ref(1)
    const itemsPerPage = 10
    const loading = ref(false)
    const selectedStudent = ref(null)
    const showUpdateModal = ref(false)
    const updateStudent = ref(null)
    const studentNotes = ref('')
    
    const scoreUpdate = ref({
      assessment_id: '',
      score: '',
      comment: ''
    })

    const timePeriods = [
      { value: 'week', label: 'This Week' },
      { value: 'month', label: 'This Month' },
      { value: 'quarter', label: 'This Quarter' },
      { value: 'year', label: 'This Year' }
    ]

    // Chart references
    const performanceChart = ref(null)
    const distributionChart = ref(null)

    // Computed properties
    const overallStats = computed(() => {
      const totalStudents = students.value.length
      const totalAssessments = assessments.value.length
      const averageScore = totalStudents > 0 
        ? Math.round(students.value.reduce((sum, student) => sum + student.average_score, 0) / totalStudents)
        : 0
      const studentsNeedingHelp = students.value.filter(student => student.average_score < 75).length
      
      return {
        totalStudents,
        totalAssessments,
        averageScore,
        studentsNeedingHelp,
        trend: Math.floor(Math.random() * 20) - 10 // Mock trend data
      }
    })

    const filteredStudents = computed(() => {
      let filtered = students.value

      if (selectedSection.value) {
        filtered = filtered.filter(student => student.section_id === selectedSection.value)
      }

      if (searchQuery.value) {
        filtered = filtered.filter(student => 
          student.full_name.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
          student.student_id.toLowerCase().includes(searchQuery.value.toLowerCase())
        )
      }

      // Sort students
      filtered.sort((a, b) => {
        switch (sortBy.value) {
          case 'average':
            return b.average_score - a.average_score
          case 'latest':
            return b.latest_score - a.latest_score
          case 'improvement':
            return b.improvement - a.improvement
          default:
            return a.full_name.localeCompare(b.full_name)
        }
      })

      // Pagination
      const start = (currentPage.value - 1) * itemsPerPage
      return filtered.slice(start, start + itemsPerPage)
    })

    const totalPages = computed(() => {
      let filtered = students.value
      if (selectedSection.value) {
        filtered = filtered.filter(student => student.section_id === selectedSection.value)
      }
      if (searchQuery.value) {
        filtered = filtered.filter(student => 
          student.full_name.toLowerCase().includes(searchQuery.value.toLowerCase())
        )
      }
      return Math.ceil(filtered.length / itemsPerPage)
    })

    // Methods
    const fetchData = async () => {
      loading.value = true
      try {
        const { data: user } = await supabase.auth.getUser()
        if (!user.user) return

        // Fetch sections
        const { data: sectionsData } = await supabase
          .from('sections')
          .select('*')
          .eq('teacher_id', user.user.id)

        sections.value = sectionsData || []

        // Fetch students with their performance data
        const { data: studentsData } = await supabase
          .from('profiles')
          .select(`
            *,
            student_enrollments!inner(
              section:sections!inner(
                id, name, subject,
                teacher_id
              )
            ),
            assessment_results(
              score,
              assessment:assessments(
                id, title, created_at
              )
            )
          `)
          .eq('role', 'student')
          .eq('student_enrollments.section.teacher_id', user.user.id)

        // Process student data
        students.value = (studentsData || []).map(student => {
          const results = student.assessment_results || []
          const scores = results.map(r => r.score).filter(s => s != null)
          
          const average_score = scores.length > 0 
            ? Math.round(scores.reduce((sum, score) => sum + score, 0) / scores.length)
            : 0
          
          const latest_score = scores.length > 0 ? scores[scores.length - 1] : 0
          const first_score = scores.length > 0 ? scores[0] : 0
          const improvement = latest_score - first_score
          
          return {
            ...student,
            section_id: student.student_enrollments[0]?.section?.id,
            section_name: student.student_enrollments[0]?.section?.name,
            assessments: results.map(r => ({
              ...r.assessment,
              score: r.score
            })),
            assessments_count: results.length,
            average_score,
            latest_score,
            improvement
          }
        })

        // Fetch assessments
        const { data: assessmentsData } = await supabase
          .from('assessments')
          .select('*')
          .eq('teacher_id', user.user.id)

        assessments.value = assessmentsData || []

      } catch (error) {
        console.error('Error fetching analytics data:', error)
      } finally {
        loading.value = false
      }
    }

    const filterBySection = () => {
      currentPage.value = 1
    }

    const sortStudents = () => {
      currentPage.value = 1
    }

    const viewStudentDetails = (student) => {
      selectedStudent.value = student
      studentNotes.value = student.notes || ''
    }

    const updateScore = (student) => {
      updateStudent.value = student
      showUpdateModal.value = true
      scoreUpdate.value = {
        assessment_id: '',
        score: '',
        comment: ''
      }
    }

    const saveScoreUpdate = async () => {
      loading.value = true
      try {
        const { error } = await supabase
          .from('assessment_results')
          .update({
            score: parseInt(scoreUpdate.value.score),
            comment: scoreUpdate.value.comment
          })
          .eq('assessment_id', scoreUpdate.value.assessment_id)
          .eq('student_id', updateStudent.value.id)

        if (error) throw error

        showUpdateModal.value = false
        await fetchData() // Refresh data
        alert('Score updated successfully!')
      } catch (error) {
        console.error('Error updating score:', error)
        alert('Error updating score')
      } finally {
        loading.value = false
      }
    }

    const flagForRemediation = async (student) => {
      try {
        const { error } = await supabase
          .from('profiles')
          .update({
            needs_remediation: true,
            remediation_flagged_at: new Date().toISOString()
          })
          .eq('id', student.id)

        if (error) throw error
        
        alert(`${student.full_name} has been flagged for remediation`)
        await fetchData()
      } catch (error) {
        console.error('Error flagging student:', error)
      }
    }

    const saveStudentNotes = async () => {
      try {
        const { error } = await supabase
          .from('profiles')
          .update({ notes: studentNotes.value })
          .eq('id', selectedStudent.value.id)

        if (error) throw error
        
        alert('Notes saved successfully!')
      } catch (error) {
        console.error('Error saving notes:', error)
      }
    }

    const exportData = () => {
      // Create CSV data
      const headers = ['Student Name', 'Section', 'Average Score', 'Latest Score', 'Assessments Count', 'Status']
      const csvData = students.value.map(student => [
        student.full_name,
        student.section_name,
        student.average_score,
        student.latest_score,
        student.assessments_count,
        getStatusText(student.average_score)
      ])

      const csvContent = [headers, ...csvData]
        .map(row => row.map(field => `"${field}"`).join(','))
        .join('\n')

      // Download CSV
      const blob = new Blob([csvContent], { type: 'text/csv' })
      const url = window.URL.createObjectURL(blob)
      const link = document.createElement('a')
      link.href = url
      link.download = `student_analytics_${new Date().toISOString().split('T')[0]}.csv`
      link.click()
      window.URL.revokeObjectURL(url)
    }

    const getInitials = (name) => {
      return name.split(' ').map(n => n[0]).join('').toUpperCase()
    }

    const getScoreClass = (score) => {
      if (score >= 90) return 'excellent'
      if (score >= 80) return 'good'
      if (score >= 75) return 'satisfactory'
      return 'needs-improvement'
    }

    const getStatusClass = (score) => {
      if (score >= 90) return 'excellent'
      if (score >= 80) return 'good'
      if (score >= 75) return 'satisfactory'
      return 'warning'
    }

    const getStatusText = (score) => {
      if (score >= 90) return 'Excellent'
      if (score >= 80) return 'Good'
      if (score >= 75) return 'Satisfactory'
      return 'Needs Help'
    }

    const formatDate = (dateString) => {
      return new Date(dateString).toLocaleDateString()
    }

    const initializeCharts = () => {
      // This would integrate with Chart.js or similar library
      // For now, we'll just show placeholders
      console.log('Charts would be initialized here')
    }

    onMounted(async () => {
      await fetchData()
      await nextTick()
      initializeCharts()
    })

    return {
      sections,
      students,
      assessments,
      selectedSection,
      selectedTimePeriod,
      searchQuery,
      sortBy,
      currentPage,
      itemsPerPage,
      loading,
      selectedStudent,
      showUpdateModal,
      updateStudent,
      studentNotes,
      scoreUpdate,
      timePeriods,
      performanceChart,
      distributionChart,
      overallStats,
      filteredStudents,
      totalPages,
      fetchData,
      filterBySection,
      sortStudents,
      viewStudentDetails,
      updateScore,
      saveScoreUpdate,
      flagForRemediation,
      saveStudentNotes,
      exportData,
      getInitials,
      getScoreClass,
      getStatusClass,
      getStatusText,
      formatDate
    }
  }
}
</script>

<style scoped>
.analytics-container {
  padding: 2rem;
  max-width: 1400px;
  margin: 0 auto;
}

.header-section {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
}

.page-title {
  font-size: 2rem;
  font-weight: bold;
  color: #1f2937;
  margin: 0;
}

.page-subtitle {
  color: #6b7280;
  margin: 0.5rem 0 0 0;
}

.header-actions {
  display: flex;
  gap: 1rem;
  align-items: center;
}

.section-filter {
  padding: 0.5rem 1rem;
  border: 1px solid #d1d5db;
  border-radius: 0.5rem;
  background: white;
}

.export-btn {
  background: #10b981;
  color: white;
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 0.5rem;
  cursor: pointer;
  font-weight: 500;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  transition: all 0.2s;
}

.export-btn:hover {
  background: #059669;
}

.overview-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
  margin-bottom: 2rem;
}

.overview-card {
  background: white;
  border-radius: 1rem;
  padding: 1.5rem;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  display: flex;
  align-items: center;
  gap: 1rem;
}

.card-icon {
  width: 4rem;
  height: 4rem;
  border-radius: 1rem;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-size: 1.5rem;
}

.card-content h3 {
  font-size: 2rem;
  font-weight: bold;
  color: #1f2937;
  margin: 0;
}

.card-content p {
  color: #6b7280;
  margin: 0.25rem 0 0.5rem 0;
  font-size: 0.875rem;
  font-weight: 500;
}

.trend {
  font-size: 0.75rem;
  font-weight: 500;
  display: flex;
  align-items: center;
  gap: 0.25rem;
}

.trend.positive {
  color: #10b981;
}

.trend.negative {
  color: #ef4444;
}

.info {
  color: #6b7280;
  font-size: 0.75rem;
}

.warning {
  color: #f59e0b;
  font-size: 0.75rem;
  font-weight: 500;
}

.charts-section {
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: 2rem;
  margin-bottom: 2rem;
}

.chart-container {
  background: white;
  border-radius: 1rem;
  padding: 1.5rem;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.chart-container h3 {
  color: #1f2937;
  font-size: 1.25rem;
  margin: 0 0 1rem 0;
}

.chart-controls {
  display: flex;
  gap: 0.5rem;
  margin-bottom: 1rem;
}

.period-btn {
  padding: 0.5rem 1rem;
  border: 1px solid #e5e7eb;
  background: white;
  color: #6b7280;
  border-radius: 0.5rem;
  cursor: pointer;
  font-size: 0.875rem;
  transition: all 0.2s;
}

.period-btn.active {
  background: #667eea;
  color: white;
  border-color: #667eea;
}

.performance-table-section {
  background: white;
  border-radius: 1rem;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  overflow: hidden;
}

.table-header {
  padding: 1.5rem;
  border-bottom: 1px solid #e5e7eb;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.table-header h3 {
  color: #1f2937;
  margin: 0;
}

.table-controls {
  display: flex;
  gap: 1rem;
  align-items: center;
}

.search-input {
  padding: 0.5rem 1rem;
  border: 1px solid #d1d5db;
  border-radius: 0.5rem;
  width: 200px;
}

.sort-select {
  padding: 0.5rem 1rem;
  border: 1px solid #d1d5db;
  border-radius: 0.5rem;
  background: white;
}

.table-wrapper {
  overflow-x: auto;
}

.performance-table {
  width: 100%;
  border-collapse: collapse;
}

.performance-table th,
.performance-table td {
  padding: 1rem;
  text-align: left;
  border-bottom: 1px solid #e5e7eb;
}

.performance-table th {
  background: #f9fafb;
  font-weight: 600;
  color: #374151;
  font-size: 0.875rem;
}

.student-cell {
  width: 200px;
}

.student-info {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.student-avatar {
  width: 2.5rem;
  height: 2.5rem;
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
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: bold;
  font-size: 0.875rem;
}

.student-name {
  font-weight: 500;
  color: #1f2937;
}

.student-id {
  font-size: 0.75rem;
  color: #6b7280;
}

.score-cell {
  min-width: 120px;
}

.score-value {
  font-weight: 600;
  color: #1f2937;
}

.score-bar {
  width: 100%;
  height: 4px;
  background: #e5e7eb;
  border-radius: 2px;
  margin-top: 0.25rem;
  overflow: hidden;
}

.score-fill {
  height: 100%;
  border-radius: 2px;
  transition: width 0.3s ease;
}

.score-fill.excellent {
  background: #10b981;
}

.score-fill.good {
  background: #3b82f6;
}

.score-fill.satisfactory {
  background: #f59e0b;
}

.score-fill.needs-improvement {
  background: #ef4444;
}

.score-badge {
  padding: 0.25rem 0.75rem;
  border-radius: 1rem;
  font-size: 0.75rem;
  font-weight: 600;
}

.score-badge.excellent {
  background: #d1fae5;
  color: #065f46;
}

.score-badge.good {
  background: #dbeafe;
  color: #1e40af;
}

.score-badge.satisfactory {
  background: #fef3c7;
  color: #92400e;
}

.score-badge.needs-improvement {
  background: #fecaca;
  color: #991b1b;
}

.improvement-badge {
  padding: 0.25rem 0.5rem;
  border-radius: 0.375rem;
  font-size: 0.75rem;
  font-weight: 500;
  display: flex;
  align-items: center;
  gap: 0.25rem;
  width: fit-content;
}

.improvement-badge.positive {
  background: #d1fae5;
  color: #065f46;
}

.improvement-badge.negative {
  background: #fecaca;
  color: #991b1b;
}

.status-badge {
  padding: 0.25rem 0.75rem;
  border-radius: 1rem;
  font-size: 0.75rem;
  font-weight: 600;
}

.status-badge.excellent {
  background: #d1fae5;
  color: #065f46;
}

.status-badge.good {
  background: #dbeafe;
  color: #1e40af;
}

.status-badge.satisfactory {
  background: #fef3c7;
  color: #92400e;
}

.status-badge.warning {
  background: #fecaca;
  color: #991b1b;
}

.actions-cell {
  width: 120px;
}

.action-btn {
  width: 2rem;
  height: 2rem;
  border: none;
  border-radius: 0.375rem;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  margin-right: 0.25rem;
  transition: all 0.2s;
}

.view-btn {
  background: #f3f4f6;
  color: #374151;
}

.view-btn:hover {
  background: #e5e7eb;
}

.edit-btn {
  background: #fef3c7;
  color: #d97706;
}

.edit-btn:hover {
  background: #fde68a;
}

.warning-btn {
  background: #fecaca;
  color: #dc2626;
}

.warning-btn:hover {
  background: #fca5a5;
}

.pagination {
  padding: 1rem 1.5rem;
  border-top: 1px solid #e5e7eb;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.page-btn {
  padding: 0.5rem 1rem;
  border: 1px solid #d1d5db;
  background: white;
  color: #374151;
  border-radius: 0.375rem;
  cursor: pointer;
  font-weight: 500;
  transition: all 0.2s;
}

.page-btn:hover:not(:disabled) {
  background: #f9fafb;
}

.page-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.page-info {
  color: #6b7280;
  font-size: 0.875rem;
}

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
  border-radius: 1rem;
  max-width: 500px;
  width: 90%;
  max-height: 90vh;
  overflow-y: auto;
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

.modal-header h3 {
  margin: 0;
  color: #1f2937;
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
  border-radius: 0.375rem;
  transition: all 0.2s;
}

.close-btn:hover {
  background: #f3f4f6;
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
  background: #f9fafb;
  border-radius: 0.5rem;
}

.summary-stat h4 {
  font-size: 1.5rem;
  font-weight: bold;
  color: #1f2937;
  margin: 0;
}

.summary-stat p {
  color: #6b7280;
  font-size: 0.875rem;
  margin: 0.25rem 0 0 0;
}

.assessment-history h4 {
  color: #1f2937;
  margin: 0 0 1rem 0;
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
  border-radius: 0.5rem;
  margin-bottom: 0.5rem;
}

.assessment-info h5 {
  font-weight: 500;
  color: #1f2937;
  margin: 0;
}

.assessment-info p {
  color: #6b7280;
  font-size: 0.75rem;
  margin: 0.25rem 0 0 0;
}

.remediation-notes {
  margin-top: 1.5rem;
}

.remediation-notes h4 {
  color: #1f2937;
  margin: 0 0 1rem 0;
}

.notes-textarea {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid #d1d5db;
  border-radius: 0.5rem;
  resize: vertical;
  font-family: inherit;
}

.save-notes-btn {
  background: #10b981;
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 0.375rem;
  cursor: pointer;
  font-weight: 500;
  margin-top: 0.5rem;
  transition: all 0.2s;
}

.save-notes-btn:hover {
  background: #059669;
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

.form-group input,
.form-group select,
.form-group textarea {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid #d1d5db;
  border-radius: 0.5rem;
  font-size: 0.875rem;
}

.form-group input:focus,
.form-group select:focus,
.form-group textarea:focus {
  outline: none;
  border-color: #667eea;
  box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
}

.modal-actions {
  display: flex;
  gap: 0.75rem;
  justify-content: flex-end;
  margin-top: 1.5rem;
}

.cancel-btn {
  padding: 0.75rem 1.5rem;
  border: 1px solid #d1d5db;
  background: white;
  color: #374151;
  border-radius: 0.5rem;
  cursor: pointer;
  font-weight: 500;
  transition: all 0.2s;
}

.cancel-btn:hover {
  background: #f9fafb;
}

.submit-btn {
  padding: 0.75rem 1.5rem;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border: none;
  border-radius: 0.5rem;
  cursor: pointer;
  font-weight: 500;
  transition: all 0.2s;
}

.submit-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.submit-btn:hover:not(:disabled) {
  transform: translateY(-1px);
}

@media (max-width: 1024px) {
  .charts-section {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 768px) {
  .analytics-container {
    padding: 1rem;
  }
  
  .header-section {
    flex-direction: column;
    gap: 1rem;
    align-items: stretch;
  }
  
  .header-actions {
    flex-direction: column;
    gap: 0.5rem;
  }
  
  .overview-grid {
    grid-template-columns: 1fr;
  }
  
  .table-header {
    flex-direction: column;
    gap: 1rem;
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
  
  .student-cell {
    width: auto;
    min-width: 150px;
  }
  
  .student-summary {
    grid-template-columns: 1fr;
  }
}
</style>