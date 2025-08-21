<template>
  <div class="dashboard-container">
    <aside class="sidebar">
      <div class="user-info">
        <div class="profile-pic-placeholder">
          <svg width="48" height="48" viewBox="0 0 24 24" fill="currentColor">
            <path d="M12,4A4,4 0 0,1 16,8A4,4 0 0,1 12,12A4,4 0 0,1 8,8A4,4 0 0,1 12,4M12,14C16.42,14 20,15.79 20,18V20H4V18C4,15.79 7.58,14 12,14Z" />
          </svg>
        </div>
        <h3>{{ fullName }}</h3>
        <p class="role">Student</p>
      </div>

      <nav class="nav-links">
        <a href="#assessments" class="nav-item">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M15,16H19V18H15V16M15,8H19V10H15V8M15,12H19V14H15V12M13,3A2,2 0 0,1 15,5V19A2,2 0 0,1 13,21H5A2,2 0 0,1 3,19V5A2,2 0 0,1 5,3H13M14,19V5H5V19H14Z" /></svg>
          Assessments
        </a>
        <a href="#results" class="nav-item">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M16.5,12A2.5,2.5 0 0,1 14,9.5A2.5,2.5 0 0,1 16.5,7A2.5,2.5 0 0,1 19,9.5A2.5,2.5 0 0,1 16.5,12M11,10.25V9.75C11,8.78 10.22,8 9.25,8H7.75C6.78,8 6,8.78 6,9.75V10.25C6,11.22 6.78,12 7.75,12H9.25C10.22,12 11,11.22 11,10.25M17.5,18A2.5,2.5 0 0,1 15,15.5A2.5,2.5 0 0,1 17.5,13A2.5,2.5 0 0,1 20,15.5A2.5,2.5 0 0,1 17.5,18M8,15.5A2.5,2.5 0 0,1 5.5,13A2.5,2.5 0 0,1 8,10.5A2.5,2.5 0 0,1 10.5,13A2.5,2.5 0 0,1 8,15.5M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2M12,4A8,8 0 0,1 20,12A8,8 0 0,1 12,20A8,8 0 0,1 4,12A8,8 0 0,1 12,4Z" /></svg>
          Past Results
        </a>
        <a href="#chat" class="nav-item">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M20,2H4A2,2 0 0,0 2,4V22L6,18H20A2,2 0 0,0 22,16V4A2,2 0 0,0 20,2M6,9H18V11H6V9M14,14H6V12H14V14M18,8H6V6H18V8Z" /></svg>
          Teacher Chat
        </a>
        <button @click="openJoinClassModal" class="nav-item join-class-btn">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M19,13H13V19H11V13H5V11H11V5H13V11H19V13Z" /></svg>
          Join Class
        </button>
      </nav>
      <button @click="handleLogout" class="logout-btn">Logout</button>
    </aside>

    <main class="main-content">
      <div class="content-wrapper">
        <header class="dashboard-header">
          <h1>Hello, {{ fullName }}!</h1>
          <p>Welcome to your learning dashboard. Here you can take assessments, track your progress, and communicate with your teacher.</p>
        </header>
        
        <div class="sections-container">
          <section class="dashboard-section card">
            <div class="section-header">
              <h2>📝 Available Assessments</h2>
              <p class="section-subtitle">Take a quiz and get instant feedback.</p>
            </div>
            <div class="assessment-grid">
              <div v-if="assessments.length === 0" class="empty-state">
                <p>No new assessments available at the moment.</p>
              </div>
              <div v-for="assessment in assessments" :key="assessment.id" class="assessment-card">
                <h3>{{ assessment.title }}</h3>
                <p>Subject: {{ assessment.subject }}</p>
                <p>Questions: {{ assessment.questions }}</p>
                <button class="start-btn">Start Quiz</button>
              </div>
            </div>
          </section>

          <section class="dashboard-section card">
            <div class="section-header">
              <h2>📈 Past Results</h2>
              <p class="section-subtitle">View your historical scores and progress over time.</p>
            </div>
            <div class="results-container">
              <div class="results-table">
                <table>
                  <thead>
                    <tr>
                      <th>Quiz Name</th>
                      <th>Score</th>
                      <th>Date Taken</th>
                      <th>Feedback</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-if="pastResults.length === 0">
                      <td colspan="4" class="empty-state">No past results found.</td>
                    </tr>
                    <tr v-for="result in pastResults" :key="result.id">
                      <td>{{ result.quizName }}</td>
                      <td>{{ result.score }} / {{ result.totalQuestions }}</td>
                      <td>{{ result.date }}</td>
                      <td>
                        <span :class="{'feedback-positive': result.score >= result.totalQuestions * 0.7, 'feedback-negative': result.score < result.totalQuestions * 0.7}">
                          {{ result.score >= result.totalQuestions * 0.7 ? 'Great job!' : 'Needs improvement' }}
                        </span>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </section>
        </div>
      </div>
    </main>

    <div v-if="showJoinClassModal" class="modal-overlay" @click.self="closeJoinClassModal">
      <div class="modal-content">
        <h3>Join a Class</h3>
        <p>Enter the class code provided by your teacher to join.</p>
        <input type="text" v-model="classCode" placeholder="Enter class code" class="class-code-input">
        <div class="modal-actions">
          <button @click="joinClass" class="modal-btn join-btn">Join</button>
          <button @click="closeJoinClassModal" class="modal-btn cancel-btn">Cancel</button>
        </div>
        <p v-if="joinClassStatus" :class="{'success-message': joinClassStatus.startsWith('Successfully'), 'error-message': !joinClassStatus.startsWith('Successfully')}">{{ joinClassStatus }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import { supabase } from '../supabase';

export default {
  name: "StudentDashboard",
  data() {
    return {
      fullName: '',
      assessments: [],
      pastResults: [],
      showJoinClassModal: false,
      classCode: '',
      joinClassStatus: null,
    };
  },
  async created() {
    await this.fetchUserProfile();
    await this.fetchAssessments();
    await this.fetchPastResults();
  },
  methods: {
    async fetchUserProfile() {
      try {
        const { data: { user } } = await supabase.auth.getUser();
        if (!user) {
          throw new Error('User not authenticated.');
        }

        const { data: profile, error } = await supabase
          .from('profiles')
          .select('full_name')
          .eq('id', user.id)
          .single();

        if (error) throw error;
        this.fullName = profile.full_name;
      } catch (err) {
        console.error('Error fetching user profile:', err);
        this.$router.push('/login');
      }
    },
    async fetchAssessments() {
      this.assessments = [
        { id: 1, title: 'Math Quiz 1', subject: 'Algebra', questions: 10 },
        { id: 2, title: 'Science Exam', subject: 'Biology', questions: 25 },
      ];
    },
    async fetchPastResults() {
      this.pastResults = [
        { id: 1, quizName: 'English Quiz', score: 8, totalQuestions: 10, date: '2024-03-15' },
        { id: 2, quizName: 'History Test', score: 18, totalQuestions: 20, date: '2024-03-10' },
      ];
    },
    openJoinClassModal() {
      this.showJoinClassModal = true;
    },
    closeJoinClassModal() {
      this.showJoinClassModal = false;
      this.classCode = '';
      this.joinClassStatus = null;
    },
    async joinClass() {
      if (!this.classCode) {
        this.joinClassStatus = 'Please enter a class code.';
        return;
      }

      try {
        const { data: { user } } = await supabase.auth.getUser();
        if (!user) throw new Error('User not authenticated.');

        const { data: classData, error: classError } = await supabase
          .from('classes')
          .select('id')
          .eq('code', this.classCode)
          .single();

        if (classError || !classData) {
          throw new Error('Invalid or non-existent class code.');
        }

        const classId = classData.id;

        const { error: joinError } = await supabase
          .from('student_classes')
          .insert({
            student_id: user.id,
            class_id: classId,
          });

        if (joinError) throw joinError;

        this.joinClassStatus = 'Successfully joined the class!';
        await this.fetchAssessments();
      } catch (err) {
        console.error('Error joining class:', err);
        this.joinClassStatus = `Error: ${err.message}`;
      }
    },
    async handleLogout() {
      try {
        const { error } = await supabase.auth.signOut();
        if (error) throw error;
        this.$router.push('/login');
      } catch (err) {
        console.error('Logout error:', err);
      }
    }
  },
};
</script>

<style>
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

html, body {
  height: 100%;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
  background-color: #f6fbf4; /* A lighter, more subtle background */
}

#app {
  height: 100vh;
  overflow: hidden;
}
</style>

