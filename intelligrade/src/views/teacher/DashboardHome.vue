<template>
  <div class="page-container">
    <div class="main-wrapper">
      <div class="hero-header card-box">
        <div class="header-content">
          <div class="welcome-text">
            <h1>Hello, Teacher {{ fullName || 'Teacher' }}!</h1>
            <p>Welcome to your teaching dashboard. Here you can manage your classes, grade assessments, and track student progress.</p>
          </div>
        </div>
        <div class="user-avatar">
          <svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-user"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
        </div>
      </div>
      
      <section class="stat-cards">
        <div class="stat-card">
          <div class="stat-icon">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-users"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>
          </div>
          <div class="stat-info">
            <div class="stat-value">{{ totalClasses }}</div>
            <div class="stat-label">Total Classes</div>
          </div>
        </div>
        <div class="stat-card">
          <div class="stat-icon">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-check-circle"><path d="M22 11.08V12a10 10 0 1 1-5.93-8.66"></path><path d="M22 4L12 14.01l-3-3"></path></svg>
          </div>
          <div class="stat-info">
            <div class="stat-value">{{ gradedToday }}</div>
            <div class="stat-label">Graded Today</div>
          </div>
        </div>
        <div class="stat-card">
          <div class="stat-icon">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-clock"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
          </div>
          <div class="stat-info">
            <div class="stat-value">{{ pendingReviews }}</div>
            <div class="stat-label">Pending Reviews</div>
          </div>
        </div>
      </section>

      <div class="content-grid">
        <section id="assessments-to-grade" class="dashboard-section card-box">
          <div class="section-header">
            <h2>📝 Assessments to Grade</h2>
            <p class="section-subtitle">A list of assessments waiting for your attention.</p>
          </div>
          <div class="assessment-grid">
            <div v-if="assessmentsToGrade.length === 0" class="empty-state">
              <p>No new assessments to grade at the moment.</p>
            </div>
            <div v-for="assessment in assessmentsToGrade" :key="assessment.id" class="assessment-card">
              <div class="card-content">
                <div class="assessment-info">
                  <h3>{{ assessment.title }}</h3>
                  <p>Class: {{ assessment.className }}</p>
                  <p class="assessment-progress">
                    Submitted: {{ assessment.studentsSubmitted }} / {{ assessment.totalStudents }}
                  </p>
                </div>
                <button class="start-btn" @click="gradeAssessment(assessment)">Grade Assessment</button>
              </div>
            </div>
          </div>
        </section>
        
        <section id="quick-links" class="dashboard-section card-box">
          <div class="section-header">
            <h2>🚀 Quick Links</h2>
            <p class="section-subtitle">Navigate to key features quickly.</p>
          </div>
          <div class="link-grid">
            <router-link to="/teacher/classes" class="quick-link-card">
              <div class="card-glow"></div>
              <h3>My Classes</h3>
              <p>View, manage, and create classes.</p>
              <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-arrow-right"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
            </router-link>
            <div class="quick-link-card" @click="createQuiz">
              <div class="card-glow"></div>
              <h3>Create a Quiz</h3>
              <p>Design a new online quiz.</p>
              <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-arrow-right"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
            </div>
          </div>
        </section>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { supabase } from '@/supabase';
import { useRouter } from 'vue-router';

const router = useRouter();
const fullName = ref('');
const assessmentsToGrade = ref([]);
const totalClasses = ref(0);
const gradedToday = ref(0);
const pendingReviews = ref(0);

const fetchUserProfile = async () => {
  try {
    const { data: { user } } = await supabase.auth.getUser();
    if (!user) {
      router.push('/login');
      return;
    }
    
    const { data: profile, error } = await supabase
      .from('profiles')
      .select('full_name')
      .eq('id', user.id)
      .single();
    
    if (error) {
      throw error;
    }
    
    fullName.value = profile.full_name;
  } catch (err) {
    console.error('Error fetching user profile:', err);
    fullName.value = 'Teacher';
  }
};

const fetchAssessmentsToGrade = () => {
  // Sample data - replace with actual API call
  assessmentsToGrade.value = [
    { id: 1, title: 'Algebra Quiz 1', className: 'Math 101', studentsSubmitted: 15, totalStudents: 20 },
    { id: 2, title: 'Science Test 2', className: 'Science 101', studentsSubmitted: 22, totalStudents: 25 },
  ];
};

const fetchDashboardStats = () => {
  // Sample data - replace with actual API calls
  totalClasses.value = 3;
  gradedToday.value = 5;
  pendingReviews.value = 8;
};

