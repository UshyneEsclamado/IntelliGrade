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
          <h1>Manage Students</h1>
          <p v-if="classData">{{ classData.name }} - {{ classData.subject }}</p>
        </div>
      </div>

      <div v-if="loading" class="loading-state">
        <div class="spinner"></div>
        <p>Loading students...</p>
      </div>

      <div v-else>
        <!-- Add Student Section -->
        <div class="add-student-section card-box">
          <h3>Add New Student</h3>
          <form @submit.prevent="addStudent" class="add-student-form">
            <div class="student-input-group">
              <div class="form-group">
                <label for="student-name">Student Name</label>
                <input 
                  type="text" 
                  id="student-name" 
                  v-model="newStudentName" 
                  placeholder="Enter student name"
                  :disabled="submitting"
                  required
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
              <button type="submit" class="add-student-btn" :disabled="!newStudentName.trim() || submitting">
                <svg v-if="submitting" class="spinner-icon" width="16" height="16" viewBox="0 0 24 24">
                  <circle cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4" fill="none" opacity="0.25"/>
                  <path d="M4 12a8 8 0 0 1 8-8" stroke="currentColor" stroke-width="4" fill="none"/>
                </svg>
                <svg v-else width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <line x1="12" y1="5" x2="12" y2="19"></line>
                  <line x1="5" y1="12" x2="19" y2="12"></line>
                </svg>
                {{ submitting ? 'Adding...' : 'Add Student' }}
              </button>
            </div>
          </form>
        </div>

        <!-- Students List -->
        <div class="students-list card-box">
          <div class="list-header">
            <h3>Students ({{ students.length }})</h3>
          </div>

          <div v-if="students.length === 0" class="empty-state">
            <svg width="64" height="64" viewBox="0 0 24 24" fill="currentColor" class="empty-icon">
              <path d="M16 4c0-1.11.89-2 2-2s2 .89 2 2 .89 2 2 2 2-.89 2-2-.89-2-2-2-2 .89-2 2zm4 18v-6h2.5l-2.54-7.63A2.98 2.98 0 0 0 17.14 6H16c-1.56 0-2.91 1.17-3.08 2.73L12.5 16H15v6h5z"/>
            </svg>
            <h4>No Students Yet</h4>
            <p>Add your first student to get started!</p>
          </div>

          <div v-else class="student-cards">
            <div v-for="student in students" :key="student.id" class="student-card">
              <div class="student-avatar">
                <svg width="32" height="32" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z"/>
                </svg>
              </div>
              <div class="student-info">
                <h4>{{ student.name }}</h4>
                <p v-if="student.email">{{ student.email }}</p>
                <span class="join-date">Added {{ formatDate(student.created_at) }}</span>
              </div>
              <button @click="confirmRemoveStudent(student)" class="remove-student-btn" :disabled="deleting">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <polyline points="3,6 5,6 21,6"></polyline>
                  <path d="M19,6v14a2,2 0 0,1 -2,2H7a2,2 0 0,1 -2,-2V6m3,0V4a2,2 0 0,1 2,-2h4a2,2 0 0,1 2,2v2"></path>
                </svg>
              </button>
            </div>
          </div>
        </div>
      </div>

      <!-- Error Message -->
      <div v-if="error" class="error-message">
        {{ error }}
      </div>
    </div>

    <!-- Remove Student Confirmation Modal -->
    <div v-if="showRemoveModal" class="modal-overlay" @click.self="cancelRemove">
      <div class="modal-content delete-modal">
        <svg class="warning-icon" width="64" height="64" viewBox="0 0 24 24" fill="currentColor">
          <path d="M12 2L1 21h22L12 2zm0 3.83L19.31 19H4.69L12 5.83zM11 16h2v2h-2v-2zm0-6h2v4h-2v-4z"/>
        </svg>
        <h3>Remove Student?</h3>
        <p>Are you sure you want to remove <strong>"{{ studentToRemove?.name }}"</strong> from this class?</p>
        <p class="warning-text">This action cannot be undone.</p>
        
        <div class="modal-actions">
          <button @click="cancelRemove" class="cancel-btn">Cancel</button>
          <button @click="removeStudent" class="delete-btn" :disabled="deleting">
            <svg v-if="deleting" class="spinner-icon" width="16" height="16" viewBox="0 0 24 24">
              <circle cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4" fill="none" opacity="0.25"/>
              <path d="M4 12a8 8 0 0 1 8-8" stroke="currentColor" stroke-width="4" fill="none"/>
            </svg>
            {{ deleting ? 'Removing...' : 'Remove Student' }}
          </button>
        </div>
      </div>
    </div>

    <!-- Success Message -->
    <div v-if="successMessage" class="success-toast">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
        <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/>
      </svg>
      {{ successMessage }}
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { supabase } from '../../supabase';

