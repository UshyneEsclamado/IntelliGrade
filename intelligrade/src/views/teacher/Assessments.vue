<template>
  <div class="assessments-page" :class="{ 'dark-mode': isDarkMode }">
    <!-- Header Section -->
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
            <svg width="36" height="36" viewBox="0 0 24 24" fill="currentColor">
              <path d="M14,2H6A2,2 0 0,0 4,4V20A2,2 0 0,0 6,22H18A2,2 0 0,0 20,20V8L14,2M18,20H6V4H13V9H18V20Z" />
            </svg>
          </div>
          
          <div class="header-text">
            <h1 class="section-header-title">Assessments</h1>
            <p class="section-header-subtitle">{{ subjectInfo?.subjectName }} - {{ subjectInfo?.sectionName }}</p>
            <p class="section-header-description">Manage and track student assessments</p>
          </div>
        </div>
        
        <div class="header-actions">
          <button @click="toggleDarkMode" class="dark-mode-toggle" :title="isDarkMode ? 'Switch to Light Mode' : 'Switch to Dark Mode'">
            <svg v-if="isDarkMode" width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M12,7A5,5 0 0,1 17,12A5,5 0 0,1 12,17A5,5 0 0,1 7,12A5,5 0 0,1 12,7M12,9A3,3 0 0,0 9,12A3,3 0 0,0 12,15A3,3 0 0,0 15,12A3,3 0 0,0 12,9M12,2L14.39,5.42C13.65,5.15 12.84,5 12,5C11.16,5 10.35,5.15 9.61,5.42L12,2M3.34,7L7.5,6.65C6.9,7.16 6.36,7.78 5.94,8.5C5.52,9.22 5.25,10 5.11,10.79L3.34,7M3.36,17L5.12,13.23C5.26,14 5.53,14.78 5.95,15.5C6.37,16.22 6.91,16.84 7.51,17.35L3.36,17M20.65,7L18.88,10.79C18.74,10 18.47,9.22 18.05,8.5C17.63,7.78 17.09,7.15 16.49,6.64L20.65,7M20.64,17L16.5,17.36C17.1,16.85 17.64,16.22 18.06,15.5C18.48,14.78 18.75,14 18.89,13.21L20.64,17M12,22L9.59,18.56C10.33,18.83 11.14,19 12,19C12.86,19 13.67,18.83 14.41,18.56L12,22Z" />
            </svg>
            <svg v-else width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M17.75,4.09L15.22,6.03L16.13,9.09L13.5,7.28L10.87,9.09L11.78,6.03L9.25,4.09L12.44,4L13.5,1L14.56,4L17.75,4.09M21.25,11L19.61,12.25L20.2,14.23L18.5,13.06L16.8,14.23L17.39,12.25L15.75,11L17.81,10.95L18.5,9L19.19,10.95L21.25,11M18.97,15.95C19.8,15.87 20.69,17.05 20.16,17.8C19.84,18.25 19.5,18.67 19.08,19.07C15.17,23 8.84,23 4.94,19.07C1.03,15.17 1.03,8.83 4.94,4.93C5.34,4.53 5.76,4.17 6.21,3.85C6.96,3.32 8.14,4.21 8.06,5.04C7.79,7.9 8.75,10.87 10.95,13.06C13.14,15.26 16.1,16.22 18.97,15.95M17.33,17.97C14.5,17.81 11.7,16.64 9.53,14.5C7.36,12.31 6.2,9.5 6.04,6.68C3.23,9.82 3.34,14.4 6.35,17.41C9.37,20.43 14,20.54 17.33,17.97Z" />
            </svg>
          </button>
          <button @click="showCreateModal = true" class="create-btn">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M19,13H13V19H11V13H5V11H11V5H13V11H19V13Z" />
            </svg>
            Add Assessment
          </button>
        </div>
      </div>
    </div>

    <!-- Filter Tabs -->
    <div class="filter-tabs">
      <button 
        v-for="filter in filters" 
        :key="filter.key"
        :class="['filter-tab', { active: activeFilter === filter.key }]"
        @click="setActiveFilter(filter.key)"
      >
        <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
          <path :d="filter.icon" />
        </svg>
        {{ filter.label }}
        <span class="count">{{ getFilteredCount(filter.key) }}</span>
      </button>
    </div>

    <!-- Assessments Grid -->
    <div class="assessments-container" v-if="!isLoading">
      <div v-if="filteredAssessments.length > 0" class="assessments-grid">
        <div v-for="assessment in filteredAssessments" :key="assessment.id" class="assessment-card">
          <div class="assessment-header">
            <div class="assessment-info">
              <h3>{{ assessment.title }}</h3>
              <p class="assessment-type">{{ assessment.type }}</p>
              <div class="assessment-meta">
                <span class="date">{{ formatDate(assessment.due_date) }}</span>
                <span :class="['status', assessment.status]">{{ assessment.status }}</span>
              </div>
            </div>
            <div class="assessment-actions">
              <button @click="editAssessment(assessment)" class="action-btn edit" title="Edit Assessment">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M20.71,7.04C21.1,6.65 21.1,6 20.71,5.63L18.37,3.29C18,2.9 17.35,2.9 16.96,3.29L15.12,5.12L18.87,8.87M3,17.25V21H6.75L17.81,9.93L14.06,6.18L3,17.25Z" />
                </svg>
              </button>
              <button @click="deleteAssessment(assessment.id)" class="action-btn delete" title="Delete Assessment">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M19,4H15.5L14.5,3H9.5L8.5,4H5V6H19M6,19A2,2 0 0,0 8,21H16A2,2 0 0,0 18,19V7H6V19Z" />
                </svg>
              </button>
            </div>
          </div>

          <div class="assessment-content">
            <p class="description">{{ assessment.description || 'No description provided' }}</p>
            
            <div class="assessment-stats">
              <div class="stat">
                <span class="stat-number">{{ assessment.total_points || 0 }}</span>
                <span class="stat-label">Points</span>
              </div>
              <div class="stat">
                <span class="stat-number">{{ assessment.duration || 'N/A' }}</span>
                <span class="stat-label">Duration</span>
              </div>
              <div class="stat">
                <span class="stat-number">{{ assessment.submissions_count || 0 }}</span>
                <span class="stat-label">Submissions</span>
              </div>
            </div>

            <div class="assessment-actions-row">
              <button @click="viewResults(assessment)" class="action-btn-primary">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M9,17H7V10H9V17M13,17H11V7H13V17M17,17H15V13H17V17M19.5,3.5L18,2L16.5,3.5L15,2L13.5,3.5L12,2L10.5,3.5L9,2L7.5,3.5L6,2L4.5,3.5L3,2V22L4.5,20.5L6,22L7.5,20.5L9,22L10.5,20.5L12,22L13.5,20.5L15,22L16.5,20.5L18,22L19.5,20.5L21,22V2L19.5,3.5Z" />
                </svg>
                View Results
              </button>
              <button @click="previewAssessment(assessment)" class="action-btn-secondary">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M12,9A3,3 0 0,0 9,12A3,3 0 0,0 12,15A3,3 0 0,0 15,12A3,3 0 0,0 12,9M12,17A5,5 0 0,1 7,12A5,5 0 0,1 12,7A5,5 0 0,1 17,12A5,5 0 0,1 12,17M12,4.5C7,4.5 2.73,7.61 1,12C2.73,16.39 7,19.5 12,19.5C17,19.5 21.27,16.39 23,12C21.27,7.61 17,4.5 12,4.5Z" />
                </svg>
                Preview
              </button>
            </div>
          </div>
        </div>
      </div>

      <div v-else class="empty-state">
        <div class="empty-icon">
          <svg width="64" height="64" viewBox="0 0 24 24" fill="currentColor">
            <path d="M14,2H6A2,2 0 0,0 4,4V20A2,2 0 0,0 6,22H18A2,2 0 0,0 20,20V8L14,2M18,20H6V4H13V9H18V20Z" />
          </svg>
        </div>
        <h3>No {{ activeFilter === 'all' ? '' : activeFilter }} assessments found</h3>
        <p>{{ getEmptyStateMessage() }}</p>
        <button @click="showCreateModal = true" class="create-first-btn">
          Create Your First Assessment
        </button>
      </div>
    </div>

    <!-- Loading State -->
    <div v-if="isLoading" class="loading-state">
      <div class="loading-spinner"></div>
      <p>{{ loadingMessage }}</p>
    </div>

    <!-- Create/Edit Assessment Modal -->
    <div v-if="showCreateModal" class="modal-overlay" @click="closeModal">
      <div class="modal-content" @click.stop>
        <div class="modal-header">
          <h2>{{ isEditing ? 'Edit Assessment' : 'Create New Assessment' }}</h2>
          <button @click="closeModal" class="close-btn">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
              <path d="M19,6.41L17.59,5L12,10.59L6.41,5L5,6.41L10.59,12L5,17.59L6.41,19L12,13.41L17.59,19L19,17.59L13.41,12L19,6.41Z" />
            </svg>
          </button>
        </div>

        <form @submit.prevent="saveAssessment" class="assessment-form">
          <div class="form-group">
            <label for="title">Assessment Title *</label>
            <input
              id="title"
              v-model="formData.title"
              type="text"
              placeholder="e.g., Chapter 1 Quiz, Midterm Exam"
              required
            />
          </div>

          <div class="form-row">
            <div class="form-group">
              <label for="type">Type *</label>
              <select id="type" v-model="formData.type" required>
                <option value="quiz">Quiz</option>
                <option value="exam">Exam</option>
                <option value="assignment">Assignment</option>
                <option value="project">Project</option>
                <option value="homework">Homework</option>
              </select>
            </div>

            <div class="form-group">
              <label for="total_points">Total Points</label>
              <input
                id="total_points"
                v-model="formData.total_points"
                type="number"
                min="1"
                placeholder="100"
              />
            </div>
          </div>

          <div class="form-row">
            <div class="form-group">
              <label for="due_date">Due Date *</label>
              <input
                id="due_date"
                v-model="formData.due_date"
                type="datetime-local"
                required
              />
            </div>

            <div class="form-group">
              <label for="duration">Duration (minutes)</label>
              <input
                id="duration"
                v-model="formData.duration"
                type="number"
                min="1"
                placeholder="60"
              />
            </div>
          </div>

          <div class="form-group">
            <label for="description">Description</label>
            <textarea
              id="description"
              v-model="formData.description"
              rows="4"
              placeholder="Describe the assessment..."
            ></textarea>
          </div>

          <div class="modal-actions">
            <button type="button" @click="closeModal" class="btn-secondary">Cancel</button>
            <button type="submit" class="btn-primary" :disabled="!formData.title || !formData.due_date">
              {{ isEditing ? 'Update Assessment' : 'Create Assessment' }}
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { supabase } from '../../supabase.js'
import { useDarkMode } from '../../composables/useDarkMode.js'

