<template>
  <div class="home-container">
    <!-- Compact Header Section -->
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
        
        <div class="header-badge">
          <div class="badge-content">
            <div class="badge-text">Active Teacher</div>
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
      pollInterval: null,
      isLoadingName: true
    };
  },
  methods: {
    async loadTeacherProfile() {
      try {
        const { data: { user }, error: authError } = await supabase.auth.getUser();
        
        if (authError || !user) {
          console.error('Auth error:', authError);
          this.$router.push('/login');
          return;
        }

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
        const response = await fetch('/api/teacher/dashboard-stats');
        if (response.ok) {
          const stats = await response.json();
          this.totalClasses = stats.totalClasses || 3;
          this.gradedToday = stats.gradedToday || 5;
          this.pendingReviews = stats.pendingReviews || 8;
        } else {
          this.totalClasses = 3;
          this.gradedToday = 5;
          this.pendingReviews = 8;
        }
      } catch (err) {
        console.log('Using sample data for dashboard stats');
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
          this.assessmentsToGrade = [
            { id: 1, title: 'Algebra Quiz 1', className: 'Math 101', studentsSubmitted: 15, totalStudents: 20 },
            { id: 2, title: 'Science Test 2', className: 'Science 101', studentsSubmitted: 22, totalStudents: 25 },
          ];
        }
      } catch (err) {
        console.log('Using sample data for assessments');
        this.assessmentsToGrade = [
          { id: 1, title: 'Algebra Quiz 1', className: 'Math 101', studentsSubmitted: 15, totalStudents: 20 },
          { id: 2, title: 'Science Test 2', className: 'Science 101', studentsSubmitted: 22, totalStudents: 25 },
        ];
      }
    },

    gradeAssessment(assessment) {
      console.log('Grading assessment:', assessment.title);
    },

    navigateToClasses() {
      console.log('Navigate to classes');
    },

    navigateToGradebook() {
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

/* OPTIMIZED CONTAINER - Perfect screen fit */
.home-container {
  padding: 1.25rem;
  max-width: 100%;
  margin: 0;
  font-family: 'Inter', sans-serif;
  background: var(--bg-primary);
  height: 100vh;
  overflow-y: auto;
  box-sizing: border-box;
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

/* COMPACT HEADER - Reduced size */
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
  overflow: hidden;
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
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

.header-badge {
  background: rgba(77, 187, 152, 0.1);
  border: 2px solid rgba(77, 187, 152, 0.2);
  border-radius: 16px;
  padding: 0.75rem 1rem;
  backdrop-filter: blur(10px);
}

.badge-content {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.badge-text {
  font-size: 0.8rem;
  font-weight: 600;
  color: var(--text-accent);
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

/* COMPACT STATS GRID */
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

/* OPTIMIZED CONTENT GRID */
.content-grid {
  display: grid;
  grid-template-columns: 1.8fr 1fr;
  gap: 1.5rem;
  height: calc(100vh - 420px);
  min-height: 350px; /* Increased minimum height */
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

/* SCROLLABLE ASSESSMENT LIST */
.assessment-list {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
  flex: 1;
  overflow-y: auto;
  padding-right: 0.5rem;
  margin-right: -0.5rem;
}

/* Custom Scrollbar Styling */
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

/* SCROLLABLE QUICK LINKS */
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

/* Custom Scrollbar for Quick Links */
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
  min-height: 80px; /* Ensure consistent button height */
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

/* RESPONSIVE OPTIMIZATIONS */
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
  .home-container {
    padding: 0.75rem;
    height: auto;
  }
  
  .section-header-card {
    padding: 1.5rem;
    min-height: 100px;
  }
  
  .section-header-left {
    flex-direction: column;
    text-align: center;
    gap: 1rem;
  }
  
  .section-header-content {
    flex-direction: column;
    gap: 1.5rem;
  }
  
  .section-header-title {
    font-size: 1.5rem;
  }
  
  .quick-links-grid {
    grid-template-columns: 1fr;
  }
  
  .assessment-item {
    flex-direction: column;
    align-items: stretch;
    gap: 0.75rem;
  }
}
</style>