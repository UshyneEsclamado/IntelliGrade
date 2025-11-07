<template>
  <div class="home-container">
    <!-- Simple Header -->
    <div class="header-card">
      <div class="header-content">
        <div class="header-left">
          <div class="user-icon">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
              <circle cx="12" cy="7" r="4"></circle>
            </svg>
          </div>
          <div>
            <h1 class="header-title">
              <span v-if="!isLoadingName">Hello, {{ fullName }}!</span>
              <span v-else>Hello, Loading...</span>
            </h1>
            <p class="header-subtitle">Welcome to your dashboard</p>
          </div>
        </div>
        
        <!-- Notification Bell -->
        <div class="notif-wrapper">
          <button class="notif-btn" @click="toggleNotifDropdown" aria-label="Notifications">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"></path>
              <path d="M13.73 21a2 2 0 0 1-3.46 0"></path>
            </svg>
            <span v-if="notifications.length" class="notif-badge">{{ notifications.length }}</span>
          </button>
          
          <!-- Notification Dropdown -->
          <div v-if="showNotifDropdown" class="notif-dropdown">
            <div class="notif-header">Notifications</div>
            <div v-if="notifications.length === 0" class="notif-empty">No notifications</div>
            <div v-for="notif in notifications" :key="notif.id" class="notif-item">
              <div class="notif-title">{{ notif.title }}</div>
              <div class="notif-body">{{ notif.body }}</div>
              <div class="notif-date">{{ notif.date }}</div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Stats Cards -->
    <div class="stats-grid">
      <div class="stat-card">
        <div class="stat-icon stat-classes">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
            <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path>
            <circle cx="9" cy="7" r="4"></circle>
            <path d="M23 21v-2a4 4 0 0 0-3-3.87"></path>
            <path d="M16 3.13a4 4 0 0 1 0 7.75"></path>
          </svg>
        </div>
        <div>
          <div class="stat-number">{{ totalClasses }}</div>
          <div class="stat-label">Total Subjects</div>
        </div>
      </div>

      <div class="stat-card">
        <div class="stat-icon stat-students">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
            <path d="M16 17v2H2v-2s0-4 7-4 7 4 7 4m-3.5-9.5A3.5 3.5 0 1 0 9 11a3.5 3.5 0 0 0 3.5-3.5m3.44 5.5A5.32 5.32 0 0 1 18 17v2h4v-2s0-3.63-6.06-4M15 4a3.39 3.39 0 0 0-1.93.59 5 5 0 0 1 0 5.82A3.39 3.39 0 0 0 15 11a3.5 3.5 0 0 0 0-7z"/>
          </svg>
        </div>
        <div>
          <div class="stat-number">{{ totalStudents }}</div>
          <div class="stat-label">Total Students</div>
        </div>
      </div>

      <div class="stat-card">
        <div class="stat-icon stat-graded">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
            <path d="M22 11.08V12a10 10 0 1 1-5.93-8.66"></path>
            <path d="M22 4L12 14.01l-3-3"></path>
          </svg>
        </div>
        <div>
          <div class="stat-number">{{ gradedToday }}</div>
          <div class="stat-label">Graded Today</div>
        </div>
      </div>

      <div class="stat-card">
        <div class="stat-icon stat-pending">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
            <circle cx="12" cy="12" r="10"></circle>
            <polyline points="12,6 12,12 16,14"></polyline>
          </svg>
        </div>
        <div>
          <div class="stat-number">{{ pendingReviews }}</div>
          <div class="stat-label">Pending Reviews</div>
        </div>
      </div>
    </div>

    <!-- Content Grid -->
    <div class="content-grid">
      <!-- Assessments to Grade -->
      <div class="content-card">
        <div class="card-header">
          <h3>Assessments to Grade</h3>
          <p class="card-desc">Review pending student submissions</p>
        </div>
        <div class="assessment-list">
          <div v-if="assessmentsToGrade.length === 0" class="empty-state">
            No assessments to grade
          </div>
          <div v-for="assessment in assessmentsToGrade" :key="assessment.id" class="assessment-item">
            <div class="assessment-info">
              <h4>{{ assessment.title }}</h4>
              <p class="assessment-class">{{ assessment.className }}</p>
              <p class="assessment-progress">{{ assessment.studentsSubmitted }} / {{ assessment.totalStudents }} submitted</p>
            </div>
            <button @click="gradeAssessment(assessment)" class="grade-btn">Grade</button>
          </div>
        </div>
      </div>

      <!-- Quick Links -->
      <div class="content-card">
        <div class="card-header">
          <h3>Quick Links</h3>
          <p class="card-desc">Access key features</p>
        </div>
        <div class="quick-links">
          <router-link to="/teacher/subjects" class="quick-link">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M14,2H6A2,2 0 0,0 4,4V20A2,2 0 0,0 6,22H18A2,2 0 0,0 20,20V8L14,2M18,20H6V4H13V9H18V20Z" />
            </svg>
            <span>Make Quiz</span>
          </router-link>
          
          <router-link to="/teacher/upload-assessment" class="quick-link">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M9,16V10H5L12,3L19,10H15V16H9M5,20V18H19V20H5Z" />
            </svg>
            <span>Upload Assessment</span>
          </router-link>
          
          <router-link to="/teacher/subjects" class="quick-link">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path>
              <circle cx="9" cy="7" r="4"></circle>
              <path d="M23 21v-2a4 4 0 0 0-3-3.87"></path>
              <path d="M16 3.13a4 4 0 0 1 0 7.75"></path>
            </svg>
            <span>My Classes</span>
          </router-link>
          
          <router-link to="/teacher/gradebook" class="quick-link">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M19,3H14.82C14.4,1.84 13.3,1 12,1C10.7,1 9.6,1.84 9.18,3H5A2,2 0 0,0 3,5V19A2,2 0 0,0 5,21H19A2,2 0 0,0 21,19V5A2,2 0 0,0 19,3M12,3A1,1 0 0,1 13,4A1,1 0 0,1 12,5A1,1 0 0,1 11,4A1,1 0 0,1 12,3Z" />
            </svg>
            <span>Gradebook</span>
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { supabase } from '../../supabase.js'

