<template>
  <div class="gradebook-container">
    <!-- Header -->
    <div class="gradebook-header">
      <div class="header-content">
        <h1 class="page-title">Gradebook</h1>
        <p class="page-subtitle">Review and grade quiz submissions</p>
      </div>
      <div class="header-actions">
        <div class="search-box">
          <i class="fas fa-search"></i>
          <input 
            v-model="searchQuery" 
            type="text" 
            placeholder="Search..."
          >
        </div>
        <button @click="refreshData" class="refresh-btn" :disabled="loading">
          <i class="fas fa-sync-alt" :class="{ 'spinning': loading }"></i>
        </button>
      </div>
    </div>

    <!-- Breadcrumb Navigation -->
    <div class="breadcrumb" v-if="selectedSubject || selectedSection">
      <button @click="resetToSubjects" class="breadcrumb-item">
        <i class="fas fa-book"></i> Subjects
      </button>
      <span v-if="selectedSubject" class="breadcrumb-separator">/</span>
      <button v-if="selectedSubject" @click="resetToSections" class="breadcrumb-item">
        {{ selectedSubject.name }}
      </button>
      <span v-if="selectedSection" class="breadcrumb-separator">/</span>
      <span v-if="selectedSection" class="breadcrumb-item active">
        {{ selectedSection.name }}
      </span>
    </div>

    <!-- Loading State -->
    <div v-if="loading" class="loading-container">
      <div class="spinner"></div>
      <p>Loading...</p>
    </div>

    <!-- Error State -->
    <div v-else-if="error" class="error-container">
      <i class="fas fa-exclamation-triangle"></i>
      <h3>Error Loading Data</h3>
      <p>{{ error }}</p>
      <button @click="refreshData" class="btn-retry">Retry</button>
    </div>

    <!-- Main Content -->
    <div v-else class="gradebook-content">
      <!-- LEVEL 1: Subject Selection -->
      <div v-if="!selectedSubject" class="subjects-grid">
        <div 
          v-for="subject in filteredSubjects" 
          :key="subject.id"
          class="subject-card"
          @click="selectSubject(subject)"
        >
          <div class="subject-icon">
            <i class="fas fa-book"></i>
          </div>
          <div class="subject-info">
            <h3>{{ subject.name }}</h3>
            <p>Grade {{ subject.grade_level }}</p>
            <div class="subject-stats">
              <span class="stat-badge">
                <i class="fas fa-users"></i>
                {{ subject.section_count }} Sections
              </span>
              <span class="stat-badge pending">
                <i class="fas fa-clock"></i>
                {{ subject.pending_count }} Pending
              </span>
            </div>
          </div>
          <div class="card-arrow">
            <i class="fas fa-chevron-right"></i>
          </div>
        </div>

        <div v-if="filteredSubjects.length === 0" class="empty-state">
          <i class="fas fa-book"></i>
          <h3>No subjects found</h3>
          <p>You don't have any subjects assigned yet.</p>
        </div>
      </div>

      <!-- LEVEL 2: Section Selection -->
      <div v-else-if="selectedSubject && !selectedSection" class="sections-grid">
        <div 
          v-for="section in filteredSections" 
          :key="section.id"
          class="section-card"
          @click="selectSection(section)"
        >
          <div class="section-icon">
            <i class="fas fa-users"></i>
          </div>
          <div class="section-info">
            <h3>{{ section.name }}</h3>
            <p>{{ section.section_code }}</p>
            <div class="section-stats">
              <span class="stat-badge">
                <i class="fas fa-clipboard-list"></i>
                {{ section.quiz_count }} Quizzes
              </span>
              <span class="stat-badge pending">
                <i class="fas fa-clock"></i>
                {{ section.pending_count }} Pending
              </span>
            </div>
          </div>
          <div class="card-arrow">
            <i class="fas fa-chevron-right"></i>
          </div>
        </div>

        <div v-if="filteredSections.length === 0" class="empty-state">
          <i class="fas fa-users"></i>
          <h3>No sections found</h3>
          <p>No sections available for this subject.</p>
        </div>
      </div>

      <!-- LEVEL 3: Submissions Table -->
      <div v-else-if="selectedSection" class="submissions-view">
        <!-- Stats Cards -->
        <div class="stats-grid">
          <div class="stat-card">
            <div class="stat-icon pending">
              <i class="fas fa-clock"></i>
            </div>
            <div class="stat-info">
              <h3>{{ sectionStats.pendingReview }}</h3>
              <p>Pending Review</p>
            </div>
          </div>
          <div class="stat-card">
            <div class="stat-icon graded">
              <i class="fas fa-check-circle"></i>
            </div>
            <div class="stat-info">
              <h3>{{ sectionStats.graded }}</h3>
              <p>Graded</p>
            </div>
          </div>
          <div class="stat-card">
            <div class="stat-icon total">
              <i class="fas fa-clipboard-list"></i>
            </div>
            <div class="stat-info">
              <h3>{{ sectionStats.total }}</h3>
              <p>Total Submissions</p>
            </div>
          </div>
          <div class="stat-card">
            <div class="stat-icon average">
              <i class="fas fa-chart-line"></i>
            </div>
            <div class="stat-info">
              <h3>{{ sectionStats.averageScore }}%</h3>
              <p>Average Score</p>
            </div>
          </div>
        </div>

        <!-- Filters -->
        <div class="submissions-filters">
          <select v-model="selectedStatus" class="filter-select">
            <option value="">All Status</option>
            <option value="submitted">Pending Review</option>
            <option value="graded">Graded</option>
          </select>
        </div>

        <!-- Submissions Table -->
        <div class="submissions-section">
          <div v-if="filteredSubmissions.length === 0" class="empty-state">
            <i class="fas fa-clipboard-list"></i>
            <h3>No submissions found</h3>
            <p>There are no quiz submissions for this section yet.</p>
          </div>

          <div v-else class="submissions-table-container">
            <table class="submissions-table">
              <thead>
                <tr>
                  <th @click="sortBy('student_name')" class="sortable">
                    Student Name
                    <i class="fas fa-sort" :class="getSortIcon('student_name')"></i>
                  </th>
                  <th @click="sortBy('quiz_title')" class="sortable">
                    Quiz
                    <i class="fas fa-sort" :class="getSortIcon('quiz_title')"></i>
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
                >
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
                        title="Review & Grade"
                      >
                        <i class="fas fa-edit"></i>
                      </button>
                      <button 
                        @click="viewSubmission(submission)" 
                        class="btn-action view"
                        title="View Details"
                      >
                        <i class="fas fa-eye"></i>
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
    </div>

    <!-- Review/Grade Modal -->
    <div v-if="showReviewModal" class="modal-overlay" @click="closeReviewModal">
      <div class="review-modal" @click.stop>
        <div class="modal-header">
          <div>
            <h3>{{ modalMode === 'view' ? 'View Submission' : 'Grade Submission' }}</h3>
            <p class="modal-subtitle" v-if="selectedSubmission">
              {{ selectedSubmission.student_name }} - {{ selectedSubmission.quiz_title }}
            </p>
          </div>
          <button @click="closeReviewModal" class="modal-close">
            <i class="fas fa-times"></i>
          </button>
        </div>

        <div class="modal-content">
          <div v-if="loadingQuestions" class="loading-questions">
            <div class="spinner-small"></div>
            <p>Loading questions...</p>
          </div>

          <div v-else-if="reviewQuestions.length === 0" class="no-questions">
            <p>No questions found for this quiz.</p>
          </div>

          <div v-else class="submission-review">
            <div class="review-summary">
              <div class="summary-stat">
                <span class="stat-label">Score</span>
                <span class="stat-value">{{ calculateReviewScore() }}/{{ maxReviewScore }}</span>
              </div>
              <div class="summary-stat">
                <span class="stat-label">Percentage</span>
                <span class="stat-value">{{ calculateReviewPercentage() }}%</span>
              </div>
              <div class="summary-stat">
                <span class="stat-label">Correct</span>
                <span class="stat-value">{{ correctAnswerCount }}/{{ reviewQuestions.length }}</span>
              </div>
            </div>

            <div class="questions-review">
              <div v-for="(question, index) in reviewQuestions" :key="question.id" class="question-review-item">
                <div class="question-header">
                  <div class="question-number">Q{{ index + 1 }}</div>
                  <div class="question-result" :class="question.is_correct ? 'correct' : 'incorrect'">
                    {{ question.is_correct ? '✓ Correct' : '✗ Incorrect' }}
                  </div>
                  <div class="question-points" v-if="modalMode === 'grade'">
                    <input 
                      v-model.number="question.manualPoints"
                      type="number"
                      :max="question.points"
                      min="0"
                      step="0.5"
                      class="points-input"
                      @input="updateQuestionPoints(question)"
                    /> / {{ question.points }} pts
                  </div>
                  <div class="question-points" v-else>
                    {{ question.points_earned }} / {{ question.points }} pts
                  </div>
                </div>

                <div class="question-text">{{ question.question_text }}</div>

                <!-- Multiple Choice -->
                <div v-if="question.question_type === 'multiple_choice'" class="answer-section">
                  <div class="answer-key-label">
                    <strong>Answer Key:</strong> {{ getCorrectOptionLabel(question) }}
                  </div>
                  <div class="options-grid">
                    <div 
                      v-for="option in question.options" 
                      :key="option.id" 
                      class="option-item"
                      :class="{
                        'selected': question.selected_option_id === option.id,
                        'correct': option.is_correct,
                        'incorrect': question.selected_option_id === option.id && !option.is_correct
                      }"
                    >
                      <div class="option-letter">{{ String.fromCharCode(65 + option.option_number - 1) }}</div>
                      <div class="option-content">
                        <div class="option-text">{{ option.option_text }}</div>
                        <div v-if="option.is_correct" class="correct-tag">✓ Correct Answer</div>
                        <div v-if="question.selected_option_id === option.id" class="selected-tag">Student's Answer</div>
                      </div>
                    </div>
                  </div>
                </div>

                <!-- True/False -->
                <div v-else-if="question.question_type === 'true_false'" class="answer-section">
                  <div class="answer-key-label">
                    <strong>Answer Key:</strong> {{ question.correct_answer }}
                  </div>
                  <div class="true-false-options">
                    <div class="tf-option" :class="{ 
                      'student-selected': question.answer_text === 'true', 
                      'correct-answer': question.correct_answer === 'true',
                      'wrong-answer': question.answer_text === 'true' && question.correct_answer !== 'true'
                    }">
                      <strong>True</strong>
                      <span v-if="question.correct_answer === 'true'" class="correct-tag">✓ Correct</span>
                      <span v-if="question.answer_text === 'true'" class="selected-tag">Student's Answer</span>
                    </div>
                    <div class="tf-option" :class="{ 
                      'student-selected': question.answer_text === 'false', 
                      'correct-answer': question.correct_answer === 'false',
                      'wrong-answer': question.answer_text === 'false' && question.correct_answer !== 'false'
                    }">
                      <strong>False</strong>
                      <span v-if="question.correct_answer === 'false'" class="correct-tag">✓ Correct</span>
                      <span v-if="question.answer_text === 'false'" class="selected-tag">Student's Answer</span>
                    </div>
                  </div>
                </div>

                <!-- Fill in the Blank -->
                <div v-else-if="question.question_type === 'fill_blank'" class="answer-section">
                  <div class="fill-blank-answers">
                    <div class="answer-key-box">
                      <div class="answer-label">Answer Key:</div>
                      <div class="answer-text correct">
                        {{ question.correct_answer }}
                      </div>
                    </div>
                    <div class="student-answer-box">
                      <div class="answer-label">Student's Answer:</div>
                      <div class="answer-text" :class="question.is_correct ? 'correct' : 'incorrect'">
                        {{ question.answer_text || 'No answer' }}
                      </div>
                    </div>
                  </div>
                </div>

                <!-- Teacher Comment -->
                <div class="teacher-comment-section" v-if="modalMode === 'grade'">
                  <textarea 
                    v-model="question.teacherComment"
                    class="comment-input"
                    placeholder="Add feedback for this question..."
                    rows="2"
                  ></textarea>
                </div>
                <div class="teacher-comment-section" v-else-if="question.teacher_comment">
                  <div class="comment-display">
                    <strong>Teacher's Feedback:</strong>
                    <p>{{ question.teacher_comment }}</p>
                  </div>
                </div>
              </div>
            </div>

            <!-- Overall Feedback -->
            <div class="overall-feedback-section" v-if="modalMode === 'grade'">
              <h4>Overall Feedback</h4>
              <textarea 
                v-model="reviewFeedback" 
                class="feedback-textarea"
                placeholder="Add overall feedback for the student..."
                rows="3"
              ></textarea>
            </div>
            <div class="overall-feedback-section" v-else-if="selectedSubmission?.teacher_feedback">
              <h4>Overall Feedback</h4>
              <div class="feedback-display">
                <p>{{ selectedSubmission.teacher_feedback }}</p>
              </div>
            </div>
          </div>
        </div>

        <div class="modal-actions">
          <button @click="closeReviewModal" class="btn-modal cancel">Close</button>
          <button v-if="modalMode === 'grade'" @click="saveGrade" class="btn-modal primary" :disabled="savingGrade">
            {{ savingGrade ? 'Saving...' : 'Save Grade' }}
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, computed, watch, onMounted } from 'vue'
import { supabase } from '@/supabase.js'