<style scoped>
.dashboard-container {
  display: flex;
  height: 100vh;
  width: 100vw;
  overflow: hidden;
}

/* Sidebar */
.sidebar {
  width: 280px;
  background-color: #fff;
  border-right: 1px solid #e0e6e0;
  display: flex;
  flex-direction: column;
  padding: 2.5rem 1.5rem;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.05);
}

.user-info {
  text-align: center;
  margin-bottom: 2.5rem;
  padding-bottom: 1.5rem;
  border-bottom: 1px solid #e0e6e0;
}

.profile-pic-placeholder {
  width: 64px;
  height: 64px;
  background-color: #A3D1C6;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 1rem;
  color: #3D8D7A;
}

.user-info h3 {
  font-size: 1.5rem;
  font-weight: 600;
  color: #3D8D7A;
  margin-bottom: 0.25rem;
}

.user-info .role {
  font-size: 0.875rem;
  color: #6c757d; /* A neutral gray for elegance */
}

.nav-links {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.nav-item {
  display: flex;
  align-items: center;
  padding: 0.75rem 1rem;
  border-radius: 8px;
  color: #3D8D7A;
  text-decoration: none;
  font-weight: 500;
  font-size: 0.875rem;
  transition: all 0.2s ease-in-out;
  background: none;
  border: none;
  cursor: pointer;
  width: 100%;
  text-align: left;
}

.nav-item svg {
  margin-right: 0.75rem;
  width: 20px;
  height: 20px;
  fill: #3D8D7A;
}

.nav-item:hover {
  background-color: #f1f7f0; /* A very light hover state */
  color: #3D8D7A;
}

.nav-item:hover svg {
  fill: #3D8D7A;
}

.join-class-btn {
  background-color: #B3D8A8;
  color: #3D8D7A;
  margin-top: 1rem;
  transition: background-color 0.2s ease-in-out;
}

.join-class-btn svg {
  fill: #3D8D7A;
}

.join-class-btn:hover {
  background-color: #A3D1C6;
}

.logout-btn {
  background-color: #3D8D7A;
  color: white;
  padding: 0.75rem 1.25rem;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  font-weight: 500;
  font-size: 0.875rem;
  transition: background-color 0.2s ease-in-out;
  margin-top: 1.5rem;
}

.logout-btn:hover {
  background-color: #A3D1C6;
}

/* Main Content */
.main-content {
  flex: 1;
  overflow: hidden;
  background-color: #f6fbf4;
}

.content-wrapper {
  height: 100vh;
  overflow-y: auto;
  padding: 2.5rem 3rem;
}

.dashboard-header {
  margin-bottom: 2rem;
}

.dashboard-header h1 {
  font-size: 2.5rem;
  font-weight: 700;
  color: #3D8D7A;
  margin-bottom: 0.5rem;
}

.dashboard-header p {
  color: #6c757d;
  font-size: 1rem;
  line-height: 1.5;
}

.sections-container {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2rem;
  max-width: 1200px;
}

.card {
  background-color: #fff;
  border-radius: 12px;
  padding: 1.5rem;
  border: 1px solid #e0e6e0;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
}

.section-header {
  margin-bottom: 1.5rem;
}

.section-header h2 {
  font-size: 1.5rem;
  font-weight: 600;
  color: #3D8D7A;
  margin-bottom: 0.25rem;
}

.section-subtitle {
  color: #6c757d;
  font-size: 0.875rem;
}

.assessment-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 1rem;
}

