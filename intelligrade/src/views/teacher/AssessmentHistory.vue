<template>
  <div :class="['history-page', isDarkMode ? 'dark' : '']">
    <!-- Top Navigation Bar (Same as Upload Assessment) -->
    <nav class="top-navbar">
      <div class="navbar-content">
        <!-- Left: Logo and Brand -->
        <div class="navbar-left">
          <div class="brand-logo">
            <img src="@/assets/LOGO WAY BG.png" alt="IntelliGrade" class="logo-img" />
            <span class="brand-name">IntelliGrade</span>
          </div>
        </div>
        
        <!-- Center: Navigation Links -->
        <div class="navbar-center">
          <router-link to="/teacher/dashboard" class="nav-item">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M10,20V14H14V20H19V12H22L12,3L2,12H5V20H10Z" />
            </svg>
            <span>Dashboard</span>
          </router-link>
          
          <router-link to="/teacher/subjects" class="nav-item">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M12,3L1,9L12,15L21,10.09V17H23V9M5,13.18V17.18L12,21L19,17.18V13.18L12,17L5,13.18Z"/>
            </svg>
            <span>Classes</span>
          </router-link>
          
          <router-link to="/teacher/gradebook" class="nav-item">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M19,3H14.82C14.4,1.84 13.3,1 12,1C10.7,1 9.6,1.84 9.18,3H5A2,2 0 0,0 3,5V19A2,2 0 0,0 5,21H19A2,2 0 0,0 21,19V5A2,2 0 0,0 19,3M12,3A1,1 0 0,1 13,4A1,1 0 0,1 12,5A1,1 0 0,1 11,4A1,1 0 0,1 12,3Z" />
            </svg>
            <span>Gradebook</span>
          </router-link>
          
          <router-link to="/teacher/analytics" class="nav-item">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M22,21H2V3H4V19H6V10H10V19H12V6H16V19H18V14H22V21Z" />
            </svg>
            <span>Analytics</span>
          </router-link>
          
          <router-link to="/teacher/messages" class="nav-item">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>
            </svg>
            <span>Messages</span>
          </router-link>
          
          <router-link to="/teacher/upload-assessment" class="nav-item">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M9,16V10H5L12,3L19,10H15V16H9M5,20V18H19V20H5Z" />
            </svg>
            <span>Upload</span>
          </router-link>

          <router-link to="/teacher/assessment-history" class="nav-item active">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <circle cx="12" cy="12" r="10"/>
              <polyline points="12,6 12,12 16,14"/>
            </svg>
            <span>History</span>
          </router-link>
        </div>
        
        <!-- Right: Actions -->
        <div class="navbar-right">
          <button @click="refreshData" class="export-btn" :disabled="loading">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M21.5 2v6h-6M2.5 22v-6h6M2 11.5a10 10 0 0 1 18.8-4.3M22 12.5a10 10 0 0 1-18.8 4.2"/>
            </svg>
            <span>{{ loading ? 'Loading...' : 'Refresh' }}</span>
          </button>
        </div>
      </div>
    </nav>

    <!-- Main Content Area -->
    <main class="main-content">
      <!-- Page Header -->
      <div class="page-header">
        <div class="header-content">
          <div class="header-left">
            <div class="header-icon">
              <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <circle cx="12" cy="12" r="10"/>
                <polyline points="12,6 12,12 16,14"/>
              </svg>
            </div>
            <div>
              <h1 class="header-title">Assessment History</h1>
              <p class="header-subtitle">View all your checked assessments organized by subject</p>
            </div>
          </div>
          
          <div class="header-actions">
            <button @click="goToUpload" class="upload-btn">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M12 5v14m-7-7h14"/>
              </svg>
              Check New Assessment
            </button>
          </div>
        </div>
      </div>

      <!-- Loading State -->
      <div v-if="loading && assessments.length === 0" class="loading-state">
        <div class="loader"></div>
        <p>Loading assessment history...</p>
      </div>

      <!-- Error State -->
      <div v-if="error && !loading" class="error-message">
        <div class="error-content">
          <strong>⚠️ Error Loading History:</strong>
          <p>{{ error }}</p>
        </div>
        <button @click="refreshData" class="retry-btn">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
            <path d="M21.5 2v6h-6M2.5 22v-6h6M2 11.5a10 10 0 0 1 18.8-4.3M22 12.5a10 10 0 0 1-18.8 4.2"/>
          </svg>
          Retry
        </button>
      </div>

      <!-- Main Content -->
      <div v-if="!loading || assessments.length > 0">
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
        <div class="subjects-section" v-if="groupedAssessments.length > 0">
          <div v-for="subject in groupedAssessments" :key="subject.name" class="subject-group">
            <div class="subject-header" @click="toggleSubject(subject.name)">
              <div class="subject-info">
                <div class="subject-icon-large">
                  <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M12,3L1,9L12,15L21,10.09V17H23V9M5,13.18V17.18L12,21L19,17.18V13.18L12,17L5,13.18Z" />
                  </svg>
                </div>
                <div>
                  <h2 class="subject-name">{{ subject.name }}</h2>
                  <p class="subject-count">{{ subject.assessments.length }} assessment{{ subject.assessments.length !== 1 ? 's' : '' }} checked</p>
                </div>
              </div>
              <button class="toggle-btn">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" :class="{ 'rotated': expandedSubjects.includes(subject.name) }">
                  <path d="M7 10l5 5 5-5z"/>
                </svg>
              </button>
            </div>

            <transition name="slide">
              <div v-if="expandedSubjects.includes(subject.name)" class="assessments-list">
                <div v-for="assessment in subject.assessments" :key="assessment.id" 
                     class="assessment-card" @click="viewAssessment(assessment)">
                  <div class="assessment-info">
                    <div class="assessment-header">
                      <h3 class="assessment-title">{{ assessment.title || assessment.assessment_title }}</h3>
                      <span class="assessment-date">{{ formatDate(assessment.checked_at || assessment.checkedAt) }}</span>
                    </div>
                    <div class="assessment-details">
                      <div class="student-name">👤 {{ assessment.student_name || assessment.studentName }}</div>
                      <div class="question-count">📝 {{ assessment.total_questions || assessment.totalQuestions }} questions</div>
                      <div class="checking-method">🤖 {{ assessment.checking_method || 'Rule-based' }}</div>
                    </div>
                  </div>
                  
                  <div class="assessment-score">
                    <div class="score-circle" :class="getScoreClass(assessment.percentage)">
                      <span class="score-value">{{ Math.round(assessment.percentage) }}%</span>
                    </div>
                    <div class="grade-info">
                      <span class="grade-letter" :class="getGradeClass(assessment.percentage)">
                        {{ getLetterGrade(assessment.percentage) }}
                      </span>
                      <span class="points">{{ assessment.points_earned || assessment.pointsEarned }}/{{ assessment.total_points || assessment.totalPoints }}</span>
                    </div>
                  </div>

                  <div class="assessment-actions">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                      <path d="M13 7l5 5m0 0l-5 5m5-5H6"/>
                    </svg>
                  </div>
                </div>
              </div>
            </transition>
          </div>
        </div>

        <!-- Empty State -->
        <div v-if="totalAssessments === 0 && !loading" class="empty-state">
          <div class="empty-icon">📋</div>
          <h3>No Assessments Yet</h3>
          <p>Start by uploading and checking your first student assessment</p>
          <button @click="goToUpload" class="btn-primary">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M12 5v14m-7-7h14"/>
            </svg>
            Check Your First Assessment
          </button>
        </div>
      </div>
    </main>

    <!-- Assessment Detail Modal -->
    <div v-if="selectedAssessment" class="modal-overlay" @click="closeModal">
      <div class="modal-content" @click.stop>
        <div class="modal-header">
          <h2>{{ selectedAssessment.title || selectedAssessment.assessment_title }}</h2>
          <button @click="closeModal" class="close-btn">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
              <path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"/>
            </svg>
          </button>
        </div>
        
        <div class="modal-body">
          <!-- Score Overview -->
          <div class="score-overview">
            <div class="score-circle-large" :class="getScoreClass(selectedAssessment.percentage)">
              <div class="score-value-large">{{ Math.round(selectedAssessment.percentage) }}%</div>
              <div class="score-label">Overall Score</div>
            </div>
            <div class="score-details">
              <div class="detail-item">
                <span class="detail-label">Student:</span>
                <span class="detail-value">{{ selectedAssessment.student_name || selectedAssessment.studentName }}</span>
              </div>
              <div class="detail-item">
                <span class="detail-label">Subject:</span>
                <span class="detail-value">{{ selectedAssessment.subject }}</span>
              </div>
              <div class="detail-item">
                <span class="detail-label">Points Earned:</span>
                <span class="detail-value">{{ selectedAssessment.points_earned || selectedAssessment.pointsEarned }} / {{ selectedAssessment.total_points || selectedAssessment.totalPoints }}</span>
              </div>
              <div class="detail-item">
                <span class="detail-label">Letter Grade:</span>
                <span class="detail-value grade-letter" :class="getGradeClass(selectedAssessment.percentage)">
                  {{ getLetterGrade(selectedAssessment.percentage) }}
                </span>
              </div>
              <div class="detail-item">
                <span class="detail-label">Checked:</span>
                <span class="detail-value">{{ formatDateLong(selectedAssessment.checked_at || selectedAssessment.checkedAt) }}</span>
              </div>
            </div>
          </div>

          <!-- AI Feedback Section -->
          <div v-if="selectedAssessment.feedback" class="feedback-section">
            <h3>📊 AI Analysis & Feedback</h3>
            
            <div v-if="selectedAssessment.feedback.strengths && selectedAssessment.feedback.strengths.length > 0" class="feedback-block">
              <h4><span class="feedback-icon">💪</span> Strengths</h4>
              <ul class="feedback-list strengths">
                <li v-for="(strength, index) in selectedAssessment.feedback.strengths" :key="index">{{ strength }}</li>
              </ul>
            </div>

            <div v-if="selectedAssessment.feedback.weaknesses && selectedAssessment.feedback.weaknesses.length > 0" class="feedback-block">
              <h4><span class="feedback-icon">🎯</span> Areas for Improvement</h4>
              <ul class="feedback-list weaknesses">
                <li v-for="(weakness, index) in selectedAssessment.feedback.weaknesses" :key="index">{{ weakness }}</li>
              </ul>
            </div>

            <div v-if="selectedAssessment.feedback.recommendations && selectedAssessment.feedback.recommendations.length > 0" class="feedback-block">
              <h4><span class="feedback-icon">📚</span> Recommendations</h4>
              <ul class="feedback-list recommendations">
                <li v-for="(rec, index) in selectedAssessment.feedback.recommendations" :key="index">{{ rec }}</li>
              </ul>
            </div>

            <div v-if="selectedAssessment.feedback.detailedAnalysis || selectedAssessment.feedback.detailed_analysis" class="feedback-block">
              <h4><span class="feedback-icon">🔍</span> Detailed Analysis</h4>
              <p class="detailed-text">{{ selectedAssessment.feedback.detailedAnalysis || selectedAssessment.feedback.detailed_analysis }}</p>
            </div>
          </div>
        </div>

        <div class="modal-footer">
          <button @click="downloadReport(selectedAssessment)" class="btn-secondary">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
              <path d="M19 9h-4V3H9v6H5l7 7 7-7zM5 18v2h14v-2H5z"/>
            </svg>
            Download Report
          </button>
          <button @click="closeModal" class="btn-primary">Close</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, computed, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { useDarkMode } from '../../composables/useDarkMode.js';

