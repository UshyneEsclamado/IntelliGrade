<template>
  <div class="dashboard-container" :class="{ 'dark': isDarkMode }">
    <!-- Top Navigation Bar (Clean) -->
    <nav class="top-navbar">
      <div class="navbar-content">
        <!-- Left: Logo and Brand -->
        <div class="navbar-left">
          <div class="brand-logo">
            <img src="@/assets/LOGO WAY BG.png" alt="IntelliGrade" class="logo-img" />
            <span class="brand-name">IntelliGrade</span>
          </div>
        </div>
        
        <!-- Center: Empty space for clean look -->
        <div class="navbar-center">
        </div>
        
        <!-- Right: User Profile and Notifications -->
        <div class="navbar-right">
          <!-- Notification Bell -->
          <div class="notif-wrapper">
            <button class="nav-icon-btn rounded-bg" aria-label="Notifications">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                <path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"></path>
                <path d="M13.73 21a2 2 0 0 1-3.46 0"></path>
              </svg>
            </button>
          </div>
          
          <!-- Refresh Button -->
          <button @click="refreshData" class="nav-icon-btn rounded-bg" :disabled="loading" aria-label="Refresh">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M21.5 2v6h-6M2.5 22v-6h6M2 11.5a10 10 0 0 1 18.8-4.3M22 12.5a10 10 0 0 1-18.8 4.2"/>
            </svg>
          </button>
          
          <!-- User Profile -->
          <div class="user-profile-wrapper">
            <div class="user-profile rounded-bg">
              <div class="user-avatar">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
                  <circle cx="12" cy="7" r="4"></circle>
                </svg>
              </div>
              <span class="user-name">Teacher</span>
              <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" class="dropdown-arrow">
                <path d="M7 10l5 5 5-5z"/>
              </svg>
            </div>
          </div>
        </div>
      </div>
    </nav>

    <!-- Sidebar Navigation -->
    <aside class="sidebar" style="background:#3D8D7A; border-right:none;">
      <nav class="sidebar-nav">
        <router-link to="/teacher/dashboard" class="sidebar-item rounded-bg">
          <div class="sidebar-icon">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M10 20v-6h4v6m5-8h3L12 3 2 12h3v8h5v-6h4v6h5v-8z" />
            </svg>
          </div>
          <span class="sidebar-tooltip">Dashboard</span>
        </router-link>
        <router-link to="/teacher/subjects" class="sidebar-item rounded-bg">
          <div class="sidebar-icon">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <rect x="3" y="7" width="18" height="13" rx="2" />
              <path d="M3 7l9-4 9 4" />
            </svg>
          </div>
          <span class="sidebar-tooltip">Classes</span>
        </router-link>
        <router-link to="/teacher/gradebook" class="sidebar-item rounded-bg">
          <div class="sidebar-icon">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <rect x="4" y="4" width="16" height="16" rx="2" />
              <path d="M8 2v4M16 2v4" />
            </svg>
          </div>
          <span class="sidebar-tooltip">Gradebook</span>
        </router-link>
        <router-link to="/teacher/upload-assessment" class="sidebar-item rounded-bg">
          <div class="sidebar-icon">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M12 19V6M5 12l7-7 7 7" />
              <rect x="5" y="19" width="14" height="2" rx="1" />
            </svg>
          </div>
          <span class="sidebar-tooltip">Upload Assessment</span>
        </router-link>
        <router-link to="/teacher/analytics" class="sidebar-item rounded-bg">
          <div class="sidebar-icon">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <rect x="3" y="12" width="4" height="8" />
              <rect x="10" y="8" width="4" height="12" />
              <rect x="17" y="4" width="4" height="16" />
            </svg>
          </div>
          <span class="sidebar-tooltip">Analytics</span>
        </router-link>
        <router-link to="/teacher/messages" class="sidebar-item rounded-bg">
          <div class="sidebar-icon">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <rect x="3" y="5" width="18" height="14" rx="2" />
              <path d="M3 5l9 7 9-7" />
            </svg>
          </div>
          <span class="sidebar-tooltip">Messages</span>
        </router-link>
      </nav>
    </aside>

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
      <div v-if="loading && assessments.length === 0" class="loading-overlay">
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
      <div v-if="!loading || assessments.length > 0" class="content-grid">
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
          <div v-for="subject in groupedAssessments" :key="subject.name" class="content-card">
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
          <div v-if="selectedAssessment.feedback" class="ai-feedback">
            <h3>📊 AI Analysis & Feedback</h3>
            
            <div v-if="selectedAssessment.feedback.strengths && selectedAssessment.feedback.strengths.length > 0" class="feedback-section">
              <h4><span class="feedback-icon">💪</span> Strengths</h4>
              <ul class="feedback-list strengths">
                <li v-for="(strength, index) in selectedAssessment.feedback.strengths" :key="index">{{ strength }}</li>
              </ul>
            </div>

            <div v-if="selectedAssessment.feedback.weaknesses && selectedAssessment.feedback.weaknesses.length > 0" class="feedback-section">
              <h4><span class="feedback-icon">🎯</span> Areas for Improvement</h4>
              <ul class="feedback-list weaknesses">
                <li v-for="(weakness, index) in selectedAssessment.feedback.weaknesses" :key="index">{{ weakness }}</li>
              </ul>
            </div>

            <div v-if="selectedAssessment.feedback.recommendations && selectedAssessment.feedback.recommendations.length > 0" class="feedback-section">
              <h4><span class="feedback-icon">📚</span> Recommendations</h4>
              <ul class="feedback-list recommendations">
                <li v-for="(rec, index) in selectedAssessment.feedback.recommendations" :key="index">{{ rec }}</li>
              </ul>
            </div>

            <div v-if="selectedAssessment.feedback.detailedAnalysis || selectedAssessment.feedback.detailed_analysis" class="detailed-analysis">
              <h4><span class="feedback-icon">🔍</span> Detailed Analysis</h4>
              <p>{{ selectedAssessment.feedback.detailedAnalysis || selectedAssessment.feedback.detailed_analysis }}</p>
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
import { ref, computed, onMounted, onUnmounted } from 'vue';
import { useRouter } from 'vue-router';
import { useDarkMode } from '../../composables/useDarkMode.js';
import { supabase } from '@/Supabase.js';

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
    const autoRefreshInterval = ref(null);

    // Helper function to get letter grade from percentage
    const getLetterGradeFromPercentage = (percentage) => {
      if (percentage >= 90) return 'A';
      if (percentage >= 80) return 'B';
      if (percentage >= 70) return 'C';
      if (percentage >= 60) return 'D';
      return 'F';
    };

    // Fetch assessment history from Supabase with debugging
    const fetchAssessmentHistory = async () => {
      loading.value = true;
      error.value = null;
      
      try {
        console.log('🔄 Starting to fetch assessment history...');
        console.log('📡 Supabase client:', supabase ? '✅ Initialized' : '❌ Not initialized');

        // First, check if we can connect to Supabase
        const { data: testConnection, error: testError } = await supabase
          .from('grading_results')
          .select('count', { count: 'exact' });

        if (testError) {
          console.error('❌ Connection test failed:', testError);
          throw new Error(`Cannot connect to database: ${testError.message}`);
        }

        console.log('✅ Database connection successful');
        console.log('📊 Total records in grading_results:', testConnection);

        // Fetch grading results with all required fields
        const { data: gradingData, error: gradingError, status } = await supabase
          .from('grading_results')
          .select('*')
          .order('graded_at', { ascending: false });

        console.log('🔍 Query status:', status);
        console.log('📋 Raw response:', gradingData);
        console.log('⚠️ Error response:', gradingError);

        if (gradingError) {
          console.error('❌ Supabase query error:', gradingError);
          throw new Error(`Database query failed: ${gradingError.message}`);
        }

        console.log('✅ Query successful');
        console.log(`📦 Received ${gradingData ? gradingData.length : 0} records`);

        if (gradingData && Array.isArray(gradingData) && gradingData.length > 0) {
          console.log('🎯 Processing assessments...');
          
          // Transform data to match component structure
          assessments.value = gradingData.map((result, index) => {
            console.log(`   [${index + 1}] Processing:`, {
              student: result.student_name,
              title: result.assessment_title,
              subject: result.subject,
              percentage: result.percentage
            });
            
            return {
              id: result.id || `assessment-${index}`,
              title: result.assessment_title || 'Untitled Assessment',
              assessment_title: result.assessment_title || 'Untitled Assessment',
              studentName: result.student_name || 'Unknown Student',
              student_name: result.student_name || 'Unknown Student',
              subject: result.subject || 'Uncategorized',
              percentage: parseFloat(result.percentage) || 0,
              pointsEarned: parseFloat(result.score) || 0,
              points_earned: parseFloat(result.score) || 0,
              totalPoints: parseFloat(result.max_score) || 0,
              total_points: parseFloat(result.max_score) || 0,
              totalQuestions: parseInt(result.total_questions) || 0,
              total_questions: parseInt(result.total_questions) || 0,
              correctAnswers: parseInt(result.correct_answers) || 0,
              correct_answers: parseInt(result.correct_answers) || 0,
              incorrectAnswers: parseInt(result.incorrect_answers) || 0,
              incorrect_answers: parseInt(result.incorrect_answers) || 0,
              letterGrade: result.letter_grade || getLetterGradeFromPercentage(result.percentage),
              letter_grade: result.letter_grade || getLetterGradeFromPercentage(result.percentage),
              checkedAt: result.graded_at || new Date().toISOString(),
              checked_at: result.graded_at || new Date().toISOString(),
              checkingMethod: result.ai_used ? 'AI-Powered' : 'Rule-based',
              checking_method: result.grading_method || (result.ai_used ? 'AI-Powered' : 'Rule-based'),
              aiUsed: result.ai_used || false,
              ai_used: result.ai_used || false,
              aiModel: result.ai_model || null,
              aiConfidence: result.ai_confidence || null,
              processingTime: result.processing_time || null,
              feedback: {
                strengths: Array.isArray(result.strengths) ? result.strengths : (result.strengths ? [result.strengths] : []),
                weaknesses: Array.isArray(result.weaknesses) ? result.weaknesses : (result.weaknesses ? [result.weaknesses] : []),
                recommendations: Array.isArray(result.recommendations) ? result.recommendations : (result.recommendations ? [result.recommendations] : []),
                detailedAnalysis: result.detailed_analysis || '',
                detailed_analysis: result.detailed_analysis || ''
              },
              questionBreakdown: result.question_breakdown || [],
              question_breakdown: result.question_breakdown || []
            };
          });
          
          console.log(`✅ Successfully transformed ${assessments.value.length} assessments`);
          
          // Auto-expand all subjects initially if we have data
          if (assessments.value.length > 0) {
            const uniqueSubjects = [...new Set(assessments.value.map(a => a.subject))];
            expandedSubjects.value = uniqueSubjects;
            console.log(`📚 Found ${uniqueSubjects.length} subjects:`, uniqueSubjects);
          }
        } else {
          console.warn('⚠️ No assessment data found');
          console.warn('   gradingData:', gradingData);
          console.warn('   Is array?', Array.isArray(gradingData));
          console.warn('   Length:', gradingData ? gradingData.length : 'undefined');
          assessments.value = [];
          expandedSubjects.value = [];
          error.value = 'No assessments found in database. Have you graded any assessments yet?';
        }
      } catch (err) {
        console.error('❌ Critical error:', err);
        console.error('   Stack:', err.stack);
        error.value = err.message || 'Failed to load assessment history. Please check console for details.';
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
          const dateA = new Date(a.checked_at || a.checkedAt || 0);
          const dateB = new Date(b.checked_at || b.checkedAt || 0);
          return dateB - dateA;
        });
      });
      
      // Sort groups alphabetically
      return Object.values(groups).sort((a, b) => a.name.localeCompare(b.name));
    });

    const totalAssessments = computed(() => assessments.value.length);
    
    const totalSubjects = computed(() => groupedAssessments.value.length);
    
    const averageScore = computed(() => {
      if (assessments.value.length === 0) return 0;
      const total = assessments.value.reduce((sum, assessment) => {
        return sum + (parseFloat(assessment.percentage) || 0);
      }, 0);
      return Math.round(total / assessments.value.length);
    });
    
    const recentChecks = computed(() => {
      const oneWeekAgo = new Date();
      oneWeekAgo.setDate(oneWeekAgo.getDate() - 7);
      
      return assessments.value.filter(assessment => {
        const checkedDate = new Date(assessment.checked_at || assessment.checkedAt || new Date());
        return checkedDate > oneWeekAgo;
      }).length;
    });

    // Methods
    const refreshData = async () => {
      console.log('🔄 Manually refreshing assessment data...');
      await fetchAssessmentHistory();
    };

    const goToUpload = () => {
      console.log('➡️ Navigating to upload assessment page');
      router.push('/teacher/upload-assessment');
    };

    const toggleSubject = (subjectName) => {
      const index = expandedSubjects.value.indexOf(subjectName);
      if (index > -1) {
        expandedSubjects.value.splice(index, 1);
        console.log(`📦 Collapsed subject: ${subjectName}`);
      } else {
        expandedSubjects.value.push(subjectName);
        console.log(`📂 Expanded subject: ${subjectName}`);
      }
    };

    const viewAssessment = (assessment) => {
      console.log('👁️ Viewing assessment details:', assessment);
      selectedAssessment.value = { ...assessment };
    };

    const closeModal = () => {
      console.log('❌ Closing assessment modal');
      selectedAssessment.value = null;
    };

    const formatDate = (dateString) => {
      if (!dateString) return 'N/A';
      try {
        const date = new Date(dateString);
        if (isNaN(date.getTime())) return 'N/A';
        return date.toLocaleDateString('en-US', {
          month: 'short',
          day: 'numeric',
          hour: '2-digit',
          minute: '2-digit'
        });
      } catch (e) {
        console.error('Error formatting date:', dateString, e);
        return 'N/A';
      }
    };

    const formatDateLong = (dateString) => {
      if (!dateString) return 'N/A';
      try {
        const date = new Date(dateString);
        if (isNaN(date.getTime())) return 'N/A';
        return date.toLocaleDateString('en-US', {
          weekday: 'long',
          year: 'numeric',
          month: 'long',
          day: 'numeric',
          hour: '2-digit',
          minute: '2-digit'
        });
      } catch (e) {
        console.error('Error formatting long date:', dateString, e);
        return 'N/A';
      }
    };

    const getScoreClass = (percentage) => {
      const pct = parseFloat(percentage) || 0;
      if (pct >= 90) return 'excellent';
      if (pct >= 80) return 'good';
      if (pct >= 70) return 'average';
      if (pct >= 60) return 'below-average';
      return 'poor';
    };

    const getLetterGrade = (percentage) => {
      const pct = parseFloat(percentage) || 0;
      if (pct >= 90) return 'A';
      if (pct >= 80) return 'B';
      if (pct >= 70) return 'C';
      if (pct >= 60) return 'D';
      return 'F';
    };

    const getGradeClass = (percentage) => {
      const pct = parseFloat(percentage) || 0;
      if (pct >= 80) return 'grade-a';
      if (pct >= 70) return 'grade-b';
      if (pct >= 60) return 'grade-c';
      return 'grade-f';
    };

    const downloadReport = (assessment) => {
      try {
        const reportData = {
          student: assessment.studentName || assessment.student_name,
          assessment: assessment.title || assessment.assessment_title,
          subject: assessment.subject,
          score: assessment.percentage,
          pointsEarned: assessment.pointsEarned || assessment.points_earned,
          totalPoints: assessment.totalPoints || assessment.total_points,
          totalQuestions: assessment.totalQuestions || assessment.total_questions,
          correctAnswers: assessment.correctAnswers || assessment.correct_answers,
          incorrectAnswers: assessment.incorrectAnswers || assessment.incorrect_answers,
          letterGrade: assessment.letterGrade || assessment.letter_grade,
          checkedAt: assessment.checkedAt || assessment.checked_at,
          checkingMethod: assessment.checkingMethod || assessment.checking_method,
          aiUsed: assessment.aiUsed || assessment.ai_used,
          aiModel: assessment.aiModel,
          aiConfidence: assessment.aiConfidence,
          processingTime: assessment.processingTime,
          feedback: assessment.feedback,
          questionBreakdown: assessment.questionBreakdown || assessment.question_breakdown
        };
        
        const blob = new Blob([JSON.stringify(reportData, null, 2)], { type: 'application/json' });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = `${(assessment.studentName || assessment.student_name || 'student').replace(/\s+/g, '_')}_${(assessment.title || assessment.assessment_title || 'assessment').replace(/\s+/g, '_')}_report_${new Date().toISOString().split('T')[0]}.json`;
        a.click();
        URL.revokeObjectURL(url);
        console.log('📥 Report downloaded successfully');
      } catch (err) {
        console.error('❌ Error downloading report:', err);
        alert('Failed to download report. Please try again.');
      }
    };

    // Lifecycle hooks
    onMounted(() => {
      console.log('🚀 AssessmentHistory component mounted');
      console.log('🕐 Current time:', new Date().toISOString());
      
      // Fetch data immediately
      fetchAssessmentHistory();
      
      // Set up auto-refresh every 30 seconds
      autoRefreshInterval.value = setInterval(() => {
        if (!loading.value) {
          console.log('⏱️ Auto-refresh triggered at', new Date().toISOString());
          fetchAssessmentHistory();
        }
      }, 30000);
    });

    onUnmounted(() => {
      console.log('🛑 AssessmentHistory component unmounted - clearing auto-refresh');
      if (autoRefreshInterval.value) {
        clearInterval(autoRefreshInterval.value);
      }
    });

    return {
      // State
      isDarkMode,
      assessments,
      loading,
      error,
      expandedSubjects,
      selectedAssessment,
      
      // Computed
      groupedAssessments,
      totalAssessments,
      totalSubjects,
      averageScore,
      recentChecks,
      
      // Methods
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

/* Dashboard container setup */
.dashboard-container {
  display: flex;
  flex-direction: row;
  width: 100vw;
  height: 100vh;
  min-height: 100vh;
  background: #f8fafc;
  font-family: 'Inter', sans-serif;
  overflow: hidden;
}

.dark .dashboard-container {
  background: #0f172a;
}

/* Top Navigation Bar (Greenish Theme) */
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
  max-width: 600px;
}

