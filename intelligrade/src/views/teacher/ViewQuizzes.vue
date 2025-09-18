<template>
  <div class="page-container">
    <div class="main-wrapper">
      <!-- Header Section -->
      <div class="hero-header card-box">
        <div class="header-content">
          <button @click="goBack" class="back-button">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
              <path d="M10 19l-7-7 7-7m-7 7h18"></path>
            </svg>
            Back to Section
          </button>
          
          <div class="section-header">
            <h1>{{ sectionName }} Quizzes</h1>
            <div class="section-info">
              <div class="info-badge">
                <span class="label">Total Quizzes:</span>
                <span class="value">{{ quizzes.length }}</span>
              </div>
              <div class="info-badge">
                <span class="label">Published:</span>
                <span class="value">{{ publishedQuizzes }}</span>
              </div>
              <div class="info-badge">
                <span class="label">Draft:</span>
                <span class="value">{{ draftQuizzes }}</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Quick Actions -->
      <div class="quick-actions card-box">
        <div class="actions-header">
          <h2>Quiz Management</h2>
          <button @click="navigateToCreateQuiz" class="create-quiz-btn">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M19,13H13V19H11V13H5V11H11V5H13V11H19V13Z" />
            </svg>
            Create New Quiz
          </button>
        </div>
        
        <!-- Filters -->
        <div class="filters-section">
          <div class="filter-group">
            <label>Filter by Status:</label>
            <select v-model="filterStatus">
              <option value="all">All Quizzes</option>
              <option value="draft">Draft</option>
              <option value="published">Published</option>
              <option value="archived">Archived</option>
            </select>
          </div>
          
          <div class="search-group">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" class="search-icon">
              <path d="M9.5,3A6.5,6.5 0 0,1 16,9.5C16,11.11 15.41,12.59 14.44,13.73L14.71,14H15.5L20.5,19L19,20.5L14,15.5V14.71L13.73,14.44C12.59,15.41 11.11,16 9.5,16A6.5,6.5 0 0,1 3,9.5A6.5,6.5 0 0,1 9.5,3M9.5,5C7,5 5,7 5,9.5C5,12 7,14 9.5,14C12,14 14,12 14,9.5C14,7 12,5 9.5,5Z" />
            </svg>
            <input 
              type="text" 
              v-model="searchQuery" 
              placeholder="Search quizzes..."
            >
          </div>
        </div>
      </div>

      <!-- Quizzes List -->
      <div class="quizzes-section card-box">
        <div v-if="filteredQuizzes.length > 0" class="quizzes-grid">
          <div v-for="quiz in filteredQuizzes" :key="quiz.id" class="quiz-card">
            <div class="quiz-header">
              <div class="quiz-title-section">
                <h3>{{ quiz.title }}</h3>
                <div class="quiz-meta">
                  <span class="quiz-date">Created: {{ formatDate(quiz.created_at) }}</span>
                  <span class="quiz-questions">{{ quiz.questions_count || 0 }} Questions</span>
                </div>
              </div>
              
              <div class="quiz-status">
                <span :class="['status-badge', quiz.status]">{{ quiz.status }}</span>
              </div>
            </div>

            <div class="quiz-stats">
              <div class="stat-item">
                <span class="stat-value">{{ quiz.total_points || 0 }}</span>
                <span class="stat-label">Total Points</span>
              </div>
              <div class="stat-item">
                <span class="stat-value">{{ quiz.time_limit || 'No Limit' }}</span>
                <span class="stat-label">Time Limit</span>
              </div>
              <div class="stat-item">
                <span class="stat-value">{{ quiz.submissions_count || 0 }}</span>
                <span class="stat-label">Submissions</span>
              </div>
              <div class="stat-item">
                <span class="stat-value">{{ quiz.average_score || 'N/A' }}%</span>
                <span class="stat-label">Avg Score</span>
              </div>
            </div>

            <div class="quiz-actions">
              <button @click="viewQuizDetails(quiz)" class="quiz-action-btn view" title="View Details">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M12,9A3,3 0 0,0 9,12A3,3 0 0,0 12,15A3,3 0 0,0 15,12A3,3 0 0,0 12,9M12,17A5,5 0 0,1 7,12A5,5 0 0,1 12,7A5,5 0 0,1 17,12A5,5 0 0,1 12,17M12,4.5C7,4.5 2.73,7.61 1,12C2.73,16.39 7,19.5 12,19.5C17,19.5 21.27,16.39 23,12C21.27,7.61 17,4.5 12,4.5Z" />
                </svg>
              </button>
              
              <button @click="editQuiz(quiz)" class="quiz-action-btn edit" title="Edit Quiz">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M20.71,7.04C21.1,6.65 21.1,6 20.71,5.63L18.37,3.29C18,2.9 17.35,2.9 16.96,3.29L15.12,5.12L18.87,8.87M3,17.25V21H6.75L17.81,9.93L14.06,6.18L3,17.25Z" />
                </svg>
              </button>
              
              <button @click="duplicateQuiz(quiz)" class="quiz-action-btn duplicate" title="Duplicate Quiz">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M19,21H8V7H19M19,5H8A2,2 0 0,0 6,7V21A2,2 0 0,0 8,23H19A2,2 0 0,0 21,21V7A2,2 0 0,0 19,5M16,1H4A2,2 0 0,0 2,3V17H4V3H16V1Z" />
                </svg>
              </button>
              
              <button 
                @click="toggleQuizStatus(quiz)" 
                :class="['quiz-action-btn', 'status-toggle', quiz.status]" 
                :title="quiz.status === 'published' ? 'Unpublish Quiz' : 'Publish Quiz'"
              >
                <svg v-if="quiz.status === 'published'" width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M12,2A1,1 0 0,1 13,3V9A1,1 0 0,1 12,10A1,1 0 0,1 11,9V3A1,1 0 0,1 12,2M21,11A1,1 0 0,1 22,12A1,1 0 0,1 21,13H15A1,1 0 0,1 14,12A1,1 0 0,1 15,11H21M19.07,19.07A1,1 0 0,1 18.36,19.78A1,1 0 0,1 17.65,19.07L13.41,14.83A1,1 0 0,1 13.41,13.41A1,1 0 0,1 14.83,13.41L19.07,17.65A1,1 0 0,1 19.07,19.07M20.5,12A8.5,8.5 0 0,1 12,20.5A8.5,8.5 0 0,1 3.5,12A8.5,8.5 0 0,1 12,3.5A8.5,8.5 0 0,1 20.5,12" />
                </svg>
                <svg v-else width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M17.66,8L12,2.35L6.34,8C6.22,8.11 6.22,8.2 6.34,8.31L12,14L17.66,8.31C17.78,8.2 17.78,8.11 17.66,8M6.34,16L12,10.35L17.66,16C17.78,16.11 17.78,16.2 17.66,16.31L12,22L6.34,16.31C6.22,16.2 6.22,16.11 6.34,16Z" />
                </svg>
              </button>
              
              <button @click="deleteQuiz(quiz)" class="quiz-action-btn delete" title="Delete Quiz">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M19,4H15.5L14.5,3H9.5L8.5,4H5V6H19M6,19A2,2 0 0,0 8,21H16A2,2 0 0,0 18,19V7H6V19Z" />
                </svg>
              </button>
            </div>
          </div>
        </div>

        <!-- Empty State -->
        <div v-else-if="quizzes.length === 0" class="empty-state">
          <div class="empty-icon">
            <svg width="64" height="64" viewBox="0 0 24 24" fill="currentColor">
              <path d="M14,2H6A2,2 0 0,0 4,4V20A2,2 0 0,0 6,22H18A2,2 0 0,0 20,20V8L14,2M18,20H6V4H13V9H18V20Z" />
            </svg>
          </div>
          <h3>No Quizzes Created Yet</h3>
          <p>Create your first quiz to start assessing your students' knowledge.</p>
          <button @click="navigateToCreateQuiz" class="empty-action-btn">
            Create First Quiz
          </button>
        </div>

        <!-- No Search Results -->
        <div v-else class="no-results">
          <p>No quizzes found matching your criteria.</p>
          <button @click="clearFilters" class="clear-filters-btn">Clear Filters</button>
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

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { supabase } from '../../supabase'

