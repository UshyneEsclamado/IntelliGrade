<template>
  <div class="home-container" :class="{ 'dark-mode': isDarkMode }">
    <!-- Compact Header Section with Bell Icon Dropdown -->
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
            <svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
              <circle cx="12" cy="7" r="4"></circle>
            </svg>
          </div>
          <div class="header-text">
            <div class="section-header-title">
              <span v-if="!isLoadingName">Hello, {{ fullName }}!</span>
              <span v-else>Hello, Loading...</span>
            </div>
            <div class="section-header-subtitle">Welcome to your teaching dashboard</div>
            <div class="section-header-description">Manage your classes, grade assessments, and track student progress</div>
          </div>
        </div>
        <div class="header-actions">
          <!-- Bell Icon Dropdown (improved positioning) -->
          <div class="notif-bell-wrapper">
            <button class="notif-bell-btn" @click="toggleNotifDropdown" aria-label="Notifications">
              <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#4DBB98" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                <path d="M18 16v-5a6 6 0 0 0-12 0v5a2 2 0 0 1-2 2h16a2 2 0 0 1-2-2z"/>
                <path d="M13.73 21a2 2 0 0 1-3.46 0"/>
                <circle cx="12" cy="7" r="4" fill="#4DBB98" opacity="0.15"/>
              </svg>
              <span v-if="notifications.length" class="notif-bell-dot"></span>
            </button>
            <div v-if="showNotifDropdown" class="notif-dropdown">
              <div class="notif-dropdown-header">Notifications</div>
              <div v-if="notifications.length === 0" class="notif-dropdown-empty">No notifications yet.</div>
              <div v-for="notif in notifications" :key="notif.id" class="notif-dropdown-item">
                <div class="notif-title">{{ notif.title }}</div>
                <div class="notif-body">{{ notif.body }}</div>
                <div class="notif-date">{{ notif.date }}</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Compact Stats Cards -->
    <div class="stats-grid">
      <div class="stat-card">
        <div class="stat-icon classes">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor">
            <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path>
            <circle cx="9" cy="7" r="4"></circle>
            <path d="M23 21v-2a4 4 0 0 0-3-3.87"></path>
            <path d="M16 3.13a4 4 0 0 1 0 7.75"></path>
          </svg>
        </div>
        <div class="stat-content">
          <div class="stat-number">{{ totalClasses }}</div>
          <div class="stat-label">TOTAL CLASSES</div>
        </div>
      </div>

      <div class="stat-card">
        <div class="stat-icon graded">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor">
            <path d="M22 11.08V12a10 10 0 1 1-5.93-8.66"></path>
            <path d="M22 4L12 14.01l-3-3"></path>
          </svg>
        </div>
        <div class="stat-content">
          <div class="stat-number">{{ gradedToday }}</div>
          <div class="stat-label">GRADED TODAY</div>
        </div>
      </div>

      <div class="stat-card">
        <div class="stat-icon pending">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor">
            <circle cx="12" cy="12" r="10"></circle>
            <polyline points="12,6 12,12 16,14"></polyline>
          </svg>
        </div>
        <div class="stat-content">
          <div class="stat-number">{{ pendingReviews }}</div>
          <div class="stat-label">PENDING REVIEWS</div>
        </div>
      </div>
    </div>

    <!-- Optimized Content Grid -->
    <div class="content-grid">
      <!-- Assessments to Grade -->
      <div class="content-card">
        <div class="card-header">
          <h3>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
              <path d="M14,2H6A2,2 0 0,0 4,4V20A2,2 0 0,0 6,22H18A2,2 0 0,0 20,20V8L14,2M18,20H6V4H13V9H18V20Z" />
            </svg>
            Assessments to Grade
          </h3>
          <p class="card-subtitle">A list of assessments waiting for your attention.</p>
        </div>
        <div class="assessment-list">
          <div v-if="assessmentsToGrade.length === 0" class="empty-state">
            <p>No new assessments to grade at the moment.</p>
          </div>
          <div v-for="assessment in assessmentsToGrade" :key="assessment.id" class="assessment-item">
            <div class="assessment-info">
              <h4>{{ assessment.title }}</h4>
              <p class="assessment-class">{{ assessment.className }}</p>
              <p class="assessment-progress">Submitted: {{ assessment.studentsSubmitted }} / {{ assessment.totalStudents }}</p>
            </div>
            <div class="assessment-actions">
              <button @click="gradeAssessment(assessment)" class="grade-btn">Grade Assessment</button>
            </div>
          </div>
        </div>
      </div>

      <!-- Quick Links -->
      <div class="content-card">
        <div class="card-header">
          <h3>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
              <path d="M13,9H18.5L13,3.5V9M6,2H14L20,8V20A2,2 0 0,1 18,22H6C4.89,22 4,21.1 4,20V4C4,2.89 4.89,2 6,2M15,18V16H6V18H15M18,14V12H6V14H18Z" />
            </svg>
            Quick Links
          </h3>
          <p class="card-subtitle">Navigate to key features quickly.</p>
        </div>
        <div class="quick-links-grid">
          <router-link to="/teacher/subjects" class="quick-link-btn quiz">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
              <path d="M14,2H6A2,2 0 0,0 4,4V20A2,2 0 0,0 6,22H18A2,2 0 0,0 20,20V8L14,2M18,20H6V4H13V9H18V20Z" />
            </svg>
            Make Quiz
            <span class="link-description">Create interactive quizzes</span>
          </router-link>
          <router-link to="/teacher/upload-assessment" class="quick-link-btn upload">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
              <path d="M14,2H6A2,2 0 0,0 4,4V20A2,2 0 0,0 6,22H18A2,2 0 0,0 20,20V8L14,2M18,20H6V4H13V9H18V20Z" />
            </svg>
            Upload Assessment
            <span class="link-description">Upload for auto-grading</span>
          </router-link>
          <button @click="navigateToClasses" class="quick-link-btn classes">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
              <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path>
              <circle cx="9" cy="7" r="4"></circle>
              <path d="M23 21v-2a4 4 0 0 0-3-3.87"></path>
              <path d="M16 3.13a4 4 0 0 1 0 7.75"></path>
            </svg>
            My Classes
            <span class="link-description">Manage your classes</span>
          </button>
          <button @click="navigateToGradebook" class="quick-link-btn gradebook">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
              <path d="M22 11.08V12a10 10 0 1 1-5.93-8.66"></path>
              <path d="M22 4L12 14.01l-3-3"></path>
            </svg>
            Gradebook
            <span class="link-description">View all grades</span>
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { supabase } from '../../supabase.js';