export default {
  name: 'AssessmentHistory',
  setup() {
    const router = useRouter();
    const { isDarkMode } = useDarkMode();
    
    // Reactive state
    const assessments = ref([]);
    const loading = ref(true);
    const error = ref(null);
    const expandedSubjects = ref([]);
    const selectedAssessment = ref(null);

    // Fetch assessment history from backend
    const fetchAssessmentHistory = async () => {
      loading.value = true;
      error.value = null;
      
      try {
        console.log('🔄 Fetching assessment history from backend...');
        
        const response = await fetch('http://localhost:8000/api/assessments/history', {
          method: 'GET',
          headers: {
            'Content-Type': 'application/json'
          }
        });

        console.log('📡 Response status:', response.status);

        if (!response.ok) {
          if (response.status === 0 || !response.status) {
            throw new Error('Backend server is not running. Please start the backend server at http://localhost:8000');
          }
          const errorText = await response.text();
          throw new Error(`Server error: ${response.status} - ${errorText}`);
        }

        const result = await response.json();
        console.log('✅ Assessment history received:', result);

        if (result.success && result.data) {
          // Convert grouped data by subject to flat array with subject property
          const flatAssessments = [];
          
          Object.keys(result.data).forEach(subject => {
            result.data[subject].forEach(assessment => {
              flatAssessments.push({
                ...assessment,
                subject: subject,
                // Normalize field names for consistency
                id: assessment.id,
                title: assessment.assessment_title || assessment.title,
                studentName: assessment.student_name || assessment.studentName,
                percentage: assessment.percentage,
                pointsEarned: assessment.points_earned || assessment.pointsEarned,
                totalPoints: assessment.total_points || assessment.totalPoints,
                totalQuestions: assessment.total_questions || assessment.totalQuestions,
                checkedAt: assessment.checked_at || assessment.checkedAt,
                checkingMethod: assessment.checking_method || assessment.checkingMethod || 'Rule-based',
                feedback: assessment.feedback || {}
              });
            });
          });

          assessments.value = flatAssessments;
          
          // Auto-expand all subjects initially
          expandedSubjects.value = Object.keys(result.data);
          
          console.log(`✅ Loaded ${flatAssessments.length} assessments from ${Object.keys(result.data).length} subjects`);
        } else {
          console.warn('⚠️ No assessment data found');
          assessments.value = [];
        }
      } catch (err) {
        console.error('❌ Error fetching assessment history:', err);
        
        if (err.message.includes('Failed to fetch') || err.message.includes('Backend server')) {
          error.value = "🚫 Backend server is not running!\n\nPlease start the backend server:\n1. Open terminal in backend folder\n2. Run: python main.py\n3. Server should start at http://localhost:8000";
        } else {
          error.value = err.message || 'Failed to load assessment history';
        }
      } finally {
        loading.value = false;
      }
    };

    // Computed properties
    const groupedAssessments = computed(() => {
      const groups = {};
      
      assessments.value.forEach(assessment => {
        const subject = assessment.subject || 'Uncategorized';
        
        if (!groups[subject]) {
          groups[subject] = {
            name: subject,
            assessments: []
          };
        }
        
        groups[subject].assessments.push(assessment);
      });
      
      // Sort assessments by date within each subject (newest first)
      Object.values(groups).forEach(group => {
        group.assessments.sort((a, b) => {
          const dateA = new Date(a.checkedAt || a.checked_at);
          const dateB = new Date(b.checkedAt || b.checked_at);
          return dateB - dateA;
        });
      });
      
      return Object.values(groups);
    });

    const totalAssessments = computed(() => assessments.value.length);
    
    const totalSubjects = computed(() => groupedAssessments.value.length);
    
    const averageScore = computed(() => {
      if (assessments.value.length === 0) return 0;
      const total = assessments.value.reduce((sum, assessment) => sum + assessment.percentage, 0);
      return Math.round(total / assessments.value.length);
    });
    
    const recentChecks = computed(() => {
      const oneWeekAgo = new Date();
      oneWeekAgo.setDate(oneWeekAgo.getDate() - 7);
      
      return assessments.value.filter(assessment => {
        const checkedDate = new Date(assessment.checkedAt || assessment.checked_at);
        return checkedDate > oneWeekAgo;
      }).length;
    });

    // Methods
    const refreshData = () => {
      fetchAssessmentHistory();
    };

    const goToUpload = () => {
      router.push('/teacher/upload-assessment');
    };

    const toggleSubject = (subjectName) => {
      const index = expandedSubjects.value.indexOf(subjectName);
      if (index > -1) {
        expandedSubjects.value.splice(index, 1);
      } else {
        expandedSubjects.value.push(subjectName);
      }
    };

    const viewAssessment = (assessment) => {
      selectedAssessment.value = assessment;
    };

    const closeModal = () => {
      selectedAssessment.value = null;
    };

    const formatDate = (dateString) => {
      if (!dateString) return 'N/A';
      const date = new Date(dateString);
      return date.toLocaleDateString('en-US', {
        month: 'short',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
      });
    };

    const formatDateLong = (dateString) => {
      if (!dateString) return 'N/A';
      const date = new Date(dateString);
      return date.toLocaleDateString('en-US', {
        weekday: 'long',
        year: 'numeric',
        month: 'long',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
      });
    };

    const getScoreClass = (percentage) => {
      if (percentage >= 90) return 'excellent';
      if (percentage >= 80) return 'good';
      if (percentage >= 70) return 'average';
      if (percentage >= 60) return 'below-average';
      return 'poor';
    };

    const getLetterGrade = (percentage) => {
      if (percentage >= 90) return 'A';
      if (percentage >= 80) return 'B';
      if (percentage >= 70) return 'C';
      if (percentage >= 60) return 'D';
      return 'F';
    };

    const getGradeClass = (percentage) => {
      if (percentage >= 80) return 'grade-a';
      if (percentage >= 70) return 'grade-b';
      if (percentage >= 60) return 'grade-c';
      return 'grade-f';
    };

    const downloadReport = (assessment) => {
      const reportData = {
        student: assessment.studentName || assessment.student_name,
        assessment: assessment.title || assessment.assessment_title,
        subject: assessment.subject,
        score: assessment.percentage,
        pointsEarned: assessment.pointsEarned || assessment.points_earned,
        totalPoints: assessment.totalPoints || assessment.total_points,
        totalQuestions: assessment.totalQuestions || assessment.total_questions,
        checkedAt: assessment.checkedAt || assessment.checked_at,
        checkingMethod: assessment.checkingMethod || assessment.checking_method,
        feedback: assessment.feedback
      };
      
      const blob = new Blob([JSON.stringify(reportData, null, 2)], { type: 'application/json' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `${assessment.studentName || assessment.student_name}_${assessment.title || assessment.assessment_title}_report.json`;
      a.click();
      URL.revokeObjectURL(url);
    };

    // Load data on mount
    onMounted(() => {
      fetchAssessmentHistory();
      
      // Auto-refresh every 30 seconds to show new assessments
      const intervalId = setInterval(() => {
        if (!loading.value) {
          fetchAssessmentHistory();
        }
      }, 30000);
      
      // Cleanup interval on unmount
      return () => clearInterval(intervalId);
    });

    return {
      isDarkMode,
      assessments,
      loading,
      error,
      expandedSubjects,
      selectedAssessment,
      groupedAssessments,
      totalAssessments,
      totalSubjects,
      averageScore,
      recentChecks,
      refreshData,
      goToUpload,
      toggleSubject,
      viewAssessment,
      closeModal,
      formatDate,
      formatDateLong,
      getScoreClass,
      getLetterGrade,
      getGradeClass,
      downloadReport
    };
  }
};
</script>

<style scoped>
/* Base Styles */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.history-page {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background: #f8fafc;
  overflow-y: auto;
  z-index: 999999;
}

.dark .history-page {
  background: #181c20;
}

/* Top Navigation Bar (Same as Upload Assessment) */
.top-navbar {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  height: 64px;
  background: linear-gradient(135deg, #3D8D7A, #2d6a5a);
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  z-index: 1000;
  box-shadow: 0 4px 20px rgba(61, 141, 122, 0.3);
}

.navbar-content {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 100%;
  max-width: 1400px;
  margin: 0 auto;
  padding: 0 1.5rem;
}

.navbar-left {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.brand-logo {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  color: white;
  font-weight: 700;
  text-decoration: none;
}

.logo-img {
  width: 36px;
  height: 36px;
  object-fit: contain;
  filter: brightness(0) invert(1);
}

.brand-name {
  font-size: 1.4rem;
  font-weight: 800;
  color: white;
  letter-spacing: -0.5px;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
}

.navbar-center {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  flex: 1;
  justify-content: center;
  max-width: 700px;
}

.nav-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.25rem;
  padding: 0.75rem 1.5rem;
  border-radius: 12px;
  text-decoration: none;
  color: rgba(255, 255, 255, 0.8);
  transition: all 0.2s ease;
  position: relative;
  font-size: 0.75rem;
  font-weight: 500;
}

.nav-item:hover {
  background: rgba(255, 255, 255, 0.1);
  color: white;
}

.nav-item.active {
  color: white;
  background: rgba(255, 255, 255, 0.15);
}

.nav-item.active::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 60%;
  height: 3px;
  background: white;
  border-radius: 2px 2px 0 0;
}

.navbar-right {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.export-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  background: rgba(255, 255, 255, 0.15);
  color: white;
  border: 1px solid rgba(255, 255, 255, 0.2);
  padding: 0.75rem 1.25rem;
  border-radius: 8px;
  font-size: 0.875rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s;
}

.export-btn:hover:not(:disabled) {
  background: rgba(255, 255, 255, 0.25);
  border-color: rgba(255, 255, 255, 0.3);
  transform: translateY(-1px);
}

.export-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

/* Main Content */
.main-content {
  margin-top: 64px;
  padding: 1.5rem;
  width: 100%;
  min-height: calc(100vh - 64px);
  max-width: 1200px;
  margin-left: auto;
  margin-right: auto;
}

/* Page Header */
.page-header {
  background: white;
  border-radius: 16px;
  padding: 1.5rem 2rem;
  margin-bottom: 1.5rem;
  border: 1px solid #e2e8f0;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
}

.dark .page-header {
  background: #2a2d33;
  border-color: rgba(32, 201, 151, 0.2);
}

.header-content {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 1rem;
}

.header-left {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.header-icon {
  width: 56px;
  height: 56px;
  background: linear-gradient(135deg, #3D8D7A, #2d6a5a);
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
}

.header-title {
  font-size: 1.75rem;
  font-weight: 700;
  color: #1e293b;
  margin-bottom: 0.25rem;
}

.dark .header-title {
  color: #e2e8f0;
}

.header-subtitle {
  font-size: 0.95rem;
  color: #64748b;
}

.dark .header-subtitle {
  color: #94a3b8;
}

.upload-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1.5rem;
  background: linear-gradient(135deg, #20c997, #17a085);
  color: white;
  border: none;
  border-radius: 10px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 4px 12px rgba(32, 201, 151, 0.3);
}

.upload-btn:hover {
  background: linear-gradient(135deg, #17a085, #138f75);
  transform: translateY(-2px);
  box-shadow: 0 6px 16px rgba(32, 201, 151, 0.4);
}

/* Loading State */
.loading-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 4rem 2rem;
  background: white;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
}

.dark .loading-state {
  background: #2a2d33;
}

.loader {
  width: 50px;
  height: 50px;
  border: 5px solid #e2e8f0;
  border-top: 5px solid #3D8D7A;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin-bottom: 1rem;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

.loading-state p {
  color: #64748b;
  font-size: 0.95rem;
}

/* Error Message */
.error-message {
  background: #fff5f5;
  color: #c53030;
  padding: 1.5rem;
  border-radius: 12px;
  border: 1px solid #fed7d7;
  margin-bottom: 1.5rem;
  box-shadow: 0 4px 12px rgba(239, 68, 68, 0.1);
}

.dark .error-message {
  background: #2d1f1f;
  border-color: #7c2d2d;
}

.error-content {
  margin-bottom: 1rem;
}

.error-content p {
  margin-top: 0.5rem;
  white-space: pre-wrap;
}

.retry-btn {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem 1rem;
  background: #c53030;
  color: white;
  border: none;
  border-radius: 6px;
  font-size: 0.875rem;
  cursor: pointer;
  transition: all 0.3s ease;
}

.retry-btn:hover {
  background: #9b2c2c;
  transform: translateY(-1px);
}

/* Stats Section */
.stats-section {
  margin-bottom: 2rem;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 1.5rem;
}

.stat-card {
  background: white;
  border-radius: 16px;
  padding: 1.5rem;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
  display: flex;
  align-items: center;
  gap: 1rem;
  border: 1px solid #e2e8f0;
  transition: all 0.3s ease;
}

.dark .stat-card {
  background: #2a2d33;
  border-color: rgba(32, 201, 151, 0.2);
}

.stat-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
}

.stat-icon {
  font-size: 2rem;
  width: 60px;
  height: 60px;
  background: linear-gradient(135deg, #3D8D7A, #2d6a5a);
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.stat-value {
  font-size: 1.875rem;
  font-weight: 700;
  color: #1e293b;
  margin-bottom: 0.25rem;
}

.dark .stat-value {
  color: #e2e8f0;
}

.stat-label {
  font-size: 0.875rem;
  color: #64748b;
  font-weight: 500;
}

.dark .stat-label {
  color: #94a3b8;
}

/* Subject Groups */
.subjects-section {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.subject-group {
  background: white;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
  border: 1px solid #e2e8f0;
  overflow: hidden;
}

.dark .subject-group {
  background: #2a2d33;
  border-color: rgba(32, 201, 151, 0.2);
}

.subject-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.5rem;
  border-bottom: 1px solid #e2e8f0;
  cursor: pointer;
  transition: all 0.3s ease;
}

.dark .subject-header {
  border-bottom-color: rgba(32, 201, 151, 0.2);
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
  background: linear-gradient(135deg, #3D8D7A, #2d6a5a);
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
}

.subject-name {
  font-size: 1.25rem;
  font-weight: 600;
  color: #1e293b;
  margin: 0;
}

.dark .subject-name {
  color: #e2e8f0;
}

.subject-count {
  font-size: 0.875rem;
  color: #64748b;
  margin: 0.25rem 0 0 0;
}

.dark .subject-count {
  color: #94a3b8;
}

.toggle-btn {
  width: 36px;
  height: 36px;
  border: none;
  background: #f1f5f9;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.3s ease;
}

.dark .toggle-btn {
  background: #1e2328;
}

.toggle-btn:hover {
  background: #e2e8f0;
}

.dark .toggle-btn:hover {
  background: #2a2f35;
}

.toggle-btn svg {
  transition: transform 0.3s ease;
}

.toggle-btn svg.rotated {
  transform: rotate(180deg);
}

/* Slide Transition */
.slide-enter-active, .slide-leave-active {
  transition: all 0.3s ease;
}

.slide-enter-from {
  opacity: 0;
  max-height: 0;
  transform: translateY(-10px);
}

.slide-enter-to {
  opacity: 1;
  max-height: 2000px;
  transform: translateY(0);
}

.slide-leave-from {
  opacity: 1;
  max-height: 2000px;
  transform: translateY(0);
}

.slide-leave-to {
  opacity: 0;
  max-height: 0;
  transform: translateY(-10px);
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
  border: 2px solid #e2e8f0;
  border-radius: 12px;
  margin-bottom: 1rem;
  cursor: pointer;
  transition: all 0.3s ease;
}

.dark .assessment-card {
  border-color: rgba(32, 201, 151, 0.2);
}

.assessment-card:hover {
  border-color: #20c997;
  background: rgba(163, 209, 198, 0.05);
  transform: translateX(4px);
  box-shadow: 0 4px 12px rgba(32, 201, 151, 0.15);
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
  color: #1e293b;
  margin: 0;
}

.dark .assessment-title {
  color: #e2e8f0;
}

.assessment-date {
  font-size: 0.875rem;
  color: #64748b;
}

.dark .assessment-date {
  color: #94a3b8;
}

.assessment-details {
  display: flex;
  gap: 1.5rem;
  font-size: 0.875rem;
  color: #64748b;
}

.dark .assessment-details {
  color: #94a3b8;
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
  color: white;
  font-weight: 700;
  font-size: 0.875rem;
}

.grade-letter.grade-a { background: #22c55e; }
.grade-letter.grade-b { background: #3b82f6; }
.grade-letter.grade-c { background: #f59e0b; }
.grade-letter.grade-f { background: #ef4444; }

.points {
  font-size: 0.75rem;
  color: #64748b;
  font-weight: 500;
}

.dark .points {
  color: #94a3b8;
}

.assessment-actions {
  width: 36px;
  height: 36px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #94a3b8;
  transition: all 0.3s ease;
}

.assessment-card:hover .assessment-actions {
  color: #20c997;
  transform: translateX(4px);
}

/* Empty State */
.empty-state {
  text-align: center;
  padding: 4rem 2rem;
  background: white;
  border-radius: 20px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
  border: 1px solid #e2e8f0;
}

.dark .empty-state {
  background: #2a2d33;
  border-color: rgba(32, 201, 151, 0.2);
}

.empty-icon {
  font-size: 4rem;
  margin-bottom: 1.5rem;
  opacity: 0.6;
}

.empty-state h3 {
  font-size: 1.5rem;
  font-weight: 700;
  color: #1e293b;
  margin-bottom: 0.5rem;
}

.dark .empty-state h3 {
  color: #e2e8f0;
}

.empty-state p {
  color: #64748b;
  margin-bottom: 2rem;
  font-size: 1.125rem;
}

.dark .empty-state p {
  color: #94a3b8;
}

.btn-primary {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.875rem 1.5rem;
  background: linear-gradient(135deg, #20c997, #17a085);
  color: white;
  border: none;
  border-radius: 10px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 4px 12px rgba(32, 201, 151, 0.3);
}

.btn-primary:hover {
  transform: translateY(-1px);
  box-shadow: 0 6px 16px rgba(32, 201, 151, 0.4);
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
  align-items: center;
  justify-content: center;
  z-index: 10000;
  padding: 1rem;
  backdrop-filter: blur(4px);
}

.modal-content {
  background: white;
  border-radius: 20px;
  max-width: 800px;
  width: 100%;
  max-height: 90vh;
  overflow-y: auto;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
}

.dark .modal-content {
  background: #2a2d33;
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.5rem 2rem;
  border-bottom: 1px solid #e2e8f0;
}

.dark .modal-header {
  border-bottom-color: rgba(32, 201, 151, 0.2);
}

.modal-header h2 {
  margin: 0;
  font-size: 1.5rem;
  font-weight: 700;
  color: #1e293b;
}

.dark .modal-header h2 {
  color: #e2e8f0;
}

.close-btn {
  width: 36px;
  height: 36px;
  border: none;
  background: #f1f5f9;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.3s ease;
}

.dark .close-btn {
  background: #1e2328;
}

.close-btn:hover {
  background: #e2e8f0;
  transform: rotate(90deg);
}

.dark .close-btn:hover {
  background: #2a2f35;
}

.modal-body {
  padding: 2rem;
}

.score-overview {
  display: flex;
  align-items: center;
  gap: 2rem;
  margin-bottom: 2rem;
  padding: 1.5rem;
  background: rgba(163, 209, 198, 0.05);
  border-radius: 12px;
}

.score-circle-large {
  width: 120px;
  height: 120px;
  border-radius: 50%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  border: 4px solid;
}

.score-circle-large.excellent { border-color: #22c55e; background: rgba(34, 197, 94, 0.1); }
.score-circle-large.good { border-color: #3b82f6; background: rgba(59, 130, 246, 0.1); }
.score-circle-large.average { border-color: #f59e0b; background: rgba(245, 158, 11, 0.1); }
.score-circle-large.below-average { border-color: #ef4444; background: rgba(239, 68, 68, 0.1); }
.score-circle-large.poor { border-color: #dc2626; background: rgba(220, 38, 38, 0.1); }

.score-value-large {
  font-size: 2rem;
  font-weight: 700;
  color: #1e293b;
}

.dark .score-value-large {
  color: #e2e8f0;
}

.score-label {
  font-size: 0.85rem;
  color: #64748b;
  margin-top: 0.25rem;
}

.dark .score-label {
  color: #94a3b8;
}

.score-details {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.detail-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.75rem;
  background: white;
  border-radius: 8px;
}

.dark .detail-item {
  background: #1e2328;
}

.detail-label {
  font-weight: 600;
  color: #64748b;
}

.dark .detail-label {
  color: #94a3b8;
}

.detail-value {
  font-weight: 700;
  color: #1e293b;
}

.dark .detail-value {
  color: #e2e8f0;
}

.feedback-section {
  margin-bottom: 2rem;
}

.feedback-section h3 {
  color: #1e293b;
  margin-bottom: 1.5rem;
  font-size: 1.25rem;
  font-weight: 700;
}

.dark .feedback-section h3 {
  color: #e2e8f0;
}

.feedback-block {
  margin-bottom: 1.5rem;
  padding: 1rem;
  background: rgba(163, 209, 198, 0.05);
  border-radius: 10px;
}

.feedback-block h4 {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin-bottom: 0.75rem;
  font-size: 1.1rem;
  font-weight: 600;
  color: #1e293b;
}

.dark .feedback-block h4 {
  color: #e2e8f0;
}

.feedback-icon {
  font-size: 1.2rem;
}

.feedback-list {
  margin: 0;
  padding-left: 1.5rem;
}

.feedback-list li {
  margin-bottom: 0.5rem;
  line-height: 1.5;
}

.feedback-list.strengths li { color: #166534; }
.feedback-list.weaknesses li { color: #dc2626; }
.feedback-list.recommendations li { color: #1d4ed8; }

.detailed-text {
  line-height: 1.6;
  color: #475569;
  margin: 0;
}

.dark .detailed-text {
  color: #94a3b8;
}

.modal-footer {
  display: flex;
  gap: 1rem;
  justify-content: flex-end;
  padding: 1.5rem 2rem;
  border-top: 1px solid #e2e8f0;
}

.dark .modal-footer {
  border-top-color: rgba(32, 201, 151, 0.2);
}

.btn-secondary {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1.25rem;
  background: white;
  color: #475569;
  border: 2px solid #e2e8f0;
  border-radius: 8px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
}

.dark .btn-secondary {
  background: #1e2328;
  color: #e2e8f0;
  border-color: rgba(32, 201, 151, 0.2);
}

.btn-secondary:hover {
  background: #f8fafc;
  border-color: #20c997;
  transform: translateY(-1px);
}

.dark .btn-secondary:hover {
  background: #2a2f35;
  border-color: #20c997;
}

/* Responsive Design */
@media (max-width: 768px) {
  .navbar-center {
    gap: 0.25rem;
  }
  
  .nav-item {
    padding: 0.5rem 1rem;
    font-size: 0.7rem;
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
    flex-wrap: wrap;
  }
  
  .assessment-score {
    justify-content: center;
    margin: 0;
  }
  
  .score-overview {
    flex-direction: column;
    text-align: center;
  }
  
  .brand-name {
    display: none;
  }
}
</style>