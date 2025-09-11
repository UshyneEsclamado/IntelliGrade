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
          <h1>Edit Class</h1>
          <p>Update your class details.</p>
        </div>
      </div>

      <div v-if="loading" class="loading-state">
        <div class="spinner"></div>
        <p>Loading class details...</p>
      </div>

      <form v-else @submit.prevent="updateClass" class="class-form card-box">
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
          <button type="button" @click="goBack" class="cancel-btn" :disabled="submitting">
            Cancel
          </button>
          <button type="submit" class="submit-btn" :disabled="submitting">
            <svg v-if="submitting" class="spinner-icon" width="20" height="20" viewBox="0 0 24 24">
              <circle cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4" fill="none" opacity="0.25"/>
              <path d="M4 12a8 8 0 0 1 8-8" stroke="currentColor" stroke-width="4" fill="none"/>
            </svg>
            {{ submitting ? 'Updating...' : 'Update Class' }}
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
        <h3>Class Updated Successfully!</h3>
        <p>Your class details have been updated.</p>
        <button @click="closeModal" class="modal-ok-btn">OK</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRouter, useRoute } from 'vue-router';
import { supabase } from '../../supabase';

const router = useRouter();
const route = useRoute();

const className = ref('');
const classSubject = ref('');
const showModal = ref(false);
const error = ref('');
const submitting = ref(false);
const loading = ref(true);

const props = defineProps({
  id: String
});

const goBack = () => {
  router.push({ name: 'MyClasses' });
};

const fetchClassDetails = async () => {
  try {
    loading.value = true;
    error.value = '';
    
    const { data: { user } } = await supabase.auth.getUser();
    if (!user) {
      router.push('/login');
      return;
    }

    const { data, error: fetchError } = await supabase
      .from('classes')
      .select('*')
      .eq('id', props.id)
      .eq('teacher_id', user.id)
      .single();

    if (fetchError) throw fetchError;

    if (data) {
      className.value = data.name;
      classSubject.value = data.subject;
    }
  } catch (err) {
    console.error('Error fetching class details:', err);
    error.value = 'Failed to load class details. Please try again.';
  } finally {
    loading.value = false;
  }
};

const updateClass = async () => {
  error.value = '';
  
  if (!className.value.trim() || !classSubject.value.trim()) {
    error.value = 'Please fill in all fields.';
    return;
  }

  submitting.value = true;
  
  try {
    const { data: { user }, error: userError } = await supabase.auth.getUser();
    
    if (userError) throw userError;
    
    if (!user) {
      error.value = 'You must be logged in to update a class.';
      router.push('/login');
      return;
    }

    const { error: updateError } = await supabase
      .from('classes')
      .update({
        name: className.value.trim(),
        subject: classSubject.value.trim()
      })
      .eq('id', props.id)
      .eq('teacher_id', user.id);

    if (updateError) {
      console.error('Update error:', updateError);
      throw updateError;
    }

    showModal.value = true;

  } catch (err) {
    console.error('Update class error:', err);
    
    if (err.code === '23505') {
      error.value = 'A class with this name already exists.';
    } else if (err.code === 'PGRST301' || err.message?.includes('JWT')) {
      error.value = 'Authentication error. Please log in again.';
      setTimeout(() => router.push('/login'), 2000);
    } else if (err.message?.includes('permission')) {
      error.value = 'You do not have permission to update this class.';
    } else {
      error.value = err.message || 'Failed to update class. Please try again.';
    }
  } finally {
    submitting.value = false;
  }
};

const closeModal = () => {
  showModal.value = false;
  router.push({ 
    name: 'MyClasses', 
    query: { updated: Date.now() } 
  });
};

onMounted(() => {
  fetchClassDetails();
});
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

.loading-state {
  text-align: center;
  padding: 4rem 2rem;
}

.spinner {
  width: 40px;
  height: 40px;
  border: 4px solid rgba(61, 141, 122, 0.2);
  border-left: 4px solid #3D8D7A;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin: 0 auto 1rem;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
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
  justify-content: space-between;
  gap: 1rem;
  margin-top: 1rem;
}

.cancel-btn {
  background: #6c757d;
  color: white;
  border: none;
  padding: 1rem 2rem;
  border-radius: 16px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s;
  min-width: 120px;
}

.cancel-btn:hover:not(:disabled) {
  background: #5a6268;
  transform: translateY(-1px);
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

.submit-btn:disabled, .cancel-btn:disabled {
  opacity: 0.7;
  cursor: not-allowed;
  transform: none;
}

.spinner-icon {
  animation: spin 1s linear infinite;
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
  
  .form-actions {
    flex-direction: column-reverse;
  }
  
  .modal-content {
    padding: 2rem;
  }
}
</style>