const { isDarkMode, toggleDarkMode } = useDarkMode()
const route = useRoute()
const router = useRouter()

// Reactive data
const assessments = ref([])
const isLoading = ref(false)
const loadingMessage = ref('Loading assessments...')
const showCreateModal = ref(false)
const isEditing = ref(false)
const currentAssessmentId = ref(null)
const activeFilter = ref('all')

// Subject and section info from route
const subjectInfo = ref({
  subjectId: route.params.subjectId,
  sectionId: route.params.sectionId,
  subjectName: route.query.subjectName,
  sectionName: route.query.sectionName,
  gradeLevel: route.query.gradeLevel
})

// Form data
const formData = ref({
  title: '',
  type: 'quiz',
  description: '',
  due_date: '',
  total_points: 100,
  duration: 60
})

// Filter options
const filters = ref([
  {
    key: 'all',
    label: 'All',
    icon: 'M9,17H7V10H9V17M13,17H11V7H13V17M17,17H15V13H17V17M19.5,3.5L18,2L16.5,3.5L15,2L13.5,3.5L12,2L10.5,3.5L9,2L7.5,3.5L6,2L4.5,3.5L3,2V22L4.5,20.5L6,22L7.5,20.5L9,22L10.5,20.5L12,22L13.5,20.5L15,22L16.5,20.5L18,22L19.5,20.5L21,22V2L19.5,3.5Z'
  },
  {
    key: 'upcoming',
    label: 'Upcoming',
    icon: 'M15,13H16.5V15.82L18.94,17.23L18.19,18.53L15,16.69V13M19,8H5V19H9.67C9.24,18.09 9,17.07 9,16A7,7 0 0,1 16,9C17.07,9 18.09,9.24 19,9.67V8M5,21C3.89,21 3,20.1 3,19V5C3,3.89 3.89,3 5,3H6V1H8V3H16V1H18V3H19A2,2 0 0,1 21,5V11.1C22.24,12.36 23,14.09 23,16A7,7 0 0,1 16,23C14.09,23 12.36,22.24 11.1,21H5M16,11.15A4.85,4.85 0 0,0 11.15,16C11.15,18.68 13.32,20.85 16,20.85A4.85,4.85 0 0,0 20.85,16C20.85,13.32 18.68,11.15 16,11.15Z'
  },
  {
    key: 'ongoing',
    label: 'Ongoing',
    icon: 'M12,20A8,8 0 0,1 4,12A8,8 0 0,1 12,4A8,8 0 0,1 20,12A8,8 0 0,1 12,20M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2M12.5,7V12.25L17,14.92L16.25,16.15L11,13V7H12.5Z'
  },
  {
    key: 'past',
    label: 'Past',
    icon: 'M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2M16.2,16.2L11,13V7H12.5V12.2L17,14.9L16.2,16.2Z'
  }
])