// Local state
const notifications = ref([])
const showNotifDropdown = ref(false)
const fullName = ref('Teacher')
const isLoadingName = ref(false)
const totalClasses = ref(0)
const totalStudents = ref(0)
const gradedToday = ref(0)
const pendingReviews = ref(0)
const assessmentsToGrade = ref([])
const teacherId = ref(null)
const userId = ref(null)

// Methods
const toggleNotifDropdown = () => {
  showNotifDropdown.value = !showNotifDropdown.value
}

const gradeAssessment = (assessment) => {
  console.log('Grading assessment:', assessment)
  // TODO: Implement grade assessment functionality
}

// Load teacher profile
const loadTeacherProfile = async () => {
  try {
    console.log('🔍 Loading teacher profile...')
    
    const { data: { user }, error: userError } = await supabase.auth.getUser()
    if (userError || !user) {
      console.error('❌ No user found:', userError)
      return false
    }
    
    userId.value = user.id
    console.log('✅ User ID:', user.id)
    
    // Get profile
    const { data: profile, error: profileError } = await supabase
      .from('profiles')
      .select('id, full_name, role')
      .eq('auth_user_id', user.id)
      .single()
    
    if (profileError || !profile) {
      console.error('❌ Profile error:', profileError)
      return false
    }
    
    console.log('✅ Profile found:', profile)
    
    // Get teacher data
    const { data: teacher, error: teacherError } = await supabase
      .from('teachers')
      .select('id, full_name')
      .eq('profile_id', profile.id)
      .single()
    
    if (teacherError || !teacher) {
      console.error('❌ Teacher error:', teacherError)
      return false
    }
    
    teacherId.value = teacher.id
    fullName.value = teacher.full_name || profile.full_name || 'Teacher'
    
    console.log('✅ Teacher loaded:', { id: teacher.id, name: fullName.value })
    return true
    
  } catch (error) {
    console.error('❌ Error loading profile:', error)
    return false
  }
}