const router = useRouter();

// Props
const props = defineProps({
  id: String
});

// Form data
const newStudentName = ref('');
const newStudentEmail = ref('');

// Data
const classData = ref(null);
const students = ref([]);

// UI state
const loading = ref(true);
const submitting = ref(false);
const deleting = ref(false);
const error = ref('');
const successMessage = ref('');
const showRemoveModal = ref(false);
const studentToRemove = ref(null);

const goBack = () => {
  router.push({ name: 'MyClasses' });
};

const fetchClassData = async () => {
  try {
    const { data: { user } } = await supabase.auth.getUser();
    if (!user) {
      router.push('/login');
      return;
    }

    // Fetch class details
    const { data: classDetails, error: classError } = await supabase
      .from('classes')
      .select('*')
      .eq('id', props.id)
      .eq('teacher_id', user.id)
      .single();

    if (classError) throw classError;
    classData.value = classDetails;

    // Fetch students
    await fetchStudents();

  } catch (err) {
    console.error('Error fetching class data:', err);
    error.value = 'Failed to load class data. Please try again.';
  } finally {
    loading.value = false;
  }
};

const fetchStudents = async () => {
  try {
    const { data, error: studentsError } = await supabase
      .from('students')
      .select('*')
      .eq('class_id', props.id)
      .order('created_at', { ascending: false });

    if (studentsError) throw studentsError;
    students.value = data || [];

  } catch (err) {
    console.error('Error fetching students:', err);
    error.value = 'Failed to load students. Please try again.';
  }
};

const addStudent = async () => {
  if (!newStudentName.value.trim()) return;
  
  // Check for duplicate names
  if (students.value.some(s => s.name.toLowerCase() === newStudentName.value.trim().toLowerCase())) {
    error.value = 'A student with this name already exists in this class.';
    return;
  }

  submitting.value = true;
  error.value = '';

  try {
    const { data: { user } } = await supabase.auth.getUser();
    if (!user) {
      router.push('/login');
      return;
    }

    const studentData = {
      name: newStudentName.value.trim(),
      email: newStudentEmail.value.trim() || null,
      class_id: props.id,
      teacher_id: user.id
    };

    const { data, error: insertError } = await supabase
      .from('students')
      .insert(studentData)
      .select()
      .single();

    if (insertError) throw insertError;

    // Add to local array
    students.value.unshift(data);

    // Update class student count
    await updateClassStudentCount();

    // Reset form
    newStudentName.value = '';
    newStudentEmail.value = '';

    // Show success message
    showSuccessMessage(`${data.name} has been added to the class!`);

  } catch (err) {
    console.error('Error adding student:', err);
    error.value = 'Failed to add student. Please try again.';
  } finally {
    submitting.value = false;
  }
};

const confirmRemoveStudent = (student) => {
  studentToRemove.value = student;
  showRemoveModal.value = true;
};

const cancelRemove = () => {
  showRemoveModal.value = false;
  studentToRemove.value = null;
};

const removeStudent = async () => {
  if (!studentToRemove.value) return;

  deleting.value = true;
  error.value = '';

  try {
    const { error: deleteError } = await supabase
      .from('students')
      .delete()
      .eq('id', studentToRemove.value.id);

    if (deleteError) throw deleteError;

    // Remove from local array
    students.value = students.value.filter(s => s.id !== studentToRemove.value.id);

    // Update class student count
    await updateClassStudentCount();

    // Show success message
    showSuccessMessage(`${studentToRemove.value.name} has been removed from the class.`);

    // Close modal
    showRemoveModal.value = false;
    studentToRemove.value = null;

  } catch (err) {
    console.error('Error removing student:', err);
    error.value = 'Failed to remove student. Please try again.';
  } finally {
    deleting.value = false;
  }
};

const updateClassStudentCount = async () => {
  try {
    const { error: updateError } = await supabase
      .from('classes')
      .update({ student_count: students.value.length })
      .eq('id', props.id);

    if (updateError) throw updateError;

  } catch (err) {
    console.error('Error updating class student count:', err);
  }
};

