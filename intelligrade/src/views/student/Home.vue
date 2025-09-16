<template>
  <div class="home-container">
    <!-- Enhanced Header Section -->
    <div class="section-header-card">
      <!-- Background Decorations -->
      <div class="header-bg-decoration"></div>
      <div class="floating-shapes">
        <div class="shape shape-1"></div>
        <div class="shape shape-2"></div>
        <div class="shape shape-3"></div>
      </div>
      
      <div class="section-header-content">
        <div class="section-header-left">
          <div class="section-header-icon">
            <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
              <circle cx="12" cy="7" r="4"></circle>
            </svg>
          </div>
          <div class="header-text">
            <div class="section-header-title">
              <span v-if="!isLoadingName">Hello, {{ studentName }}!</span>
              <span v-else>Hello, Loading...</span>
            </div>
            <div class="section-header-subtitle">Welcome to your student dashboard</div>
            <div class="section-header-description">Track your academic progress and stay on top of your studies</div>
          </div>
        </div>
        
        <div class="header-badge">
          <div class="badge-content">
            <div class="badge-text">Active Student</div>
          </div>
        </div>
      </div>
    </div>

    <!-- Stats Cards -->
    <div class="stats-grid">
      <div class="stat-card">
        <div class="stat-icon subjects">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
            <path d="M19,3H5C3.9,3 3,3.9 3,5V19C3,20.1 3.9,21 5,21H19C20.1,21 21,20.1 21,19V5C21,3.9 20.1,3 19,3M5,19V5H19V19H5Z" />
          </svg>
        </div>
        <div class="stat-content">
          <div class="stat-number">{{ totalSubjects }}</div>
          <div class="stat-label">ENROLLED SUBJECTS</div>
        </div>
      </div>

      <div class="stat-card">
        <div class="stat-icon assessments">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
            <path d="M14,2H6A2,2 0 0,0 4,4V20A2,2 0 0,0 6,22H18A2,2 0 0,0 20,20V8L14,2M18,20H6V4H13V9H18V20Z" />
          </svg>
        </div>
        <div class="stat-content">
          <div class="stat-number">{{ pendingAssessments }}</div>
          <div class="stat-label">PENDING ASSESSMENTS</div>
        </div>
      </div>
    </div>

    <!-- Main Content Grid -->
    <div class="content-grid">
      <!-- Recent Assessments -->
      <div class="content-card">
        <div class="card-header">
          <h3>
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M14,2H6A2,2 0 0,0 4,4V20A2,2 0 0,0 6,22H18A2,2 0 0,0 20,20V8L14,2M18,20H6V4H13V9H18V20Z" />
            </svg>
            Recent Assessments
          </h3>
          <p class="card-subtitle">Keep track of your upcoming deadlines.</p>
        </div>
        <div class="assessment-list">
          <div v-for="assessment in recentAssessments" :key="assessment.id" class="assessment-item">
            <div class="assessment-info">
              <h4>{{ assessment.title }}</h4>
              <p class="assessment-subject">{{ assessment.subject }}</p>
            </div>
            <div class="assessment-due">
              <span class="due-date">{{ formatDate(assessment.dueDate) }}</span>
              <span :class="['status', assessment.status]">{{ assessment.status }}</span>
            </div>
          </div>
        </div>
      </div>

      <!-- Quick Links -->
      <div class="content-card">
        <div class="card-header">
          <h3>
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M13,9H18.5L13,3.5V9M6,2H14L20,8V20A2,2 0 0,1 18,22H6C4.89,22 4,21.1 4,20V4C4,2.89 4.89,2 6,2M15,18V16H6V18H15M18,14V12H6V14H18Z" />
            </svg>
            Quick Links
          </h3>
          <p class="card-subtitle">Navigate to key features quickly.</p>
        </div>
        <div class="quick-links-grid">
          <button @click="navigateToSubjects" class="quick-link-btn subjects">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M19,3H5C3.9,3 3,3.9 3,5V19C3,20.1 3.9,21 5,21H19C20.1,21 21,20.1 21,19V5C21,3.9 20.1,3 19,3M5,19V5H19V19H5Z" />
            </svg>
            My Subjects
          </button>
          <button @click="navigateToCalendar" class="quick-link-btn calendar">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M19,19H5V8H19M19,3H18V1H16V3H8V1H6V3H5C3.89,3 3,3.89 3,5V19A2,2 0 0,0 5,21H19A2,2 0 0,0 21,19V5C21,3.89 20.1,3 19,3M16.5,13.5H11V18.5H16.5V13.5Z" />
            </svg>
            Calendar
          </button>
          <button @click="navigateToMessages" class="quick-link-btn messages">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M22 6c0-1.1-.9-2-2-2H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6zM4 6h16v.5l-8 5-8-5V6zm0 13.5V8l8 5 8-5v11.5H4z" />
            </svg>
            Messages
          </button>
          <button @click="navigateToSettings" class="quick-link-btn settings">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M12,15.5A3.5,3.5 0 0,1 8.5,12A3.5,3.5 0 0,1 12,8.5A3.5,3.5 0 0,1 15.5,12A3.5,3.5 0 0,1 12,15.5M19.43,12.97C19.47,12.65 19.5,12.33 19.5,12C19.5,11.67 19.47,11.34 19.43,11.03L21.54,9.37C21.73,9.22 21.78,8.96 21.66,8.74L19.65,5.27C19.54,5.05 19.27,4.96 19.05,5.05L16.56,6.05C16.04,5.66 15.5,5.32 14.9,5.07L14.5,2.42C14.46,2.18 14.25,2 14,2H10C9.75,2 9.54,2.18 9.5,2.42L9.1,5.07C8.5,5.32 7.96,5.66 7.44,6.05L4.95,5.05C4.73,4.96 4.46,5.05 4.34,5.27L2.34,8.74C2.21,8.96 2.27,9.22 2.46,9.37L4.57,11.03C4.53,11.34 4.5,11.67 4.5,12C4.5,12.33 4.53,12.65 4.57,12.97L2.46,14.63C2.27,14.78 2.21,15.04 2.34,15.26L4.34,18.73C4.46,18.95 4.73,19.04 4.95,18.95L7.44,17.94C7.96,18.34 8.5,18.68 9.1,18.93L9.5,21.58C9.54,21.82 9.75,22 10,22H14C14.25,22 14.46,21.82 14.5,21.58L14.9,18.93C15.5,18.68 16.04,18.34 16.56,17.94L19.05,18.95C19.27,19.04 19.54,18.95 19.66,18.73L21.66,15.26C21.78,15.04 21.73,14.78 21.54,14.63L19.43,12.97Z" />
            </svg>
            Settings
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { supabase } from '../../supabase.js';

