<template>
  <div class="gradebook-container">
    <!-- Header -->
    <div class="gradebook-header">
      <div class="header-content">
        <h1 class="page-title">Gradebook</h1>
        <p class="page-subtitle">Review and manage quiz submissions</p>
      </div>
      <div class="header-actions">
        <div class="search-box">
          <i class="fas fa-search"></i>
          <input 
            v-model="searchQuery" 
            type="text" 
            placeholder="Search by student name or quiz title..."
          >
        </div>
        <select v-model="selectedSubject" class="filter-select">
          <option value="">All Subjects</option>
          <option v-for="subject in subjects" :key="subject.id" :value="subject.id">
            {{ subject.name }}
          </option>
        </select>
        <select v-model="selectedStatus" class="filter-select">
          <option value="">All Status</option>
          <option value="submitted">Pending Review</option>
          <option value="graded">Auto Graded</option>
          <option value="reviewed">Manually Reviewed</option>
        </select>
      </div>
    </div>

    <!-- Loading State -->
    <div v-if="loading" class="loading-container">
      <div class="spinner"></div>
      <p>Loading submissions...</p>
    </div>

    <!-- Main Content -->
    <div v-else class="gradebook-content">
      <!-- Stats Cards -->
      <div class="stats-grid">
        <div class="stat-card">
          <div class="stat-icon pending">
            <i class="fas fa-clock"></i>
          </div>
          <div class="stat-info">
            <h3>{{ stats.pendingReview }}</h3>
            <p>Pending Review</p>
          </div>
        </div>
        <div class="stat-card">
          <div class="stat-icon graded">
            <i class="fas fa-check-circle"></i>
          </div>
          <div class="stat-info">
            <h3>{{ stats.autoGraded }}</h3>
            <p>Auto Graded</p>
          </div>
        </div>
        <div class="stat-card">
          <div class="stat-icon reviewed">
            <i class="fas fa-user-check"></i>
          </div>
          <div class="stat-info">
            <h3>{{ stats.manuallyReviewed }}</h3>
            <p>Manually Reviewed</p>
          </div>
        </div>
        <div class="stat-card">
          <div class="stat-icon average">
            <i class="fas fa-chart-line"></i>
          </div>
          <div class="stat-info">
            <h3>{{ stats.averageScore }}%</h3>
            <p>Average Score</p>
          </div>
        </div>
      </div>

      <!-- Quiz Submissions Table -->
      <div class="submissions-section">
        <div class="section-header">
          <h2>Quiz Submissions</h2>
          <div class="bulk-actions">
            <button 
              v-if="selectedSubmissions.length > 0" 
              @click="bulkFinalize" 
              class="btn-bulk-action"
            >
              Finalize Selected ({{ selectedSubmissions.length }})
            </button>
          </div>
        </div>

        <div v-if="filteredSubmissions.length === 0" class="empty-state">
          <i class="fas fa-clipboard-list"></i>
          <h3>No submissions found</h3>
          <p>There are no quiz submissions matching your current filters.</p>
        </div>

        <div v-else class="submissions-table-container">
          <table class="submissions-table">
            <thead>
              <tr>
                <th class="checkbox-column">
                  <input 
                    type="checkbox" 
                    v-model="selectAll" 
                    @change="toggleSelectAll"
                  >
                </th>
                <th @click="sortBy('student_name')" class="sortable">
                  Student Name
                  <i class="fas fa-sort" :class="getSortIcon('student_name')"></i>
                </th>
                <th @click="sortBy('quiz_title')" class="sortable">
                  Quiz Title
                  <i class="fas fa-sort" :class="getSortIcon('quiz_title')"></i>
                </th>
                <th @click="sortBy('subject_name')" class="sortable">
                  Subject
                  <i class="fas fa-sort" :class="getSortIcon('subject_name')"></i>
                </th>
                <th @click="sortBy('submitted_at')" class="sortable">
                  Submitted
                  <i class="fas fa-sort" :class="getSortIcon('submitted_at')"></i>
                </th>
                <th @click="sortBy('percentage')" class="sortable">
                  Score
                  <i class="fas fa-sort" :class="getSortIcon('percentage')"></i>
                </th>
                <th>Status</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody>
              <tr 
                v-for="submission in paginatedSubmissions" 
                :key="submission.id"
                :class="{ 'selected': selectedSubmissions.includes(submission.id) }"
              >
                <td class="checkbox-column">
                  <input 
                    type="checkbox" 
                    :value="submission.id"
                    v-model="selectedSubmissions"
                  >
                </td>
                <td>
                  <div class="student-info">
                    <div class="student-avatar">
                      {{ getInitials(submission.student_name) }}
                    </div>
                    <div>
                      <div class="student-name">{{ submission.student_name }}</div>
                      <div class="student-email">{{ submission.student_email }}</div>
                    </div>
                  </div>
                </td>
                <td>
                  <div class="quiz-info">
                    <div class="quiz-title">{{ submission.quiz_title }}</div>
                    <div class="quiz-code">{{ submission.quiz_code }}</div>
                  </div>
                </td>
                <td>
                  <span class="subject-badge">{{ submission.subject_name }}</span>
                </td>
                <td>
                  <div class="date-info">
                    <div class="date">{{ formatDate(submission.submitted_at) }}</div>
                    <div class="time">{{ formatTime(submission.submitted_at) }}</div>
                  </div>
                </td>
                <td>
                  <div class="score-display">
                    <div class="score-percentage" :class="getScoreClass(submission.percentage)">
                      {{ submission.percentage }}%
                    </div>
                    <div class="score-fraction">
                      {{ submission.total_score }}/{{ submission.max_score }}
                    </div>
                  </div>
                </td>
                <td>
                  <span class="status-badge" :class="submission.status">
                    {{ getStatusText(submission.status) }}
                  </span>
                </td>
                <td>
                  <div class="action-buttons">
                    <button 
                      @click="reviewSubmission(submission)" 
                      class="btn-action review"
                      title="Review Submission"
                    >
                      <i class="fas fa-eye"></i>
                    </button>
                    <button 
                      v-if="!submission.finalized"
                      @click="finalizeSubmission(submission.id)" 
                      class="btn-action finalize"
                      title="Finalize Grade"
                    >
                      <i class="fas fa-check"></i>
                    </button>
                    <button 
                      @click="downloadSubmission(submission)" 
                      class="btn-action download"
                      title="Download Report"
                    >
                      <i class="fas fa-download"></i>
                    </button>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>

        <!-- Pagination -->
        <div v-if="totalPages > 1" class="pagination">
          <button 
            @click="currentPage--" 
            :disabled="currentPage === 1"
            class="pagination-btn"
          >
            <i class="fas fa-chevron-left"></i>
          </button>
          <span class="pagination-info">
            Page {{ currentPage }} of {{ totalPages }}
            ({{ filteredSubmissions.length }} submissions)
          </span>
          <button 
            @click="currentPage++" 
            :disabled="currentPage === totalPages"
            class="pagination-btn"
          >
            <i class="fas fa-chevron-right"></i>
          </button>
        </div>
      </div>
    </div>

    <!-- Review Modal -->
    <div v-if="showReviewModal" class="modal-overlay" @click="closeReviewModal">
      <div class="review-modal" @click.stop>
        <div class="modal-header">
          <h3>Review Submission</h3>
          <button @click="closeReviewModal" class="modal-close">
            <i class="fas fa-times"></i>
          </button>
        </div>
        <div class="modal-content">
          <SubmissionReview 
            v-if="selectedSubmission"
            :submission="selectedSubmission"
            @submission-updated="onSubmissionUpdated"
            @close="closeReviewModal"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted, computed, watch } from 'vue'