// Load dashboard stats
const loadDashboardStats = async () => {
  if (!teacherId.value) {
    console.warn('⚠️ No teacher ID, cannot load stats')
    return
  }
  
  try {
    console.log('📊 Loading dashboard stats for teacher:', teacherId.value)
    
    // Get total classes (subjects)
    const { data: subjects, error: subjectsError } = await supabase
      .from('subjects')
      .select('id')
      .eq('teacher_id', teacherId.value)
      .eq('is_active', true)
    
    if (!subjectsError && subjects) {
      totalClasses.value = subjects.length
      console.log('📚 Total subjects:', subjects.length)
    }
    
    // Get total students across all sections taught by this teacher
    // First, get all sections for this teacher's subjects
    const { data: teacherSections, error: sectionsError } = await supabase
      .from('sections')
      .select(`
        id,
        subject_id,
        subjects!inner(teacher_id)
      `)
      .eq('subjects.teacher_id', teacherId.value)
    
    if (!sectionsError && teacherSections && teacherSections.length > 0) {
      console.log('📋 Found sections:', teacherSections.length)
      
      // Get unique student count across all sections
      const sectionIds = teacherSections.map(s => s.id)
      
      const { data: enrollments, error: enrollError } = await supabase
        .from('enrollments')
        .select('student_id')
        .in('section_id', sectionIds)
        .eq('status', 'active')
      
      if (!enrollError && enrollments) {
        // Count unique students (in case a student is in multiple sections)
        const uniqueStudents = new Set(enrollments.map(e => e.student_id))
        totalStudents.value = uniqueStudents.size
        console.log('👥 Total unique students:', uniqueStudents.size)
        console.log('� Total enrollments:', enrollments.length)
      } else {
        console.error('❌ Enrollment error:', enrollError)
      }
    } else {
      console.log('⚠️ No sections found for teacher')
      if (sectionsError) console.error('❌ Sections error:', sectionsError)
    }
    
    // Get graded today
    const today = new Date()
    today.setHours(0, 0, 0, 0)
    const todayISO = today.toISOString()
    
    const { data: graded, error: gradedError } = await supabase
      .from('quiz_attempts')
      .select('id, quiz_id!inner(teacher_id)')
      .eq('quiz_id.teacher_id', teacherId.value)
      .eq('status', 'graded')
      .gte('graded_at', todayISO)
    
    if (!gradedError && graded) {
      gradedToday.value = graded.length
      console.log('✅ Graded today:', graded.length)
    }
    
    // Get pending assessments
    const { data: quizzes, error: quizzesError } = await supabase
      .from('quizzes')
      .select(`
        id,
        title,
        subject_id,
        section_id,
        subjects!inner(name),
        sections!inner(name)
      `)
      .eq('teacher_id', teacherId.value)
      .eq('status', 'published')
    
    if (!quizzesError && quizzes) {
      const assessmentsWithSubmissions = []
      
      for (const quiz of quizzes) {
        // Get submitted attempts
        const { data: attempts } = await supabase
          .from('quiz_attempts')
          .select('id, student_id')
          .eq('quiz_id', quiz.id)
          .eq('status', 'submitted')
        
        if (attempts && attempts.length > 0) {
          // Get total students in section
          const { data: enrollments } = await supabase
            .from('enrollments')
            .select('student_id')
            .eq('section_id', quiz.section_id)
            .eq('status', 'active')
          
          assessmentsWithSubmissions.push({
            id: quiz.id,
            title: quiz.title,
            className: `${quiz.subjects.name} - ${quiz.sections.name}`,
            studentsSubmitted: attempts.length,
            totalStudents: enrollments?.length || 0,
            sectionId: quiz.section_id,
            subjectId: quiz.subject_id
          })
        }
      }
      
      assessmentsToGrade.value = assessmentsWithSubmissions
      pendingReviews.value = assessmentsWithSubmissions.length
      
      console.log('📝 Assessments to grade:', assessmentsWithSubmissions.length)
    }
    
    console.log('✅ Dashboard stats loaded successfully')
    
  } catch (error) {
    console.error('❌ Error loading dashboard stats:', error)
  }
}

// Lifecycle
onMounted(async () => {
  console.log('🚀 Dashboard mounting...')
  
  const profileLoaded = await loadTeacherProfile()
  
  if (profileLoaded) {
    await loadDashboardStats()
    
    // Auto-refresh every 30 seconds
    const intervalId = setInterval(() => {
      loadDashboardStats()
    }, 30000)
    
    // Cleanup on unmount
    return () => {
      clearInterval(intervalId)
    }
  }
})
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.home-container {
  min-height: 100vh;
  background: #FBFFE4;
  padding: 1.5rem;
  font-family: 'Inter', sans-serif;
}
.dark .home-container {
  background: #181c20;
}

/* Header */
.header-card {
  background: white;
  border: 1.5px solid #3D8D7A;
  border-radius: 16px;
  padding: 1.5rem;
  margin-bottom: 1.5rem;
  box-shadow: 0 2px 8px rgba(61, 141, 122, 0.1);
}
.dark .header-card {
  background: #23272b;
  border: 1.5px solid #A3D1C6;
  box-shadow: 0 2px 8px rgba(163, 209, 198, 0.1);
}

