<template>
  <div class="sections-container" :class="{ 'dark-mode': isDarkMode }">
    <!-- Header -->
    <div class="header-section">
      <div class="header-content">
        <h1 class="page-title">My Sections</h1>
        <p class="page-subtitle">Manage your assigned sections and student rosters</p>
      </div>
      <button @click="showCreateModal = true" class="create-btn">
        <i class="fas fa-plus"></i>
        Create Section
      </button>
    </div>

    <!-- Stats Cards -->
    <div class="stats-grid">
      <div class="stat-card">
        <div class="stat-icon">
          <i class="fas fa-users"></i>
        </div>
        <div class="stat-content">
          <h3>{{ totalSections }}</h3>
          <p>Total Sections</p>
        </div>
      </div>
      <div class="stat-card">
        <div class="stat-icon">
          <i class="fas fa-user-graduate"></i>
        </div>
        <div class="stat-content">
          <h3>{{ totalStudents }}</h3>
          <p>Total Students</p>
        </div>
      </div>
      <div class="stat-card">
        <div class="stat-icon">
          <i class="fas fa-chart-line"></i>
        </div>
        <div class="stat-content">
          <h3>{{ averageStudentsPerSection }}</h3>
          <p>Avg. Students/Section</p>
        </div>
      </div>
    </div>

    <!-- Sections List -->
    <div class="sections-list">
      <div v-for="section in sections" :key="section.id" class="section-card">
        <div class="section-header">
          <div class="section-info">
            <h3>{{ section.name }}</h3>
            <p class="section-subject">{{ section.subject }}</p>
            <div class="section-meta">
              <span class="meta-item">
                <i class="fas fa-users"></i>
                {{ section.student_count || 0 }} Students
              </span>
              <span class="meta-item">
                <i class="fas fa-calendar"></i>
                {{ section.schedule }}
              </span>
            </div>
          </div>
          <div class="section-actions">
            <button @click="viewSection(section)" class="action-btn view-btn">
              <i class="fas fa-eye"></i>
              View
            </button>
            <button @click="editSection(section)" class="action-btn edit-btn">
              <i class="fas fa-edit"></i>
              Edit
            </button>
            <button @click="deleteSection(section)" class="action-btn delete-btn">
              <i class="fas fa-trash"></i>
              Delete
            </button>
          </div>
        </div>

        <!-- Student List (expandable) -->
        <div v-if="expandedSections.includes(section.id)" class="students-list">
          <div class="students-header">
            <h4>Students ({{ section.students?.length || 0 }})</h4>
            <button @click="showEnrollModal(section)" class="enroll-btn">
              <i class="fas fa-user-plus"></i>
              Enroll Student
            </button>
          </div>
          
          <div v-if="section.students?.length" class="students-grid">
            <div v-for="student in section.students" :key="student.id" class="student-card">
              <div class="student-avatar">
                <img v-if="student.avatar_url" :src="student.avatar_url" :alt="student.full_name">
                <div v-else class="avatar-placeholder">
                  {{ getInitials(student.full_name) }}
                </div>
              </div>
              <div class="student-info">
                <h5>{{ student.full_name }}</h5>
                <p>{{ student.email }}</p>
                <p class="student-id">ID: {{ student.student_id }}</p>
              </div>
              <div class="student-actions">
                <button @click="viewStudentProfile(student)" class="student-action-btn">
                  <i class="fas fa-eye"></i>
                </button>
                <button @click="removeStudent(section, student)" class="student-action-btn remove">
                  <i class="fas fa-times"></i>
                </button>
              </div>
            </div>
          </div>
          
          <div v-else class="empty-students">
            <i class="fas fa-users"></i>
            <p>No students enrolled yet</p>
            <button @click="showEnrollModal(section)" class="enroll-btn">
              Enroll Students
            </button>
          </div>
        </div>
      </div>

      <!-- Empty State -->
      <div v-if="!sections.length" class="empty-state">
        <i class="fas fa-chalkboard"></i>
        <h3>No Sections Yet</h3>
        <p>Create your first section to start managing students</p>
        <button @click="showCreateModal = true" class="create-btn">
          Create Section
        </button>
      </div>
    </div>

    <!-- Create Section Modal -->
    <div v-if="showCreateModal" class="modal-overlay" @click.self="showCreateModal = false">
      <div class="modal">
        <div class="modal-header">
          <h3>Create New Section</h3>
          <button @click="showCreateModal = false" class="close-btn">
            <i class="fas fa-times"></i>
          </button>
        </div>
        
        <form @submit.prevent="createSection" class="modal-form">
          <div class="form-group">
            <label>Section Name</label>
            <input v-model="newSection.name" type="text" required placeholder="e.g., Grade 10-A">
          </div>
          
          <div class="form-group">
            <label>Subject</label>
            <select v-model="newSection.subject" required>
              <option value="">Select Subject</option>
              <option value="Mathematics">Mathematics</option>
              <option value="English">English</option>
              <option value="Science">Science</option>
              <option value="Social Studies">Social Studies</option>
              <option value="Filipino">Filipino</option>
            </select>
          </div>
          
          <div class="form-group">
            <label>Schedule</label>
            <input v-model="newSection.schedule" type="text" required placeholder="e.g., MWF 10:00-11:00 AM">
          </div>
          
          <div class="form-group">
            <label>Room</label>
            <input v-model="newSection.room" type="text" placeholder="e.g., Room 205">
          </div>
          
          <div class="form-group">
            <label>Description</label>
            <textarea v-model="newSection.description" rows="3" placeholder="Optional description"></textarea>
          </div>
          
          <div class="modal-actions">
            <button type="button" @click="showCreateModal = false" class="cancel-btn">Cancel</button>
            <button type="submit" :disabled="loading" class="submit-btn">
              {{ loading ? 'Creating...' : 'Create Section' }}
            </button>
          </div>
        </form>
      </div>
    </div>

    <!-- Enroll Student Modal -->
    <div v-if="showEnrollStudentModal" class="modal-overlay" @click.self="showEnrollStudentModal = false">
      <div class="modal">
        <div class="modal-header">
          <h3>Enroll Students to {{ selectedSection?.name }}</h3>
          <button @click="showEnrollStudentModal = false" class="close-btn">
            <i class="fas fa-times"></i>
          </button>
        </div>
        
        <div class="modal-content">
          <div class="search-bar">
            <input 
              v-model="studentSearch" 
              type="text" 
              placeholder="Search students by name or email..."
              class="search-input"
            >
          </div>
          
          <div class="available-students">
            <div v-for="student in filteredAvailableStudents" :key="student.id" class="student-item">
              <div class="student-info">
                <div class="student-avatar">
                  <img v-if="student.avatar_url" :src="student.avatar_url" :alt="student.full_name">
                  <div v-else class="avatar-placeholder">
                    {{ getInitials(student.full_name) }}
                  </div>
                </div>
                <div>
                  <h5>{{ student.full_name }}</h5>
                  <p>{{ student.email }}</p>
                  <p class="student-id">ID: {{ student.student_id }}</p>
                </div>
              </div>
              <button @click="enrollStudent(student)" class="enroll-action-btn">
                <i class="fas fa-plus"></i>
                Enroll
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted, computed } from 'vue'
import { supabase } from '../../supabase.js'

