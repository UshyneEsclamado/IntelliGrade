@media (max-width: 768px) {
  .stats-grid {
    gap: 0.25rem;
    margin-bottom: 0.25rem;
  }
  .stat-card {
    gap: 0.25rem;
    padding: 0.5rem 0.5rem;
  }
  .stat-value {
    font-size: 1.1rem;
    margin-right: 0.25rem;
  }
  .stat-label {
    font-size: 0.8rem;
    margin-left: 0.1rem;
  }
}
/* code: Responsive mobile improvements for back button and stat boxes */
@media (max-width: 768px) {
  .section-header-content {
    flex-direction: column;
    align-items: flex-start;
    gap: 0.5rem;
  }
  .back-btn {
    align-self: flex-start;
    margin-bottom: 0.5rem;
    padding: 0.5rem;
    min-width: 0;
    width: 40px;
    height: 40px;
    border-radius: 50%;
    justify-content: center;
    font-size: 1.25rem;
    gap: 0;
  }
  .back-btn span {
    display: none;
  }
  .stats-grid {
    grid-template-columns: 1fr;
    gap: 0.5rem;
    margin-bottom: 0.5rem;
  }
  .stat-card {
    flex-direction: row;
    align-items: center;
    justify-content: flex-start;
    gap: 0.5rem;
    padding: 0.75rem 1rem;
  }
  .stat-value {
    font-size: 1.25rem;
    margin-right: 0.5rem;
  }
  .stat-label {
    font-size: 0.85rem;
    margin-left: 0.25rem;
  }
}

<template>
  <div class="subjects-container">
    <!-- Header Section (Uniform Card Style) -->
    <div class="section-header-card minimal-header-card">
      <div class="section-header-left">
        <div class="section-header-icon minimal-header-icon desktop-only">
          <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M19,3H5C3.9,3 3,3.9 3,5V19C3,20.1 3.9,21 5,21H19C20.1,21 21,20.1 21,19V5C21,3.9 20.1,3 19,3M5,19V5H19V19H5Z" />
          </svg>
        </div>
        <div style="width:100%">
          <div class="section-header-title minimal-header-title">My Subjects</div>
          <div class="section-header-sub minimal-header-sub">View and manage your enrolled subjects</div>
          <!-- Enhanced Mobile Card -->
          <div class="header-stats-mobile formal-mobile-card">
            <div class="formal-mobile-stats">
              <div class="stat-item">
                <span class="stat-number">{{ totalSubjects }}</span>
                <span class="stat-label">Total Subjects</span>
              </div>
              <div class="enrollment-info-badge">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M13,9H11V7H13M13,17H11V11H13M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2Z"/>
                </svg>
                <span>Enrolled by Teacher</span>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="section-header-stats header-stats-desktop">
        <div class="stat-item">
          <span class="stat-number">{{ totalSubjects }}</span>
          <span class="stat-label">Total Subjects</span>
        </div>
        <div class="enrollment-info-badge desktop">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor">
            <path d="M13,9H11V7H13M13,17H11V11H13M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2Z"/>
          </svg>
          <span>Enrolled by Teacher</span>
        </div>
      </div>
    </div>

    <!-- Filter and Search -->
    <div class="controls-section">
      <div class="search-box">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
          <path d="M9.5,3A6.5,6.5 0 0,1 16,9.5C16,11.11 15.41,12.59 14.44,13.73L14.71,14H15.5L20.5,19L19,20.5L14,15.5V14.71L13.73,14.44C12.59,15.41 11.11,16 9.5,16A6.5,6.5 0 0,1 3,9.5A6.5,6.5 0 0,1 9.5,3M9.5,5C7,5 5,7 5,9.5C5,12 7,14 9.5,14C12,14 14,12 14,9.5C14,7 12,5 9.5,5Z" />
        </svg>
        <input 
          type="text" 
          v-model="searchQuery" 
          placeholder="Search subjects..."
          class="search-input"
        />
      </div>
      <div class="filter-tabs">
        <button 
          v-for="filter in filters" 
          :key="filter.key"
          @click="activeFilter = filter.key"
          :class="['filter-tab', { 'active': activeFilter === filter.key }]"
        >
          {{ filter.label }}
        </button>
      </div>
    </div>

    <!-- Subjects Grid -->
    <div class="subjects-grid">
      <div 
        v-for="subject in filteredSubjects" 
        :key="subject.id" 
        :class="[
          'subject-card',
          { 'favorite-card': favoriteSubjects.has(subject.id) },
          { 'archived-card': archivedSubjects.has(subject.id) }
        ]"
      >
        <div class="subject-header">
          <div class="subject-header-left">
            <div class="subject-icon" :style="{ background: subject.color }">
              <span>{{ subject.code.substring(0, 2) }}</span>
            </div>
            <div class="subject-status">
              <span :class="['status-badge', subject.status]">{{ subject.status }}</span>
            </div>
          </div>
          <div class="subject-header-right">
            <!-- Star/Favorite Button -->
            <button 
              @click.stop="toggleFavorite(subject.id)"
              :class="['star-btn', { 'favorited': favoriteSubjects.has(subject.id) }]"
              :title="favoriteSubjects.has(subject.id) ? 'Remove from favorites' : 'Add to favorites'"
            >
              <svg width="20" height="20" viewBox="0 0 24 24" :fill="favoriteSubjects.has(subject.id) ? 'currentColor' : 'none'" stroke="currentColor" stroke-width="2">
                <polygon points="12,2 15.09,8.26 22,9.27 17,14.14 18.18,21.02 12,17.77 5.82,21.02 7,14.14 2,9.27 8.91,8.26 12,2"></polygon>
              </svg>
            </button>
            <!-- Options Menu -->
            <div class="options-menu" :ref="`options-${subject.id}`">
              <button 
                @click.stop="toggleOptionsMenu(subject.id)"
                class="options-btn"
                :title="'More options'"
              >
                <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M12,16A2,2 0 0,1 14,18A2,2 0 0,1 12,20A2,2 0 0,1 10,18A2,2 0 0,1 12,16M12,10A2,2 0 0,1 14,12A2,2 0 0,1 12,14A2,2 0 0,1 10,12A2,2 0 0,1 12,10M12,4A2,2 0 0,1 14,6A2,2 0 0,1 12,8A2,2 0 0,1 10,6A2,2 0 0,1 12,4Z" />
                </svg>
              </button>
              <div v-if="subject.showOptions" class="options-dropdown" @click.stop>
                <button 
                  @click.stop="confirmUnenroll(subject)"
                  class="dropdown-item unenroll-item"
                >
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M19,6.41L17.59,5L12,10.59L6.41,5L5,6.41L10.59,12L5,17.59L6.41,19L12,13.41L17.59,19L19,17.59L13.41,12L19,6.41Z" />
                  </svg>
                  Unenroll from Class
                </button>
                <button 
                  @click.stop="toggleArchive(subject.id)"
                  class="dropdown-item"
                >
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M3,3H21V6.5H20V19A2,2 0 0,1 18,21H6A2,2 0 0,1 4,19V6.5H3V3M6.5,6.5V18.5H17.5V6.5H6.5M8,8V16.5H9.5V8H8M14.5,8V16.5H16V8H14.5Z" />
                  </svg>
                  {{ archivedSubjects.has(subject.id) ? 'Unarchive' : 'Archive' }}
                </button>
              </div>
            </div>
          </div>
        </div>
        
        <div class="subject-content">
          <h3 class="subject-title">{{ subject.name }}</h3>
          <p class="subject-code">{{ subject.code }}</p>
          <p class="subject-instructor">Teacher: {{ subject.instructor }}</p>
          <p class="subject-section">Section: {{ subject.section }}</p>
          <p class="subject-grade">Grade {{ subject.gradeLevel }}</p>
        </div>
        
        <div class="subject-stats compact">
          <div class="stat">
            <span class="stat-value">{{ subject.totalAssessments || 0 }}</span>
            <span class="stat-text">Total</span>
          </div>
          <div class="stat">
            <span class="stat-value">{{ subject.completedAssessments || 0 }}</span>
            <span class="stat-text">Completed</span>
          </div>
          <div class="stat">
            <span class="stat-value">{{ subject.currentGrade || '--' }}</span>
            <span class="stat-text">Grade</span>
          </div>
        </div>
        
        <!-- Assessment Management Actions -->
        <div class="assessment-actions">
          <h4 class="actions-title">Assessments</h4>
          <div class="action-buttons-grid">
            <!-- Quizzes -->
            <button 
              class="assessment-action-btn quiz-btn"
              @click.stop="viewAssessments(subject, 'quiz')"
              :class="{ 'has-available': subject.availableQuizzes > 0 }"
            >
              <div class="btn-icon quiz-icon">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M9,5V9H21V7.5L22.5,6L21,4.5L19.5,6L18,4.5L16.5,6L18,7.5V9H15V5H9M9,19V15H15V19H9M21,15V13.5L19.5,12L18,13.5V15H21Z" />
                </svg>
              </div>
              <div class="btn-content">
                <span class="btn-title">Quizzes</span>
                <span class="btn-count">{{ subject.availableQuizzes || 0 }} available</span>
              </div>
              <div v-if="subject.availableQuizzes > 0" class="notification-badge">{{ subject.availableQuizzes }}</div>
            </button>

            <!-- Assignments -->
            <button 
              class="assessment-action-btn assignment-btn"
              @click.stop="viewAssessments(subject, 'assignment')"
              :class="{ 'has-available': subject.availableAssignments > 0 }"
            >
              <div class="btn-icon assignment-icon">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M14,2H6A2,2 0 0,0 4,4V20A2,2 0 0,0 6,22H18A2,2 0 0,0 20,20V8L14,2M18,20H6V4H13V9H18V20Z" />
                </svg>
              </div>
              <div class="btn-content">
                <span class="btn-title">Assignments</span>
                <span class="btn-count">{{ subject.availableAssignments || 0 }} available</span>
              </div>
              <div v-if="subject.availableAssignments > 0" class="notification-badge">{{ subject.availableAssignments }}</div>
            </button>
          </div>
        </div>

        <div class="subject-actions compact">
          <button class="action-btn secondary full-width" @click.stop="viewGrades(subject)">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
              <path d="M19,3H5C3.9,3 3,3.9 3,5V19C3,20.1 3.9,21 5,21H19C20.1,21 21,20.1 21,19V5C21,3.9 20.1,3 19,3M19,19H5V5H19V19M17,12H7V10H17V12M15,16H7V14H15V16M17,8H7V6H17V8Z" />
            </svg>
            View Grades
          </button>
        </div>
      </div>
    </div>

    <!-- Empty State -->
    <div v-if="filteredSubjects.length === 0 && !isLoading" class="empty-state">
      <div class="empty-icon">
        <svg width="64" height="64" viewBox="0 0 24 24" fill="currentColor">
          <path d="M19,3H5C3.9,3 3,3.9 3,5V19C3,20.1 3.9,21 5,21H19C20.1,21 21,20.1 21,19V5C21,3.9 20.1,3 19,3M5,19V5H19V19H5Z" />
        </svg>
      </div>
      <h3>No subjects found</h3>
      <p v-if="searchQuery || activeFilter !== 'all'">Try adjusting your search or filter criteria</p>
      <div v-else class="enrollment-notice">
        <div class="notice-icon">
          <svg width="48" height="48" viewBox="0 0 24 24" fill="currentColor">
            <path d="M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2M12,4A8,8 0 0,1 20,12A8,8 0 0,1 12,20A8,8 0 0,1 4,12A8,8 0 0,1 12,4M11,16.5L6.5,12L7.91,10.59L11,13.67L16.59,8.09L18,9.5L11,16.5Z"/>
          </svg>
        </div>
        <p class="notice-title">Waiting for Teacher Enrollment</p>
        <p class="notice-description">Your teacher will enroll you in their classes. Once enrolled, your subjects will appear here.</p>
        <div class="notice-tip">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
            <path d="M11,9H13V7H11M12,20C7.59,20 4,16.41 4,12C4,7.59 7.59,4 12,4C16.41,4 20,7.59 20,12C20,16.41 16.41,20 12,20M11,17H13V11H11V17Z"/>
          </svg>
          <span>Contact your teacher if you believe you should be enrolled in a class</span>
        </div>
      </div>
    </div>

    <!-- Unenroll Confirmation Modal -->
    <div v-if="showUnenrollModal" class="modal-overlay" @click="cancelUnenroll">
      <div class="modal-content unenroll-modal" @click.stop>
        <div class="modal-header">
          <h2>Confirm Unenrollment</h2>
          <button @click="cancelUnenroll" class="close-btn">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
              <path d="M19,6.41L17.59,5L12,10.59L6.41,5L5,6.41L10.59,12L5,17.59L6.41,19L12,13.41L17.59,19L19,17.59L13.41,12L19,6.41Z" />
            </svg>
          </button>
        </div>

        <div class="unenroll-content">
          <div class="warning-icon">
            <svg width="48" height="48" viewBox="0 0 24 24" fill="currentColor">
              <path d="M13,13H11V7H13M13,17H11V15H13M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2Z" />
            </svg>
          </div>
          
          <p class="warning-text">
            Are you sure you want to unenroll from <strong>{{ unenrollSubject?.name }}</strong>?
          </p>
          
          <div class="unenroll-details">
            <p><strong>Section:</strong> {{ unenrollSubject?.section }}</p>
            <p><strong>Teacher:</strong> {{ unenrollSubject?.instructor }}</p>
            <p><strong>Code:</strong> {{ unenrollSubject?.code }}</p>
          </div>

          <div class="warning-note">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M13,14H11V10H13M13,18H11V16H13M1,21H23L12,2L1,21Z" />
            </svg>
            <span>This action cannot be undone. You will lose access to all quizzes and grades for this class.</span>
          </div>

          <div class="modal-actions">
            <button type="button" @click="cancelUnenroll" class="cancel-btn">Cancel</button>
            <button type="button" @click="processUnenroll" :disabled="isUnenrolling" class="unenroll-btn">
              {{ isUnenrolling ? 'Unenrolling...' : 'Yes, Unenroll' }}
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Loading Overlay -->
    <div v-if="isLoading" class="loading-overlay">
      <div class="loading-content">
        <div class="loading-spinner-container">
          <div class="loading-spinner"></div>
        </div>
        <p class="loading-text">{{ loadingMessage }}</p>
        <p class="loading-subtext">Please wait a moment...</p>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { supabase } from '../../supabase.js'