export default {
  name: 'TeacherHome',
  data() {
    return {
      fullName: 'Teacher',
      totalClasses: 0,
      gradedToday: 0,
      pendingReviews: 0,
      assessmentsToGrade: [],
      notifications: [],
      pollInterval: null,
      isLoadingName: true,
      userId: null,
      profileId: null,
      teacherId: null,
      showNotifDropdown: false
    };
  },
  methods: {
    toggleNotifDropdown() {
      this.showNotifDropdown = !this.showNotifDropdown;
    },
    async loadTeacherProfile() {
      try {
        this.isLoadingName = true;
        
        const { data: { user }, error: authError } = await supabase.auth.getUser();
        
        if (authError || !user) {
          console.error('Auth error in Teacher Home:', authError);
          this.$router.push('/login');
          return;
        }

        this.userId = user.id;
        console.log('Loading teacher profile for user:', user.id);

        const { data: profile, error: profileError } = await supabase
          .from('profiles')
          .select('id, full_name, email, role')
          .eq('auth_user_id', user.id)
          .single();

        if (profileError) {
          console.error('Profile error in Teacher Home:', profileError);
          
          if (profileError.code === 'PGRST116') {
            console.warn('No profile found for user in Teacher Home');
            this.fullName = user.email?.split('@')[0] || 'Teacher';
            return;
          }
          
          this.fullName = 'Teacher';
          return;
        }

        console.log('Profile found in Teacher Home:', profile);
        this.profileId = profile.id;

        if (profile.role !== 'teacher') {
          console.warn('User is not a teacher in Teacher Home');
          this.$router.push('/login');
          return;
        }

        const { data: teacherData, error: teacherError } = await supabase
          .from('teachers')
          .select('id, employee_id, full_name, email, department, is_active')
          .eq('profile_id', profile.id)
          .single();

        if (teacherError) {
          console.warn('Teacher data error in Teacher Home:', teacherError);
          
          if (teacherError.code === 'PGRST116') {
            console.log('No teacher record found, creating one...');
            await this.createMissingTeacherRecord(profile);
            return;
          }
          
          this.fullName = profile.full_name || 'Teacher';
          return;
        }

        console.log('Teacher data found in Teacher Home:', teacherData);
        this.teacherId = teacherData.id;
        
        this.fullName = teacherData.full_name || profile.full_name || 'Teacher';
        
        await this.loadDashboardStats();

      } catch (error) {
        console.error('Error loading teacher profile in Teacher Home:', error);
        this.fullName = 'Teacher';
      } finally {
        this.isLoadingName = false;
      }
    },

    async createMissingTeacherRecord(profile) {
      try {
        console.log('Creating missing teacher record for profile:', profile.id);
        
        const employeeId = await this.generateEmployeeId(profile.id);
        
        const { data, error } = await supabase
          .from('teachers')
          .insert([{
            profile_id: profile.id,
            employee_id: employeeId,
            full_name: profile.full_name,
            email: profile.email,
            department: 'General',
            is_active: true
          }])
          .select()
          .single();

        if (error) {
          console.error('Error creating teacher record:', error);
          this.fullName = profile.full_name || 'Teacher';
          return;
        }

        console.log('Created teacher record:', data);
        this.teacherId = data.id;
        this.fullName = data.full_name;
        
      } catch (error) {
        console.error('Error in createMissingTeacherRecord:', error);
        this.fullName = profile.full_name || 'Teacher';
      }
    },

    async generateEmployeeId(profileId) {
      try {
        const year = new Date().getFullYear();
        const shortId = profileId.slice(-6).toUpperCase();
        const random = Math.floor(Math.random() * 99).toString().padStart(2, '0');
        const employeeId = `T${year}${shortId}${random}`;
        
        const { data: existingTeacher } = await supabase
          .from('teachers')
          .select('employee_id')
          .eq('employee_id', employeeId)
          .single();
        
        if (existingTeacher) {
          return await this.generateEmployeeId(profileId);
        }
        
        console.log('Generated employee ID:', employeeId);
        return employeeId;
      } catch (error) {
        console.error('Error generating employee ID:', error);
        return `T${Date.now().toString().slice(-8)}`;
      }
    },

    async loadDashboardStats() {
      try {
        if (!this.teacherId) {
          console.warn('No teacher ID available for dashboard stats');
          this.totalClasses = 0;
          this.gradedToday = 0;
          this.pendingReviews = 0;
          return;
        }

        const { data: subjects, error: subjectsError } = await supabase
          .from('teacher_dashboard')
          .select('subject_id')
          .eq('teacher_id', this.teacherId);

        if (subjectsError) {
          console.error('Error loading teacher subjects:', subjectsError);
        } else {
          const uniqueSubjects = new Set(subjects?.map(s => s.subject_id) || []);
          this.totalClasses = uniqueSubjects.size;
          console.log('Total classes:', this.totalClasses);
        }

        this.gradedToday = 0;
        this.pendingReviews = 0;

        await this.loadAssessmentsToGrade();

      } catch (error) {
        console.error('Error loading dashboard stats:', error);
        this.totalClasses = 0;
        this.gradedToday = 0;
        this.pendingReviews = 0;
      }
    },

    async loadAssessmentsToGrade() {
      try {
        this.assessmentsToGrade = [
          { 
            id: 1, 
            title: 'Mathematics Quiz 1', 
            className: 'Grade 7 Math', 
            studentsSubmitted: 15, 
            totalStudents: 20 
          },
          { 
            id: 2, 
            title: 'Science Test', 
            className: 'Grade 8 Science', 
            studentsSubmitted: 18, 
            totalStudents: 22 
          }
        ];

        this.pendingReviews = this.assessmentsToGrade.length;

      } catch (error) {
        console.error('Error loading assessments to grade:', error);
        this.assessmentsToGrade = [];
      }
    },

    async fetchDashboardStats() {
      console.log('Dashboard stats refresh triggered');
      await this.loadDashboardStats();
    },

    async fetchAssessmentsToGrade() {
      await this.loadAssessmentsToGrade();
    },

    gradeAssessment(assessment) {
      console.log('Grading assessment:', assessment.title);
    },

    navigateToClasses() {
      this.$parent.navigateTo('subjects');
    },

    navigateToGradebook() {
      console.log('Navigate to gradebook');
    },

    async fetchAllData() {
      await Promise.all([
        this.loadDashboardStats(),
        this.loadAssessmentsToGrade()
      ]);
    },

    async loadNotifications() {
      const { data, error } = await supabase
        .from('notifications')
        .select('*')
        .eq('user_id', this.userId)
        .order('created_at', { ascending: false })
        .limit(10);
      if (!error && data) {
        this.notifications = data.map(n => ({
          id: n.id,
          title: n.title,
          body: n.body,
          date: n.created_at ? new Date(n.created_at).toLocaleString() : ''
        }));
      }
    },

    setupRealtimeSubscriptions() {
      if (!this.userId) return;

      const notifSubscription = supabase
        .channel('teacher_home_notifications')
        .on(
          'postgres_changes',
          {
            event: '*',
            schema: 'public',
            table: 'notifications',
            filter: `user_id=eq.${this.userId}`
          },
          (payload) => {
            console.log('Notification update:', payload);
            this.loadNotifications();
          }
        )
        .subscribe();

      const profileSubscription = supabase
        .channel('teacher_home_profile_changes')
        .on(
          'postgres_changes',
          {
            event: '*',
            schema: 'public',
            table: 'profiles',
            filter: `auth_user_id=eq.${this.userId}`
          },
          (payload) => {
            console.log('Profile updated in Teacher Home:', payload);
            this.loadTeacherProfile();
          }
        )
        .subscribe();

      const teacherSubscription = supabase
        .channel('teacher_home_teacher_changes')
        .on(
          'postgres_changes',
          {
            event: '*',
            schema: 'public',
            table: 'teachers'
          },
          (payload) => {
            console.log('Teacher data updated in Teacher Home:', payload);
            this.loadTeacherProfile();
          }
        )
        .subscribe();

      const subjectsSubscription = supabase
        .channel('teacher_home_subjects_changes')
        .on(
          'postgres_changes',
          {
            event: '*',
            schema: 'public',
            table: 'subjects'
          },
          (payload) => {
            console.log('Subjects updated in Teacher Home:', payload);
            this.loadDashboardStats();
          }
        )
        .subscribe();

      this.subscriptions = [notifSubscription, profileSubscription, teacherSubscription, subjectsSubscription];
    }
  },

  async mounted() {
    console.log('Teacher Home component mounted');
    await this.loadTeacherProfile();
    await this.loadNotifications();
    this.setupRealtimeSubscriptions();
    this.pollInterval = setInterval(() => {
      this.fetchAllData();
      this.loadNotifications();
    }, 30000);
  },

  beforeDestroy() {
    console.log('Teacher Home component being destroyed');
    
    if (this.pollInterval) {
      clearInterval(this.pollInterval);
    }
    
    if (this.subscriptions) {
      this.subscriptions.forEach(subscription => {
        subscription.unsubscribe();
      });
    }
  }
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

/* Fix the main container to not clip dropdowns */
.home-container {
  padding: 1.25rem;
  max-width: 100%;
  margin: 0;
  font-family: 'Inter', sans-serif;
  background: var(--bg-primary);
  height: 100vh;
  overflow-y: auto;
  box-sizing: border-box;
  position: relative; /* Add relative positioning */
}

.home-container::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: 
    radial-gradient(circle at 20% 80%, rgba(61, 141, 122, 0.1) 0%, transparent 50%),
    radial-gradient(circle at 80% 20%, rgba(179, 216, 168, 0.15) 0%, transparent 50%),
    radial-gradient(circle at 50% 50%, rgba(163, 209, 198, 0.08) 0%, transparent 50%);
  z-index: -1;
  pointer-events: none;
}

