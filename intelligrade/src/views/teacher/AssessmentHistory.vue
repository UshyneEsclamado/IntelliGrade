<template>
  <div class="history-page">
    <!-- Header Section -->
    <div class="page-header">
      <div class="header-container">
        <div class="header-content">
          <div class="page-info">
            <div class="page-icon">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                <path d="M13,3A9,9 0 0,0 4,12H1L4.96,16.03L9,12H6A7,7 0 0,1 13,5A7,7 0 0,1 20,12A7,7 0 0,1 13,19C11.07,19 9.32,18.21 8.06,16.94L6.64,18.36C8.27,20 10.5,21 13,21A9,9 0 0,0 22,12A9,9 0 0,0 13,3Z" />
              </svg>
            </div>
            <div class="page-details">
              <h1>Assessment History & Results</h1>
              <p>View all your checked assessments organized by subject</p>
            </div>
          </div>
          <button @click="goToUpload" class="upload-btn">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M12 6v6m0 0v6m0-6h6m-6 0H6"/>
            </svg>
            Check New Assessment
          </button>
        </div>
      </div>
    </div>

    <!-- Main Content -->
    <div class="main-content">
      <!-- Summary Stats -->
      <div class="stats-section">
        <div class="stats-grid">
          <div class="stat-card">
            <div class="stat-icon">📊</div>
            <div class="stat-info">
              <div class="stat-value">{{ totalAssessments }}</div>
              <div class="stat-label">Total Assessments</div>
            </div>
          </div>
          <div class="stat-card">
            <div class="stat-icon">📚</div>
            <div class="stat-info">
              <div class="stat-value">{{ totalSubjects }}</div>
              <div class="stat-label">Subjects</div>
            </div>
          </div>
          <div class="stat-card">
            <div class="stat-icon">⭐</div>
            <div class="stat-info">
              <div class="stat-value">{{ averageScore }}%</div>
              <div class="stat-label">Average Score</div>
            </div>
          </div>
          <div class="stat-card">
            <div class="stat-icon">📅</div>
            <div class="stat-info">
              <div class="stat-value">{{ recentChecks }}</div>
              <div class="stat-label">This Week</div>
            </div>
          </div>
        </div>
      </div>

      <!-- Subject Groups -->
      <div class="subjects-section">
        <div v-for="subject in groupedAssessments" :key="subject.name" class="subject-group">
          <div class="subject-header">
            <div class="subject-info">
              <div class="subject-icon-large">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M12,3L1,9L12,15L21,9V10H23V9M5,13.18V17.18L12,21L19,17.18V13.18L12,17L5,13.18Z" />
                </svg>
              </div>
              <div>
                <h2 class="subject-name">{{ subject.name }}</h2>
                <p class="subject-count">{{ subject.assessments.length }} assessments checked</p>
              </div>
            </div>
            <button @click="toggleSubject(subject.name)" class="toggle-btn">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" :class="{ 'rotated': expandedSubjects.includes(subject.name) }">
                <path d="M7 10l5 5 5-5z"/>
              </svg>
            </button>
          </div>

          <div v-if="expandedSubjects.includes(subject.name)" class="assessments-list slide-down">
            <div v-for="assessment in subject.assessments" :key="assessment.id" 
                 class="assessment-card" @click="viewAssessment(assessment)">
              <div class="assessment-info">
                <div class="assessment-header">
                  <h3 class="assessment-title">{{ assessment.title }}</h3>
                  <span class="assessment-date">{{ formatDate(assessment.checkedAt) }}</span>
                </div>
                <div class="assessment-details">
                  <div class="student-name">👤 {{ assessment.studentName }}</div>
                  <div class="question-count">📝 {{ assessment.totalQuestions }} questions</div>
                </div>
              </div>
              
              <div class="assessment-score">
                <div class="score-circle" :class="getScoreClass(assessment.percentage)">
                  <span class="score-value">{{ assessment.percentage }}%</span>
                </div>
                <div class="grade-info">
                  <span class="grade-letter" :class="getGradeClass(assessment.percentage)">
                    {{ getLetterGrade(assessment.percentage) }}
                  </span>
                  <span class="points">{{ assessment.pointsEarned }}/{{ assessment.totalPoints }}</span>
                </div>
              </div>

              <div class="assessment-actions">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M13 7l5 5m0 0l-5 5m5-5H6"/>
                </svg>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Empty State -->
      <div v-if="totalAssessments === 0" class="empty-state">
        <div class="empty-icon">📋</div>
        <h3>No Assessments Yet</h3>
        <p>Start by uploading and checking your first student assessment</p>
        <button @click="goToUpload" class="btn-primary">
          Check Your First Assessment
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'AssessmentHistory',
  data() {
    return {
      expandedSubjects: ['Science', 'Mathematics'], // Default expanded subjects
      assessments: [],
      loading: true,
      error: null,
      
      // Sample data - will be replaced by API data
      sampleAssessments: [
        {
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
            strengths: ["Strong understanding of cell structure", "Good knowledge of photosynthesis"],
            weaknesses: ["Needs work on mitosis phases", "Confused about DNA replication"],
            recommendations: ["Review cell division chapter", "Practice more diagram labeling"]
          }
        },
        {
          id: 2,
          title: "Algebra Test - Linear Equations",
          studentName: "Sarah Johnson",
          subject: "Mathematics",
          percentage: 92,
          pointsEarned: 46,
          totalPoints: 50,
          totalQuestions: 15,
          checkedAt: "2024-01-14T14:20:00Z",
          feedback: {
            strengths: ["Excellent problem-solving skills", "Clear understanding of concepts"],
            weaknesses: ["Minor calculation errors", "Rushed through word problems"],
            recommendations: ["Double-check calculations", "Take more time with word problems"]
          }
        },
        {
          id: 3,
          title: "Physics - Motion and Forces",
          studentName: "Mike Chen", 
          subject: "Science",
          percentage: 78,
          pointsEarned: 78,
          totalPoints: 100,
          totalQuestions: 25,
          checkedAt: "2024-01-13T09:15:00Z",
          feedback: {
            strengths: ["Good understanding of velocity", "Correct use of formulas"],
            weaknesses: ["Struggled with acceleration problems", "Unit conversion errors"],
            recommendations: ["Practice more acceleration problems", "Review unit conversions"]
          }
        },
        {
          id: 4,
          title: "Geometry - Triangles and Angles",
          studentName: "Emma Davis",
          subject: "Mathematics", 
          percentage: 88,
          pointsEarned: 44,
          totalPoints: 50,
          totalQuestions: 12,
          checkedAt: "2024-01-12T11:45:00Z",
          feedback: {
            strengths: ["Strong geometric reasoning", "Accurate angle calculations"],
            weaknesses: ["Some theorem applications incorrect", "Drawing could be neater"],
            recommendations: ["Review triangle theorems", "Practice geometric constructions"]
          }
        },
        {
          id: 5,
          title: "Chemistry - Periodic Table",
          studentName: "Alex Rodriguez",
          subject: "Science",
          percentage: 95,
          pointsEarned: 95,
          totalPoints: 100,
          totalQuestions: 30,
          checkedAt: "2024-01-11T13:30:00Z",
          feedback: {
            strengths: ["Excellent memorization of elements", "Perfect understanding of trends"],
            weaknesses: ["Minor error in electron configuration"],
            recommendations: ["Continue excellent work", "Practice electron configurations"]
          }
        }
      ]
    };
  },
  async mounted() {
    await this.fetchAssessmentHistory();
  },
  computed: {
    groupedAssessments() {
      const groups = {};
      const dataToUse = this.assessments.length > 0 ? this.assessments : this.sampleAssessments;
      dataToUse.forEach(assessment => {
        if (!groups[assessment.subject]) {
          groups[assessment.subject] = {
            name: assessment.subject,
            assessments: []
          };
        }
        groups[assessment.subject].assessments.push(assessment);
      });
      
      // Sort assessments by date within each subject
      Object.values(groups).forEach(group => {
        group.assessments.sort((a, b) => new Date(b.checkedAt) - new Date(a.checkedAt));
      });
      
      return Object.values(groups);
    },
    totalAssessments() {
      const dataToUse = this.assessments.length > 0 ? this.assessments : this.sampleAssessments;
      return dataToUse.length;
    },
    totalSubjects() {
      return this.groupedAssessments.length;
    },
    averageScore() {
      const dataToUse = this.assessments.length > 0 ? this.assessments : this.sampleAssessments;
      if (dataToUse.length === 0) return 0;
      const total = dataToUse.reduce((sum, assessment) => sum + assessment.percentage, 0);
      return Math.round(total / dataToUse.length);
    },
    recentChecks() {
      const oneWeekAgo = new Date();
      oneWeekAgo.setDate(oneWeekAgo.getDate() - 7);
      const dataToUse = this.assessments.length > 0 ? this.assessments : this.sampleAssessments;
      return dataToUse.filter(assessment => 
        new Date(assessment.checkedAt) > oneWeekAgo
      ).length;
    }
  },
  methods: {
    async fetchAssessmentHistory() {
      try {
        this.loading = true;
        const response = await fetch('http://localhost:8000/api/assessments/history');
        const result = await response.json();
        
        if (result.success && result.data) {
          // Convert grouped data to array format
          this.assessments = [];
          Object.keys(result.data).forEach(subject => {
            result.data[subject].forEach(assessment => {
              this.assessments.push({
                ...assessment,
                subject: subject,
                checkedAt: assessment.checked_at
              });
            });
          });
        }
      } catch (error) {
        console.error('Error fetching assessment history:', error);
        this.error = 'Failed to load assessment history';
        // Keep using sample data on error
      } finally {
        this.loading = false;
      }
    },
    goToUpload() {
      this.$router.push('/teacher/upload-assessment');
    },
    toggleSubject(subjectName) {
      if (this.expandedSubjects.includes(subjectName)) {
        this.expandedSubjects = this.expandedSubjects.filter(name => name !== subjectName);
      } else {
        this.expandedSubjects.push(subjectName);
      }
    },
    viewAssessment(assessment) {
      // Navigate to detailed assessment view
      this.$router.push(`/teacher/assessment-details/${assessment.id}`);
    },
    formatDate(dateString) {
      const date = new Date(dateString);
      return date.toLocaleDateString('en-US', {
        month: 'short',
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
  }
};
</script>

<style scoped>
/* Color Theme Variables */
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

/* Base Styles */
.history-page {
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
}

.page-info {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.page-icon {
  width: 48px;
  height: 48px;
  background: linear-gradient(135deg, var(--primary-green), var(--mint-green));
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--white);
}

.page-details h1 {
  font-size: 1.875rem;
  font-weight: 700;
  color: var(--gray-800);
  margin: 0;
}

.page-details p {
  color: var(--gray-600);
  margin: 0.25rem 0 0 0;
  font-size: 0.95rem;
}

.upload-btn {
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

.upload-btn:hover {
  transform: translateY(-1px);
  box-shadow: 0 6px 16px rgba(61, 141, 122, 0.4);
}

/* Main Content */
.main-content {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
}

/* Stats Section */
.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1.5rem;
  margin-bottom: 2rem;
}

.stat-card {
  background: var(--white);
  border-radius: 16px;
  padding: 1.5rem;
  display: flex;
  align-items: center;
  gap: 1rem;
  box-shadow: var(--shadow-md);
  border: 1px solid rgba(61, 141, 122, 0.1);
  transition: all 0.3s ease;
}

.stat-card:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-lg);
}

