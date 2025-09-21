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
          <div class="stat clickable-stat" @click="viewStudentRoster(subject)">
            <span class="stat-number">{{ getTotalStudents(subject) }}</span>
            <span class="stat-label">Students</span>
            <small class="view-hint">Click to view roster</small>
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

    <!-- Student Roster Modal -->
    <div v-if="showStudentRosterModal && currentStudentRoster" class="modal-overlay" @click="closeStudentRosterModal">
      <div class="modal-content student-roster-modal" @click.stop>
        <div class="modal-header">
          <div>
            <h2>{{ currentStudentRoster.subject.name }} - Student Roster</h2>
            <p class="roster-subtitle">
              Grade {{ currentStudentRoster.subject.grade_level }} | 
              Total: {{ currentStudentRoster.totalActualStudents }} Students
            </p>
          </div>
          <button @click="closeStudentRosterModal" class="close-btn">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
              <path d="M19,6.41L17.59,5L12,10.59L6.41,5L5,6.41L10.59,12L5,17.59L6.41,19L12,13.41L17.59,19L19,17.59L13.41,12L19,6.41Z" />
            </svg>
          </button>
        </div>

        <div class="roster-content">
          <div v-if="Object.keys(currentStudentRoster.studentsBySection).length === 0" class="no-students">
            <div class="empty-icon">
              <svg width="64" height="64" viewBox="0 0 24 24" fill="currentColor">
                <path d="M16 4C18.2 4 20 5.8 20 8S18.2 12 16 12 12 10.2 12 8 13.8 4 16 4M16 14C20.4 14 24 15.8 24 18V20H8V18C8 15.8 11.6 14 16 14M12.5 11.5C12.8 10.9 13 10.2 13 9.5C13 8.1 12.6 6.8 11.9 5.7C10.8 4.6 9.4 4 8 4S5.2 4.6 4.1 5.7C3.4 6.8 3 8.1 3 9.5S3.4 12.2 4.1 13.3C5.2 14.4 6.6 15 8 15C8.8 15 9.5 14.8 10.1 14.5C9.4 15.4 9 16.6 9 18V20H1V18C1 15.8 4.6 14 9 14C10.5 14 11.8 14.3 12.5 14.8V11.5Z" />
              </svg>
            </div>
            <h3>No Students Enrolled</h3>
            <p>Students haven't joined any sections yet.</p>
          </div>

          <div v-else class="sections-roster">
            <div v-for="(sectionData, sectionKey) in currentStudentRoster.studentsBySection" :key="sectionKey" class="section-roster">
              <div class="section-roster-header">
                <h3>{{ sectionData.section.name }}</h3>
                <div class="section-details">
                  <span class="section-code">{{ sectionData.section.section_code }}</span>
                  <span class="student-count">{{ sectionData.students.length }} student{{ sectionData.students.length !== 1 ? 's' : '' }}</span>
                </div>
              </div>

              <div class="students-table">
                <div class="table-header">
                  <div class="col-id">Student ID</div>
                  <div class="col-name">Name</div>
                  <div class="col-email">Email</div>
                  <div class="col-grade">Grade</div>
                  <div class="col-date">Enrolled</div>
                </div>
                
                <div class="table-body">
                  <div v-for="student in sectionData.students" :key="student.id" class="student-row">
                    <div class="col-id">{{ student.student_id }}</div>
                    <div class="col-name">{{ student.first_name }} {{ student.last_name }}</div>
                    <div class="col-email">{{ student.email }}</div>
                    <div class="col-grade">{{ student.grade_level }}</div>
                    <div class="col-date">{{ formatEnrollmentDate(student.enrollment_date) }}</div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="roster-actions">
          <button @click="exportStudentRoster" class="export-btn">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
              <path d="M14,2H6A2,2 0 0,0 4,4V20A2,2 0 0,0 6,22H18A2,2 0 0,0 20,20V8L14,2M18,20H6V4H13V9H18V20Z" />
            </svg>
            Export List
          </button>
          <button @click="closeStudentRosterModal" class="close-roster-btn">Close</button>
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
import { ref, onMounted, computed, nextTick } from 'vue'
import { useRouter } from 'vue-router'
import { supabase } from '../../supabase.js'