export default {
  name: 'SectionsView',
  setup() {
    const sections = ref([])
    const availableStudents = ref([])
    const expandedSections = ref([])
    const loading = ref(false)
    const showCreateModal = ref(false)
    const showEnrollStudentModal = ref(false)
    const selectedSection = ref(null)
    const studentSearch = ref('')
    
    const newSection = ref({
      name: '',
      subject: '',
      schedule: '',
      room: '',
      description: ''
    })

    const totalSections = computed(() => sections.value.length)
    const totalStudents = computed(() => 
      sections.value.reduce((sum, section) => sum + (section.student_count || 0), 0)
    )
    const averageStudentsPerSection = computed(() => 
      totalSections.value ? Math.round(totalStudents.value / totalSections.value) : 0
    )

    const filteredAvailableStudents = computed(() => {
      if (!studentSearch.value) return availableStudents.value
      
      return availableStudents.value.filter(student => 
        student.full_name.toLowerCase().includes(studentSearch.value.toLowerCase()) ||
        student.email.toLowerCase().includes(studentSearch.value.toLowerCase()) ||
        student.student_id.toLowerCase().includes(studentSearch.value.toLowerCase())
      )
    })

    const fetchSections = async () => {
      loading.value = true
      try {
        const { data: user } = await supabase.auth.getUser()
        if (!user.user) return

        const { data: sectionsData, error } = await supabase
          .from('sections')
          .select(`
            *,
            enrollments:student_enrollments(
              student:profiles(*)
            )
          `)
          .eq('teacher_id', user.user.id)

        if (error) throw error

        sections.value = sectionsData.map(section => ({
          ...section,
          students: section.enrollments?.map(enrollment => enrollment.student) || [],
          student_count: section.enrollments?.length || 0
        }))
      } catch (error) {
        console.error('Error fetching sections:', error)
        alert('Error loading sections')
      } finally {
        loading.value = false
      }
    }

    const fetchAvailableStudents = async () => {
      try {
        const { data, error } = await supabase
          .from('profiles')
          .select('*')
          .eq('role', 'student')

        if (error) throw error
        availableStudents.value = data || []
      } catch (error) {
        console.error('Error fetching students:', error)
      }
    }

    const createSection = async () => {
      loading.value = true
      try {
        const { data: user } = await supabase.auth.getUser()
        if (!user.user) return

        const { data, error } = await supabase
          .from('sections')
          .insert([{
            ...newSection.value,
            teacher_id: user.user.id
          }])
          .select()

        if (error) throw error

        sections.value.push({
          ...data[0],
          students: [],
          student_count: 0
        })

        showCreateModal.value = false
        newSection.value = {
          name: '',
          subject: '',
          schedule: '',
          room: '',
          description: ''
        }
      } catch (error) {
        console.error('Error creating section:', error)
        alert('Error creating section')
      } finally {
        loading.value = false
      }
    }

    const viewSection = (section) => {
      const index = expandedSections.value.indexOf(section.id)
      if (index > -1) {
        expandedSections.value.splice(index, 1)
      } else {
        expandedSections.value.push(section.id)
      }
    }

    const editSection = (section) => {
      console.log('Edit section:', section)
    }

    const deleteSection = async (section) => {
      if (!confirm(`Are you sure you want to delete section "${section.name}"?`)) return

      try {
        const { error } = await supabase
          .from('sections')
          .delete()
          .eq('id', section.id)

        if (error) throw error

        sections.value = sections.value.filter(s => s.id !== section.id)
      } catch (error) {
        console.error('Error deleting section:', error)
        alert('Error deleting section')
      }
    }

    const showEnrollModal = (section) => {
      selectedSection.value = section
      showEnrollStudentModal.value = true
      fetchAvailableStudents()
    }

    const enrollStudent = async (student) => {
      try {
        const { error } = await supabase
          .from('student_enrollments')
          .insert([{
            section_id: selectedSection.value.id,
            student_id: student.id
          }])

        if (error) throw error

        const sectionIndex = sections.value.findIndex(s => s.id === selectedSection.value.id)
        if (sectionIndex > -1) {
          sections.value[sectionIndex].students.push(student)
          sections.value[sectionIndex].student_count += 1
        }

        availableStudents.value = availableStudents.value.filter(s => s.id !== student.id)
        alert(`${student.full_name} has been enrolled successfully!`)
      } catch (error) {
        console.error('Error enrolling student:', error)
        alert('Error enrolling student')
      }
    }

    const removeStudent = async (section, student) => {
      if (!confirm(`Remove ${student.full_name} from ${section.name}?`)) return

      try {
        const { error } = await supabase
          .from('student_enrollments')
          .delete()
          .eq('section_id', section.id)
          .eq('student_id', student.id)

        if (error) throw error

        const sectionIndex = sections.value.findIndex(s => s.id === section.id)
        if (sectionIndex > -1) {
          sections.value[sectionIndex].students = sections.value[sectionIndex].students.filter(s => s.id !== student.id)
          sections.value[sectionIndex].student_count -= 1
        }
      } catch (error) {
        console.error('Error removing student:', error)
        alert('Error removing student')
      }
    }

    const viewStudentProfile = (student) => {
      console.log('View student profile:', student)
    }

    const getInitials = (name) => {
      return name.split(' ').map(n => n[0]).join('').toUpperCase()
    }

    onMounted(() => {
      fetchSections()
    })

    return {
      sections,
      availableStudents,
      expandedSections,
      loading,
      showCreateModal,
      showEnrollStudentModal,
      selectedSection,
      studentSearch,
      newSection,
      totalSections,
      totalStudents,
      averageStudentsPerSection,
      filteredAvailableStudents,
      fetchSections,
      createSection,
      viewSection,
      editSection,
      deleteSection,
      showEnrollModal,
      enrollStudent,
      removeStudent,
      viewStudentProfile,
      getInitials
    }
  }
}
</script>

