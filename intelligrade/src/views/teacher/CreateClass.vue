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
          <h1>Create New Class</h1>
          <p>Fill in the details below to create a new class.</p>
        </div>
      </div>

      <form @submit.prevent="submitClass" class="class-form card-box">
        <div class="form-group">
          <label for="class-name">Class Name</label>
          <input 
            type="text" 
            id="class-name" 
            v-model="className" 
            required 
            :disabled="submitting"
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
            :disabled="submitting"
            placeholder="e.g., Mathematics"
          >
        </div>
        
        <div class="form-actions">
          <button type="submit" class="submit-btn" :disabled="submitting">
            <svg v-if="submitting" class="spinner-icon" width="20" height="20" viewBox="0 0 24 24">
              <circle cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4" fill="none" opacity="0.25"/>
              <path d="M4 12a8 8 0 0 1 8-8" stroke="currentColor" stroke-width="4" fill="none"/>
            </svg>
            {{ submitting ? 'Creating...' : 'Create Class' }}
          </button>
        </div>
      </form>

      <div v-if="error" class="error-message">
        {{ error }}
      </div>
    </div>

    <div v-if="showModal" class="modal-overlay" @click.self="closeModal">
      <div class="modal-content">
        <svg class="success-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor">
          <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/>
        </svg>
        <h3>Successfully Created Class!</h3>
        <p>You have successfully added <strong>{{ className }}</strong> to your list of classes.</p>
        <button @click="closeModal" class="modal-ok-btn">OK</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { supabase } from '../../supabase';

const router = useRouter();

const className = ref('');
const classSubject = ref('');
const showModal = ref(false);
const error = ref('');
const submitting = ref(false);

const goBack = () => {
  router.push({ name: 'MyClasses' });
};

const submitClass = async () => {
  error.value = '';
  
  // Basic validation
  if (!className.value.trim() || !classSubject.value.trim()) {
    error.value = 'Please fill in all fields.';
    return;
  }

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
    const { data, error: insertError } = await supabase
      .from('classes')
      .insert([{
        name: className.value.trim(),
        subject: classSubject.value.trim(),
        teacher_id: user.id,
        students: 0,
        assessments: 0,
        created_at: new Date().toISOString()
      }])
      .select()
      .single();

    if (insertError) {
      console.error('Insert error:', insertError);
      throw insertError;
    }

    console.log('Class created successfully:', data);
    
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

input[type="text"] {
  width: 100%;
  padding: 1rem;
  border: 2px solid #e1e1e1;
  border-radius: 12px;
  font-size: 1rem;
  transition: all 0.3s;
  background: #fff;
  box-sizing: border-box;
}

input[type="text"]:focus {
  outline: none;
  border-color: #3D8D7A;
  box-shadow: 0 0 0 3px rgba(61, 141, 122, 0.2);
}

input[type="text"]:disabled {
  background: #f5f5f5;
  color: #999;
  cursor: not-allowed;
}

input[type="text"]::placeholder {
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
  min-width: 140px;
  justify-content: center;
}

.submit-btn:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 16px 48px rgba(61, 141, 122, 0.3);
}

.submit-btn:disabled {
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
  
  .modal-content {
    padding: 2rem;
  }
}
</style>