import { supabase } from '../../supabase.js'
import SubmissionReview from '../../components/teacher/SubmissionReview.vue'

export default {
  name: 'Gradebook',
  components: {
    SubmissionReview
  },
  setup() {
    
    // Reactive data
    const loading = ref(true)
    const submissions = ref([])
    const subjects = ref([])
    const searchQuery = ref('')
    const selectedSubject = ref('')
    const selectedStatus = ref('')
    const selectedSubmissions = ref([])
    const selectAll = ref(false)
    const currentPage = ref(1)
    const itemsPerPage = ref(10)
    const sortField = ref('submitted_at')
    const sortDirection = ref('desc')
    const showReviewModal = ref(false)
    const selectedSubmission = ref(null)

    // Stats
    const stats = ref({
      pendingReview: 0,
      autoGraded: 0,
      manuallyReviewed: 0,
      averageScore: 0
    })

    // Computed properties
    const filteredSubmissions = computed(() => {
      let filtered = submissions.value

      // Filter by search query
      if (searchQuery.value) {
        const query = searchQuery.value.toLowerCase()
        filtered = filtered.filter(submission => 
          submission.student_name.toLowerCase().includes(query) ||
          submission.quiz_title.toLowerCase().includes(query) ||
          submission.student_email.toLowerCase().includes(query)
        )
      }

      // Filter by subject
      if (selectedSubject.value) {
        filtered = filtered.filter(submission => 
          submission.subject_id === selectedSubject.value
        )
      }

      // Filter by status
      if (selectedStatus.value) {
        filtered = filtered.filter(submission => 
          submission.status === selectedStatus.value
        )
      }

      // Sort
      filtered.sort((a, b) => {
        let aValue = a[sortField.value]
        let bValue = b[sortField.value]

        if (sortField.value === 'submitted_at') {
          aValue = new Date(aValue)
          bValue = new Date(bValue)
        }

        if (aValue < bValue) {
          return sortDirection.value === 'asc' ? -1 : 1
        }
        if (aValue > bValue) {
          return sortDirection.value === 'asc' ? 1 : -1
        }
        return 0
      })

      return filtered
    })

    const paginatedSubmissions = computed(() => {
      const start = (currentPage.value - 1) * itemsPerPage.value
      const end = start + itemsPerPage.value
      return filteredSubmissions.value.slice(start, end)
    })

    const totalPages = computed(() => {
      return Math.ceil(filteredSubmissions.value.length / itemsPerPage.value)
    })

    // Methods
    const fetchSubmissions = async () => {
      try {
        loading.value = true

        // Get current user's teacher ID
        const { data: { session } } = await supabase.auth.getSession()
        if (!session) return

        const { data: profile } = await supabase
          .from('profiles')
          .select('id')
          .eq('auth_user_id', session.user.id)
          .single()

        if (!profile) return

        const { data: teacher } = await supabase
          .from('teachers')
          .select('id')
          .eq('profile_id', profile.id)
          .single()

        if (!teacher) return

        const { data, error } = await supabase
          .from('quiz_attempts')
          .select(`
            id,
            quiz_id,
            student_id,
            total_score,
            max_score,
            percentage,
            status,
            submitted_at,
            time_taken_minutes,
            teacher_feedback,
            students!inner (
              full_name,
              email
            ),
            quizzes!inner (
              title,
              quiz_code,
              subject_id,
              teacher_id,
              subjects!inner (
                name
              )
            ),
            quiz_results (
              finalized,
              visible_to_student
            )
          `)
          .eq('quizzes.teacher_id', teacher.id)
          .in('status', ['submitted', 'graded', 'reviewed'])
          .order('submitted_at', { ascending: false })

        if (error) throw error

        submissions.value = data.map(submission => ({
          id: submission.id,
          quiz_id: submission.quiz_id,
          student_id: submission.student_id,
          student_name: submission.students.full_name,
          student_email: submission.students.email,
          quiz_title: submission.quizzes.title,
          quiz_code: submission.quizzes.quiz_code,
          subject_id: submission.quizzes.subject_id,
          subject_name: submission.quizzes.subjects.name,
          total_score: submission.total_score,
          max_score: submission.max_score,
          percentage: Math.round(submission.percentage),
          status: submission.status,
          submitted_at: submission.submitted_at,
          time_taken_minutes: submission.time_taken_minutes,
          teacher_feedback: submission.teacher_feedback,
          finalized: submission.quiz_results?.[0]?.finalized || false,
          visible_to_student: submission.quiz_results?.[0]?.visible_to_student || false
        }))

        calculateStats()
      } catch (error) {
        console.error('Error fetching submissions:', error)
      } finally {
        loading.value = false
      }
    }

    const fetchSubjects = async () => {
      try {
        const { data, error } = await supabase
          .from('subjects')
          .select('id, name')
          .eq('is_active', true)

        if (error) throw error
        subjects.value = data
      } catch (error) {
        console.error('Error fetching subjects:', error)
      }
    }

    const calculateStats = () => {
      const pending = submissions.value.filter(s => s.status === 'submitted').length
      const graded = submissions.value.filter(s => s.status === 'graded').length
      const reviewed = submissions.value.filter(s => s.status === 'reviewed').length
      const total = submissions.value.length
      const averageScore = total > 0 
        ? Math.round(submissions.value.reduce((sum, s) => sum + s.percentage, 0) / total)
        : 0

      stats.value = {
        pendingReview: pending,
        autoGraded: graded,
        manuallyReviewed: reviewed,
        averageScore
      }
    }

    const sortBy = (field) => {
      if (sortField.value === field) {
        sortDirection.value = sortDirection.value === 'asc' ? 'desc' : 'asc'
      } else {
        sortField.value = field
        sortDirection.value = 'asc'
      }
    }

    const getSortIcon = (field) => {
      if (sortField.value !== field) return ''
      return sortDirection.value === 'asc' ? 'fa-sort-up' : 'fa-sort-down'
    }

    const toggleSelectAll = () => {
      if (selectAll.value) {
        selectedSubmissions.value = paginatedSubmissions.value.map(s => s.id)
      } else {
        selectedSubmissions.value = []
      }
    }

    const reviewSubmission = (submission) => {
      selectedSubmission.value = submission
      showReviewModal.value = true
    }

    const closeReviewModal = () => {
      showReviewModal.value = false
      selectedSubmission.value = null
    }

    const finalizeSubmission = async (submissionId) => {
      try {
        const submission = submissions.value.find(s => s.id === submissionId)
        
        const { error } = await supabase.rpc('finalize_quiz_results', {
          p_quiz_id: submission.quiz_id
        })

        if (error) throw error

        // Update local state
        const index = submissions.value.findIndex(s => s.id === submissionId)
        if (index !== -1) {
          submissions.value[index].finalized = true
          submissions.value[index].visible_to_student = true
        }

        alert('Grade finalized successfully!')
      } catch (error) {
        console.error('Error finalizing submission:', error)
        alert('Error finalizing grade. Please try again.')
      }
    }

    const bulkFinalize = async () => {
      if (!confirm(`Finalize ${selectedSubmissions.value.length} submissions?`)) {
        return
      }

      try {
        const uniqueQuizIds = [...new Set(
          submissions.value
            .filter(s => selectedSubmissions.value.includes(s.id))
            .map(s => s.quiz_id)
        )]

        for (const quizId of uniqueQuizIds) {
          await supabase.rpc('finalize_quiz_results', {
            p_quiz_id: quizId
          })
        }

        // Update local state
        submissions.value.forEach(submission => {
          if (selectedSubmissions.value.includes(submission.id)) {
            submission.finalized = true
            submission.visible_to_student = true
          }
        })

        selectedSubmissions.value = []
        selectAll.value = false
        alert('Grades finalized successfully!')
      } catch (error) {
        console.error('Error bulk finalizing:', error)
        alert('Error finalizing grades. Please try again.')
      }
    }

    const onSubmissionUpdated = (updatedSubmission) => {
      const index = submissions.value.findIndex(s => s.id === updatedSubmission.id)
      if (index !== -1) {
        submissions.value[index] = { ...submissions.value[index], ...updatedSubmission }
      }
      calculateStats()
    }

    const downloadSubmission = (submission) => {
      // TODO: Implement submission report download
      console.log('Download submission:', submission)
    }

    // Utility functions
    const getInitials = (name) => {
      return name.split(' ').map(n => n[0]).join('').toUpperCase()
    }

    const formatDate = (dateString) => {
      return new Date(dateString).toLocaleDateString()
    }

    const formatTime = (dateString) => {
      return new Date(dateString).toLocaleTimeString([], { 
        hour: '2-digit', 
        minute: '2-digit' 
      })
    }

    const getStatusText = (status) => {
      const statusMap = {
        submitted: 'Pending',
        graded: 'Auto Graded',
        reviewed: 'Reviewed'
      }
      return statusMap[status] || status
    }

    const getScoreClass = (percentage) => {
      if (percentage >= 90) return 'excellent'
      if (percentage >= 80) return 'good'
      if (percentage >= 70) return 'average'
      return 'needs-improvement'
    }

    // Watchers
    watch([searchQuery, selectedSubject, selectedStatus], () => {
      currentPage.value = 1
      selectedSubmissions.value = []
      selectAll.value = false
    })

    // Lifecycle
    onMounted(() => {
      fetchSubmissions()
      fetchSubjects()
    })

    return {
      loading,
      submissions,
      subjects,
      searchQuery,
      selectedSubject,
      selectedStatus,
      selectedSubmissions,
      selectAll,
      currentPage,
      totalPages,
      filteredSubmissions,
      paginatedSubmissions,
      stats,
      showReviewModal,
      selectedSubmission,
      sortBy,
      getSortIcon,
      toggleSelectAll,
      reviewSubmission,
      closeReviewModal,
      finalizeSubmission,
      bulkFinalize,
      onSubmissionUpdated,
      downloadSubmission,
      getInitials,
      formatDate,
      formatTime,
      getStatusText,
      getScoreClass
    }
  }
}
</script>

