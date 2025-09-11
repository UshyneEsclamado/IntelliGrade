<template>
  <div class="page-container">
    <div class="main-wrapper">
      <div class="hero-header card-box">
        <div class="header-content">
          <button @click="goBack" class="back-button">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
              <path d="M10 19l-7-7 7-7m-7 7h18"></path>
            </svg>
            Back to Classes
          </button>
          <h1>{{ currentStep === 1 ? 'Create New Class' : 'Add Students' }}</h1>
          <p>{{ currentStep === 1 ? 'Fill in the details below to create a new class.' : 'Add students to your new class.' }}</p>
        </div>
      </div>

      <!-- Step 1: Class Details -->
      <div v-if="currentStep === 1" class="class-form card-box">
        <form @submit.prevent="nextStep">
          <div class="form-group">
            <label for="class-name">Class Name</label>
            <input 
              type="text" 
              id="class-name" 
              v-model="className" 
              required 
              placeholder="e.g., Grade 10 - Rizal"
            >
          </div>
          
          <div class="form-group">
            <label for="class-subject">Subject</label>
            <input 
              type="text" 
              id="class-subject" 
              v-model="classSubject" 
              required 
              placeholder="e.g., Mathematics"
            >
          </div>
          
          <div class="form-actions">
            <button type="submit" class="submit-btn">
              Next: Add Students
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <polyline points="9,18 15,12 9,6"></polyline>
              </svg>
            </button>
          </div>
        </form>
      </div>

      <!-- Step 2: Add Students -->
      <div v-if="currentStep === 2" class="students-form card-box">
        <div class="students-section">
          <div class="students-header">
            <h3>Add Students to "{{ className }}"</h3>
            <p>You can add students now or skip and add them later.</p>
          </div>

          <!-- Add Student Form -->
          <form @submit.prevent="addStudent" class="add-student-form">
            <div class="student-input-group">
              <div class="form-group">
                <label for="student-id">Student ID</label>
                <input 
                  type="text" 
                  id="student-id" 
                  v-model="newStudentId" 
                  placeholder="Enter student ID"
                  :disabled="submitting"
                >
              </div>
              <div class="form-group">
                <label for="student-name">Student Name</label>
                <input 
                  type="text" 
                  id="student-name" 
                  v-model="newStudentName" 
                  placeholder="Enter student name"
                  :disabled="submitting"
                >
              </div>
              <div class="form-group">
                <label for="student-email">Email (Optional)</label>
                <input 
                  type="email" 
                  id="student-email" 
                  v-model="newStudentEmail" 
                  placeholder="student@example.com"
                  :disabled="submitting"
                >
              </div>
              <button type="submit" class="add-student-btn" :disabled="!newStudentName.trim() || !newStudentId.trim() || submitting">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <line x1="12" y1="5" x2="12" y2="19"></line>
                  <line x1="5" y1="12" x2="19" y2="12"></line>
                </svg>
                Add Student
              </button>
            </div>
          </form>

          <!-- Students List -->
          <div v-if="students.length > 0" class="students-list">
            <h4>Added Students ({{ students.length }})</h4>
            <div class="student-cards">
              <div v-for="(student, index) in students" :key="index" class="student-card">
                <div class="student-info">
                  <h5>{{ student.name }}</h5>
                  <p class="student-id">ID: {{ student.student_id }}</p>
                  <p v-if="student.email" class="student-email">{{ student.email }}</p>
                </div>
                <button @click="removeStudent(index)" class="remove-student-btn" :disabled="submitting">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <line x1="18" y1="6" x2="6" y2="18"></line>
                    <line x1="6" y1="6" x2="18" y2="18"></line>
                  </svg>
                </button>
              </div>
            </div>
          </div>

          <!-- Action Buttons -->
          <div class="step-actions">
            <button @click="previousStep" class="back-step-btn" :disabled="submitting">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <polyline points="15,18 9,12 15,6"></polyline>
              </svg>
              Back to Class Details
            </button>
            <button @click="finishCreation" class="finish-btn" :disabled="submitting">
              <svg v-if="submitting" class="spinner-icon" width="20" height="20" viewBox="0 0 24 24">
                <circle cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4" fill="none" opacity="0.25"/>
                <path d="M4 12a8 8 0 0 1 8-8" stroke="currentColor" stroke-width="4" fill="none"/>
              </svg>
              <svg v-else width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <polyline points="20,6 9,17 4,12"></polyline>
              </svg>
              {{ submitting ? 'Creating Class...' : 'Create Class' }}
            </button>
          </div>
        </div>
      </div>

      <!-- Error Message -->
      <div v-if="error" class="error-message">
        {{ error }}
      </div>
    </div>

    <!-- Success Modal -->
    <div v-if="showModal" class="modal-overlay" @click.self="closeModal">
      <div class="modal-content">
        <svg class="success-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor">
          <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/>
        </svg>
        <h3>Class Created Successfully!</h3>
        <p>
          <strong>"{{ className }}"</strong> has been created with 
          <strong>{{ students.length }}</strong> student{{ students.length !== 1 ? 's' : '' }}.
        </p>
        <button @click="closeModal" class="modal-ok-btn">View My Classes</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { supabase } from '../../supabase';