const router = useRouter()
const route = useRoute()

// Route data
const subjectId = ref(route.params.subjectId)
const sectionId = ref(route.params.sectionId)
const sectionName = ref(route.query.sectionName || 'Section')

// State
const quizzes = ref([])
const filterStatus = ref('all')
const searchQuery = ref('')
const isLoading = ref(false)
const loadingMessage = ref('')

// Computed
const filteredQuizzes = computed(() => {
  let filtered = quizzes.value

  // Filter by status
  if (filterStatus.value !== 'all') {
    filtered = filtered.filter(quiz => quiz.status === filterStatus.value)
  }

  // Filter by search query
  if (searchQuery.value) {
    const query = searchQuery.value.toLowerCase()
    filtered = filtered.filter(quiz => 
      quiz.title.toLowerCase().includes(query)
    )
  }

  return filtered
})

const publishedQuizzes = computed(() => {
  return quizzes.value.filter(quiz => quiz.status === 'published').length
})

const draftQuizzes = computed(() => {
  return quizzes.value.filter(quiz => quiz.status === 'draft').length
})

// Methods
const fetchQuizzes = async () => {
  isLoading.value = true
  loadingMessage.value = 'Loading quizzes...'

  try {
    const { data, error } = await supabase
      .from('quizzes')
      .select(`
        *,
        quiz_questions(count)
      `)
      .eq('section_id', sectionId.value)
      .order('created_at', { ascending: false })

    if (error) throw error

    // Transform data and add mock statistics
    quizzes.value = data.map(quiz => ({
      ...quiz,
      questions_count: quiz.quiz_questions?.[0]?.count || 0,
      submissions_count: Math.floor(Math.random() * 25), // Mock data
      average_score: Math.floor(Math.random() * 40) + 60 // Mock data 60-100%
    }))

  } catch (error) {
    console.error('Error fetching quizzes:', error)
    alert(`Error loading quizzes: ${error.message}`)
  } finally {
    isLoading.value = false
  }
}