<style scoped>
.gradebook-container {
  padding: 2rem;
  max-width: 1400px;
  margin: 0 auto;
  min-height: 100vh;
  background: #f8fafc;
}

.gradebook-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 2rem;
  flex-wrap: wrap;
  gap: 1rem;
}

.header-content {
  flex: 1;
}

.page-title {
  font-size: 2.5rem;
  font-weight: 700;
  color: #1a202c;
  margin: 0 0 0.5rem 0;
}

.page-subtitle {
  color: #64748b;
  font-size: 1.1rem;
  margin: 0;
}

.header-actions {
  display: flex;
  gap: 1rem;
  align-items: center;
  flex-wrap: wrap;
}

.search-box {
  position: relative;
  min-width: 300px;
}

.search-box i {
  position: absolute;
  left: 1rem;
  top: 50%;
  transform: translateY(-50%);
  color: #64748b;
}

.search-box input {
  width: 100%;
  padding: 0.75rem 1rem 0.75rem 2.5rem;
  border: 1px solid #e2e8f0;
  border-radius: 0.5rem;
  font-size: 0.95rem;
  background: white;
}

.filter-select {
  padding: 0.75rem 1rem;
  border: 1px solid #e2e8f0;
  border-radius: 0.5rem;
  background: white;
  font-size: 0.95rem;
  min-width: 140px;
}