const router = useRouter();

// Form data
const className = ref('');
const classSubject = ref('');
const students = ref([]);
const newStudentName = ref('');
const newStudentId = ref('');
const newStudentEmail = ref('');

// UI state
const currentStep = ref(1);
const showModal = ref(false);
const error = ref('');
const submitting = ref(false);

const goBack = () => {
  router.push({ name: 'MyClasses' });
};

const nextStep = () => {
  if (!className.value.trim() || !classSubject.value.trim()) {
    error.value = 'Please fill in all required fields.';
    return;
  }
  error.value = '';
  currentStep.value = 2;
};

const previousStep = () => {
  currentStep.value = 1;
};

const addStudent = () => {
  if (!newStudentName.value.trim() || !newStudentId.value.trim()) return;
  
  // Check for duplicate student IDs
  if (students.value.some(s => s.student_id.toLowerCase() === newStudentId.value.trim().toLowerCase())) {
    error.value = 'A student with this ID already exists.';
    return;
  }
  
  // Check for duplicate names
  if (students.value.some(s => s.name.toLowerCase() === newStudentName.value.trim().toLowerCase())) {
    error.value = 'A student with this name already exists.';
    return;
  }
  
  students.value.push({
    student_id: newStudentId.value.trim(),
    name: newStudentName.value.trim(),
    email: newStudentEmail.value.trim() || null
  });
  
  // Clear form
  newStudentId.value = '';
  newStudentName.value = '';
  newStudentEmail.value = '';
  error.value = '';
};

const removeStudent = (index) => {
  students.value.splice(index, 1);
};

const finishCreation = async () => {
  error.value = '';
  submitting.value = true;
  
  try {
    // Get current user
    const { data: { user }, error: userError } = await supabase.auth.getUser();
    
    if (userError) throw userError;
    
    if (!user) {
      error.value = 'You must be logged in to create a class.';
      router.push('/login');
      return;
    }

    // Insert new class into Supabase
    const { data: classData, error: insertError } = await supabase
      .from('classes')
      .insert([{
        name: className.value.trim(),
        subject: classSubject.value.trim(),
        teacher_id: user.id,
        student_count: students.value.length,
        assessments: 0,
        created_at: new Date().toISOString()
      }])
      .select()
      .single();

    if (insertError) {
      console.error('Insert class error:', insertError);
      throw insertError;
    }

    // Insert students if any
    if (students.value.length > 0) {
      const studentsData = students.value.map(student => ({
        class_id: classData.id,
        student_id: student.student_id,
        name: student.name,
        email: student.email,
        teacher_id: user.id,
        created_at: new Date().toISOString()
      }));

      const { error: studentsError } = await supabase
        .from('students')
        .insert(studentsData);

      if (studentsError) {
        console.error('Insert students error:', studentsError);
        // Don't throw here - class is created, just log the error
        console.warn('Class created but some students failed to add:', studentsError);
      }
    }

    console.log('Class created successfully:', classData);
    
    // Show success modal
    showModal.value = true;

  } catch (err) {
    console.error('Create class error:', err);
    
    // Handle specific error cases
    if (err.code === '23505') {
      error.value = 'A class with this name already exists.';
    } else if (err.code === 'PGRST301' || err.message?.includes('JWT')) {
      error.value = 'Authentication error. Please log in again.';
      setTimeout(() => router.push('/login'), 2000);
    } else if (err.message?.includes('permission')) {
      error.value = 'You do not have permission to create classes.';
    } else {
      error.value = err.message || 'Failed to create class. Please try again.';
    }
  } finally {
    submitting.value = false;
  }
};

