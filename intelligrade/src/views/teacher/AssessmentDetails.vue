<template>
  <div class="assessment-details-page">
    <!-- Header Section -->
    <div class="page-header">
      <div class="header-container">
        <div class="header-content">
          <button @click="goBack" class="back-btn">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M20,11V13H8L13.5,18.5L12.08,19.92L4.16,12L12.08,4.08L13.5,5.5L8,11H20Z" />
            </svg>
            Back to History
          </button>
          
          <div class="assessment-info">
            <div class="assessment-icon">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                <path d="M14,2H6A2,2 0 0,0 4,4V20A2,2 0 0,0 6,22H18A2,2 0 0,0 20,20V8L14,2M18,20H6V4H13V9H18V20Z" />
              </svg>
            </div>
            <div class="assessment-details">
              <h1>{{ assessment.title }}</h1>
              <p>{{ assessment.studentName }} • {{ assessment.subject }} • {{ formatDate(assessment.checkedAt) }}</p>
            </div>
          </div>

          <div class="header-actions">
            <button @click="downloadReport" class="download-btn">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                <path d="M5,20H19V18H5M19,9H15V3H9V9H5L12,16L19,9Z" />
              </svg>
              Download
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Main Content -->
    <div class="main-content">
      <!-- Score Overview -->
      <div class="overview-section">
        <div class="score-card">
          <div class="score-visual">
            <div class="score-circle" :class="getScoreClass(assessment.percentage)">
              <div class="score-value">{{ assessment.percentage }}%</div>
              <div class="score-label">Overall Score</div>
            </div>
          </div>
          
          <div class="score-details">
            <div class="detail-row">
              <span class="detail-label">Points Earned:</span>
              <span class="detail-value">{{ assessment.pointsEarned }} / {{ assessment.totalPoints }}</span>
            </div>
            <div class="detail-row">
              <span class="detail-label">Letter Grade:</span>
              <span class="detail-value grade-letter" :class="getGradeClass(assessment.percentage)">
                {{ getLetterGrade(assessment.percentage) }}
              </span>
            </div>
            <div class="detail-row">
              <span class="detail-label">Questions:</span>
              <span class="detail-value">{{ assessment.totalQuestions }} questions</span>
            </div>
            <div class="detail-row">
              <span class="detail-label">Subject:</span>
              <span class="detail-value">{{ assessment.subject }}</span>
            </div>
          </div>

          <div class="performance-indicator">
            <div class="performance-bar">
              <div class="progress-fill" :style="{ width: assessment.percentage + '%' }" :class="getScoreClass(assessment.percentage)"></div>
            </div>
            <div class="performance-labels">
              <span>0%</span>
              <span>50%</span>
              <span>100%</span>
            </div>
          </div>
        </div>
      </div>

      <!-- AI Feedback Section -->
      <div class="feedback-section">
        <div class="section-header">
          <div class="section-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
              <path d="M13,3A9,9 0 0,0 4,12H1L4.96,16.03L9,12H6A7,7 0 0,1 13,5A7,7 0 0,1 20,12A7,7 0 0,1 13,19C11.07,19 9.32,18.21 8.06,16.94L6.64,18.36C8.27,20 10.5,21 13,21A9,9 0 0,0 22,12A9,9 0 0,0 13,3Z" />
            </svg>
          </div>
          <h2>AI-Generated Feedback</h2>
        </div>

        <div class="feedback-grid">
          <!-- Strengths -->
          <div class="feedback-card strengths">
            <div class="feedback-header">
              <span class="feedback-icon">💪</span>
              <h3>Strengths</h3>
            </div>
            <ul class="feedback-list">
              <li v-for="strength in assessment.feedback.strengths" :key="strength">
                {{ strength }}
              </li>
            </ul>
          </div>

          <!-- Weaknesses -->
          <div class="feedback-card weaknesses">
            <div class="feedback-header">
              <span class="feedback-icon">🎯</span>
              <h3>Areas for Improvement</h3>
            </div>
            <ul class="feedback-list">
              <li v-for="weakness in assessment.feedback.weaknesses" :key="weakness">
                {{ weakness }}
              </li>
            </ul>
          </div>

          <!-- Recommendations -->
          <div class="feedback-card recommendations">
            <div class="feedback-header">
              <span class="feedback-icon">📚</span>
              <h3>Recommendations</h3>
            </div>
            <ul class="feedback-list">
              <li v-for="recommendation in assessment.feedback.recommendations" :key="recommendation">
                {{ recommendation }}
              </li>
            </ul>
          </div>
        </div>
      </div>

      <!-- Question Breakdown -->
      <div class="breakdown-section">
        <div class="section-header">
          <div class="section-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
              <path d="M8.228 9c.549-1.165 2.03-2 3.772-2 2.21 0 4 1.343 4 3 0 1.4-1.278 2.575-3.006 2.907-.542.104-.994.54-.994 1.093m0 3h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
            </svg>
          </div>
          <h2>Question-by-Question Analysis</h2>
        </div>

        <div class="questions-list">
          <div v-for="(question, index) in sampleQuestions" :key="index" 
               class="question-card" :class="{ 'correct': question.isCorrect, 'incorrect': !question.isCorrect }">
            <div class="question-header">
              <div class="question-number">
                <span class="question-badge">{{ index + 1 }}</span>
                <span class="question-type">{{ question.type }}</span>
              </div>
              <div class="question-status">
                <span v-if="question.isCorrect" class="status-correct">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M9 16.2L4.8 12l-1.4 1.4L9 19 21 7l-1.4-1.4L9 16.2z"/>
                  </svg>
                  Correct
                </span>
                <span v-else class="status-incorrect">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"/>
                  </svg>
                  Incorrect
                </span>
              </div>
              <div class="question-points">
                {{ question.pointsEarned }}/{{ question.pointsPossible }} pts
              </div>
            </div>

            <div class="question-content">
              <p class="question-text">{{ question.text }}</p>
              
              <div v-if="question.type === 'Multiple Choice'" class="question-options">
                <div v-for="(option, optIndex) in question.options" :key="optIndex" 
                     class="option-item" :class="{ 
                       'selected': option.selected, 
                       'correct': option.correct,
                       'incorrect': option.selected && !option.correct
                     }">
                  <span class="option-letter">{{ String.fromCharCode(65 + optIndex) }}.</span>
                  <span class="option-text">{{ option.text }}</span>
                  <span v-if="option.correct" class="option-indicator correct">✓</span>
                  <span v-else-if="option.selected" class="option-indicator incorrect">✗</span>
                </div>
              </div>

              <div v-if="question.type === 'True/False'" class="tf-answer">
                <div class="tf-options">
                  <div class="tf-option" :class="{ 
                    'selected': question.studentAnswer === 'True', 
                    'correct': question.correctAnswer === 'True',
                    'incorrect': question.studentAnswer === 'True' && question.correctAnswer !== 'True'
                  }">
                    <span>True</span>
                    <span v-if="question.correctAnswer === 'True'" class="option-indicator correct">✓</span>
                    <span v-else-if="question.studentAnswer === 'True'" class="option-indicator incorrect">✗</span>
                  </div>
                  <div class="tf-option" :class="{ 
                    'selected': question.studentAnswer === 'False', 
                    'correct': question.correctAnswer === 'False',
                    'incorrect': question.studentAnswer === 'False' && question.correctAnswer !== 'False'
                  }">
                    <span>False</span>
                    <span v-if="question.correctAnswer === 'False'" class="option-indicator correct">✓</span>
                    <span v-else-if="question.studentAnswer === 'False'" class="option-indicator incorrect">✗</span>
                  </div>
                </div>
              </div>

              <div v-if="question.feedback" class="question-feedback">
                <div class="feedback-content">
                  <span class="feedback-label">AI Feedback:</span>
                  <p>{{ question.feedback }}</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'AssessmentDetails',
  data() {
    return {
      assessment: {
        id: 1,
        title: "Chapter 5 Biology Quiz",
        studentName: "John Smith",
        subject: "Science",
        percentage: 85,
        pointsEarned: 85,
        totalPoints: 100,
        totalQuestions: 20,
        checkedAt: "2024-01-15T10:30:00Z",
        feedback: {
          strengths: [
            "Strong understanding of cell structure and organelles",
            "Excellent grasp of photosynthesis process",
            "Good recall of biological terminology",
            "Consistent performance across different question types"
          ],
          weaknesses: [
            "Confusion about mitosis vs meiosis phases",
            "Struggled with DNA replication timing",
            "Mixed up enzyme functions in cellular respiration",
            "Needs improvement in diagram interpretation"
          ],
          recommendations: [
            "Review cell division chapter with focus on phase differences",
            "Practice more diagram labeling exercises",
            "Study enzyme pathways in cellular processes",
            "Create comparison charts for similar biological processes"
          ]
        }
      },
      sampleQuestions: [
        {
          type: "Multiple Choice",
          text: "Which organelle is responsible for photosynthesis in plant cells?",
          options: [
            { text: "Mitochondria", selected: false, correct: false },
            { text: "Chloroplast", selected: true, correct: true },
            { text: "Nucleus", selected: false, correct: false },
            { text: "Ribosome", selected: false, correct: false }
          ],
          isCorrect: true,
          pointsEarned: 5,
          pointsPossible: 5,
          feedback: "Excellent! Chloroplasts contain chlorophyll and are the sites of photosynthesis."
        },
        {
          type: "True/False",
          text: "DNA replication occurs during the S phase of the cell cycle.",
          studentAnswer: "False",
          correctAnswer: "True",
          isCorrect: false,
          pointsEarned: 0,
          pointsPossible: 5,
          feedback: "This statement is True. DNA replication specifically occurs during the S (synthesis) phase of interphase."
        },
        {
          type: "Multiple Choice",
          text: "What is the primary function of mitochondria?",
          options: [
            { text: "Protein synthesis", selected: false, correct: false },
            { text: "ATP production", selected: true, correct: true },
            { text: "Lipid storage", selected: false, correct: false },
            { text: "Waste removal", selected: false, correct: false }
          ],
          isCorrect: true,
          pointsEarned: 5,
          pointsPossible: 5,
          feedback: "Correct! Mitochondria are the powerhouses of the cell, producing ATP through cellular respiration."
        },
        {
          type: "True/False",
          text: "Meiosis results in four genetically identical daughter cells.",
          studentAnswer: "True",
          correctAnswer: "False",
          isCorrect: false,
          pointsEarned: 0,
          pointsPossible: 5,
          feedback: "This is False. Meiosis produces four genetically different gametes, while mitosis produces identical cells."
        }
      ]
    };
  },
  methods: {
    goBack() {
      this.$router.push('/teacher/assessment-history');
    },
    downloadReport() {
      // Generate and download assessment report
      const reportData = {
        assessment: this.assessment,
        questions: this.sampleQuestions,
        generatedAt: new Date().toISOString()
      };
      
      const blob = new Blob([JSON.stringify(reportData, null, 2)], { type: 'application/json' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `${this.assessment.studentName}_${this.assessment.title}_detailed_report.json`;
      a.click();
      URL.revokeObjectURL(url);
    },
    formatDate(dateString) {
      const date = new Date(dateString);
      return date.toLocaleDateString('en-US', {
        weekday: 'long',
        year: 'numeric',
        month: 'long',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
      });
    },
    getScoreClass(percentage) {
      if (percentage >= 90) return 'excellent';
      if (percentage >= 80) return 'good';
      if (percentage >= 70) return 'average';
      if (percentage >= 60) return 'below-average';
      return 'poor';
    },
    getLetterGrade(percentage) {
      if (percentage >= 90) return 'A';
      if (percentage >= 80) return 'B';
      if (percentage >= 70) return 'C';
      if (percentage >= 60) return 'D';
      return 'F';
    },
    getGradeClass(percentage) {
      if (percentage >= 80) return 'grade-a';
      if (percentage >= 70) return 'grade-b';
      if (percentage >= 60) return 'grade-c';
      return 'grade-f';
    }
  },
  mounted() {
    // In real app, fetch assessment details based on route params
    // const assessmentId = this.$route.params.id;
    // this.fetchAssessmentDetails(assessmentId);
  }
};
</script>

<style scoped>
/* Using the same color variables */
:root {
  --primary-green: #3D8D7A;
  --light-green: #B3D8A8;
  --mint-green: #A3D1C6;
  --white: #FFFFFF;
  --gray-50: #f9fafb;
  --gray-100: #f3f4f6;
  --gray-200: #e5e7eb;
  --gray-300: #d1d5db;
  --gray-400: #9ca3af;
  --gray-500: #6b7280;
  --gray-600: #4b5563;
  --gray-700: #374151;
  --gray-800: #1f2937;
  --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
  --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
  --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
  --shadow-xl: 0 20px 25px -5px rgba(0, 0, 0, 0.1);
}

.assessment-details-page {
  min-height: 100vh;
  background: linear-gradient(135deg, var(--light-green) 0%, var(--mint-green) 100%);
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
}

/* Header Section */
.page-header {
  background: var(--white);
  box-shadow: var(--shadow-md);
  border-bottom: 3px solid var(--primary-green);
}

.header-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem;
}