export default {
  name: 'StudentSubjects',
  data() {
    return {
      searchQuery: '',
      activeFilter: 'all',
      showUnenrollModal: false,
      isUnenrolling: false,
      isLoading: true,
      loadingMessage: 'Loading your subjects...',
      unenrollSubject: null,
      filters: [
        { key: 'all', label: 'All Subjects' },
        { key: 'favorites', label: 'Favorites' },
        { key: 'active', label: 'Active' },
        { key: 'archived', label: 'Archived' }
      ],
      subjects: [],
      pollingInterval: null,
      currentUser: null,
      studentInfo: null,
      profile: null,
      favoriteSubjects: new Set(),
      archivedSubjects: new Set(),
    };
  },
  watch: {
    $route() {
      this.fetchSubjects();
    }
  },
  computed: {
    totalSubjects() {
      return this.subjects.length;
    },
    filteredSubjects() {
      let filtered = this.subjects;
      
      if (this.activeFilter === 'favorites') {
        filtered = filtered.filter(subject => this.favoriteSubjects.has(subject.id));
      } else if (this.activeFilter === 'archived') {
        filtered = filtered.filter(subject => this.archivedSubjects.has(subject.id));
      } else {
        filtered = filtered.filter(subject => !this.archivedSubjects.has(subject.id));
      }
      
      if (this.activeFilter !== 'all' && this.activeFilter !== 'favorites' && this.activeFilter !== 'archived') {
        filtered = filtered.filter(subject => subject.status === this.activeFilter);
      }
      
      if (this.searchQuery) {
        filtered = filtered.filter(subject => 
          subject.name.toLowerCase().includes(this.searchQuery.toLowerCase()) ||
          subject.code.toLowerCase().includes(this.searchQuery.toLowerCase()) ||
          subject.instructor.toLowerCase().includes(this.searchQuery.toLowerCase())
        );
      }
      
      if (this.activeFilter !== 'archived') {
        filtered.sort((a, b) => {
          const aIsFavorite = this.favoriteSubjects.has(a.id);
          const bIsFavorite = this.favoriteSubjects.has(b.id);
          if (aIsFavorite && !bIsFavorite) return -1;
          if (!aIsFavorite && bIsFavorite) return 1;
          return 0;
        });
      }
      
      return filtered;
    },
  },
  methods: {
    async initializeAuth() {
      try {
        console.log('🔐 Initializing student authentication...')
        
        const { data: { session }, error: sessionError } = await supabase.auth.getSession()
        
        if (sessionError) {
          console.error('❌ Session error:', sessionError)
          throw sessionError
        }
        
        if (!session?.user) {
          console.log('⚠️ No active session found')
          await this.$router.push('/login')
          return false
        }
        
        console.log('✓ Session found for user:', session.user.id)
        this.currentUser = session.user
        
        const { data: profile, error: profileError } = await supabase
          .from('profiles')
          .select('id, role, full_name, email')
          .eq('auth_user_id', session.user.id)
          .maybeSingle()
        
        if (profileError) {
          console.error('❌ Error getting profile:', profileError)
          throw profileError
        }

        if (!profile) {
          console.log('⚠️ Profile not found, creating...')
          const { data: newProfile, error: createError } = await supabase
            .from('profiles')
            .insert({
              auth_user_id: session.user.id,
              full_name: session.user.user_metadata?.full_name || session.user.email?.split('@')[0] || 'Student',
              email: session.user.email,
              role: 'student'
            })
            .select()
            .single()

          if (createError) {
            console.error('❌ Failed to create profile:', createError)
            throw createError
          }

          this.profile = newProfile
          console.log('✓ Profile created')
        } else {
          this.profile = profile
          console.log('✓ Profile loaded')
        }

        if (this.profile.role !== 'student') {
          console.error('❌ Not a student account')
          alert('Access denied. Student account required.')
          await this.$router.push('/login')
          return false
        }

        const { data: student, error: studentError } = await supabase
          .from('students')
          .select('*')
          .eq('profile_id', this.profile.id)
          .maybeSingle()

        if (studentError && studentError.code !== 'PGRST116') {
          console.error('❌ Error getting student info:', studentError)
          throw studentError
        }

        if (!student) {
          console.log('⚠️ Student record not found, creating...')
          
          const gradeLevel = session.user.user_metadata?.grade_level || 7
          
          const { data: newStudent, error: createStudentError } = await supabase
            .from('students')
            .insert({
              profile_id: this.profile.id,
              full_name: this.profile.full_name,
              email: this.profile.email,
              grade_level: gradeLevel,
              is_active: true
            })
            .select()
            .single()

          if (createStudentError) {
            console.error('❌ Failed to create student record:', createStudentError)
            throw createStudentError
          }

          this.studentInfo = newStudent
          console.log('✓ Student record created:', newStudent.id)
        } else {
          if (!student.is_active) {
            console.error('❌ Student account inactive')
            alert('Your account is currently inactive. Please contact support.')
            await this.$router.push('/login')
            return false
          }

          this.studentInfo = student
          console.log('✓ Student info loaded:', student.id)
        }

        return true

      } catch (error) {
        console.error('❌ Auth initialization error:', error)
        alert(`Authentication error: ${error.message || 'Unknown error'}`)
        await this.$router.push('/login')
        return false
      }
    },

    generateSubjectColor(subjectName) {
      const colors = ['#3D8D7A', '#6366f1', '#f59e0b', '#ef4444', '#8b5cf6', '#10b981'];
      const hash = subjectName.split('').reduce((a, b) => {
        a = ((a << 5) - a) + b.charCodeAt(0);
        return a & a;
      }, 0);
      return colors[Math.abs(hash) % colors.length];
    },

    async fetchSubjects() {
      try {
        if (!this.studentInfo?.id) {
          console.log('⚠️ No student info available')
          this.subjects = []
          this.isLoading = false
          return
        }

        console.log('📚 Fetching subjects for student:', this.studentInfo.id)
        this.isLoading = true
        this.loadingMessage = 'Loading your subjects...'

        let { data: enrollments, error: viewError } = await supabase
          .from('student_dashboard')
          .select('*')
          .eq('student_id', this.studentInfo.id)
          .eq('enrollment_status', 'active')

        console.log('View query result:', { enrollments, viewError })

        if (viewError || !enrollments || enrollments.length === 0) {
          console.log('⚠️ View query failed or empty, using direct query...')
          
          const { data: enrollmentsData, error: enrollError } = await supabase
            .from('enrollments')
            .select('id, student_id, section_id, subject_id, status, enrolled_at')
            .eq('student_id', this.studentInfo.id)
            .eq('status', 'active')

          if (enrollError) {
            console.error('❌ Enrollment query error:', enrollError)
            throw enrollError
          }

          if (!enrollmentsData || enrollmentsData.length === 0) {
            console.log('ℹ️ No enrollments found')
            this.subjects = []
            this.isLoading = false
            return
          }

          console.log('✓ Found', enrollmentsData.length, 'enrollments')

          const sectionIds = enrollmentsData.map(e => e.section_id)
          const { data: sectionsData } = await supabase
            .from('sections')
            .select('id, name, section_code, subject_id')
            .in('id', sectionIds)

          const subjectIds = [...new Set(sectionsData.map(s => s.subject_id))]
          const { data: subjectsData } = await supabase
            .from('subjects')
            .select('id, name, grade_level, description, teacher_id')
            .in('id', subjectIds)

          const teacherIds = [...new Set(subjectsData.map(s => s.teacher_id))]
          const { data: teachersData } = await supabase
            .from('teachers')
            .select('id, full_name, email, department')
            .in('id', teacherIds)

          const sectionsMap = new Map(sectionsData.map(s => [s.id, s]))
          const subjectsMap = new Map(subjectsData.map(s => [s.id, s]))
          const teachersMap = new Map(teachersData.map(t => [t.id, t]))

          enrollments = enrollmentsData.map(e => {
            const section = sectionsMap.get(e.section_id)
            const subject = subjectsMap.get(section?.subject_id)
            const teacher = subject ? teachersMap.get(subject.teacher_id) : null

            return {
              enrollment_id: e.id,
              student_id: e.student_id,
              section_id: e.section_id,
              subject_id: subject?.id,
              enrollment_status: e.status,
              enrolled_at: e.enrolled_at,
              section_name: section?.name,
              section_code: section?.section_code,
              subject_name: subject?.name,
              subject_grade_level: subject?.grade_level,
              subject_description: subject?.description,
              teacher_id: teacher?.id,
              teacher_name: teacher?.full_name,
              teacher_email: teacher?.email,
              teacher_department: teacher?.department
            }
          })
        }

        if (!enrollments || enrollments.length === 0) {
          console.log('ℹ️ No enrollments found after processing')
          this.subjects = []
          this.isLoading = false
          return
        }

        console.log('✓ Processing', enrollments.length, 'enrollments')

        const sectionIds = enrollments.map(e => e.section_id)

        // ============================================
        // FETCH QUIZZES - FIXED LOGIC
        // ============================================
        console.log('📝 Fetching quizzes for sections:', sectionIds)
        
        // 🔍 DEBUG: Check ALL quizzes in the entire database first
        const { data: debugAllQuizzes, error: debugError } = await supabase
          .from('quizzes')
          .select('id, section_id, subject_id, title, status, created_at')
          .limit(20)
        
        console.log('🔍 DEBUG - ALL quizzes in database (up to 20):', {
          count: debugAllQuizzes?.length || 0,
          quizzes: debugAllQuizzes,
          error: debugError
        })
        
        if (debugAllQuizzes && debugAllQuizzes.length > 0) {
          console.log('🔍 DEBUG - Section IDs in quizzes table:', debugAllQuizzes.map(q => q.section_id))
          console.log('🔍 DEBUG - Student enrolled section IDs:', sectionIds)
          console.log('🔍 DEBUG - Do any match?', debugAllQuizzes.some(q => sectionIds.includes(q.section_id)))
        }
        
        const { data: allQuizzes, error: quizzesError } = await supabase
          .from('quizzes')
          .select('id, section_id, title, status, start_date, end_date, created_at')
          .in('section_id', sectionIds)
          .eq('status', 'published')  // ✅ CRITICAL: Only fetch published quizzes

        console.log('📊 Quizzes query result:', { 
          count: allQuizzes?.length || 0, 
          error: quizzesError,
          quizzes: allQuizzes 
        })

        if (quizzesError) {
          console.error('❌ Error fetching quizzes:', quizzesError)
        }

        const quizzesBySection = {}
        if (allQuizzes) {
          allQuizzes.forEach(quiz => {
            if (!quizzesBySection[quiz.section_id]) {
              quizzesBySection[quiz.section_id] = []
            }
            quizzesBySection[quiz.section_id].push(quiz)
          })
        }

        console.log('📦 Quizzes grouped by section:', quizzesBySection)

        // Fetch quiz results for student
        const allQuizIds = allQuizzes ? allQuizzes.map(q => q.id) : []
        const resultsByQuizId = {}
        
        if (allQuizIds.length > 0) {
          console.log('📈 Fetching quiz results for', allQuizIds.length, 'quizzes')
          
          const { data: allResults, error: resultsError } = await supabase
            .from('quiz_results')
            .select('quiz_id, best_score, best_percentage, total_attempts')
            .eq('student_id', this.studentInfo.id)
            .in('quiz_id', allQuizIds)
          
          console.log('📊 Quiz results:', { count: allResults?.length || 0, error: resultsError })
          
          if (resultsError) {
            console.error('❌ Error fetching quiz results:', resultsError)
          }
          
          if (allResults) {
            allResults.forEach(result => {
              resultsByQuizId[result.quiz_id] = result
            })
          }
        }

        console.log('📋 Results by quiz ID:', resultsByQuizId)

        // ============================================
        // FETCH ASSIGNMENTS
        // ============================================
        const assignmentsBySection = {}
        const assignmentsCompletedBySection = {}
        
        if (sectionIds.length > 0) {
          console.log('📝 Fetching assignments for sections:', sectionIds)
          
          const { data: allAssignments, error: assignmentsError } = await supabase
            .from('assignments')
            .select('id, section_id, subject_id, status, due_date')
            .in('section_id', sectionIds)
            .eq('status', 'published')

          console.log('📝 Assignments query result:', { 
            count: allAssignments?.length || 0, 
            error: assignmentsError,
            assignments: allAssignments 
          })

          if (assignmentsError) {
            console.error('❌ Error fetching assignments:', assignmentsError)
          }

          if (allAssignments) {
            allAssignments.forEach(assignment => {
              const sectionId = assignment.section_id
              assignmentsBySection[sectionId] = (assignmentsBySection[sectionId] || 0) + 1
            })

            const assignmentIds = allAssignments.map(a => a.id)
            if (assignmentIds.length > 0) {
              const { data: submissions, error: submissionsError } = await supabase
                .from('assignment_submissions')
                .select('assignment_id, assignment:assignments!inner(section_id)')
                .in('assignment_id', assignmentIds)
                .eq('student_id', this.studentInfo.id)

              console.log('📋 Submissions query result:', { 
                count: submissions?.length || 0, 
                error: submissionsError 
              })

              if (submissionsError) {
                console.error('❌ Error fetching submissions:', submissionsError)
              }

              if (submissions) {
                submissions.forEach(submission => {
                  const sectionId = submission.assignment?.section_id || submission.assignments?.section_id
                  if (sectionId) {
                    assignmentsCompletedBySection[sectionId] = (assignmentsCompletedBySection[sectionId] || 0) + 1
                  }
                })
              }
            }
          }

          sectionIds.forEach(sId => {
            if (!(sId in assignmentsBySection)) {
              assignmentsBySection[sId] = 0
            }
            if (!(sId in assignmentsCompletedBySection)) {
              assignmentsCompletedBySection[sId] = 0
            }
          })

          console.log('📊 Assignment counts by section:', assignmentsBySection)
          console.log('📊 Completed assignments by section:', assignmentsCompletedBySection)
        }

        // ============================================
        // BUILD SUBJECTS ARRAY
        // ============================================
        const now = new Date()
        
        const newSubjects = enrollments.map(enrollment => {
          const sectionId = enrollment.section_id
          const subjectId = enrollment.subject_id

          const sectionQuizzes = quizzesBySection[sectionId] || []
          
          console.log(`\n📚 Processing section ${sectionId}:`)
          console.log('  Total quizzes:', sectionQuizzes.length)
          
          // ✅ FIXED: Calculate available quizzes correctly
          const availableQuizzesList = sectionQuizzes.filter(quiz => {
            // Check if quiz has started
            const hasStarted = !quiz.start_date || new Date(quiz.start_date) <= now
            // Check if quiz has not expired
            const hasNotExpired = !quiz.end_date || new Date(quiz.end_date) > now
            // Check if quiz is not completed
            const result = resultsByQuizId[quiz.id]
            const isNotCompleted = !result || result.total_attempts === 0
            
            const isAvailable = hasStarted && hasNotExpired && isNotCompleted
            
            console.log(`  Quiz "${quiz.title}":`, {
              hasStarted,
              hasNotExpired,
              isNotCompleted,
              isAvailable,
              result: result ? `${result.total_attempts} attempts` : 'no attempts'
            })
            
            return isAvailable
          })
          
          const completedQuizIds = sectionQuizzes
            .map(q => q.id)
            .filter(quizId => {
              const result = resultsByQuizId[quizId]
              return result && result.total_attempts > 0
            })

          const totalQuizzes = sectionQuizzes.length
          const completedQuizzes = completedQuizIds.length
          const availableQuizzes = availableQuizzesList.length

          console.log('  Final counts:', {
            total: totalQuizzes,
            completed: completedQuizzes,
            available: availableQuizzes
          })

          // Get assignment counts
          const totalAssignments = assignmentsBySection[sectionId] || 0
          const completedAssignments = assignmentsCompletedBySection[sectionId] || 0
          const availableAssignments = Math.max(0, totalAssignments - completedAssignments)

          console.log(`  Assignments:`, { 
            total: totalAssignments, 
            completed: completedAssignments, 
            available: availableAssignments 
          })

          // Calculate total assessments
          const totalAssessments = totalQuizzes + totalAssignments
          const completedAssessments = completedQuizzes + completedAssignments

          // Calculate grade
          let currentGrade = '--'
          let overallScore = null
          
          if (completedQuizIds.length > 0) {
            const scores = completedQuizIds.map(qId => resultsByQuizId[qId].best_percentage || 0)
            overallScore = scores.reduce((sum, score) => sum + score, 0) / scores.length
            
            if (overallScore >= 95) currentGrade = 'A+'
            else if (overallScore >= 90) currentGrade = 'A'
            else if (overallScore >= 85) currentGrade = 'B+'
            else if (overallScore >= 80) currentGrade = 'B'
            else if (overallScore >= 75) currentGrade = 'C+'
            else if (overallScore >= 70) currentGrade = 'C'
            else if (overallScore >= 65) currentGrade = 'D+'
            else if (overallScore >= 60) currentGrade = 'D'
            else currentGrade = 'F'
          }

          return {
            id: subjectId,
            name: enrollment.subject_name || 'Unknown Subject',
            code: enrollment.section_code || 'NO-CODE',
            section: enrollment.section_name || 'Unknown Section',
            instructor: enrollment.teacher_name || 'Teacher Not Available',
            gradeLevel: enrollment.subject_grade_level || 'N/A',
            color: this.generateSubjectColor(enrollment.subject_name || 'default'),
            status: 'active',
            // Quiz stats
            completedQuizzes,
            availableQuizzes,
            totalQuizzes,
            // Assignment stats
            completedAssignments,
            availableAssignments,
            totalAssignments,
            // Overall stats
            totalAssessments,
            completedAssessments,
            currentGrade,
            overallScore,
            enrollmentId: enrollment.enrollment_id,
            sectionId: sectionId,
            showOptions: false
          }
        })
        
        this.subjects = newSubjects
        console.log('\n✅ Successfully loaded', this.subjects.length, 'subjects')
        console.log('📋 Final subjects data:', this.subjects)

      } catch (error) {
        console.error('❌ Error fetching subjects:', error)
        alert(`Unable to load subjects: ${error.message}`)
        this.subjects = []
      } finally {
        this.isLoading = false
      }
    },

    confirmUnenroll(subject) {
      this.unenrollSubject = subject
      this.showUnenrollModal = true
      this.closeAllOptionsMenus()
    },

    cancelUnenroll() {
      this.showUnenrollModal = false
      this.unenrollSubject = null
    },

    async processUnenroll() {
      if (!this.unenrollSubject || !this.studentInfo) return

      this.isUnenrolling = true

      try {
        const { error } = await supabase
          .from('enrollments')
          .update({ status: 'dropped' })
          .eq('id', this.unenrollSubject.enrollmentId)
          .eq('student_id', this.studentInfo.id)

        if (error) throw error

        this.showUnenrollModal = false
        
        this.favoriteSubjects.delete(this.unenrollSubject.id)
        this.archivedSubjects.delete(this.unenrollSubject.id)
        this.saveUserPreferences()

        await this.fetchSubjects()

        alert(`You have been successfully unenrolled from ${this.unenrollSubject.name}.`)
        this.unenrollSubject = null

      } catch (error) {
        console.error('❌ Unenrollment error:', error)
        alert(`Failed to unenroll: ${error.message}`)
      } finally {
        this.isUnenrolling = false
      }
    },

    viewAssessments(subject, type) {
      if (type === 'assignment') {
        this.$router.push({
          name: 'TakeAssignments',
          params: {
            subjectId: subject.id,
            sectionId: subject.sectionId
          },
          query: {
            subjectName: subject.name,
            sectionName: subject.section,
            instructor: subject.instructor
          }
        })
      } else if (type === 'quiz') {
        this.$router.push({
          name: 'TakeQuiz',
          params: {
            subjectId: subject.id,
            sectionId: subject.sectionId
          },
          query: {
            subjectName: subject.name,
            sectionName: subject.section,
            instructor: subject.instructor
          }
        })
      } else {
        this.$router.push({
          name: 'StudentAssessments',
          params: {
            subjectId: subject.id,
            sectionId: subject.sectionId
          },
          query: {
            subjectName: subject.name,
            sectionName: subject.section,
            type: type,
            instructor: subject.instructor
          }
        })
      }
    },

    takeQuiz(subject) {
      this.$router.push({
        name: 'TakeQuiz',
        params: {
          subjectId: subject.id,
          sectionId: subject.sectionId
        },
        query: {
          subjectName: subject.name,
          sectionName: subject.section,
          gradeLevel: subject.gradeLevel,
          sectionCode: subject.code
        }
      })
    },

    viewGrades(subject) {
      this.$router.push({
        name: 'StudentGrades',
        params: {
          subjectId: subject.id,
          sectionId: subject.sectionId
        },
        query: {
          subjectName: subject.name,
          sectionName: subject.section,
          instructor: subject.instructor,
          currentGrade: subject.currentGrade,
          overallScore: subject.overallScore
        }
      })
    },

    toggleFavorite(subjectId) {
      if (this.favoriteSubjects.has(subjectId)) {
        this.favoriteSubjects.delete(subjectId)
      } else {
        this.favoriteSubjects.add(subjectId)
      }
      this.saveUserPreferences()
    },

    toggleArchive(subjectId) {
      if (this.archivedSubjects.has(subjectId)) {
        this.archivedSubjects.delete(subjectId)
      } else {
        this.archivedSubjects.add(subjectId)
        this.favoriteSubjects.delete(subjectId)
      }
      this.saveUserPreferences()
      this.closeAllOptionsMenus()
    },

    toggleOptionsMenu(subjectId) {
      this.subjects.forEach(subject => {
        if (subject.id !== subjectId) {
          subject.showOptions = false
        }
      })
      
      const subject = this.subjects.find(s => s.id === subjectId)
      if (subject) {
        subject.showOptions = !subject.showOptions
      }
    },

    closeAllOptionsMenus() {
      this.subjects.forEach(subject => {
        subject.showOptions = false
      })
    },

    getUserStorageKey(key) {
      const userId = this.currentUser?.id || 'anonymous'
      return `intelligrade_${key}_${userId}`
    },

    saveUserPreferences() {
      try {
        localStorage.setItem(
          this.getUserStorageKey('favorites'),
          JSON.stringify(Array.from(this.favoriteSubjects))
        )
        localStorage.setItem(
          this.getUserStorageKey('archived'),
          JSON.stringify(Array.from(this.archivedSubjects))
        )
      } catch (error) {
        console.warn('Failed to save preferences:', error)
      }
    },

    loadUserPreferences() {
      try {
        const favoritesData = localStorage.getItem(this.getUserStorageKey('favorites'))
        const archivedData = localStorage.getItem(this.getUserStorageKey('archived'))
        
        if (favoritesData) {
          this.favoriteSubjects = new Set(JSON.parse(favoritesData))
        }
        if (archivedData) {
          this.archivedSubjects = new Set(JSON.parse(archivedData))
        }
      } catch (error) {
        console.warn('Failed to load preferences:', error)
        this.favoriteSubjects = new Set()
        this.archivedSubjects = new Set()
      }
    },
  },

  async mounted() {
    console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    console.log('🚀 COMPONENT MOUNTED')
    console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    
    try {
      const authSuccess = await this.initializeAuth()
      
      if (!authSuccess) {
        console.log('❌ Auth failed')
        return
      }

      this.loadUserPreferences()
      await this.fetchSubjects()
      
      document.addEventListener('click', this.closeAllOptionsMenus)
      
      console.log('✅ INITIALIZATION COMPLETE')
      
    } catch (error) {
      console.error('❌ MOUNT ERROR:', error)
      await this.$router.push('/login')
    }

    supabase.auth.onAuthStateChange(async (event, session) => {
      console.log('🔐 Auth state changed:', event)
      if (event === 'SIGNED_IN' && session?.user) {
        const success = await this.initializeAuth()
        if (success) await this.fetchSubjects()
      } else if (event === 'SIGNED_OUT') {
        this.subjects = []
        this.currentUser = null
        this.studentInfo = null
        await this.$router.push('/login')
      }
    })
  },
  
  beforeUnmount() {
    if (this.pollingInterval) clearInterval(this.pollingInterval)
    document.removeEventListener('click', this.closeAllOptionsMenus)
  }
}
</script>


