<template>
  <div class="subjects-page">
    <div class="page-header">
      <div class="header-content">
        <h1>My Subjects</h1>
        <p class="header-subtitle">Create and manage your class subjects with multiple sections</p>
      </div>
      <button @click="showCreateModal = true" class="create-btn">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
          <path d="M19,13H13V19H11V13H5V11H11V5H13V11H19V13Z" />
        </svg>
        Create New Subject
      </button>
    </div>

    <div class="subjects-grid" v-if="subjects.length > 0">
      <div v-for="subject in subjects" :key="subject.id" class="subject-card">
        <div class="subject-header">
          <div class="subject-info">
            <h3>{{ subject.name }}</h3>
            <p class="grade-level">Grade {{ subject.grade_level }}</p>
          </div>
          <div class="subject-actions">
            <button @click="editSubject(subject)" class="action-btn edit" title="Edit Subject">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                <path d="M20.71,7.04C21.1,6.65 21.1,6 20.71,5.63L18.37,3.29C18,2.9 17.35,2.9 16.96,3.29L15.12,5.12L18.87,8.87M3,17.25V21H6.75L17.81,9.93L14.06,6.18L3,17.25Z" />
              </svg>
            </button>
            <button @click="deleteSubject(subject.id)" class="action-btn delete" title="Delete Subject">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                <path d="M19,4H15.5L14.5,3H9.5L8.5,4H5V6H19M6,19A2,2 0 0,0 8,21H16A2,2 0 0,0 18,19V7H6V19Z" />
              </svg>
            </button>
          </div>
        </div>

        <div class="subject-stats">
          <div class="stat">
            <span class="stat-number">{{ subject.sections?.length || 0 }}</span>
            <span class="stat-label">Sections</span>
          </div>
          <div class="stat">
            <span class="stat-number">{{ getTotalStudents(subject) }}</span>
            <span class="stat-label">Students</span>
          </div>
          <div class="stat">
            <span class="stat-number">{{ subject.grade_level }}</span>
            <span class="stat-label">Grade</span>
          </div>
        </div>

        <!-- Sections List with Section Codes -->
        <div class="sections-list" v-if="subject.sections && subject.sections.length > 0">
          <h4>Sections & Codes:</h4>
          <div class="sections">
            <div v-for="section in subject.sections" :key="section.id" class="section-item enhanced-section">
              <div class="section-info">
                <div class="section-header-info">
                  <span class="section-name">{{ section.name }}</span>
                  <div class="section-code-display">
                    <span class="code-label">Section Code:</span>
                    <span class="section-code">{{ section.section_code }}</span>
                    <button @click="copyCode(section.section_code, section.id)" class="copy-code-btn">
                      <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor">
                        <path d="M19,21H8V7H19M19,5H8A2,2 0 0,0 6,7V21A2,2 0 0,0 8,23H19A2,2 0 0,0 21,21V7A2,2 0 0,0 19,5M16,1H4A2,2 0 0,0 2,3V17H4V3H16V1Z" />
                      </svg>
                      {{ copiedCodeId === section.id ? 'Copied!' : 'Copy' }}
                    </button>
                  </div>
                </div>
                <div class="section-stats-info">
                  <span class="student-count">{{ section.student_count || 0 }} students enrolled</span>
                </div>
                
                <!-- Section Action Buttons -->
                <div class="section-actions">
                  <button 
                    @click="navigateToCreateQuiz(subject, section)"
                    class="section-action-btn create-quiz"
                    title="Create Quiz/Assessment"
                  >
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                      <path d="M14,2H6A2,2 0 0,0 4,4V20A2,2 0 0,0 6,22H18A2,2 0 0,0 20,20V8L14,2M18,20H6V4H13V9H18V20Z" />
                    </svg>
                    Create Quiz
                  </button>
                  
                  <button 
                    @click="viewQuizzes(subject, section)"
                    class="section-action-btn view-quizzes"
                    title="View Past Quizzes"
                  >
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                      <path d="M13,9V3.5L18.5,9M6,2C4.89,2 4,2.89 4,4V20A2,2 0 0,0 6,22H18A2,2 0 0,0 20,20V8L14,2H6Z" />
                    </svg>
                    View Quizzes
                  </button>
                  
                  <button 
                    @click="manageGrades(subject, section)"
                    class="section-action-btn manage-grades"
                    title="Grade Management"
                  >
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                      <path d="M19,3H5C3.9,3 3,3.9 3,5V19C3,20.1 3.9,21 5,21H19C20.1,21 21,20.1 21,19V5C21,3.9 20.1,3 19,3M19,19H5V5H19V19M17,12H7V10H17V12M15,16H7V14H15V16M17,8H7V6H17V8Z" />
                    </svg>
                    Grades
                  </button>
                  
                  <button 
                    @click="generateReports(subject, section)"
                    class="section-action-btn generate-reports"
                    title="Generate Reports"
                  >
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                      <path d="M9,17H7V10H9V17M13,17H11V7H13V17M17,17H15V13H17V17M19.5,3.5L18,2L16.5,3.5L15,2L13.5,3.5L12,2L10.5,3.5L9,2L7.5,3.5L6,2L4.5,3.5L3,2V22L4.5,20.5L6,22L7.5,20.5L9,22L10.5,20.5L12,22L13.5,20.5L15,22L16.5,20.5L18,22L19.5,20.5L21,22V2L19.5,3.5Z" />
                    </svg>
                    Reports
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div v-else class="empty-state">
      <div class="empty-icon">
        <svg width="64" height="64" viewBox="0 0 24 24" fill="currentColor">
          <path d="M12,3L1,9L12,15L21,10.09V17H23V9M5,13.18V17.18L12,21L19,17.18V13.18L12,17L5,13.18Z" />
        </svg>
      </div>
      <h3>No Subjects Created Yet</h3>
      <p>Create your first subject to start managing your classes and student sections</p>
      <button @click="showCreateModal = true" class="create-first-btn">
        Create Your First Subject
      </button>
    </div>

    <!-- Create/Edit Subject Modal -->
    <div v-if="showCreateModal" class="modal-overlay" @click="closeModal">
      <div class="modal-content" @click.stop>
        <div class="modal-header">
          <h2>{{ isEditing ? 'Edit Subject' : 'Create New Subject' }}</h2>
          <button @click="closeModal" class="close-btn">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
              <path d="M19,6.41L17.59,5L12,10.59L6.41,5L5,6.41L10.59,12L5,17.59L6.41,19L12,13.41L17.59,19L19,17.59L13.41,12L19,6.41Z" />
            </svg>
          </button>
        </div>

        <form @submit.prevent="currentStep === 1 ? nextStep() : saveSubject()" class="subject-form">
          <!-- Step 1: Basic Information -->
          <div v-if="currentStep === 1" class="step-content">
            <h3 class="step-title">Step 1: Subject Information</h3>
            
            <div class="form-group">
              <label for="subjectName">Subject Name *</label>
              <input
                id="subjectName"
                v-model="formData.name"
                type="text"
                placeholder="e.g., English, Mathematics, Science"
                required
              />
            </div>

            <div class="form-group">
              <label for="gradeLevel">Grade Level *</label>
              <select id="gradeLevel" v-model="formData.grade_level" required>
                <option value="">Select Grade Level</option>
                <option value="7">Grade 7</option>
                <option value="8">Grade 8</option>
                <option value="9">Grade 9</option>
                <option value="10">Grade 10</option>
                <option value="11">Grade 11</option>
                <option value="12">Grade 12</option>
              </select>
            </div>

            <div class="form-group">
              <label for="numberOfSections">Number of Sections *</label>
              <select id="numberOfSections" v-model="formData.number_of_sections" required @change="generateSections">
                <option value="">Select Number of Sections</option>
                <option v-for="n in 10" :key="n" :value="n">{{ n }} Section{{ n > 1 ? 's' : '' }}</option>
              </select>
            </div>

            <div class="modal-actions">
              <button type="button" @click="closeModal" class="cancel-btn">Cancel</button>
              <button type="submit" :disabled="!canProceedToStep2" class="next-btn">
                Next: Setup Sections
                <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M4,11V13H16L10.5,18.5L11.92,19.92L19.84,12L11.92,4.08L10.5,5.5L16,11H4Z" />
                </svg>
              </button>
            </div>
          </div>

          <!-- Step 2: Section Setup -->
          <div v-if="currentStep === 2" class="step-content">
            <h3 class="step-title">Step 2: Setup Sections</h3>
            <p class="step-subtitle">Customize section names and unique codes will be generated</p>

            <div class="sections-setup">
              <div v-for="(section, index) in formData.sections" :key="index" class="section-setup-item">
                <div class="section-number">{{ index + 1 }}</div>
                <div class="section-input">
                  <label :for="`section-${index}`">Section {{ index + 1 }} Name</label>
                  <input
                    :id="`section-${index}`"
                    v-model="section.name"
                    type="text"
                    :placeholder="`Section ${index + 1}`"
                    required
                  />
                  <small class="section-code-preview">Code will be: {{ generateSectionCode(section.name || `Section ${index + 1}`, index) }}</small>
                </div>
              </div>
            </div>

            <div class="modal-actions">
              <button type="button" @click="currentStep = 1" class="back-btn">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M20,11V13H8L13.5,18.5L12.08,19.92L4.16,12L12.08,4.08L13.5,5.5L8,11H20Z" />
                </svg>
                Back
              </button>
              <button type="submit" :disabled="isLoading" class="save-btn">
                {{ isLoading ? 'Creating...' : (isEditing ? 'Update Subject' : 'Create Subject') }}
              </button>
            </div>
          </div>
        </form>
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
import { useRouter } from 'vue-router'
import { supabase } from '../../supabase.js'

