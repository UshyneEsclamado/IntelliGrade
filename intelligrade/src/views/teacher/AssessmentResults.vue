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
          <h1>{{ assessment.title }} Results</h1>
          <p>Detailed scores and AI feedback for this assessment.</p>
        </div>
      </div>

      <section class="results-table-section card-box">
        <div class="section-header">
          <h2>Student Results</h2>
          <p class="section-subtitle">A summary of student performance graded by AI.</p>
        </div>
        <div class="table-container">
          <table class="results-table">
            <thead>
              <tr>
                <th>Student</th>
                <th>Score</th>
                <th>Feedback</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="result in assessment.results" :key="result.studentName">
                <td>{{ result.studentName }}</td>
                <td class="score">{{ result.score }} / {{ assessment.maxScore }}</td>
                <td>{{ result.feedback }}</td>
                <td>
                  <button @click="showStudentDetails(result)" class="view-details-btn">
                    View Details
                  </button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </section>

      <div v-if="showModal" class="modal-overlay" @click.self="closeModal">
        <div class="modal-content">
          <button @click="closeModal" class="modal-close-btn">&times;</button>
          <h3>{{ selectedStudent.studentName }}'s Details</h3>
          <div class="details-container">
            <div class="score-card">
              <h4>Final Score</h4>
              <p>{{ selectedStudent.score }} / {{ assessment.maxScore }}</p>
            </div>
            <div class="feedback-card">
              <h4>AI Feedback</h4>
              <p>{{ selectedStudent.feedback }}</p>
            </div>
            <div class="answers-card">
              <h4>Answers</h4>
              <div v-for="(answer, index) in selectedStudent.answers" :key="index" class="answer-item">
                <p class="question">Q{{ index + 1 }}: {{ answer.question }}</p>
                <p class="your-answer">Your Answer: <span>{{ answer.studentAnswer }}</span></p>
                <p class="correct-answer">Correct Answer: <span>{{ answer.correctAnswer }}</span></p>
              </div>
            </div>
          </div>
        </div>
      </div>

    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter, useRoute } from 'vue-router';

const router = useRouter();
const route = useRoute();

const assessmentId = route.params.id;

const assessment = ref({
  id: assessmentId,
  title: 'Algebra Quiz 1',
  maxScore: 20,
  results: [
    {
      studentName: 'Juan Dela Cruz',
      score: 18,
      feedback: 'Excellent work! Your understanding of algebraic expressions is strong. Review the concept of factoring polynomials for a perfect score.',
      answers: [
        { question: 'What is x + 2 = 5?', studentAnswer: '3', correctAnswer: '3' },
        { question: 'Factor x^2 - 4.', studentAnswer: '(x-2)(x+2)', correctAnswer: '(x-2)(x+2)' },
        { question: 'Simplify 2x + 3x.', studentAnswer: '5x', correctAnswer: '5x' },
        { question: 'Solve for y in 2y = 10.', studentAnswer: '5', correctAnswer: '5' }
      ]
    },
    {
      studentName: 'Maria Santos',
      score: 15,
      feedback: 'Good effort, Maria. You have a solid grasp on most topics. Pay close attention to the order of operations in your next quiz.',
      answers: [
        { question: 'What is x + 2 = 5?', studentAnswer: '3', correctAnswer: '3' },
        { question: 'Factor x^2 - 4.', studentAnswer: '(x-2)^2', correctAnswer: '(x-2)(x+2)' },
        { question: 'Simplify 2x + 3x.', studentAnswer: '5x', correctAnswer: '5x' },
        { question: 'Solve for y in 2y = 10.', studentAnswer: '5', correctAnswer: '5' }
      ]
    }
  ]
});

const showModal = ref(false);
const selectedStudent = ref(null);

const goBack = () => {
  router.back();
};

const showStudentDetails = (result) => {
  selectedStudent.value = result;
  showModal.value = true;
};

