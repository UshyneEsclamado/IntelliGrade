<template>
  <div class="home-container">
    <!-- Welcome Header -->
    <div class="welcome-header">
      <div class="welcome-content">
        <h1 class="greeting">Hello, {{ studentName }}!</h1>
        <p class="welcome-message">
          Welcome to your student dashboard. Here you can view your subjects, assessments, grades, and track your academic progress.
        </p>
      </div>
      <div class="profile-avatar">
        <div class="avatar-circle">
          <svg width="32" height="32" viewBox="0 0 24 24" fill="currentColor">
            <path d="M12,4A4,4 0 0,1 16,8A4,4 0 0,1 12,12A4,4 0 0,1 8,8A4,4 0 0,1 12,4M12,14C16.42,14 20,15.79 20,18V20H4V18C4,15.79 7.58,14 12,14Z" />
          </svg>
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
export default {
  name: 'Home',
  data() {
    return {
      // This should be dynamically fetched from your authentication system
      studentName: 'Student Juan', // Replace with actual logged-in user name
      totalSubjects: 6,
      pendingAssessments: 4,
      recentAssessments: [
        {
          id: 1,
          title: 'Math Quiz 1',
          subject: 'Mathematics 101',
          dueDate: new Date('2024-09-20'),
          status: 'pending'
        },
        {
          id: 2,
          title: 'Essay Assignment',
          subject: 'English Literature',
          dueDate: new Date('2024-09-22'),
          status: 'in-progress'
        },
        {
          id: 3,
          title: 'Lab Report',
          subject: 'Chemistry 101',
          dueDate: new Date('2024-09-25'),
          status: 'pending'
        }
      ]
    };
  },
  methods: {
    formatDate(date) {
      return date.toLocaleDateString('en-US', {
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
    }
  },
  mounted() {
    // TODO: Fetch actual user data from your authentication system
    // Example:
    // this.fetchUserData();
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
}

.welcome-header {
  background: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(20px);
  border-radius: 24px;
  padding: 2.5rem;
  margin-bottom: 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  box-shadow: 0 8px 32px rgba(61, 141, 122, 0.1);
  border: 1px solid rgba(61, 141, 122, 0.1);
}

.greeting {
  font-size: 2.5rem;
  font-weight: 800;
  color: #3D8D7A;
  margin-bottom: 1rem;
  text-shadow: 0 2px 4px rgba(61, 141, 122, 0.1);
}

.welcome-message {
  font-size: 1.1rem;
  color: #666;
  line-height: 1.6;
  max-width: 600px;
}

.profile-avatar {
  flex-shrink: 0;
}

.avatar-circle {
  width: 80px;
  height: 80px;
  background: linear-gradient(135deg, #3D8D7A 0%, #A3D1C6 100%);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  box-shadow: 0 8px 32px rgba(61, 141, 122, 0.3);
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1.5rem;
  margin-bottom: 2rem;
}

.stat-card {
  background: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(20px);
  border-radius: 20px;
  padding: 2rem;
  display: flex;
  align-items: center;
  gap: 1.5rem;
  box-shadow: 0 8px 32px rgba(61, 141, 122, 0.1);
  border: 1px solid rgba(61, 141, 122, 0.1);
  transition: all 0.3s ease;
}

.stat-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 40px rgba(61, 141, 122, 0.15);
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
  color: #3D8D7A;
  line-height: 1;
}

.stat-label {
  font-size: 0.875rem;
  font-weight: 600;
  color: #777;
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
  background: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(20px);
  border-radius: 24px;
  padding: 2rem;
  box-shadow: 0 8px 32px rgba(61, 141, 122, 0.1);
  border: 1px solid rgba(61, 141, 122, 0.1);
}

.card-header {
  margin-bottom: 2rem;
}

.card-header h3 {
  font-size: 1.5rem;
  font-weight: 700;
  color: #3D8D7A;
  display: flex;
  align-items: center;
  gap: 0.75rem;
  margin-bottom: 0.5rem;
}

.card-subtitle {
  color: #666;
  font-size: 0.95rem;
}

.assessment-list {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.assessment-item {
  background: rgba(251, 255, 228, 0.5);
  border-radius: 16px;
  padding: 1.5rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  border: 1px solid rgba(61, 141, 122, 0.1);
  transition: all 0.3s ease;
}

.assessment-item:hover {
  background: rgba(251, 255, 228, 0.8);
  transform: translateX(4px);
}

.assessment-info h4 {
  font-weight: 600;
  color: #3D8D7A;
  margin-bottom: 0.25rem;
}

.assessment-subject {
  font-size: 0.875rem;
  color: #777;
}

.assessment-due {
  text-align: right;
}

.due-date {
  display: block;
  font-weight: 600;
  color: #3D8D7A;
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
  color: #3D8D7A;
}

.quick-links-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
}

.quick-link-btn {
  background: rgba(251, 255, 228, 0.5);
  border: 1px solid rgba(61, 141, 122, 0.1);
  border-radius: 16px;
  padding: 1.5rem 1rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.75rem;
  cursor: pointer;
  transition: all 0.3s ease;
  font-weight: 600;
  color: #3D8D7A;
  text-decoration: none;
}

.quick-link-btn:hover {
  background: rgba(61, 141, 122, 0.1);
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(61, 141, 122, 0.15);
}

@media (max-width: 768px) {
  .home-container {
    padding: 1rem;
  }
  
  .welcome-header {
    flex-direction: column;
    text-align: center;
    gap: 1.5rem;
    padding: 2rem;
  }
  
  .greeting {
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
}
</style>