// Router
const router = useRouter()

// State
const subjects = ref([])
const showCreateModal = ref(false)
const isEditing = ref(false)
const isLoading = ref(false)
const loadingMessage = ref('')
const currentSubjectId = ref(null)
const currentStep = ref(1)
const copiedCodeId = ref(null)

// Form data
const formData = ref({
  name: '',
  grade_level: '',
  number_of_sections: '',
  sections: []
})

// Computed
const canProceedToStep2 = computed(() => {
  return formData.value.name && formData.value.grade_level && formData.value.number_of_sections
})

// ASSESSMENT METHODS
const navigateToCreateQuiz = (subject, section) => {
  router.push({
    name: 'CreateQuiz',
    params: {
      subjectId: subject.id,
      sectionId: section.id
    },
    query: {
      subjectName: subject.name,
      sectionName: section.name,
      gradeLevel: subject.grade_level,
      sectionCode: section.section_code
    }
  })
}

const viewQuizzes = (subject, section) => {
  alert(`View Quizzes for:\nSubject: ${subject.name}\nSection: ${section.name}\n\nThis feature will show all past quizzes for this section.`)
}

const manageGrades = (subject, section) => {
  alert(`Grade Management for:\nSubject: ${subject.name}\nSection: ${section.name}\n\nThis feature will show the gradebook for this section.`)
}