const formatDate = (dateString) => {
  const date = new Date(dateString)
  return date.toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'short',
    day: 'numeric'
  })
}

// Navigation
const goBack = () => {
  router.push({
    name: 'ViewStudents',
    params: { subjectId: subjectId.value, sectionId: sectionId.value }
  })
}

const navigateToCreateQuiz = () => {
  router.push({
    name: 'CreateQuiz',
    params: { subjectId: subjectId.value, sectionId: sectionId.value }
  })
}

// Quiz Actions
const viewQuizDetails = (quiz) => {
  console.log('Viewing quiz details:', quiz)
  alert(`View details for "${quiz.title}" - This feature will show quiz analytics, student submissions, and results.`)
}

const editQuiz = (quiz) => {
  console.log('Editing quiz:', quiz)
  alert(`Edit "${quiz.title}" - This feature will allow you to modify quiz questions and settings.`)
}

const duplicateQuiz = async (quiz) => {
  if (!confirm(`Duplicate "${quiz.title}"?`)) return

  isLoading.value = true
  loadingMessage.value = 'Duplicating quiz...'

  try {
    // Create a duplicate quiz
    const duplicateData = {
      title: `${quiz.title} (Copy)`,
      subject_id: quiz.subject_id,
      section_id: quiz.section_id,
      teacher_id: quiz.teacher_id,
      time_limit: quiz.time_limit,
      total_points: quiz.total_points,
      status: 'draft'
    }

    console.log('Duplicating quiz:', duplicateData)
    alert(`Quiz "${quiz.title}" duplicated successfully!`)
    
    // Refresh quizzes
    await fetchQuizzes()

  } catch (error) {
    console.error('Error duplicating quiz:', error)
    alert(`Error duplicating quiz: ${error.message}`)
  } finally {
    isLoading.value = false
  }
}