// Router
const router = useRouter()

// State
const subjects = ref([])
const showCreateModal = ref(false)
const showStudentRosterModal = ref(false)
const currentStudentRoster = ref(null)
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

    console.log('Fetching subjects for teacher:', user.id)

    // Fetch subjects with sections
    const { data: subjectsData, error: subjectsError } = await supabase
      .from('subjects')
      .select(`
        id,
        name,
        grade_level,
        teacher_id,
        created_at,
        updated_at,
        sections(
          id,
          name,
          section_code,
          student_count,
          created_at,
          updated_at
        )
      `)
      .eq('teacher_id', user.id)
      .order('created_at', { ascending: false })

    if (subjectsError) {
      console.error('Error fetching subjects:', subjectsError)
      throw subjectsError
    }

    console.log('Fetched subjects data:', subjectsData)

    // Get actual enrollment counts for each subject
    if (subjectsData && subjectsData.length > 0) {
      for (let subject of subjectsData) {
        if (subject.sections && subject.sections.length > 0) {
          const sectionIds = subject.sections.map(s => s.id)
          
          // Get actual enrollment count
          const { count, error: countError } = await supabase
            .from('enrollments')
            .select('*', { count: 'exact', head: true })
            .in('section_id', sectionIds)

          if (!countError) {
            subject.actualStudentCount = count || 0
          } else {
            subject.actualStudentCount = 0
          }

          // Also get count per section
          for (let section of subject.sections) {
            const { count: sectionCount, error: sectionCountError } = await supabase
              .from('enrollments')
              .select('*', { count: 'exact', head: true })
              .eq('section_id', section.id)

            if (!sectionCountError) {
              section.actualStudentCount = sectionCount || 0
            } else {
              section.actualStudentCount = 0
            }
          }
        } else {
          subject.actualStudentCount = 0
        }
      }
    }

    console.log('Previous subjects count:', subjects.value.length)
    
    // Force reactivity update
    subjects.value = [...(subjectsData || [])]
    
    console.log('Updated subjects count:', subjects.value.length)
    console.log('Updated subjects array:', subjects.value)

    // Force Vue to re-render
    await nextTick()

  } catch (error) {
    console.error('Error in fetchSubjects:', error)
    alert(`Database Error: ${error.message}\n\nPlease check your database setup.`)
  } finally {
    isLoading.value = false
  }
}

// Updated getTotalStudents to use actual count
const getTotalStudents = (subject) => {
  // Use the actualStudentCount we calculated in fetchSubjects
  return subject.actualStudentCount || 0
}

