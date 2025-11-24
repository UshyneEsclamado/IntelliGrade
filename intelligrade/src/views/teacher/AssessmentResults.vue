<template>
  <div class="page-container" :class="{ 'dark-mode': isDarkMode }">
    <div class="main-wrapper">
      <!-- Enhanced Header Section -->
      <section class="section-header-card">
        <div class="floating-shapes">
          <div class="shape shape-1"></div>
          <div class="shape shape-2"></div>
          <div class="shape shape-3"></div>
          <div class="shape shape-4"></div>
        </div>
        
        <div class="header-content">
          <button @click="goBack" class="back-button">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M10 19l-7-7 7-7m-7 7h18"></path>
            </svg>
            Back to Classes
          </button>
          
          <div class="hero-header">
            <h1>{{ assessment.title }} Results</h1>
            <p class="hero-subtitle">Detailed scores and AI feedback for this assessment</p>
          </div>
          
          <div class="section-info">
            <div class="info-badge assessment">
              <div class="icon">📊</div>
              <div class="text">
                <span class="label">Total Students</span>
                <span class="value">{{ assessment.results.length }}</span>
              </div>
            </div>
            <div class="info-badge score">
              <div class="icon">🎯</div>
              <div class="text">
                <span class="label">Max Score</span>
                <span class="value">{{ assessment.maxScore }}</span>
              </div>
            </div>
            <div class="info-badge average">
              <div class="icon">📈</div>
              <div class="text">
                <span class="label">Class Average</span>
                <span class="value">{{ calculateAverage() }}%</span>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- Results Table Section -->
      <section class="content-card">
        <div class="card-header">
          <h3>Student Results</h3>
          <p class="card-subtitle">AI-graded assessment results with detailed feedback</p>
        </div>
        
        <div class="table-container">
          <table class="results-table">
            <thead>
              <tr>
                <th>Student</th>
                <th>Score</th>
                <th>Percentage</th>
                <th>Feedback</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="result in assessment.results" :key="result.studentName" class="table-row">
                <td class="student-name">
                  <div class="student-avatar">{{ result.studentName.charAt(0) }}</div>
                  {{ result.studentName }}
                </td>
                <td class="score">{{ result.score }} / {{ assessment.maxScore }}</td>
                <td class="percentage">
                  <div class="progress-bar">
                    <div class="progress-fill" :style="{ width: calculatePercentage(result.score) + '%' }"></div>
                  </div>
                  <span class="percentage-text">{{ calculatePercentage(result.score) }}%</span>
                </td>
                <td class="feedback">{{ truncateFeedback(result.feedback) }}</td>
                <td class="actions">
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
      <div v-if="showModal && selectedStudent" class="modal-overlay" @click.self="closeModal">
        <div class="modal-content">
          <div class="modal-header">
            <h3>{{ selectedStudent.studentName }}'s Detailed Results</h3>
            <button @click="closeModal" class="modal-close-btn">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                <path d="M18 6L6 18M6 6l12 12"></path>
              </svg>
            </button>
          </div>
          
          <div class="modal-body">
            <div class="details-grid">
              <div class="score-card">
                <div class="card-icon">🎯</div>
                <h4>Final Score</h4>
                <p class="score-value">{{ selectedStudent.score }} / {{ assessment.maxScore }}</p>
                <p class="percentage-value">{{ calculatePercentage(selectedStudent.score) }}%</p>
              </div>
              
              <div class="feedback-card">
                <div class="card-icon">💬</div>
                <h4>AI Feedback</h4>
                <p class="feedback-text">{{ selectedStudent.feedback }}</p>
              </div>
            </div>
            
            <div class="answers-section">
              <h4>Detailed Answers</h4>
              <div class="answers-list">
                <div v-for="(answer, index) in selectedStudent.answers" :key="index" class="answer-item">
                  <div class="question-header">
                    <span class="question-number">Q{{ index + 1 }}</span>
                    <span class="question-text">{{ answer.question }}</span>
                  </div>
                  <div class="answer-comparison">
                    <div class="student-answer">
                      <label>Student Answer:</label>
                      <p>{{ answer.studentAnswer }}</p>
                    </div>
                    <div class="correct-answer">
                      <label>Correct Answer:</label>
                      <p>{{ answer.correctAnswer }}</p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { useRouter, useRoute } from 'vue-router';