.assessment-card {
  border: 1px solid #e0e6e0;
  border-radius: 8px;
  padding: 1.25rem;
  background-color: #fff;
  transition: all 0.2s ease-in-out;
}

.assessment-card:hover {
  border-color: #A3D1C6;
  box-shadow: 0 4px 12px rgba(163, 209, 198, 0.25);
}

.assessment-card h3 {
  font-size: 1.125rem;
  color: #3D8D7A;
  margin-bottom: 0.5rem;
  font-weight: 600;
}

.assessment-card p {
  color: #6c757d;
  font-size: 0.875rem;
  margin-bottom: 0.25rem;
}

.start-btn {
  background-color: #B3D8A8;
  color: #3D8D7A;
  padding: 0.75rem 1rem;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  margin-top: 1rem;
  font-size: 0.875rem;
  font-weight: 500;
  transition: background-color 0.2s ease-in-out;
}

.start-btn:hover {
  background-color: #A3D1C6;
}

.results-container {
  overflow-x: auto;
}

.results-table table {
  width: 100%;
  border-collapse: collapse;
}

.results-table th,
.results-table td {
  padding: 0.75rem 1rem;
  text-align: left;
  border-bottom: 1px solid #e0e6e0;
  font-size: 0.875rem;
  color: #3D8D7A;
}