// Enhanced viewStudentRoster function with correct enrollment mapping
const viewStudentRoster = async (subject) => {
  try {
    isLoading.value = true
    loadingMessage.value = 'Loading student roster...'
    
    console.log('=== DEBUGGING STUDENT ROSTER ===')
    console.log('Subject:', subject)
    
    // Get all sections for this subject
    const { data: sections, error: sectionsError } = await supabase
      .from('sections')
      .select('*')
      .eq('class_id', subject.id)

    if (sectionsError) {
      console.error('Error fetching sections:', sectionsError)
      throw sectionsError
    }

    console.log('Sections found:', sections)

    if (!sections || sections.length === 0) {
      currentStudentRoster.value = {
        subject,
        studentsBySection: {},
        totalActualStudents: 0
      }
      showStudentRosterModal.value = true
      return
    }

    // Get all enrollments for these sections
    const sectionIds = sections.map(s => s.id)
    console.log('Section IDs:', sectionIds)
    
    const { data: enrollments, error: enrollmentsError } = await supabase
      .from('enrollments')
      .select('*')
      .in('section_id', sectionIds)

    if (enrollmentsError) {
      console.error('Error fetching enrollments:', enrollmentsError)
      throw enrollmentsError
    }

    console.log('Enrollments found:', enrollments)

    // Get student details - enrollments.student_id is likely auth_user_id from profiles
    let studentDetails = []
    if (enrollments && enrollments.length > 0) {
      const studentIds = enrollments.map(e => e.student_id)
      console.log('Student IDs to fetch (UUIDs):', studentIds)
      
      // Method 1: Try profiles table using auth_user_id (most likely match)
      console.log('Trying profiles table with auth_user_id...')
      try {
        const { data: profilesData, error: profilesError } = await supabase
          .from('profiles')
          .select('*')
          .in('auth_user_id', studentIds)

        console.log('Profiles table (auth_user_id) response:', { data: profilesData, error: profilesError })

        if (!profilesError && profilesData && profilesData.length > 0) {
          studentDetails = profilesData.map(profile => ({
            id: profile.auth_user_id, // Use auth_user_id as the main ID for matching
            student_id: profile.student_id || profile.auth_user_id,
            first_name: profile.full_name ? profile.full_name.split(' ')[0] : 'Unknown',
            last_name: profile.full_name ? profile.full_name.split(' ').slice(1).join(' ') : 'Student',
            email: profile.email || 'N/A',
            grade_level: profile.course_year || 'N/A',
            role: profile.role || 'N/A'
          }))
          console.log('✅ Students found in profiles table via auth_user_id:', studentDetails)
        }
      } catch (profilesError) {
        console.log('❌ Profiles table (auth_user_id) error:', profilesError)
      }

      // Method 2: If no match with auth_user_id, try profiles table with id
      if (studentDetails.length === 0) {
        console.log('Trying profiles table with id...')
        try {
          const { data: profilesData, error: profilesError } = await supabase
            .from('profiles')
            .select('*')
            .in('id', studentIds)

          console.log('Profiles table (id) response:', { data: profilesData, error: profilesError })

          if (!profilesError && profilesData && profilesData.length > 0) {
            studentDetails = profilesData.map(profile => ({
              id: profile.id,
              student_id: profile.student_id || profile.id,
              first_name: profile.full_name ? profile.full_name.split(' ')[0] : 'Unknown',
              last_name: profile.full_name ? profile.full_name.split(' ').slice(1).join(' ') : 'Student',
              email: profile.email || 'N/A',
              grade_level: profile.course_year || 'N/A',
              role: profile.role || 'N/A'
            }))
            console.log('✅ Students found in profiles table via id:', studentDetails)
          }
        } catch (profilesError) {
          console.log('❌ Profiles table (id) error:', profilesError)
        }
      }

      // Method 3: Try students table (less likely but worth checking)
      if (studentDetails.length === 0) {
        console.log('Trying students table...')
        try {
          const { data: studentsData, error: studentsError } = await supabase
            .from('students')
            .select('*')
            .in('id', studentIds)

          console.log('Students table response:', { data: studentsData, error: studentsError })
          
          if (!studentsError && studentsData && studentsData.length > 0) {
            studentDetails = studentsData.map(student => ({
              id: student.id,
              student_id: student.student_id || student.id,
              first_name: student.first_name || 'Unknown',
              last_name: student.last_name || 'Student',
              email: student.email || 'N/A',
              grade_level: student.grade_level?.toString() || 'N/A'
            }))
            console.log('✅ Students found in students table:', studentDetails)
          }
        } catch (studentsTableError) {
          console.log('❌ Students table error:', studentsTableError)
        }
      }

      // Method 4: Try to find students via profile_id relationship
      if (studentDetails.length === 0) {
        console.log('Trying to find students via profile relationship...')
        try {
          // First get profiles by auth_user_id, then get students by profile_id
          const { data: profilesData, error: profilesError } = await supabase
            .from('profiles')
            .select('id, auth_user_id, full_name, email, student_id, course_year, role')
            .in('auth_user_id', studentIds)

          if (!profilesError && profilesData && profilesData.length > 0) {
            console.log('Found profiles, now looking for students:', profilesData)
            
            const profileIds = profilesData.map(p => p.id)
            const { data: studentsData, error: studentsError } = await supabase
              .from('students')
              .select('*')
              .in('profile_id', profileIds)

            if (!studentsError && studentsData && studentsData.length > 0) {
              // Merge student and profile data
              studentDetails = studentsData.map(student => {
                const profile = profilesData.find(p => p.id === student.profile_id)
                return {
                  id: profile?.auth_user_id || student.id,
                  student_id: student.student_id || profile?.student_id || student.id,
                  first_name: student.first_name || (profile?.full_name ? profile.full_name.split(' ')[0] : 'Unknown'),
                  last_name: student.last_name || (profile?.full_name ? profile.full_name.split(' ').slice(1).join(' ') : 'Student'),
                  email: student.email || profile?.email || 'N/A',
                  grade_level: student.grade_level?.toString() || profile?.course_year || 'N/A',
                  role: profile?.role || 'N/A'
                }
              })
              console.log('✅ Students found via profile relationship:', studentDetails)
            }
          }
        } catch (relationError) {
          console.log('❌ Profile relationship error:', relationError)
        }
      }

      console.log('Final student details:', studentDetails)
    }

    // Group students by section
    const studentsBySection = {}
    let totalActualStudents = 0
    
    // Create section groups
    sections.forEach(section => {
      const sectionKey = `${section.name} (${section.section_code})`
      studentsBySection[sectionKey] = {
        section: section,
        students: []
      }
    })

    // Add students to their respective sections
    enrollments?.forEach(enrollment => {
      const section = sections.find(s => s.id === enrollment.section_id)
      const student = studentDetails.find(s => s.id === enrollment.student_id)
      
      console.log('Processing enrollment:', {
        enrollment_id: enrollment.id,
        student_id: enrollment.student_id,
        section_id: enrollment.section_id,
        found_student: student,
        found_section: section
      })
      
      if (section) {
        const sectionKey = `${section.name} (${section.section_code})`
        
        if (student) {
          console.log('✅ Adding student with data:', student)
          studentsBySection[sectionKey].students.push({
            ...student,
            enrollment_date: enrollment.created_at,
            enrollment_id: enrollment.id
          })
        } else {
          console.log('❌ No student data found, creating placeholder')
          // Show more detailed placeholder for debugging
          const shortId = enrollment.student_id.toString().substring(0, 8)
          studentsBySection[sectionKey].students.push({
            id: enrollment.student_id,
            student_id: `Missing-${shortId}`,
            first_name: 'Data',
            last_name: 'Not Found',
            email: `student-${shortId}@unknown.com`,
            grade_level: 'N/A',
            enrollment_date: enrollment.created_at,
            enrollment_id: enrollment.id,
            debug_note: 'Student data not found in any table'
          })
        }
        totalActualStudents++
      }
    })

    console.log('Final studentsBySection:', studentsBySection)
    console.log('Total actual students:', totalActualStudents)

    // Sort students within each section by last name
    Object.keys(studentsBySection).forEach(sectionKey => {
      studentsBySection[sectionKey].students.sort((a, b) => 
        (a.last_name || '').localeCompare(b.last_name || '')
      )
    })

    // Store for modal display
    currentStudentRoster.value = {
      subject,
      studentsBySection,
      totalActualStudents
    }
    
    showStudentRosterModal.value = true

  } catch (error) {
    console.error('Error viewing student roster:', error)
    
    // Show basic roster with section info even if student details fail
    const basicRoster = {
      subject,
      studentsBySection: {},
      totalActualStudents: 0
    }
    
    // Try to at least show sections
    try {
      const { data: sections } = await supabase
        .from('sections')
        .select('*')
        .eq('class_id', subject.id)
      
      sections?.forEach(section => {
        const sectionKey = `${section.name} (${section.section_code})`
        basicRoster.studentsBySection[sectionKey] = {
          section: section,
          students: []
        }
      })
    } catch (sectionsError) {
      console.error('Could not even fetch sections:', sectionsError)
    }
    
    currentStudentRoster.value = basicRoster
    showStudentRosterModal.value = true
    
    alert(`Unable to load complete student roster: ${error.message}\n\nShowing available section information. Please ensure you have proper database tables set up.`)
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
    console.log('Copied section code:', code)
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

    console.log('Starting subject save process...')
    console.log('Form data:', formData.value)

    // Prepare subject data
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

      console.log('Updated subject:', updatedSubject)

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
      console.log('Created new subject:', newSubject)
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

      console.log(`Processing section ${i + 1}:`, section.name)

      // Ensure section code is unique
      while (!isSectionUnique && sectionAttempts < maxAttempts) {
        const subjectPrefix = formData.value.name.substring(0, 3).toUpperCase().replace(/[^A-Z]/g, '') || 'SUB'
        const gradeLevel = formData.value.grade_level
        const cleanSectionName = section.name.replace(/[^a-zA-Z0-9]/g, '').substring(0, 1).toUpperCase() || 'S'
        const uniqueTimestamp = (baseTimestamp + i + sectionAttempts).toString().slice(-5)
        const randomSuffix = Math.random().toString(36).substring(2, 3).toUpperCase()
        
        sectionCode = `${subjectPrefix}${gradeLevel}-${cleanSectionName}${uniqueTimestamp}${randomSuffix}`
        
        console.log('Generated section code:', sectionCode)
        
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
          console.log('Section code is unique:', sectionCode)
        } else {
          console.log('Section code exists, generating new one...')
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

    console.log('Sections to insert:', sectionsToInsert)

    // Insert all sections
    const { data: insertedSections, error: sectionsError } = await supabase
      .from('sections')
      .insert(sectionsToInsert)
      .select()

    if (sectionsError) {
      console.error('Error inserting sections:', sectionsError)
      throw sectionsError
    }

    console.log('Inserted sections:', insertedSections)

    // Close modal first
    closeModal()

    // Force refresh subjects list with delay to ensure database consistency
    console.log('Subject saved successfully, refreshing list...')
    setTimeout(async () => {
      await fetchSubjects()
      console.log('Subjects list refreshed after creation')
    }, 500)

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
    console.log('Deleting subject:', subjectId)

    // Delete subject (CASCADE will handle sections and enrollments)
    const { error } = await supabase
      .from('subjects')
      .delete()
      .eq('id', subjectId)

    if (error) throw error

    console.log('Subject deleted successfully, refreshing list...')
    await fetchSubjects()
    alert(`Subject "${subject?.name}" deleted successfully!`)
  } catch (error) {
    console.error('Error deleting subject:', error)
    alert(`Error deleting subject: ${error.message}`)
  } finally {
    isLoading.value = false
  }
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

const closeStudentRosterModal = () => {
  showStudentRosterModal.value = false
  currentStudentRoster.value = null
}

const formatEnrollmentDate = (dateString) => {
  if (!dateString) return 'N/A'
  const date = new Date(dateString)
  return date.toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'short',
    day: 'numeric'
  })
}