<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
/* Dark mode for empty state */
.dark .empty-state {
  background: #23272b;
  border-color: #20c997;
  box-shadow: 0 2px 8px rgba(32, 201, 151, 0.08);
}
.dark .empty-icon {
  background: rgba(32, 201, 151, 0.08);
  color: #20c997;
}
.dark .empty-state h3 {
  color: #fbffe4;
}
.dark .empty-state p {
  color: #a3d1c6;
}
/* More dark mode for stats and buttons */
.dark .subject-stats {
  background: #23272b;
  border-color: #20c997;
}
.dark .stat-value {
  color: #20c997;
}
.dark .stat-text {
  color: #a3d1c6;
}
.dark .action-btn.primary {
  background: #20c997;
  color: #181c20;
  box-shadow: 0 2px 8px rgba(32, 201, 151, 0.15);
}
.dark .action-btn.primary:hover {
  background: #3d8d7a;
}
.dark .action-btn.secondary,
.dark .action-btn.clickable {
  background: #23272b;
  color: #20c997;
  border: 1px solid #20c997;
}
.dark .action-btn.clickable:hover {
  background: #181c20;
  border-color: #3d8d7a;
}
.dark .action-btn.completed {
  background: rgba(32, 201, 151, 0.08);
  color: #20c997;
  border: 1px solid #20c997;
}

