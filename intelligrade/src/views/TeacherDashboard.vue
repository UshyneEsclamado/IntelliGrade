<template>
  <div class="dashboard-container">
    <aside class="sidebar">
      <div class="user-info">
        <div class="profile-pic-placeholder">
          <svg width="48" height="48" viewBox="0 0 24 24" fill="currentColor">
            <path d="M12,4A4,4 0 0,1 16,8A4,4 0 0,1 12,12A4,4 0 0,1 8,8A4,4 0 0,1 12,4M12,14C16.42,14 20,15.79 20,18V20H4V18C4,15.79 7.58,14 12,14Z" />
          </svg>
        </div>
        <h3>{{ fullName || 'Loading...' }}</h3>
        <p class="role">Teacher</p>
      </div>

      <nav class="nav-links">
        <a href="#assessments-to-grade" class="nav-item">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M15,16H19V18H15V16M15,8H19V10H15V8M15,12H19V14H15V12M13,3A2,2 0 0,1 15,5V19A2,2 0 0,1 13,21H5A2,2 0 0,1 3,19V5A2,2 0 0,1 5,3H13M14,19V5H5V19H14Z" /></svg>
          Assessments
        </a>
        <a href="#classes" class="nav-item">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M13,11A1,1 0 0,0 12,10A1,1 0 0,0 11,11V14H10A1,1 0 0,0 9,15A1,1 0 0,0 10,16H11V17A1,1 0 0,0 12,18A1,1 0 0,0 13,17V16H14A1,1 0 0,0 15,15A1,1 0 0,0 14,14H13V11M20,2A2,2 0 0,1 22,4V22A2,2 0 0,1 20,24H4A2,2 0 0,1 2,22V4A2,2 0 0,1 4,2H11C11,1.45 11.45,1 12,1C12.55,1 13,1.45 13,2H20M20,4H13V2H11V4H4V22H20V4Z" /></svg>
          My Classes
        </a>
        <a href="#create-quiz" class="nav-item">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2A10 10 0 0 0 2 12A10 10 0 0 0 12 22A10 10 0 0 0 22 12A10 10 0 0 0 12 2M12 4A8 8 0 0 1 20 12A8 8 0 0 1 12 20A8 8 0 0 1 4 12A8 8 0 0 1 12 4M11 7H13V13H11V7M11 15H13V17H11V15Z" /></svg>
          Create Quiz
        </a>
        <a href="#results" class="nav-item">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2M12,4A8,8 0 0,1 20,12A8,8 0 0,1 12,20A8,8 0 0,1 4,12A8,8 0 0,1 12,4M15,16H19V18H15V16M15,8H19V10H15V8M15,12H19V14H15V12M13,3A2,2 0 0,1 15,5V19A2,2 0 0,1 13,21H5A2,2 0 0,1 3,19V5A2,2 0 0,1 5,3H13M14,19V5H5V19H14Z" /></svg>
          Past Results
        </a>
        <a href="#chat" class="nav-item">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M20,2H4A2,2 0 0,0 2,4V22L6,18H20A2,2 0 0,0 22,16V4A2,2 0 0,0 20,2M6,9H18V11H6V9M14,14H6V12H14V14M18,8H6V6H18V8Z" /></svg>
          Student Chat
        </a>
        <a href="#analytics" class="nav-item">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M16 11V3H8V11H16M12 2C12.55 2 13 2.45 13 3V11H15V3A2 2 0 0 0 13 1H11A2 2 0 0 0 9 3V11H11V3C11 2.45 11.45 2 12 2M15 13V15H17A2 2 0 0 1 19 17A2 2 0 0 1 17 19H15V21H17A4 4 0 0 0 21 17A4 4 0 0 0 17 13H15M8 13V21H10V13H8M11 13V21H13V13H11Z" /></svg>
          Analytics
        </a>
        <button @click="openCreateClassModal" class="nav-item create-class-btn">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M19,13H13V19H11V13H5V11H11V5H13V11H19V13Z" /></svg>
          Create Class
        </button>
      </nav>
      <button @click="openLogoutModal" class="logout-btn">Logout</button>
    </aside>

    <main class="main-content">
      <div class="content-wrapper">
        <header class="dashboard-header">
          <h1>Hello, Teacher {{ fullName || 'Teacher' }}!</h1>
          <p>Welcome to your teaching dashboard. Here you can manage your classes, grade assessments, and track student progress.</p>
        </header>

        <div class="sections-container">
          <section id="assessments-to-grade" class="dashboard-section card">
            <div class="section-header">
              <h2>📝 Assessments to Grade</h2>
              <p class="section-subtitle">A list of assessments waiting for your attention.</p>
            </div>
            <div class="assessment-grid">
              <div v-if="assessmentsToGrade.length === 0" class="empty-state">
                <p>No new assessments to grade at the moment.</p>
              </div>
              <div v-for="assessment in assessmentsToGrade" :key="assessment.id" class="assessment-card">
                <h3>{{ assessment.title }}</h3>
                <p>Class: {{ assessment.className }}</p>
                <p>Submitted: {{ assessment.studentsSubmitted }} / {{ assessment.totalStudents }}</p>
                <button class="start-btn">Grade Assessment</button>
              </div>
            </div>
            <button class="upload-btn">Upload Assessment for Auto-Check</button>
          </section>

          <section id="classes" class="dashboard-section card">
            <div class="section-header">
              <h2>📚 My Classes</h2>
              <p class="section-subtitle">Manage your classes and sections.</p>
            </div>
            <div class="classes-container">
              <div v-if="classes.length === 0" class="empty-state">
                <p>You have not created any classes yet.</p>
              </div>
              <div v-for="classItem in classes" :key="classItem.id" class="class-card">
                <h3>{{ classItem.className }}</h3>
                <p>Section: {{ classItem.sectionName }}</p>
                <p>Students: {{ classItem.studentsEnrolled }}</p>
                <div class="class-code-display">
                  <span class="code-label">Class Code:</span>
                  <span class="code-value">{{ classItem.classCode }}</span>
                </div>
              </div>
            </div>
            <button @click="openCreateClassModal" class="create-class-main-btn">
              Create New Class
            </button>
          </section>

          <section id="create-quiz" class="dashboard-section card">
            <div class="section-header">
              <h2>✍️ Create Online Quiz</h2>
              <p class="section-subtitle">Build new quizzes directly in the system.</p>
            </div>
            <div class="empty-state">
              <p>This feature will be available soon. Please check back later.</p>
            </div>
          </section>

          <section id="results" class="dashboard-section card">
            <div class="section-header">
              <h2>📈 View Past Results</h2>
              <p class="section-subtitle">See student results and detailed analytics after grading.</p>
            </div>
            <div class="empty-state">
              <p>This feature will be available soon. Please check back later.</p>
            </div>
          </section>
        </div>
      </div>
    </main>

    <div v-if="showCreateClassModal" class="modal-overlay" @click.self="closeCreateClassModal">
      <div class="modal-content">
        <h3>Create a New Class</h3>
        <p>Enter the class name and section to generate a unique class code.</p>
        <input type="text" v-model="newClass.name" placeholder="Class Name (e.g., Science 101)" class="class-input">
        <input type="text" v-model="newClass.section" placeholder="Section (e.g., A)" class="class-input">
        <div class="modal-actions">
          <button @click="createClass" class="modal-btn create-btn">Create</button>
          <button @click="closeCreateClassModal" class="modal-btn cancel-btn">Cancel</button>
        </div>
        <p v-if="createClassStatus" :class="{'success-message': createClassStatus.startsWith('Successfully'), 'error-message': !createClassStatus.startsWith('Successfully')}">{{ createClassStatus }}</p>
      </div>
    </div>

    <div v-if="showLogoutModal" class="modal-overlay" @click.self="closeLogoutModal">
      <div class="modal-content">
        <h3>Confirm Logout</h3>
        <p>Are you sure you want to log out?</p>
        <div class="modal-actions">
          <button @click="handleLogout" class="modal-btn create-btn">Confirm</button>
          <button @click="closeLogoutModal" class="modal-btn cancel-btn">Cancel</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { supabase } from '../supabase';