const exportStudentRoster = () => {
  if (!currentStudentRoster.value) return
  
  // Create CSV content
  let csvContent = `Subject: ${currentStudentRoster.value.subject.name} (Grade ${currentStudentRoster.value.subject.grade_level})\n`
  csvContent += `Total Students: ${currentStudentRoster.value.totalActualStudents}\n\n`
  
  Object.keys(currentStudentRoster.value.studentsBySection).forEach(sectionKey => {
    const sectionData = currentStudentRoster.value.studentsBySection[sectionKey]
    csvContent += `Section: ${sectionData.section.name} (${sectionData.section.section_code})\n`
    csvContent += `Student ID,First Name,Last Name,Email,Grade,Enrollment Date\n`
    
    sectionData.students.forEach(student => {
      csvContent += `"${student.student_id}","${student.first_name}","${student.last_name}","${student.email}","${student.grade_level}","${formatEnrollmentDate(student.enrollment_date)}"\n`
    })
    csvContent += `\n`
  })
  
  // Download CSV
  const blob = new Blob([csvContent], { type: 'text/csv' })
  const url = window.URL.createObjectURL(blob)
  const a = document.createElement('a')
  a.href = url
  a.download = `${currentStudentRoster.value.subject.name}_Student_Roster.csv`
  document.body.appendChild(a)
  a.click()
  document.body.removeChild(a)
  window.URL.revokeObjectURL(url)
}