const generateReports = (subject, section) => {
  alert(`Generate Reports for:\nSubject: ${subject.name}\nSection: ${section.name}\n\nThis feature will show analytics and performance reports for this section.`)
}

// CORE METHODS
const fetchSubjects = async () => {
  try {
    const { data: { user } } = await supabase.auth.getUser()
    if (!user) {
      console.log('No user found')
      return
    }

    loadingMessage.value = 'Loading subjects...'
    isLoading.value = true

    const { data: subjectsData, error: subjectsError } = await supabase
      .from('subjects')
      .select(`
        *,
        sections(
          id,
          name,
          section_code,
          student_count,
          created_at
        )
      `)
      .eq('teacher_id', user.id)
      .order('created_at', { ascending: false })

    if (subjectsError) {
      console.error('Error fetching subjects:', subjectsError)
      if (subjectsError.code === 'PGRST116') {
        throw new Error('Subjects table does not exist. Please create the subjects table first.')
      }
      throw subjectsError
    }

    subjects.value = subjectsData || []
    console.log('Fetched subjects:', subjects.value)

  } catch (error) {
    console.error('Error in fetchSubjects:', error)
    alert(`Database Error: ${error.message}\n\nPlease ensure the subjects table is created in your Supabase database.`)
  } finally {
    isLoading.value = false
  }
}