// Computed properties
const filteredAssessments = computed(() => {
  const now = new Date()
  
  if (activeFilter.value === 'all') return assessments.value
  
  return assessments.value.filter(assessment => {
    const dueDate = new Date(assessment.due_date)
    
    switch (activeFilter.value) {
      case 'upcoming':
        return dueDate > now && assessment.status !== 'completed'
      case 'ongoing':
        return assessment.status === 'active' || assessment.status === 'in_progress'
      case 'past':
        return dueDate < now || assessment.status === 'completed'
      default:
        return true
    }
  })
})

// Methods
const setActiveFilter = (filter) => {
  activeFilter.value = filter
}

const getFilteredCount = (filter) => {
  const now = new Date()
  
  if (filter === 'all') return assessments.value.length
  
  return assessments.value.filter(assessment => {
    const dueDate = new Date(assessment.due_date)
    
    switch (filter) {
      case 'upcoming':
        return dueDate > now && assessment.status !== 'completed'
      case 'ongoing':
        return assessment.status === 'active' || assessment.status === 'in_progress'
      case 'past':
        return dueDate < now || assessment.status === 'completed'
      default:
        return true
    }
  }).length
}

const getEmptyStateMessage = () => {
  switch (activeFilter.value) {
    case 'upcoming':
      return 'No upcoming assessments scheduled'
    case 'ongoing':
      return 'No assessments currently active'
    case 'past':
      return 'No past assessments found'
    default:
      return 'Create your first assessment to get started'
  }
}

