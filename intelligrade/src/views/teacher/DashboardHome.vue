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
              <span v-if="!isLoadingName">Hello, {{ fullName }}!</span>
              <span v-else>Hello, Loading...</span>
            </div>
            <div class="section-header-subtitle">Welcome to your teaching dashboard</div>
            <div class="section-header-description">Manage your classes, grade assessments, and track student progress</div>
          </div>
        </div>
        
        <div class="header-badge">
          <div class="badge-content">
            <div class="badge-text">Active Teacher</div>
          </div>
        </div>
      </div>
    </div>

    <!-- Stats Cards -->
    <div class="stats-grid">
      <div class="stat-card">
        <div class="stat-icon classes">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
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
          <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
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
          <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
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

    <!-- Main Content Grid -->
    <div class="content-grid">
      <!-- Assessments to Grade -->
      <div class="content-card">
        <div class="card-header">
          <h3>
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
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
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M13,9H18.5L13,3.5V9M6,2H14L20,8V20A2,2 0 0,1 18,22H6C4.89,22 4,21.1 4,20V4C4,2.89 4.89,2 6,2M15,18V16H6V18H15M18,14V12H6V14H18Z" />
            </svg>
            Quick Links
          </h3>
          <p class="card-subtitle">Navigate to key features quickly.</p>
        </div>
        <div class="quick-links-grid">
          <router-link to="/teacher/subjects" class="quick-link-btn quiz">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M14,2H6A2,2 0 0,0 4,4V20A2,2 0 0,0 6,22H18A2,2 0 0,0 20,20V8L14,2M18,20H6V4H13V9H18V20Z" />
            </svg>
            Make Quiz
            <span class="link-description">Create interactive quizzes</span>
          </router-link>
          <router-link to="/teacher/upload-assessment" class="quick-link-btn upload">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M14,2H6A2,2 0 0,0 4,4V20A2,2 0 0,0 6,22H18A2,2 0 0,0 20,20V8L14,2M18,20H6V4H13V9H18V20Z" />
            </svg>
            Upload Assessment
            <span class="link-description">Upload for auto-grading</span>
          </router-link>
          <button @click="navigateToClasses" class="quick-link-btn classes">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path>
              <circle cx="9" cy="7" r="4"></circle>
              <path d="M23 21v-2a4 4 0 0 0-3-3.87"></path>
              <path d="M16 3.13a4 4 0 0 1 0 7.75"></path>
            </svg>
            My Classes
            <span class="link-description">Manage your classes</span>
          </button>
          <button @click="navigateToGradebook" class="quick-link-btn gradebook">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
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
      fullName: 'Teacher', // Default fallback
      totalClasses: 0,
      gradedToday: 0,
      pendingReviews: 0,
      assessmentsToGrade: [],
      pollInterval: null,
      isLoadingName: true
    };
  },
  methods: {
    async loadTeacherProfile() {
      try {
        // Get the current user from Supabase auth
        const { data: { user }, error: authError } = await supabase.auth.getUser();
        
        if (authError || !user) {
          console.error('Auth error:', authError);
          this.$router.push('/login');
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
          this.fullName = 'Teacher';
        } else if (profile) {
          this.fullName = profile.full_name || 'Teacher';
        }
      } catch (error) {
        console.error('Error loading teacher profile:', error);
        this.fullName = 'Teacher';
      } finally {
        this.isLoadingName = false;
      }
    },

    async fetchDashboardStats() {
      try {
        // Replace with your actual backend API endpoints
        const response = await fetch('/api/teacher/dashboard-stats');
        if (response.ok) {
          const stats = await response.json();
          this.totalClasses = stats.totalClasses || 3;
          this.gradedToday = stats.gradedToday || 5;
          this.pendingReviews = stats.pendingReviews || 8;
        } else {
          // Fallback to sample data
          this.totalClasses = 3;
          this.gradedToday = 5;
          this.pendingReviews = 8;
        }
      } catch (err) {
        console.log('Using sample data for dashboard stats');
        // Sample data fallback
        this.totalClasses = 3;
        this.gradedToday = 5;
        this.pendingReviews = 8;
      }
    },

    async fetchAssessmentsToGrade() {
      try {
        const response = await fetch('/api/teacher/assessments-to-grade');
        if (response.ok) {
          const assessments = await response.json();
          this.assessmentsToGrade = Array.isArray(assessments) ? assessments : [];
        } else {
          // Fallback to sample data
          this.assessmentsToGrade = [
            { id: 1, title: 'Algebra Quiz 1', className: 'Math 101', studentsSubmitted: 15, totalStudents: 20 },
            { id: 2, title: 'Science Test 2', className: 'Science 101', studentsSubmitted: 22, totalStudents: 25 },
          ];
        }
      } catch (err) {
        console.log('Using sample data for assessments');
        // Sample data fallback
        this.assessmentsToGrade = [
          { id: 1, title: 'Algebra Quiz 1', className: 'Math 101', studentsSubmitted: 15, totalStudents: 20 },
          { id: 2, title: 'Science Test 2', className: 'Science 101', studentsSubmitted: 22, totalStudents: 25 },
        ];
      }
    },

    gradeAssessment(assessment) {
      console.log('Grading assessment:', assessment.title);
      // Add navigation to grading interface
      // this.$router.push(`/teacher/grade/${assessment.id}`);
    },

    navigateToClasses() {
      // this.$router.push('/teacher/classes');
      console.log('Navigate to classes');
    },

    navigateToGradebook() {
      // this.$router.push('/teacher/gradebook');
      console.log('Navigate to gradebook');
    },

    async fetchAllData() {
      await Promise.all([
        this.fetchDashboardStats(),
        this.fetchAssessmentsToGrade()
      ]);
    }
  },
  async mounted() {
    await this.loadTeacherProfile();
    await this.fetchAllData();
    
    // Set up real-time polling every 30 seconds
    this.pollInterval = setInterval(this.fetchAllData, 30000);
  },
  beforeDestroy() {
    if (this.pollInterval) {
      clearInterval(this.pollInterval);
    }
  }
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

