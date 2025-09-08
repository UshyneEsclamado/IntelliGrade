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

      <!-- Modal for Student Details -->
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
import { ref, onMounted } from 'vue';
import { useRouter, useRoute } from 'vue-router';

const router = useRouter();
const route = useRoute();

const assessmentId = route.params.id; // Get the assessmentId from the route

const assessment = ref({
  title: 'Loading...',
  maxScore: 0,
  results: []
});

const showModal = ref(false);
const selectedStudent = ref(null);

// Fetch assessment results from the backend
const fetchAssessmentResults = async () => {
  try {
    const response = await fetch(`http://127.0.0.1:8000/assessment/${assessmentId}/results`);
    if (response.ok) {
      const data = await response.json();
      assessment.value = data;
    } else {
      console.error('Failed to fetch assessment results');
    }
  } catch (error) {
    console.error('Error fetching results:', error);
  }
};

// Go back to the previous page
const goBack = () => {
  router.back();
};

// Show student details in a modal
const showStudentDetails = (result) => {
  selectedStudent.value = result;
  showModal.value = true;
};

// Close the modal
const closeModal = () => {
  showModal.value = false;
  selectedStudent.value = null;
};

// Fetch assessment data when component is mounted
onMounted(() => {
  fetchAssessmentResults();
});
</script>

<style scoped>
/* Styles for the page */
</style>