.loading-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 400px;
  color: #64748b;
}

.spinner {
  width: 40px;
  height: 40px;
  border: 4px solid #e2e8f0;
  border-top: 4px solid #3b82f6;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin-bottom: 1rem;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1rem;
  margin-bottom: 2rem;
}

.stat-card {
  background: white;
  padding: 1.5rem;
  border-radius: 0.75rem;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  display: flex;
  align-items: center;
  gap: 1rem;
}

.stat-icon {
  width: 60px;
  height: 60px;
  border-radius: 0.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.5rem;
  color: white;
}

.stat-icon.pending {
  background: #f59e0b;
}

.stat-icon.graded {
  background: #10b981;
}

.stat-icon.reviewed {
  background: #3b82f6;
}

.stat-icon.average {
  background: #8b5cf6;
}

.stat-info h3 {
  font-size: 1.75rem;
  font-weight: 700;
  color: #1a202c;
  margin: 0 0 0.25rem 0;
}

.stat-info p {
  color: #64748b;
  margin: 0;
  font-size: 0.9rem;
}

.submissions-section {
  background: white;
  border-radius: 0.75rem;
  overflow: hidden;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.section-header {
  padding: 1.5rem;
  border-bottom: 1px solid #e2e8f0;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.section-header h2 {
  font-size: 1.5rem;
  font-weight: 600;
  color: #1a202c;
  margin: 0;
}

.btn-bulk-action {
  background: #3b82f6;
  color: white;
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 0.5rem;
  font-weight: 500;
  cursor: pointer;
  transition: background 0.2s;
}

.btn-bulk-action:hover {
  background: #2563eb;
}

.empty-state {
  padding: 4rem 2rem;
  text-align: center;
  color: #64748b;
}

.empty-state i {
  font-size: 4rem;
  margin-bottom: 1rem;
  color: #cbd5e1;
}

.empty-state h3 {
  font-size: 1.25rem;
  margin-bottom: 0.5rem;
  color: #374151;
}

.submissions-table-container {
  overflow-x: auto;
}

.submissions-table {
  width: 100%;
  border-collapse: collapse;
}

.submissions-table th,
.submissions-table td {
  padding: 1rem;
  text-align: left;
  border-bottom: 1px solid #e2e8f0;
}

.submissions-table th {
  background: #f8fafc;
  font-weight: 600;
  color: #374151;
  font-size: 0.875rem;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.submissions-table th.sortable {
  cursor: pointer;
  user-select: none;
}

.submissions-table th.sortable:hover {
  background: #f1f5f9;
}

.submissions-table th i {
  margin-left: 0.5rem;
  opacity: 0.5;
}

.checkbox-column {
  width: 50px;
}

.student-info {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.student-avatar {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: #3b82f6;
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 600;
  font-size: 0.875rem;
}

.student-name {
  font-weight: 500;
  color: #1a202c;
}

.student-email {
  font-size: 0.875rem;
  color: #64748b;
}

.quiz-info {
  max-width: 200px;
}

.quiz-title {
  font-weight: 500;
  color: #1a202c;
  margin-bottom: 0.25rem;
}

.quiz-code {
  font-size: 0.75rem;
  color: #64748b;
  font-family: 'Courier New', monospace;
  background: #f1f5f9;
  padding: 0.125rem 0.5rem;
  border-radius: 0.25rem;
  display: inline-block;
}

.subject-badge {
  background: #e0f2fe;
  color: #0369a1;
  padding: 0.25rem 0.75rem;
  border-radius: 1rem;
  font-size: 0.875rem;
  font-weight: 500;
}

.date-info {
  font-size: 0.875rem;
}

.date {
  color: #1a202c;
  font-weight: 500;
}

.time {
  color: #64748b;
}

.score-display {
  text-align: center;
}

.score-percentage {
  font-weight: 700;
  font-size: 1.125rem;
  margin-bottom: 0.25rem;
}

.score-percentage.excellent {
  color: #059669;
}

.score-percentage.good {
  color: #0369a1;
}

.score-percentage.average {
  color: #d97706;
}

.score-percentage.needs-improvement {
  color: #dc2626;
}

.score-fraction {
  font-size: 0.75rem;
  color: #64748b;
}

.status-badge {
  padding: 0.25rem 0.75rem;
  border-radius: 1rem;
  font-size: 0.75rem;
  font-weight: 500;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.status-badge.submitted {
  background: #fef3c7;
  color: #92400e;
}

.status-badge.graded {
  background: #d1fae5;
  color: #065f46;
}

.status-badge.reviewed {
  background: #dbeafe;
  color: #1e40af;
}

.action-buttons {
  display: flex;
  gap: 0.5rem;
}

.btn-action {
  width: 32px;
  height: 32px;
  border: none;
  border-radius: 0.25rem;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.2s;
}

.btn-action.review {
  background: #f3f4f6;
  color: #374151;
}

.btn-action.review:hover {
  background: #e5e7eb;
}

.btn-action.finalize {
  background: #dcfce7;
  color: #16a34a;
}

.btn-action.finalize:hover {
  background: #bbf7d0;
}

.btn-action.download {
  background: #fef3c7;
  color: #d97706;
}

.btn-action.download:hover {
  background: #fde68a;
}

.pagination {
  padding: 1.5rem;
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 1rem;
  border-top: 1px solid #e2e8f0;
}

.pagination-btn {
  width: 40px;
  height: 40px;
  border: 1px solid #e2e8f0;
  background: white;
  border-radius: 0.5rem;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.2s;
}

.pagination-btn:hover:not(:disabled) {
  background: #f8fafc;
  border-color: #cbd5e1;
}

.pagination-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.pagination-info {
  color: #64748b;
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
  padding: 1rem;
}

.review-modal {
  background: white;
  border-radius: 0.75rem;
  width: 100%;
  max-width: 900px;
  max-height: 90vh;
  overflow: hidden;
  display: flex;
  flex-direction: column;
}

.modal-header {
  padding: 1.5rem;
  border-bottom: 1px solid #e2e8f0;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.modal-header h3 {
  font-size: 1.25rem;
  font-weight: 600;
  color: #1a202c;
  margin: 0;
}

.modal-close {
  width: 40px;
  height: 40px;
  border: none;
  background: none;
  cursor: pointer;
  border-radius: 0.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #64748b;
  transition: all 0.2s;
}

.modal-close:hover {
  background: #f1f5f9;
  color: #374151;
}

.modal-content {
  flex: 1;
  overflow-y: auto;
}

.submissions-table tr.selected {
  background: #eff6ff;
}

@media (max-width: 768px) {
  .gradebook-container {
    padding: 1rem;
  }

  .gradebook-header {
    flex-direction: column;
    align-items: stretch;
  }

  .header-actions {
    flex-direction: column;
  }

  .search-box {
    min-width: auto;
  }

  .stats-grid {
    grid-template-columns: 1fr;
  }

  .submissions-table {
    font-size: 0.875rem;
  }

  .submissions-table th,
  .submissions-table td {
    padding: 0.75rem 0.5rem;
  }

  .student-info {
    flex-direction: column;
    align-items: flex-start;
    gap: 0.5rem;
  }

  .action-buttons {
    flex-direction: column;
  }
}
</style>