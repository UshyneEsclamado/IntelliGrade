<template>
  <div class="analytics-container" :class="{ 'dark-mode': isDarkMode }">
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
              <path d="M22,21H2V3H4V19H6V10H10V19H12V6H16V19H18V14H22V21Z" />
            </svg>
          </div>
          <div class="header-text">
            <div class="section-header-title">Student Analytics</div>
            <div class="section-header-subtitle">Performance Insights</div>
            <div class="section-header-description">Monitor and analyze student performance across all assessments</div>
          </div>
        </div>
        
        <div class="header-actions">
          <select v-model="selectedSection" @change="filterBySection" class="section-filter">
            <option value="">All Sections</option>
            <option v-for="section in sections" :key="section.id" :value="section.id">
              {{ section.name }} - {{ section.subject }}
            </option>
          </select>
          <button @click="exportData" class="export-btn">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M14,2H6A2,2 0 0,0 4,4V20A2,2 0 0,0 6,22H18A2,2 0 0,0 20,20V8L14,2M18,20H6V4H13V9H18V20Z" />
            </svg>
            Export Data
          </button>
        </div>
      </div>
    </div>

    <!-- Enhanced Overview Cards -->
    <div class="overview-grid">
      <div class="overview-card">
        <div class="card-floating-shapes">
          <div class="card-shape shape-1"></div>
        </div>
        <div class="card-icon">
          <svg width="28" height="28" viewBox="0 0 24 24" fill="currentColor">
            <path d="M16,6L18.29,8.29L13.41,13.17L9.41,9.17L2,16.59L3.41,18L9.41,12L13.41,16L19.71,9.71L22,12V6H16Z" />
          </svg>
        </div>
        <div class="card-content">
          <h3>{{ overallStats.averageScore }}%</h3>
          <p>Overall Average</p>
          <span class="trend" :class="overallStats.trend > 0 ? 'positive' : 'negative'">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
              <path :d="overallStats.trend > 0 ? 'M7,14H17V16H7V14M12,2A10,10 0 0,1 22,12A10,10 0 0,1 12,22A10,10 0 0,1 2,12A10,10 0 0,1 12,2M12,4A8,8 0 0,0 4,12A8,8 0 0,0 12,20A8,8 0 0,0 20,12A8,8 0 0,0 12,4M7,9H17V11H7V9Z' : 'M7,9H17V11H7V9M12,2A10,10 0 0,1 22,12A10,10 0 0,1 12,22A10,10 0 0,1 2,12A10,10 0 0,1 12,2M12,4A8,8 0 0,0 4,12A8,8 0 0,0 12,20A8,8 0 0,0 20,12A8,8 0 0,0 12,4Z'" />
            </svg>
            {{ Math.abs(overallStats.trend) }}% from last month
          </span>
        </div>
      </div>

      <div class="overview-card">
        <div class="card-floating-shapes">
          <div class="card-shape shape-2"></div>
        </div>
        <div class="card-icon">
          <svg width="28" height="28" viewBox="0 0 24 24" fill="currentColor">
            <path d="M12,5.5A3.5,3.5 0 0,1 15.5,9A3.5,3.5 0 0,1 12,12.5A3.5,3.5 0 0,1 8.5,9A3.5,3.5 0 0,1 12,5.5M5,8C5.56,8 6.08,8.15 6.53,8.42C6.38,9.85 6.8,11.27 7.66,12.38C7.16,13.34 6.16,14 5,14A3,3 0 0,1 2,11A3,3 0 0,1 5,8M19,8A3,3 0 0,1 22,11A3,3 0 0,1 19,14C17.84,14 16.84,13.34 16.34,12.38C17.2,11.27 17.62,9.85 17.47,8.42C17.92,8.15 18.44,8 19,8M5.5,18.25C5.5,16.18 8.41,14.5 12,14.5C15.59,14.5 18.5,16.18 18.5,18.25V20H5.5V18.25M0,20V18.5C0,17.11 1.89,15.94 4.45,15.6C3.86,16.28 3.5,17.22 3.5,18.25V20H0M24,20H20.5V18.25C20.5,17.22 20.14,16.28 19.55,15.6C22.11,15.94 24,17.11 24,18.5V20Z" />
          </svg>
        </div>
        <div class="card-content">
          <h3>{{ overallStats.totalStudents }}</h3>
          <p>Total Students</p>
          <span class="info">Across {{ sections.length }} sections</span>
        </div>
      </div>

      <div class="overview-card">
        <div class="card-floating-shapes">
          <div class="card-shape shape-3"></div>
        </div>
        <div class="card-icon">
          <svg width="28" height="28" viewBox="0 0 24 24" fill="currentColor">
            <path d="M19,3H5C3.9,3 3,3.9 3,5V19C3,20.1 3.9,21 5,21H19C20.1,21 21,20.1 21,19V5C21,3.9 20.1,3 19,3M9,17H7V10H9V17M13,17H11V7H13V17M17,17H15V13H17V17Z" />
          </svg>
        </div>
        <div class="card-content">
          <h3>{{ overallStats.totalAssessments }}</h3>
          <p>Assessments Given</p>
          <span class="info">This academic year</span>
        </div>
      </div>

      <div class="overview-card alert-card">
        <div class="card-floating-shapes">
          <div class="card-shape shape-4"></div>
        </div>
        <div class="card-icon">
          <svg width="28" height="28" viewBox="0 0 24 24" fill="currentColor">
            <path d="M13,14H11V10H13M13,18H11V16H13M1,21H23L12,2L1,21Z" />
          </svg>
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