.stat-icon {
  font-size: 2rem;
  width: 60px;
  height: 60px;
  background: linear-gradient(135deg, var(--primary-green), var(--mint-green));
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.stat-value {
  font-size: 1.875rem;
  font-weight: 700;
  color: var(--gray-800);
  margin-bottom: 0.25rem;
}

.stat-label {
  font-size: 0.875rem;
  color: var(--gray-600);
  font-weight: 500;
}

/* Subject Groups */
.subject-group {
  background: var(--white);
  border-radius: 16px;
  margin-bottom: 1.5rem;
  box-shadow: var(--shadow-md);
  border: 1px solid rgba(61, 141, 122, 0.1);
  overflow: hidden;
}

.subject-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.5rem;
  border-bottom: 1px solid var(--gray-200);
  cursor: pointer;
  transition: all 0.3s ease;
}

.subject-header:hover {
  background: rgba(163, 209, 198, 0.05);
}

.subject-info {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.subject-icon-large {
  width: 48px;
  height: 48px;
  background: linear-gradient(135deg, var(--primary-green), var(--mint-green));
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--white);
}

.subject-name {
  font-size: 1.25rem;
  font-weight: 600;
  color: var(--gray-800);
  margin: 0;
}

.subject-count {
  font-size: 0.875rem;
  color: var(--gray-600);
  margin: 0.25rem 0 0 0;
}