.header-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.5rem 0;
  gap: 2rem;
}

.back-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1.5rem;
  background: var(--gray-100);
  color: var(--gray-600);
  border: 1px solid var(--gray-300);
  border-radius: 10px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s ease;
}

.back-btn:hover {
  background: var(--gray-200);
  color: var(--gray-700);
  transform: translateY(-1px);
}

.assessment-info {
  display: flex;
  align-items: center;
  gap: 1rem;
  flex: 1;
}

.assessment-icon {
  width: 48px;
  height: 48px;
  background: linear-gradient(135deg, var(--primary-green), var(--mint-green));
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--white);
}

.assessment-details h1 {
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--gray-800);
  margin: 0;
}

.assessment-details p {
  color: var(--gray-600);
  margin: 0.25rem 0 0 0;
  font-size: 0.95rem;
}

.download-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.875rem 1.5rem;
  background: linear-gradient(135deg, var(--primary-green), var(--mint-green));
  color: var(--white);
  border: none;
  border-radius: 10px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 4px 12px rgba(61, 141, 122, 0.3);
}

.download-btn:hover {
  transform: translateY(-1px);
  box-shadow: 0 6px 16px rgba(61, 141, 122, 0.4);
}

/* Main Content */
.main-content {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
}

/* Score Overview */
.overview-section {
  margin-bottom: 2rem;
}

