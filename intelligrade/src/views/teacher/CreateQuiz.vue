<template>
  <div class="page-container">
    <div class="main-wrapper">
      <div class="hero-header card-box">
        <div class="header-content">
          <button @click="goBack" class="back-button">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
              <path d="M10 19l-7-7 7-7m-7 7h18"></path>
            </svg>
            Back to Class
          </button>
          <h1>Create New Quiz</h1>
          <p>For class: **{{ className }}**</p>
        </div>
      </div>

      <form @submit.prevent="submitQuiz" class="quiz-form card-box">
        <div class="form-group">
          <label for="quiz-title">Quiz Title</label>
          <input type="text" id="quiz-title" v-model="quizTitle" required>
        </div>

        <div class="questions-list">
          <div v-for="(question, index) in questions" :key="index" class="question-item">
            <h4>Question {{ index + 1 }}</h4>
            <div class="form-group">
              <label :for="'question-' + index">Question Text</label>
              <textarea :id="'question-' + index" v-model="question.text" required></textarea>
            </div>
            <div class="form-group">
              <label :for="'answer-' + index">Answer Key</label>
              <input type="text" :id="'answer-' + index" v-model="question.answer" required>
            </div>
            <button type="button" class="remove-question-btn" @click="removeQuestion(index)">&times; Remove</button>
          </div>
        </div>
        
        <div class="form-actions">
          <button type="button" class="add-question-btn" @click="addQuestion">
            Add New Question
          </button>
          <button type="submit" class="submit-quiz-btn">
            Create Quiz
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRouter, useRoute } from 'vue-router';

const router = useRouter();
const route = useRoute();
const classId = ref(route.params.classId);
const className = ref('');

const quizTitle = ref('');
const questions = ref([
  { text: '', answer: '' } // Start with one empty question
]);

// Mock function to fetch class name
const fetchClassName = () => {
  if (classId.value == 1) {
    className.value = 'Grade 10 - Rizal';
  } else if (classId.value == 2) {
    className.value = 'Grade 9 - Bonifacio';
  }
};

const addQuestion = () => {
  questions.value.push({ text: '', answer: '' });
};

const removeQuestion = (index) => {
  if (questions.value.length > 1) {
    questions.value.splice(index, 1);
  } else {
    alert('A quiz must have at least one question.');
  }
};

const submitQuiz = async () => {
  // Check if all fields are filled
  if (!quizTitle.value || questions.value.some(q => !q.text || !q.answer)) {
    alert('Please fill in all the fields.');
    return;
  }

  // Here you would send the data to your backend API
  const quizData = {
    classId: classId.value,
    title: quizTitle.value,
    questions: questions.value
  };

  console.log('Submitting new quiz:', quizData);
  alert('Quiz created successfully!');

  // Redirect back to class details page after submission
  router.push({ name: 'ClassDetails', params: { id: classId.value } });
};

const goBack = () => {
  router.back();
};

onMounted(() => {
  fetchClassName();
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

.quiz-form {
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

input[type="text"], textarea {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid #ccc;
  border-radius: 8px;
  font-size: 1rem;
  transition: border-color 0.3s;
}

input:focus, textarea:focus {
  outline: none;
  border-color: #3D8D7A;
  box-shadow: 0 0 0 3px rgba(61, 141, 122, 0.2);
}

.questions-list {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.question-item {
  background: #f8fff6;
  padding: 1.5rem;
  border-radius: 16px;
  border: 1px solid rgba(61, 141, 122, 0.1);
  position: relative;
}

.question-item h4 {
  color: #3D8D7A;
  margin-top: 0;
  margin-bottom: 1rem;
}

.remove-question-btn {
  position: absolute;
  top: 1rem;
  right: 1rem;
  background: #ff4d4f;
  color: #fff;
  border: none;
  border-radius: 8px;
  padding: 0.5rem 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s;
}

.remove-question-btn:hover {
  background: #e60000;
}

.form-actions {
  display: flex;
  gap: 1.5rem;
  justify-content: flex-end;
  margin-top: 1.5rem;
}

.add-question-btn {
  background: #A3D1C6;
  color: #3D8D7A;
  border: none;
  padding: 1rem 2rem;
  border-radius: 16px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s;
}

.add-question-btn:hover {
  background: #8ec3b2;
}

.submit-quiz-btn {
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

.submit-quiz-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 16px 48px rgba(61, 141, 122, 0.3);
}
</style>