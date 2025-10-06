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
          <div class="stat-label">Total Classes</div>
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
          
          <button @click="navigateToClasses" class="quick-link">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path>
              <circle cx="9" cy="7" r="4"></circle>
              <path d="M23 21v-2a4 4 0 0 0-3-3.87"></path>
              <path d="M16 3.13a4 4 0 0 1 0 7.75"></path>
            </svg>
            <span>My Classes</span>
          </button>
          
          <button @click="navigateToGradebook" class="quick-link">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M19,3H14.82C14.4,1.84 13.3,1 12,1C10.7,1 9.6,1.84 9.18,3H5A2,2 0 0,0 3,5V19A2,2 0 0,0 5,21H19A2,2 0 0,0 21,19V5A2,2 0 0,0 19,3M12,3A1,1 0 0,1 13,4A1,1 0 0,1 12,5A1,1 0 0,1 11,4A1,1 0 0,1 12,3Z" />
            </svg>
            <span>Gradebook</span>
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
        const year = new Date().getFullYear();
        const shortId = profileId.slice(-6).toUpperCase();
        const random = Math.floor(Math.random() * 99).toString().padStart(2, '0');
        const employeeId = `T${year}${shortId}${random}`;
        
          .select('employee_id')
          .eq('employee_id', employeeId)
          .single();
        
        if (existingTeacher) {
      color: #F3F4F6;
        }
        
        console.log('Generated employee ID:', employeeId);
        return employeeId;
      } catch (error) {
        console.error('Error generating employee ID:', error);
        return `T${Date.now().toString().slice(-8)}`;
      }
    },

      color: #A3D1C6;
      try {
        if (!this.teacherId) {
          console.warn('No teacher ID available for dashboard stats');
      background: #23272b;
      border-color: #A3D1C6;
      color: #A3D1C6;
          return;
        }

      background: #20c997;
      color: #181c20;
      transform: scale(1.05);
          .select('subject_id')
          .eq('teacher_id', this.teacherId);

      background: #23272b;
      border-color: #23272b;
      box-shadow: 0 8px 24px rgba(0,0,0,0.35);
          const uniqueSubjects = new Set(subjects?.map(s => s.subject_id) || []);
          this.totalClasses = uniqueSubjects.size;
          console.log('Total classes:', this.totalClasses);
      color: #F3F4F6;
      background: #23272b;
      border-bottom: 1px solid #A3D1C6;
        this.pendingReviews = 0;

        await this.loadAssessmentsToGrade();
      border-bottom: 1px solid #23272b;
      } catch (error) {
        console.error('Error loading dashboard stats:', error);
        this.totalClasses = 0;
      background: #23272b;
        this.pendingReviews = 0;
      }
    },
      background: #23272b;
      border-color: #A3D1C6;
      try {
        this.assessmentsToGrade = [
          { 
      background: #181c20;
      border-color: #20c997;
            className: 'Grade 7 Math', 
            studentsSubmitted: 15, 
            totalStudents: 20 
      background: #20c997;
      color: #181c20;
      border: none;
      box-shadow: none;
            id: 2, 
            title: 'Science Test', 
            className: 'Grade 8 Science', 
      background: #A3D1C6;
      color: #181c20;
            studentsSubmitted: 18, 
            totalStudents: 22 
          }
      background: #23272b;
      border-color: #A3D1C6;
      color: #A3D1C6;

      } catch (error) {
        console.error('Error loading assessments to grade:', error);
      background: #20c997;
      color: #181c20;
    },

    async fetchDashboardStats() {
      color: #20c997;
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
  border-radius: 16px;
  padding: 1.5rem;
  margin-bottom: 1.5rem;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
}
.dark .header-card {
  background: #23272b;
  box-shadow: 0 2px 8px rgba(0,0,0,0.25);
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
  font-weight: 700;
  color: #1f2937;
  margin-bottom: 0.25rem;
}
.dark .header-title {
  color: #F3F4F6;
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
  color: #F3F4F6;
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
  color: #F3F4F6;
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
  grid-template-columns: repeat(3, 1fr);
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
.stat-graded { background: #B3D8A8; }
.stat-pending { background: #A3D1C6; }

.stat-number {
  font-size: 1.875rem;
  font-weight: 700;
  color: #1f2937;
  line-height: 1;
}
.dark .stat-number {
  color: #F3F4F6;
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
  color: #F3F4F6;
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
  border: 1px solid #e5e7eb;
}
.dark .assessment-item {
  background: #23272b;
  border-color: #3D8D7A;
}

.assessment-item:hover {
  background: #f0f9ff;
  border-color: #A3D1C6;
}
.dark .assessment-item:hover {
  background: #181c20;
  border-color: #A3D1C6;
}

.assessment-info h4 {
  font-size: 0.938rem;
  font-weight: 600;
  color: #1f2937;
  margin-bottom: 0.25rem;
}
.dark .assessment-info h4 {
  color: #F3F4F6;
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
  background: #3D8D7A;
  color: white;
  border: none;
  padding: 0.5rem 1.25rem;
  border-radius: 8px;
  font-size: 0.875rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s;
}
.dark .grade-btn {
  background: #3D8D7A;
  color: #F3F4F6;
}

.grade-btn:hover {
  background: #2d6b5f;
  transform: translateY(-1px);
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
  border: 1px solid #e5e7eb;
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
  border-color: #3D8D7A;
  color: #A3D1C6;
}

.quick-link:hover {
  background: #A3D1C6;
  border-color: #3D8D7A;
  transform: translateY(-2px);
}
.dark .quick-link:hover {
  background: #3D8D7A;
  color: #F3F4F6;
}

.quick-link svg {
  color: #3D8D7A;
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
  
  .header-content {
    flex-direction: column;
    gap: 1rem;
  }
  
  .header-left {
    width: 100%;
  }
  
  .notif-wrapper {
    align-self: flex-end;
  }
  
  .notif-dropdown {
    right: 0;
    left: auto;
    width: calc(100vw - 3rem);
    max-width: 320px;
  }
}
</style>