.header-content {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.header-left {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.user-icon {
  width: 56px;
  height: 56px;
  background: #3D8D7A;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
}

.header-title {
  font-size: 1.5rem;
  font-weight: 800;
  color: #1f2937;
  margin-bottom: 0.25rem;
}

.header-title span {
  font-weight: 800 !important;
}
.dark .header-title {
  color: #A3D1C6;
  font-weight: 800;
}

.dark .header-title span {
  font-weight: 800 !important;
}

.header-subtitle {
  font-size: 0.875rem;
  color: #6b7280;
}
.dark .header-subtitle {
  color: #A3D1C6;
}

/* Notification */
.notif-wrapper {
  position: relative;
}

.notif-btn {
  width: 48px;
  height: 48px;
  background: #FBFFE4;
  border: 2px solid #A3D1C6;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.2s;
  position: relative;
  color: #3D8D7A;
}
.dark .notif-btn {
  background: #23272b;
  border-color: #3D8D7A;
  color: #A3D1C6;
}

.notif-btn:hover {
  background: #A3D1C6;
  transform: scale(1.05);
}

.notif-badge {
  position: absolute;
  top: -4px;
  right: -4px;
  background: #ef4444;
  color: white;
  font-size: 0.75rem;
  font-weight: 600;
  padding: 0.125rem 0.375rem;
  border-radius: 999px;
  min-width: 20px;
  text-align: center;
}

.notif-dropdown {
  position: absolute;
  top: 60px;
  right: 0;
  width: 320px;
  max-height: 400px;
  background: white;
  border-radius: 12px;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
  overflow-y: auto;
  z-index: 1000;
  border: 1px solid #e5e7eb;
}
.dark .notif-dropdown {
  background: #23272b;
  border-color: #3D8D7A;
  box-shadow: 0 8px 24px rgba(0,0,0,0.35);
}

.notif-header {
  padding: 1rem 1.25rem;
  font-weight: 600;
  color: #1f2937;
  border-bottom: 1px solid #e5e7eb;
  position: sticky;
  top: 0;
  background: white;
}
.dark .notif-header {
  color: #A3D1C6;
  background: #23272b;
  border-bottom: 1px solid #3D8D7A;
}

.notif-empty {
  padding: 2rem 1.25rem;
  text-align: center;
  color: #9ca3af;
  font-size: 0.875rem;
}
.dark .notif-empty {
  color: #A3D1C6;
}

.notif-item {
  padding: 1rem 1.25rem;
  border-bottom: 1px solid #f3f4f6;
  transition: background 0.2s;
  cursor: pointer;
}
.dark .notif-item {
  border-bottom: 1px solid #232a2f;
}

.notif-item:hover {
  background: #f9fafb;
}
.dark .notif-item:hover {
  background: #23272b;
}

.notif-item:last-child {
  border-bottom: none;
}

.notif-title {
  font-weight: 600;
  color: #1f2937;
  font-size: 0.875rem;
  margin-bottom: 0.25rem;
}
.dark .notif-title {
  color: #A3D1C6;
}

.notif-body {
  font-size: 0.813rem;
  color: #6b7280;
  margin-bottom: 0.375rem;
}
.dark .notif-body {
  color: #A3D1C6;
}

.notif-date {
  font-size: 0.75rem;
  color: #9ca3af;
}
.dark .notif-date {
  color: #A3D1C6;
}

/* Stats Grid */
.stats-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1rem;
  margin-bottom: 1.5rem;
}

.stat-card {
  background: white;
  border-radius: 12px;
  padding: 1.25rem;
  display: flex;
  align-items: center;
  gap: 1rem;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
}
.dark .stat-card {
  background: #23272b;
  border: 1px solid #20c997;
  box-shadow: 0 2px 8px rgba(0,0,0,0.25);
}

.stat-icon {
  width: 48px;
  height: 48px;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  flex-shrink: 0;
}

.stat-classes { background: #3D8D7A; }
.stat-students { background: #20c997; }
.stat-graded { background: #B3D8A8; }
.stat-pending { background: #A3D1C6; }

.stat-number {
  font-size: 1.875rem;
  font-weight: 700;
  color: #1f2937;
  line-height: 1;
}
.dark .stat-number {
  color: #A3D1C6;
}

.stat-label {
  font-size: 0.813rem;
  color: #6b7280;
  margin-top: 0.25rem;
  font-weight: 500;
}
.dark .stat-label {
  color: #A3D1C6;
}

/* Content Grid */
.content-grid {
  display: grid;
  grid-template-columns: 1.5fr 1fr;
  gap: 1.5rem;
}

.content-card {
  background: white;
  border-radius: 12px;
  padding: 1.5rem;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
  display: flex;
  flex-direction: column;
  max-height: 500px;
}
.dark .content-card {
  background: #23272b;
  border: 1px solid #20c997;
  box-shadow: 0 2px 8px rgba(0,0,0,0.25);
}

.card-header {
  margin-bottom: 1.25rem;
}

.card-header h3 {
  font-size: 1.125rem;
  font-weight: 600;
  color: #1f2937;
  margin-bottom: 0.25rem;
}
.dark .card-header h3 {
  color: #A3D1C6;
}

.card-desc {
  font-size: 0.813rem;
  color: #6b7280;
}
.dark .card-desc {
  color: #A3D1C6;
}

/* Assessment List */
.assessment-list {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
  overflow-y: auto;
  flex: 1;
}

.assessment-list::-webkit-scrollbar {
  width: 6px;
}

.assessment-list::-webkit-scrollbar-track {
  background: #f3f4f6;
  border-radius: 3px;
}

.assessment-list::-webkit-scrollbar-thumb {
  background: #A3D1C6;
  border-radius: 3px;
}

.assessment-item {
  background: #FBFFE4;
  border-radius: 10px;
  padding: 1rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  transition: all 0.2s;
  border: 1px solid #A3D1C6;
}
.dark .assessment-item {
  background: #23272b;
  border-color: #20c997;
}

.assessment-item:hover {
  background: #A3D1C6;
  border-color: #3D8D7A;
}
.dark .assessment-item:hover {
  background: #23272b;
  border-color: #A3D1C6;
}

.assessment-info h4 {
  font-size: 0.938rem;
  font-weight: 600;
  color: #1f2937;
  margin-bottom: 0.25rem;
}
.dark .assessment-info h4 {
  color: #A3D1C6;
}

.assessment-class {
  font-size: 0.813rem;
  color: #6b7280;
  margin-bottom: 0.25rem;
}
.dark .assessment-class {
  color: #A3D1C6;
}

.assessment-progress {
  font-size: 0.75rem;
  color: #3D8D7A;
  font-weight: 500;
}
.dark .assessment-progress {
  color: #A3D1C6;
}

.grade-btn {
  background: #20c997;
  color: #181c20;
  border: 1px solid #A3D1C6;
  padding: 0.5rem 1.25rem;
  border-radius: 8px;
  font-size: 0.875rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s;
}
.dark .grade-btn {
  background: #20c997;
  color: #181c20;
  border: 1px solid #A3D1C6;
}

.grade-btn:hover {
  background: #A3D1C6;
  color: #23272b;
  border-color: #20c997;
  transform: translateY(-1px);
}
.dark .grade-btn:hover {
  background: #A3D1C6;
  color: #23272b;
  border-color: #20c997;
}

.empty-state {
  text-align: center;
  color: #9ca3af;
  padding: 2rem;
  font-size: 0.875rem;
}
.dark .empty-state {
  color: #A3D1C6;
}

/* Quick Links */
.quick-links {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0.75rem;
  overflow-y: auto;
  flex: 1;
}

.quick-links::-webkit-scrollbar {
  width: 6px;
}

.quick-links::-webkit-scrollbar-track {
  background: #f3f4f6;
  border-radius: 3px;
}

.quick-links::-webkit-scrollbar-thumb {
  background: #A3D1C6;
  border-radius: 3px;
}

.quick-link {
  background: #FBFFE4;
  border: 1px solid #A3D1C6;
  border-radius: 10px;
  padding: 1rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.5rem;
  cursor: pointer;
  transition: all 0.2s;
  text-decoration: none;
  color: #1f2937;
  font-weight: 500;
  font-size: 0.875rem;
}
.dark .quick-link {
  background: #23272b;
  border-color: #20c997;
  color: #A3D1C6;
}

.quick-link:hover {
  background: #A3D1C6;
  color: #181c20;
  border-color: #3D8D7A;
  transform: translateY(-2px);
}
.dark .quick-link:hover {
  background: #A3D1C6;
  color: #23272b;
  border-color: #20c997;
}

.quick-link svg {
  color: #20c997;
}
.dark .quick-link svg {
  color: #A3D1C6;
}

/* Responsive */
@media (max-width: 1024px) {
  .content-grid {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 768px) {
  .stats-grid {
    grid-template-columns: 1fr;
  }
  
  .quick-links {
    grid-template-columns: 1fr;
  }
}
</style>