.score-card {
  background: var(--white);
  border-radius: 20px;
  padding: 2rem;
  box-shadow: var(--shadow-lg);
  border: 1px solid rgba(61, 141, 122, 0.1);
}

.score-visual {
  display: flex;
  justify-content: center;
  margin-bottom: 2rem;
}

.score-circle {
  width: 150px;
  height: 150px;
  border-radius: 50%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  border: 5px solid;
  position: relative;
}

.score-circle.excellent { 
  border-color: #22c55e; 
  background: rgba(34, 197, 94, 0.1);
}

.score-circle.good { 
  border-color: #3b82f6; 
  background: rgba(59, 130, 246, 0.1);
}

.score-circle.average { 
  border-color: #f59e0b; 
  background: rgba(245, 158, 11, 0.1);
}

.score-circle.below-average { 
  border-color: #ef4444; 
  background: rgba(239, 68, 68, 0.1);
}

.score-circle.poor { 
  border-color: #dc2626; 
  background: rgba(220, 38, 38, 0.1);
}

.score-value {
  font-size: 2.5rem;
  font-weight: 700;
  color: var(--gray-800);
}

.score-label {
  font-size: 0.875rem;
  color: var(--gray-600);
  margin-top: 0.25rem;
}

.score-details {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1rem;
  margin-bottom: 2rem;
}