// Debug function to check database structure
const debugDatabaseStructure = async () => {
  console.log('=== DATABASE STRUCTURE DEBUG ===')
  
  const tablesToCheck = ['students', 'profiles', 'users', 'auth.users']
  
  for (const tableName of tablesToCheck) {
    try {
      console.log(`Checking table: ${tableName}`)
      const { data, error, count } = await supabase
        .from(tableName)
        .select('*', { count: 'exact' })
        .limit(1)
      
      if (error) {
        console.log(`❌ Table ${tableName} error:`, error.message)
      } else {
        console.log(`✅ Table ${tableName} exists with ${count} total records`)
        if (data && data.length > 0) {
          console.log(`Sample record from ${tableName}:`, data[0])
          console.log(`Columns in ${tableName}:`, Object.keys(data[0]))
        }
      }
    } catch (err) {
      console.log(`❌ Exception checking table ${tableName}:`, err)
    }
  }
  
  // Also check what's in enrollments
  try {
    const { data: enrollmentsData, error } = await supabase
      .from('enrollments')
      .select('*')
      .limit(5)
    
    if (!error && enrollmentsData) {
      console.log('Sample enrollments data:', enrollmentsData)
    }
  } catch (err) {
    console.log('Error checking enrollments:', err)
  }
}

// Force refresh function for debugging (updated)
const forceRefresh = async () => {
  console.log('Force refreshing subjects...')
  await debugDatabaseStructure() // Add database debugging
  await fetchSubjects()
}