const generateSections = () => {
  const numSections = parseInt(formData.value.number_of_sections)
  formData.value.sections = []
  
  for (let i = 1; i <= numSections; i++) {
    formData.value.sections.push({
      name: `Section ${i}`,
      section_code: ''
    })
  }
}

const generateSectionCode = (sectionName, index = 0) => {
  if (!formData.value.name || !formData.value.grade_level) return 'CODE-PREVIEW'
  
  const subjectPrefix = formData.value.name.substring(0, 3).toUpperCase().replace(/[^A-Z]/g, '') || 'SUB'
  const gradeLevel = formData.value.grade_level
  const cleanSectionName = sectionName.replace(/[^a-zA-Z0-9]/g, '').substring(0, 1).toUpperCase() || 'S'
  const timestamp = Date.now().toString().slice(-4)
  const indexSuffix = String(index + 1).padStart(2, '0')
  
  return `${subjectPrefix}${gradeLevel}-${cleanSectionName}${indexSuffix}${timestamp}`
}

const copyCode = async (code, codeId) => {
  try {
    await navigator.clipboard.writeText(code)
    copiedCodeId.value = codeId
    setTimeout(() => {
      copiedCodeId.value = null
    }, 2000)
  } catch (err) {
    console.error('Failed to copy code:', err)
    // Fallback for older browsers
    const textArea = document.createElement('textarea')
    textArea.value = code
    document.body.appendChild(textArea)
    textArea.select()
    document.execCommand('copy')
    document.body.removeChild(textArea)
    copiedCodeId.value = codeId
    setTimeout(() => {
      copiedCodeId.value = null
    }, 2000)
  }
}

const nextStep = () => {
  if (canProceedToStep2.value) {
    generateSections()
    currentStep.value = 2
  }
}