const formatDate = (dateString) => {
  const date = new Date(dateString);
  const now = new Date();
  const diffInDays = Math.floor((now - date) / (1000 * 60 * 60 * 24));

  if (diffInDays === 0) return 'Today';
  if (diffInDays === 1) return 'Yesterday';
  if (diffInDays < 7) return `${diffInDays} days ago`;
  if (diffInDays < 30) return `${Math.floor(diffInDays / 7)} week${Math.floor(diffInDays / 7) > 1 ? 's' : ''} ago`;
  
  return date.toLocaleDateString();
};

const showSuccessMessage = (message) => {
  successMessage.value = message;
  setTimeout(() => {
    successMessage.value = '';
  }, 3000);
};

// Clear error when user starts typing
const clearError = () => {
  if (error.value) {
    error.value = '';
  }
};

// Watch for input changes to clear errors
import { watch } from 'vue';
watch([newStudentName, newStudentEmail], clearError);

onMounted(() => {
  fetchClassData();
});
</script>

<style scoped>
.page-container {
  min-height: 100vh;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  padding: 2rem 1rem;
}

.main-wrapper {
  max-width: 1000px;
  margin: 0 auto;
}

.card-box {
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(10px);
  border-radius: 20px;
  box-shadow: 0 8px 32px rgba(31, 38, 135, 0.37);
  border: 1px solid rgba(255, 255, 255, 0.18);
  margin-bottom: 2rem;
}

.hero-header {
  padding: 2rem;
}

.header-content h1 {
  font-size: 2.5rem;
  font-weight: 700;
  color: #2d3748;
  margin-bottom: 0.5rem;
}

.header-content p {
  font-size: 1.2rem;
  color: #4a5568;
  margin: 0;
}

.back-button {
  background: linear-gradient(135deg, #4299e1 0%, #3182ce 100%);
  color: white;
  border: none;
  border-radius: 12px;
  padding: 0.75rem 1.5rem;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin-bottom: 1.5rem;
  transition: all 0.3s ease;
}

.back-button:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(66, 153, 225, 0.4);
}

.loading-state {
  text-align: center;
  padding: 3rem;
  color: #4a5568;
}

.spinner {
  width: 40px;
  height: 40px;
  border: 4px solid #e2e8f0;
  border-top: 4px solid #4299e1;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin: 0 auto 1rem;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.add-student-section {
  padding: 2rem;
}

.add-student-section h3 {
  font-size: 1.5rem;
  font-weight: 600;
  color: #2d3748;
  margin-bottom: 1.5rem;
}

.student-input-group {
  display: grid;
  grid-template-columns: 1fr 1fr auto;
  gap: 1rem;
  align-items: end;
}

.form-group {
  display: flex;
  flex-direction: column;
}

.form-group label {
  font-weight: 600;
  color: #4a5568;
  margin-bottom: 0.5rem;
  font-size: 0.9rem;
}

.form-group input {
  padding: 0.875rem 1rem;
  border: 2px solid #e2e8f0;
  border-radius: 12px;
  font-size: 1rem;
  transition: all 0.3s ease;
  background: white;
}

.form-group input:focus {
  outline: none;
  border-color: #4299e1;
  box-shadow: 0 0 0 3px rgba(66, 153, 225, 0.1);
}

.form-group input:disabled {
  background: #f7fafc;
  color: #a0aec0;
  cursor: not-allowed;
}

.add-student-btn {
  background: linear-gradient(135deg, #48bb78 0%, #38a169 100%);
  color: white;
  border: none;
  border-radius: 12px;
  padding: 0.875rem 1.5rem;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  transition: all 0.3s ease;
  white-space: nowrap;
}

.add-student-btn:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(72, 187, 120, 0.4);
}

.add-student-btn:disabled {
  opacity: 0.6;
  cursor: not-allowed;
  transform: none;
}

.spinner-icon {
  animation: spin 1s linear infinite;
}

.students-list {
  padding: 2rem;
}

.list-header {
  margin-bottom: 2rem;
}

.list-header h3 {
  font-size: 1.5rem;
  font-weight: 600;
  color: #2d3748;
  margin: 0;
}

.empty-state {
  text-align: center;
  padding: 4rem 2rem;
  color: #718096;
}

.empty-icon {
  opacity: 0.5;
  margin-bottom: 1rem;
}