/* Fix the header card positioning to not interfere */
.section-header-card {
  position: relative;
  background: var(--bg-secondary);
  backdrop-filter: blur(20px);
  border-radius: 24px;
  padding: 2rem;
  margin-bottom: 1.5rem;
  min-height: 120px;
  box-shadow: 
    0 16px 32px var(--shadow-medium),
    0 8px 16px var(--shadow-light),
    inset 0 1px 0 rgba(255, 255, 255, 0.8);
  border: 2px solid var(--border-color);
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  overflow: visible; /* Make sure overflow is visible */
  z-index: 1; /* Lower z-index than notification */
}

.section-header-card:hover {
  transform: translateY(-2px);
  box-shadow: 
    0 24px 48px var(--shadow-strong),
    0 12px 24px var(--shadow-medium),
    inset 0 1px 0 rgba(255, 255, 255, 0.9);
}

.header-bg-decoration {
  position: absolute;
  top: -50%;
  right: -20%;
  width: 120%;
  height: 200%;
  background: radial-gradient(ellipse at center, rgba(77, 187, 152, 0.08) 0%, transparent 70%);
  z-index: 1;
}

.floating-shapes {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 1;
  pointer-events: none;
}

.shape {
  position: absolute;
  border-radius: 50%;
  background: linear-gradient(135deg, rgba(77, 187, 152, 0.1) 0%, rgba(51, 128, 107, 0.05) 100%);
}