import { useDarkMode } from '../../composables/useDarkMode.js';

// Dark mode
const { isDarkMode, initDarkMode } = useDarkMode();

// TypeScript interfaces
interface StudentResult {
  studentName: string;
  score: number;
  feedback: string;
  answers: {
    question: string;
    studentAnswer: string;
    correctAnswer: string;
  }[];
}

interface Assessment {
  title: string;
  maxScore: number;
  results: StudentResult[];
}

const router = useRouter();
const route = useRoute();

const assessmentId = route.params.id; // Get the assessmentId from the route

const assessment = ref<Assessment>({
  title: 'Loading...',
  maxScore: 0,
  results: []
});

const showModal = ref(false);
const selectedStudent = ref<StudentResult | null>(null);

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

// Calculate percentage for a given score
const calculatePercentage = (score: number) => {
  if (assessment.value.maxScore === 0) return 0;
  return Math.round((score / assessment.value.maxScore) * 100);
};

// Calculate class average
const calculateAverage = () => {
  if (assessment.value.results.length === 0) return 0;
  const total = assessment.value.results.reduce((sum: number, result: StudentResult) => sum + result.score, 0);
  const average = total / assessment.value.results.length;
  return Math.round((average / assessment.value.maxScore) * 100);
};

// Truncate feedback for table display
const truncateFeedback = (feedback: string) => {
  if (feedback.length > 50) {
    return feedback.substring(0, 50) + '...';
  }
  return feedback;
};

// Go back to the previous page
const goBack = () => {
  router.back();
};