const formatDate = (dateString) => {
  const date = new Date(dateString)
  return date.toLocaleDateString('en-US', {
    weekday: 'short',
    year: 'numeric',
    month: 'short',
    day: 'numeric',
    hour: '2-digit',
    minute: '2-digit'
  })
}

const fetchAssessments = async () => {
  try {
    isLoading.value = true
    loadingMessage.value = 'Loading assessments...'

    const { data, error } = await supabase
      .from('assessments')
      .select('*')
      .eq('section_id', subjectInfo.value.sectionId)
      .order('due_date', { ascending: false })

    if (error) {
      console.error('Error fetching assessments:', error)
      throw error
    }

    assessments.value = data || []
    console.log('Assessments loaded:', assessments.value.length)
  } catch (error) {
    console.error('Error in fetchAssessments:', error)
    alert(`Error loading assessments: ${error.message}`)
  } finally {
    isLoading.value = false
  }
}

const saveAssessment = async () => {
  try {
    if (!formData.value.title || !formData.value.due_date) return

    isLoading.value = true
    loadingMessage.value = isEditing.value ? 'Updating assessment...' : 'Creating assessment...'

    const assessmentData = {
      title: formData.value.title,
      type: formData.value.type,
      description: formData.value.description,
      due_date: formData.value.due_date,
      total_points: formData.value.total_points || null,
      duration: formData.value.duration || null,
      section_id: subjectInfo.value.sectionId,
      subject_id: subjectInfo.value.subjectId,
      status: 'draft'
    }

    let result
    if (isEditing.value) {
      result = await supabase
        .from('assessments')
        .update(assessmentData)
        .eq('id', currentAssessmentId.value)
    } else {
      result = await supabase
        .from('assessments')
        .insert([assessmentData])
    }

    if (result.error) {
      console.error('Error saving assessment:', result.error)
      throw result.error
    }

    await fetchAssessments()
    closeModal()
    alert(`Assessment ${isEditing.value ? 'updated' : 'created'} successfully!`)
  } catch (error) {
    console.error('Error saving assessment:', error)
    alert(`Error ${isEditing.value ? 'updating' : 'creating'} assessment: ${error.message}`)
  } finally {
    isLoading.value = false
  }
}

const editAssessment = (assessment) => {
  isEditing.value = true
  currentAssessmentId.value = assessment.id
  formData.value = {
    title: assessment.title,
    type: assessment.type,
    description: assessment.description || '',
    due_date: assessment.due_date,
    total_points: assessment.total_points || 100,
    duration: assessment.duration || 60
  }
  showCreateModal.value = true
}

const deleteAssessment = async (assessmentId) => {
  try {
    const assessment = assessments.value.find(a => a.id === assessmentId)
    if (!confirm(`Are you sure you want to delete "${assessment?.title}"?\n\nThis action cannot be undone.`)) {
      return
    }

    isLoading.value = true
    loadingMessage.value = 'Deleting assessment...'

    const { error } = await supabase
      .from('assessments')
      .delete()
      .eq('id', assessmentId)

    if (error) {
      console.error('Error deleting assessment:', error)
      throw error
    }

    await fetchAssessments()
    alert('Assessment deleted successfully!')
  } catch (error) {
    console.error('Error deleting assessment:', error)
    alert(`Error deleting assessment: ${error.message}`)
  } finally {
    isLoading.value = false
  }
}

const closeModal = () => {
  showCreateModal.value = false
  isEditing.value = false
  currentAssessmentId.value = null
  formData.value = {
    title: '',
    type: 'quiz',
    description: '',
    due_date: '',
    total_points: 100,
    duration: 60
  }
}

const viewResults = (assessment) => {
  // Navigate to assessment results page
  router.push({
    name: 'AssessmentResults',
    params: { assessmentId: assessment.id }
  })
}