.shape-1 {
  width: 80px;
  height: 80px;
  top: -20px;
  right: 10%;
  animation: float 6s ease-in-out infinite;
}

.shape-2 {
  width: 60px;
  height: 60px;
  bottom: -15px;
  right: 25%;
  animation: float 8s ease-in-out infinite reverse;
}

.shape-3 {
  width: 45px;
  height: 45px;
  top: 50%;
  right: 5%;
  animation: float 7s ease-in-out infinite;
}

@keyframes float {
  0%, 100% { transform: translateY(0) rotate(0deg); }
  50% { transform: translateY(-15px) rotate(8deg); }
}

.section-header-content {
  position: relative;
  z-index: 2;
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
}

.section-header-left {
  display: flex;
  align-items: center;
  gap: 1.5rem;
}

.section-header-icon {
  width: 60px;
  height: 60px;
  background: linear-gradient(135deg, var(--accent-color) 0%, #A3D1C6 100%);
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #fff;
  box-shadow: 
    0 8px 16px var(--shadow-light),
    inset 0 1px 0 rgba(255, 255, 255, 0.2);
  transition: all 0.3s ease;
}

.section-header-icon:hover {
  transform: scale(1.05);
}

.header-text {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}

.section-header-title {
  font-size: 1.75rem;
  font-weight: 800;
  color: var(--text-accent);
  letter-spacing: -0.02em;
  background: linear-gradient(135deg, var(--accent-color) 0%, #A3D1C6 100%);
  background-clip: text;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  margin-bottom: 0.1rem;
}

.section-header-subtitle {
  font-size: 1rem;
  font-weight: 600;
  color: var(--text-secondary);
  margin-bottom: 0.1rem;
}

.section-header-description {
  font-size: 0.875rem;
  color: var(--text-muted);
  font-weight: 400;
  opacity: 0.9;
}

/* Ensure header actions don't clip the dropdown */
.header-actions {
  display: flex;
  align-items: center;
  gap: 1.25rem;
  position: relative;
  z-index: 9999; /* High z-index for the actions container */
}

/* Fix the notification wrapper positioning */
.notif-bell-wrapper {
  position: relative;
  display: flex;
  align-items: center;
  z-index: 9999; /* Increase base z-index */
}

.notif-bell-btn {
  background: var(--bg-accent);
  border: 2px solid var(--accent-color);
  cursor: pointer;
  position: relative;
  padding: 0.25rem;
  border-radius: 50%;
  transition: background 0.2s, box-shadow 0.2s;
  outline: none;
  box-shadow: 0 2px 8px var(--shadow-light);
}

.notif-bell-btn:focus {
  box-shadow: 0 0 0 3px var(--accent-color);
}

.notif-bell-btn:hover {
  background: var(--accent-hover);
}

.notif-bell-dot {
  position: absolute;
  top: 8px;
  right: 8px;
  width: 8px;
  height: 8px;
  background: #ff4757;
  border-radius: 50%;
  border: 2px solid white;
  animation: pulse 2s infinite;
}

@keyframes pulse {
  0% { transform: scale(1); opacity: 1; }
  50% { transform: scale(1.2); opacity: 0.8; }
  100% { transform: scale(1); opacity: 1; }
}

/* Ensure the dropdown has the highest z-index */
.notif-dropdown {
  position: absolute;
  top: 56px;
  right: 0;
  min-width: 320px;
  max-width: 400px;
  max-height: 350px;
  background: var(--bg-secondary);
  border: 1.5px solid var(--border-color);
  border-radius: 16px;
  box-shadow: 0 20px 64px rgba(0, 0, 0, 0.2), 0 8px 24px rgba(0, 0, 0, 0.15), 0 4px 8px rgba(0, 0, 0, 0.1);
  z-index: 999999; /* Super high z-index to ensure it's on top */
  padding: 1rem;
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
  overflow-y: auto;
  overflow-x: hidden;
  backdrop-filter: blur(30px);
  transform-origin: top right;
  animation: dropdownSlide 0.2s cubic-bezier(0.4, 0, 0.2, 1) forwards;
  /* Prevent the dropdown from being clipped */
  will-change: transform;
  isolation: isolate;
}

@keyframes dropdownSlide {
  from {
    opacity: 0;
    transform: translateY(-10px) scale(0.95);
  }
  to {
    opacity: 1;
    transform: translateY(0) scale(1);
  }
}

.notif-dropdown::before {
  content: '';
  position: absolute;
  top: -8px;
  right: 25px;
  width: 0;
  height: 0;
  border-left: 8px solid transparent;
  border-right: 8px solid transparent;
  border-bottom: 8px solid var(--border-color);
  z-index: 1;
}

.notif-dropdown::after {
  content: '';
  position: absolute;
  top: -6px;
  right: 26px;
  width: 0;
  height: 0;
  border-left: 7px solid transparent;
  border-right: 7px solid transparent;
  border-bottom: 7px solid var(--bg-secondary);
  z-index: 2;
}

.notif-dropdown::-webkit-scrollbar {
  width: 6px;
}

.notif-dropdown::-webkit-scrollbar-track {
  background: var(--bg-accent);
  border-radius: 10px;
}

.notif-dropdown::-webkit-scrollbar-thumb {
  background: var(--accent-color);
  border-radius: 10px;
  opacity: 0.7;
}

.notif-dropdown::-webkit-scrollbar-thumb:hover {
  background: var(--accent-hover);
  opacity: 1;
}

.notif-dropdown-header {
  font-weight: 700;
  color: var(--text-accent);
  font-size: 1.1rem;
  margin-bottom: 0.5rem;
  padding-bottom: 0.5rem;
  border-bottom: 1px solid var(--border-color);
  text-align: center;
}

.notif-dropdown-empty {
  color: var(--text-muted);
  font-size: 0.9rem;
  text-align: center;
  padding: 2rem 1rem;
  font-style: italic;
}

.notif-dropdown-item {
  background: var(--bg-accent);
  border-radius: 12px;
  padding: 0.875rem;
  border: 1px solid var(--border-color);
  display: flex;
  flex-direction: column;
  gap: 0.375rem;
  transition: all 0.2s ease;
  cursor: pointer;
}

.notif-dropdown-item:hover {
  background: var(--bg-accent-hover);
  transform: translateX(2px);
  border-color: var(--accent-color);
}

.notif-title {
  font-weight: 600;
  color: var(--text-accent);
  font-size: 0.95rem;
  line-height: 1.3;
}

.notif-body {
  font-size: 0.85rem;
  color: var(--text-secondary);
  line-height: 1.4;
}

.notif-date {
  font-size: 0.75rem;
  color: var(--text-muted);
  align-self: flex-end;
  margin-top: 0.25rem;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1rem;
  margin-bottom: 1.5rem;
}

.stat-card {
  background: var(--bg-card);
  backdrop-filter: blur(20px);
  border-radius: 16px;
  padding: 1.25rem;
  display: flex;
  align-items: center;
  gap: 1rem;
  box-shadow: 0 6px 24px var(--shadow-medium);
  border: 1px solid var(--border-color);
  transition: all 0.3s ease;
}

.stat-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 32px var(--shadow-strong);
}

.stat-icon {
  width: 45px;
  height: 45px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  flex-shrink: 0;
}

.stat-icon.classes {
  background: linear-gradient(135deg, var(--accent-color) 0%, #A3D1C6 100%);
}

.stat-icon.graded {
  background: linear-gradient(135deg, #B3D8A8 0%, var(--accent-color) 100%);
}

.stat-icon.pending {
  background: linear-gradient(135deg, #A3D1C6 0%, #B3D8A8 100%);
}

.stat-number {
  font-size: 1.75rem;
  font-weight: 800;
  color: var(--text-accent);
  line-height: 1;
}

.stat-label {
  font-size: 0.75rem;
  font-weight: 600;
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-top: 0.25rem;
}

.content-grid {
  display: grid;
  grid-template-columns: 1.8fr 1fr;
  gap: 1.5rem;
  height: calc(100vh - 420px);
  min-height: 350px;
}

.content-card {
  background: var(--bg-card);
  backdrop-filter: blur(20px);
  border-radius: 20px;
  padding: 1.5rem;
  box-shadow: 0 6px 24px var(--shadow-medium);
  border: 1px solid var(--border-color);
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

.card-header {
  margin-bottom: 1.25rem;
  flex-shrink: 0;
}

.card-header h3 {
  font-size: 1.25rem;
  font-weight: 700;
  color: var(--text-accent);
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin-bottom: 0.375rem;
}

.card-subtitle {
  color: var(--text-secondary);
  font-size: 0.875rem;
}

.assessment-list {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
  flex: 1;
  overflow-y: auto;
  padding-right: 0.5rem;
  margin-right: -0.5rem;
}

.assessment-list::-webkit-scrollbar {
  width: 6px;
}

.assessment-list::-webkit-scrollbar-track {
  background: var(--bg-accent);
  border-radius: 10px;
}

.assessment-list::-webkit-scrollbar-thumb {
  background: var(--accent-color);
  border-radius: 10px;
  opacity: 0.7;
}

.assessment-list::-webkit-scrollbar-thumb:hover {
  background: var(--accent-hover);
  opacity: 1;
}

.assessment-item {
  background: var(--bg-accent);
  border-radius: 12px;
  padding: 1rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  border: 1px solid var(--border-color);
  transition: all 0.3s ease;
  flex-shrink: 0;
}

.assessment-item:hover {
  background: var(--bg-accent-hover);
  transform: translateX(4px);
}

.assessment-info h4 {
  font-weight: 600;
  color: var(--text-accent);
  margin-bottom: 0.2rem;
  font-size: 0.95rem;
}

.assessment-class {
  font-size: 0.8rem;
  color: var(--text-muted);
  margin-bottom: 0.2rem;
}

.assessment-progress {
  font-size: 0.8rem;
  font-weight: 600;
  color: var(--text-accent);
}

.grade-btn {
  background: linear-gradient(135deg, var(--accent-color) 0%, #A3D1C6 100%);
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 8px;
  font-size: 0.8rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 2px 8px var(--shadow-light);
}

.grade-btn:hover {
  transform: translateY(-1px);
  box-shadow: 0 4px 12px var(--shadow-medium);
}

.empty-state {
  text-align: center;
  color: var(--text-muted);
  padding: 2rem;
  font-style: italic;
  font-size: 0.9rem;
}

.quick-links-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0.75rem;
  flex: 1;
  overflow-y: auto;
  padding-right: 0.5rem;
  margin-right: -0.5rem;
  align-content: start;
}

.quick-links-grid::-webkit-scrollbar {
  width: 6px;
}

.quick-links-grid::-webkit-scrollbar-track {
  background: var(--bg-accent);
  border-radius: 10px;
}

.quick-links-grid::-webkit-scrollbar-thumb {
  background: var(--accent-color);
  border-radius: 10px;
  opacity: 0.7;
}

.quick-links-grid::-webkit-scrollbar-thumb:hover {
  background: var(--accent-hover);
  opacity: 1;
}

.quick-link-btn {
  background: var(--bg-accent);
  border: 1px solid var(--border-color);
  border-radius: 12px;
  padding: 1rem 0.75rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.375rem;
  cursor: pointer;
  transition: all 0.3s ease;
  font-weight: 600;
  color: var(--text-accent);
  text-decoration: none;
  text-align: center;
  font-size: 0.85rem;
  height: fit-content;
  min-height: 80px;
}

.quick-link-btn:hover {
  background: var(--bg-accent-hover);
  transform: translateY(-2px);
  box-shadow: 0 6px 20px var(--shadow-strong);
  text-decoration: none;
  color: var(--text-accent);
}

.link-description {
  font-size: 0.7rem;
  font-weight: 400;
  color: var(--text-muted);
  margin-top: 0.2rem;
}

@media (max-width: 1200px) {
  .home-container {
    padding: 1rem;
  }
  
  .content-grid {
    grid-template-columns: 1fr;
    height: auto;
  }
  
  .stats-grid {
    grid-template-columns: 1fr;
    gap: 0.75rem;
  }
}

  @media (max-width: 768px) {
    .notif-dropdown {
      position: fixed; /* Use fixed positioning on mobile */
      top: auto;
      bottom: 20px; /* Position from bottom */
      right: 0.75rem;
      left: 0.75rem;
      min-width: auto;
      max-width: none;
      max-height: 300px;
      z-index: 999999;
      transform-origin: center bottom;
    }
    /* Remove the arrow on mobile since it's positioned differently */
    .notif-dropdown::before,
    .notif-dropdown::after {
      display: none;
    }
    /* Alternative: Keep it at top but with better positioning */
    .notif-dropdown.top-positioned {
      position: fixed;
      top: 120px;
      bottom: auto;
      transform-origin: top center;
    }
    .notif-dropdown.top-positioned::before {
      display: block;
      right: 40px;
    }
    .notif-dropdown.top-positioned::after {
      display: block;
      right: 41px;
    }
  }

/* Add a backdrop overlay to prevent interaction with other elements */
.notif-backdrop {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 99999; /* Just below dropdown */
  background: transparent;
  display: none;
}

.notif-backdrop.active {
  display: block;
}
</style>