const saveSubject = async () => {
  isLoading.value = true
  loadingMessage.value = isEditing.value ? 'Updating subject...' : 'Creating subject...'

  try {
    const { data: { user } } = await supabase.auth.getUser()
    if (!user) {
      throw new Error('Please login to continue')
    }

    // Prepare subject data (remove class_code since we're not using it)
    const subjectData = {
      name: formData.value.name,
      grade_level: parseInt(formData.value.grade_level),
      teacher_id: user.id
    }

    let subjectId

    if (isEditing.value) {
      // Update existing subject
      const { data: updatedSubject, error: updateError } = await supabase
        .from('subjects')
        .update(subjectData)
        .eq('id', currentSubjectId.value)
        .select()
        .single()

      if (updateError) throw updateError
      subjectId = currentSubjectId.value

      // Delete existing sections for this subject
      const { error: deleteError } = await supabase
        .from('sections')
        .delete()
        .eq('class_id', subjectId)

      if (deleteError) throw deleteError

    } else {
      // Create new subject
      const { data: newSubject, error: insertError } = await supabase
        .from('subjects')
        .insert([subjectData])
        .select()
        .single()

      if (insertError) throw insertError
      subjectId = newSubject.id
    }

    // Create sections with unique section codes
    const sectionsToInsert = []
    const baseTimestamp = Date.now()
    const maxAttempts = 10
    
    for (let i = 0; i < formData.value.sections.length; i++) {
      const section = formData.value.sections[i]
      let sectionCode
      let isSectionUnique = false
      let sectionAttempts = 0

      // Ensure section code is unique
      while (!isSectionUnique && sectionAttempts < maxAttempts) {
        const subjectPrefix = formData.value.name.substring(0, 3).toUpperCase().replace(/[^A-Z]/g, '') || 'SUB'
        const gradeLevel = formData.value.grade_level
        const cleanSectionName = section.name.replace(/[^a-zA-Z0-9]/g, '').substring(0, 1).toUpperCase() || 'S'
        const uniqueTimestamp = (baseTimestamp + i + sectionAttempts).toString().slice(-5)
        const randomSuffix = Math.random().toString(36).substring(2, 3).toUpperCase()
        
        sectionCode = `${subjectPrefix}${gradeLevel}${cleanSectionName}${uniqueTimestamp}${randomSuffix}`
        
        // Check if section code already exists
        const { data: existingSection, error: sectionCheckError } = await supabase
          .from('sections')
          .select('section_code')
          .eq('section_code', sectionCode)
          .maybeSingle()

        if (sectionCheckError) {
          console.error('Error checking section code uniqueness:', sectionCheckError)
          throw sectionCheckError
        }

        if (!existingSection) {
          isSectionUnique = true
        }
        
        sectionAttempts++
      }

      if (!isSectionUnique) {
        throw new Error(`Could not generate unique section code for ${section.name}. Please try again.`)
      }

      sectionsToInsert.push({
        class_id: subjectId,
        name: section.name,
        section_code: sectionCode,
        student_count: 0
      })
    }

    // Insert all sections
    const { data: insertedSections, error: sectionsError } = await supabase
      .from('sections')
      .insert(sectionsToInsert)
      .select()

    if (sectionsError) throw sectionsError

    // Refresh subjects list
    await fetchSubjects()
    closeModal()

    // Show success message with all section codes
    const sectionCodes = insertedSections.map(s => `${s.name}: ${s.section_code}`).join('\n')
    alert(`Subject "${formData.value.name}" ${isEditing.value ? 'updated' : 'created'} successfully!\n\nSection Codes:\n${sectionCodes}\n\nShare these codes with your students to join their respective sections.`)

  } catch (error) {
    console.error('Error saving subject:', error)
    alert(`Error ${isEditing.value ? 'updating' : 'creating'} subject:\n\n${error.message}`)
  } finally {
    isLoading.value = false
  }
}

const editSubject = (subject) => {
  isEditing.value = true
  currentSubjectId.value = subject.id
  formData.value = {
    name: subject.name,
    grade_level: subject.grade_level.toString(),
    number_of_sections: subject.sections?.length.toString() || '1',
    sections: subject.sections?.map(s => ({ name: s.name, section_code: s.section_code })) || []
  }
  showCreateModal.value = true
  currentStep.value = 1
}

const deleteSubject = async (subjectId) => {
  const subject = subjects.value.find(s => s.id === subjectId)
  if (!confirm(`Are you sure you want to delete "${subject?.name}"?\n\nThis will permanently remove:\n• All sections (${subject?.sections?.length || 0} sections)\n• All enrolled students\n• All class data\n\nThis action cannot be undone.`)) {
    return
  }

  isLoading.value = true
  loadingMessage.value = 'Deleting subject...'

  try {
    const { error } = await supabase
      .from('subjects')
      .delete()
      .eq('id', subjectId)

    if (error) throw error

    await fetchSubjects()
    alert(`Subject "${subject?.name}" deleted successfully!`)
  } catch (error) {
    console.error('Error deleting subject:', error)
    alert(`Error deleting subject: ${error.message}`)
  } finally {
    isLoading.value = false
  }
}

const getTotalStudents = (subject) => {
  if (!subject.sections) return 0
  return subject.sections.reduce((total, section) => total + (section.student_count || 0), 0)
}