/* CSS Variables for consistent theming */
:root {
  --bg-primary: linear-gradient(135deg, #FBFFE4 0%, #B3D8A8 50%, #A3D1C6 100%);
  --bg-secondary: rgba(255, 255, 255, 0.85);
  --bg-card: rgba(255, 255, 255, 0.9);
  --bg-accent: rgba(251, 255, 228, 0.7);
  --bg-accent-hover: rgba(251, 255, 228, 0.9);
  --text-accent: #3D8D7A;
  --text-secondary: #666;
  --text-muted: #777;
  --border-color: rgba(61, 141, 122, 0.15);
  --shadow-light: rgba(61, 141, 122, 0.05);
  --shadow-medium: rgba(61, 141, 122, 0.1);
  --shadow-strong: rgba(61, 141, 122, 0.2);
}

.home-container {
  padding: 2rem;
  max-width: 1200px;
  margin: 0 auto;
  font-family: 'Inter', sans-serif;
  background: var(--bg-primary);
  min-height: 100vh;
  position: relative;
  overflow-x: hidden;
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

/* Enhanced Header Design */
.section-header-card {
  position: relative;
  background: var(--bg-secondary);
  backdrop-filter: blur(20px);
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
  background: linear-gradient(135deg, #3D8D7A 0%, #A3D1C6 100%);
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
  background: linear-gradient(135deg, #3D8D7A 0%, #A3D1C6 100%);
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

.badge-text {
  font-size: 0.9rem;
  font-weight: 600;
  color: var(--text-accent);
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

/* Stats Grid */
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

.stat-icon.classes {
  background: linear-gradient(135deg, #3D8D7A 0%, #A3D1C6 100%);
}

.stat-icon.graded {
  background: linear-gradient(135deg, #B3D8A8 0%, #3D8D7A 100%);
}

.stat-icon.pending {
  background: linear-gradient(135deg, #A3D1C6 0%, #B3D8A8 100%);
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

.assessment-class {
  font-size: 0.875rem;
  color: var(--text-muted);
  margin-bottom: 0.25rem;
}

.assessment-progress {
  font-size: 0.875rem;
  font-weight: 600;
  color: var(--text-accent);
}

.grade-btn {
  background: linear-gradient(135deg, #3D8D7A 0%, #A3D1C6 100%);
  color: white;
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 12px;
  font-size: 0.9rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 4px 16px rgba(61, 141, 122, 0.2);
}

.grade-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(61, 141, 122, 0.3);
}

.empty-state {
  text-align: center;
  color: var(--text-muted);
  padding: 2rem;
  font-style: italic;
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
  gap: 0.5rem;
  cursor: pointer;
  transition: all 0.3s ease;
  font-weight: 600;
  color: var(--text-accent);
  text-decoration: none;
  text-align: center;
}

.quick-link-btn:hover {
  background: var(--bg-accent-hover);
  transform: translateY(-2px);
  box-shadow: 0 8px 25px var(--shadow-strong);
  text-decoration: none;
  color: var(--text-accent);
}

.link-description {
  font-size: 0.75rem;
  font-weight: 400;
  color: var(--text-muted);
  margin-top: 0.25rem;
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
  
  .assessment-item {
    flex-direction: column;
    align-items: stretch;
    gap: 1rem;
  }
}
</style>