export default {
  name: 'Home',
  data() {
    return {
      studentName: 'Student', // Default fallback
      totalSubjects: 0,
      pendingAssessments: 0,
      recentAssessments: [],
      pollInterval: null,
      isLoadingName: true
    };
  },
  methods: {
    async loadStudentProfile() {
      try {
        // Get the current user from Supabase auth
        const { data: { user }, error: authError } = await supabase.auth.getUser();
        
        if (authError || !user) {
          console.error('Auth error:', authError);
          this.studentName = 'Student';
          this.isLoadingName = false;
          return;
        }

        // Fetch the user profile from the profiles table
        const { data: profile, error: profileError } = await supabase
          .from('profiles')
          .select('full_name')
          .eq('id', user.id)
          .single();

        if (profileError) {
          console.error('Profile error:', profileError);
          this.studentName = 'Student';
        } else if (profile) {
          this.studentName = profile.full_name || 'Student';
        }
      } catch (error) {
        console.error('Error loading student profile:', error);
        this.studentName = 'Student';
      } finally {
        this.isLoadingName = false;
      }
    },
    formatDate(date) {
      if (!date) return '';
      const d = typeof date === 'string' ? new Date(date) : date;
      return d.toLocaleDateString('en-US', {
        month: 'short',
        day: 'numeric'
      });
    },
    navigateToSubjects() {
      this.$parent.navigateTo('subjects');
    },
    navigateToCalendar() {
      this.$parent.navigateTo('calendar');
    },
    navigateToMessages() {
      this.$parent.navigateTo('messages');
    },
    navigateToSettings() {
      this.$parent.navigateTo('settings');
    },
    async fetchDashboardData() {
      try {
        // Replace with your actual backend API endpoints
        const statsRes = await fetch('/api/student/dashboard-stats');
        const stats = await statsRes.json();
        this.studentName = stats.studentName || 'Student Juan';
        this.totalSubjects = stats.totalSubjects || 0;
        this.pendingAssessments = stats.pendingAssessments || 0;

        const assessmentsRes = await fetch('/api/student/recent-assessments');
        const assessments = await assessmentsRes.json();
        this.recentAssessments = Array.isArray(assessments)
          ? assessments.map(a => ({
              ...a,
              dueDate: a.dueDate ? new Date(a.dueDate) : null
            }))
          : [];
      } catch (err) {
        // Optionally handle error
        // console.error('Failed to fetch dashboard data', err);
      }
    }
  },
  async mounted() {
    await this.loadStudentProfile();
    this.fetchDashboardData();
    this.pollInterval = setInterval(this.fetchDashboardData, 5000);
  },
  beforeDestroy() {
    if (this.pollInterval) clearInterval(this.pollInterval);
  }
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

.home-container {
  padding: 2rem;
  max-width: 1200px;
  margin: 0 auto;
  font-family: 'Inter', sans-serif;
  background: var(--bg-primary);
  min-height: 100vh;
}

/* Enhanced Header Design */
.section-header-card {
  position: relative;
  background: linear-gradient(135deg, var(--bg-primary) 0%, var(--bg-secondary) 100%);
  border-radius: 32px;
  padding: 3.5rem;
  margin-bottom: 2.5rem;
  min-height: 180px;
  box-shadow: 
    0 24px 48px var(--shadow-medium),
    0 12px 24px var(--shadow-light),
    inset 0 1px 0 rgba(255, 255, 255, 0.8);
  border: 2px solid var(--border-color);
  overflow: hidden;
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}

.section-header-card:hover {
  transform: translateY(-2px);
  box-shadow: 
    0 32px 64px var(--shadow-strong),
    0 16px 32px var(--shadow-medium),
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
  width: 120px;
  height: 120px;
  top: -30px;
  right: 10%;
  animation: float 6s ease-in-out infinite;
}

.shape-2 {
  width: 80px;
  height: 80px;
  bottom: -20px;
  right: 25%;
  animation: float 8s ease-in-out infinite reverse;
}

.shape-3 {
  width: 60px;
  height: 60px;
  top: 50%;
  right: 5%;
  animation: float 7s ease-in-out infinite;
}

@keyframes float {
  0%, 100% { transform: translateY(0) rotate(0deg); }
  50% { transform: translateY(-20px) rotate(10deg); }
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
  gap: 2.5rem;
}

.section-header-icon {
  width: 80px;
  height: 80px;
  background: linear-gradient(135deg, #4dbb98 0%, #33806b 100%);
  border-radius: 24px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #fff;
  box-shadow: 
    0 12px 24px rgba(61, 141, 122, 0.2),
    inset 0 1px 0 rgba(255, 255, 255, 0.2);
  transition: all 0.3s ease;
}

.section-header-icon:hover {
  transform: scale(1.05);
}

.header-text {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.section-header-title {
  font-size: 2.5rem;
  font-weight: 800;
  color: var(--text-accent);
  letter-spacing: -0.02em;
  background: linear-gradient(135deg, #33806b 0%, #4dbb98 100%);
  background-clip: text;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  margin-bottom: 0.25rem;
}

.section-header-subtitle {
  font-size: 1.25rem;
  font-weight: 600;
  color: var(--text-secondary);
  margin-bottom: 0.25rem;
}

.section-header-description {
  font-size: 1rem;
  color: var(--text-muted);
  font-weight: 400;
  opacity: 0.9;
}

.header-badge {
  background: rgba(77, 187, 152, 0.1);
  border: 2px solid rgba(77, 187, 152, 0.2);
  border-radius: 20px;
  padding: 1rem 1.5rem;
  backdrop-filter: blur(10px);
}

.badge-content {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.badge-icon {
  font-size: 1.5rem;
}

.badge-text {
  font-size: 0.9rem;
  font-weight: 600;
  color: var(--text-accent);
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

/* Rest of the styles remain the same */
.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1.5rem;
  margin-bottom: 2rem;
}

.stat-card {
  background: var(--bg-card);
  backdrop-filter: blur(20px);
  border-radius: 20px;
  padding: 2rem;
  display: flex;
  align-items: center;
  gap: 1.5rem;
  box-shadow: 0 8px 32px var(--shadow-medium);
  border: 1px solid var(--border-color);
  transition: all 0.3s ease;
}

.stat-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 40px var(--shadow-strong);
}

.stat-icon {
  width: 60px;
  height: 60px;
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
}

.stat-icon.subjects {
  background: linear-gradient(135deg, #3D8D7A 0%, #A3D1C6 100%);
}

.stat-icon.assessments {
  background: linear-gradient(135deg, #B3D8A8 0%, #3D8D7A 100%);
}

.stat-number {
  font-size: 2.5rem;
  font-weight: 800;
  color: var(--text-accent);
  line-height: 1;
}

.stat-label {
  font-size: 0.875rem;
  font-weight: 600;
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-top: 0.5rem;
}

.content-grid {
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: 2rem;
}

.content-card {
  background: var(--bg-card);
  backdrop-filter: blur(20px);
  border-radius: 24px;
  padding: 2rem;
  box-shadow: 0 8px 32px var(--shadow-medium);
  border: 1px solid var(--border-color);
}

.card-header {
  margin-bottom: 2rem;
}

.card-header h3 {
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--text-accent);
  display: flex;
  align-items: center;
  gap: 0.75rem;
  margin-bottom: 0.5rem;
}

.card-subtitle {
  color: var(--text-secondary);
  font-size: 0.95rem;
}

.assessment-list {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.assessment-item {
  background: var(--bg-accent);
  border-radius: 16px;
  padding: 1.5rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  border: 1px solid var(--border-color);
  transition: all 0.3s ease;
}

.assessment-item:hover {
  background: var(--bg-accent-hover);
  transform: translateX(4px);
}

.assessment-info h4 {
  font-weight: 600;
  color: var(--text-accent);
  margin-bottom: 0.25rem;
}

.assessment-subject {
  font-size: 0.875rem;
  color: var(--text-muted);
}

.assessment-due {
  text-align: right;
}

.due-date {
  display: block;
  font-weight: 600;
  color: var(--text-accent);
  margin-bottom: 0.25rem;
}

.status {
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
  padding: 0.25rem 0.75rem;
  border-radius: 12px;
  letter-spacing: 0.5px;
}

.status.pending {
  background: rgba(255, 193, 7, 0.2);
  color: #e6b000;
}

.status.in-progress {
  background: rgba(61, 141, 122, 0.2);
  color: var(--text-accent);
}

.quick-links-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
}

.quick-link-btn {
  background: var(--bg-accent);
  border: 1px solid var(--border-color);
  border-radius: 16px;
  padding: 1.5rem 1rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.75rem;
  cursor: pointer;
  transition: all 0.3s ease;
  font-weight: 600;
  color: var(--text-accent);
  text-decoration: none;
}

.quick-link-btn:hover {
  background: var(--bg-accent-hover);
  transform: translateY(-2px);
  box-shadow: 0 8px 25px var(--shadow-strong);
}

@media (max-width: 768px) {
  .home-container {
    padding: 1rem;
  }
  
  .section-header-card {
    padding: 2.5rem 2rem;
    min-height: 140px;
  }
  
  .section-header-left {
    flex-direction: column;
    text-align: center;
    gap: 1.5rem;
  }
  
  .section-header-content {
    flex-direction: column;
    gap: 2rem;
  }
  
  .section-header-title {
    font-size: 2rem;
  }
  
  .content-grid {
    grid-template-columns: 1fr;
    gap: 1.5rem;
  }
  
  .stats-grid {
    grid-template-columns: 1fr;
  }
  
  .quick-links-grid {
    grid-template-columns: 1fr;
  }
}</style>