const closeModal = () => {
  showCreateModal.value = false
  isEditing.value = false
  currentSubjectId.value = null
  currentStep.value = 1
  formData.value = {
    name: '',
    grade_level: '',
    number_of_sections: '',
    sections: []
  }
}

// Lifecycle
onMounted(() => {
  fetchSubjects()
})
</script>

<style scoped>
/* Enhanced Section Styles */
.enhanced-section {
  background: white;
  border: 2px solid rgba(61, 141, 122, 0.1);
  border-radius: 16px;
  padding: 1.5rem;
  transition: all 0.3s ease;
  box-shadow: 0 2px 8px rgba(61, 141, 122, 0.05);
}

.enhanced-section:hover {
  border-color: rgba(61, 141, 122, 0.3);
  box-shadow: 0 8px 24px rgba(61, 141, 122, 0.15);
  transform: translateY(-2px);
}

.section-header-info {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
  margin-bottom: 1rem;
}

.section-code-display {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.75rem;
  background: rgba(61, 141, 122, 0.05);
  border-radius: 10px;
  border: 1px solid rgba(61, 141, 122, 0.1);
}

.code-label {
  font-weight: 600;
  color: #3D8D7A;
  font-size: 0.9rem;
}

.section-code {
  font-family: 'Courier New', monospace;
  font-weight: 700;
  color: #3D8D7A;
  font-size: 1.1rem;
  background: white;
  padding: 0.5rem 0.75rem;
  border-radius: 6px;
  border: 1px solid rgba(61, 141, 122, 0.2);
  flex: 1;
}

.copy-code-btn {
  background: #3D8D7A;
  color: white;
  border: none;
  padding: 0.5rem 0.75rem;
  border-radius: 6px;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 0.3rem;
  font-size: 0.8rem;
  font-weight: 600;
  transition: all 0.3s ease;
}

.copy-code-btn:hover {
  background: #2a6b5f;
  transform: scale(1.05);
}

.section-stats-info {
  margin-bottom: 1rem;
}

.section-actions {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
  gap: 0.75rem;
  margin-bottom: 1rem;
}

.section-action-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  padding: 0.75rem 1rem;
  border: none;
  border-radius: 10px;
  cursor: pointer;
  font-weight: 600;
  font-size: 0.85rem;
  transition: all 0.3s ease;
  text-align: center;
  min-height: 44px;
}

