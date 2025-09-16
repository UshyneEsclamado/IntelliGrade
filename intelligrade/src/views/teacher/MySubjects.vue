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
            <p class="subject-code">Class Code: <strong>{{ subject.class_code }}</strong></p>
          </div>
          <div class="subject-actions">
            <button @click="editSubject(subject)" class="action-btn edit" title="Edit Subject">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                <path d="M20.71,7.04C21.1,6.65 21.1,6 20.71,5.63L18.37,3.29C18,2.9 17.35,2.9 16.96,3.29L15.12,5.12L18.87,8.87M3,17.25V21H6.75L17.81,9.93L14.06,6.18L3,17.25Z" />
              </svg>
            </button>
            <button @click="viewClassLink(subject)" class="action-btn view" title="View All Links">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                <path d="M3.9,12C3.9,10.29 5.29,8.9 7,8.9H11V7H7A5,5 0 0,0 2,12A5,5 0 0,0 7,17H11V15.1H7C5.29,15.1 3.9,13.71 3.9,12M8,13H16V11H8V13M17,7H13V8.9H17C18.71,8.9 20.1,10.29 20.1,12C20.1,13.71 18.71,15.1 17,15.1H13V17H17A5,5 0 0,0 22,12A5,5 0 0,0 17,7Z" />
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

        <!-- Main Class Link -->
        <div class="main-class-link">
          <div class="class-link-header">
            <h4>Main Class Link:</h4>
            <button @click="copyLink(generateMainClassLink(subject.class_code), `main-${subject.id}`)" class="copy-btn-small">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor">
                <path d="M19,21H8V7H19M19,5H8A2,2 0 0,0 6,7V21A2,2 0 0,0 8,23H19A2,2 0 0,0 21,21V7A2,2 0 0,0 19,5M16,1H4A2,2 0 0,0 2,3V17H4V3H16V1Z" />
              </svg>
              {{ copiedLinkId === `main-${subject.id}` ? 'Copied!' : 'Copy' }}
            </button>
          </div>
          <div class="link-display">
            <input 
              :value="generateMainClassLink(subject.class_code)" 
              readonly 
              class="link-input-small"
            />
          </div>
          <small class="link-description">Students can join any section using this main link</small>
        </div>

        <div class="sections-list" v-if="subject.sections && subject.sections.length > 0">
          <h4>Sections:</h4>
          <div class="sections">
            <div v-for="section in subject.sections" :key="section.id" class="section-item">
              <div class="section-info">
                <span class="section-name">{{ section.name }}</span>
                <span class="section-code">Code: {{ section.section_code }}</span>
                <div class="section-link-display">
                  <input 
                    :value="generateSectionLink(subject.class_code, section.section_code)" 
                    readonly 
                    class="section-link-input"
                  />
                  <button @click="copyLink(generateSectionLink(subject.class_code, section.section_code), section.id)" class="copy-btn-small">
                    <svg width="12" height="12" viewBox="0 0 24 24" fill="currentColor">
                      <path d="M19,21H8V7H19M19,5H8A2,2 0 0,0 6,7V21A2,2 0 0,0 8,23H19A2,2 0 0,0 21,21V7A2,2 0 0,0 19,5M16,1H4A2,2 0 0,0 2,3V17H4V3H16V1Z" />
                    </svg>
                    {{ copiedLinkId === section.id ? 'Copied!' : 'Copy' }}
                  </button>
                </div>
              </div>
              <div class="section-stats">
                <span class="student-count">{{ section.student_count || 0 }} students</span>
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
            <p class="step-subtitle">Customize section names and codes will be auto-generated</p>

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
                  <small class="section-code-preview">Code will be: {{ generateSectionCode(section.name || `Section ${index + 1}`) }}</small>
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

    <!-- Class Link Modal (same as before) -->
    <div v-if="showClassLinkModal" class="modal-overlay" @click="showClassLinkModal = false">
      <div class="modal-content class-link-modal" @click.stop>
        <div class="modal-header">
          <h2>{{ selectedSubject?.name }} - All Class Links</h2>
          <button @click="showClassLinkModal = false" class="close-btn">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
              <path d="M19,6.41L17.59,5L12,10.59L6.41,5L5,6.41L10.59,12L5,17.59L6.41,19L12,13.41L17.59,19L19,17.59L13.41,12L19,6.41Z" />
            </svg>
          </button>
        </div>

        <div class="class-link-content">
          <div class="class-info">
            <h3>{{ selectedSubject?.name }}</h3>
            <p>Grade {{ selectedSubject?.grade_level }} • Class Code: <strong>{{ selectedSubject?.class_code }}</strong></p>
          </div>

          <!-- Main Class Link Section -->
          <div class="main-link-section">
            <h4>
              <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" style="margin-right: 8px;">
                <path d="M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2M7.07,18.28C7.5,17.38 10.12,16.5 12,16.5C13.88,16.5 16.5,17.38 16.93,18.28C15.57,19.36 13.86,20 12,20C10.14,20 8.43,19.36 7.07,18.28M18.36,16.83C16.93,15.09 13.46,14.5 12,14.5C10.54,14.5 7.07,15.09 5.64,16.83C4.62,15.5 4,13.82 4,12C4,7.59 7.59,4 12,4C16.41,4 20,7.59 20,12C20,13.82 19.38,15.5 18.36,16.83M12,6C10.06,6 8.5,7.56 8.5,9.5C8.5,11.44 10.06,13 12,13C13.94,13 15.5,11.44 15.5,9.5C15.5,7.56 13.94,6 12,6M12,11A1.5,1.5 0 0,1 10.5,9.5A1.5,1.5 0 0,1 12,8A1.5,1.5 0 0,1 13.5,9.5A1.5,1.5 0 0,1 12,11Z" />
              </svg>
              Main Class Link
            </h4>
            <p class="section-description">Students can use this link to join any available section in this class</p>
            
            <div class="link-item main-link">
              <div class="link-info">
                <span class="link-label">{{ selectedSubject?.name }} Grade {{ selectedSubject?.grade_level }}</span>
                <span class="link-code">Class Code: {{ selectedSubject?.class_code }}</span>
              </div>
              <div class="link-url-container">
                <input 
                  :value="generateMainClassLink(selectedSubject?.class_code)" 
                  readonly 
                  class="link-input"
                  :id="`main-link-${selectedSubject?.id}`"
                />
                <button @click="copyLink(generateMainClassLink(selectedSubject?.class_code), `main-modal-${selectedSubject?.id}`)" class="copy-btn">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M19,21H8V7H19M19,5H8A2,2 0 0,0 6,7V21A2,2 0 0,0 8,23H19A2,2 0 0,0 21,21V7A2,2 0 0,0 19,5M16,1H4A2,2 0 0,0 2,3V17H4V3H16V1Z" />
                  </svg>
                  {{ copiedLinkId === `main-modal-${selectedSubject?.id}` ? 'Copied!' : 'Copy' }}
                </button>
              </div>
            </div>
          </div>

          <!-- Section-Specific Links -->
          <div class="sections-links">
            <h4>
              <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" style="margin-right: 8px;">
                <path d="M12,2L13.09,8.26L22,9L17.5,13.74L18.18,21L12,17.77L5.82,21L6.5,13.74L2,9L10.91,8.26L12,2Z" />
              </svg>
              Section-Specific Links
            </h4>
            <p class="section-description">Direct links to specific sections - students will join exactly this section</p>
            
            <div v-for="section in selectedSubject?.sections" :key="section.id" class="link-item">
              <div class="link-info">
                <span class="link-label">{{ section.name }}</span>
                <span class="link-code">{{ section.section_code }}</span>
                <span class="student-count">{{ section.student_count || 0 }} students enrolled</span>
              </div>
              <div class="link-url-container">
                <input 
                  :value="generateSectionLink(selectedSubject?.class_code, section.section_code)" 
                  readonly 
                  class="link-input"
                  :id="`section-link-${section.id}`"
                />
                <button @click="copyLink(generateSectionLink(selectedSubject?.class_code, section.section_code), `section-modal-${section.id}`)" class="copy-btn">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M19,21H8V7H19M19,5H8A2,2 0 0,0 6,7V21A2,2 0 0,0 8,23H19A2,2 0 0,0 21,21V7A2,2 0 0,0 19,5M16,1H4A2,2 0 0,0 2,3V17H4V3H16V1Z" />
                  </svg>
                  {{ copiedLinkId === `section-modal-${section.id}` ? 'Copied!' : 'Copy' }}
                </button>
              </div>
            </div>
          </div>

          <div class="share-instructions">
            <h4>How to use these links:</h4>
            <div class="instruction-grid">
              <div class="instruction-item">
                <div class="instruction-icon main">
                  <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2M7.07,18.28C7.5,17.38 10.12,16.5 12,16.5C13.88,16.5 16.5,17.38 16.93,18.28C15.57,19.36 13.86,20 12,20C10.14,20 8.43,19.36 7.07,18.28M18.36,16.83C16.93,15.09 13.46,14.5 12,14.5C10.54,14.5 7.07,15.09 5.64,16.83C4.62,15.5 4,13.82 4,12C4,7.59 7.59,4 12,4C16.41,4 20,7.59 20,12C20,13.82 19.38,15.5 18.36,16.83M12,6C10.06,6 8.5,7.56 8.5,9.5C8.5,11.44 10.06,13 12,13C13.94,13 15.5,11.44 15.5,9.5C15.5,7.56 13.94,6 12,6M12,11A1.5,1.5 0 0,1 10.5,9.5A1.5,1.5 0 0,1 12,8A1.5,1.5 0 0,1 13.5,9.5A1.5,1.5 0 0,1 12,11Z" />
                  </svg>
                </div>
                <div class="instruction-content">
                  <h5>Main Class Link</h5>
                  <p>Share when you want students to choose their own section or when sections aren't full</p>
                </div>
              </div>
              <div class="instruction-item">
                <div class="instruction-icon section">
                  <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M12,2L13.09,8.26L22,9L17.5,13.74L18.18,21L12,17.77L5.82,21L6.5,13.74L2,9L10.91,8.26L12,2Z" />
                  </svg>
                </div>
                <div class="instruction-content">
                  <h5>Section-Specific Links</h5>
                  <p>Share when you want students to join a specific section directly</p>
                </div>
              </div>
            </div>
          </div>
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
import { supabase } from '../../supabase'

