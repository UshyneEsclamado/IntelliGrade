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
        <a href="#" @click.prevent="currentView = 'home'" :class="['nav-item', { 'is-active': currentView === 'home' }]">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M10,20V14H14V20H19V12H22L12,3L2,12H5V20H10Z" /></svg>
          <span>Home</span>
        </a>
        <a href="#" @click.prevent="currentView = 'subjects'" :class="['nav-item', { 'is-active': currentView.includes('subjects') }]">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M3,5.5V18.5A2.5,2.5 0 0,0 5.5,21A2.5,2.5 0 0,0 8,18.5V5.5A2.5,2.5 0 0,0 5.5,3A2.5,2.5 0 0,0 3,5.5M12,5.5V18.5A2.5,2.5 0 0,0 14.5,21A2.5,2.5 0 0,0 17,18.5V5.5A2.5,2.5 0 0,0 14.5,3A2.5,2.5 0 0,0 12,5.5M21,5.5V18.5A2.5,2.5 0 0,0 23.5,21A2.5,2.5 0 0,0 26,18.5V5.5A2.5,2.5 0 0,0 23.5,3A2.5,2.5 0 0,0 21,5.5Z" /></svg>
          <span>Subjects</span>
        </a>
        <a href="#" @click.prevent="currentView = 'calendar'" :class="['nav-item', { 'is-active': currentView === 'calendar' }]">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M19,19H5V8H19M19,3H18V1H16V3H8V1H6V3H5C3.89,3 3,3.89 3,5V19A2,2 0 0,0 5,21H19A2,2 0 0,0 21,19V5C21,3.89 20.1,3 19,3M16.5,13.5H11V18.5H16.5V13.5Z" /></svg>
          <span>Calendar</span>
        </a>
        <a href="#" @click.prevent="currentView = 'messages'" :class="['nav-item', { 'is-active': currentView === 'messages' }]">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M20,2H4A2,2 0 0,0 2,4V22L6,18H20A2,2 0 0,0 22,16V4A2,2 0 0,0 20,2M6,9H18V11H6V9M14,14H6V12H14V14M18,8H6V6H18V8Z" /></svg>
          <span>Messages</span>
        </a>
        <a href="#" @click.prevent="currentView = 'settings'" :class="['nav-item', { 'is-active': currentView === 'settings' }]">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M12,15.5A3.5,3.5 0 0,1 8.5,12A3.5,3.5 0 0,1 12,8.5A3.5,3.5 0 0,1 15.5,12A3.5,3.5 0 0,1 12,15.5M19.43,12.97C19.47,12.65 19.5,12.33 19.5,12C19.5,11.67 19.47,11.34 19.43,11.03L21.54,9.37C21.73,9.22 21.78,8.96 21.66,8.74L19.65,5.27C19.54,5.05 19.27,4.96 19.05,5.05L16.56,6.05C16.04,5.66 15.5,5.32 14.9,5.07L14.5,2.42C14.46,2.18 14.25,2 14,2H10C9.75,2 9.54,2.18 9.5,2.42L9.1,5.07C8.5,5.32 7.96,5.66 7.44,6.05L4.95,5.05C4.73,4.96 4.46,5.05 4.34,5.27L2.34,8.74C2.21,8.96 2.27,9.22 2.46,9.37L4.57,11.03C4.53,11.34 4.5,11.67 4.5,12C4.5,12.33 4.53,12.65 4.57,12.97L2.46,14.63C2.27,14.78 2.21,15.04 2.34,15.26L4.34,18.73C4.46,18.95 4.73,19.04 4.95,18.95L7.44,17.94C7.96,18.34 8.5,18.68 9.1,18.93L9.5,21.58C9.54,21.82 9.75,22 10,22H14C14.25,22 14.46,21.82 14.5,21.58L14.9,18.93C15.5,18.68 16.04,18.34 16.56,17.94L19.05,18.95C19.27,19.04 19.54,18.95 19.66,18.73L21.66,15.26C21.78,15.04 21.73,14.78 21.54,14.63L19.43,12.97Z" /></svg>
          <span>Settings</span>
        </a>
      </nav>

      <button @click="handleLogout" class="logout-btn">
        <span>Logout</span>
      </button>
    </aside>

    <main class="main-content">
      <div class="content-wrapper">
        <header class="dashboard-header">
          <h1>Hello, {{ fullName }}! 👋</h1>
          <p>Welcome to your learning dashboard. Here you can take assessments, track your progress, and communicate with your teacher.</p>
        </header>

        <section v-show="currentView === 'home'" class="dashboard-section card" id="home">
          <div class="section-header">
            <h2>🏠 Dashboard Overview</h2>
            <p class="section-subtitle">A quick glance at your most important information.</p>
          </div>
          <div class="overview-grid">
            <div class="overview-item">
              <h3>📝 Upcoming Assessments</h3>
              <p>You have **{{ upcomingAssessments.length }}** assessments due soon.</p>
              <a href="#" @click.prevent="showSubjectsAndAssessments" class="link-btn">View All →</a>
            </div>
            <div class="overview-item">
              <h3>🗓️ Next Due Date</h3>
              <p v-if="nextDueDate">Your next assignment is due on **{{ nextDueDate.date }}**.</p>
              <p v-else>No upcoming due dates.</p>
              <a href="#" @click.prevent="currentView = 'calendar'" class="link-btn">Open Calendar →</a>
            </div>
          </div>
        </section>

        <section v-show="currentView === 'subjects'" class="dashboard-section card" id="subjects">
          <div class="section-header">
            <h2>📚 My Subjects</h2>
            <p class="section-subtitle">Access your class materials and assessments.</p>
          </div>
          <button @click="openJoinClassModal" class="join-class-btn-subjects">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M19,13H13V19H11V13H5V11H11V5H13V11H19V13Z" /></svg>
            <span>Join Class</span>
          </button>
          <div class="subject-grid">
            <div v-if="subjects.length === 0" class="empty-state">
              <p>You are not enrolled in any subjects yet.</p>
            </div>
            <div v-for="subject in subjects" :key="subject.id" class="subject-card" @click="showSubjectDetails(subject)">
              <h3>{{ subject.name }}</h3>
              <p>Teacher: {{ subject.teacher }}</p>
              <button class="view-btn">View Assessments</button>
            </div>
          </div>
        </section>

        <section v-if="currentView === 'subject-details'" class="dashboard-section card" id="subject-details">
          <button @click="currentView = 'subjects'" class="back-btn">← Back to Subjects</button>
          <div class="section-header">
            <h2>{{ selectedSubject.name }} Assessments</h2>
            <p class="section-subtitle">Teacher: {{ selectedSubject.teacher }}</p>
          </div>
          
          <div class="assessments-container">
            <div class="assessment-section">
              <h3>📝 Upcoming Assessments</h3>
              <div class="assessment-grid">
                <div v-if="upcomingAssessmentsForSubject.length === 0" class="empty-state">
                  <p>No upcoming assessments for this subject.</p>
                </div>
                <div v-for="assessment in upcomingAssessmentsForSubject" :key="assessment.id" class="assessment-card">
                  <h3>{{ assessment.title }}</h3>
                  <p>Questions: {{ assessment.questions }}</p>
                  <p>Due Date: **{{ assessment.date }}**</p>
                  <button class="start-btn">Start Quiz</button>
                </div>
              </div>
            </div>

            <div class="assessment-section">
              <h3>✅ Past Assessments</h3>
              <div class="assessment-grid">
                <div v-if="pastAssessmentsForSubject.length === 0" class="empty-state">
                  <p>No past assessments for this subject.</p>
                </div>
                <div v-for="assessment in pastAssessmentsForSubject" :key="assessment.id" class="assessment-card past-assessment">
                  <h3>{{ assessment.title }}</h3>
                  <p>Questions: {{ assessment.questions }}</p>
                  <p>Completed: **{{ assessment.date }}**</p>
                  <button class="view-result-btn">View Result</button>
                </div>
              </div>
            </div>
          </div>

        </section>

        <section v-show="currentView === 'calendar'" class="dashboard-section card" id="calendar">
          <div class="section-header">
            <h2>🗓️ Upcoming Deadlines</h2>
            <p class="section-subtitle">Stay on track with your academic schedule.</p>
          </div>
          <div class="calendar-view">
            <div v-if="calendarEvents.length === 0" class="empty-state">
              <p>No upcoming events or deadlines.</p>
            </div>
            <ul class="event-list">
              <li v-for="event in calendarEvents" :key="event.id" class="event-item">
                <div class="event-icon">📅</div>
                <div class="event-details">
                  <span class="event-title">{{ event.title }}</span>
                  <span class="event-date">{{ event.date }}</span>
                </div>
              </li>
            </ul>
          </div>
        </section>

        <section v-show="currentView === 'messages'" class="dashboard-section card" id="messages">
          <div class="section-header">
            <h2>📬 Messages & Notifications</h2>
            <p class="section-subtitle">View communications from your teachers.</p>
          </div>
          <div class="messages-container">
            <div v-if="messages.length === 0" class="empty-state">
              <p>You have no new messages.</p>
            </div>
            <ul class="message-list">
              <li v-for="message in messages" :key="message.id" class="message-item">
                <div class="message-sender">{{ message.sender }}</div>
                <div class="message-content">
                  <p>{{ message.content }}</p>
                  <span class="message-date">{{ message.date }}</span>
                </div>
              </li>
            </ul>
          </div>
        </section>

        <section v-show="currentView === 'settings'" class="dashboard-section card" id="settings">
          <div class="section-header">
            <h2>⚙️ Settings</h2>
            <p class="section-subtitle">Manage your account and preferences.</p>
          </div>
          <div class="settings-container">
            <div class="setting-item">
              <h3>Profile Information</h3>
              <p>Update your name and profile picture.</p>
              <button class="settings-btn">Edit Profile</button>
            </div>
            <div class="setting-item">
              <h3>Account Security</h3>
              <p>Change your password or manage linked accounts.</p>
              <button class="settings-btn">Security Settings</button>
            </div>
          </div>
        </section>
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
      currentView: 'home',
      selectedSubject: null,
      assessments: [],
      pastResults: [],
      upcomingAssessments: [],
      calendarEvents: [],
      messages: [],
      subjects: [],
      showJoinClassModal: false,
      classCode: '',
      joinClassStatus: null,
    };
  },
  computed: {
    upcomingAssessmentsForSubject() {
      if (!this.selectedSubject) return [];
      const today = new Date();
      return this.assessments
        .filter(assessment => assessment.subjectId === this.selectedSubject.id && new Date(assessment.date) >= today)
        .sort((a, b) => new Date(a.date) - new Date(b.date));
    },
    pastAssessmentsForSubject() {
      if (!this.selectedSubject) return [];
      const today = new Date();
      return this.assessments
        .filter(assessment => assessment.subjectId === this.selectedSubject.id && new Date(assessment.date) < today)
        .sort((a, b) => new Date(b.date) - new Date(a.date));
    },
    nextDueDate() {
      return this.calendarEvents.length > 0 ? this.calendarEvents[0] : null;
    }
  },
  async created() {
    await this.fetchUserProfile();
    await this.fetchSubjects();
    await this.fetchAssessments();
    await this.fetchUpcomingAssessments();
    await this.fetchCalendarEvents();
    await this.fetchMessages();
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
    async fetchSubjects() {
      this.subjects = [
        { id: 1, name: 'Algebra II', teacher: 'Ms. Rodriguez' },
        { id: 2, name: 'World History', teacher: 'Mr. Smith' },
        { id: 3, name: 'Biology', teacher: 'Mr. Brown' },
      ];
    },
    async fetchAssessments() {
      const today = new Date().toISOString().slice(0, 10);
      this.assessments = [
        { id: 1, title: 'Math Quiz 1', subjectId: 1, questions: 10, date: today }, // Mock a "past" assessment
        { id: 2, title: 'Science Exam', subjectId: 3, questions: 25, date: '2025-09-12' },
        { id: 3, title: 'Chapter 5 Test', subjectId: 1, questions: 20, date: '2025-09-15' },
        { id: 4, title: 'History Essay', subjectId: 2, questions: 1, date: '2025-08-20' }, // Mock a "past" assessment
        { id: 5, title: 'Chapter 1 Quiz', subjectId: 3, questions: 15, date: '2025-09-22' },
        { id: 6, title: 'Finals Exam', subjectId: 1, questions: 50, date: '2025-09-28' },
      ];
    },
    async fetchUpcomingAssessments() {
      const today = new Date();
      this.upcomingAssessments = this.assessments
        .filter(a => new Date(a.date) >= today)
        .sort((a, b) => new Date(a.date) - new Date(b.date))
        .slice(0, 2);
    },
    async fetchCalendarEvents() {
      this.calendarEvents = this.assessments
        .filter(a => new Date(a.date) >= new Date()) // Only include upcoming events
        .map(a => ({
          id: a.id,
          title: a.title + ' due',
          date: a.date
        }))
        .sort((a, b) => new Date(a.date) - new Date(b.date));
    },
    async fetchMessages() {
      this.messages = [
        { id: 1, sender: 'Ms. Rodriguez', content: 'Reminder: The Math Quiz 1 is on Friday. Good luck!', date: '2025-09-02' },
        { id: 2, sender: 'Mr. Brown', content: 'The Biology exam study guide is now available in the class materials.', date: '2025-09-08' },
        { id: 3, sender: 'Mr. Smith', content: 'I have posted the instructions for the History Essay. Let me know if you have questions.', date: '2025-09-18' },
      ];
    },
    showSubjectDetails(subject) {
      this.selectedSubject = subject;
      this.currentView = 'subject-details';
    },
    showSubjectsAndAssessments() {
      this.currentView = 'subjects';
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
          .insert({ student_id: user.id, class_id: classId });
        if (joinError) throw joinError;
        this.joinClassStatus = 'Successfully joined the class!';
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

<style scoped>
/* All CSS styles are the same as the previous response */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

.dashboard-container {
  display: flex;
  height: 100vh;
  width: 100vw;
  margin: 0;
  padding: 0;
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  font-family: 'Inter', sans-serif;
  background: linear-gradient(135deg, #FBFFE4 0%, #B3D8A8 50%, #A3D1C6 100%);
  overflow: hidden;
}

.dashboard-container::before {
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
  z-index: 0;
  pointer-events: none;
}

.sidebar {
  width: 300px;
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(20px);
  border-right: 1px solid rgba(61, 141, 122, 0.1);
  display: flex;
  flex-direction: column;
  padding: 2.5rem 1.5rem;
  box-shadow: 
    0 8px 32px rgba(61, 141, 122, 0.1),
    0 0 0 1px rgba(255, 255, 255, 0.2);
  overflow-y: auto;
  flex-shrink: 0;
  position: relative;
  z-index: 1;
}

.user-info {
  text-align: center;
  margin-bottom: 2.5rem;
  padding: 2rem 1.5rem;
  background: rgba(251, 255, 228, 0.3);
  border-radius: 20px;
  border: 1px solid rgba(61, 141, 122, 0.15);
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.user-info:hover {
  box-shadow: 0 8px 32px rgba(61, 141, 122, 0.2);
  transform: translateY(-2px);
}

.profile-pic-placeholder {
  width: 80px;
  height: 80px;
  background: linear-gradient(135deg, #3D8D7A 0%, #A3D1C6 100%);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 1rem;
  color: white;
  box-shadow: 0 8px 32px rgba(61, 141, 122, 0.3);
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.profile-pic-placeholder:hover {
  transform: scale(1.05);
  box-shadow: 0 12px 40px rgba(61, 141, 122, 0.4);
}

.profile-pic-placeholder svg {
  width: 48px;
  height: 48px;
}

.user-info h3 {
  font-size: 1.5rem;
  font-weight: 700;
  color: #3D8D7A;
  margin-bottom: 0.5rem;
  text-shadow: 0 1px 2px rgba(61, 141, 122, 0.1);
}

.user-info .role {
  font-size: 0.875rem;
  color: #777;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  background: rgba(61, 141, 122, 0.1);
  padding: 0.25rem 0.75rem;
  border-radius: 12px;
  display: inline-block;
}

.nav-links {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.nav-item {
  display: flex;
  align-items: center;
  padding: 1rem 1.25rem;
  border-radius: 16px;
  color: #3D8D7A;
  text-decoration: none;
  font-weight: 600;
  font-size: 0.95rem;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  background: rgba(251, 255, 228, 0.5);
  border: 1px solid rgba(61, 141, 122, 0.1);
  cursor: pointer;
  width: 100%;
  text-align: left;
  position: relative;
  overflow: hidden;
}

.nav-item::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(135deg, rgba(179, 216, 168, 0.3) 0%, rgba(163, 209, 198, 0.2) 100%);
  transition: left 0.3s ease;
  z-index: 0;
}

.nav-item.is-active::before {
    left: 0;
}

.nav-item svg {
  margin-right: 1rem;
  width: 22px;
  height: 22px;
  fill: #3D8D7A;
  transition: all 0.3s ease;
  position: relative;
  z-index: 1;
}

.nav-item span {
  position: relative;
  z-index: 1;
}

.nav-item:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(61, 141, 122, 0.15);
  border-color: rgba(61, 141, 122, 0.2);
}

.nav-item:hover::before {
  left: 0;
}

.nav-item:hover svg {
  transform: scale(1.1);
}

.logout-btn {
  background: linear-gradient(135deg, #3D8D7A 0%, #A3D1C6 100%);
  color: white;
  padding: 1rem 1.5rem;
  border: none;
  border-radius: 16px;
  cursor: pointer;
  font-weight: 600;
  font-size: 0.95rem;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  margin-top: 1.5rem;
  box-shadow: 0 8px 32px rgba(61, 141, 122, 0.2);
  position: relative;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
  line-height: 1;
  width: 100%;
}

.logout-btn::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(135deg, #A3D1C6 0%, #3D8D7A 100%);
  transition: left 0.3s ease;
  z-index: 0;
}

.logout-btn span {
  position: relative;
  z-index: 1;
  display: inline-block;
}

.logout-btn:hover {
  transform: translateY(-3px);
  box-shadow: 0 16px 48px rgba(61, 141, 122, 0.3);
}

.logout-btn:hover::before {
  left: 0;
}

.main-content {
  flex: 1;
  overflow: hidden;
  background: transparent;
  min-width: 0;
  position: relative;
  z-index: 1;
}

.content-wrapper {
  height: 100vh;
  overflow-y: auto;
  padding: 2.5rem 3rem;
}

.dashboard-header {
  margin-bottom: 2rem;
  color: #3D8D7A;
}

.dashboard-header h1 {
  font-size: 2.5rem;
  font-weight: 800;
  margin-bottom: 0.5rem;
  text-shadow: 0 2px 4px rgba(61, 141, 122, 0.2);
}

.dashboard-header p {
  color: #6c757d;
  font-size: 1rem;
  line-height: 1.6;
}

.dashboard-section {
  display: none;
}

.dashboard-section.card {
  display: block;
  background: rgba(255, 255, 255, 0.8);
  backdrop-filter: blur(10px);
  border-radius: 20px;
  padding: 2rem;
  border: 1px solid rgba(61, 141, 122, 0.15);
  box-shadow: 0 8px 32px rgba(61, 141, 122, 0.1);
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  min-height: 500px;
}

.dashboard-section.card:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 40px rgba(61, 141, 122, 0.2);
}

.section-header {
  margin-bottom: 1.5rem;
}

.section-header h2 {
  font-size: 1.5rem;
  font-weight: 700;
  color: #3D8D7A;
  margin-bottom: 0.25rem;
}

.section-subtitle {
  color: #777;
  font-size: 0.875rem;
  font-weight: 500;
}

/* Home Section */
.overview-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
}

.overview-item {
  background: rgba(179, 216, 168, 0.2);
  border: 1px solid rgba(179, 216, 168, 0.4);
  padding: 1.5rem;
  border-radius: 16px;
  transition: all 0.3s ease;
}

.overview-item:hover {
  background: rgba(179, 216, 168, 0.4);
  transform: translateY(-2px);
}

.overview-item h3 {
  font-size: 1.25rem;
  color: #3D8D7A;
  margin-bottom: 0.5rem;
}

.overview-item p {
  color: #555;
  font-weight: 500;
}

.link-btn {
  display: inline-block;
  margin-top: 1rem;
  color: #3D8D7A;
  font-weight: 600;
  font-size: 0.9rem;
  text-decoration: none;
  transition: all 0.3s ease;
}

.link-btn:hover {
  transform: translateX(5px);
  text-decoration: underline;
}

/* Assessments */
.assessments-container {
    display: flex;
    flex-direction: column;
    gap: 2rem;
}

.assessment-section h3 {
    font-size: 1.25rem;
    font-weight: 700;
    color: #3D8D7A;
    margin-bottom: 1rem;
}

.assessment-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 1.5rem;
}

.assessment-card {
  border: 1px solid rgba(61, 141, 122, 0.1);
  border-radius: 16px;
  padding: 1.5rem;
  background: rgba(251, 255, 228, 0.5);
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.assessment-card:hover {
  background: rgba(251, 255, 228, 0.8);
  transform: translateY(-2px);
  box-shadow: 0 4px 16px rgba(163, 209, 198, 0.25);
  border-color: rgba(61, 141, 122, 0.2);
}

.assessment-card h3 {
  font-size: 1.125rem;
  color: #3D8D7A;
  margin-bottom: 0.5rem;
  font-weight: 700;
}

.assessment-card p {
  color: #6c757d;
  font-size: 0.875rem;
  margin-bottom: 0.25rem;
}

.start-btn {
  background: linear-gradient(135deg, #B3D8A8 0%, #A3D1C6 100%);
  color: #3D8D7A;
  padding: 0.75rem 1.25rem;
  border: none;
  border-radius: 12px;
  cursor: pointer;
  margin-top: 1rem;
  font-size: 0.875rem;
  font-weight: 600;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  box-shadow: 0 4px 12px rgba(163, 209, 198, 0.3);
}

.start-btn:hover {
  transform: translateY(-1px);
  box-shadow: 0 6px 16px rgba(163, 209, 198, 0.5);
}

.view-result-btn {
  background: #fff;
  color: #3D8D7A;
  border: 1px solid #3D8D7A;
  padding: 0.75rem 1.25rem;
  border-radius: 12px;
  cursor: pointer;
  margin-top: 1rem;
  font-size: 0.875rem;
  font-weight: 600;
  transition: all 0.3s ease;
}

.view-result-btn:hover {
  background: #3D8D7A;
  color: #fff;
}

/* Calendar */
.calendar-view {
  min-height: 200px;
}

.event-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.event-item {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 0.75rem 1rem;
  border-bottom: 1px solid rgba(61, 141, 122, 0.1);
  transition: background-color 0.3s ease;
}

.event-item:hover {
  background-color: rgba(61, 141, 122, 0.05);
}

.event-icon {
  font-size: 1.5rem;
  line-height: 1;
}

.event-details {
  flex: 1;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.event-title {
  font-weight: 600;
  color: #3D8D7A;
}

.event-date {
  font-size: 0.8rem;
  color: #777;
}

/* Messages */
.messages-container {
  min-height: 200px;
}

.message-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.message-item {
  border-bottom: 1px solid rgba(61, 141, 122, 0.1);
  padding: 1rem 0;
}

.message-item:last-child {
  border-bottom: none;
}

.message-sender {
  font-weight: 700;
  color: #3D8D7A;
  margin-bottom: 0.25rem;
}

.message-content {
  font-size: 0.9rem;
  color: #555;
}

.message-date {
  font-size: 0.75rem;
  color: #999;
  display: block;
  margin-top: 0.25rem;
}

/* Subjects */
.join-class-btn-subjects {
  background: linear-gradient(135deg, #B3D8A8 0%, #A3D1C6 100%);
  color: #3D8D7A;
  border: none;
  border-radius: 12px;
  font-weight: 700;
  box-shadow: 0 4px 16px rgba(163, 209, 198, 0.5);
  width: 200px;
  padding: 0.75rem 1.25rem;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  cursor: pointer;
  margin-bottom: 2rem;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.join-class-btn-subjects:hover {
  transform: translateY(-2px) scale(1.02);
  box-shadow: 0 8px 25px rgba(163, 209, 198, 0.7);
}

.join-class-btn-subjects svg {
  fill: #3D8D7A;
}

.subject-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 1.5rem;
}

.subject-card {
  border: 1px solid rgba(61, 141, 122, 0.1);
  border-radius: 16px;
  padding: 1.5rem;
  background: rgba(179, 216, 168, 0.2);
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  cursor: pointer;
}

.subject-card:hover {
  background: rgba(179, 216, 168, 0.4);
  transform: translateY(-2px);
  box-shadow: 0 4px 16px rgba(163, 209, 198, 0.25);
  border-color: rgba(61, 141, 122, 0.2);
}

.subject-card h3 {
  font-size: 1.125rem;
  color: #3D8D7A;
  margin-bottom: 0.5rem;
  font-weight: 700;
}

.subject-card p {
  color: #6c757d;
  font-size: 0.875rem;
}

.view-btn {
  background: linear-gradient(135deg, #A3D1C6 0%, #B3D8A8 100%);
  color: #3D8D7A;
  padding: 0.6rem 1rem;
  border: none;
  border-radius: 12px;
  cursor: pointer;
  margin-top: 1rem;
  font-size: 0.8rem;
  font-weight: 600;
  transition: all 0.3s ease;
}

.view-btn:hover {
  transform: scale(1.05);
}

.back-btn {
  background: transparent;
  border: none;
  color: #3D8D7A;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  margin-bottom: 1rem;
  transition: all 0.3s ease;
}

.back-btn:hover {
  text-decoration: underline;
  transform: translateX(-5px);
}


/* Settings */
.settings-container {
  display: grid;
  gap: 1.5rem;
}

.setting-item {
  border: 1px solid rgba(61, 141, 122, 0.1);
  border-radius: 16px;
  padding: 1.5rem;
  background: rgba(251, 255, 228, 0.5);
  transition: all 0.3s ease;
}

.setting-item:hover {
  background: rgba(251, 255, 228, 0.8);
  transform: translateY(-2px);
}

.setting-item h3 {
  font-size: 1.125rem;
  color: #3D8D7A;
  margin-bottom: 0.5rem;
}

.setting-item p {
  font-size: 0.875rem;
  color: #6c757d;
}

.settings-btn {
  background: #fff;
  color: #3D8D7A;
  border: 1px solid #3D8D7A;
  padding: 0.6rem 1rem;
  border-radius: 12px;
  cursor: pointer;
  margin-top: 1rem;
  font-size: 0.8rem;
  font-weight: 600;
  transition: all 0.3s ease;
}

.settings-btn:hover {
  background: #3D8D7A;
  color: #fff;
}

/* Modal */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.4);
  backdrop-filter: blur(5px);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
}

.modal-content {
  background: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(15px);
  padding: 2.5rem;
  border-radius: 20px;
  width: 90%;
  max-width: 450px;
  text-align: center;
  box-shadow: 0 16px 40px rgba(0, 0, 0, 0.15);
  border: 1px solid rgba(255, 255, 255, 0.5);
  animation: modal-fade-in 0.3s cubic-bezier(0.25, 0.46, 0.45, 0.94) forwards;
}

@keyframes modal-fade-in {
  from {
    opacity: 0;
    transform: translateY(-20px) scale(0.9);
  }
  to {
    opacity: 1;
    transform: translateY(0) scale(1);
  }
}

.modal-content h3 {
  font-size: 1.75rem;
  margin-bottom: 0.5rem;
  color: #3D8D7A;
  font-weight: 700;
}

.class-code-input {
  width: 100%;
  padding: 0.75rem;
  margin: 1.5rem 0;
  border: 1px solid rgba(61, 141, 122, 0.2);
  border-radius: 12px;
  text-align: center;
  font-size: 1rem;
  background: rgba(251, 255, 228, 0.5);
  transition: all 0.3s ease;
}

.class-code-input:focus {
  outline: none;
  border-color: #B3D8A8;
  box-shadow: 0 0 0 4px rgba(179, 216, 168, 0.3);
}

.modal-actions {
  display: flex;
  gap: 0.75rem;
  justify-content: center;
}

.modal-btn {
  padding: 0.75rem 1.5rem;
  border: none;
  border-radius: 12px;
  font-weight: 600;
  cursor: pointer;
  font-size: 0.95rem;
  transition: all 0.3s ease;
}

.join-btn {
  background: linear-gradient(135deg, #B3D8A8 0%, #A3D1C6 100%);
  color: #3D8D7A;
}

.join-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(163, 209, 198, 0.4);
}

.cancel-btn {
  background-color: rgba(61, 141, 122, 0.1);
  color: #3D8D7A;
}

.cancel-btn:hover {
  background-color: rgba(61, 141, 122, 0.2);
}

.success-message {
  color: #3D8D7A;
  font-weight: 600;
  margin-top: 1rem;
  font-size: 0.9rem;
}

.error-message {
  color: #ef4444;
  font-weight: 600;
  margin-top: 1rem;
  font-size: 0.9rem;
}

/* Responsive */
@media (max-width: 1024px) {
  .dashboard-section.card {
    min-height: auto;
  }
}

@media (max-width: 768px) {
  .dashboard-container {
    flex-direction: column;
    height: auto;
    overflow-y: auto;
  }

  .sidebar {
    width: 100%;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
    padding: 1.5rem;
    border-right: none;
    border-bottom: 1px solid rgba(61, 141, 122, 0.1);
    position: sticky;
    top: 0;
    z-index: 10;
    height: auto;
    backdrop-filter: blur(20px);
  }

  .user-info {
    flex-direction: row;
    align-items: center;
    gap: 1rem;
    text-align: left;
    margin-bottom: 0;
    padding: 1rem 1.5rem;
    background: rgba(251, 255, 228, 0.5);
    border-radius: 16px;
  }

  .profile-pic-placeholder {
    width: 50px;
    height: 50px;
    margin: 0;
  }

  .profile-pic-placeholder svg {
    width: 28px;
    height: 28px;
  }

  .user-info h3 {
    font-size: 1.1rem;
    margin-bottom: 0.25rem;
  }

  .user-info .role {
    font-size: 0.75rem;
    padding: 0.2rem 0.5rem;
  }

  .nav-links {
    display: none;
  }

  .join-class-btn {
    display: none;
  }

  .logout-btn {
    margin-top: 0;
    padding: 0.75rem 1.25rem;
    font-size: 0.85rem;
    border-radius: 12px;
  }

  .main-content {
    flex: 1;
    overflow-y: auto;
    height: calc(100vh - 72px);
  }

  .content-wrapper {
    padding: 1.25rem 1rem;
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

@media (max-width: 480px) {
  .sidebar {
    padding: 1rem;
  }

  .user-info {
    padding: 0.75rem 1rem;
    gap: 0.75rem;
  }

  .profile-pic-placeholder {
    width: 40px;
    height: 40px;
  }

  .profile-pic-placeholder svg {
    width: 24px;
    height: 24px;
  }

  .user-info h3 {
    font-size: 1rem;
  }

  .logout-btn {
    padding: 0.6rem 1rem;
    font-size: 0.8rem;
  }
}
</style>