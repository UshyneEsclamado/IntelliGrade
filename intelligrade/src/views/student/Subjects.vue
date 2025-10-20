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
              <button class="join-class-btn formal-join-btn" @click="showJoinModal = true">
                <svg width="18" height="18" fill="none" viewBox="0 0 24 24"><path d="M12 5v14m7-7H5" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
                Join Class
              </button>
            </div>
          </div>
        </div>
      </div>
      <div class="section-header-stats header-stats-desktop">
        <div class="stat-item">
          <span class="stat-number">{{ totalSubjects }}</span>
          <span class="stat-label">Total Subjects</span>
        </div>
        <button @click="showJoinModal = true" class="join-class-btn">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
            <path d="M19,13H13V19H11V13H5V11H11V5H13V11H19V13Z" />
          </svg>
          Join Class
        </button>
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
            <span class="stat-value">{{ subject.completedQuizzes }}</span>
            <span class="stat-text">Completed</span>
          </div>
          <div class="stat">
            <span class="stat-value">{{ subject.availableQuizzes }}</span>
            <span class="stat-text">Available</span>
          </div>
          <div class="stat">
            <span class="stat-value">{{ subject.currentGrade || '--' }}</span>
            <span class="stat-text">Grade</span>
          </div>
        </div>
        <div class="subject-actions compact">
          <!-- Dynamic Quiz Button -->
          <button 
            v-if="subject.availableQuizzes > 0"
            class="action-btn primary pulse" 
            @click.stop="takeQuiz(subject)"
            :title="`${subject.availableQuizzes} quiz${subject.availableQuizzes > 1 ? 'zes' : ''} available`"
          >
            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
              <path d="M14,2H6A2,2 0 0,0 4,4V20A2,2 0 0,0 6,22H18A2,2 0 0,0 20,20V8L14,2M18,20H6V4H13V9H18V20Z" />
            </svg>
            Take Quiz ({{ subject.availableQuizzes }})
          </button>
          
          <button 
            v-else-if="subject.completedQuizzes > 0"
            class="action-btn completed"
            @click.stop="viewCompletedQuizzes(subject)"
            disabled
          >
            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
              <path d="M21,7L9,19L3.5,13.5L4.91,12.09L9,16.17L19.59,5.59L21,7Z" />
            </svg>
            All Quizzes Completed
          </button>
          
          <button 
            v-else
            class="action-btn clickable"
            @click.stop="takeQuiz(subject)"
          >
            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
              <path d="M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2M12,17A5,5 0 0,1 7,12A5,5 0 0,1 12,7A5,5 0 0,1 17,12A5,5 0 0,1 12,17Z" />
            </svg>
            Take Quiz
          </button>

          <button class="action-btn secondary" @click.stop="viewGrades(subject)">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
              <path d="M19,3H5C3.9,3 3,3.9 3,5V19C3,20.1 3.9,21 5,21H19C20.1,21 21,20.1 21,19V5C21,3.9 20.1,3 19,3M19,19H5V5H19V19M17,12H7V10H17V12M15,16H7V14H15V16M17,8H7V6H17V8Z" />
            </svg>
            Grades
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
      <p>{{ searchQuery || activeFilter !== 'all' ? 'Try adjusting your search or filter criteria' : 'Join your first class to get started' }}</p>
      <button v-if="!searchQuery && activeFilter === 'all'" @click="showJoinModal = true" class="join-first-btn">
        Join Your First Class
      </button>
    </div>

    <!-- Join Class Modal -->
    <div v-if="showJoinModal" class="modal-overlay" @click="closeJoinModal">
      <div class="modal-content" @click.stop>
        <div class="modal-header">
          <h2>Join a Class</h2>
          <button @click="closeJoinModal" class="close-btn">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
              <path d="M19,6.41L17.59,5L12,10.59L6.41,5L5,6.41L10.59,12L5,17.59L6.41,19L12,13.41L17.59,19L19,17.59L13.41,12L19,6.41Z" />
            </svg>
          </button>
        </div>

        <form @submit.prevent="joinClass" class="join-form">
          <div class="form-group">
            <label for="sectionCode">Section Code</label>
            <div class="input-with-icon">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                <path d="M12,17A2,2 0 0,0 14,15C14,13.89 13.1,13 12,13A2,2 0 0,0 10,15A2,2 0 0,0 12,17M18,8A2,2 0 0,1 20,10V20A2,2 0 0,1 18,22H6A2,2 0 0,1 4,20V10C4,8.89 4.9,8 6,8H7V6A5,5 0 0,1 12,1A5,5 0 0,1 17,6V8H18M12,3A3,3 0 0,0 9,6V8H15V6A3,3 0 0,0 12,3Z" />
              </svg>
              <input
                id="sectionCode"
                v-model="joinForm.sectionCode"
                type="text"
                placeholder="Enter section code (e.g., MAT7-A01234B)"
                required
                :class="{ 'error': joinError }"
                @input="clearJoinError"
              />
            </div>
            <small class="form-help">Ask your teacher for the section code to join their class</small>
            <div v-if="joinError" class="error-message">{{ joinError }}</div>
          </div>

          <div v-if="previewSubject" class="subject-preview">
            <h3>Class Preview</h3>
            <div class="preview-card">
              <div class="preview-icon" :style="{ background: previewSubject.color }">
                {{ previewSubject.code.substring(0, 2) }}
              </div>
              <div class="preview-info">
                <h4>{{ previewSubject.name }}</h4>
                <p>Grade {{ previewSubject.grade_level }}</p>
                <p>Section: {{ previewSubject.section }}</p>
                <p>Teacher: {{ previewSubject.instructor }}</p>
              </div>
            </div>
          </div>

          <div class="modal-actions">
            <button type="button" @click="closeJoinModal" class="cancel-btn">Cancel</button>
            <button type="submit" :disabled="isJoining || !joinForm.sectionCode" class="join-btn">
              {{ isJoining ? 'Joining...' : 'Join Class' }}
            </button>
          </div>
        </form>
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
      showJoinModal: false,
      isJoining: false,
      isLoading: true, // Start with loading true
      loadingMessage: 'Loading your subjects...',
      joinError: '',
      joinSuccess: '',
      previewSubject: null,
      filters: [
        { key: 'all', label: 'All Subjects' },
        { key: 'favorites', label: 'Favorites' },
        { key: 'active', label: 'Active' },
        { key: 'completed', label: 'Completed' },
        { key: 'pending', label: 'Pending' },
        { key: 'archived', label: 'Archived' }
      ],
      subjects: [],
      joinForm: {
        sectionCode: ''
      },
      pollingInterval: null,
      validationTimeout: null,
      currentUser: null,
      studentInfo: null,
      favoriteSubjects: new Set(),
      archivedSubjects: new Set(),
    };
  },
  watch: {
    $route() {
      // Reload subjects data when route changes
      this.fetchSubjects();
    }
  },
  computed: {
    totalSubjects() {
      return this.subjects.length;
    },
    filteredSubjects() {
      let filtered = this.subjects;
      
      // Filter by favorites/archive status first
      if (this.activeFilter === 'favorites') {
        filtered = filtered.filter(subject => this.favoriteSubjects.has(subject.id));
      } else if (this.activeFilter === 'archived') {
        filtered = filtered.filter(subject => this.archivedSubjects.has(subject.id));
      } else {
        // For all other filters, exclude archived subjects
        filtered = filtered.filter(subject => !this.archivedSubjects.has(subject.id));
      }
      
      // Filter by status (only if not favorites or archived)
      if (this.activeFilter !== 'all' && this.activeFilter !== 'favorites' && this.activeFilter !== 'archived') {
        filtered = filtered.filter(subject => subject.status === this.activeFilter);
      }
      
      // Filter by search query
      if (this.searchQuery) {
        filtered = filtered.filter(subject => 
          subject.name.toLowerCase().includes(this.searchQuery.toLowerCase()) ||
          subject.code.toLowerCase().includes(this.searchQuery.toLowerCase()) ||
          subject.instructor.toLowerCase().includes(this.searchQuery.toLowerCase())
        );
      }
      
      // Sort favorites to the top (except when viewing archived)
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
    canJoinClass() {
      return this.joinForm.sectionCode && 
             this.joinForm.sectionCode.length >= 8 && 
             this.previewSubject && 
             !this.joinError && 
             !this.isJoining;
    }
  },
  methods: {
    // Initialize authentication with new database structure
    async initializeAuth() {
      try {
        console.log('Initializing student authentication...')
        
        // Get current session
        const { data: { session }, error: sessionError } = await supabase.auth.getSession()
        
        if (sessionError) {
          console.error('Session error:', sessionError)
          throw sessionError
        }
        
        if (!session?.user) {
          console.log('No active session found')
          await this.$router.push('/login')
          return false
        }
        
        console.log('Session found for user:', session.user.id)
        this.currentUser = session.user
        
        // Get profile info first
        const { data: profile, error: profileError } = await supabase
          .from('profiles')
          .select('id, role, full_name, email')
          .eq('auth_user_id', session.user.id)
          .single()
        
        if (profileError || !profile) {
          console.error('Error getting profile:', profileError)
          alert('User profile not found. Please contact support.')
          await this.$router.push('/login')
          return false
        }

        if (profile.role !== 'student') {
          console.log('User is not a student:', profile.role)
          alert('Access denied. Student account required.')
          await this.$router.push('/login')
          return false
        }

        // Now get the student record using the profile_id
        const { data: student, error: studentError } = await supabase
          .from('students')
          .select('*')
          .eq('profile_id', profile.id)
          .eq('is_active', true)
          .single()

        if (studentError || !student) {
          console.error('Error getting student info:', studentError)
          alert('Student record not found. Please contact support.')
          await this.$router.push('/login')
          return false
        }

        this.studentInfo = student
        console.log('Student info loaded:', this.studentInfo.id)
        return true

      } catch (error) {
        console.error('Authentication initialization error:', error)
        alert(`Authentication error: ${error.message}`)
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

    // Optimized fetch with single batch query
    async fetchSubjects() {
      try {
        if (!this.studentInfo?.id) {
          console.log('No student info available, skipping fetch')
          this.isLoading = false
          return
        }

        console.log('Fetching subjects for student:', this.studentInfo.id)
        this.isLoading = true
        this.loadingMessage = 'Loading your subjects...'

        // Fetch enrollments using the student_dashboard view
        const { data: enrollments, error } = await supabase
          .from('student_dashboard')
          .select('*')
          .eq('student_id', this.studentInfo.id)
          .eq('enrollment_status', 'active')

        if (error) {
          console.error('Database error fetching enrollments:', error)
          throw error
        }

        if (!enrollments || enrollments.length === 0) {
          this.subjects = []
          this.isLoading = false
          return
        }

        console.log('Found', enrollments.length, 'enrollments')

        // Extract all section IDs for batch queries
        const sectionIds = enrollments.map(e => e.section_id)

        // BATCH FETCH: Get all quizzes for all sections in ONE query
        const { data: allQuizzes } = await supabase
          .from('quizzes')
          .select('id, section_id, title, status')
          .in('section_id', sectionIds)
          .eq('status', 'published')

        // Group quizzes by section for quick lookup
        const quizzesBySection = {}
        if (allQuizzes) {
          allQuizzes.forEach(quiz => {
            if (!quizzesBySection[quiz.section_id]) {
              quizzesBySection[quiz.section_id] = []
            }
            quizzesBySection[quiz.section_id].push(quiz)
          })
        }

        // BATCH FETCH: Get all quiz results for this student in ONE query
        const allQuizIds = allQuizzes ? allQuizzes.map(q => q.id) : []
  const resultsByQuizId = {}
        
        if (allQuizIds.length > 0) {
          const { data: allResults } = await supabase
            .from('quiz_results')
            .select('quiz_id, best_score, best_percentage')
            .eq('student_id', this.studentInfo.id)
            .in('quiz_id', allQuizIds)
          
          // Group results by quiz ID for quick lookup
          if (allResults) {
            allResults.forEach(result => {
              resultsByQuizId[result.quiz_id] = result
            })
          }
        }

        // Process all enrollments with pre-fetched data
        const newSubjects = enrollments.map(enrollment => {
          const sectionId = enrollment.section_id
          const subjectId = enrollment.subject_id

          // Get quizzes for this section
          const sectionQuizzes = quizzesBySection[sectionId] || []
          
          // Get completed quiz results for this section
          const completedQuizIds = sectionQuizzes
            .map(q => q.id)
            .filter(quizId => resultsByQuizId[quizId])

          const totalQuizzes = sectionQuizzes.length
          const completedQuizzes = completedQuizIds.length
          const availableQuizzes = Math.max(0, totalQuizzes - completedQuizzes)

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
            completedQuizzes,
            availableQuizzes,
            totalQuizzes,
            currentGrade,
            overallScore,
            enrollmentId: enrollment.enrollment_id,
            sectionId: sectionId,
            showOptions: false
          }
        })
        
        this.subjects = newSubjects
        console.log('Successfully loaded', this.subjects.length, 'subjects')

      } catch (error) {
        console.error('Error fetching subjects:', error)
        
        if (error.code === 'PGRST301' || error.message?.includes('JWT')) {
          alert('Your session has expired. Please log in again.')
          await this.$router.push('/login')
        } else {
          alert(`Unable to load subjects: ${error.message}`)
          this.subjects = []
        }
      } finally {
        this.isLoading = false
      }
    },

    // Validate section code using new schema
    async validateSectionCode() {
      if (!this.joinForm.sectionCode || this.joinForm.sectionCode.length < 8) {
        this.previewSubject = null
        this.joinError = ''
        return
      }

      try {
        const searchCode = this.joinForm.sectionCode.trim().toUpperCase()
        console.log('Validating section code:', searchCode)

        // First, try to find section directly with joins
        const { data: sectionData, error: sectionError } = await supabase
          .from('sections')
          .select(`
            id,
            name,
            section_code,
            max_students,
            is_active,
            subject_id,
            subjects!subject_id (
              id,
              name,
              grade_level,
              is_active,
              teacher_id,
              teachers!teacher_id (
                id,
                full_name,
                is_active
              )
            )
          `)
          .eq('section_code', searchCode)
          .eq('is_active', true)
          .single()

        if (sectionError || !sectionData) {
          console.error('Section lookup error:', sectionError)
          this.joinError = 'Section not found or inactive. Please check with your teacher.'
          this.previewSubject = null
          return
        }

        console.log('Found section data:', sectionData)

        // Check if subject and teacher are active
        // Ensure subjects is an object, not array
        const subjectObj = Array.isArray(sectionData.subjects) ? sectionData.subjects[0] : sectionData.subjects;
        if (!subjectObj || !subjectObj.is_active || !(subjectObj.teachers && subjectObj.teachers[0] && subjectObj.teachers[0].is_active)) {
          this.joinError = 'This section is currently inactive. Please contact your teacher.'
          this.previewSubject = null
          return
        }

        // Check if section has space
        const { count: enrollmentCount } = await supabase
          .from('enrollments')
          .select('id', { count: 'exact' })
          .eq('section_id', sectionData.id)
          .eq('status', 'active')

        const currentEnrollments = enrollmentCount || 0
        const hasSpace = currentEnrollments < sectionData.max_students

        if (!hasSpace) {
          this.joinError = 'This section is full. Please contact your teacher.'
          this.previewSubject = null
          return
        }

        // Check grade level match
        if (this.studentInfo && subjectObj.grade_level !== this.studentInfo.grade_level) {
          this.joinError = `This subject is for Grade ${subjectObj.grade_level} students. You are in Grade ${this.studentInfo.grade_level}.`
          this.previewSubject = null
          return
        }

        // Check if already enrolled in this section
        const { data: existingEnrollment } = await supabase
          .from('enrollments')
          .select('id')
          .eq('student_id', this.studentInfo.id)
          .eq('section_id', sectionData.id)
          .eq('status', 'active')
          .maybeSingle()

        if (existingEnrollment) {
          this.joinError = 'You are already enrolled in this class.'
          this.previewSubject = null
          return
        }

        // Check if already enrolled in same subject (different section)
        const { data: sameSubjectEnrollment } = await supabase
          .from('enrollments')
          .select('id')
          .eq('student_id', this.studentInfo.id)
          .eq('subject_id', sectionData.subject_id)
          .eq('status', 'active')
          .maybeSingle()

        if (sameSubjectEnrollment) {
          this.joinError = 'You are already enrolled in this subject in another section.'
          this.previewSubject = null
          return
        }

        // Show preview - everything is valid
        this.previewSubject = {
          id: sectionData.subject_id,
          name: subjectObj.name,
          code: sectionData.section_code,
          section: sectionData.name,
          instructor: subjectObj.teachers && subjectObj.teachers[0] ? subjectObj.teachers[0].full_name : 'Teacher Name Not Available',
          grade_level: subjectObj.grade_level,
          color: this.generateSubjectColor(subjectObj.name),
          sectionId: sectionData.id
        }
        this.joinError = ''

        console.log('Preview subject set:', this.previewSubject)

      } catch (error) {
        console.error('Error validating section code:', error)
        this.joinError = 'Error validating section code. Please try again.'
        this.previewSubject = null
      }
    },

    // Improved join class with better database sync
    async joinClass() {
      if (!this.joinForm.sectionCode || !this.studentInfo || !this.previewSubject) return

      this.isJoining = true
      this.joinError = ''
      this.joinSuccess = ''

      try {
        console.log('Starting join process for section:', this.joinForm.sectionCode)
        console.log('Preview subject:', this.previewSubject)

        // Use the validate_enrollment function from your schema
        const { data: validation, error: validationError } = await supabase
          .rpc('validate_enrollment', {
            p_student_id: this.studentInfo.id,
            p_section_id: this.previewSubject.sectionId
          })

        if (validationError) {
          console.error('Validation error:', validationError)
          throw new Error('Validation failed: ' + validationError.message)
        }

        console.log('Validation result:', validation)

        if (!validation || validation.length === 0 || !validation[0]?.is_valid) {
          throw new Error(validation?.[0]?.error_message || 'Enrollment validation failed')
        }

        // Create enrollment
        const { data: newEnrollment, error: enrollmentError } = await supabase
          .from('enrollments')
          .insert([{
            student_id: this.studentInfo.id,
            section_id: this.previewSubject.sectionId,
            subject_id: this.previewSubject.id,
            status: 'active'
          }])
          .select()
          .single()

        if (enrollmentError) {
          console.error('Enrollment error:', enrollmentError)
          throw enrollmentError
        }

        console.log('Successfully enrolled:', newEnrollment)

        // Show success message BEFORE closing modal
        this.joinSuccess = `Successfully joined ${this.previewSubject.name}! Loading your updated subjects...`
        this.joinError = ''

        // Wait a moment for database to sync, then refresh subjects
        await new Promise(resolve => setTimeout(resolve, 1500))
        
        // Force a fresh fetch to ensure we get the new enrollment
        await this.fetchSubjects()
        
        // Wait a bit more for UI to update
        await new Promise(resolve => setTimeout(resolve, 500))

        // Close modal 
        this.closeJoinModal()

        // Final confirmation
        setTimeout(() => {
          alert(`Welcome to ${this.previewSubject.name}!\n\nThe subject has been added to your dashboard.`)
        }, 200)

      } catch (error) {
        console.error('Error joining class:', error)
        this.joinError = error.message || 'Failed to join class. Please try again.'
        this.joinSuccess = ''
      } finally {
        this.isJoining = false
      }
    },

    // Improved clearJoinError with better debouncing
    clearJoinError() {
      this.joinError = ''
      this.joinSuccess = ''
      
      clearTimeout(this.validationTimeout)
      this.validationTimeout = setTimeout(() => {
        if (this.joinForm.sectionCode.length >= 8) {
          this.validateSectionCode()
        } else {
          this.previewSubject = null
        }
      }, 800)
    },

    closeJoinModal() {
      this.showJoinModal = false
      this.joinForm.sectionCode = ''
      this.joinError = ''
      this.joinSuccess = ''
      this.previewSubject = null
      
      if (this.validationTimeout) {
        clearTimeout(this.validationTimeout)
        this.validationTimeout = null
      }
    },

    viewSubjectDetails(subject) {
      this.$router.push({
        name: 'SubjectDetails',
        params: {
          subjectId: subject.id,
          sectionId: subject.sectionId
        },
        query: {
          subjectName: subject.name,
          sectionName: subject.section,
          instructor: subject.instructor,
          gradeLevel: subject.gradeLevel,
          sectionCode: subject.code
        }
      })
    },

    async refreshSubjectStats(subjectId) {
      try {
        const subject = this.subjects.find(s => s.id === subjectId)
        if (!subject) return

        const { data: quizzes } = await supabase
          .from('quizzes')
          .select('id, title, status')
          .eq('section_id', subject.sectionId)
          .eq('status', 'published')

        const { data: results } = await supabase
          .from('quiz_results')
          .select('quiz_id, best_score, best_percentage')
          .eq('student_id', this.studentInfo.id)
          .in('quiz_id', (quizzes || []).map(q => q.id))

        subject.totalQuizzes = (quizzes || []).length
        subject.completedQuizzes = (results || []).length
        subject.availableQuizzes = Math.max(0, subject.totalQuizzes - subject.completedQuizzes)

        if (results && results.length > 0) {
          const avgScore = results.reduce((sum, r) => sum + r.best_percentage, 0) / results.length
          subject.overallScore = avgScore
        }
      } catch (error) {
        console.warn('Failed to refresh subject stats:', error)
      }
    },

    takeQuiz(subject) {
      console.log('Navigating to TakeQuiz for subject:', subject)
      
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
          sectionCode: subject.code,
          availableQuizzes: subject.availableQuizzes || 0
        }
      }).catch(error => {
        console.error('Navigation error:', error);
        alert('Unable to navigate to quiz page. Please try again.');
      });
    },

    viewCompletedQuizzes(subject) {
      this.$router.push({
        name: 'CompletedQuizzes',
        params: {
          subjectId: subject.id,
          sectionId: subject.sectionId
        },
        query: {
          subjectName: subject.name
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
      }).catch(error => {
        console.error('Navigation error:', error);
        alert('Unable to navigate to grades page. Please try again.');
      });
    },

    // Favorite and Archive functionality methods
    toggleFavorite(subjectId) {
      if (this.favoriteSubjects.has(subjectId)) {
        this.favoriteSubjects.delete(subjectId);
      } else {
        this.favoriteSubjects.add(subjectId);
      }
      this.saveUserPreferences();
    },

    toggleArchive(subjectId) {
      if (this.archivedSubjects.has(subjectId)) {
        this.archivedSubjects.delete(subjectId);
      } else {
        this.archivedSubjects.add(subjectId);
        this.favoriteSubjects.delete(subjectId);
      }
      this.saveUserPreferences();
      this.closeAllOptionsMenus();
    },

    toggleOptionsMenu(subjectId) {
      this.subjects.forEach(subject => {
        if (subject.id !== subjectId) {
          subject.showOptions = false;
        }
      });
      
      const subject = this.subjects.find(s => s.id === subjectId);
      if (subject) {
        subject.showOptions = !subject.showOptions;
      }
    },

    closeAllOptionsMenus() {
      this.subjects.forEach(subject => {
        subject.showOptions = false;
      });
    },

    // localStorage persistence methods
    getUserStorageKey(key) {
      const userId = this.currentUser?.id || 'anonymous';
      return `intelligrade_${key}_${userId}`;
    },

    saveUserPreferences() {
      try {
        localStorage.setItem(
          this.getUserStorageKey('favorites'),
          JSON.stringify(Array.from(this.favoriteSubjects))
        );
        localStorage.setItem(
          this.getUserStorageKey('archived'),
          JSON.stringify(Array.from(this.archivedSubjects))
        );
      } catch (error) {
        console.warn('Failed to save user preferences:', error);
      }
    },

    loadUserPreferences() {
      try {
        const favoritesData = localStorage.getItem(this.getUserStorageKey('favorites'));
        const archivedData = localStorage.getItem(this.getUserStorageKey('archived'));
        
        if (favoritesData) {
          this.favoriteSubjects = new Set(JSON.parse(favoritesData));
        }
        if (archivedData) {
          this.archivedSubjects = new Set(JSON.parse(archivedData));
        }
      } catch (error) {
        console.warn('Failed to load user preferences:', error);
        this.favoriteSubjects = new Set();
        this.archivedSubjects = new Set();
      }
    },

    clearUserPreferences() {
      try {
        localStorage.removeItem(this.getUserStorageKey('favorites'));
        localStorage.removeItem(this.getUserStorageKey('archived'));
        this.favoriteSubjects = new Set();
        this.archivedSubjects = new Set();
      } catch (error) {
        console.warn('Failed to clear user preferences:', error);
      }
    },
  },

  async mounted() {
    console.log('Component mounted - Student Subjects page')
    
    try {
      const authSuccess = await this.initializeAuth()
      
      if (!authSuccess) {
        console.log('Auth initialization failed')
        return
      }

      this.loadUserPreferences()
      
      await this.fetchSubjects()
      
      // Set up polling every 30 seconds
      this.pollingInterval = setInterval(() => {
        this.fetchSubjects()
      }, 30000)
      
      console.log('Component initialization complete')
      
      document.addEventListener('click', this.closeAllOptionsMenus)
      
    } catch (error) {
      console.error('Component mount error:', error)
      await this.$router.push('/login')
    }

    // Auth state listener
    supabase.auth.onAuthStateChange(async (event, session) => {
      if (event === 'SIGNED_IN' && session?.user) {
        const success = await this.initializeAuth()
        if (success) {
          await this.fetchSubjects()
        }
      } else if (event === 'SIGNED_OUT') {
        this.subjects = []
        this.currentUser = null
        this.studentInfo = null
        await this.$router.push('/login')
      }
    })
  },

  beforeUnmount() {
    console.log('Component unmounting - cleaning up')
    if (this.pollingInterval) {
      clearInterval(this.pollingInterval)
    }
    if (this.validationTimeout) {
      clearTimeout(this.validationTimeout)
    }
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

.dark .join-class-btn {
  background: #3d8d7a;
  color: #fbffe4;
  box-shadow: 0 2px 8px rgba(32, 201, 151, 0.15);
}
.dark .join-class-btn:hover {
  background: #20c997;
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

.join-class-btn {
  background: #20c997;
  color: white;
  border: none;
  padding: 1rem 1.5rem;
  border-radius: 12px;
  font-weight: 600;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  transition: all 0.2s ease;
  font-size: 1rem;
  font-family: 'Inter', sans-serif;
  box-shadow: 0 2px 8px rgba(32, 201, 151, 0.15);
}

.join-class-btn:hover {
  background: #1ba085;
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(32, 201, 151, 0.25);
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

.subject-card {
  background: #fbffe4;
  border-radius: 12px;
  padding: 1.5rem;
  box-shadow: 0 2px 8px rgba(61, 141, 122, 0.08);
  border: 2px solid #a3d1c6;
  transition: all 0.2s ease;
  cursor: pointer;
  display: flex;
  flex-direction: column;
  gap: 1rem;
  position: relative;
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

.join-first-btn {
  background: #20c997;
  color: white;
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 10px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
  font-size: 0.95rem;
  font-family: 'Inter', sans-serif;
}

.join-first-btn:hover {
  background: #1ba085;
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(32, 201, 151, 0.25);
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
    padding: 0;
    min-height: calc(100vh - 150px);
  }

  /* Header optimizations for mobile */
  .section-header-card,
  .minimal-header-card {
    margin: 1rem;
    margin-bottom: 1.5rem;
    padding: 1rem;
    border-radius: 12px;
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
</style>
<style scoped>
@media (max-width: 768px) {
  .header-stats-desktop {
    display: none !important;
  }
  .header-stats-mobile {
    display: block !important;
    width: 100%;
    margin-top: 1.1rem;
  }
  .formal-mobile-card {
    background: #f8fffe;
    border-radius: 12px;
    box-shadow: 0 2px 8px rgba(61, 141, 122, 0.06);
    border: 1.5px solid #e6f2ed;
    padding: 1.1rem 1rem 1.2rem 1rem;
    margin-top: 0.5rem;
    margin-bottom: 0.2rem;
    display: flex;
    flex-direction: column;
    align-items: stretch;
    gap: 0.9rem;
  }
  .formal-mobile-stats {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
    gap: 1.2rem;
  }
  .formal-mobile-stats .stat-item {
    flex: 1;
    text-align: left;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    gap: 0.1rem;
  }
  .formal-mobile-stats .stat-number {
    font-size: 1.5rem;
    font-weight: 700;
    color: #3d8d7a;
    margin-bottom: 0.1rem;
  }
  .formal-mobile-stats .stat-label {
    font-size: 0.85rem;
    font-weight: 600;
    color: #20c997;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }
  .formal-join-btn {
    background: #20c997;
    color: #fff;
    border: none;
    border-radius: 10px;
    font-weight: 600;
    font-size: 1rem;
    padding: 0.85rem 1.3rem;
    box-shadow: 0 2px 8px rgba(32, 201, 151, 0.13);
    margin-left: 1.2rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
    transition: background 0.2s, box-shadow 0.2s;
  }
  .formal-join-btn:hover {
    background: #1ba085;
    box-shadow: 0 4px 12px rgba(32, 201, 151, 0.22);
  }
}
@media (min-width: 769px) {
  .header-stats-mobile {
    display: none !important;
  }
}
</style>