.detail-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
  background: var(--gray-50);
  border-radius: 10px;
}

.detail-label {
  font-weight: 600;
  color: var(--gray-600);
}

.detail-value {
  font-weight: 700;
  color: var(--gray-800);
}

.grade-letter {
  padding: 0.25rem 0.75rem;
  border-radius: 6px;
  color: var(--white);
  font-weight: 700;
}

.grade-letter.grade-a { background: #22c55e; }
.grade-letter.grade-b { background: #3b82f6; }
.grade-letter.grade-c { background: #f59e0b; }
.grade-letter.grade-f { background: #ef4444; }

.performance-indicator {
  margin-top: 1.5rem;
}

.performance-bar {
  width: 100%;
  height: 12px;
  background: var(--gray-200);
  border-radius: 6px;
  overflow: hidden;
  margin-bottom: 0.5rem;
}

.progress-fill {
  height: 100%;
  border-radius: 6px;
  transition: width 0.8s ease;
}

.progress-fill.excellent { background: #22c55e; }
.progress-fill.good { background: #3b82f6; }
.progress-fill.average { background: #f59e0b; }
.progress-fill.below-average { background: #ef4444; }
.progress-fill.poor { background: #dc2626; }

.performance-labels {
  display: flex;
  justify-content: space-between;
  font-size: 0.75rem;
  color: var(--gray-500);
}

/* Feedback Section */
.feedback-section {
  margin-bottom: 2rem;
}

.section-header {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 1.5rem;
}

.section-icon {
  width: 48px;
  height: 48px;
  background: linear-gradient(135deg, var(--primary-green), var(--mint-green));
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--white);
}

.section-header h2 {
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--gray-800);
  margin: 0;
}

.feedback-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1.5rem;
}

.feedback-card {
  background: var(--white);
  border-radius: 16px;
  padding: 1.5rem;
  box-shadow: var(--shadow-md);
  border: 1px solid rgba(61, 141, 122, 0.1);
  transition: all 0.3s ease;
}

.feedback-card:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-lg);
}

.feedback-card.strengths {
  border-left: 4px solid #22c55e;
}

.feedback-card.weaknesses {
  border-left: 4px solid #ef4444;
}

.feedback-card.recommendations {
  border-left: 4px solid #3b82f6;
}

.feedback-header {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  margin-bottom: 1rem;
}

.feedback-icon {
  font-size: 1.5rem;
}

.feedback-header h3 {
  font-size: 1.125rem;
  font-weight: 600;
  color: var(--gray-800);
  margin: 0;
}

.feedback-list {
  margin: 0;
  padding-left: 1.5rem;
}

.feedback-list li {
  margin-bottom: 0.75rem;
  line-height: 1.5;
  color: var(--gray-700);
}

/* Question Breakdown */
.breakdown-section {
  margin-bottom: 2rem;
}

.questions-list {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.question-card {
  background: var(--white);
  border-radius: 16px;
  padding: 1.5rem;
  box-shadow: var(--shadow-md);
  border: 1px solid rgba(61, 141, 122, 0.1);
  transition: all 0.3s ease;
}

.question-card.correct {
  border-left: 4px solid #22c55e;
}

.question-card.incorrect {
  border-left: 4px solid #ef4444;
}

.question-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
  padding-bottom: 1rem;
  border-bottom: 1px solid var(--gray-200);
}

.question-number {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.question-badge {
  width: 32px;
  height: 32px;
  background: linear-gradient(135deg, var(--primary-green), var(--mint-green));
  color: var(--white);
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 0.875rem;
}

.question-type {
  font-size: 0.875rem;
  color: var(--gray-600);
  background: var(--gray-100);
  padding: 0.25rem 0.75rem;
  border-radius: 12px;
}

.question-status {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-weight: 600;
}

.status-correct {
  color: #22c55e;
  display: flex;
  align-items: center;
  gap: 0.25rem;
}

.status-incorrect {
  color: #ef4444;
  display: flex;
  align-items: center;
  gap: 0.25rem;
}

.question-points {
  font-weight: 600;
  color: var(--gray-600);
  background: var(--gray-100);
  padding: 0.25rem 0.75rem;
  border-radius: 12px;
}

.question-text {
  font-size: 1.125rem;
  font-weight: 500;
  color: var(--gray-800);
  margin-bottom: 1rem;
  line-height: 1.5;
}

.question-options {
  margin-bottom: 1rem;
}

.option-item {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.75rem;
  border: 2px solid var(--gray-200);
  border-radius: 8px;
  margin-bottom: 0.5rem;
  transition: all 0.3s ease;
}

.option-item.correct {
  border-color: #22c55e;
  background: rgba(34, 197, 94, 0.05);
}

.option-item.incorrect {
  border-color: #ef4444;
  background: rgba(239, 68, 68, 0.05);
}

.option-item.selected:not(.correct) {
  border-color: #ef4444;
  background: rgba(239, 68, 68, 0.05);
}

.option-letter {
  font-weight: 700;
  color: var(--gray-600);
  min-width: 20px;
}

.option-text {
  flex: 1;
  color: var(--gray-800);
}

.option-indicator {
  font-weight: 700;
  padding: 0.25rem 0.5rem;
  border-radius: 4px;
  font-size: 0.875rem;
}

.option-indicator.correct {
  background: #22c55e;
  color: var(--white);
}

.option-indicator.incorrect {
  background: #ef4444;
  color: var(--white);
}

.tf-answer {
  margin-bottom: 1rem;
}

.tf-options {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
}

.tf-option {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1rem;
  border: 2px solid var(--gray-200);
  border-radius: 8px;
  transition: all 0.3s ease;
}

.tf-option.correct {
  border-color: #22c55e;
  background: rgba(34, 197, 94, 0.05);
}

.tf-option.incorrect {
  border-color: #ef4444;
  background: rgba(239, 68, 68, 0.05);
}

.question-feedback {
  margin-top: 1rem;
  padding: 1rem;
  background: rgba(163, 209, 198, 0.1);
  border-radius: 8px;
  border-left: 4px solid var(--primary-green);
}

.feedback-content {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.feedback-label {
  font-weight: 600;
  color: var(--primary-green);
  font-size: 0.875rem;
}

.feedback-content p {
  margin: 0;
  color: var(--gray-700);
  line-height: 1.5;
}

/* Responsive Design */
@media (max-width: 768px) {
  .assessment-details-page {
    padding: 1rem;
  }
  
  .header-container {
    padding: 0 1rem;
  }
  
  .header-content {
    flex-direction: column;
    gap: 1rem;
  }
  
  .main-content {
    padding: 1rem;
  }
  
  .feedback-grid {
    grid-template-columns: 1fr;
  }
  
  .score-details {
    grid-template-columns: 1fr;
  }
  
  .question-header {
    flex-direction: column;
    gap: 0.5rem;
    align-items: flex-start;
  }
  
  .tf-options {
    grid-template-columns: 1fr;
  }
}
</style>