const previewAssessment = (assessment) => {
  // Navigate to assessment preview page
  router.push({
    name: 'AssessmentPreview',
    params: { assessmentId: assessment.id }
  })
}

// Lifecycle
onMounted(() => {
  fetchAssessments()
})
</script>

<style scoped>
.assessments-page {
  min-height: 100vh;
  background: var(--bg-primary);
  padding: 2rem;
  color: var(--primary-text-color);
  transition: all 0.3s ease;
}

/* Header Styles */
.section-header-card {
  margin-bottom: 2rem;
  position: relative;
  overflow: hidden;
  background: rgba(248, 250, 252, 0.9);
  backdrop-filter: blur(20px);
  border: 1px solid rgba(16, 185, 129, 0.1);
  border-radius: 24px;
  padding: 2rem;
  box-shadow: 0 20px 40px rgba(16, 185, 129, 0.1);
  transition: all 0.3s ease;
}

.header-bg-decoration {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 100%;
  background: linear-gradient(135deg, rgba(16, 185, 129, 0.05) 0%, rgba(52, 211, 153, 0.03) 100%);
  border-radius: 24px;
}

.section-header-card:hover {
  box-shadow: 
    0 32px 64px rgba(16, 185, 129, 0.15),
    0 16px 32px rgba(16, 185, 129, 0.1),
    inset 0 1px 0 rgba(255, 255, 255, 0.1);
  transform: translateY(-2px);
}

.floating-shapes {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  overflow: hidden;
  pointer-events: none;
}

.shape {
  position: absolute;
  border-radius: 50%;
  background: linear-gradient(135deg, rgba(16, 185, 129, 0.1) 0%, rgba(52, 211, 153, 0.05) 100%);
}

.shape-1 {
  width: 120px;
  height: 120px;
  top: 20%;
  right: 10%;
  animation: float 6s ease-in-out infinite;
}

.shape-2 {
  width: 80px;
  height: 80px;
  top: 60%;
  right: 20%;
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
  0%, 100% { transform: translateY(0px) rotate(0deg); }
  50% { transform: translateY(-20px) rotate(180deg); }
}

.section-header-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  position: relative;
  z-index: 2;
}

.section-header-left {
  display: flex;
  align-items: center;
  gap: 1.5rem;
}