// Lifecycle
onMounted(async () => {
  console.log('Component mounted, fetching subjects...')
  await fetchSubjects()
})
</script>

<style scoped>
/* Base Styles */
.subjects-page {
  padding: 2rem;
  max-width: 1400px;
  margin: 0 auto;
  background: var(--bg-primary);
  min-height: 100vh;
  color: var(--primary-text-color);
  transition: all 0.3s ease;
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
  margin-bottom: 0.5rem;
}

.stat-label {
  font-size: 0.9rem;
  color: #666;
  font-weight: 600;
}

/* Clickable Student Stats */
.clickable-stat {
  cursor: pointer;
  transition: all 0.3s ease;
  border-radius: 12px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-weight: 600;
  flex-shrink: 0;
  padding: 0.5rem;
  position: relative;
}

.clickable-stat:hover {
  background: rgba(61, 141, 122, 0.1);
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(61, 141, 122, 0.2);
}

.clickable-stat .stat-number {
  font-size: 2rem;
  font-weight: 800;
  color: #3D8D7A;
  margin-bottom: 0.25rem;
  transition: all 0.3s ease;
}

.clickable-stat:hover .stat-number {
  transform: scale(1.1);
}

.clickable-stat .stat-label {
  font-size: 0.9rem;
  color: #666;
  font-weight: 600;
  margin-bottom: 0.25rem;
}

.view-hint {
  display: block;
  color: #3D8D7A;
  font-size: 0.7rem;
  margin-top: 0.2rem;
  font-weight: 500;
  text-align: center;
  opacity: 0;
  transition: opacity 0.3s ease;
}

.clickable-stat:hover .view-hint {
  opacity: 1;
}

.sections-list {
  margin-top: 1.5rem;
}

.sections-list h4 {
  color: #3D8D7A;
  font-size: 1.2rem;
  font-weight: 700;
  margin-bottom: 1rem;
}