import { useRouter } from 'vue-router';

const router = useRouter();

const fullName = ref('');
const assessmentsToGrade = ref([]);
const classes = ref([]);
const showCreateClassModal = ref(false);
const showLogoutModal = ref(false);
const newClass = ref({
  name: '',
  section: ''
});
const createClassStatus = ref(null);

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
    router.push('/login');
  }
};

const fetchAssessmentsToGrade = async () => {
  // Mock data for display. Replace with real Supabase calls.
  assessmentsToGrade.value = [
    { id: 1, title: 'Algebra Quiz', className: 'Math 101', studentsSubmitted: 15, totalStudents: 20 },
    { id: 2, title: 'Cell Biology Test', className: 'Science 101', studentsSubmitted: 22, totalStudents: 25 },
  ];
};

const fetchClasses = async () => {
  // Mock data for display. Replace with real Supabase calls.
  classes.value = [
    { id: 1, className: 'Math 101', sectionName: 'A', studentsEnrolled: 20, classCode: 'MATH101A' },
    { id: 2, className: 'Science 101', sectionName: 'B', studentsEnrolled: 25, classCode: 'SCI101B' },
  ];
};

const openCreateClassModal = () => {
  showCreateClassModal.value = true;
  newClass.value.name = '';
  newClass.value.section = '';
  createClassStatus.value = null;
};