.empty-state h4 {
  font-size: 1.25rem;
  font-weight: 600;
  margin-bottom: 0.5rem;
  color: #4a5568;
}

.student-cards {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 1.5rem;
}

.student-card {
  background: white;
  border: 2px solid #e2e8f0;
  border-radius: 16px;
  padding: 1.5rem;
  transition: all 0.3s ease;
  position: relative;
  display: flex;
  align-items: center;
  gap: 1rem;
}

.student-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
  border-color: #cbd5e0;
}

.student-avatar {
  width: 60px;
  height: 60px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  flex-shrink: 0;
}

.student-info {
  flex-grow: 1;
  min-width: 0;
}

.student-info h4 {
  font-size: 1.1rem;
  font-weight: 600;
  color: #2d3748;
  margin: 0 0 0.25rem 0;
  word-wrap: break-word;
}

.student-info p {
  color: #4a5568;
  margin: 0 0 0.5rem 0;
  font-size: 0.9rem;
  word-wrap: break-word;
}

.join-date {
  color: #718096;
  font-size: 0.8rem;
}

.remove-student-btn {
  background: #fed7d7;
  color: #c53030;
  border: 2px solid #feb2b2;
  border-radius: 8px;
  padding: 0.5rem;
  cursor: pointer;
  transition: all 0.3s ease;
  flex-shrink: 0;
}

.remove-student-btn:hover:not(:disabled) {
  background: #fc8181;
  color: white;
  border-color: #f56565;
}

.remove-student-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
  padding: 1rem;
}

.modal-content {
  background: white;
  border-radius: 20px;
  padding: 2rem;
  max-width: 400px;
  width: 100%;
  text-align: center;
  position: relative;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
}

.delete-modal .warning-icon {
  color: #ed8936;
  margin-bottom: 1rem;
}

.delete-modal h3 {
  font-size: 1.5rem;
  font-weight: 600;
  color: #2d3748;
  margin-bottom: 1rem;
}

.delete-modal p {
  color: #4a5568;
  margin-bottom: 1rem;
  line-height: 1.6;
}

.warning-text {
  color: #e53e3e !important;
  font-weight: 600;
  font-size: 0.9rem;
}

.modal-actions {
  display: flex;
  gap: 1rem;
  justify-content: center;
  margin-top: 2rem;
}

.cancel-btn {
  background: #e2e8f0;
  color: #4a5568;
  border: 2px solid #cbd5e0;
  border-radius: 12px;
  padding: 0.75rem 1.5rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
}

.cancel-btn:hover {
  background: #cbd5e0;
}

.delete-btn {
  background: linear-gradient(135deg, #e53e3e 0%, #c53030 100%);
  color: white;
  border: none;
  border-radius: 12px;
  padding: 0.75rem 1.5rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.delete-btn:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(229, 62, 62, 0.4);
}

.delete-btn:disabled {
  opacity: 0.6;
  cursor: not-allowed;
  transform: none;
}

.success-toast {
  position: fixed;
  top: 2rem;
  right: 2rem;
  background: linear-gradient(135deg, #48bb78 0%, #38a169 100%);
  color: white;
  padding: 1rem 1.5rem;
  border-radius: 12px;
  box-shadow: 0 8px 25px rgba(72, 187, 120, 0.4);
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-weight: 600;
  z-index: 1100;
  animation: slideIn 0.3s ease;
}

@keyframes slideIn {
  from {
    transform: translateX(100%);
    opacity: 0;
  }
  to {
    transform: translateX(0);
    opacity: 1;
  }
}

.error-message {
  background: linear-gradient(135deg, #fc8181 0%, #e53e3e 100%);
  color: white;
  padding: 1rem 1.5rem;
  border-radius: 12px;
  margin-top: 1rem;
  font-weight: 600;
  text-align: center;
}

@media (max-width: 768px) {
  .page-container {
    padding: 1rem 0.5rem;
  }

  .hero-header {
    padding: 1.5rem;
  }

  .header-content h1 {
    font-size: 2rem;
  }

  .student-input-group {
    grid-template-columns: 1fr;
    gap: 1rem;
  }

  .add-student-btn {
    justify-self: start;
  }

  .student-cards {
    grid-template-columns: 1fr;
  }

  .success-toast {
    top: 1rem;
    right: 1rem;
    left: 1rem;
  }
}
</style>