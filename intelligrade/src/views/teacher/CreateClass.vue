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
          <input type="text" id="class-name" v-model="className" required>
        </div>
        <div class="form-group">
          <label for="class-subject">Subject</label>
          <input type="text" id="class-subject" v-model="classSubject" required>
        </div>
        
        <div class="form-actions">
          <button type="submit" class="submit-btn">
            Create Class
          </button>
        </div>
      </form>
    </div>

    <div v-if="showModal" class="modal-overlay" @click.self="closeModal">
      <div class="modal-content">
        <svg class="success-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor">
            <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/>
        </svg>
        <h3>Successfully Created Class!</h3>
        <p>You have successfully added **{{ className }}** to your list of classes.</p>
        <button @click="closeModal" class="modal-ok-btn">OK</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();

const className = ref('');
const classSubject = ref('');
const showModal = ref(false);

const goBack = () => {
  router.push({ name: 'MyClasses' });
};

const submitClass = async () => {
  if (!className.value || !classSubject.value) {
    alert('Please fill in all fields.');
    return;
  }

  // Simulating API call
  console.log('Creating new class:', {
    name: className.value,
    subject: classSubject.value,
  });

  // Display modal on success
  showModal.value = true;

  // Automatically redirect after 3 seconds
  setTimeout(() => {
    router.push({ name: 'MyClasses' });
  }, 3000); 
};

const closeModal = () => {
  showModal.value = false;
  router.push({ name: 'MyClasses' });
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
}

input[type="text"] {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid #ccc;
  border-radius: 8px;
  font-size: 1rem;
  transition: border-color 0.3s;
}

input:focus {
  outline: none;
  border-color: #3D8D7A;
  box-shadow: 0 0 0 3px rgba(61, 141, 122, 0.2);
}

.form-actions {
  display: flex;
  justify-content: flex-end;
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
}

.submit-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 16px 48px rgba(61, 141, 122, 0.3);
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
  z-index: 100;
}

.modal-content {
  background: #fff;
  border-radius: 24px;
  padding: 3rem;
  text-align: center;
  box-shadow: 0 16px 64px rgba(61, 141, 122, 0.3);
  max-width: 500px;
  width: 90%;
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
</style>