const closeCreateClassModal = () => {
  showCreateClassModal.value = false;
};

const openLogoutModal = () => {
  showLogoutModal.value = true;
};

const closeLogoutModal = () => {
  showLogoutModal.value = false;
};

const createClass = async () => {
  if (!newClass.value.name || !newClass.value.section) {
    createClassStatus.value = 'Please fill in all fields.';
    return;
  }
  
  try {
    // Generate a simple class code. For a real app, use a more robust method.
    const classCode = `${newClass.value.name.substring(0, 4).toUpperCase()}${Math.floor(Math.random() * 1000)}`;
    
    // In a real app, you would insert this into your 'classes' table.
    // Example: const { data, error } = await supabase.from('classes').insert({...});
    const newClassEntry = {
      id: Date.now(),
      className: newClass.value.name,
      sectionName: newClass.value.section,
      studentsEnrolled: 0,
      classCode: classCode
    };
    
    classes.value.push(newClassEntry);
    createClassStatus.value = 'Successfully created class! Code: ' + classCode;
  } catch (err) {
    console.error('Error creating class:', err);
    createClassStatus.value = `Error: ${err.message}`;
  }
};

const handleLogout = async () => {
  try {
    closeLogoutModal();
    const { error } = await supabase.auth.signOut();
    if (error) {
      throw error;
    }
    
    router.push('/login');
  } catch (err) {
    console.error('Logout error:', err);
  }
};

onMounted(() => {
  fetchUserProfile();
  fetchAssessmentsToGrade();
  fetchClasses();
});
</script>

<style>
/* Global styles */
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

html, body {
  height: 100%;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
  background-color: #f6fbf4;
}

#app {
  height: 100vh;
}
</style>

<style scoped>
/* Scoped styles specific to this component */
.dashboard-container {
  display: flex;
  height: 100vh;
  width: 100vw;
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
  overflow-y: auto;
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
  color: #6c757d;
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
  background-color: #f1f7f0;
  color: #3D8D7A;
}

.nav-item:hover svg {
  fill: #3D8D7A;
}

.create-class-btn {
  background-color: #B3D8A8;
  color: #3D8D7A;
  margin-top: 1rem;
  transition: background-color 0.2s ease-in-out;
}

.create-class-btn svg {
  fill: #3D8D7A;
}

.create-class-btn:hover {
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
  overflow-y: auto;
  background-color: #f6fbf4;
}

.content-wrapper {
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

.start-btn, .upload-btn, .create-class-main-btn {
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

.start-btn:hover, .upload-btn:hover, .create-class-main-btn:hover {
  background-color: #A3D1C6;
}

.classes-container {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 1rem;
}

.class-card {
  border: 1px solid #e0e6e0;
  border-radius: 8px;
  padding: 1.25rem;
  background-color: #fff;
  transition: all 0.2s ease-in-out;
}

.class-card:hover {
  border-color: #A3D1C6;
  box-shadow: 0 4px 12px rgba(163, 209, 198, 0.25);
}

.class-card h3 {
  font-size: 1.125rem;
  color: #3D8D7A;
  margin-bottom: 0.5rem;
  font-weight: 600;
}

.class-card p {
  color: #6c757d;
  font-size: 0.875rem;
  margin-bottom: 0.25rem;
}

.class-code-display {
  background-color: #f1f7f0;
  border: 1px dashed #A3D1C6;
  border-radius: 6px;
  padding: 0.5rem 0.75rem;
  margin-top: 1rem;
  text-align: center;
}

.code-label {
  font-size: 0.75rem;
  font-weight: 500;
  color: #6c757d;
}

.code-value {
  font-size: 1rem;
  font-weight: 600;
  color: #3D8D7A;
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

.class-input {
  width: 100%;
  padding: 0.75rem;
  margin: 0.75rem 0;
  border: 1px solid #e0e6e0;
  border-radius: 8px;
  text-align: center;
  font-size: 1rem;
  transition: border-color 0.2s ease-in-out;
}

.class-input:focus {
  outline: none;
  border-color: #B3D8A8;
}

.modal-actions {
  display: flex;
  gap: 0.75rem;
  justify-content: center;
  margin-top: 1.25rem;
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

.create-btn {
  background-color: #B3D8A8;
  color: #3D8D7A;
}

.create-btn:hover {
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
    height: auto;
  }
  
  .sidebar {
    width: 100%;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
    padding: 1rem 1.25rem;
    border-right: none;
    border-bottom: 1px solid #e0e6e0;
    position: sticky;
    top: 0;
    z-index: 10;
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
  
  .main-content {
    flex: 1;
    overflow-y: auto;
    padding-top: 1.25rem;
  }

  .content-wrapper {
    padding: 0 1rem;
  }
  
  .dashboard-header {
    padding: 1rem 0;
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