const closeModal = () => {
  showModal.value = false;
  
  // Navigate back to MyClasses with a timestamp to trigger refresh
  router.push({ 
    name: 'MyClasses', 
    query: { createdAt: Date.now() } 
  });
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

.page-container {
  padding: 2rem 5%;
  font-family: 'Inter', sans-serif;
  min-height: 100vh;
}

.main-wrapper {
  max-width: 1400px;
  margin: 0 auto;
}

.card-box {
  background: rgba(255, 255, 255, 0.85);
  backdrop-filter: blur(20px);
  border: 1px solid rgba(61, 141, 122, 0.1);
  border-radius: 24px;
  padding: 2.5rem;
  box-shadow: 
    0 8px 32px rgba(61, 141, 122, 0.1),
    0 0 0 1px rgba(255, 255, 255, 0.2);
}

.hero-header {
  margin-bottom: 2rem;
}

.back-button {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  background: none;
  border: none;
  color: #3D8D7A;
  font-weight: 600;
  font-size: 1rem;
  cursor: pointer;
  transition: all 0.3s;
  margin-bottom: 1rem;
}

.back-button:hover {
  color: #2e6b5c;
  transform: translateX(-5px);
}

.hero-header h1 {
  font-size: 2.5rem;
  font-weight: 800;
  color: #3D8D7A;
  margin: 0;
}

.hero-header p {
  font-size: 1.1rem;
  color: #666;
  margin: 0;
}

/* Step 1: Class Form */
.class-form {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

label {
  font-weight: 600;
  color: #444;
  font-size: 1rem;
}

input[type="text"], input[type="email"] {
  width: 100%;
  padding: 1rem;
  border: 2px solid #e1e1e1;
  border-radius: 12px;
  font-size: 1rem;
  transition: all 0.3s;
  background: #fff;
  box-sizing: border-box;
}

input[type="text"]:focus, input[type="email"]:focus {
  outline: none;
  border-color: #3D8D7A;
  box-shadow: 0 0 0 3px rgba(61, 141, 122, 0.2);
}

input[type="text"]:disabled, input[type="email"]:disabled {
  background: #f5f5f5;
  color: #999;
  cursor: not-allowed;
}

input[type="text"]::placeholder, input[type="email"]::placeholder {
  color: #aaa;
}

.form-actions {
  display: flex;
  justify-content: flex-end;
  margin-top: 1rem;
}

.submit-btn {
  background: linear-gradient(135deg, #3D8D7A 0%, #A3D1C6 100%);
  color: #fff;
  border: none;
  padding: 1rem 2rem;
  border-radius: 16px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s;
  box-shadow: 0 8px 32px rgba(61, 141, 122, 0.2);
  display: flex;
  align-items: center;
  gap: 0.5rem;
  min-width: 180px;
  justify-content: center;
}

.submit-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 16px 48px rgba(61, 141, 122, 0.3);
}

/* Step 2: Students Form */
.students-section {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.students-header h3 {
  font-size: 1.5rem;
  font-weight: 700;
  color: #3D8D7A;
  margin-bottom: 0.5rem;
}

.students-header p {
  color: #666;
  margin: 0;
}

.add-student-form {
  border: 2px dashed rgba(61, 141, 122, 0.2);
  border-radius: 16px;
  padding: 2rem;
  background: rgba(61, 141, 122, 0.02);
}

.student-input-group {
  display: grid;
  grid-template-columns: 1fr 2fr 1.5fr auto;
  gap: 1rem;
  align-items: end;
}

.add-student-btn {
  background: #3D8D7A;
  color: white;
  border: none;
  padding: 1rem 1.5rem;
  border-radius: 12px;
  font-size: 0.9rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  white-space: nowrap;
}

.add-student-btn:hover:not(:disabled) {
  background: #2e6b5c;
  transform: translateY(-1px);
}

.add-student-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
  transform: none;
}

/* Students List */
.students-list h4 {
  font-size: 1.2rem;
  font-weight: 600;
  color: #3D8D7A;
  margin-bottom: 1rem;
}

.student-cards {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 1rem;
}

.student-card {
  background: white;
  border: 1px solid #e1e1e1;
  border-radius: 12px;
  padding: 1rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  transition: all 0.3s;
}

.student-card:hover {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  transform: translateY(-2px);
}

.student-info h5 {
  font-size: 1rem;
  font-weight: 600;
  color: #333;
  margin: 0 0 0.25rem 0;
}

.student-info p.student-id {
  color: #3D8D7A;
  font-weight: 600;
  margin: 0 0 0.25rem 0;
  font-size: 0.85rem;
}

.student-info p.student-email {
  color: #666;
  margin: 0;
  font-size: 0.85rem;
}

.remove-student-btn {
  background: #dc3545;
  color: white;
  border: none;
  width: 32px;
  height: 32px;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.3s;
  display: flex;
  align-items: center;
  justify-content: center;
}

.remove-student-btn:hover:not(:disabled) {
  background: #c82333;
  transform: scale(1.1);
}

.remove-student-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
  transform: none;
}

/* Step Actions */
.step-actions {
  display: flex;
  justify-content: space-between;
  gap: 1rem;
  margin-top: 2rem;
  padding-top: 2rem;
  border-top: 1px solid #e1e1e1;
}

.back-step-btn {
  background: #6c757d;
  color: white;
  border: none;
  padding: 1rem 1.5rem;
  border-radius: 12px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.back-step-btn:hover:not(:disabled) {
  background: #5a6268;
  transform: translateY(-1px);
}

.finish-btn {
  background: linear-gradient(135deg, #3D8D7A 0%, #A3D1C6 100%);
  color: #fff;
  border: none;
  padding: 1rem 2rem;
  border-radius: 16px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s;
  box-shadow: 0 8px 32px rgba(61, 141, 122, 0.2);
  display: flex;
  align-items: center;
  gap: 0.5rem;
  min-width: 160px;
  justify-content: center;
}

.finish-btn:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 16px 48px rgba(61, 141, 122, 0.3);
}

.finish-btn:disabled {
  opacity: 0.7;
  cursor: not-allowed;
  transform: none;
}

.spinner-icon {
  animation: spin 1s linear infinite;
}

@keyframes spin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}

.error-message {
  background: #ffebee;
  color: #c62828;
  padding: 1rem;
  border-radius: 12px;
  margin-top: 1rem;
  border: 1px solid #ffcdd2;
  font-weight: 500;
}

/* Modal Styles */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
  backdrop-filter: blur(4px);
}