.sections {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.section-item {
  padding: 1rem;
  background: rgba(163, 209, 198, 0.1);
  border-radius: 12px;
  border: 1px solid rgba(61, 141, 122, 0.2);
}

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

.section-info {
  width: 100%;
}

.section-name {
  font-weight: 600;
  color: #3D8D7A;
  font-size: 1.1rem;
  margin-bottom: 0.5rem;
  display: block;
}

.section-stats-info {
  margin-bottom: 1rem;
}

.student-count {
  color: #666;
  font-size: 0.9rem;
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

/* Empty State */
.empty-state {
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
  font-size: 1.5rem;
  font-weight: 700;
  margin-bottom: 1rem;
}

.empty-state p {
  font-size: 1.1rem;
  margin-bottom: 2rem;
}

.create-first-btn {
  background: linear-gradient(135deg, #3D8D7A 0%, #A3D1C6 100%);
  color: white;
  border: none;
  padding: 1rem 2rem;
  border-radius: 16px;
  font-weight: 600;
  cursor: pointer;
  font-size: 1rem;
  transition: all 0.3s ease;
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
  backdrop-filter: blur(4px);
}

.modal-content {
  background: white;
  border-radius: 20px;
  padding: 2rem;
  max-width: 600px;
  width: 100%;
  max-height: 90vh;
  overflow-y: auto;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
  position: relative;
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 2rem;
  padding-bottom: 1rem;
  border-bottom: 2px solid rgba(61, 141, 122, 0.1);
}

.modal-header h2 {
  color: #3D8D7A;
  font-size: 1.8rem;
  font-weight: 700;
  margin: 0;
}

.close-btn {
  background: rgba(239, 68, 68, 0.1);
  color: #ef4444;
  border: none;
  padding: 0.5rem;
  border-radius: 10px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.close-btn:hover {
  background: rgba(239, 68, 68, 0.2);
  transform: scale(1.1);
}

.subject-form {
  width: 100%;
}

.step-content {
  animation: slideIn 0.3s ease;
}

@keyframes slideIn {
  from {
    opacity: 0;
    transform: translateX(20px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

.step-title {
  color: #3D8D7A;
  font-size: 1.4rem;
  font-weight: 700;
  margin-bottom: 0.5rem;
}

.step-subtitle {
  color: #666;
  margin-bottom: 2rem;
}

.form-group {
  margin-bottom: 1.5rem;
}

.form-group label {
  display: block;
  font-weight: 600;
  color: #3D8D7A;
  margin-bottom: 0.5rem;
}

.form-group input,
.form-group select {
  width: 100%;
  padding: 0.75rem;
  border: 2px solid rgba(61, 141, 122, 0.2);
  border-radius: 10px;
  font-size: 1rem;
  transition: all 0.3s ease;
  background: white;
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
  gap: 1rem;
  max-height: 300px;
  overflow-y: auto;
  padding: 1rem;
  background: rgba(251, 255, 228, 0.3);
  border-radius: 12px;
  border: 1px solid rgba(61, 141, 122, 0.1);
}

.section-setup-item {
  display: flex;
  align-items: flex-start;
  gap: 1rem;
  padding: 1rem;
  background: white;
  border-radius: 10px;
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
  font-weight: 700;
  font-size: 0.9rem;
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
  backdrop-filter: blur(4px);
}

.loading-content {
  background: white;
  padding: 2rem;
  border-radius: 16px;
  text-align: center;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
  min-width: 200px;
}

.loading-content p {
  color: #3D8D7A;
  font-weight: 600;
  margin: 0;
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

/* Student Roster Modal */
.student-roster-modal {
  max-width: 90vw;
  width: 1200px;
  max-height: 90vh;
}

.roster-subtitle {
  color: #666;
  font-size: 0.9rem;
  margin-top: 0.25rem;
}

.roster-content {
  padding: 1.5rem;
  max-height: 70vh;
  overflow-y: auto;
}

.no-students {
  text-align: center;
  padding: 3rem 2rem;
  color: #666;
}

.no-students .empty-icon {
  color: #A3D1C6;
  margin-bottom: 1rem;
}

.no-students h3 {
  color: #3D8D7A;
  margin-bottom: 0.5rem;
}

.sections-roster {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.section-roster {
  background: rgba(251, 255, 228, 0.3);
  border: 1px solid rgba(61, 141, 122, 0.1);
  border-radius: 16px;
  overflow: hidden;
}

.section-roster-header {
  background: rgba(61, 141, 122, 0.1);
  padding: 1.5rem;
  border-bottom: 1px solid rgba(61, 141, 122, 0.1);
}

.section-roster-header h3 {
  color: #3D8D7A;
  font-size: 1.3rem;
  font-weight: 700;
  margin-bottom: 0.5rem;
}

.section-details {
  display: flex;
  gap: 1rem;
  align-items: center;
}

.students-table {
  background: white;
}

.table-header {
  display: grid;
  grid-template-columns: 120px 200px 250px 80px 120px;
  gap: 1rem;
  padding: 1rem 1.5rem;
  background: rgba(61, 141, 122, 0.05);
  border-bottom: 2px solid rgba(61, 141, 122, 0.1);
  font-weight: 700;
  color: #3D8D7A;
  font-size: 0.85rem;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.table-body {
  max-height: 300px;
  overflow-y: auto;
}

.student-row {
  display: grid;
  grid-template-columns: 120px 200px 250px 80px 120px;
  gap: 1rem;
  padding: 1rem 1.5rem;
  border-bottom: 1px solid rgba(61, 141, 122, 0.1);
  transition: all 0.2s ease;
}

.student-row:hover {
  background: rgba(61, 141, 122, 0.05);
}

.student-row:last-child {
  border-bottom: none;
}

.col-id {
  font-family: 'Courier New', monospace;
  font-weight: 600;
  color: #3D8D7A;
  font-size: 0.9rem;
}

.col-name {
  font-weight: 600;
  color: #333;
}

.col-email {
  color: #666;
  font-size: 0.9rem;
}

.col-grade {
  text-align: center;
  font-weight: 600;
  color: #3D8D7A;
}

.col-date {
  font-size: 0.85rem;
  color: #666;
}

.roster-actions {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.5rem;
  border-top: 1px solid rgba(61, 141, 122, 0.1);
  background: rgba(251, 255, 228, 0.2);
}

.export-btn {
  background: linear-gradient(135deg, #10b981 0%, #34d399 100%);
  color: white;
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 10px;
  cursor: pointer;
  font-weight: 600;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  transition: all 0.3s ease;
}

.export-btn:hover {
  background: linear-gradient(135deg, #059669 0%, #10b981 100%);
  transform: translateY(-1px);
  box-shadow: 0 6px 20px rgba(16, 185, 129, 0.4);
}

.close-roster-btn {
  background: transparent;
  color: #666;
  border: 2px solid #ddd;
  padding: 0.75rem 1.5rem;
  border-radius: 10px;
  cursor: pointer;
  font-weight: 600;
  transition: all 0.3s ease;
}

.close-roster-btn:hover {
  border-color: #3D8D7A;
  color: #3D8D7A;
}

/* Error handling styles */
.error-message {
  background: rgba(239, 68, 68, 0.1);
  border: 1px solid rgba(239, 68, 68, 0.3);
  color: #dc2626;
  padding: 1rem;
  border-radius: 10px;
  margin: 1rem 0;
  text-align: center;
}

.error-message h3 {
  margin: 0 0 0.5rem 0;
  font-weight: 600;
}

.error-message p {
  margin: 0;
  font-size: 0.9rem;
}

/* Responsive Design */
@media (max-width: 1024px) {
  .subjects-grid {
    grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
  }
  
  .student-roster-modal {
    width: 95vw;
    max-width: none;
  }
  
  .table-header,
  .student-row {
    grid-template-columns: 100px 180px 200px 70px 100px;
    font-size: 0.85rem;
  }
}

@media (max-width: 768px) {
  .subjects-page {
    padding: 1rem;
  }
  
  .subjects-grid {
    grid-template-columns: 1fr;
  }
  
  .page-header {
    flex-direction: column;
    align-items: stretch;
  }
  
  .header-content h1 {
    font-size: 2rem;
  }
  
  .create-btn {
    justify-content: center;
    width: 100%;
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
  
  .modal-content {
    padding: 1.5rem;
  }
  
  .section-code-display {
    flex-direction: column;
    align-items: stretch;
    gap: 0.5rem;
  }
  
  .table-header,
  .student-row {
    grid-template-columns: 1fr;
    gap: 0.5rem;
    padding: 1rem;
  }
  
  .table-header {
    display: none;
  }
  
  .student-row {
    display: block;
    border-bottom: 2px solid rgba(61, 141, 122, 0.1);
    margin-bottom: 0.5rem;
  }
  
  .student-row > div {
    display: flex;
    justify-content: space-between;
    padding: 0.25rem 0;
    border-bottom: 1px solid rgba(61, 141, 122, 0.05);
  }
  
  .student-row > div:before {
    content: attr(class);
    font-weight: 600;
    color: #3D8D7A;
    text-transform: capitalize;
  }
  
  .col-id:before { content: "Student ID: "; }
  .col-name:before { content: "Name: "; }
  .col-email:before { content: "Email: "; }
  .col-grade:before { content: "Grade: "; }
  .col-date:before { content: "Enrolled: "; }
  
  .section-setup-item {
    flex-direction: column;
    align-items: stretch;
  }
  
  .section-number {
    align-self: flex-start;
  }
}
</style>