<style scoped>
.sections-container {
  padding: 1.5rem;
  max-width: 1200px;
  margin: 0 auto;
  background: var(--bg-primary);
  min-height: 100vh;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  color: var(--primary-text-color);
  transition: all 0.3s ease;
}

.page-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 2.5rem;
  background: var(--card-background);
  backdrop-filter: blur(20px);
  padding: 2rem;
  border-radius: 1.25rem;
  border: 1px solid var(--card-border-color);
  box-shadow: 0 8px 32px var(--shadow-light);
}

.page-title {
  font-size: 2.25rem;
  font-weight: 700;
  color: var(--primary-text-color);
  margin: 0;
  letter-spacing: -0.025em;
  background: linear-gradient(135deg, var(--accent-color), #059669, #db2777);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.page-subtitle {
  color: var(--secondary-text-color);
  margin: 0.5rem 0 0 0;
  font-size: 1rem;
  font-weight: 400;
}

.page-title {
  font-size: 2.25rem;
  font-weight: 700;
  color: #0f172a;
  margin: 0;
  letter-spacing: -0.025em;
  background: linear-gradient(135deg, #10b981, #059669, #db2777);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.page-subtitle {
  color: #64748b;
  margin: 0.5rem 0 0 0;
  font-size: 1rem;
  font-weight: 400;
}

.create-btn {
  background: linear-gradient(135deg, var(--accent-color) 0%, #059669 50%, #db2777 100%);
  color: var(--text-inverse);
  border: none;
  padding: 0.875rem 1.75rem;
  border-radius: 0.75rem;
  cursor: pointer;
  font-weight: 600;
  font-size: 0.875rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  box-shadow: 0 4px 14px var(--shadow-medium);
}

.create-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 25px var(--shadow-strong);
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 1.5rem;
  margin-bottom: 3rem;
}

.stat-card {
  background: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(20px);
  border-radius: 1.25rem;
  padding: 2rem;
  border: 1px solid rgba(255, 255, 255, 0.2);
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.06);
  display: flex;
  align-items: center;
  gap: 1.25rem;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  position: relative;
  overflow: hidden;
}

.stat-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 3px;
  background: linear-gradient(90deg, #10b981, #059669, #db2777);
}

.stat-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
}