.create-quiz {
  background: linear-gradient(135deg, #10b981 0%, #34d399 100%);
  color: white;
}

.create-quiz:hover {
  background: linear-gradient(135deg, #059669 0%, #10b981 100%);
  transform: translateY(-1px);
  box-shadow: 0 6px 20px rgba(16, 185, 129, 0.4);
}

.view-quizzes {
  background: linear-gradient(135deg, #3b82f6 0%, #60a5fa 100%);
  color: white;
}

.view-quizzes:hover {
  background: linear-gradient(135deg, #2563eb 0%, #3b82f6 100%);
  transform: translateY(-1px);
  box-shadow: 0 6px 20px rgba(59, 130, 246, 0.4);
}

.manage-grades {
  background: linear-gradient(135deg, #f59e0b 0%, #fbbf24 100%);
  color: white;
}

.manage-grades:hover {
  background: linear-gradient(135deg, #d97706 0%, #f59e0b 100%);
  transform: translateY(-1px);
  box-shadow: 0 6px 20px rgba(245, 158, 11, 0.4);
}

.generate-reports {
  background: linear-gradient(135deg, #8b5cf6 0%, #a78bfa 100%);
  color: white;
}

.generate-reports:hover {
  background: linear-gradient(135deg, #7c3aed 0%, #8b5cf6 100%);
  transform: translateY(-1px);
  box-shadow: 0 6px 20px rgba(139, 92, 246, 0.4);
}

/* Base Styles */
.subjects-page {
  padding: 2rem;
  max-width: 1400px;
  margin: 0 auto;
}

.page-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 2rem;
  flex-wrap: wrap;
  gap: 1rem;
}

.header-content h1 {
  font-size: 2.5rem;
  font-weight: 800;
  color: #3D8D7A;
  margin-bottom: 0.5rem;
}

.header-subtitle {
  color: #666;
  font-size: 1.1rem;
}

.create-btn {
  background: linear-gradient(135deg, #3D8D7A 0%, #A3D1C6 100%);
  color: white;
  border: none;
  padding: 1rem 2rem;
  border-radius: 16px;
  font-weight: 600;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  transition: all 0.3s ease;
  font-size: 1rem;
}

.create-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 12px 32px rgba(61, 141, 122, 0.3);
}

.subjects-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(450px, 1fr));
  gap: 2rem;
}

.subject-card {
  background: rgba(255, 255, 255, 0.95);
  border-radius: 20px;
  padding: 2rem;
  box-shadow: 0 8px 32px rgba(61, 141, 122, 0.1);
  border: 1px solid rgba(61, 141, 122, 0.1);
  transition: all 0.3s ease;
}

.subject-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 16px 48px rgba(61, 141, 122, 0.2);
}

.subject-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 2rem;
}

.subject-info h3 {
  color: #3D8D7A;
  font-size: 1.5rem;
  font-weight: 700;
  margin-bottom: 0.5rem;
}

.grade-level {
  background: linear-gradient(135deg, #3D8D7A 0%, #A3D1C6 100%);
  color: white;
  padding: 0.3rem 1rem;
  border-radius: 20px;
  font-size: 0.85rem;
  font-weight: 600;
  display: inline-block;
  margin-bottom: 0.5rem;
}

.subject-actions {
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
  background: rgba(59, 130, 246, 0.1);
  color: #3b82f6;
}

.action-btn.delete {
  background: rgba(239, 68, 68, 0.1);
  color: #ef4444;
}

.action-btn:hover {
  transform: scale(1.1);
}

.subject-stats {
  display: flex;
  gap: 2rem;
  margin-bottom: 2rem;
  padding: 1.5rem;
  background: rgba(251, 255, 228, 0.7);
  border-radius: 16px;
}

.stat {
  text-align: center;
  flex: 1;
}

.stat-number {
  display: block;
  font-size: 2rem;
  font-weight: 800;
  color: #3D8D7A;
}

.stat-label {
  font-size: 0.85rem;
  color: #666;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  font-weight: 600;
}

.sections-list {
  margin-bottom: 1.5rem;
}

.sections-list h4 {
  color: #3D8D7A;
  margin-bottom: 1rem;
  font-size: 1.1rem;
  font-weight: 600;
}

.sections {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.section-item {
  width: 100%;
}

.section-name {
  font-weight: 700;
  color: #3D8D7A;
  font-size: 1.2rem;
  margin-bottom: 0.5rem;
}

.student-count {
  color: #666;
  font-size: 0.9rem;
  font-weight: 500;
}

.empty-state {
  text-align: center;
  padding: 4rem 2rem;
  background: rgba(255, 255, 255, 0.95);
  border-radius: 20px;
  box-shadow: 0 8px 32px rgba(61, 141, 122, 0.1);
}

.empty-icon {
  color: #A3D1C6;
  margin-bottom: 2rem;
}

.empty-state h3 {
  color: #3D8D7A;
  font-size: 2rem;
  margin-bottom: 1rem;
  font-weight: 700;
}

.empty-state p {
  color: #666;
  margin-bottom: 2rem;
  font-size: 1.1rem;
}

.create-first-btn {
  background: linear-gradient(135deg, #3D8D7A 0%, #A3D1C6 100%);
  color: white;
  border: none;
  padding: 1rem 2rem;
  border-radius: 16px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  font-size: 1rem;
}

.create-first-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 12px 32px rgba(61, 141, 122, 0.3);
}

/* Modal Styles */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.6);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
  padding: 2rem;
}

.modal-content {
  background: white;
  border-radius: 20px;
  max-width: 600px;
  width: 100%;
  max-height: 90vh;
  overflow-y: auto;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 2rem 2rem 1rem;
  border-bottom: 1px solid rgba(61, 141, 122, 0.1);
}

.modal-header h2 {
  color: #3D8D7A;
  font-size: 1.5rem;
  font-weight: 700;
}

.close-btn {
  background: none;
  border: none;
  color: #666;
  cursor: pointer;
  transition: all 0.3s ease;
  padding: 0.5rem;
  border-radius: 8px;
}

.close-btn:hover {
  color: #3D8D7A;
  background: rgba(61, 141, 122, 0.1);
}

.subject-form {
  padding: 2rem;
}

.step-content {
  min-height: 300px;
}

.step-title {
  color: #3D8D7A;
  font-size: 1.25rem;
  font-weight: 700;
  margin-bottom: 0.5rem;
}

.step-subtitle {
  color: #666;
  margin-bottom: 2rem;
}

.form-group {
  margin-bottom: 2rem;
}

.form-group label {
  display: block;
  margin-bottom: 0.75rem;
  color: #3D8D7A;
  font-weight: 600;
  font-size: 1rem;
}

.form-group input,
.form-group select {
  width: 100%;
  padding: 1rem;
  border: 2px solid rgba(61, 141, 122, 0.1);
  border-radius: 12px;
  font-size: 1rem;
  transition: all 0.3s ease;
}

.form-group input:focus,
.form-group select:focus {
  outline: none;
  border-color: #3D8D7A;
  box-shadow: 0 0 0 3px rgba(61, 141, 122, 0.1);
}

.sections-setup {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.section-setup-item {
  display: flex;
  align-items: flex-start;
  gap: 1rem;
  padding: 1.5rem;
  background: rgba(251, 255, 228, 0.5);
  border-radius: 12px;
  border: 1px solid rgba(61, 141, 122, 0.1);
}

.section-number {
  background: #3D8D7A;
  color: white;
  width: 32px;
  height: 32px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 600;
  flex-shrink: 0;
}

.section-input {
  flex: 1;
}

.section-input label {
  margin-bottom: 0.5rem;
  font-size: 0.9rem;
}

.section-code-preview {
  color: #666;
  font-size: 0.8rem;
  font-family: 'Courier New', monospace;
  margin-top: 0.5rem;
  display: block;
}

.modal-actions {
  display: flex;
  gap: 1rem;
  justify-content: flex-end;
  margin-top: 2rem;
}

.cancel-btn, .back-btn {
  background: transparent;
  color: #666;
  border: 2px solid #ddd;
  padding: 0.75rem 1.5rem;
  border-radius: 10px;
  cursor: pointer;
  font-weight: 600;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.cancel-btn:hover, .back-btn:hover {
  border-color: #3D8D7A;
  color: #3D8D7A;
}

.next-btn, .save-btn {
  background: linear-gradient(135deg, #3D8D7A 0%, #A3D1C6 100%);
  color: white;
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 10px;
  cursor: pointer;
  font-weight: 600;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.next-btn:hover, .save-btn:hover {
  transform: translateY(-1px);
  box-shadow: 0 6px 20px rgba(61, 141, 122, 0.3);
}

.next-btn:disabled, .save-btn:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

/* Loading Styles */
.loading-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.6);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1100;
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
  border: 4px solid rgba(61, 141, 122, 0.1);
  border-left: 4px solid #3D8D7A;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin: 0 auto 1rem;
}

@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

/* Responsive Design */
@media (max-width: 768px) {
  .subjects-grid {
    grid-template-columns: 1fr;
  }
  
  .page-header {
    flex-direction: column;
    align-items: stretch;
  }
  
  .subject-stats {
    gap: 1rem;
  }
  
  .section-actions {
    grid-template-columns: 1fr 1fr;
  }
  
  .modal-overlay {
    padding: 1rem;
  }
  
  .section-code-display {
    flex-direction: column;
    align-items: stretch;
    gap: 0.5rem;
  }
}
</style>