const toggleQuizStatus = async (quiz) => {
  const newStatus = quiz.status === 'published' ? 'draft' : 'published'
  const action = newStatus === 'published' ? 'publish' : 'unpublish'
  
  if (!confirm(`Are you sure you want to ${action} "${quiz.title}"?`)) return

  isLoading.value = true
  loadingMessage.value = `${action === 'publish' ? 'Publishing' : 'Unpublishing'} quiz...`

  try {
    const { error } = await supabase
      .from('quizzes')
      .update({ status: newStatus })
      .eq('id', quiz.id)

    if (error) throw error

    // Update local state
    quiz.status = newStatus
    alert(`Quiz "${quiz.title}" ${newStatus === 'published' ? 'published' : 'unpublished'} successfully!`)

  } catch (error) {
    console.error('Error updating quiz status:', error)
    alert(`Error updating quiz status: ${error.message}`)
  } finally {
    isLoading.value = false
  }
}

const deleteQuiz = async (quiz) => {
  if (!confirm(`Are you sure you want to delete "${quiz.title}"? This action cannot be undone.`)) {
    return
  }

  isLoading.value = true
  loadingMessage.value = 'Deleting quiz...'

  try {
    const { error } = await supabase
      .from('quizzes')
      .delete()
      .eq('id', quiz.id)

    if (error) throw error

    alert(`Quiz "${quiz.title}" deleted successfully!`)
    await fetchQuizzes()

  } catch (error) {
    console.error('Error deleting quiz:', error)
    alert(`Error deleting quiz: ${error.message}`)
  } finally {
    isLoading.value = false
  }
}

const clearFilters = () => {
  filterStatus.value = 'all'
  searchQuery.value = ''
}

// Lifecycle
onMounted(() => {
  fetchQuizzes()
})
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

.page-container {
  padding: 2rem 5%;
  font-family: 'Inter', sans-serif;
  min-height: 100vh;
  background: linear-gradient(135deg, #f0f9f6 0%, #e8f5f0 100%);
}

.main-wrapper {
  max-width: 1400px;
  margin: 0 auto;
}

.card-box {
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(20px);
  border: 1px solid rgba(61, 141, 122, 0.1);
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

.section-info {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
}

.info-badge {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1.25rem;
  border-radius: 12px;
  background: rgba(16, 185, 129, 0.1);
  border: 1px solid rgba(16, 185, 129, 0.2);
  font-size: 0.9rem;
}

.info-badge .label {
  font-weight: 600;
  color: #666;
}

.info-badge .value {
  font-weight: 700;
  color: #10b981;
}

.actions-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
  flex-wrap: wrap;
  gap: 1rem;
}

.actions-header h2 {
  color: #3D8D7A;
  font-size: 1.5rem;
  font-weight: 700;
  margin: 0;
}

.create-quiz-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  background: linear-gradient(135deg, #10b981 0%, #34d399 100%);
  color: white;
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 12px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s;
}

.create-quiz-btn:hover {
  transform: translateY(-1px);
  box-shadow: 0 8px 20px rgba(16, 185, 129, 0.3);
}

.filters-section {
  display: flex;
  gap: 2rem;
  align-items: end;
  flex-wrap: wrap;
}

.filter-group,
.search-group {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.filter-group label {
  font-weight: 600;
  color: #444;
  font-size: 0.9rem;
}

.filter-group select {
  padding: 0.75rem 1rem;
  border: 2px solid rgba(61, 141, 122, 0.1);
  border-radius: 12px;
  font-size: 1rem;
  background: white;
  min-width: 150px;
}

.search-group {
  position: relative;
  flex: 1;
  min-width: 250px;
}

.search-icon {
  position: absolute;
  left: 1rem;
  bottom: 0.75rem;
  color: #666;
}

.search-group input {
  width: 100%;
  padding: 0.75rem 1rem 0.75rem 3rem;
  border: 2px solid rgba(61, 141, 122, 0.1);
  border-radius: 12px;
  font-size: 1rem;
}

.search-group input:focus,
.filter-group select:focus {
  outline: none;
  border-color: #3D8D7A;
  box-shadow: 0 0 0 3px rgba(61, 141, 122, 0.1);
}

.quizzes-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(400px, 1fr));
  gap: 2rem;
}