.toggle-btn {
  width: 36px;
  height: 36px;
  border: none;
  background: var(--gray-100);
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.3s ease;
}

.toggle-btn:hover {
  background: var(--gray-200);
}

.toggle-btn svg {
  transition: transform 0.3s ease;
}

.toggle-btn svg.rotated {
  transform: rotate(180deg);
}

/* Assessment Cards */
.assessments-list {
  padding: 0 1.5rem 1.5rem;
}

.assessment-card {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1.25rem;
  border: 2px solid var(--gray-200);
  border-radius: 12px;
  margin-bottom: 1rem;
  cursor: pointer;
  transition: all 0.3s ease;
}

.assessment-card:hover {
  border-color: var(--mint-green);
  background: rgba(163, 209, 198, 0.05);
  transform: translateX(4px);
}

.assessment-info {
  flex: 1;
}

.assessment-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 0.5rem;
}

.assessment-title {
  font-size: 1.125rem;
  font-weight: 600;
  color: var(--gray-800);
  margin: 0;
}

.assessment-date {
  font-size: 0.875rem;
  color: var(--gray-500);
}

.assessment-details {
  display: flex;
  gap: 1.5rem;
  font-size: 0.875rem;
  color: var(--gray-600);
}

.assessment-score {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin: 0 1rem;
}