.stat-icon {
  width: 3.5rem;
  height: 3.5rem;
  border-radius: 1rem;
  background: linear-gradient(135deg, #10b981 0%, #059669 50%, #db2777 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-size: 1.5rem;
  box-shadow: 0 8px 16px rgba(79, 70, 229, 0.3);
}

.stat-content h3 {
  font-size: 2rem;
  font-weight: 700;
  color: #0f172a;
  margin: 0;
}

.stat-content p {
  color: #64748b;
  margin: 0.25rem 0 0 0;
  font-size: 0.875rem;
  font-weight: 500;
}

.section-card {
  background: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(20px);
  border-radius: 1.25rem;
  border: 1px solid rgba(255, 255, 255, 0.2);
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.06);
  margin-bottom: 1.5rem;
  overflow: hidden;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.section-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
}

.section-header {
  padding: 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid rgba(148, 163, 184, 0.1);
}

.section-info h3 {
  font-size: 1.5rem;
  font-weight: 700;
  color: #0f172a;
  margin: 0;
}

.section-subject {
  color: #10b981;
  font-weight: 600;
  margin: 0.5rem 0 1rem 0;
  font-size: 0.875rem;
  text-transform: uppercase;
}

.section-meta {
  display: flex;
  gap: 1.5rem;
}

.meta-item {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  color: #64748b;
  font-size: 0.875rem;
  font-weight: 500;
}