export default {
  name: 'Gradebook',
  setup() {
    const loading = ref(true)
    const loadingQuestions = ref(false)
    const savingGrade = ref(false)
    const error = ref(null)
    const searchQuery = ref('')
    const teacherId = ref(null)

    // Hierarchy state
    const subjects = ref([])
    const selectedSubject = ref(null)
    const sections = ref([])
    const selectedSection = ref(null)
    const submissions = ref([])

    // Table state
    const selectedStatus = ref('')
    const currentPage = ref(1)
    const itemsPerPage = ref(10)
    const sortField = ref('submitted_at')
    const sortDirection = ref('desc')

    // Review modal state
    const showReviewModal = ref(false)
    const selectedSubmission = ref(null)
    const reviewQuestions = ref([])
    const reviewFeedback = ref('')
    const modalMode = ref('view')

    const sectionStats = computed(() => {
      const pending = submissions.value.filter(s => s.status === 'submitted').length
      const graded = submissions.value.filter(s => s.status === 'graded').length
      const total = submissions.value.length
      const averageScore = total > 0 
        ? Math.round(submissions.value.reduce((sum, s) => sum + (s.percentage || 0), 0) / total)
        : 0
      return { pendingReview: pending, graded, total, averageScore }
    })

    const correctAnswerCount = computed(() => {
      return reviewQuestions.value.filter(q => q.is_correct).length
    })

    const maxReviewScore = computed(() => {
      return reviewQuestions.value.reduce((sum, q) => sum + (q.points || 1), 0)
    })

    const filteredSubjects = computed(() => {
      if (!searchQuery.value) return subjects.value
      const query = searchQuery.value.toLowerCase()
      return subjects.value.filter(s => 
        s.name.toLowerCase().includes(query) || 
        s.grade_level.toString().includes(query)
      )
    })

    const filteredSections = computed(() => {
      if (!searchQuery.value) return sections.value
      const query = searchQuery.value.toLowerCase()
      return sections.value.filter(s => 
        s.name.toLowerCase().includes(query) || 
        s.section_code.toLowerCase().includes(query)
      )
    })

    const filteredSubmissions = computed(() => {
      let filtered = submissions.value

      if (searchQuery.value) {
        const query = searchQuery.value.toLowerCase()
        filtered = filtered.filter(submission => 
          submission.student_name.toLowerCase().includes(query) ||
          submission.quiz_title.toLowerCase().includes(query) ||
          submission.student_email.toLowerCase().includes(query)
        )
      }

      if (selectedStatus.value) {
        filtered = filtered.filter(submission => 
          submission.status === selectedStatus.value
        )
      }

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

    const getTeacherInfo = async () => {
      try {
        const { data: { session }, error: sessionError } = await supabase.auth.getSession()
        if (sessionError || !session) {
          error.value = 'Authentication error'
          return false
        }

        const { data: profile, error: profileError } = await supabase
          .from('profiles')
          .select('id, role')
          .eq('auth_user_id', session.user.id)
          .single()

        if (profileError || !profile || profile.role !== 'teacher') {
          error.value = 'Access denied - Teacher role required'
          return false
        }

        const { data: teacher, error: teacherError } = await supabase
          .from('teachers')
          .select('id')
          .eq('profile_id', profile.id)
          .single()

        if (teacherError || !teacher) {
          error.value = 'Teacher record not found'
          return false
        }

        teacherId.value = teacher.id
        return true
      } catch (err) {
        console.error('Error in getTeacherInfo:', err)
        error.value = 'An error occurred'
        return false
      }
    }

    const fetchSubjects = async () => {
      try {
        loading.value = true
        error.value = null

        // Optimized: Get subjects with aggregated stats in a single query
        const { data: subjectsData, error: subjectsError } = await supabase
          .from('subjects')
          .select(`
            id,
            name,
            grade_level,
            description,
            sections (id),
            quizzes (id)
          `)
          .eq('teacher_id', teacherId.value)
          .eq('is_active', true)

        if (subjectsError) throw subjectsError

        // Process subjects with pending count
        const subjectsWithStats = await Promise.all(
          (subjectsData || []).map(async (subject) => {
            const sectionCount = subject.sections?.length || 0
            const quizIds = subject.quizzes?.map(q => q.id) || []
            
            let pendingCount = 0
            if (quizIds.length > 0) {
              const { count } = await supabase
                .from('quiz_attempts')
                .select('id', { count: 'exact', head: true })
                .in('quiz_id', quizIds)
                .eq('status', 'submitted')
                .not('submitted_at', 'is', null)

              pendingCount = count || 0
            }

            return {
              id: subject.id,
              name: subject.name,
              grade_level: subject.grade_level,
              description: subject.description || '',
              section_count: sectionCount,
              pending_count: pendingCount
            }
          })
        )

        subjects.value = subjectsWithStats
      } catch (err) {
        console.error('Error fetching subjects:', err)
        error.value = `Failed to load subjects: ${err.message}`
      } finally {
        loading.value = false
      }
    }

    const selectSubject = async (subject) => {
      selectedSubject.value = subject
      await fetchSections(subject.id)
    }

    const fetchSections = async (subjectId) => {
      try {
        loading.value = true
        error.value = null

        // Optimized: Get sections with quiz data
        const { data: sectionsData, error: sectionsError } = await supabase
          .from('sections')
          .select(`
            id,
            name,
            section_code,
            max_students,
            quizzes (id)
          `)
          .eq('subject_id', subjectId)
          .eq('is_active', true)

        if (sectionsError) throw sectionsError

        // Process sections with pending count
        const sectionsWithStats = await Promise.all(
          (sectionsData || []).map(async (section) => {
            const quizCount = section.quizzes?.length || 0
            const quizIds = section.quizzes?.map(q => q.id) || []
            
            let pendingCount = 0
            if (quizIds.length > 0) {
              const { count } = await supabase
                .from('quiz_attempts')
                .select('id', { count: 'exact', head: true })
                .in('quiz_id', quizIds)
                .eq('status', 'submitted')
                .not('submitted_at', 'is', null)

              pendingCount = count || 0
            }

            return {
              id: section.id,
              name: section.name,
              section_code: section.section_code,
              max_students: section.max_students,
              quiz_count: quizCount,
              pending_count: pendingCount
            }
          })
        )

        sections.value = sectionsWithStats
      } catch (err) {
        console.error('Error fetching sections:', err)
        error.value = `Failed to load sections: ${err.message}`
      } finally {
        loading.value = false
      }
    }

    const selectSection = async (section) => {
      selectedSection.value = section
      await fetchSubmissions(section.id)
    }

    const fetchSubmissions = async (sectionId) => {
      try {
        loading.value = true
        error.value = null

        // Step 1: Get all quizzes for this section
        const { data: quizzes, error: quizzesError } = await supabase
          .from('quizzes')
          .select('id, title, quiz_code')
          .eq('section_id', sectionId)

        if (quizzesError) throw quizzesError

        if (!quizzes || quizzes.length === 0) {
          submissions.value = []
          loading.value = false
          return
        }

        const quizIds = quizzes.map(q => q.id)

        // Step 2: Get all quiz attempts for these quizzes
        const { data: submissionsData, error: submissionsError } = await supabase
          .from('quiz_attempts')
          .select(`
            id,
            quiz_id,
            student_id,
            attempt_number,
            total_score,
            max_score,
            percentage,
            status,
            submitted_at,
            time_taken_minutes,
            teacher_feedback,
            students (
              id,
              full_name,
              email
            )
          `)
          .in('quiz_id', quizIds)
          .order('submitted_at', { ascending: false })

        if (submissionsError) throw submissionsError

        // Create quiz lookup
        const quizMap = {}
        quizzes.forEach(q => { quizMap[q.id] = q })

        // Map submissions with all data
        submissions.value = (submissionsData || []).map(attempt => ({
          id: attempt.id,
          quiz_id: attempt.quiz_id,
          student_id: attempt.student_id,
          attempt_number: attempt.attempt_number,
          student_name: attempt.students?.full_name || 'Unknown Student',
          student_email: attempt.students?.email || '',
          quiz_title: quizMap[attempt.quiz_id]?.title || 'Unknown Quiz',
          quiz_code: quizMap[attempt.quiz_id]?.quiz_code || '',
          total_score: attempt.total_score || 0,
          max_score: attempt.max_score || 0,
          percentage: Math.round(attempt.percentage || 0),
          status: attempt.status || 'submitted',
          submitted_at: attempt.submitted_at,
          time_taken_minutes: attempt.time_taken_minutes,
          teacher_feedback: attempt.teacher_feedback
        }))

        console.log('Submissions loaded:', submissions.value.length)
      } catch (err) {
        console.error('Error fetching submissions:', err)
        error.value = `Failed to load submissions: ${err.message}`
      } finally {
        loading.value = false
      }
    }

    const resetToSubjects = () => {
      selectedSubject.value = null
      selectedSection.value = null
      sections.value = []
      submissions.value = []
      searchQuery.value = ''
    }

    const resetToSections = () => {
      selectedSection.value = null
      submissions.value = []
      searchQuery.value = ''
    }

    const refreshData = async () => {
      if (!selectedSubject && !selectedSection) {
        await fetchSubjects()
      } else if (selectedSubject && !selectedSection) {
        await fetchSections(selectedSubject.value.id)
      } else if (selectedSection) {
        await fetchSubmissions(selectedSection.value.id)
      }
    }

    const loadQuestionsAndAnswers = async (submission) => {
      try {
        loadingQuestions.value = true

        // Optimized: Get all question data with related records
        const { data: questions, error: questionsError } = await supabase
          .from('quiz_questions')
          .select(`
            id,
            question_number,
            question_type,
            question_text,
            points,
            question_options (
              id,
              option_number,
              option_text,
              is_correct
            ),
            question_answers (
              correct_answer
            )
          `)
          .eq('quiz_id', submission.quiz_id)
          .order('question_number')

        if (questionsError) throw questionsError

        if (!questions || questions.length === 0) {
          reviewQuestions.value = []
          return
        }

        const questionIds = questions.map(q => q.id)

        // Get student answers for this attempt
        const { data: studentAnswers, error: studentAnswersError } = await supabase
          .from('student_answers')
          .select('*')
          .eq('attempt_id', submission.id)

        if (studentAnswersError) throw studentAnswersError

        // Map everything together
        reviewQuestions.value = questions.map(q => {
          const studentAnswer = (studentAnswers || []).find(sa => sa.question_id === q.id)
          const questionAnswer = q.question_answers?.[0]

          return {
            id: q.id,
            question_number: q.question_number,
            question_type: q.question_type,
            question_text: q.question_text,
            points: q.points || 1,
            options: q.question_options || [],
            correct_answer: questionAnswer?.correct_answer || null,
            selected_option_id: studentAnswer?.selected_option_id || null,
            answer_text: studentAnswer?.answer_text || null,
            is_correct: studentAnswer?.is_correct || false,
            points_earned: studentAnswer?.points_earned || 0,
            teacher_comment: studentAnswer?.teacher_comment || '',
            manualPoints: studentAnswer?.points_earned || 0,
            student_answer_id: studentAnswer?.id || null
          }
        })
      } catch (err) {
        console.error('Error loading questions:', err)
        alert('Failed to load questions: ' + err.message)
      } finally {
        loadingQuestions.value = false
      }
    }

    const reviewSubmission = async (submission) => {
      modalMode.value = 'grade'
      selectedSubmission.value = submission
      reviewFeedback.value = submission.teacher_feedback || ''
      showReviewModal.value = true
      await loadQuestionsAndAnswers(submission)
    }

    const viewSubmission = async (submission) => {
      modalMode.value = 'view'
      selectedSubmission.value = submission
      reviewFeedback.value = submission.teacher_feedback || ''
      showReviewModal.value = true
      await loadQuestionsAndAnswers(submission)
    }

    const updateQuestionPoints = (question) => {
      if (question.manualPoints > question.points) {
        question.manualPoints = question.points
      }
      if (question.manualPoints < 0) {
        question.manualPoints = 0
      }
    }

    const calculateReviewScore = () => {
      if (modalMode.value === 'grade') {
        return reviewQuestions.value.reduce((sum, q) => sum + (parseFloat(q.manualPoints) || 0), 0)
      } else {
        return reviewQuestions.value.reduce((sum, q) => sum + (parseFloat(q.points_earned) || 0), 0)
      }
    }

    const calculateReviewPercentage = () => {
      if (maxReviewScore.value === 0) return 0
      return Math.round((calculateReviewScore() / maxReviewScore.value) * 100)
    }

    const closeReviewModal = () => {
      showReviewModal.value = false
      selectedSubmission.value = null
      reviewQuestions.value = []
      reviewFeedback.value = ''
      modalMode.value = 'view'
    }

    const getCorrectOptionLabel = (question) => {
      const correctOption = question.options.find(opt => opt.is_correct)
      if (correctOption) {
        return String.fromCharCode(65 + correctOption.option_number - 1)
      }
      return 'N/A'
    }

    const saveGrade = async () => {
      try {
        if (!selectedSubmission.value) return

        savingGrade.value = true
        const finalScore = calculateReviewScore()
        const finalPercentage = calculateReviewPercentage()

        // Update quiz attempt
        const { error: updateError } = await supabase
          .from('quiz_attempts')
          .update({
            total_score: finalScore,
            percentage: finalPercentage,
            status: 'graded',
            teacher_feedback: reviewFeedback.value,
            manually_reviewed: true,
            graded_by: teacherId.value,
            graded_at: new Date().toISOString()
          })
          .eq('id', selectedSubmission.value.id)

        if (updateError) throw updateError

        // Batch update student answers
        const answerUpdates = reviewQuestions.value
          .filter(q => q.student_answer_id)
          .map(q => ({
            id: q.student_answer_id,
            teacher_comment: q.teacherComment || null,
            points_earned: parseFloat(q.manualPoints) || 0
          }))

        if (answerUpdates.length > 0) {
          for (const update of answerUpdates) {
            await supabase
              .from('student_answers')
              .update({
                teacher_comment: update.teacher_comment,
                points_earned: update.points_earned
              })
              .eq('id', update.id)
          }
        }

        // Upsert quiz results
        await supabase
          .from('quiz_results')
          .upsert({
            quiz_id: selectedSubmission.value.quiz_id,
            student_id: selectedSubmission.value.student_id,
            best_attempt_id: selectedSubmission.value.id,
            best_score: finalScore,
            best_percentage: finalPercentage,
            total_attempts: selectedSubmission.value.attempt_number,
            latest_attempt_date: selectedSubmission.value.submitted_at,
            status: 'graded',
            finalized: true,
            visible_to_student: true
          }, {
            onConflict: 'quiz_id,student_id',
            ignoreDuplicates: false
          })

        // Update local data
        const index = submissions.value.findIndex(s => s.id === selectedSubmission.value.id)
        if (index !== -1) {
          submissions.value[index].status = 'graded'
          submissions.value[index].total_score = finalScore
          submissions.value[index].percentage = finalPercentage
          submissions.value[index].teacher_feedback = reviewFeedback.value
        }

        closeReviewModal()
        alert('Grade saved successfully!')
      } catch (err) {
        console.error('Error saving grade:', err)
        alert(`Error saving grade: ${err.message}`)
      } finally {
        savingGrade.value = false
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

    const getInitials = (name) => {
      if (!name) return '?'
      return name.split(' ').map(n => n[0]).join('').toUpperCase().substring(0, 2)
    }

    const formatDate = (dateString) => {
      if (!dateString) return 'N/A'
      return new Date(dateString).toLocaleDateString()
    }

    const formatTime = (dateString) => {
      if (!dateString) return 'N/A'
      return new Date(dateString).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
    }

    const getStatusText = (status) => {
      const map = {
        'in_progress': 'In Progress',
        'submitted': 'Pending Review',
        'graded': 'Graded',
        'reviewed': 'Reviewed'
      }
      return map[status] || status
    }

    const getScoreClass = (percentage) => {
      if (percentage >= 90) return 'excellent'
      if (percentage >= 80) return 'good'
      if (percentage >= 70) return 'average'
      return 'needs-improvement'
    }

    watch([searchQuery, selectedStatus], () => {
      currentPage.value = 1
    })

    onMounted(async () => {
      const success = await getTeacherInfo()
      if (success) {
        await fetchSubjects()
      } else {
        loading.value = false
      }
    })

    return {
      loading,
      loadingQuestions,
      savingGrade,
      error,
      searchQuery,
      subjects,
      selectedSubject,
      sections,
      selectedSection,
      submissions,
      selectedStatus,
      currentPage,
      totalPages,
      filteredSubjects,
      filteredSections,
      filteredSubmissions,
      paginatedSubmissions,
      sectionStats,
      showReviewModal,
      selectedSubmission,
      reviewQuestions,
      reviewFeedback,
      correctAnswerCount,
      maxReviewScore,
      modalMode,
      selectSubject,
      selectSection,
      resetToSubjects,
      resetToSections,
      refreshData,
      sortBy,
      getSortIcon,
      reviewSubmission,
      viewSubmission,
      updateQuestionPoints,
      closeReviewModal,
      saveGrade,
      calculateReviewScore,
      calculateReviewPercentage,
      getInitials,
      formatDate,
      formatTime,
      getStatusText,
      getScoreClass,
      getCorrectOptionLabel
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

.refresh-btn {
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
  color: #64748b;
}

.refresh-btn:hover:not(:disabled) {
  background: #f8fafc;
  border-color: #cbd5e1;
  color: #3b82f6;
}

.refresh-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.spinning {
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.loading-container, .error-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 400px;
}

.loading-container {
  color: #64748b;
}

.error-container {
  color: #dc2626;
  text-align: center;
  padding: 2rem;
}

.error-container i {
  font-size: 4rem;
  margin-bottom: 1rem;
  color: #fca5a5;
}

.error-container h3 {
  font-size: 1.5rem;
  margin-bottom: 0.5rem;
  color: #991b1b;
}

.btn-retry {
  padding: 0.75rem 1.5rem;
  background: #dc2626;
  color: white;
  border: none;
  border-radius: 0.5rem;
  cursor: pointer;
  font-size: 1rem;
  margin-top: 1rem;
}

.btn-retry:hover {
  background: #b91c1c;
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

.stat-icon.pending { background: #f59e0b; }
.stat-icon.graded { background: #10b981; }
.stat-icon.reviewed { background: #3b82f6; }
.stat-icon.average { background: #8b5cf6; }

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
}

.section-header h2 {
  font-size: 1.5rem;
  font-weight: 600;
  color: #1a202c;
  margin: 0;
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
  font-family: monospace;
  background: #f1f5f9;
  padding: 0.125rem 0.5rem;
  border-radius: 0.25rem;
  display: inline-block;
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

.score-percentage.excellent { color: #059669; }
.score-percentage.good { color: #0369a1; }
.score-percentage.average { color: #d97706; }
.score-percentage.needs-improvement { color: #dc2626; }

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

.btn-action.auto-grade {
  background: #fef3c7;
  color: #92400e;
}

.btn-action.auto-grade:hover {
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

.modal-subtitle {
  color: #64748b;
  font-size: 0.875rem;
  margin: 0.25rem 0 0 0;
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
}

.modal-close:hover {
  background: #f1f5f9;
  color: #374151;
}

.modal-content {
  flex: 1;
  overflow-y: auto;
}

.loading-questions, .no-questions {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 3rem 2rem;
  color: #64748b;
}

.spinner-small {
  width: 30px;
  height: 30px;
  border: 3px solid #e2e8f0;
  border-top: 3px solid #3b82f6;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin-bottom: 1rem;
}

.submission-review {
  padding: 1.5rem;
}

.review-summary {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 1rem;
  padding: 1.5rem;
  background: #f8fafc;
  border-radius: 0.5rem;
  margin-bottom: 1.5rem;
}

.summary-stat {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
}

.stat-label {
  font-size: 0.875rem;
  color: #64748b;
  margin-bottom: 0.5rem;
}

.stat-value {
  font-size: 1.5rem;
  font-weight: 700;
  color: #1a202c;
}

.questions-review {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.question-review-item {
  border: 1px solid #e2e8f0;
  border-radius: 0.5rem;
  padding: 1.5rem;
  background: white;
}

.question-header {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 1rem;
  flex-wrap: wrap;
}

.question-number {
  background: #3b82f6;
  color: white;
  padding: 0.5rem 0.75rem;
  border-radius: 0.375rem;
  font-weight: 600;
  font-size: 0.875rem;
}

.question-result {
  padding: 0.5rem 0.75rem;
  border-radius: 0.375rem;
  font-weight: 600;
  font-size: 0.875rem;
}

.question-result.correct {
  background: #d1fae5;
  color: #065f46;
}

.question-result.incorrect {
  background: #fee2e2;
  color: #991b1b;
}

.question-points {
  margin-left: auto;
  color: #64748b;
  font-weight: 600;
}

.question-text {
  font-size: 1.125rem;
  color: #1a202c;
  margin-bottom: 1rem;
  line-height: 1.6;
}

.answer-section {
  margin: 1rem 0;
}

.options-grid {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.option-item {
  display: flex;
  align-items: flex-start;
  gap: 0.75rem;
  padding: 1rem;
  border: 2px solid #e2e8f0;
  border-radius: 0.5rem;
  background: white;
}

.option-item.correct {
  border-color: #10b981;
  background: #ecfdf5;
}

.option-item.incorrect {
  border-color: #ef4444;
  background: #fef2f2;
}

.option-letter {
  min-width: 32px;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #f1f5f9;
  border-radius: 50%;
  font-weight: 700;
  color: #475569;
}

.option-item.correct .option-letter {
  background: #10b981;
  color: white;
}

.option-item.incorrect .option-letter {
  background: #ef4444;
  color: white;
}

.option-content {
  flex: 1;
}

.option-text {
  color: #1a202c;
  line-height: 1.5;
}

.true-false-options {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
}

.tf-option {
  padding: 1.5rem;
  border: 2px solid #e2e8f0;
  border-radius: 0.5rem;
  text-align: center;
  background: white;
}

.tf-option.student-selected {
  border-color: #3b82f6;
  background: #eff6ff;
}

.tf-option.correct-answer {
  border-color: #10b981;
  background: #ecfdf5;
}

.tf-option strong {
  display: block;
  font-size: 1.125rem;
  color: #1a202c;
}

.fill-blank-answers {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.student-answer-box, .correct-answer-box {
  padding: 1rem;
  border-radius: 0.5rem;
  border: 1px solid #e2e8f0;
}

.answer-label {
  font-size: 0.875rem;
  color: #64748b;
  margin-bottom: 0.5rem;
  font-weight: 600;
}

.answer-text {
  padding: 0.75rem;
  border-radius: 0.375rem;
  font-size: 1rem;
}

.answer-text.correct {
  background: #d1fae5;
  color: #065f46;
}

.answer-text.incorrect {
  background: #fee2e2;
  color: #991b1b;
}

.teacher-comment-section {
  margin-top: 1rem;
}

.comment-input {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid #e2e8f0;
  border-radius: 0.375rem;
  font-family: inherit;
  font-size: 0.875rem;
  resize: vertical;
}

.comment-input:focus {
  outline: none;
  border-color: #3b82f6;
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
}

.overall-feedback-section {
  margin-top: 1.5rem;
  padding-top: 1.5rem;
  border-top: 2px solid #e2e8f0;
}

.overall-feedback-section h4 {
  font-size: 1.125rem;
  color: #1a202c;
  margin-bottom: 0.75rem;
}

.feedback-textarea {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid #e2e8f0;
  border-radius: 0.375rem;
  font-family: inherit;
  font-size: 0.875rem;
  resize: vertical;
}

.feedback-textarea:focus {
  outline: none;
  border-color: #3b82f6;
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
}

.modal-actions {
  padding: 1.5rem;
  border-top: 1px solid #e2e8f0;
  display: flex;
  justify-content: flex-end;
  gap: 1rem;
}

.btn-modal {
  padding: 0.75rem 1.5rem;
  border: none;
  border-radius: 0.5rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
}

.btn-modal.cancel {
  background: #f1f5f9;
  color: #475569;
}

.btn-modal.cancel:hover {
  background: #e2e8f0;
}

.btn-modal.primary {
  background: #3b82f6;
  color: white;
}

.btn-modal.primary:hover:not(:disabled) {
  background: #2563eb;
}

.btn-modal:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

@media (max-width: 768px) {
  .gradebook-container {
    padding: 1rem;
  }

  .gradebook-header {
    flex-direction: column;
    align-items: stretch;
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

  .true-false-options {
    grid-template-columns: 1fr;
  }

  .review-summary {
    grid-template-columns: 1fr;
  }
}

/* Breadcrumb Navigation */
.breadcrumb {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 1rem 0;
  margin-bottom: 1rem;
}

.breadcrumb-item {
  background: none;
  border: none;
  color: #64748b;
  cursor: pointer;
  padding: 0.5rem 0.75rem;
  border-radius: 0.375rem;
  font-size: 0.875rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  transition: all 0.2s;
}

.breadcrumb-item:hover {
  background: #f1f5f9;
  color: #3b82f6;
}

.breadcrumb-item.active {
  color: #1a202c;
  font-weight: 600;
  cursor: default;
}

.breadcrumb-item.active:hover {
  background: none;
}

.breadcrumb-separator {
  color: #cbd5e1;
}

/* Subject Cards */
.subjects-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 1.5rem;
}

.subject-card {
  background: white;
  border-radius: 0.75rem;
  padding: 1.5rem;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  cursor: pointer;
  transition: all 0.2s;
  display: flex;
  align-items: center;
  gap: 1rem;
}

.subject-card:hover {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  transform: translateY(-2px);
}

.subject-icon {
  width: 60px;
  height: 60px;
  border-radius: 0.75rem;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-size: 1.5rem;
  flex-shrink: 0;
}

.subject-info {
  flex: 1;
}

.subject-info h3 {
  font-size: 1.25rem;
  font-weight: 600;
  color: #1a202c;
  margin: 0 0 0.25rem 0;
}

.subject-info p {
  color: #64748b;
  font-size: 0.875rem;
  margin: 0 0 0.75rem 0;
  font-family: monospace;
}

.subject-stats {
  display: flex;
  gap: 0.5rem;
  flex-wrap: wrap;
}

.stat-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.375rem;
  padding: 0.25rem 0.625rem;
  background: #f1f5f9;
  border-radius: 0.375rem;
  font-size: 0.75rem;
  color: #475569;
  font-weight: 500;
}

.stat-badge.pending {
  background: #fef3c7;
  color: #92400e;
}

.stat-badge i {
  font-size: 0.625rem;
}

.card-arrow {
  color: #cbd5e1;
  font-size: 1.25rem;
}

/* Section Cards */
.sections-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 1.5rem;
}

.section-card {
  background: white;
  border-radius: 0.75rem;
  padding: 1.5rem;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  cursor: pointer;
  transition: all 0.2s;
  display: flex;
  align-items: center;
  gap: 1rem;
}

.section-card:hover {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  transform: translateY(-2px);
}

.section-icon {
  width: 60px;
  height: 60px;
  border-radius: 0.75rem;
  background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-size: 1.5rem;
  flex-shrink: 0;
}

.section-info {
  flex: 1;
}

.section-info h3 {
  font-size: 1.25rem;
  font-weight: 600;
  color: #1a202c;
  margin: 0 0 0.25rem 0;
}

.section-info p {
  color: #64748b;
  font-size: 0.875rem;
  margin: 0 0 0.75rem 0;
}

.section-stats {
  display: flex;
  gap: 0.5rem;
  flex-wrap: wrap;
}

/* Submissions View */
.submissions-view {
  animation: fadeIn 0.3s ease-in;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.submissions-filters {
  padding: 1rem 0;
  display: flex;
  justify-content: flex-end;
}

.stat-card .stat-icon.total {
  background: #6366f1;
}

/* Points Input in Modal */
.points-input {
  width: 60px;
  padding: 0.25rem 0.5rem;
  border: 1px solid #e2e8f0;
  border-radius: 0.25rem;
  text-align: center;
  font-weight: 600;
  font-size: 0.875rem;
}

.points-input:focus {
  outline: none;
  border-color: #3b82f6;
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
}

/* True/False styling updates */
.tf-option.wrong-answer {
  border-color: #ef4444;
  background: #fef2f2;
}

.tf-option.correct-answer.student-selected {
  border-color: #10b981;
  background: #ecfdf5;
}

/* Responsive adjustments */
@media (max-width: 768px) {
  .subjects-grid,
  .sections-grid {
    grid-template-columns: 1fr;
  }

  .breadcrumb {
    flex-wrap: wrap;
  }

  .subject-card,
  .section-card {
    padding: 1rem;
  }

  .subject-icon,
  .section-icon {
    width: 50px;
    height: 50px;
    font-size: 1.25rem;
  }
}
</style>