.navbar-right {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.nav-icon-btn {
  width: 44px;
  height: 44px;
  background: rgba(255, 255, 255, 0.15);
  border: none;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: opacity 0.2s;
  z-index: 10;
}

.sidebar-item:hover .sidebar-tooltip {
  opacity: 1;
  pointer-events: auto;
}

/* Main Content */
.main-content {
  flex: 1;
  display: flex;
  flex-direction: column;
  position: relative;
  width: calc(100% - 80px);
  margin-left: 80px;
  margin-top: 64px;
  padding: 32px 40px 40px 40px;
  min-height: calc(100vh - 64px);
  max-height: calc(100vh - 64px);
  overflow-y: auto;
  background: #f8fafc;
  padding-bottom: 2rem;
}

.dark .main-content {
  background: #0f172a;
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

.header-actions {
  display: flex;
  gap: 1rem;
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

/* Content Grid */
.content-grid {
  display: grid;
  gap: 1.5rem;
  grid-template-columns: 1fr;
}

/* Loading Overlay */
.loading-overlay {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 4rem 2rem;
  background: white;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
}

.dark .loading-overlay {
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

.loading-overlay p {
  color: #64748b;
  font-size: 0.95rem;
}

.dark .loading-overlay p {
  color: #94a3b8;
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

.stat-info {
  flex: 1;
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

.content-card {
  background: white;
  border-radius: 20px;
  box-shadow: 0 4px 20px rgba(32, 201, 151, 0.08);
  border: 2px solid rgba(163, 209, 198, 0.3);
  transition: all 0.3s ease;
  overflow: hidden;
}

.dark .content-card {
  background: #23272b;
  border-color: rgba(32, 201, 151, 0.3);
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
}

.content-card:hover {
  box-shadow: 0 8px 25px rgba(32, 201, 151, 0.15);
  border-color: rgba(32, 201, 151, 0.6);
  transform: translateY(-2px);
}

.dark .content-card:hover {
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.5);
  border-color: rgba(32, 201, 151, 0.6);
}

.subject-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.5rem;
  border-bottom: 2px solid rgba(163, 209, 198, 0.15);
  cursor: pointer;
  transition: all 0.3s ease;
  background: linear-gradient(135deg, rgba(32, 201, 151, 0.05), rgba(163, 209, 198, 0.05));
}

.dark .subject-header {
  border-bottom: 2px solid rgba(32, 201, 151, 0.2);
  background: linear-gradient(135deg, rgba(32, 201, 151, 0.08), rgba(163, 209, 198, 0.08));
}

.subject-header:hover {
  background: rgba(163, 209, 198, 0.1);
}

.dark .subject-header:hover {
  background: rgba(32, 201, 151, 0.12);
}

.subject-info {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.subject-icon-large {
  width: 48px;
  height: 48px;
  background: #3D8D7A;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  box-shadow: 0 2px 8px rgba(61, 141, 122, 0.3);
}

.subject-name {
  font-size: 1.25rem;
  font-weight: 700;
  color: #2d3748;
  margin: 0 0 0.25rem 0;
  background: linear-gradient(135deg, #20c997, #17a085);
  background-clip: text;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.dark .subject-name {
  color: #e2e8f0;
  background: linear-gradient(135deg, #20c997, #17a085);
  background-clip: text;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.subject-count {
  font-size: 0.85rem;
  color: #718096;
  margin: 0;
  font-weight: 500;
}

.dark .subject-count {
  color: #a0aec0;
}

.toggle-btn {
  width: 36px;
  height: 36px;
  border: none;
  background: rgba(255, 255, 255, 0.8);
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.3s ease;
}

.dark .toggle-btn {
  background: rgba(45, 55, 72, 0.8);
}

.toggle-btn:hover {
  background: white;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.dark .toggle-btn:hover {
  background: #2d3748;
}

.toggle-btn svg {
  transition: transform 0.3s ease;
  color: #4a5568;
}

.dark .toggle-btn svg {
  color: #e2e8f0;
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
  padding: 1.5rem;
}

.assessment-card {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1.25rem;
  border: 2px solid rgba(163, 209, 198, 0.3);
  border-radius: 12px;
  margin-bottom: 1rem;
  cursor: pointer;
  transition: all 0.3s ease;
  background: rgba(255, 255, 255, 0.8);
}

.dark .assessment-card {
  border-color: rgba(32, 201, 151, 0.2);
  background: rgba(45, 55, 72, 0.8);
}

.assessment-card:hover {
  border-color: #20c997;
  background: rgba(32, 201, 151, 0.05);
  transform: translateX(4px);
  box-shadow: 0 4px 12px rgba(32, 201, 151, 0.15);
}

.dark .assessment-card:hover {
  background: rgba(32, 201, 151, 0.12);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
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
  box-shadow: 0 4px 20px rgba(32, 201, 151, 0.08);
  border: 2px solid rgba(163, 209, 198, 0.3);
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
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.btn-primary:hover {
  background: linear-gradient(135deg, #17a085, #138f75);
  transform: translateY(-2px);
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
  animation: fadeIn 0.3s ease;
}

@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

.modal-content {
  background: white;
  border-radius: 20px;
  max-width: 800px;
  width: 100%;
  max-height: 90vh;
  overflow-y: auto;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
  animation: slideUp 0.3s ease;
}

@keyframes slideUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@media (max-width: 1024px) {
  .main-content {
    padding: 1rem;
  }
  
  .stats-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 768px) {
  .main-content {
    width: 100%;
    margin-left: 0;
    padding: 1rem;
  }
  
  .sidebar {
    display: none;
  }
  
  .brand-name {
    display: none;
  }
  
  .navbar-right {
    gap: 0.5rem;
  }
  
  .user-name {
    display: none;
  }
  
  .stats-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 1rem;
  }
  
  .stat-card {
    padding: 1rem;
  }
  
  .stat-icon {
    width: 50px;
    height: 50px;
    font-size: 1.5rem;
  }
  
  .stat-value {
    font-size: 1.5rem;
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
    gap: 1rem;
  }
  
  .assessment-score {
    justify-content: center;
    margin: 0;
  }
  
  .score-overview {
    flex-direction: column;
    text-align: center;
  }
  
  .modal-content {
    max-width: 95%;
    margin: 1rem;
  }
  
  .modal-header {
    padding: 1rem;
  }
  
  .modal-body {
    padding: 1rem;
  }
  
  .modal-footer {
    padding: 1rem;
    flex-direction: column;
  }
  
  .btn-primary,
  .btn-secondary {
    width: 100%;
    justify-content: center;
  }
}

@media (max-width: 480px) {
  .page-header {
    padding: 1rem;
  }
  
  .header-left {
    flex-direction: column;
    align-items: flex-start;
  }
  
  .header-icon {
    width: 48px;
    height: 48px;
  }
  
  .header-title {
    font-size: 1.25rem;
  }
  
  .header-subtitle {
    font-size: 0.85rem;
  }
  
  .header-actions {
    width: 100%;
  }
  
  .upload-btn {
    width: 100%;
    justify-content: center;
  }
  
  .stats-grid {
    grid-template-columns: 1fr;
  }
  
  .subject-header {
    padding: 1rem;
  }
  
  .subject-icon-large {
    width: 40px;
    height: 40px;
  }
  
  .subject-name {
    font-size: 1.1rem;
  }
  
  .assessments-list {
    padding: 1rem;
  }
  
  .assessment-card {
    padding: 1rem;
  }
}

.dark .modal-content {
  background: #2a2d33;
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.5rem 2rem;
  border-bottom: 2px solid rgba(163, 209, 198, 0.15);
  background: linear-gradient(135deg, rgba(32, 201, 151, 0.05), rgba(163, 209, 198, 0.05));
}

.dark .modal-header {
  border-bottom: 2px solid rgba(32, 201, 151, 0.2);
  background: linear-gradient(135deg, rgba(32, 201, 151, 0.08), rgba(163, 209, 198, 0.08));
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
  background: rgba(255, 255, 255, 0.8);
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.3s ease;
}

.dark .close-btn {
  background: rgba(45, 55, 72, 0.8);
}

.close-btn:hover {
  background: #f1f5f9;
  transform: rotate(90deg);
}

.dark .close-btn:hover {
  background: #2d3748;
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
  background: rgba(163, 209, 198, 0.1);
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
  background: rgba(255, 255, 255, 0.8);
  border-radius: 8px;
}

.dark .detail-item {
  background: rgba(45, 55, 72, 0.8);
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

/* AI Feedback */
.ai-feedback {
  margin-bottom: 2rem;
}

.ai-feedback h3 {
  color: #1e293b;
  margin-bottom: 1.5rem;
  font-size: 1.25rem;
  font-weight: 700;
}

.dark .ai-feedback h3 {
  color: #e2e8f0;
}

.feedback-section {
  margin-bottom: 1.5rem;
  padding: 1rem;
  background: rgba(255, 255, 255, 0.6);
  border-radius: 10px;
}

.dark .feedback-section {
  background: rgba(45, 55, 72, 0.6);
}

.feedback-section h4 {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin-bottom: 0.75rem;
  font-size: 1.1rem;
  font-weight: 600;
  color: #1e293b;
}

.dark .feedback-section h4 {
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

.detailed-analysis {
  padding: 1rem;
  background: rgba(179, 216, 168, 0.1);
  border-radius: 8px;
  border-left: 4px solid #3D8D7A;
}

.dark .detailed-analysis {
  background: rgba(32, 201, 151, 0.12);
}

.detailed-analysis h4 {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin-bottom: 0.75rem;
  color: #1e293b;
}

.dark .detailed-analysis h4 {
  color: #e2e8f0;
}

.detailed-analysis p {
  line-height: 1.6;
  color: #475569;
  margin: 0;
}

.dark .detailed-analysis p {
  color: #94a3b8;
}

.modal-footer {
  display: flex;
  gap: 1rem;
  justify-content: flex-end;
  padding: 1.5rem 2rem;
  border-top: 2px solid rgba(163, 209, 198, 0.15);
  background: linear-gradient(135deg, rgba(32, 201, 151, 0.02), rgba(163, 209, 198, 0.02));
}

.dark .modal-footer {
  border-top: 2px solid rgba(32, 201, 151, 0.2);
  background: linear-gradient(135deg, rgba(32, 201, 151, 0.05), rgba(163, 209, 198, 0.05));
}

.btn-secondary {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1.25rem;
  background: white;
  color: #475569;
  border: 2px solid rgba(163, 209, 198, 0.4);
  border-radius: 8px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 4px 15px rgba(163, 209, 198, 0.2);
}

.dark .btn-secondary {
  background: #2d3748;
  color: #e2e8f0;
  border: 2px solid rgba(32, 201, 151, 0.3);
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
}

.btn-secondary:hover {
  background: rgba(32, 201, 151, 0.05);
  border-color: #20c997;
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(163, 209, 198, 0.3);
}

.dark .btn-secondary:hover {
  background: rgba(32, 201, 151, 0.1);
  border-color: #20c997;
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.4);
}

/* Responsive Design */
@media (max-width: 1200px) {
  .main-content {
    padding: 1.5rem all 0.2s ease;
  color: rgba(255, 255, 255, 0.9);
  position: relative;
}
}

.nav-icon-btn:hover {
  background: rgba(255, 255, 255, 0.25);
  color: white;
}

.nav-icon-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.user-profile-wrapper {
  position: relative;
}

.user-profile {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.5rem 0.75rem;
  border-radius: 12px;
  transition: background 0.2s;
  cursor: pointer;
}

.user-profile:hover {
  background: rgba(255, 255, 255, 0.1);
}

.user-avatar {
  width: 36px;
  height: 36px;
  background: rgba(255, 255, 255, 0.2);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
}

.user-name {
  font-size: 0.9rem;
  font-weight: 600;
  color: white;
}

.dropdown-arrow {
  color: rgba(255, 255, 255, 0.8);
  transition: transform 0.2s;
}

.user-profile:hover .dropdown-arrow {
  transform: rotate(180deg);
}

/* Rounded semi-transparent backgrounds for sidebar and navbar icons/buttons */
.rounded-bg {
  background: rgba(255,255,255,0.13);
  border-radius: 16px;
  transition: background 0.2s;
}

.rounded-bg:hover {
  background: rgba(255,255,255,0.22);
}

/* Sidebar Navigation */
.sidebar {
  position: fixed;
  top: 64px;
  left: 0;
  width: 80px;
  height: calc(100vh - 64px);
  background: #3D8D7A;
  border-right: none;
  z-index: 900;
  box-shadow: 2px 0 10px rgba(0, 0, 0, 0.05);
  overflow: visible;
}

.sidebar-nav {
  padding: 2rem 0.5rem 1rem 0.5rem;
}

.sidebar-item {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 56px;
  width: 56px;
  margin: 8px 0;
  border-radius: 12px;
  transition: background 0.2s, box-shadow 0.2s;
  cursor: pointer;
  position: relative;
  text-decoration: none;
}

.sidebar-item:hover {
  background: rgba(255,255,255,0.22);
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
}

.sidebar-item.active {
  border: 2px solid #fff;
  background: rgba(255, 255, 255, 0.13);
  box-sizing: border-box;
}

.sidebar-icon svg {
  display: block;
}

.sidebar-tooltip {
  position: absolute;
  left: 60px;
  top: 50%;
  transform: translateY(-50%);
  background: #fff;
  color: #3D8D7A;
  padding: 4px 12px;
  border-radius: 6px;
  font-size: 14px;
  font-family: Inter, sans-serif;
  white-space: nowrap;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  opacity: 0;
  pointer-events: none;
transition: opacity 0.2s;
  z-index: 10;
}

.sidebar-item:hover .sidebar-tooltip {
  opacity: 1;
  pointer-events: auto;
}

/* Responsive Design continuation */
@media (max-width: 1200px) {
  .main-content {
    padding: 1.5rem;
  }
}

@media (max-width: 1024px) {
  .main-content {
    padding: 1rem;
  }
  
  .stats-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 768px) {
  .main-content {
    width: 100%;
    margin-left: 0;
    padding: 1rem;
  }
  
  .sidebar {
    display: none;
  }
  
  .brand-name {
    display: none;
  }
  
  .navbar-right {
    gap: 0.5rem;
  }
  
  .user-name {
    display: none;
  }
  
  .stats-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 1rem;
  }
  
  .stat-card {
    padding: 1rem;
  }
  
  .stat-icon {
    width: 50px;
    height: 50px;
    font-size: 1.5rem;
  }
  
  .stat-value {
    font-size: 1.5rem;
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
    gap: 1rem;
  }
  
  .assessment-score {
    justify-content: center;
    margin: 0;
  }
  
  .score-overview {
    flex-direction: column;
    text-align: center;
  }
  
  .modal-content {
    max-width: 95%;
    margin: 1rem;
  }
  
  .modal-header {
    padding: 1rem;
  }
  
  .modal-body {
    padding: 1rem;
  }
  
  .modal-footer {
    padding: 1rem;
    flex-direction: column;
  }
  
  .btn-primary,
  .btn-secondary {
    width: 100%;
    justify-content: center;
  }
}

@media (max-width: 480px) {
  .page-header {
    padding: 1rem;
  }
  
  .header-left {
    flex-direction: column;
    align-items: flex-start;
  }
  
  .header-icon {
    width: 48px;
    height: 48px;
  }
  
  .header-title {
    font-size: 1.25rem;
  }
  
  .header-subtitle {
    font-size: 0.85rem;
  }
  
  .header-actions {
    width: 100%;
  }
  
  .upload-btn {
    width: 100%;
    justify-content: center;
  }
  
  .stats-grid {
    grid-template-columns: 1fr;
  }
  
  .subject-header {
    padding: 1rem;
  }
  
  .subject-icon-large {
    width: 40px;
    height: 40px;
  }
  
  .subject-name {
    font-size: 1.1rem;
  }
  
  .assessments-list {
    padding: 1rem;
  }
  
  .assessment-card {
    padding: 1rem;
  }
}
</style>