.meta-item i {
  color: #10b981;
}

.section-actions {
  display: flex;
  gap: 0.75rem;
}

.action-btn {
  padding: 0.625rem 1.25rem;
  border: none;
  border-radius: 0.625rem;
  cursor: pointer;
  font-size: 0.875rem;
  font-weight: 600;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.view-btn {
  background: rgba(79, 70, 229, 0.1);
  color: #10b981;
  border: 1px solid rgba(79, 70, 229, 0.2);
}

.view-btn:hover {
  background: #10b981;
  color: white;
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(79, 70, 229, 0.3);
}

.edit-btn {
  background: rgba(245, 158, 11, 0.1);
  color: #f59e0b;
  border: 1px solid rgba(245, 158, 11, 0.2);
}

.edit-btn:hover {
  background: #f59e0b;
  color: white;
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(245, 158, 11, 0.3);
}

.delete-btn {
  background: rgba(239, 68, 68, 0.1);
  color: #ef4444;
  border: 1px solid rgba(239, 68, 68, 0.2);
}

.delete-btn:hover {
  background: #ef4444;
  color: white;
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(239, 68, 68, 0.3);
}

.students-list {
  background: rgba(248, 250, 252, 0.5);
  padding: 2rem;
}

.students-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1.5rem;
}

.students-header h4 {
  color: #0f172a;
  font-size: 1.125rem;
  font-weight: 700;
  margin: 0;
}

.enroll-btn {
  background: linear-gradient(135deg, #10b981 0%, #059669 100%);
  color: white;
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 0.75rem;
  cursor: pointer;
  font-size: 0.875rem;
  font-weight: 600;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  box-shadow: 0 4px 14px rgba(16, 185, 129, 0.3);
}

.enroll-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(16, 185, 129, 0.4);
}

.students-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 1.25rem;
}

.student-card {
  background: rgba(255, 255, 255, 0.8);
  backdrop-filter: blur(10px);
  border-radius: 1rem;
  padding: 1.5rem;
  display: flex;
  align-items: center;
  gap: 1rem;
  border: 1px solid rgba(255, 255, 255, 0.2);
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.04);
}

.student-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 12px 32px rgba(0, 0, 0, 0.08);
}