const gradeAssessment = (assessment) => {
  console.log('Grading assessment:', assessment.title);
  // Add navigation to grading interface
};

const createQuiz = () => {
  console.log('Navigating to quiz creation...');
  // Navigate to the MyClasses page, from which the user can select a class to create a quiz in.
  router.push({ name: 'MyClasses' });
};

onMounted(() => {
  fetchUserProfile();
  fetchAssessmentsToGrade();
  fetchDashboardStats();
});
</script>

<style scoped>
/*
 * Imported fonts
 */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

/* Main Layout & Background */
.page-container {
  padding: 2rem;
  font-family: 'Inter', sans-serif;
  background: linear-gradient(135deg, #FBFFE4 0%, #B3D8A8 50%, #A3D1C6 100%);
  min-height: 100%;
  position: relative;
  overflow-x: hidden;
}

.page-container::before {
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

.main-wrapper {
  max-width: 1400px;
  margin: 0 auto;
}

/* Hero Header Section */
.hero-header {
  background: rgba(255, 255, 255, 0.85);
  backdrop-filter: blur(20px);
  border: 1px solid rgba(61, 141, 122, 0.1);
  border-radius: 24px;
  padding: 2.5rem;
  margin-bottom: 2rem;
  box-shadow: 
    0 8px 32px rgba(61, 141, 122, 0.1),
    0 0 0 1px rgba(255, 255, 255, 0.2);
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 2rem;
}

.welcome-text h1 {
  font-size: 2.5rem;
  font-weight: 800;
  color: #3D8D7A;
  margin-bottom: 0.5rem;
  margin: 0 0 0.5rem 0;
}

.welcome-text p {
  font-size: 1.1rem;
  color: #666;
  font-weight: 500;
  margin: 0;
}

.user-avatar {
  background: linear-gradient(135deg, #3D8D7A 0%, #A3D1C6 100%);
  border-radius: 50%;
  width: 80px;
  height: 80px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  box-shadow: 0 8px 32px rgba(61, 141, 122, 0.3);
}

.user-avatar svg {
  color: #fff;
  width: 40px;
  height: 40px;
}

/* Stat Cards */
.stat-cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 2rem;
  margin-bottom: 2rem;
}

.stat-card {
  background: linear-gradient(135deg, rgba(251, 255, 228, 0.8) 0%, rgba(179, 216, 168, 0.5) 100%);
  backdrop-filter: blur(15px);
  border: 1px solid rgba(61, 141, 122, 0.15);
  border-radius: 20px;
  padding: 2rem;
  display: flex;
  align-items: center;
  gap: 1.5rem;
  box-shadow: 0 4px 16px rgba(61, 141, 122, 0.1);
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.stat-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 12px 24px rgba(61, 141, 122, 0.2);
  border-color: rgba(61, 141, 122, 0.25);
}

.stat-icon {
  width: 56px;
  height: 56px;
  background: linear-gradient(135deg, #3D8D7A 0%, #A3D1C6 100%);
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  box-shadow: 0 4px 16px rgba(61, 141, 122, 0.3);
}

.stat-icon svg {
  color: white;
}

.stat-value {
  font-size: 2.25rem;
  font-weight: 800;
  color: #3D8D7A;
  text-shadow: 0 2px 4px rgba(61, 141, 122, 0.1);
  margin: 0;
}

.stat-label {
  font-size: 0.9rem;
  color: #666;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin: 0;
}

/* Main Content Grid */
.content-grid {
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: 2rem;
}

/* Reusable Components */
.dashboard-section {
  background: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(20px);
  border: 1px solid rgba(61, 141, 122, 0.1);
  border-radius: 24px;
  padding: 2.5rem;
  box-shadow: 
    0 8px 32px rgba(61, 141, 122, 0.1),
    0 0 0 1px rgba(255, 255, 255, 0.2);
}

.section-header h2 {
  font-size: 1.8rem;
  font-weight: 700;
  color: #3D8D7A;
  margin-bottom: 0.5rem;
  text-shadow: 0 1px 2px rgba(61, 141, 122, 0.1);
  margin: 0 0 0.5rem 0;
}

.section-subtitle {
  color: #777;
  font-size: 1rem;
  font-weight: 500;
  margin-bottom: 1.5rem;
  margin: 0 0 1.5rem 0;
}

/* Assessment Grid */
.assessment-grid {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.assessment-card {
  background: rgba(251, 255, 228, 0.7);
  border: 1px solid rgba(61, 141, 122, 0.15);
  border-radius: 20px;
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  position: relative;
  overflow: hidden;
  box-shadow: 0 4px 16px rgba(61, 141, 122, 0.1);
}

.assessment-card:hover {
  transform: translateY(-8px) scale(1.01);
  box-shadow: 0 20px 40px rgba(61, 141, 122, 0.2);
  border-color: rgba(61, 141, 122, 0.3);
}

.assessment-card .card-content {
  padding: 2rem;
  position: relative;
  z-index: 1;
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 1.5rem;
}

.assessment-info h3 {
  font-size: 1.4rem;
  font-weight: 700;
  color: #3D8D7A;
  margin-bottom: 0.5rem;
  margin: 0 0 0.5rem 0;
}

.assessment-info p {
  color: #777;
  font-size: 0.95rem;
  margin: 0.25rem 0;
}

.assessment-progress {
  font-weight: 600 !important;
  color: #3D8D7A !important;
}

.start-btn {
  background: linear-gradient(135deg, #3D8D7A 0%, #A3D1C6 100%);
  color: #fff;
  border: none;
  padding: 1rem 2rem;
  border-radius: 16px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  display: flex;
  align-items: center;
  gap: 0.75rem;
  box-shadow: 0 8px 32px rgba(61, 141, 122, 0.2);
  position: relative;
  overflow: hidden;
  white-space: nowrap;
}

.start-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 16px 48px rgba(61, 141, 122, 0.3);
}

.empty-state {
  text-align: center;
  color: #888;
  padding: 2rem;
  font-style: italic;
  font-weight: 500;
}

.empty-state p {
  margin: 0;
}

/* Quick Links Grid */
.link-grid {
  display: grid;
  gap: 1.5rem;
}

.quick-link-card {
  background: rgba(251, 255, 228, 0.7);
  border: 1px solid rgba(61, 141, 122, 0.15);
  border-radius: 20px;
  padding: 1.5rem;
  text-decoration: none;
  color: #3D8D7A;
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  position: relative;
  overflow: hidden;
  box-shadow: 0 4px 16px rgba(61, 141, 122, 0.1);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  cursor: pointer;
  min-height: 120px;
}

.quick-link-card h3 {
  font-size: 1.2rem;
  font-weight: 700;
  margin-bottom: 0.25rem;
  color: #3D8D7A;
  margin: 0 0 0.25rem 0;
}

.quick-link-card p {
  font-size: 0.9rem;
  color: #777;
  margin: 0;
  flex-grow: 1;
}

.quick-link-card:hover {
  transform: translateY(-8px) scale(1.02);
  box-shadow: 0 20px 40px rgba(61, 141, 122, 0.2);
  border-color: rgba(61, 141, 122, 0.3);
  text-decoration: none;
  color: #3D8D7A;
}

.quick-link-card svg {
  position: absolute;
  bottom: 1.5rem;
  right: 1.5rem;
  color: #A3D1C6;
  transition: all 0.3s ease;
}

.quick-link-card:hover svg {
  color: #3D8D7A;
  transform: translateX(4px);
}

.card-glow {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(135deg, rgba(179, 216, 168, 0.2) 0%, rgba(163, 209, 198, 0.15) 100%);
  opacity: 0;
  transition: opacity 0.3s ease;
  z-index: 0;
}

.quick-link-card:hover .card-glow {
  opacity: 1;
}

/* Responsive Styles */
@media (max-width: 1024px) {
  .content-grid {
    grid-template-columns: 1fr;
  }
  
  .stat-cards {
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  }
}

@media (max-width: 768px) {
  .page-container {
    padding: 1rem;
  }
  
  .hero-header {
    flex-direction: column;
    text-align: center;
    padding: 2rem;
    gap: 1.5rem;
  }
  
  .welcome-text h1 {
    font-size: 2rem;
  }
  
  .stat-card {
    padding: 1.5rem;
  }
  
  .dashboard-section {
    padding: 1.5rem;
  }
  
  .assessment-card .card-content {
    flex-direction: column;
    align-items: flex-start;
    gap: 1rem;
  }
  
  .start-btn {
    align-self: stretch;
    justify-content: center;
  }
}

@media (max-width: 480px) {
  .page-container {
    padding: 0.5rem;
  }
  
  .hero-header {
    padding: 1.5rem;
  }
  
  .welcome-text h1 {
    font-size: 1.75rem;
  }
  
  .stat-card {
    padding: 1.5rem;
  }
  
  .dashboard-section {
    padding: 1rem;
  }
}
</style>