<script lang="ts">
import { ref, onMounted, computed, nextTick } from 'vue'
import { supabase } from '../../supabase.js'
import { useDarkMode } from '../../composables/useDarkMode.js'

export default {
  name: 'AnalyticsView',
  setup() {
    // Dark mode
    const { isDarkMode, initDarkMode } = useDarkMode()
    
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
      initDarkMode()
      await fetchData()
      await nextTick()
      initializeCharts()
    })

    return {
      isDarkMode,
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
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

.analytics-container {
  padding: 2rem 5%;
  font-family: 'Inter', sans-serif;
  min-height: 100vh;
  background: linear-gradient(135deg, #f0f9f6 0%, #e8f5f0 100%);
}

/* Enhanced Header Section */
.section-header-card {
  position: relative;
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(20px);
  border: 1px solid rgba(61, 141, 122, 0.1);
  border-radius: 24px;
  padding: 2.5rem;
  margin-bottom: 2rem;
  overflow: hidden;
  box-shadow: 
    0 8px 32px rgba(61, 141, 122, 0.1),
    0 0 0 1px rgba(255, 255, 255, 0.2);
}

.header-bg-decoration {
  position: absolute;
  top: 0;
  right: 0;
  width: 200px;
  height: 200px;
  background: linear-gradient(135deg, rgba(61, 141, 122, 0.05), rgba(163, 209, 198, 0.05));
  border-radius: 50%;
  transform: translate(50%, -50%);
  pointer-events: none;
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

.shape {
  position: absolute;
  border-radius: 50%;
  background: linear-gradient(135deg, #3D8D7A, #A3D1C6);
  opacity: 0.1;
  animation: floatBackground 8s ease-in-out infinite;
}

.shape.shape-1 {
  width: 80px;
  height: 80px;
  top: 20%;
  left: 10%;
  animation-delay: 0s;
}

.shape.shape-2 {
  width: 120px;
  height: 120px;
  top: 60%;
  right: 15%;
  animation-delay: 2s;
}

.shape.shape-3 {
  width: 60px;
  height: 60px;
  bottom: 20%;
  left: 70%;
  animation-delay: 4s;
}

@keyframes floatBackground {
  0%, 100% { transform: translateY(0px) rotate(0deg); opacity: 0.1; }
  50% { transform: translateY(-30px) rotate(180deg); opacity: 0.15; }
}

.section-header-content {
  position: relative;
  z-index: 2;
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 2rem;
}

.section-header-left {
  display: flex;
  align-items: center;
  gap: 1.5rem;
  flex: 1;
}

.section-header-icon {
  width: 60px;
  height: 60px;
  background: linear-gradient(135deg, #3D8D7A, #2c6b5c);
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  box-shadow: 0 4px 12px rgba(61, 141, 122, 0.3);
}

.header-text {
  flex: 1;
}

.section-header-title {
  font-size: 2rem;
  font-weight: 800;
  color: #3D8D7A;
  margin-bottom: 0.5rem;
  letter-spacing: -0.5px;
}

.section-header-subtitle {
  font-size: 1.1rem;
  font-weight: 600;
  color: #10b981;
  margin-bottom: 0.5rem;
}

.section-header-description {
  font-size: 0.95rem;
  color: #6b7280;
  font-weight: 500;
}

.header-actions {
  display: flex;
  gap: 1rem;
  align-items: center;
  flex-wrap: wrap;
}

.section-filter {
  padding: 0.875rem 1.25rem;
  border: 2px solid rgba(61, 141, 122, 0.1);
  border-radius: 16px;
  font-size: 0.95rem;
  font-weight: 500;
  background: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(10px);
  color: #3D8D7A;
  min-width: 200px;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  cursor: pointer;
}

.section-filter:focus {
  outline: none;
  border-color: rgba(61, 141, 122, 0.3);
  box-shadow: 0 0 0 4px rgba(61, 141, 122, 0.1);
  transform: translateY(-1px);
}

.export-btn {
  background: linear-gradient(135deg, #10b981, #059669);
  color: white;
  border: none;
  padding: 0.875rem 1.75rem;
  border-radius: 16px;
  cursor: pointer;
  font-weight: 600;
  font-size: 0.95rem;
  display: flex;
  align-items: center;
  gap: 0.75rem;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  position: relative;
  overflow: hidden;
}

.export-btn::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
  transition: left 0.5s;
}

.export-btn:hover::before {
  left: 100%;
}

.export-btn:hover {
  background: linear-gradient(135deg, #059669, #047857);
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(16, 185, 129, 0.4);
}

.export-btn:hover svg {
  transform: scale(1.1);
}

/* Enhanced Overview Cards */
.overview-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.5rem;
  margin-bottom: 2.5rem;
}

.overview-card {
  position: relative;
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(20px);
  border: 1px solid rgba(61, 141, 122, 0.1);
  border-radius: 20px;
  padding: 2rem 1.5rem;
  overflow: hidden;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  box-shadow: 
    0 4px 16px rgba(61, 141, 122, 0.05),
    0 0 0 1px rgba(255, 255, 255, 0.1);
}

.overview-card:hover {
  transform: translateY(-4px);
  box-shadow: 
    0 12px 32px rgba(61, 141, 122, 0.15),
    0 0 0 1px rgba(255, 255, 255, 0.2);
  border-color: rgba(61, 141, 122, 0.2);
}

.overview-card.alert-card {
  border-color: rgba(249, 115, 22, 0.2);
  background: rgba(255, 255, 255, 0.98);
}

.overview-card.alert-card:hover {
  border-color: rgba(249, 115, 22, 0.3);
  box-shadow: 
    0 12px 32px rgba(249, 115, 22, 0.15),
    0 0 0 1px rgba(255, 255, 255, 0.2);
}

.card-floating-shapes {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  pointer-events: none;
  overflow: hidden;
}

.card-shape {
  position: absolute;
  border-radius: 50%;
  opacity: 0.08;
  animation: floatCard 4s ease-in-out infinite;
}

.card-shape.shape-1 {
  width: 60px;
  height: 60px;
  background: linear-gradient(135deg, #10b981, #059669);
  top: -20px;
  right: -20px;
  animation-delay: 0s;
}

.card-shape.shape-2 {
  width: 80px;
  height: 80px;
  background: linear-gradient(135deg, #3b82f6, #2563eb);
  bottom: -30px;
  left: -30px;
  animation-delay: 1s;
}

.card-shape.shape-3 {
  width: 50px;
  height: 50px;
  background: linear-gradient(135deg, #10b981, #059669);
  top: 50%;
  right: -15px;
  animation-delay: 2s;
}

.card-shape.shape-4 {
  width: 70px;
  height: 70px;
  background: linear-gradient(135deg, #f59e0b, #d97706);
  bottom: -25px;
  right: 20%;
  animation-delay: 1.5s;
}

@keyframes floatCard {
  0%, 100% { transform: translateY(0px) scale(1); }
  50% { transform: translateY(-10px) scale(1.1); }
}

.card-icon {
  width: 56px;
  height: 56px;
  background: linear-gradient(135deg, #3D8D7A, #2c6b5c);
  border-radius: 14px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  margin-bottom: 1.25rem;
  position: relative;
  z-index: 2;
  box-shadow: 0 4px 12px rgba(61, 141, 122, 0.25);
  transition: all 0.3s ease;
}

.overview-card:hover .card-icon {
  transform: scale(1.05);
  box-shadow: 0 6px 20px rgba(61, 141, 122, 0.35);
}

.card-content {
  position: relative;
  z-index: 2;
}

.card-content h3 {
  font-size: 2rem;
  font-weight: 800;
  color: #3D8D7A;
  margin: 0 0 0.5rem 0;
  letter-spacing: -0.5px;
}

.card-content p {
  font-size: 1rem;
  font-weight: 600;
  color: #374151;
  margin: 0 0 0.75rem 0;
}

.trend {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.85rem;
  font-weight: 600;
  padding: 0.375rem 0.75rem;
  border-radius: 8px;
  transition: all 0.3s ease;
}

.trend.positive {
  background: linear-gradient(135deg, rgba(16, 185, 129, 0.1), rgba(5, 150, 105, 0.1));
  color: #059669;
  border: 1px solid rgba(16, 185, 129, 0.2);
}

.trend.negative {
  background: linear-gradient(135deg, rgba(239, 68, 68, 0.1), rgba(220, 38, 38, 0.1));
  color: #dc2626;
  border: 1px solid rgba(239, 68, 68, 0.2);
}

.info {
  display: inline-flex;
  align-items: center;
  font-size: 0.85rem;
  font-weight: 500;
  color: #6b7280;
  background: rgba(107, 114, 128, 0.1);
  padding: 0.375rem 0.75rem;
  border-radius: 8px;
  border: 1px solid rgba(107, 114, 128, 0.15);
}

.warning {
  display: inline-flex;
  align-items: center;
  font-size: 0.85rem;
  font-weight: 600;
  color: #d97706;
  background: linear-gradient(135deg, rgba(245, 158, 11, 0.1), rgba(217, 119, 6, 0.1));
  padding: 0.375rem 0.75rem;
  border-radius: 8px;
  border: 1px solid rgba(245, 158, 11, 0.2);
}

.export-btn:hover {
  background: var(--accent-hover);
}

.overview-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
  margin-bottom: 2rem;
}

.overview-card {
  background: var(--card-background);
  border-radius: 1rem;
  padding: 1.5rem;
  box-shadow: 0 1px 3px var(--shadow-light);
  display: flex;
  align-items: center;
  gap: 1rem;
  border: 1px solid var(--card-border-color);
}

.card-icon {
  width: 4rem;
  height: 4rem;
  border-radius: 1rem;
  background: linear-gradient(135deg, var(--accent-color) 0%, #764ba2 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-size: 1.5rem;
}

.card-content h3 {
  font-size: 2rem;
  font-weight: bold;
  color: var(--primary-text-color);
  margin: 0;
}

.card-content p {
  color: var(--secondary-text-color);
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
  color: var(--success-color);
}

.trend.negative {
  color: var(--error-color);
}

.info {
  color: var(--secondary-text-color);
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
  background: var(--card-background);
  border-radius: 1rem;
  padding: 1.5rem;
  box-shadow: 0 1px 3px var(--shadow-light);
  border: 1px solid var(--card-border-color);
}

.chart-container h3 {
  color: var(--primary-text-color);
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
  border: 1px solid var(--border-color);
  background: var(--card-background);
  color: var(--secondary-text-color);
  border-radius: 0.5rem;
  cursor: pointer;
  font-size: 0.875rem;
  transition: all 0.2s;
}

.period-btn.active {
  background: var(--accent-color);
  color: white;
  border-color: var(--accent-color);
}

.performance-table-section {
  background: var(--card-background);
  border-radius: 1rem;
  box-shadow: 0 1px 3px var(--shadow-light);
  border: 1px solid var(--card-border-color);
  overflow: hidden;
}

.table-header {
  padding: 1.5rem;
  border-bottom: 1px solid var(--border-color);
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.table-header h3 {
  color: var(--primary-text-color);
  margin: 0;
}

.table-controls {
  display: flex;
  gap: 1rem;
  align-items: center;
}

.search-input {
  padding: 0.5rem 1rem;
  border: 1px solid var(--border-color);
  border-radius: 0.5rem;
  background: var(--input-bg);
  color: var(--primary-text-color);
  width: 200px;
}

.sort-select {
  padding: 0.5rem 1rem;
  border: 1px solid var(--border-color);
  background: var(--input-bg);
  color: var(--primary-text-color);
  border-radius: 0.5rem;
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
  border-bottom: 1px solid var(--border-color);
}

.performance-table th {
  background: var(--bg-accent);
  font-weight: 600;
  color: var(--primary-text-color);
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
  background: linear-gradient(135deg, var(--accent-color) 0%, #764ba2 100%);
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: bold;
  font-size: 0.875rem;
}

.student-name {
  font-weight: 500;
  color: var(--primary-text-color);
}

.student-id {
  font-size: 0.75rem;
  color: var(--secondary-text-color);
}

.score-cell {
  min-width: 120px;
}

.score-value {
  font-weight: 600;
  color: var(--primary-text-color);
}

.score-bar {
  width: 100%;
  height: 4px;
  background: var(--border-color);
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
  background: var(--success-color);
}

.score-fill.good {
  background: var(--accent-color);
}

.score-fill.satisfactory {
  background: #f59e0b;
}

.score-fill.needs-improvement {
  background: var(--error-color);
}

.score-badge {
  padding: 0.25rem 0.75rem;
  border-radius: 1rem;
  font-size: 0.75rem;
  font-weight: 600;
}

.score-badge.excellent {
  background: var(--success-bg);
  color: var(--success-color);
}

.score-badge.good {
  background: var(--bg-accent);
  color: var(--accent-color);
}

.score-badge.satisfactory {
  background: #fef3c7;
  color: #92400e;
}

.score-badge.needs-improvement {
  background: var(--error-bg);
  color: var(--error-color);
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
  background: var(--success-bg);
  color: var(--success-color);
}

.improvement-badge.negative {
  background: var(--error-bg);
  color: var(--error-color);
}

.status-badge {
  padding: 0.25rem 0.75rem;
  border-radius: 1rem;
  font-size: 0.75rem;
  font-weight: 600;
}

.status-badge.excellent {
  background: var(--success-bg);
  color: var(--success-color);
}

.status-badge.good {
  background: var(--bg-accent);
  color: var(--accent-color);
}

.status-badge.satisfactory {
  background: #fef3c7;
  color: #92400e;
}

.status-badge.warning {
  background: var(--error-bg);
  color: var(--error-color);
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