/* Dark Mode - Assessment Action Buttons */
.dark .assessment-actions {
  border-top-color: rgba(32, 201, 151, 0.2);
}

.dark .actions-title {
  color: #20c997;
}

.dark .assessment-action-btn {
  background: #23272b;
  border-color: #3d4852;
}

.dark .assessment-action-btn:hover {
  box-shadow: 0 4px 12px rgba(32, 201, 151, 0.12);
}

.dark .assessment-action-btn.quiz-btn {
  border-color: #1e3a5f;
  background: linear-gradient(135deg, #23272b 0%, #1a2332 100%);
}

.dark .assessment-action-btn.quiz-btn:hover {
  border-color: #3b82f6;
  box-shadow: 0 4px 12px rgba(59, 130, 246, 0.2);
}

.dark .assessment-action-btn.quiz-btn.has-available {
  border-color: #3b82f6;
  background: linear-gradient(135deg, #1e293b 0%, #1e3a5f 100%);
}

.dark .assessment-action-btn.assignment-btn {
  border-color: #4a1942;
  background: linear-gradient(135deg, #23272b 0%, #2d1b28 100%);
}

.dark .assessment-action-btn.assignment-btn:hover {
  border-color: #ec4899;
  box-shadow: 0 4px 12px rgba(236, 72, 153, 0.2);
}

.dark .assessment-action-btn.assignment-btn.has-available {
  border-color: #ec4899;
  background: linear-gradient(135deg, #27212e 0%, #4a1942 100%);
}

.dark .quiz-icon {
  background: linear-gradient(135deg, #1e3a5f 0%, #1e40af 100%);
  color: #60a5fa;
}

.dark .assignment-icon {
  background: linear-gradient(135deg, #4a1942 0%, #831843 100%);
  color: #f472b6;
}

.dark .btn-title {
  color: #e5e7eb;
}

.dark .btn-count {
  color: #9ca3af;
}

/* DARK MODE OVERRIDES */
.dark .subjects-container {
  background: #181c20;
}

.dark .section-header-card,
.dark .minimal-header-card {
  background: #23272b;
  box-shadow: 0 2px 8px rgba(32, 201, 151, 0.08);
  border: 2px solid #20c997;
}

.dark .minimal-header-icon {
  background: #20c997;
  color: #181c20;
  box-shadow: 0 2px 8px rgba(32, 201, 151, 0.15);
}

.dark .minimal-header-title {
  color: #fbffe4;
}

.dark .minimal-header-sub {
  color: #a3d1c6;
}

.dark .section-header-stats .stat-number {
  color: #20c997;
}

.dark .section-header-stats .stat-label {
  color: #a3d1c6;
}

.dark .controls-section {
  background: #23272b;
  border-color: #20c997;
  box-shadow: 0 2px 8px rgba(32, 201, 151, 0.08);
}

.dark .search-box {
  background: #181c20;
  border-color: #20c997;
}
.dark .search-box svg {
  color: #20c997;
}
.dark .search-input {
  color: #fbffe4;
}
.dark .search-input::placeholder {
  color: #a3d1c6;
}

.dark .filter-tab {
  background: #23272b;
  border-color: #20c997;
  color: #a3d1c6;
}
.dark .filter-tab.active {
  background: #20c997;
  color: #181c20;
  border-color: #20c997;
}
.dark .filter-tab:hover {
  background: #23272b;
  border-color: #3d8d7a;
}

.dark .subjects-grid .subject-card {
  background: #23272b;
  border-color: #20c997;
  color: #fbffe4;
}
.dark .subject-card:hover {
  border-color: #20c997;
}
.dark .subject-card.favorite-card {
  background: rgba(32, 201, 151, 0.08);
  border-color: #ffd600;
}
.dark .subject-card.archived-card {
  background: rgba(163, 209, 198, 0.08);
}
.dark .subject-title,
.dark .subject-instructor,
.dark .subject-section {
  color: #fbffe4;
}
.dark .star-btn {
  color: #a3d1c6;
}
.dark .star-btn:hover {
  background: rgba(255, 193, 7, 0.1);
  color: #ffd600;
}
.dark .options-menu {
  background: #23272b;
  color: #fbffe4;
  border-color: #20c997;
}
.dark .dropdown-item:hover {
  background: #20c997;
  color: #181c20;
}
.dark .subject-preview {
  background: #23272b;
  border-color: #20c997;
}
.dark .preview-card {
  background: #181c20;
  border-color: #20c997;
}
.dark .preview-icon {
  background: #20c997;
  color: #181c20;
}
.dark .loading-overlay {
  background: rgba(24, 28, 32, 0.95);
}
.dark .loading-content {
  background: #23272b;
  border-color: #20c997;
  color: #fbffe4;
}

/* Add border for both light and dark mode */
.section-header-card,
.minimal-header-card {
  border: 2px solid #a3d1c6;
}
.dark .section-header-card,
.dark .minimal-header-card {
  border: 2px solid #20c997;
}


:root {
  --bg-card-muted: rgba(var(--bg-card-rgb, 255, 255, 255), 0.6);
}

.subjects-container {
  padding: 1.5rem;
  max-width: 1200px;
  margin: 0 auto;
  font-family: 'Inter', sans-serif;
  background: #fbffe4;
  min-height: 100vh;
}

.section-header-card {
  display: flex;
  align-items: center;
  background: #fbffe4;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(61, 141, 122, 0.08);
  padding: 1.25rem;
  margin-bottom: 1.5rem;
  min-height: auto;
  gap: 1.25rem;
  justify-content: space-between;
}

.minimal-header-card {
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(61, 141, 122, 0.08);
  background: #fbffe4;
  padding: 1.25rem;
  min-height: auto;
  gap: 1.25rem;
}

.minimal-header-icon {
  width: 48px;
  height: 48px;
  background: #3d8d7a;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #fff;
  box-shadow: 0 2px 8px rgba(61, 141, 122, 0.15);
}

.minimal-header-title {
  font-size: 1.5rem;
  font-weight: 500;
  color: #181c20;
  margin-bottom: 0.25rem;
  letter-spacing: -0.01em;
}

.minimal-header-sub {
  font-size: 0.95rem;
  color: #3d8d7a;
  font-weight: 400;
  margin-bottom: 0;
}

.section-header-left {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.section-header-stats {
  display: flex;
  align-items: center;
  gap: 2rem;
}

.stat-item {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.stat-number {
  font-size: 2rem;
  font-weight: 700;
  color: #3d8d7a;
  line-height: 1;
}

.stat-label {
  font-size: 0.875rem;
  font-weight: 600;
  color: #23272b;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-top: 0.5rem;
}

.enrollment-info-badge {
  background: linear-gradient(135deg, #e0f2fe 0%, #bae6fd 100%);
  color: #0369a1;
  border: 2px solid #7dd3fc;
  padding: 0.625rem 1rem;
  border-radius: 10px;
  font-weight: 600;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.875rem;
  font-family: 'Inter', sans-serif;
  box-shadow: 0 2px 6px rgba(14, 165, 233, 0.1);
  white-space: nowrap;
}

.enrollment-info-badge.desktop {
  padding: 0.75rem 1.25rem;
  font-size: 0.9375rem;
}

.dark .enrollment-info-badge {
  background: linear-gradient(135deg, #075985 0%, #0c4a6e 100%);
  color: #7dd3fc;
  border-color: #0ea5e9;
  box-shadow: 0 2px 6px rgba(14, 165, 233, 0.2);
}

.controls-section {
  background: #fbffe4;
  border-radius: 12px;
  padding: 1.5rem;
  margin-bottom: 1.5rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 2rem;
  box-shadow: 0 2px 8px rgba(61, 141, 122, 0.08);
  border: 2px solid #a3d1c6;
}

.search-box {
  display: flex;
  align-items: center;
  background: white;
  border: 1px solid #a3d1c6;
  border-radius: 10px;
  padding: 0.75rem 1rem;
  gap: 0.75rem;
  min-width: 280px;
  transition: all 0.2s ease;
}

.search-box:focus-within {
  border-color: #3d8d7a;
  box-shadow: 0 0 0 3px rgba(61, 141, 122, 0.08);
}

.search-box svg {
  color: #3d8d7a;
  flex-shrink: 0;
}

.search-input {
  border: none;
  background: transparent;
  outline: none;
  font-size: 0.95rem;
  color: #181c20;
  width: 100%;
  font-family: 'Inter', sans-serif;
}

.search-input::placeholder {
  color: #6b7280;
}

.filter-tabs {
  display: flex;
  gap: 0.5rem;
}

.filter-tab {
  background: white;
  border: 1px solid #a3d1c6;
  border-radius: 8px;
  padding: 0.5rem 1rem;
  cursor: pointer;
  transition: all 0.2s ease;
  font-weight: 500;
  color: #181c20;
  font-family: 'Inter', sans-serif;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.875rem;
}

.filter-count {
  background: rgba(61, 141, 122, 0.1);
  color: #3d8d7a;
  border-radius: 6px;
  padding: 0.15rem 0.5rem;
  font-size: 0.75rem;
  font-weight: 600;
  min-width: 1.2rem;
  text-align: center;
  line-height: 1;
}

.filter-tab.active .filter-count {
  background: rgba(255, 255, 255, 0.25);
  color: white;
}

.filter-tab:hover {
  background: #f8fffe;
  border-color: #3d8d7a;
}

.filter-tab.active {
  background: #3d8d7a;
  color: white;
  border-color: #3d8d7a;
}

.subjects-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 1.2rem;
  margin-bottom: 1.2rem;
}

  .subjects-grid {
    gap: 1rem;
    margin-bottom: 0.25rem;
  }
  .subject-card {
    padding: 1.2rem 1.2rem 1.5rem 1.2rem;
    gap: 0.15rem;
    border-radius: 6px;
    border: 2px solid #3D8D7A;
    box-shadow: 0 2px 8px rgba(61, 141, 122, 0.10);
    background: #fff;
  }
  .subject-header {
    gap: 0.15rem;
    margin-bottom: 0.08rem;
  }

.subject-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 16px rgba(61, 141, 122, 0.12);
  border-color: #3d8d7a;
}

/* Favorite Card Styling */
.subject-card.favorite-card {
  border: 1.5px solid rgba(255, 193, 7, 0.3);
  background: var(--bg-card-translucent);
  position: relative;
}

.subject-card.favorite-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(135deg, rgba(255, 193, 7, 0.02) 0%, rgba(255, 193, 7, 0.05) 100%);
  border-radius: 18px;
  pointer-events: none;
}

.subject-card.favorite-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 16px 48px var(--shadow-medium), 0 0 0 1px rgba(255, 193, 7, 0.1);
}

/* Archived Card Styling */
.subject-card.archived-card {
  opacity: 0.7;
  background: var(--bg-card-muted);
}

.subject-card.archived-card .subject-title,
.subject-card.archived-card .subject-instructor,
.subject-card.archived-card .subject-section {
  color: var(--text-muted);
}

/* Star/Favorite Button Styles */
.star-btn {
  background: none;
  border: none;
  color: var(--text-muted);
  cursor: pointer;
  padding: 0.5rem;
  border-radius: 8px;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  justify-content: center;
}

.star-btn:hover {
  background: rgba(255, 193, 7, 0.1);
  color: #f59e0b;
  transform: scale(1.1);
}

.star-btn.favorited {
  color: #f59e0b;
}

.star-btn.favorited:hover {
  background: rgba(255, 193, 7, 0.2);
  transform: scale(1.1);
}

/* Options Menu Styles */
.options-menu {
  position: relative;
}

.options-btn {
  background: none;
  border: none;
  color: var(--text-muted);
  cursor: pointer;
  padding: 0.5rem;
  border-radius: 8px;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  justify-content: center;
}

.options-btn:hover {
  background: var(--bg-hover);
  color: var(--text-primary);
}

.options-dropdown {
  position: absolute;
  top: 100%;
  right: 0;
  background: var(--bg-card);
  border: 1px solid var(--border-color-light);
  border-radius: 12px;
  box-shadow: 0 8px 32px var(--shadow-medium);
  padding: 0.5rem 0;
  z-index: 10;
  min-width: 140px;
  backdrop-filter: blur(20px);
}

.dropdown-item {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  width: 100%;
  padding: 0.75rem 1rem;
  border: none;
  background: none;
  color: var(--text-primary);
  cursor: pointer;
  transition: all 0.2s ease;
  font-family: 'Inter', sans-serif;
  font-size: 0.875rem;
  font-weight: 500;
  text-align: left;
}

.dropdown-item:hover {
  background: var(--bg-hover);
  color: #3D8D7A;
}





.subject-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
}

.subject-header-left {
  display: flex;
  align-items: flex-start;
  gap: 0.75rem;
}

.subject-header-right {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 0.5rem;
}

.subject-actions-top {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.subject-icon {
  width: 60px;
  height: 60px;
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-weight: 800;
  font-size: 1.25rem;
  box-shadow: 0 8px 32px rgba(61, 141, 122, 0.2);
}

.status-badge {
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
  padding: 0.5rem 1rem;
  border-radius: 12px;
  letter-spacing: 0.5px;
}

.status-badge.active {
  background: rgba(34, 197, 94, 0.2);
  color: #16a34a;
}

.status-badge.completed {
  background: rgba(59, 130, 246, 0.2);
  color: #2563eb;
}

.status-badge.pending {
  background: rgba(255, 193, 7, 0.2);
  color: #e6b000;
}

.subject-content {
  flex: 1;
}

.subject-title {
  font-size: 1.25rem;
  font-weight: 700;
  color: #181c20;
  margin-bottom: 0.5rem;
  line-height: 1.3;
}

.subject-code {
  font-size: 0.875rem;
  font-weight: 600;
  color: #3d8d7a;
  margin-bottom: 0.3rem;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.subject-instructor {
  font-size: 0.95rem;
  color: #23272b;
  margin: 0 0 0.3rem 0;
  font-weight: 500;
}

.subject-section {
  font-size: 0.875rem;
  color: #3d8d7a;
  margin: 0;
  font-weight: 600;
}

.subject-grade {
  font-size: 0.875rem;
  color: #3d8d7a;
  margin: 0.3rem 0 0 0;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.subject-stats {
  background: white;
  border-radius: 10px;
  padding: 1rem;
  display: flex;
  justify-content: space-around;
  gap: 0.75rem;
  border: 1px solid #e6f2ed;
}

.stat {
  text-align: center;
  flex: 1;
}

.stat-value {
  display: block;
  font-size: 1.25rem;
  font-weight: 700;
  color: #3d8d7a;
  line-height: 1;
}

.stat-text {
  font-size: 0.75rem;
  font-weight: 600;
  color: #23272b;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-top: 0.25rem;
}

.subject-actions {
  display: flex;
  gap: 0.75rem;
  position: relative;
  z-index: 2; /* Higher than the card */
}

.action-btn {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  padding: 0.875rem 1rem;
  border-radius: 12px;
  cursor: pointer;
  transition: all 0.3s ease;
  font-weight: 600;
  font-size: 0.875rem;
  border: none;
  font-family: 'Inter', sans-serif;
  pointer-events: auto !important; /* Ensure button is clickable */
  z-index: 1; /* Make sure it's above other elements */
}

.action-btn.primary {
  background: #20c997;
  color: white;
  box-shadow: 0 2px 8px rgba(32, 201, 151, 0.15);
  position: relative;
}

.action-btn.primary:hover {
  background: #1ba085;
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(32, 201, 151, 0.25);
}

.action-btn.secondary {
  background: white;
  color: #3d8d7a;
  border: 1px solid #a3d1c6;
}

.action-btn.primary.pulse {
  animation: pulse-glow 2s infinite;
}

@keyframes pulse-glow {
  0% { box-shadow: 0 4px 16px rgba(61, 141, 122, 0.2); }
  50% { box-shadow: 0 4px 20px rgba(61, 141, 122, 0.4), 0 0 20px rgba(61, 141, 122, 0.3); }
  100% { box-shadow: 0 4px 16px rgba(61, 141, 122, 0.2); }
}

.action-btn.completed {
  background: rgba(34, 197, 94, 0.1);
  color: #16a34a;
  border: 1px solid rgba(34, 197, 94, 0.2);
  cursor: default;
}

.action-btn.clickable {
  background: white;
  color: #3d8d7a;
  border: 1px solid #a3d1c6;
  cursor: pointer;
}

.action-btn.clickable:hover {
  transform: translateY(-1px);
  background: #f8fffe;
  border-color: #3d8d7a;
}

/* Assessment Management Section */
.assessment-actions {
  margin: 1.25rem 0;
  padding-top: 1rem;
  border-top: 1px solid rgba(163, 209, 198, 0.3);
}

.actions-title {
  font-size: 0.875rem;
  font-weight: 600;
  color: #3d8d7a;
  margin-bottom: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.action-buttons-grid {
  display: grid;
  gap: 0.625rem;
}

.assessment-action-btn {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.875rem 1rem;
  background: white;
  border: 1.5px solid #e5e7eb;
  border-radius: 10px;
  cursor: pointer;
  transition: all 0.3s ease;
  width: 100%;
  text-align: left;
  position: relative;
}

.assessment-action-btn:hover {
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
}

.assessment-action-btn.quiz-btn {
  border-color: #dbeafe;
  background: linear-gradient(135deg, #ffffff 0%, #f0f9ff 100%);
}

.assessment-action-btn.quiz-btn:hover {
  border-color: #60a5fa;
  box-shadow: 0 4px 12px rgba(96, 165, 250, 0.15);
}

.assessment-action-btn.quiz-btn.has-available {
  border-color: #60a5fa;
  background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%);
}

.assessment-action-btn.assignment-btn {
  border-color: #fce7f3;
  background: linear-gradient(135deg, #ffffff 0%, #fdf2f8 100%);
}

.assessment-action-btn.assignment-btn:hover {
  border-color: #f472b6;
  box-shadow: 0 4px 12px rgba(244, 114, 182, 0.15);
}

.assessment-action-btn.assignment-btn.has-available {
  border-color: #f472b6;
  background: linear-gradient(135deg, #fdf2f8 0%, #fce7f3 100%);
}

.btn-icon {
  flex-shrink: 0;
  width: 36px;
  height: 36px;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease;
}

.quiz-icon {
  background: linear-gradient(135deg, #dbeafe 0%, #bfdbfe 100%);
  color: #2563eb;
}

.assignment-icon {
  background: linear-gradient(135deg, #fce7f3 0%, #fbcfe8 100%);
  color: #db2777;
}

.btn-content {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 0.125rem;
}

.btn-title {
  font-size: 0.9375rem;
  font-weight: 600;
  color: #1f2937;
}

.btn-count {
  font-size: 0.8125rem;
  color: #6b7280;
}

.notification-badge {
  position: absolute;
  right: 1rem;
  top: 50%;
  transform: translateY(-50%);
  background: #ef4444;
  color: white;
  font-size: 0.75rem;
  font-weight: 700;
  padding: 0.25rem 0.5rem;
  border-radius: 12px;
  min-width: 24px;
  text-align: center;
}

.action-btn.full-width {
  width: 100%;
}

.empty-state {
  text-align: center;
  padding: 3rem 2rem;
  background: #fbffe4;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(61, 141, 122, 0.08);
  border: 2px solid #a3d1c6;
}

.empty-icon {
  width: 64px;
  height: 64px;
  background: rgba(61, 141, 122, 0.1);
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #3d8d7a;
  margin: 0 auto 1.5rem;
}

.empty-state h3 {
  font-size: 1.25rem;
  font-weight: 700;
  color: #181c20;
  margin-bottom: 0.75rem;
}

.empty-state p {
  color: #23272b;
  font-size: 0.95rem;
  margin: 0 0 1.5rem 0;
}

/* Enrollment Notice Styles */
.enrollment-notice {
  max-width: 500px;
  margin: 0 auto;
  padding: 2rem;
  background: linear-gradient(135deg, #e0f2fe 0%, #f0f9ff 100%);
  border: 2px solid #7dd3fc;
  border-radius: 16px;
  box-shadow: 0 4px 12px rgba(14, 165, 233, 0.15);
}

.notice-icon {
  width: 64px;
  height: 64px;
  background: linear-gradient(135deg, #0ea5e9 0%, #0284c7 100%);
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  margin: 0 auto 1.5rem;
  box-shadow: 0 4px 12px rgba(14, 165, 233, 0.3);
}

.notice-title {
  font-size: 1.25rem;
  font-weight: 700;
  color: #0c4a6e;
  margin-bottom: 0.75rem;
}

.notice-description {
  color: #075985;
  font-size: 0.9375rem;
  line-height: 1.6;
  margin: 0 0 1.5rem 0;
}

.notice-tip {
  display: flex;
  align-items: flex-start;
  gap: 0.75rem;
  padding: 1rem;
  background: rgba(14, 165, 233, 0.1);
  border-left: 3px solid #0ea5e9;
  border-radius: 8px;
}

.notice-tip svg {
  flex-shrink: 0;
  color: #0284c7;
  margin-top: 0.125rem;
}

.notice-tip span {
  color: #0c4a6e;
  font-size: 0.875rem;
  line-height: 1.5;
  font-weight: 500;
}

.dark .enrollment-notice {
  background: linear-gradient(135deg, #0c4a6e 0%, #075985 100%);
  border-color: #0ea5e9;
  box-shadow: 0 4px 12px rgba(14, 165, 233, 0.25);
}

.dark .notice-icon {
  background: linear-gradient(135deg, #0284c7 0%, #0369a1 100%);
}

.dark .notice-title {
  color: #7dd3fc;
}

.dark .notice-description {
  color: #bae6fd;
}

.dark .notice-tip {
  background: rgba(14, 165, 233, 0.15);
  border-left-color: #0ea5e9;
}

.dark .notice-tip svg {
  color: #7dd3fc;
}

.dark .notice-tip span {
  color: #e0f2fe;
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
  background: #fbffe4;
  border-radius: 12px;
  max-width: 480px;
  width: 100%;
  max-height: 90vh;
  overflow-y: auto;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.15);
  border: 2px solid #a3d1c6;
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.5rem 1.5rem 1rem;
  border-bottom: 1px solid #a3d1c6;
}

.modal-header h2 {
  color: #181c20;
  font-size: 1.25rem;
  font-weight: 700;
  margin: 0;
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
  color: #3d8d7a;
  background: rgba(61, 141, 122, 0.1);
}

.join-form {
  padding: 1.5rem;
}

.form-group {
  margin-bottom: 1.5rem;
}

.form-group label {
  display: block;
  margin-bottom: 0.5rem;
  color: #181c20;
  font-weight: 600;
  font-size: 0.95rem;
}

.input-with-icon {
  position: relative;
  display: flex;
  align-items: center;
}

.input-with-icon svg {
  position: absolute;
  left: 1rem;
  color: #3D8D7A;
  z-index: 1;
}

.input-with-icon input {
  width: 100%;
  padding: 0.75rem 0.75rem 0.75rem 2.5rem;
  border: 1px solid #a3d1c6;
  border-radius: 8px;
  font-size: 0.95rem;
  transition: all 0.2s ease;
  font-family: 'Inter', sans-serif;
  background: white;
}

.input-with-icon input:focus {
  outline: none;
  border-color: #3d8d7a;
  box-shadow: 0 0 0 3px rgba(61, 141, 122, 0.1);
}

.input-with-icon input.error {
  border-color: #ef4444;
}

.form-help {
  display: block;
  margin-top: 0.5rem;
  font-size: 0.875rem;
  color: var(--text-muted);
}

.error-message {
  margin-top: 0.5rem;
  padding: 0.75rem;
  background: rgba(239, 68, 68, 0.1);
  border: 1px solid rgba(239, 68, 68, 0.2);
  border-radius: 8px;
  color: #dc2626;
  font-size: 0.875rem;
  font-weight: 500;
}

.subject-preview {
  margin: 1.5rem 0;
  padding: 1rem;
  background: white;
  border-radius: 10px;
  border: 1px solid #a3d1c6;
}

.subject-preview h3 {
  color: #181c20;
  font-size: 1rem;
  font-weight: 600;
  margin-bottom: 0.75rem;
}

.preview-card {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  background: #f8fffe;
  padding: 0.75rem;
  border-radius: 8px;
  border: 1px solid #e6f2ed;
}

.preview-icon {
  width: 48px;
  height: 48px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-weight: 700;
  font-size: 1.1rem;
  flex-shrink: 0;
}

.preview-info h4 {
  color: #181c20;
  font-size: 1rem;
  font-weight: 700;
  margin-bottom: 0.25rem;
}

.preview-info p {
  color: #23272b;
  font-size: 0.875rem;
  margin: 0.1rem 0;
}

.modal-actions {
  display: flex;
  gap: 1rem;
  justify-content: flex-end;
  margin-top: 2rem;
}

.cancel-btn {
  background: white;
  color: #23272b;
  border: 1px solid #a3d1c6;
  padding: 0.75rem 1.25rem;
  border-radius: 8px;
  cursor: pointer;
  font-weight: 600;
  transition: all 0.2s ease;
  font-family: 'Inter', sans-serif;
}

.cancel-btn:hover {
  border-color: #3d8d7a;
  background: #f8fffe;
}

.join-btn {
  background: #20c997;
  color: white;
  border: none;
  padding: 0.75rem 1.25rem;
  border-radius: 8px;
  cursor: pointer;
  font-weight: 600;
  transition: all 0.2s ease;
  font-family: 'Inter', sans-serif;
}

.join-btn:hover {
  background: #1ba085;
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(32, 201, 151, 0.25);
}

.join-btn:disabled {
  pointer-events: none;
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
  background: rgba(251, 255, 228, 0.95);
  backdrop-filter: blur(8px);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 9999;
  animation: fadeIn 0.3s ease;
}

@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

.loading-content {
  background: white;
  padding: 3rem 4rem;
  border-radius: 20px;
  text-align: center;
  box-shadow: 0 20px 60px rgba(61, 141, 122, 0.15);
  border: 2px solid #a3d1c6;
  animation: slideUp 0.4s ease;
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

.loading-spinner-container {
  position: relative;
  width: 80px;
  height: 80px;
  margin: 0 auto 1.5rem;
}

.loading-spinner {
  width: 80px;
  height: 80px;
  border: 5px solid rgba(61, 141, 122, 0.1);
  border-left: 5px solid #3d8d7a;
  border-top: 5px solid #20c997;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin: 0 auto;
  box-shadow: 0 0 20px rgba(61, 141, 122, 0.1);
}

@keyframes spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

.loading-text {
  font-size: 1.25rem;
  font-weight: 700;
  color: #181c20;
  margin: 0 0 0.5rem 0;
  font-family: 'Inter', sans-serif;
}

.loading-subtext {
  font-size: 0.95rem;
  font-weight: 500;
  color: #3d8d7a;
  margin: 0;
  font-family: 'Inter', sans-serif;
}

/* ==================== END NEW LOADING STYLES ==================== */

/* ==================== MOBILE RESPONSIVE STYLES ==================== */

@media (max-width: 1024px) {
  .subjects-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 1.25rem;
  }
}

@media (max-width: 768px) {
  /* Remove icon for mobile: adjust left padding if needed */
  .section-header-left > .section-header-icon {
    display: none !important;
  }
  .section-header-left > div[style] {
    width: 100%;
  }
  .subjects-container {
    padding: 0.25rem;
    min-height: calc(100vh - 120px);
  }

  /* Header optimizations for mobile */
  .section-header-card,
  .minimal-header-card {
    margin: 0.5rem;
    margin-bottom: 0.75rem;
    padding: 0.5rem;
    border-radius: 10px;
  }

  .minimal-header-icon {
    width: 50px;
    height: 50px;
  }

  .minimal-header-title {
    font-size: 1.25rem;
    margin-bottom: 0.25rem;
  }

  .minimal-header-sub {
    font-size: 0.9rem;
  }

  .section-header-stats {
    flex-direction: row;
    gap: 1.5rem;
    margin-top: 1rem;
  }

  .stat-item {
    text-align: center;
  }

  .stat-number {
    font-size: 1.5rem;
  }

  .stat-label {
    font-size: 0.8rem;
  }

  .join-class-btn {
    padding: 0.75rem 1.25rem;
    font-size: 0.9rem;
    border-radius: 12px;
    width: 100%;
    margin-top: 1rem;
  }

  /* Controls section mobile optimization */
  .controls-section {
    margin: 0 1rem 1.5rem 1rem;
    flex-direction: column;
    gap: 1rem;
    padding: 1rem;
    border-radius: 12px;
  }

  .search-box {
    width: 100%;
    max-width: none;
  }

  .search-input {
    padding: 0.875rem 1rem 0.875rem 2.5rem;
    font-size: 1rem;
    border-radius: 12px;
  }

  .filter-tabs {
    width: 100%;
    overflow-x: auto;
    padding-bottom: 0.25rem;
  }

  .filter-tab {
    padding: 0.75rem 1rem;
    font-size: 0.85rem;
    white-space: nowrap;
    border-radius: 10px;
    min-width: auto;
  }

  .filter-count {
    font-size: 0.75rem;
    padding: 0.2rem 0.5rem;
  }

  /* Subjects grid mobile layout */
  .subjects-grid {
    grid-template-columns: 1fr;
    gap: 1rem;
    margin: 0 1rem;
  }

  .subject-card {
    padding: 1.25rem;
    border-radius: 16px;
  }

  .subject-header {
    margin-bottom: 1rem;
  }

  .subject-header-right {
    gap: 0.75rem;
  }

  .star-btn,
  .options-btn {
    width: 40px;
    height: 40px;
    border-radius: 10px;
  }

  .subject-icon {
    width: 50px;
    height: 50px;
    border-radius: 12px;
    margin-bottom: 0.75rem;
  }

  .subject-title {
    font-size: 1.1rem;
    margin-bottom: 0.5rem;
  }

  .subject-code {
    font-size: 0.8rem;
    padding: 0.4rem 0.75rem;
    border-radius: 8px;
  }

  .subject-instructor {
    font-size: 0.85rem;
    margin-bottom: 0.25rem;
  }

  .subject-section {
    font-size: 0.8rem;
  }

  .subject-grade {
    font-size: 0.85rem;
    margin: 0.75rem 0;
  }

  .subject-stats {
    margin: 1rem 0;
    gap: 1rem;
  }

  .stat {
    padding: 0.75rem;
    border-radius: 10px;
    min-width: 80px;
  }

  .stat-value {
    font-size: 1.25rem;
  }

  .stat-text {
    font-size: 0.75rem;
  }

  .subject-actions {
    gap: 0.75rem;
    flex-direction: column;
  }

  .action-btn {
    padding: 0.875rem 1.25rem;
    font-size: 0.9rem;
    border-radius: 12px;
    width: 100%;
    min-height: 48px;
  }

  /* Options dropdown mobile optimization */
  .options-dropdown {
    position: fixed;
    bottom: 1rem;
    left: 1rem;
    right: 1rem;
    top: auto;
    transform: none;
    border-radius: 16px;
    max-height: 60vh;
    overflow-y: auto;
  }

  .dropdown-item {
    padding: 1rem;
    font-size: 0.95rem;
    min-height: 56px;
    border-radius: 12px;
  }

  /* Empty state mobile optimization */
  .empty-state {
    padding: 2rem 1rem;
    margin: 1rem;
    border-radius: 16px;
  }

  .empty-icon {
    width: 80px;
    height: 80px;
    margin-bottom: 1rem;
  }

  .empty-state h3 {
    font-size: 1.1rem;
    margin-bottom: 0.75rem;
  }

  .empty-state p {
    font-size: 0.9rem;
    margin-bottom: 1.5rem;
  }

  .join-first-btn {
    padding: 0.875rem 1.5rem;
    font-size: 0.95rem;
    border-radius: 12px;
  }

  /* Modal mobile optimization */
  .modal-overlay {
    padding: 1rem;
  }

  .modal-content {
    margin: 0;
    width: 100%;
    max-width: none;
    border-radius: 16px;
    max-height: 85vh;
    overflow-y: auto;
  }

  .modal-header {
    padding: 1.25rem;
    border-radius: 16px 16px 0 0;
  }

  .modal-header h2 {
    font-size: 1.1rem;
  }

  .close-btn {
    width: 40px;
    height: 40px;
    border-radius: 10px;
  }

  .join-form {
    padding: 1.25rem;
  }

  .form-group {
    margin-bottom: 1.25rem;
  }

  .form-group label {
    font-size: 0.9rem;
    margin-bottom: 0.5rem;
  }

  .input-with-icon input {
    padding: 0.875rem 1rem 0.875rem 2.75rem;
    font-size: 1rem;
    border-radius: 12px;
  }

  .input-with-icon svg {
    left: 1rem;
  }

  .error-message {
    font-size: 0.85rem;
    padding: 0.75rem;
    border-radius: 10px;
  }

  .modal-actions {
    padding: 1.25rem;
    gap: 0.75rem;
    flex-direction: column;
  }

  .modal-actions .btn {
    width: 100%;
    padding: 0.875rem;
    font-size: 0.95rem;
    border-radius: 12px;
  }

  /* Loading overlay mobile */
  .loading-overlay {
    border-radius: 16px;
  }

  .loading-content {
    padding: 2rem 1rem;
  }

  .loading-text {
    font-size: 1.1rem;
  }

  .loading-subtext {
    font-size: 0.85rem;
  }

  /* Subject preview mobile */
  .subject-preview {
    margin: 1rem;
    border-radius: 16px;
  }

  .preview-card {
    padding: 1.25rem;
    border-radius: 16px;
  }

  .preview-icon {
    width: 60px;
    height: 60px;
    border-radius: 12px;
    margin-bottom: 1rem;
  }
}

@media (max-width: 480px) {
  /* Extra small mobile optimizations */
  .section-header-card,
  .minimal-header-card {
    margin: 0.75rem;
    padding: 0.875rem;
  }

  .minimal-header-title {
    font-size: 1.125rem;
  }

  .section-header-stats {
    gap: 1rem;
  }

  .stat-number {
    font-size: 1.25rem;
  }

  .controls-section {
    margin: 0 0.75rem 1.25rem 0.75rem;
    padding: 0.875rem;
  }

  .subjects-grid {
    margin: 0 0.75rem;
    gap: 0.875rem;
  }

  .subject-card {
    padding: 1rem;
  }

  .subject-icon {
    width: 45px;
    height: 45px;
  }

  .subject-title {
    font-size: 1rem;
  }

  .subject-stats {
    gap: 0.75rem;
  }

  .stat {
    padding: 0.625rem;
    min-width: 70px;
  }

  .stat-value {
    font-size: 1.125rem;
  }

  .action-btn {
    padding: 0.75rem 1rem;
    font-size: 0.85rem;
    min-height: 44px;
  }

  .empty-state {
    margin: 0.75rem;
    padding: 1.5rem 0.875rem;
  }

  .empty-icon {
    width: 70px;
    height: 70px;
  }

  .modal-header,
  .join-form,
  .modal-actions {
    padding: 1rem;
  }

  .dropdown-item {
    padding: 0.875rem;
    min-height: 52px;
  }

  /* Touch optimization for small screens */
  .star-btn,
  .options-btn {
    width: 44px;
    height: 44px;
    border-radius: 10px;
  }

  .filter-tab {
    padding: 0.625rem 0.875rem;
    font-size: 0.8rem;
  }
}

/* iPhone 12 Pro specific optimizations */
@media (max-width: 390px) {
  .section-header-card,
  .minimal-header-card {
    margin: 0.5rem;
  }

  .controls-section {
    margin: 0 0.5rem 1rem 0.5rem;
  }

  .subjects-grid {
    margin: 0 0.5rem;
  }

  .empty-state {
    margin: 0.5rem;
  }

  .options-dropdown {
    left: 0.5rem;
    right: 0.5rem;
  }

  .modal-overlay {
    padding: 0.5rem;
  }
}

/* ==================== END MOBILE RESPONSIVE STYLES ==================== */

/* ==================== UNENROLL MODAL STYLES ==================== */
.unenroll-modal {
  max-width: 500px;
}

.unenroll-content {
  padding: 1.5rem;
}

.warning-icon {
  width: 80px;
  height: 80px;
  background: rgba(239, 68, 68, 0.1);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 1.5rem;
  color: #ef4444;
}

.warning-text {
  text-align: center;
  font-size: 1.1rem;
  color: #181c20;
  margin-bottom: 1.5rem;
  line-height: 1.5;
}

.warning-text strong {
  color: #ef4444;
  font-weight: 700;
}

.unenroll-details {
  background: #f8fffe;
  border: 1px solid #e6f2ed;
  border-radius: 12px;
  padding: 1.25rem;
  margin-bottom: 1.5rem;
}

.unenroll-details p {
  margin: 0.5rem 0;
  color: #23272b;
  font-size: 0.95rem;
}

.unenroll-details strong {
  color: #3d8d7a;
  font-weight: 600;
  margin-right: 0.5rem;
}

.warning-note {
  display: flex;
  align-items: flex-start;
  gap: 0.75rem;
  background: rgba(239, 68, 68, 0.05);
  border: 1px solid rgba(239, 68, 68, 0.2);
  border-radius: 10px;
  padding: 1rem;
  margin-bottom: 1.5rem;
}

.warning-note svg {
  color: #ef4444;
  flex-shrink: 0;
  margin-top: 0.125rem;
}

.warning-note span {
  color: #dc2626;
  font-size: 0.875rem;
  font-weight: 500;
  line-height: 1.5;
}

.unenroll-btn {
  background: #ef4444;
  color: white;
  border: none;
  padding: 0.75rem 1.25rem;
  border-radius: 8px;
  cursor: pointer;
  font-weight: 600;
  transition: all 0.2s ease;
  font-family: 'Inter', sans-serif;
}

.unenroll-btn:hover {
  background: #dc2626;
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(239, 68, 68, 0.25);
}

.unenroll-btn:disabled {
  pointer-events: none;
  opacity: 0.6;
  cursor: not-allowed;
}

.dropdown-item.unenroll-item {
  color: #ef4444;
}

.dropdown-item.unenroll-item:hover {
  background: rgba(239, 68, 68, 0.1);
  color: #dc2626;
}

.dropdown-item.unenroll-item svg {
  color: #ef4444;
}

/* Dark mode unenroll styles */
.dark .unenroll-modal {
  background: #23272b;
  border-color: #20c997;
}

.dark .unenroll-content {
  color: #fbffe4;
}

.dark .warning-icon {
  background: rgba(239, 68, 68, 0.15);
}

.dark .warning-text {
  color: #fbffe4;
}

.dark .warning-text strong {
  color: #ff6b6b;
}

.dark .unenroll-details {
  background: #181c20;
  border-color: #20c997;
}

.dark .unenroll-details p {
  color: #a3d1c6;
}

.dark .unenroll-details strong {
  color: #20c997;
}

.dark .warning-note {
  background: rgba(239, 68, 68, 0.1);
  border-color: rgba(239, 68, 68, 0.3);
}

.dark .warning-note span {
  color: #ff8787;
}

.dark .unenroll-btn {
  background: #ef4444;
}

.dark .unenroll-btn:hover {
  background: #dc2626;
}

.dark .dropdown-item.unenroll-item {
  color: #ff6b6b;
}

.dark .dropdown-item.unenroll-item:hover {
  background: rgba(239, 68, 68, 0.15);
  color: #ff8787;
}

/* Mobile responsive for unenroll modal */
@media (max-width: 768px) {
  .unenroll-modal {
    max-width: none;
    width: 100%;
  }

  .unenroll-content {
    padding: 1.25rem;
  }

  .warning-icon {
    width: 70px;
    height: 70px;
    margin-bottom: 1.25rem;
  }

  .warning-text {
    font-size: 1rem;
    margin-bottom: 1.25rem;
  }

  .unenroll-details {
    padding: 1rem;
    margin-bottom: 1.25rem;
  }

  .unenroll-details p {
    font-size: 0.9rem;
    margin: 0.4rem 0;
  }

  .warning-note {
    padding: 0.875rem;
    gap: 0.625rem;
    margin-bottom: 1.25rem;
  }

  .warning-note span {
    font-size: 0.8rem;
  }

  .modal-actions {
    flex-direction: column;
    gap: 0.75rem;
  }

  .modal-actions .cancel-btn,
  .modal-actions .unenroll-btn {
    width: 100%;
    padding: 0.875rem;
    font-size: 0.95rem;
  }
}

@media (max-width: 480px) {
  .warning-icon {
    width: 60px;
    height: 60px;
  }

  .warning-text {
    font-size: 0.95rem;
  }

  .unenroll-details p {
    font-size: 0.85rem;
  }

  .warning-note span {
    font-size: 0.75rem;
  }
}

/* ==================== END UNENROLL MODAL STYLES ==================== */

/* ==================== VALIDATION LOADING STYLES ==================== */
.validation-loading {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 2rem 1rem;
  margin-top: 1rem;
  background: rgba(61, 141, 122, 0.05);
  border-radius: 12px;
  border: 1px solid rgba(61, 141, 122, 0.2);
}

.validation-spinner {
  width: 40px;
  height: 40px;
  border: 3px solid rgba(61, 141, 122, 0.2);
  border-top: 3px solid #3d8d7a;
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
  margin-bottom: 0.75rem;
}

.validation-loading p {
  color: #3d8d7a;
  font-size: 0.95rem;
  font-weight: 600;
  margin: 0;
}

.dark .validation-loading {
  background: rgba(32, 201, 151, 0.08);
  border-color: rgba(32, 201, 151, 0.3);
}

.dark .validation-spinner {
  border-color: rgba(32, 201, 151, 0.2);
  border-top-color: #20c997;
}

.dark .validation-loading p {
  color: #20c997;
}

@media (max-width: 768px) {
  .validation-loading {
    padding: 1.5rem 1rem;
  }

  .validation-spinner {
    width: 36px;
    height: 36px;
  }

  .validation-loading p {
    font-size: 0.9rem;
  }
}
/* ==================== END VALIDATION LOADING STYLES ==================== */
</style>