.section-header-icon {
  background: linear-gradient(135deg, #10b981 0%, #34d399 100%);
  color: white;
  padding: 1rem;
  border-radius: 20px;
  box-shadow: 0 8px 24px rgba(16, 185, 129, 0.3);
}

.section-header-title {
  color: #10b981;
  font-size: 2.5rem;
  font-weight: 800;
  margin-bottom: 0.5rem;
  text-shadow: 0 2px 4px rgba(16, 185, 129, 0.1);
  transition: all 0.3s ease;
}

.section-header-subtitle {
  color: #059669;
  font-size: 1.2rem;
  font-weight: 600;
  margin-bottom: 0.3rem;
}

.section-header-description {
  color: #6b7280;
  font-size: 1rem;
  margin: 0;
}

.header-actions {
  display: flex;
  gap: 1rem;
}

.dark-mode-toggle {
  padding: 0.75rem;
  background: rgba(255, 255, 255, 0.9);
  border: 1px solid rgba(16, 185, 129, 0.2);
  border-radius: 12px;
  cursor: pointer;
  color: #10b981;
  transition: all 0.3s ease;
  box-shadow: 0 4px 12px rgba(16, 185, 129, 0.1);
}

.dark-mode-toggle:hover {
  background: rgba(16, 185, 129, 0.1);
  border-color: #10b981;
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(16, 185, 129, 0.2);
}

.create-btn {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.75rem 1.5rem;
  background: linear-gradient(135deg, #10b981 0%, #34d399 100%);
  color: white;
  border: none;
  border-radius: 12px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 8px 24px rgba(16, 185, 129, 0.3);
}

.create-btn:hover {
  background: linear-gradient(135deg, #059669 0%, #10b981 100%);
  transform: translateY(-2px);
  box-shadow: 0 12px 32px rgba(16, 185, 129, 0.4);
}

/* Filter Tabs */
.filter-tabs {
  display: flex;
  gap: 1rem;
  margin-bottom: 2rem;
  flex-wrap: wrap;
}

.filter-tab {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1.5rem;
  background: rgba(255, 255, 255, 0.8);
  border: 1px solid rgba(16, 185, 129, 0.2);
  border-radius: 12px;
  cursor: pointer;
  transition: all 0.3s ease;
  color: #6b7280;
  font-weight: 500;
  backdrop-filter: blur(10px);
  box-shadow: 0 4px 12px rgba(16, 185, 129, 0.05);
}

.filter-tab:hover {
  background: rgba(16, 185, 129, 0.1);
  border-color: #10b981;
}

.filter-tab.active {
  background: linear-gradient(135deg, #10b981 0%, #34d399 100%);
  color: white;
  border-color: #10b981;
  box-shadow: 0 4px 12px rgba(16, 185, 129, 0.3);
}

.filter-tab .count {
  background: rgba(255, 255, 255, 0.2);
  padding: 0.2rem 0.5rem;
  border-radius: 8px;
  font-size: 0.8rem;
  font-weight: 600;
}

.filter-tab.active .count {
  background: rgba(255, 255, 255, 0.3);
}

/* Assessments Grid */
.assessments-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
  gap: 2rem;
}

.assessment-card {
  background: rgba(255, 255, 255, 0.95);
  border-radius: 20px;
  padding: 2rem;
  box-shadow: 0 8px 32px rgba(16, 185, 129, 0.1);
  border: 1px solid rgba(16, 185, 129, 0.1);
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
}

.assessment-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 4px;
  background: linear-gradient(90deg, #10b981, #059669, #047857);
  border-radius: 20px 20px 0 0;
}

.assessment-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 16px 48px rgba(16, 185, 129, 0.2);
  border-color: rgba(16, 185, 129, 0.3);
}

.assessment-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 1.5rem;
}

.assessment-info h3 {
  color: #10b981;
  font-size: 1.5rem;
  font-weight: 700;
  margin-bottom: 0.5rem;
}

.assessment-type {
  background: linear-gradient(135deg, #10b981 0%, #059669 100%);
  color: white;
  padding: 0.3rem 1rem;
  border-radius: 20px;
  font-size: 0.85rem;
  font-weight: 600;
  display: inline-block;
  margin-bottom: 0.5rem;
  text-transform: capitalize;
}

.assessment-meta {
  display: flex;
  gap: 1rem;
  align-items: center;
}

.date {
  color: #6b7280;
  font-size: 0.9rem;
}

.status {
  padding: 0.2rem 0.8rem;
  border-radius: 12px;
  font-size: 0.8rem;
  font-weight: 600;
  text-transform: capitalize;
}

.status.draft {
  background: rgba(107, 114, 128, 0.1);
  color: #6b7280;
}

.status.active {
  background: rgba(16, 185, 129, 0.1);
  color: #10b981;
}

.status.completed {
  background: rgba(99, 102, 241, 0.1);
  color: #6366f1;
}

.assessment-actions {
  display: flex;
  gap: 0.5rem;
}

.action-btn {
  padding: 0.6rem;
  border: none;
  border-radius: 12px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.action-btn.edit {
  background: rgba(16, 185, 129, 0.1);
  color: #10b981;
}

.action-btn.delete {
  background: rgba(239, 68, 68, 0.1);
  color: #ef4444;
}

.action-btn:hover {
  transform: scale(1.1);
}

.assessment-content .description {
  color: #6b7280;
  margin-bottom: 1.5rem;
  line-height: 1.6;
}

.assessment-stats {
  display: flex;
  gap: 1.5rem;
  margin-bottom: 1.5rem;
  padding: 1rem;
  background: rgba(251, 255, 228, 0.7);
  border-radius: 12px;
}

.stat {
  text-align: center;
  flex: 1;
}

.stat-number {
  display: block;
  font-size: 1.5rem;
  font-weight: 800;
  color: #10b981;
  margin-bottom: 0.25rem;
}

.stat-label {
  color: #6b7280;
  font-size: 0.8rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.assessment-actions-row {
  display: flex;
  gap: 1rem;
}

.action-btn-primary {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  padding: 0.75rem 1rem;
  background: linear-gradient(135deg, #10b981 0%, #34d399 100%);
  color: white;
  border: none;
  border-radius: 12px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
}

.action-btn-primary:hover {
  background: linear-gradient(135deg, #059669 0%, #10b981 100%);
  transform: translateY(-1px);
}

.action-btn-secondary {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  padding: 0.75rem 1rem;
  background: rgba(16, 185, 129, 0.1);
  color: #10b981;
  border: 1px solid rgba(16, 185, 129, 0.3);
  border-radius: 12px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
}

.action-btn-secondary:hover {
  background: rgba(16, 185, 129, 0.2);
  transform: translateY(-1px);
}

/* Empty State */
.empty-state {
  text-align: center;
  padding: 4rem 2rem;
  color: #6b7280;
}

.empty-icon {
  color: #d1d5db;
  margin-bottom: 2rem;
}

.empty-state h3 {
  font-size: 1.5rem;
  font-weight: 600;
  margin-bottom: 1rem;
  color: #374151;
}

.empty-state p {
  font-size: 1.1rem;
  margin-bottom: 2rem;
}

.create-first-btn {
  padding: 1rem 2rem;
  background: linear-gradient(135deg, #10b981 0%, #34d399 100%);
  color: white;
  border: none;
  border-radius: 12px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 8px 24px rgba(16, 185, 129, 0.3);
}

.create-first-btn:hover {
  background: linear-gradient(135deg, #059669 0%, #10b981 100%);
  transform: translateY(-2px);
  box-shadow: 0 12px 32px rgba(16, 185, 129, 0.4);
}

/* Loading State */
.loading-state {
  text-align: center;
  padding: 4rem 2rem;
  color: #6b7280;
}

.loading-spinner {
  width: 48px;
  height: 48px;
  border: 4px solid rgba(16, 185, 129, 0.2);
  border-top: 4px solid #10b981;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin: 0 auto 1rem;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

/* Modal Styles */
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
  padding: 2rem;
}

.modal-content {
  background: white;
  border-radius: 20px;
  padding: 0;
  max-width: 600px;
  width: 100%;
  max-height: 90vh;
  overflow-y: auto;
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.2);
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 2rem 2rem 0;
  margin-bottom: 2rem;
}

.modal-header h2 {
  color: #10b981;
  font-size: 1.8rem;
  font-weight: 700;
  margin: 0;
}

.close-btn {
  padding: 0.5rem;
  background: rgba(239, 68, 68, 0.1);
  color: #ef4444;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.close-btn:hover {
  background: rgba(239, 68, 68, 0.2);
  transform: scale(1.1);
}

.assessment-form {
  padding: 0 2rem 2rem;
}

.form-group {
  margin-bottom: 1.5rem;
}

.form-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
}

.form-group label {
  display: block;
  color: #374151;
  font-weight: 600;
  margin-bottom: 0.5rem;
}

.form-group input,
.form-group select,
.form-group textarea {
  width: 100%;
  padding: 0.75rem;
  border: 2px solid #e5e7eb;
  border-radius: 8px;
  font-size: 1rem;
  transition: all 0.3s ease;
}

.form-group input:focus,
.form-group select:focus,
.form-group textarea:focus {
  outline: none;
  border-color: #10b981;
  box-shadow: 0 0 0 3px rgba(16, 185, 129, 0.1);
}

.modal-actions {
  display: flex;
  gap: 1rem;
  justify-content: flex-end;
  margin-top: 2rem;
}

.btn-secondary {
  padding: 0.75rem 1.5rem;
  background: rgba(107, 114, 128, 0.1);
  color: #6b7280;
  border: 1px solid #d1d5db;
  border-radius: 8px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
}

.btn-secondary:hover {
  background: rgba(107, 114, 128, 0.2);
}

.btn-primary {
  padding: 0.75rem 1.5rem;
  background: linear-gradient(135deg, #10b981 0%, #34d399 100%);
  color: white;
  border: none;
  border-radius: 8px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
}

.btn-primary:hover:not(:disabled) {
  background: linear-gradient(135deg, #059669 0%, #10b981 100%);
  transform: translateY(-1px);
}

.btn-primary:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

/* Dark Mode */
.assessments-page.dark-mode {
  background: var(--bg-primary);
  color: var(--primary-text-color);
}

.dark-mode .section-header-card {
  background: var(--bg-secondary);
  border: 1px solid var(--border-color);
  backdrop-filter: blur(20px);
}

.dark-mode .section-header-card:hover {
  box-shadow: 
    0 24px 48px rgba(0, 0, 0, 0.4),
    0 12px 24px rgba(0, 0, 0, 0.3),
    inset 0 1px 0 rgba(255, 255, 255, 0.1);
}

.dark-mode .section-header-title {
  color: var(--primary-text-color);
}

.dark-mode .section-header-subtitle {
  color: var(--secondary-text-color);
}

.dark-mode .section-header-description {
  color: var(--text-muted);
}

.dark-mode .dark-mode-toggle {
  background: var(--bg-card);
  border-color: var(--border-color);
  color: var(--accent-color);
}

.dark-mode .dark-mode-toggle:hover {
  border-color: var(--accent-color);
  box-shadow: 0 8px 24px rgba(95, 179, 160, 0.2);
}

.dark-mode .create-btn {
  background: linear-gradient(135deg, var(--accent-color) 0%, #4a9b87 100%);
  box-shadow: 0 8px 24px rgba(95, 179, 160, 0.3);
}

.dark-mode .create-btn:hover {
  box-shadow: 0 12px 32px rgba(95, 179, 160, 0.4);
}

.dark-mode .filter-tab {
  background: var(--bg-card);
  border-color: var(--border-color);
  color: var(--secondary-text-color);
  backdrop-filter: blur(20px);
}

.dark-mode .filter-tab:hover {
  background: rgba(95, 179, 160, 0.1);
  border-color: var(--accent-color);
}

.dark-mode .filter-tab.active {
  background: linear-gradient(135deg, var(--accent-color) 0%, #4a9b87 100%);
  color: white;
  border-color: var(--accent-color);
  box-shadow: 0 4px 12px rgba(95, 179, 160, 0.3);
}

.dark-mode .assessment-card {
  background: var(--card-background);
  border: 1px solid var(--card-border-color);
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
}

.dark-mode .assessment-card:hover {
  box-shadow: 0 16px 48px rgba(0, 0, 0, 0.4);
  border-color: var(--accent-color);
}

.dark-mode .assessment-info h3 {
  color: var(--primary-text-color);
}

.dark-mode .assessment-type {
  background: linear-gradient(135deg, var(--accent-color) 0%, #4a9b87 100%);
}

.dark-mode .assessment-content .description {
  color: var(--secondary-text-color);
}

.dark-mode .assessment-stats {
  background: var(--bg-accent);
}

.dark-mode .stat-number {
  color: var(--accent-color);
}

.dark-mode .stat-label {
  color: var(--secondary-text-color);
}

.dark-mode .date {
  color: var(--text-muted);
}

.dark-mode .action-btn.edit {
  background: rgba(59, 130, 246, 0.2);
  color: #60a5fa;
}

.dark-mode .action-btn.delete {
  background: rgba(239, 68, 68, 0.2);
  color: #f87171;
}

.dark-mode .action-btn-primary {
  background: linear-gradient(135deg, var(--accent-color) 0%, #4a9b87 100%);
}

.dark-mode .action-btn-secondary {
  background: rgba(95, 179, 160, 0.1);
  color: var(--accent-color);
  border-color: rgba(95, 179, 160, 0.3);
}

.dark-mode .action-btn-secondary:hover {
  background: rgba(95, 179, 160, 0.2);
}

.dark-mode .empty-state {
  color: var(--text-muted);
}

.dark-mode .empty-icon {
  color: var(--text-muted);
}

.dark-mode .empty-state h3 {
  color: var(--secondary-text-color);
}

.dark-mode .create-first-btn {
  background: linear-gradient(135deg, var(--accent-color) 0%, #4a9b87 100%);
  box-shadow: 0 8px 24px rgba(95, 179, 160, 0.3);
}

.dark-mode .create-first-btn:hover {
  box-shadow: 0 12px 32px rgba(95, 179, 160, 0.4);
}

.dark-mode .loading-state {
  color: var(--text-muted);
}

.dark-mode .loading-spinner {
  border-color: rgba(95, 179, 160, 0.2);
  border-top-color: var(--accent-color);
}

.dark-mode .modal-overlay {
  background: rgba(0, 0, 0, 0.7);
}

.dark-mode .modal-content {
  background: var(--bg-secondary);
  color: var(--primary-text-color);
  border: 1px solid var(--border-color);
}

.dark-mode .modal-header h2 {
  color: var(--primary-text-color);
}

.dark-mode .close-btn {
  background: rgba(239, 68, 68, 0.2);
  color: #f87171;
}

.dark-mode .close-btn:hover {
  background: rgba(239, 68, 68, 0.3);
}

.dark-mode .form-group label {
  color: var(--primary-text-color);
}

.dark-mode .form-group input,
.dark-mode .form-group select,
.dark-mode .form-group textarea {
  background: var(--bg-card);
  border-color: var(--border-color);
  color: var(--primary-text-color);
}

.dark-mode .form-group input:focus,
.dark-mode .form-group select:focus,
.dark-mode .form-group textarea:focus {
  border-color: var(--accent-color);
  box-shadow: 0 0 0 3px rgba(95, 179, 160, 0.1);
}

.dark-mode .form-group input::placeholder,
.dark-mode .form-group textarea::placeholder {
  color: var(--text-muted);
}

.dark-mode .btn-secondary {
  background: rgba(107, 114, 128, 0.2);
  color: var(--secondary-text-color);
  border-color: var(--border-color);
}

.dark-mode .btn-secondary:hover {
  background: rgba(107, 114, 128, 0.3);
}

.dark-mode .btn-primary {
  background: linear-gradient(135deg, var(--accent-color) 0%, #4a9b87 100%);
}

.dark-mode .btn-primary:hover:not(:disabled) {
  background: linear-gradient(135deg, #4a9b87 0%, var(--accent-color) 100%);
}

/* Responsive */
@media (max-width: 768px) {
  .assessments-page {
    padding: 1rem;
  }
  
  .section-header-content {
    flex-direction: column;
    gap: 1.5rem;
    text-align: center;
  }
  
  .filter-tabs {
    justify-content: center;
  }
  
  .assessments-grid {
    grid-template-columns: 1fr;
  }
  
  .form-row {
    grid-template-columns: 1fr;
  }
}
</style>