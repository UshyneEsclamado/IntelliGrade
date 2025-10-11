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
              {{ section.name }} - {{ section.subject }}
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

    <!-- Stats Cards -->
    <div class="stats-grid">
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
          <div class="stat-number">{{ overallStats.totalAssessments }}</div>
          <div class="stat-label">Assessments Given</div>
        </div>
      </div>

    </div>

    <!-- Content Grid -->
    <div class="content-grid">
      <!-- Performance Charts -->
      <div class="content-card">
        <div class="card-header">
          <h3>Performance Trends</h3>
          <p class="card-desc">Track student performance over time</p>
        </div>
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
        <div class="chart-placeholder">
          <canvas ref="performanceChart"></canvas>
        </div>
      </div>

      <!-- Score Distribution -->
      <div class="content-card">
        <div class="card-header">
          <h3>Score Distribution</h3>
          <p class="card-desc">Distribution of student scores</p>
        </div>
        <div class="chart-placeholder">
          <canvas ref="distributionChart"></canvas>
        </div>
      </div>
    </div>

    <!-- Student Performance Table -->
    <div class="content-card">
      <div class="card-header">
        <h3>Individual Student Performance</h3>
        <p class="card-desc">Detailed performance data for each student</p>
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
              <th>Assessments</th>
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
              <td>{{ student.average_score }}%</td>
              <td>
                <span :class="['score-badge', getScoreClass(student.latest_score)]">
                  {{ student.latest_score }}%
                </span>
              </td>
              <td>
                <span :class="['improvement-badge', student.improvement >= 0 ? 'positive' : 'negative']">
                  {{ student.improvement >= 0 ? '+' : '' }}{{ student.improvement }}%
                </span>
              </td>
              <td>
                <span :class="['status-badge', getStatusClass(student.average_score)]">
                  {{ getStatusText(student.average_score) }}
                </span>
              </td>
              <td class="actions-cell">
                <button @click="viewStudentDetails(student)" class="action-btn view-btn">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M12,9A3,3 0 0,0 9,12A3,3 0 0,0 12,15A3,3 0 0,0 15,12A3,3 0 0,0 12,9M12,17A5,5 0 0,1 7,12A5,5 0 0,1 12,7A5,5 0 0,1 17,12A5,5 0 0,1 12,17M12,4.5C7,4.5 2.73,7.61 1,12C2.73,16.39 7,19.5 12,19.5C17,19.5 21.27,16.39 23,12C21.27,7.61 17,4.5 12,4.5Z" />
                  </svg>
                </button>
                <button @click="updateScore(student)" class="action-btn edit-btn">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M20.71,7.04C21.1,6.65 21.1,6 20.71,5.63L18.37,3.29C18,2.9 17.35,2.9 16.96,3.29L15.12,5.12L18.87,8.87M3,17.25V21H6.75L17.81,9.93L14.06,6.18L3,17.25Z" />
                  </svg>
                </button>
                <button 
                  v-if="student.average_score < 75" 
                  @click="flagForRemediation(student)" 
                  class="action-btn warning-btn"
                >
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M14.4,6L14,4H5V21H7V14H12.6L13,16H20V6H14.4Z" />
                  </svg>
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- Simple Pagination -->
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
  border-radius: 16px;
  padding: 1.5rem;
  margin-bottom: 1.5rem;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
}
.dark .header-card {
  background: #23272b;
  border: 1px solid #20c997;
  box-shadow: 0 2px 8px rgba(0,0,0,0.25);
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
</style>