// State
const subjects = ref([])
const showCreateModal = ref(false)
const showClassLinkModal = ref(false)
const selectedSubject = ref(null)
const isEditing = ref(false)
const isLoading = ref(false)
const loadingMessage = ref('')
const currentSubjectId = ref(null)
const currentStep = ref(1)
const copiedLinkId = ref(null)

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

// Methods
const fetchSubjects = async () => {
  try {
    const { data: { user } } = await supabase.auth.getUser()
    if (!user) {
      console.log('No user found')
      return
    }

    loadingMessage.value = 'Loading subjects...'
    isLoading.value = true

    // Fetch subjects with sections from real database
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

const generateClassCode = (subjectName, gradeLevel) => {
  const subjectPrefix = subjectName.substring(0, 3).toUpperCase().replace(/[^A-Z]/g, '') || 'SUB'
  const year = new Date().getFullYear()
  const randomSuffix = Math.random().toString(36).substring(2, 4).toUpperCase()
  return `${subjectPrefix}${gradeLevel}${randomSuffix}${year}`
}

const generateSectionCode = (sectionName, index = 0) => {
  if (!formData.value.name || !formData.value.grade_level) return 'CODE-PREVIEW'
  
  const subjectPrefix = formData.value.name.substring(0, 3).toUpperCase().replace(/[^A-Z]/g, '') || 'SUB'
  const gradeLevel = formData.value.grade_level
  const cleanSectionName = sectionName.replace(/[^a-zA-Z0-9]/g, '').substring(0, 1).toUpperCase() || 'S'
  // Use timestamp + index to ensure uniqueness during preview
  const timestamp = Date.now().toString().slice(-4)
  const indexSuffix = String(index + 1).padStart(2, '0')
  
  return `${subjectPrefix}${gradeLevel}-${cleanSectionName}${indexSuffix}${timestamp}`
}

// Generate main class link (students choose section)
const generateMainClassLink = (classCode) => {
  const baseUrl = window.location.origin
  return `${baseUrl}/join-class/${classCode}`
}

// Generate section-specific link (direct to section)  
const generateSectionLink = (classCode, sectionCode) => {
  const baseUrl = window.location.origin
  return `${baseUrl}/join-section/${classCode}/${sectionCode}`
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

    // Generate unique class code
    let classCode
    let isUnique = false
    let attempts = 0
    const maxAttempts = 10

    // Ensure class code is unique
    while (!isUnique && attempts < maxAttempts) {
      classCode = generateClassCode(formData.value.name, formData.value.grade_level)
      
      // Check if class code already exists
      const { data: existingSubject, error: checkError } = await supabase
        .from('subjects')
        .select('class_code')
        .eq('class_code', classCode)
        .maybeSingle()

      if (checkError) {
        console.error('Error checking class code uniqueness:', checkError)
        throw checkError
      }

      if (!existingSubject) {
        isUnique = true
      }
      
      attempts++
    }

    if (!isUnique) {
      throw new Error('Could not generate unique class code. Please try again.')
    }

    // Prepare subject data
    const subjectData = {
      name: formData.value.name,
      grade_level: parseInt(formData.value.grade_level),
      class_code: classCode,
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
    
    for (let i = 0; i < formData.value.sections.length; i++) {
      const section = formData.value.sections[i]
      let sectionCode
      let isSectionUnique = false
      let sectionAttempts = 0

      // Ensure section code is unique
      while (!isSectionUnique && sectionAttempts < maxAttempts) {
        // Generate section code with more randomness
        const subjectPrefix = formData.value.name.substring(0, 3).toUpperCase().replace(/[^A-Z]/g, '') || 'SUB'
        const gradeLevel = formData.value.grade_level
        const cleanSectionName = section.name.replace(/[^a-zA-Z0-9]/g, '').substring(0, 1).toUpperCase() || 'S'
        const uniqueTimestamp = (baseTimestamp + i + sectionAttempts).toString().slice(-5)
        const randomSuffix = Math.random().toString(36).substring(2, 3).toUpperCase()
        
        sectionCode = `${subjectPrefix}${gradeLevel}-${cleanSectionName}${uniqueTimestamp}${randomSuffix}`
        
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

    // Show success message with class code and links
    const mainLink = generateMainClassLink(classCode)
    alert(`✅ Subject "${formData.value.name}" ${isEditing.value ? 'updated' : 'created'} successfully!\n\n🔑 Class Code: ${classCode}\n\n🔗 Main Class Link:\n${mainLink}\n\n📚 Students can use this link to join any section in your class.\n\nYou can also find section-specific links in the subject card!`)

  } catch (error) {
    console.error('Error saving subject:', error)
    alert(`❌ Error ${isEditing.value ? 'updating' : 'creating'} subject:\n\n${error.message}`)
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
  if (!confirm(`⚠️ Are you sure you want to delete "${subject?.name}"?\n\nThis will permanently remove:\n• All sections (${subject?.sections?.length || 0} sections)\n• All enrolled students\n• All class data\n\nThis action cannot be undone.`)) {
    return
  }

  isLoading.value = true
  loadingMessage.value = 'Deleting subject...'

  try {
    // Delete the subject (sections will be deleted automatically via foreign key cascade)
    const { error } = await supabase
      .from('subjects')
      .delete()
      .eq('id', subjectId)

    if (error) throw error

    await fetchSubjects()
    alert(`✅ Subject "${subject?.name}" deleted successfully!`)
  } catch (error) {
    console.error('Error deleting subject:', error)
    alert(`❌ Error deleting subject: ${error.message}`)
  } finally {
    isLoading.value = false
  }
}

const viewClassLink = (subject) => {
  selectedSubject.value = subject
  showClassLinkModal.value = true
}

const copyLink = async (link, linkId) => {
  try {
    await navigator.clipboard.writeText(link)
    copiedLinkId.value = linkId
    setTimeout(() => {
      copiedLinkId.value = null
    }, 2000)
  } catch (err) {
    console.error('Failed to copy link:', err)
    // Fallback for older browsers
    const textArea = document.createElement('textarea')
    textArea.value = link
    document.body.appendChild(textArea)
    textArea.select()
    document.execCommand('copy')
    document.body.removeChild(textArea)
    copiedLinkId.value = linkId
    setTimeout(() => {
      copiedLinkId.value = null
    }, 2000)
  }
}

const getTotalStudents = (subject) => {
  if (!subject.sections) return 0
  return subject.sections.reduce((total, section) => total + (section.student_count || 0), 0)
}

const closeModal = () => {
  showCreateModal.value = false
  showClassLinkModal.value = false
  selectedSubject.value = null
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

.subject-code {
  color: #666;
  font-size: 0.9rem;
  font-family: 'Courier New', monospace;
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

.action-btn.view {
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

/* Main Class Link Styles */
.main-class-link {
  background: rgba(16, 185, 129, 0.05);
  border: 1px solid rgba(16, 185, 129, 0.2);
  border-radius: 12px;
  padding: 1.5rem;
  margin-bottom: 2rem;
}

.class-link-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
}

.class-link-header h4 {
  color: #10b981;
  margin: 0;
  font-size: 1rem;
  font-weight: 600;
}

.link-display {
  margin-bottom: 0.5rem;
}

.link-input-small {
  width: 100%;
  padding: 0.6rem;
  border: 1px solid rgba(16, 185, 129, 0.3);
  border-radius: 8px;
  font-family: 'Courier New', monospace;
  font-size: 0.85rem;
  background: rgba(16, 185, 129, 0.05);
  color: #059669;
}

.link-description {
  color: #666;
  font-size: 0.8rem;
  font-style: italic;
}

.copy-btn-small {
  background: #10b981;
  color: white;
  border: none;
  padding: 0.4rem 0.8rem;
  border-radius: 6px;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 0.3rem;
  font-size: 0.8rem;
  transition: all 0.3s ease;
}

.copy-btn-small:hover {
  background: #059669;
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
  gap: 1rem;
}

.section-item {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  padding: 1rem;
  background: white;
  border-radius: 12px;
  border: 1px solid rgba(61, 141, 122, 0.1);
  transition: all 0.3s ease;
}

.section-item:hover {
  box-shadow: 0 4px 12px rgba(61, 141, 122, 0.1);
}

.section-info {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.section-name {
  font-weight: 600;
  color: #3D8D7A;
  font-size: 1rem;
}

.section-code {
  color: #666;
  font-size: 0.8rem;
  font-family: 'Courier New', monospace;
}

.section-link-display {
  display: flex;
  gap: 0.5rem;
  margin-top: 0.5rem;
}

.section-link-input {
  flex: 1;
  padding: 0.4rem 0.6rem;
  border: 1px solid rgba(61, 141, 122, 0.2);
  border-radius: 6px;
  font-family: 'Courier New', monospace;
  font-size: 0.75rem;
  background: rgba(251, 255, 228, 0.5);
}

.section-stats {
  display: flex;
  align-items: center;
  gap: 1rem;
  flex-shrink: 0;
}

.student-count {
  color: #666;
  font-size: 0.9rem;
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

.class-link-modal {
  max-width: 900px;
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
  border-radius: 12px;
  cursor: pointer;
  font-weight: 600;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.cancel-btn:hover, .back-btn:hover {
  background: #f5f5f5;
  border-color: #999;
}

.next-btn, .save-btn {
  background: linear-gradient(135deg, #3D8D7A 0%, #A3D1C6 100%);
  color: white;
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 12px;
  cursor: pointer;
  font-weight: 600;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.next-btn:hover:not(:disabled), .save-btn:hover:not(:disabled) {
  transform: translateY(-1px);
  box-shadow: 0 8px 20px rgba(61, 141, 122, 0.3);
}

.next-btn:disabled, .save-btn:disabled {
  opacity: 0.7;
  cursor: not-allowed;
}

/* Enhanced Class Link Modal Styles */
.class-link-content {
  padding: 2rem;
}

.class-info {
  margin-bottom: 3rem;
  padding: 1.5rem;
  background: rgba(251, 255, 228, 0.5);
  border-radius: 12px;
}

.class-info h3 {
  color: #3D8D7A;
  font-size: 1.5rem;
  font-weight: 700;
  margin-bottom: 0.5rem;
}

.class-info p {
  color: #666;
}

.main-link-section {
  margin-bottom: 2rem;
}

.link-item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1rem;
  border: 1px solid rgba(61, 141, 122, 0.1);
  border-radius: 12px;
  background: white;
  margin-bottom: 1rem;
  transition: all 0.3s ease;
}

.link-item:hover {
  box-shadow: 0 4px 12px rgba(61, 141, 122, 0.1);
}

.link-info {
  flex: 1;
}

.link-label {
  font-weight: 600;
  color: #3D8D7A;
  font-size: 1rem;
  margin-bottom: 0.2rem;
}

.link-code {
  font-family: 'Courier New', monospace;
  color: #666;
  font-size: 0.9rem;
}

.link-url-container {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.link-input {
  flex: 1;
  padding: 0.75rem;
  border: 2px solid rgba(61, 141, 122, 0.1);
  border-radius: 8px;
  font-family: 'Courier New', monospace;
  font-size: 0.9rem;
  background: rgba(251, 255, 228, 0.3);
}

.copy-btn {
  background: #3D8D7A;
  color: white;
  border: none;
  padding: 0.75rem 1rem;
  border-radius: 8px;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  transition: all 0.3s ease;
  white-space: nowrap;
}

.copy-btn:hover {
  background: #2d6b5a;
}

.share-instructions {
  margin-top: 2rem;
  padding: 1.5rem;
  background: rgba(179, 216, 168, 0.1);
  border-radius: 12px;
  border-left: 4px solid #3D8D7A;
}

.share-instructions h4 {
  color: #3D8D7A;
  margin-bottom: 1rem;
}

.share-instructions ol {
  color: #666;
  padding-left: 1.5rem;
}

.share-instructions li {
  margin-bottom: 0.5rem;
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
  .subjects-page {
    padding: 1rem;
  }

  .page-header {
    flex-direction: column;
    align-items: stretch;
  }

  .subjects-grid {
    grid-template-columns: 1fr;
    gap: 1rem;
  }

  .subject-card {
    padding: 1.5rem;
  }

  .subject-stats {
    gap: 1rem;
  }

  .modal-overlay {
    padding: 1rem;
  }

  .modal-content {
    margin: 0;
  }

  .modal-header,
  .subject-form,
  .class-link-content {
    padding: 1.5rem;
  }

  .section-setup-item {
    flex-direction: column;
    align-items: stretch;
  }

  .section-number {
    align-self: flex-start;
  }
}
</style>