.student-avatar {
  width: 3rem;
  height: 3rem;
  border-radius: 50%;
  overflow: hidden;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.student-avatar img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.avatar-placeholder {
  width: 100%;
  height: 100%;
  background: linear-gradient(135deg, #10b981 0%, #059669 50%, #db2777 100%);
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 0.875rem;
}

.student-info {
  flex: 1;
}

.student-info h5 {
  font-size: 0.95rem;
  font-weight: 600;
  color: #0f172a;
  margin: 0;
}

.student-info p {
  font-size: 0.8rem;
  color: #64748b;
  margin: 0.25rem 0 0 0;
}

.student-id {
  font-weight: 600;
  color: #10b981;
}

.student-actions {
  display: flex;
  gap: 0.5rem;
}

.student-action-btn {
  width: 2.25rem;
  height: 2.25rem;
  border: none;
  border-radius: 0.5rem;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.student-action-btn:not(.remove) {
  background: rgba(79, 70, 229, 0.1);
  color: #10b981;
  border: 1px solid rgba(79, 70, 229, 0.2);
}

.student-action-btn:not(.remove):hover {
  background: #10b981;
  color: white;
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(79, 70, 229, 0.3);
}

.student-action-btn.remove {
  background: rgba(239, 68, 68, 0.1);
  color: #ef4444;
  border: 1px solid rgba(239, 68, 68, 0.2);
}

.student-action-btn.remove:hover {
  background: #ef4444;
  color: white;
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(239, 68, 68, 0.3);
}

.empty-students {
  text-align: center;
  padding: 3rem;
  color: #64748b;
}

.empty-students i {
  font-size: 4rem;
  margin-bottom: 1.5rem;
  color: #cbd5e1;
}

.empty-state {
  text-align: center;
  padding: 4rem;
  color: #64748b;
}

.empty-state i {
  font-size: 5rem;
  margin-bottom: 2rem;
  color: #cbd5e1;
}

.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(15, 23, 42, 0.6);
  backdrop-filter: blur(8px);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
  animation: fadeIn 0.3s ease-out;
}

@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

.modal {
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(20px);
  border-radius: 1.5rem;
  max-width: 500px;
  width: 90%;
  max-height: 90vh;
  overflow-y: auto;
  border: 1px solid rgba(255, 255, 255, 0.2);
  box-shadow: 0 25px 50px rgba(0, 0, 0, 0.15);
  animation: slideUp 0.3s ease-out;
}

@keyframes slideUp {
  from { 
    opacity: 0; 
    transform: translateY(20px); 
  }
  to { 
    opacity: 1; 
    transform: translateY(0); 
  }
}

.modal-header {
  padding: 2rem;
  border-bottom: 1px solid rgba(148, 163, 184, 0.1);
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.modal-header h3 {
  margin: 0;
  color: #0f172a;
  font-weight: 700;
  font-size: 1.5rem;
}

.close-btn {
  background: rgba(239, 68, 68, 0.1);
  border: 1px solid rgba(239, 68, 68, 0.2);
  font-size: 1.125rem;
  cursor: pointer;
  color: #ef4444;
  width: 2.5rem;
  height: 2.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 0.75rem;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.close-btn:hover {
  background: #ef4444;
  color: white;
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(239, 68, 68, 0.3);
}

.modal-form {
  padding: 2rem;
}

.form-group {
  margin-bottom: 1.5rem;
}

.form-group label {
  display: block;
  font-weight: 600;
  color: #0f172a;
  margin-bottom: 0.75rem;
  font-size: 0.875rem;
}

.form-group input,
.form-group select,
.form-group textarea {
  width: 100%;
  padding: 1rem;
  border: 2px solid rgba(148, 163, 184, 0.2);
  border-radius: 0.75rem;
  font-size: 0.875rem;
  background: rgba(255, 255, 255, 0.8);
  backdrop-filter: blur(10px);
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  font-weight: 500;
}

.form-group input:focus,
.form-group select:focus,
.form-group textarea:focus {
  outline: none;
  border-color: #10b981;
  box-shadow: 0 0 0 4px rgba(79, 70, 229, 0.1);
  background: rgba(255, 255, 255, 0.95);
}

.modal-actions {
  display: flex;
  gap: 1rem;
  justify-content: flex-end;
  margin-top: 2rem;
}

.cancel-btn {
  padding: 0.875rem 1.75rem;
  border: 2px solid rgba(148, 163, 184, 0.2);
  background: rgba(255, 255, 255, 0.8);
  color: #64748b;
  border-radius: 0.75rem;
  cursor: pointer;
  font-weight: 600;
  font-size: 0.875rem;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.cancel-btn:hover {
  background: rgba(148, 163, 184, 0.1);
  border-color: rgba(148, 163, 184, 0.3);
  transform: translateY(-1px);
}

.submit-btn {
  padding: 0.875rem 1.75rem;
  background: linear-gradient(135deg, #10b981 0%, #059669 50%, #db2777 100%);
  color: white;
  border: none;
  border-radius: 0.75rem;
  cursor: pointer;
  font-weight: 600;
  font-size: 0.875rem;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  box-shadow: 0 4px 14px rgba(79, 70, 229, 0.3);
}

.submit-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.submit-btn:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(79, 70, 229, 0.4);
}

.modal-content {
  padding: 2rem;
}

.search-input {
  width: 100%;
  padding: 1rem;
  border: 2px solid rgba(148, 163, 184, 0.2);
  border-radius: 0.75rem;
  margin-bottom: 1.5rem;
  background: rgba(255, 255, 255, 0.8);
  backdrop-filter: blur(10px);
  font-weight: 500;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.search-input:focus {
  outline: none;
  border-color: #10b981;
  box-shadow: 0 0 0 4px rgba(79, 70, 229, 0.1);
  background: rgba(255, 255, 255, 0.95);
}

.available-students {
  max-height: 350px;
  overflow-y: auto;
}

.student-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.25rem;
  border: 2px solid rgba(148, 163, 184, 0.1);
  border-radius: 1rem;
  margin-bottom: 1rem;
  background: rgba(255, 255, 255, 0.6);
  backdrop-filter: blur(10px);
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.student-item:hover {
  border-color: rgba(79, 70, 229, 0.2);
  background: rgba(255, 255, 255, 0.8);
  transform: translateY(-1px);
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.06);
}

.enroll-action-btn {
  background: linear-gradient(135deg, #10b981 0%, #059669 100%);
  color: white;
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 0.75rem;
  cursor: pointer;
  font-size: 0.875rem;
  font-weight: 600;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  box-shadow: 0 4px 14px rgba(16, 185, 129, 0.3);
}

.enroll-action-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(16, 185, 129, 0.4);
}

@media (max-width: 768px) {
  .sections-container {
    padding: 1rem;
  }
  
  .header-section {
    flex-direction: column;
    gap: 1.5rem;
    align-items: stretch;
    padding: 1.5rem;
  }
  
  .page-title {
    font-size: 1.875rem;
    text-align: center;
  }
  
  .create-btn {
    justify-content: center;
  }
  
  .stats-grid {
    grid-template-columns: 1fr;
    gap: 1rem;
  }
  
  .section-header {
    flex-direction: column;
    gap: 1.5rem;
    align-items: stretch;
  }
  
  .section-actions {
    justify-content: center;
    flex-wrap: wrap;
  }
  
  .students-header {
    flex-direction: column;
    gap: 1rem;
    align-items: stretch;
  }
  
  .students-grid {
    grid-template-columns: 1fr;
  }
  
  .modal {
    margin: 1rem;
    width: calc(100% - 2rem);
  }
  
  .modal-header,
  .modal-form,
  .modal-content {
    padding: 1.5rem;
  }
  
  .modal-actions {
    flex-direction: column;
    gap: 0.75rem;
  }
  
  .cancel-btn,
  .submit-btn {
    width: 100%;
    justify-content: center;
  }
}

/* Dark Mode Styles */
.dark-mode .sections-container {
  background: var(--bg-primary);
}

.dark-mode .header-section {
  background: rgba(17, 24, 39, 0.95);
  border: 1px solid rgba(255, 255, 255, 0.08);
}

.dark-mode .page-title {
  color: var(--primary-text-color);
}

.dark-mode .page-subtitle {
  color: var(--secondary-text-color);
}

.dark-mode .create-btn {
  background: linear-gradient(135deg, var(--accent-color), #2563eb);
  box-shadow: 0 4px 14px rgba(59, 130, 246, 0.3);
}

.dark-mode .create-btn:hover {
  box-shadow: 0 8px 25px rgba(59, 130, 246, 0.4);
}

.dark-mode .stat-card {
  background: rgba(17, 24, 39, 0.95);
  border: 1px solid rgba(255, 255, 255, 0.08);
  box-shadow: 
    0 4px 12px rgba(0, 0, 0, 0.25),
    0 2px 6px rgba(0, 0, 0, 0.15);
}

.dark-mode .stat-card:hover {
  box-shadow: 
    0 8px 25px rgba(0, 0, 0, 0.4),
    0 4px 12px rgba(0, 0, 0, 0.25);
}

.dark-mode .stat-card h3 {
  color: var(--primary-text-color);
}

.dark-mode .stat-card p {
  color: var(--secondary-text-color);
}

.dark-mode .section-card {
  background: rgba(17, 24, 39, 0.95);
  border: 1px solid rgba(255, 255, 255, 0.08);
  box-shadow: 
    0 4px 12px rgba(0, 0, 0, 0.25),
    0 2px 6px rgba(0, 0, 0, 0.15);
}

.dark-mode .section-card:hover {
  box-shadow: 
    0 8px 25px rgba(0, 0, 0, 0.4),
    0 4px 12px rgba(0, 0, 0, 0.25);
}

.dark-mode .section-card h3 {
  color: var(--primary-text-color);
}

.dark-mode .section-card p {
  color: var(--secondary-text-color);
}

.dark-mode .section-meta .meta-item .label {
  color: var(--secondary-text-color);
}

.dark-mode .section-meta .meta-item .value {
  color: var(--primary-text-color);
}

.dark-mode .section-actions .action-btn {
  background: rgba(75, 85, 99, 0.2);
  border: 1px solid rgba(255, 255, 255, 0.1);
  color: var(--secondary-text-color);
}

.dark-mode .section-actions .action-btn:hover {
  background: rgba(75, 85, 99, 0.3);
  color: var(--primary-text-color);
}

.dark-mode .section-actions .action-btn.primary {
  background: linear-gradient(135deg, var(--accent-color), #2563eb);
  color: white;
}

.dark-mode .section-actions .action-btn.primary:hover {
  box-shadow: 0 6px 20px rgba(59, 130, 246, 0.4);
}

.dark-mode .students-card {
  background: rgba(31, 41, 55, 0.8);
  border: 1px solid rgba(255, 255, 255, 0.05);
}

.dark-mode .students-header h4 {
  color: var(--primary-text-color);
}

.dark-mode .student-card {
  background: rgba(17, 24, 39, 0.8);
  border: 1px solid rgba(255, 255, 255, 0.05);
}

.dark-mode .student-card:hover {
  background: rgba(17, 24, 39, 0.95);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
}

.dark-mode .student-info .student-name {
  color: var(--primary-text-color);
}

.dark-mode .student-info .student-email {
  color: var(--secondary-text-color);
}

.dark-mode .student-actions .action-btn.danger:hover {
  box-shadow: 0 4px 12px rgba(239, 68, 68, 0.4);
}

.dark-mode .modal {
  background: rgba(17, 24, 39, 0.95);
  border: 1px solid rgba(255, 255, 255, 0.08);
  box-shadow: 
    0 20px 50px rgba(0, 0, 0, 0.5),
    0 10px 25px rgba(0, 0, 0, 0.3);
}

.dark-mode .modal-header h2 {
  color: var(--primary-text-color);
}

.dark-mode .close-btn {
  background: rgba(75, 85, 99, 0.2);
  color: var(--secondary-text-color);
}

.dark-mode .close-btn:hover {
  background: #ef4444;
  color: white;
}

.dark-mode .form-group label {
  color: var(--secondary-text-color);
}

.dark-mode .form-group input,
.dark-mode .form-group select,
.dark-mode .form-group textarea {
  background: rgba(17, 24, 39, 0.8);
  border: 2px solid rgba(255, 255, 255, 0.08);
  color: var(--primary-text-color);
}

.dark-mode .form-group input:focus,
.dark-mode .form-group select:focus,
.dark-mode .form-group textarea:focus {
  border-color: var(--accent-color);
  box-shadow: 0 0 0 4px rgba(59, 130, 246, 0.15);
  background: rgba(17, 24, 39, 1);
}

.dark-mode .cancel-btn {
  background: rgba(75, 85, 99, 0.2);
  border: 2px solid rgba(255, 255, 255, 0.1);
  color: var(--secondary-text-color);
}

.dark-mode .cancel-btn:hover {
  background: rgba(75, 85, 99, 0.3);
  border-color: rgba(255, 255, 255, 0.2);
}

.dark-mode .submit-btn {
  background: linear-gradient(135deg, var(--accent-color), #2563eb);
  box-shadow: 0 4px 14px rgba(59, 130, 246, 0.3);
}

.dark-mode .submit-btn:hover:not(:disabled) {
  box-shadow: 0 8px 25px rgba(59, 130, 246, 0.4);
}

.dark-mode .search-input {
  background: rgba(17, 24, 39, 0.8);
  border: 2px solid rgba(255, 255, 255, 0.08);
  color: var(--primary-text-color);
}

.dark-mode .search-input:focus {
  border-color: var(--accent-color);
  box-shadow: 0 0 0 4px rgba(59, 130, 246, 0.15);
  background: rgba(17, 24, 39, 1);
}

.dark-mode .student-item {
  background: rgba(17, 24, 39, 0.6);
  border: 2px solid rgba(255, 255, 255, 0.05);
}

.dark-mode .student-item:hover {
  border-color: rgba(59, 130, 246, 0.3);
  background: rgba(17, 24, 39, 0.8);
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3);
}

.dark-mode .enroll-action-btn {
  box-shadow: 0 4px 14px rgba(16, 185, 129, 0.3);
}

.dark-mode .enroll-action-btn:hover {
  box-shadow: 0 8px 25px rgba(16, 185, 129, 0.4);
}
</style>