.modal-content {
  background: #fff;
  border-radius: 24px;
  padding: 3rem;
  text-align: center;
  box-shadow: 0 16px 64px rgba(61, 141, 122, 0.3);
  max-width: 500px;
  width: 90%;
  transform: scale(0.9);
  animation: modalScale 0.3s forwards;
}

@keyframes modalScale {
  to {
    transform: scale(1);
  }
}

.success-icon {
  color: #3D8D7A;
  width: 80px;
  height: 80px;
  margin-bottom: 1.5rem;
}

.modal-content h3 {
  color: #3D8D7A;
  font-size: 2rem;
  font-weight: 800;
  margin-bottom: 0.5rem;
}

.modal-content p {
  color: #666;
  font-size: 1rem;
  margin-bottom: 1.5rem;
}

.modal-ok-btn {
  background: linear-gradient(135deg, #3D8D7A 0%, #A3D1C6 100%);
  color: #fff;
  border: none;
  padding: 1rem 2rem;
  border-radius: 16px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s;
}

.modal-ok-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 32px rgba(61, 141, 122, 0.2);
}

/* Responsive Design */
@media (max-width: 768px) {
  .page-container {
    padding: 1rem 3%;
  }
  
  .card-box {
    padding: 1.5rem;
  }
  
  .hero-header h1 {
    font-size: 2rem;
  }
  
  .student-input-group {
    grid-template-columns: 1fr;
  }
  
  .step-actions {
    flex-direction: column-reverse;
  }
  
  .student-cards {
    grid-template-columns: 1fr;
  }
  
  .modal-content {
    padding: 2rem;
  }
}
</style>