const closeModal = () => {
  showModal.value = false;
  selectedStudent.value = null;
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600&display=swap');

.page-container {
  padding: 2rem 5%;
  font-family: 'Inter', sans-serif;
  background: linear-gradient(135deg, #FBFFE4 0%, #B3D8A8 50%, #A3D1C6 100%);
  min-height: 100vh;
  position: relative;
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

.hero-header h1 {
  font-size: 2.5rem;
  font-weight: 800;
  color: #3D8D7A;
  margin-top: 1rem;
}

.hero-header p {
  font-size: 1.1rem;
  color: #666;
  font-weight: 500;
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
}

.back-button:hover {
  color: #2e6b5c;
  transform: translateX(-5px);
}

.section-header h2 {
  font-size: 1.8rem;
  font-weight: 700;
  color: #3D8D7A;
  margin-bottom: 0.5rem;
}

.section-subtitle {
  color: #777;
  font-size: 1rem;
  font-weight: 500;
  margin-bottom: 1.5rem;
}

.results-table-section {
  overflow-x: auto;
}

.results-table {
  width: 100%;
  border-collapse: collapse;
}

.results-table th, .results-table td {
  padding: 1.2rem 1rem;
  border-bottom: 1px solid rgba(61, 141, 122, 0.1);
  text-align: left;
}

.results-table th {
  background-color: #f0f8f5;
  color: #3D8D7A;
  font-weight: 700;
  text-transform: uppercase;
  font-size: 0.85rem;
  letter-spacing: 0.5px;
}

.results-table tbody tr:hover {
  background-color: rgba(61, 141, 122, 0.05);
}

.score {
  font-weight: 600;
  color: #3D8D7A;
}

.view-details-btn {
  background: #A3D1C6;
  color: #3D8D7A;
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 12px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s;
}

.view-details-btn:hover {
  background: #8ec3b2;
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
  padding: 1rem;
}

.modal-content {
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(30px);
  border-radius: 24px;
  padding: 2.5rem;
  width: 100%;
  max-width: 800px;
  position: relative;
  box-shadow: 0 16px 64px rgba(61, 141, 122, 0.3);
  max-height: 90vh;
  overflow-y: auto;
}

.modal-close-btn {
  position: absolute;
  top: 1.5rem;
  right: 1.5rem;
  background: none;
  border: none;
  font-size: 2rem;
  color: #3D8D7A;
  cursor: pointer;
}

.modal-content h3 {
  font-size: 1.8rem;
  font-weight: 700;
  color: #3D8D7A;
  margin-bottom: 2rem;
}

.details-container {
  display: grid;
  gap: 1.5rem;
}

.score-card, .feedback-card, .answers-card {
  background: rgba(251, 255, 228, 0.7);
  border: 1px solid rgba(61, 141, 122, 0.15);
  border-radius: 20px;
  padding: 1.5rem;
  box-shadow: 0 4px 16px rgba(61, 141, 122, 0.1);
}

.score-card h4, .feedback-card h4, .answers-card h4 {
  font-size: 1.2rem;
  font-weight: 600;
  color: #3D8D7A;
  margin-bottom: 0.5rem;
}

.answers-card {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.answer-item {
  border-bottom: 1px dashed rgba(61, 141, 122, 0.2);
  padding-bottom: 1.5rem;
}

.answer-item:last-child {
  border-bottom: none;
}

.question {
  font-weight: 600;
  color: #444;
  margin-bottom: 0.5rem;
}

.your-answer span, .correct-answer span {
  font-family: 'JetBrains Mono', monospace;
  font-weight: 500;
  background-color: #e6f3ef;
  padding: 0.25rem 0.5rem;
  border-radius: 8px;
}

.correct-answer span {
  color: #3D8D7A;
}

@media (max-width: 768px) {
  .results-table th, .results-table td {
    padding: 0.75rem 0.5rem;
    font-size: 0.8rem;
  }
}
</style>