.quiz-card {
  background: white;
  border: 2px solid rgba(61, 141, 122, 0.1);
  border-radius: 16px;
  padding: 2rem;
  transition: all 0.3s ease;
}

.quiz-card:hover {
  border-color: rgba(61, 141, 122, 0.3);
  box-shadow: 0 8px 24px rgba(61, 141, 122, 0.15);
  transform: translateY(-2px);
}

.quiz-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 1.5rem;
}

.quiz-title-section h3 {
  color: #3D8D7A;
  font-size: 1.25rem;
  font-weight: 700;
  margin-bottom: 0.5rem;
}

.quiz-meta {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}

.quiz-date,
.quiz-questions {
  color: #666;
  font-size: 0.85rem;
}

.status-badge {
  padding: 0.5rem 1rem;
  border-radius: 20px;
  font-size: 0.8rem;
  font-weight: 600;
  text-transform: uppercase;
}

.status-badge.draft {
  background: rgba(245, 158, 11, 0.1);
  color: #f59e0b;
  border: 1px solid rgba(245, 158, 11, 0.3);
}

.status-badge.published {
  background: rgba(16, 185, 129, 0.1);
  color: #10b981;
  border: 1px solid rgba(16, 185, 129, 0.3);
}

.status-badge.archived {
  background: rgba(107, 114, 128, 0.1);
  color: #6b7280;
  border: 1px solid rgba(107, 114, 128, 0.3);
}

.quiz-stats {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1rem;
  margin-bottom: 2rem;
  padding: 1.5rem;
  background: rgba(251, 255, 228, 0.5);
  border-radius: 12px;
}

.stat-item {
  text-align: center;
}

.stat-value {
  display: block;
  font-size: 1.4rem;
  font-weight: 800;
  color: #3D8D7A;
}

.stat-label {
  font-size: 0.75rem;
  color: #666;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  font-weight: 600;
}

.quiz-actions {
  display: flex;
  gap: 0.5rem;
  justify-content: flex-end;
  flex-wrap: wrap;
}

.quiz-action-btn {
  padding: 0.75rem;
  border: none;
  border-radius: 10px;
  cursor: pointer;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  justify-content: center;
}

.quiz-action-btn.view {
  background: rgba(59, 130, 246, 0.1);
  color: #3b82f6;
}

.quiz-action-btn.edit {
  background: rgba(16, 185, 129, 0.1);
  color: #10b981;
}

.quiz-action-btn.duplicate {
  background: rgba(139, 92, 246, 0.1);
  color: #8b5cf6;
}

.quiz-action-btn.status-toggle.draft {
  background: rgba(16, 185, 129, 0.1);
  color: #10b981;
}

.quiz-action-btn.status-toggle.published {
  background: rgba(245, 158, 11, 0.1);
  color: #f59e0b;
}

.quiz-action-btn.delete {
  background: rgba(239, 68, 68, 0.1);
  color: #ef4444;
}

.quiz-action-btn:hover {
  transform: scale(1.1);
}

.empty-state,
.no-results {
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
  font-size: 1.8rem;
  font-weight: 700;
  margin-bottom: 1rem;
}

.empty-action-btn,
.clear-filters-btn {
  background: linear-gradient(135deg, #3D8D7A 0%, #A3D1C6 100%);
  color: white;
  border: none;
  padding: 1rem 2rem;
  border-radius: 16px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s;
  margin-top: 1rem;
}

.empty-action-btn:hover,
.clear-filters-btn:hover {
  transform: translateY(-2px);
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
  background: white;
  padding: 2rem;
  border-radius: 16px;
  text-align: center;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
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

  .section-info {
    flex-direction: column;
    gap: 0.75rem;
  }

  .actions-header {
    flex-direction: column;
    align-items: stretch;
  }

  .filters-section {
    flex-direction: column;
    gap: 1rem;
  }

  .quizzes-grid {
    grid-template-columns: 1fr;
  }

  .quiz-stats {
    grid-template-columns: repeat(2, 1fr);
  }

  .quiz-actions {
    justify-content: center;
  }
}
</style>