.results-table th {
  background-color: #f6fbf4;
  font-weight: 600;
  color: #3D8D7A;
}

.results-table tr:hover {
  background-color: #fcfdfb;
}

.feedback-positive {
  color: #3D8D7A;
  font-weight: 500;
}

.feedback-negative {
  color: #ef4444;
  font-weight: 500;
}

.empty-state {
  text-align: center;
  color: #6c757d;
  padding: 2rem 1.25rem;
  font-size: 0.875rem;
}

/* Modal */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.4);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
}

.modal-content {
  background: #fff;
  padding: 2rem;
  border-radius: 12px;
  width: 90%;
  max-width: 400px;
  text-align: center;
  box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
}

.modal-content h3 {
  font-size: 1.5rem;
  margin-bottom: 0.5rem;
  color: #3D8D7A;
  font-weight: 600;
}

.class-code-input {
  width: 100%;
  padding: 0.75rem;
  margin: 1.25rem 0;
  border: 1px solid #e0e6e0;
  border-radius: 8px;
  text-align: center;
  font-size: 1rem;
  transition: border-color 0.2s ease-in-out;
}

.class-code-input:focus {
  outline: none;
  border-color: #B3D8A8;
}

.modal-actions {
  display: flex;
  gap: 0.75rem;
  justify-content: center;
}

.modal-btn {
  padding: 0.625rem 1.25rem;
  border: none;
  border-radius: 8px;
  font-weight: 500;
  cursor: pointer;
  font-size: 0.875rem;
  transition: background-color 0.2s ease-in-out, transform 0.1s ease-in-out;
}

.modal-btn:active {
  transform: scale(0.98);
}

.join-btn {
  background-color: #B3D8A8;
  color: #3D8D7A;
}

.join-btn:hover {
  background-color: #A3D1C6;
}

.cancel-btn {
  background-color: #e0e6e0;
  color: #3d8d7a;
}

.cancel-btn:hover {
  background-color: #c9d2ce;
}

.success-message {
  color: #3D8D7A;
  font-weight: 500;
  margin-top: 1rem;
  font-size: 0.875rem;
}

.error-message {
  color: #ef4444;
  font-weight: 500;
  margin-top: 1rem;
  font-size: 0.875rem;
}

/* Responsive */
@media (max-width: 1024px) {
  .content-wrapper {
    padding: 1.5rem 2rem;
  }
  
  .sections-container {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 768px) {
  .dashboard-container {
    flex-direction: column;
  }
  
  .sidebar {
    width: 100%;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
    padding: 1rem 1.25rem;
    border-right: none;
    border-bottom: 1px solid #e0e6e0;
  }
  
  .user-info {
    flex-direction: row;
    align-items: center;
    gap: 0.75rem;
    text-align: left;
    margin-bottom: 0;
    padding-bottom: 0;
    border-bottom: none;
  }
  
  .profile-pic-placeholder {
    width: 40px;
    height: 40px;
    margin: 0;
  }
  
  .user-info h3 {
    font-size: 1rem;
  }
  
  .nav-links {
    display: none;
  }
  
  .logout-btn {
    margin-top: 0;
    padding: 0.5rem 1rem;
    font-size: 0.75rem;
  }
  
  .content-wrapper {
    padding: 1.25rem 1rem;
    height: calc(100vh - 72px);
  }
  
  .dashboard-header h1 {
    font-size: 1.5rem;
  }
  
  .sections-container {
    gap: 1.5rem;
  }
  
  .dashboard-section {
    padding: 1.25rem;
  }
}
</style>