.score-circle {
  width: 60px;
  height: 60px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 3px solid;
  font-weight: 700;
  font-size: 0.875rem;
}

.score-circle.excellent { 
  border-color: #22c55e; 
  background: rgba(34, 197, 94, 0.1);
  color: #22c55e;
}

.score-circle.good { 
  border-color: #3b82f6; 
  background: rgba(59, 130, 246, 0.1);
  color: #3b82f6;
}

.score-circle.average { 
  border-color: #f59e0b; 
  background: rgba(245, 158, 11, 0.1);
  color: #f59e0b;
}

.score-circle.below-average { 
  border-color: #ef4444; 
  background: rgba(239, 68, 68, 0.1);
  color: #ef4444;
}

.score-circle.poor { 
  border-color: #dc2626; 
  background: rgba(220, 38, 38, 0.1);
  color: #dc2626;
}

.grade-info {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.25rem;
}

.grade-letter {
  padding: 0.25rem 0.75rem;
  border-radius: 6px;
  color: var(--white);
  font-weight: 700;
  font-size: 0.875rem;
}

.grade-letter.grade-a { background: #22c55e; }
.grade-letter.grade-b { background: #3b82f6; }
.grade-letter.grade-c { background: #f59e0b; }
.grade-letter.grade-f { background: #ef4444; }

.points {
  font-size: 0.75rem;
  color: var(--gray-600);
  font-weight: 500;
}

.assessment-actions {
  width: 36px;
  height: 36px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--gray-400);
  transition: all 0.3s ease;
}

.assessment-card:hover .assessment-actions {
  color: var(--primary-green);
  transform: translateX(4px);
}

/* Empty State */
.empty-state {
  text-align: center;
  padding: 4rem 2rem;
  background: var(--white);
  border-radius: 20px;
  box-shadow: var(--shadow-lg);
  border: 1px solid rgba(61, 141, 122, 0.1);
}

.empty-icon {
  font-size: 4rem;
  margin-bottom: 1.5rem;
  opacity: 0.6;
}

.empty-state h3 {
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--gray-800);
  margin-bottom: 0.5rem;
}

.empty-state p {
  color: var(--gray-600);
  margin-bottom: 2rem;
  font-size: 1.125rem;
}

.btn-primary {
  display: inline-flex;
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

.btn-primary:hover {
  transform: translateY(-1px);
  box-shadow: 0 6px 16px rgba(61, 141, 122, 0.4);
}

/* Animations */
@keyframes slideDown {
  from {
    opacity: 0;
    max-height: 0;
    transform: translateY(-10px);
  }
  to {
    opacity: 1;
    max-height: 1000px;
    transform: translateY(0);
  }
}

.slide-down {
  animation: slideDown 0.3s ease-out;
}

/* Responsive Design */
@media (max-width: 768px) {
  .history-page {
    padding: 1rem;
  }
  
  .header-container {
    padding: 0 1rem;
  }
  
  .header-content {
    flex-direction: column;
    gap: 1rem;
    text-align: center;
  }
  
  .main-content {
    padding: 1rem;
  }
  
  .stats-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 1rem;
  }
  
  .assessment-card {
    flex-direction: column;
    gap: 1rem;
    text-align: center;
  }
  
  .assessment-header {
    flex-direction: column;
    gap: 0.5rem;
  }
  
  .assessment-details {
    justify-content: center;
  }
  
  .assessment-score {
    justify-content: center;
    margin: 0;
  }
}
</style>