// Show student details in a modal
const showStudentDetails = (result: StudentResult) => {
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
/* Enhanced Student Folder Design Pattern */
.page-container {
  min-height: 100vh;
  background: var(--body-background);
  padding: 2rem 5%;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', sans-serif;
}

.main-wrapper {
  max-width: 1400px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

/* Enhanced Header Section */
.section-header-card {
  background: var(--card-background);
  backdrop-filter: blur(20px);
  border: 1px solid var(--border-color);
  border-radius: 24px;
  padding: 3rem;
  position: relative;
  overflow: hidden;
  box-shadow: 
    0 20px 60px var(--shadow-medium),
    0 8px 30px var(--shadow-light),
    0 0 0 1px rgba(255, 255, 255, 0.3);
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.section-header-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 2px;
  background: linear-gradient(90deg, var(--primary-color), var(--accent-color), var(--primary-color));
  opacity: 0.8;
}

/* Floating Shapes */
.floating-shapes {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
  overflow: hidden;
}

.shape {
  position: absolute;
  border-radius: 50%;
  background: linear-gradient(135deg, var(--primary-color-alpha), var(--accent-color-alpha));
  animation: float 6s ease-in-out infinite;
}

.shape-1 {
  width: 120px;
  height: 120px;
  top: -60px;
  right: -60px;
  animation-delay: 0s;
}

.shape-2 {
  width: 80px;
  height: 80px;
  top: 50%;
  left: -40px;
  animation-delay: 1s;
}

.shape-3 {
  width: 100px;
  height: 100px;
  bottom: -50px;
  right: 20%;
  animation-delay: 2s;
}

.shape-4 {
  width: 60px;
  height: 60px;
  top: 20%;
  right: 15%;
  animation-delay: 3s;
}

@keyframes float {
  0%, 100% {
    transform: translateY(0px) rotate(0deg);
    opacity: 0.5;
  }
  50% {
    transform: translateY(-20px) rotate(180deg);
    opacity: 0.8;
  }
}

.header-content {
  position: relative;
  z-index: 2;
}

.back-button {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  background: transparent;
  color: var(--primary-color);
  border: none;
  font-weight: 600;
  font-size: 0.95rem;
  cursor: pointer;
  padding: 0.5rem 0;
  margin-bottom: 2rem;
  transition: all 0.3s ease;
  text-decoration: none;
}

.back-button:hover {
  color: var(--primary-color-dark);
  transform: translateX(-5px);
}

.hero-header {
  text-align: center;
  margin-bottom: 3rem;
}

.hero-header h1 {
  font-size: 2.5rem;
  font-weight: 800;
  color: var(--primary-color);
  margin: 0 0 1rem 0;
  background: linear-gradient(135deg, var(--primary-color), var(--accent-color));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.hero-subtitle {
  font-size: 1.1rem;
  color: var(--secondary-text-color);
  margin: 0;
  max-width: 600px;
  margin: 0 auto;
}

.section-info {
  display: flex;
  gap: 1.5rem;
  flex-wrap: wrap;
  justify-content: center;
}

.info-badge {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1rem 1.5rem;
  border-radius: 16px;
  font-size: 0.95rem;
  min-width: 150px;
  backdrop-filter: blur(10px);
  border: 1px solid var(--border-color);
  transition: all 0.3s ease;
}

.info-badge.assessment {
  background: linear-gradient(135deg, rgba(59, 130, 246, 0.1), rgba(147, 197, 253, 0.1));
  border-color: rgba(59, 130, 246, 0.2);
}

.info-badge.score {
  background: linear-gradient(135deg, rgba(16, 185, 129, 0.1), rgba(110, 231, 183, 0.1));
  border-color: rgba(16, 185, 129, 0.2);
}

.info-badge.average {
  background: linear-gradient(135deg, rgba(139, 92, 246, 0.1), rgba(196, 181, 253, 0.1));
  border-color: rgba(139, 92, 246, 0.2);
}

.info-badge .icon {
  font-size: 1.5rem;
}

.info-badge .text {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}

.info-badge .label {
  font-weight: 500;
  color: var(--secondary-text-color);
  font-size: 0.85rem;
}

.info-badge .value {
  font-weight: 700;
  color: var(--primary-text-color);
  font-size: 1.1rem;
}

/* Content Card */
.content-card {
  background: var(--card-background);
  backdrop-filter: blur(20px);
  border: 1px solid var(--border-color);
  border-radius: 24px;
  padding: 2.5rem;
  box-shadow: 
    0 20px 60px var(--shadow-medium),
    0 8px 30px var(--shadow-light),
    0 0 0 1px rgba(255, 255, 255, 0.3);
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.content-card:hover {
  transform: translateY(-2px);
  box-shadow: 
    0 25px 70px var(--shadow-medium),
    0 12px 40px var(--shadow-light),
    0 0 0 1px rgba(255, 255, 255, 0.4);
}

.card-header {
  margin-bottom: 2rem;
  text-align: center;
}

.card-header h3 {
  font-size: 1.75rem;
  font-weight: 700;
  color: var(--primary-text-color);
  margin: 0 0 0.5rem 0;
}

.card-subtitle {
  color: var(--secondary-text-color);
  font-size: 1rem;
  margin: 0;
}

/* Table Styling */
.table-container {
  overflow-x: auto;
  border-radius: 16px;
  border: 1px solid var(--border-color);
}

.results-table {
  width: 100%;
  border-collapse: collapse;
  background: var(--card-background);
}

.results-table thead {
  background: var(--primary-color);
  background: linear-gradient(135deg, var(--primary-color), var(--primary-color-dark));
}

.results-table th {
  padding: 1.25rem 1.5rem;
  text-align: left;
  font-weight: 600;
  color: white;
  font-size: 0.95rem;
  border: none;
}

.results-table th:first-child {
  border-top-left-radius: 16px;
}

.results-table th:last-child {
  border-top-right-radius: 16px;
}

.table-row {
  border-bottom: 1px solid var(--border-color);
  transition: all 0.3s ease;
}

.table-row:hover {
  background: var(--hover-background);
}

.results-table td {
  padding: 1.25rem 1.5rem;
  color: var(--primary-text-color);
  vertical-align: middle;
}

.student-name {
  display: flex;
  align-items: center;
  gap: 1rem;
  font-weight: 600;
}

.student-avatar {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: linear-gradient(135deg, var(--primary-color), var(--accent-color));
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 1.1rem;
}

.score {
  font-weight: 700;
  color: var(--primary-color);
}

.percentage {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.progress-bar {
  width: 80px;
  height: 8px;
  background: var(--border-color);
  border-radius: 4px;
  overflow: hidden;
}

.progress-fill {
  height: 100%;
  background: linear-gradient(90deg, var(--accent-color), var(--success-color));
  border-radius: 4px;
  transition: width 0.3s ease;
}

.percentage-text {
  font-weight: 600;
  color: var(--primary-text-color);
  font-size: 0.9rem;
}

.feedback {
  color: var(--secondary-text-color);
  max-width: 300px;
}

.view-details-btn {
  background: linear-gradient(135deg, var(--primary-color), var(--primary-color-light));
  color: white;
  border: none;
  padding: 0.6rem 1.2rem;
  border-radius: 12px;
  font-weight: 600;
  cursor: pointer;
  font-size: 0.9rem;
  transition: all 0.3s ease;
}

.view-details-btn:hover {
  transform: translateY(-1px);
  box-shadow: 0 8px 20px var(--primary-color-alpha);
}

/* Modal Styling */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  backdrop-filter: blur(5px);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
  padding: 2rem;
}

.modal-content {
  background: var(--card-background);
  border-radius: 24px;
  max-width: 800px;
  width: 100%;
  max-height: 90vh;
  overflow-y: auto;
  box-shadow: 
    0 25px 70px rgba(0, 0, 0, 0.3),
    0 12px 40px rgba(0, 0, 0, 0.2);
  border: 1px solid var(--border-color);
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 2rem 2.5rem 1rem;
  border-bottom: 1px solid var(--border-color);
}

.modal-header h3 {
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--primary-text-color);
  margin: 0;
}

.modal-close-btn {
  background: transparent;
  border: none;
  color: var(--secondary-text-color);
  cursor: pointer;
  padding: 0.5rem;
  border-radius: 8px;
  transition: all 0.3s ease;
}

.modal-close-btn:hover {
  background: var(--hover-background);
  color: var(--primary-text-color);
}

.modal-body {
  padding: 2rem 2.5rem;
}

.details-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2rem;
  margin-bottom: 2rem;
}

.score-card,
.feedback-card {
  background: var(--hover-background);
  padding: 2rem;
  border-radius: 16px;
  border: 1px solid var(--border-color);
  text-align: center;
}

.card-icon {
  font-size: 2.5rem;
  margin-bottom: 1rem;
}

.score-card h4,
.feedback-card h4 {
  font-size: 1.1rem;
  font-weight: 600;
  color: var(--secondary-text-color);
  margin: 0 0 1rem 0;
}

.score-value {
  font-size: 2rem;
  font-weight: 800;
  color: var(--primary-color);
  margin: 0;
}

.percentage-value {
  font-size: 1.2rem;
  font-weight: 600;
  color: var(--accent-color);
  margin: 0.5rem 0 0 0;
}

.feedback-text {
  color: var(--primary-text-color);
  line-height: 1.6;
  margin: 0;
}

.answers-section h4 {
  font-size: 1.3rem;
  font-weight: 700;
  color: var(--primary-text-color);
  margin: 0 0 1.5rem 0;
}

.answers-list {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.answer-item {
  background: var(--hover-background);
  padding: 1.5rem;
  border-radius: 12px;
  border: 1px solid var(--border-color);
}

.question-header {
  display: flex;
  gap: 0.75rem;
  margin-bottom: 1rem;
  align-items: flex-start;
}

.question-number {
  background: var(--primary-color);
  color: white;
  padding: 0.25rem 0.75rem;
  border-radius: 8px;
  font-weight: 700;
  font-size: 0.85rem;
  flex-shrink: 0;
}

.question-text {
  color: var(--primary-text-color);
  font-weight: 600;
  line-height: 1.5;
}

.answer-comparison {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
}

.student-answer,
.correct-answer {
  padding: 1rem;
  border-radius: 8px;
}

.student-answer {
  background: rgba(239, 68, 68, 0.1);
  border: 1px solid rgba(239, 68, 68, 0.2);
}

.correct-answer {
  background: rgba(16, 185, 129, 0.1);
  border: 1px solid rgba(16, 185, 129, 0.2);
}

.student-answer label,
.correct-answer label {
  font-weight: 600;
  font-size: 0.85rem;
  color: var(--secondary-text-color);
  display: block;
  margin-bottom: 0.5rem;
}

.student-answer p,
.correct-answer p {
  color: var(--primary-text-color);
  margin: 0;
  line-height: 1.4;
}

/* Responsive Design */
@media (max-width: 768px) {
  .page-container {
    padding: 1rem 3%;
  }

  .section-header-card,
  .content-card {
    padding: 2rem 1.5rem;
  }

  .hero-header h1 {
    font-size: 2rem;
  }

  .section-info {
    flex-direction: column;
    gap: 1rem;
  }

  .info-badge {
    min-width: unset;
  }

  .details-grid {
    grid-template-columns: 1fr;
  }

  .answer-comparison {
    grid-template-columns: 1fr;
  }

  .modal-overlay {
    padding: 1rem;
  }

  .modal-header,
  .modal-body {
    padding: 1.5rem;
  }

  .table-container {
    font-size: 0.9rem;
  }

  .results-table th,
  .results-table td {
    padding: 1rem;
  }
}

/* Dark Mode Styles */
.dark-mode .page-container {
  background: var(--bg-primary);
}

.dark-mode .section-header-card {
  background: rgba(17, 24, 39, 0.95);
  border: 1px solid rgba(255, 255, 255, 0.08);
  box-shadow: 
    0 4px 12px rgba(0, 0, 0, 0.25),
    0 2px 6px rgba(0, 0, 0, 0.15);
}

.dark-mode .back-button {
  background: rgba(75, 85, 99, 0.2);
  color: var(--secondary-text-color);
}

.dark-mode .back-button:hover {
  color: var(--accent-color);
}

.dark-mode .hero-header h1 {
  color: var(--primary-text-color);
}

.dark-mode .hero-subtitle {
  color: var(--secondary-text-color);
}

.dark-mode .info-badge.assessment {
  background: rgba(59, 130, 246, 0.15);
  border: 1px solid rgba(59, 130, 246, 0.3);
}

.dark-mode .info-badge.score {
  background: rgba(16, 185, 129, 0.15);
  border: 1px solid rgba(16, 185, 129, 0.3);
}

.dark-mode .info-badge.average {
  background: rgba(234, 179, 8, 0.15);
  border: 1px solid rgba(234, 179, 8, 0.3);
}

.dark-mode .info-badge .label {
  color: var(--secondary-text-color);
}

.dark-mode .info-badge .value {
  color: var(--primary-text-color);
}

.dark-mode .content-card {
  background: rgba(17, 24, 39, 0.95);
  border: 1px solid rgba(255, 255, 255, 0.08);
  box-shadow: 
    0 4px 12px rgba(0, 0, 0, 0.25),
    0 2px 6px rgba(0, 0, 0, 0.15);
}

.dark-mode .card-header h3 {
  color: var(--primary-text-color);
}

.dark-mode .card-subtitle {
  color: var(--secondary-text-color);
}

.dark-mode .results-table {
  background: rgba(17, 24, 39, 0.8);
  border: 1px solid rgba(255, 255, 255, 0.05);
}

.dark-mode .results-table th {
  background: rgba(31, 41, 55, 0.8);
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
  color: var(--primary-text-color);
}

.dark-mode .results-table td {
  border-bottom: 1px solid rgba(255, 255, 255, 0.05);
  color: var(--primary-text-color);
}

.dark-mode .table-row:hover {
  background: rgba(31, 41, 55, 0.6);
}

.dark-mode .student-avatar {
  background: var(--accent-color);
}

.dark-mode .progress-bar {
  background: rgba(75, 85, 99, 0.3);
}

.dark-mode .view-details-btn {
  background: rgba(75, 85, 99, 0.2);
  border: 1px solid rgba(255, 255, 255, 0.1);
  color: var(--secondary-text-color);
}

.dark-mode .view-details-btn:hover {
  background: rgba(75, 85, 99, 0.3);
  color: var(--primary-text-color);
}

.dark-mode .modal-overlay {
  background: rgba(0, 0, 0, 0.8);
}

.dark-mode .modal-content {
  background: rgba(17, 24, 39, 0.95);
  border: 1px solid rgba(255, 255, 255, 0.08);
  box-shadow: 
    0 20px 50px rgba(0, 0, 0, 0.5),
    0 10px 25px rgba(0, 0, 0, 0.3);
}

.dark-mode .modal-header h3 {
  color: var(--primary-text-color);
}

.dark-mode .modal-close-btn {
  background: rgba(75, 85, 99, 0.2);
  color: var(--secondary-text-color);
}

.dark-mode .modal-close-btn:hover {
  background: #ef4444;
  color: white;
}

.dark-mode .details-section h4 {
  color: var(--primary-text-color);
}

.dark-mode .detail-item .label {
  color: var(--secondary-text-color);
}

.dark-mode .detail-item .value {
  color: var(--primary-text-color);
}

.dark-mode .answers-section h5 {
  color: var(--primary-text-color);
}

.dark-mode .question-analysis {
  background: rgba(31, 41, 55, 0.8);
  border: 1px solid rgba(255, 255, 255, 0.05);
}

.dark-mode .question-text {
  color: var(--primary-text-color);
}

.dark-mode .student-answer label,
.dark-mode .correct-answer label {
  color: var(--secondary-text-color);
}

.dark-mode .student-answer p,
.dark-mode .correct-answer p {
  color: var(--primary-text-color);
}

/* Custom Scrollbar Styling - Green Theme */
::-webkit-scrollbar {
  width: 8px;
  height: 8px;
}

::-webkit-scrollbar-track {
  background: #f1f5f9;
  border-radius: 10px;
}

::-webkit-scrollbar-thumb {
  background: linear-gradient(135deg, #3D8D7A, #20c997);
  border-radius: 10px;
  border: 1px solid #e2e8f0;
  transition: all 0.3s ease;
}

::-webkit-scrollbar-thumb:hover {
  background: linear-gradient(135deg, #2d6a5a, #18a577);
  box-shadow: 0 2px 8px rgba(61, 141, 122, 0.3);
}

::-webkit-scrollbar-thumb:active {
  background: linear-gradient(135deg, #1e5a4a, #146e5a);
}

::-webkit-scrollbar-corner {
  background: #f1f5f9;
}

/* Firefox Scrollbar */
* {
  scrollbar-width: thin;
  scrollbar-color: #3D8D7A #f1f5f9;
}

/* Dark mode scrollbar */
.dark ::-webkit-scrollbar-track {
  background: #1a1d21;
}

.dark ::-webkit-scrollbar-thumb {
  background: linear-gradient(135deg, #20c997, #18a577);
  border: 1px solid #374151;
}

.dark ::-webkit-scrollbar-thumb:hover {
  background: linear-gradient(135deg, #18a577, #146e5a);
  box-shadow: 0 2px 8px rgba(32, 201, 151, 0.3);
}

.dark ::-webkit-scrollbar-corner {
  background: #1a1d21;
}

/* Main content scroll behavior */
.main-content {
  scroll-behavior: smooth;
  overflow-y: auto;
  overflow-x: hidden;
}

</style>
