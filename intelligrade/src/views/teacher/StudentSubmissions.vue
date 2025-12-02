<template>
  <div class="student-submissions">
    <!-- Top Navigation Bar -->
    <nav class="top-navbar">
      <div class="navbar-content">
        <!-- Left: Logo and Brand -->
        <div class="navbar-left">
          <div class="brand-logo">
            <img src="@/assets/LOGO WAY BG.png" alt="IntelliGrade" class="logo-img" />
            <span class="brand-name">IntelliGrade</span>
          </div>
        </div>
        <!-- Center: Empty space -->
        <div class="navbar-center"></div>
        <!-- Right: User info -->
        <div class="navbar-right">
          <div class="user-profile rounded-bg">
            <div class="user-avatar">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                <path d="M12,4A4,4 0 0,1 16,8A4,4 0 0,1 12,12A4,4 0 0,1 8,8A4,4 0 0,1 12,4M12,14C16.42,14 20,15.79 20,18V20H4V18C4,15.79 7.58,14 12,14Z"/>
              </svg>
            </div>
            <span class="user-name">Teacher</span>
          </div>
        </div>
      </div>
    </nav>

    <!-- Main Content -->
    <main class="main-content">
      <!-- Page Header -->
      <div class="page-header">
        <div class="header-content">
          <div class="header-left">
            <button @click="goBack" class="back-btn">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                <path d="M20,11V13H8L13.5,18.5L12.08,19.92L4.16,12L12.08,4.08L13.5,5.5L8,11H20Z" />
              </svg>
              Back to Section
            </button>
            <div class="header-icon">
              <svg width="28" height="28" viewBox="0 0 24 24" fill="currentColor">
                <path d="M14,2H6A2,2 0 0,0 4,4V20A2,2 0 0,0 6,22H18A2,2 0 0,0 20,20V8L14,2M18,20H6V4H13V9H18V20Z"/>
              </svg>
            </div>
            <div>
              <h1 class="header-title">Student Submissions</h1>
              <p class="header-subtitle">{{ subjectName }} - {{ sectionName }}</p>
            </div>
          </div>
        </div>
      </div>

        <!-- Content Wrapper -->
        <div class="content-wrapper">
          <!-- Loading State -->
          <div v-if="loading" class="loading-container">
            <div class="loading-spinner"></div>
            <p>Loading submissions...</p>
          </div>

          <!-- Error State -->
          <div v-else-if="error" class="error-container">
            <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <circle cx="12" cy="12" r="10"/>
              <line x1="12" y1="8" x2="12" y2="12"/>
              <line x1="12" y1="16" x2="12.01" y2="16"/>
            </svg>
            <p>{{ error }}</p>
            <button @click="fetchSubmissions" class="retry-button">Retry</button>
          </div>

          <!-- Main Content -->
          <div v-else class="submissions-container">
            <!-- Filters Section -->
            <div class="filters-section">
              <div class="search-filter-bar">
                <div class="search-input-container">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" class="search-icon">
                    <circle cx="11" cy="11" r="8" stroke="currentColor" stroke-width="2"/>
                    <path d="m21 21-4.35-4.35" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                  <input
                    v-model="searchQuery"
                    class="search-input"
                    type="text"
                    placeholder="Search by student name..."
                  />
                </div>
                <select v-model="filterType" class="grade-filter">
                  <option value="all">All Submissions</option>
                  <option value="quiz">Quizzes Only</option>
                  <option value="assignment">Assignments Only</option>
                </select>
                <select v-model="filterStatus" class="status-filter">
                  <option value="all">All Status</option>
                  <option value="submitted">Submitted</option>
                  <option value="graded">Graded</option>
                  <option value="pending">Pending Review</option>
                </select>
              </div>
            </div>

                  <!-- Statistics Cards -->
            <div class="stats-grid">
              <div class="stat-card">
                <div class="stat-icon quiz">
                  <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
                    <polyline points="14 2 14 8 20 8"/>
                    <line x1="9" y1="15" x2="15" y2="15"/>
                  </svg>
                </div>
                <div class="stat-info">
                  <h3>{{ stats.totalQuizSubmissions }}</h3>
                  <p>Quiz Submissions</p>
                </div>
              </div>

              <div class="stat-card">
                <div class="stat-icon assignment">
                  <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
                    <polyline points="14 2 14 8 20 8"/>
                  </svg>
                </div>
                <div class="stat-info">
                  <h3>{{ stats.totalAssignmentSubmissions }}</h3>
                  <p>Assignment Submissions</p>
                </div>
              </div>

              <div class="stat-card">
                <div class="stat-icon pending">
                  <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <circle cx="12" cy="12" r="10"/>
                    <polyline points="12 6 12 12 16 14"/>
                  </svg>
                </div>
                <div class="stat-info">
                  <h3>{{ stats.pendingReview }}</h3>
                  <p>Pending Review</p>
                </div>
              </div>

              <div class="stat-card">
                <div class="stat-icon graded">
                  <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <polyline points="20 6 9 17 4 12"/>
                  </svg>
                </div>
                <div class="stat-info">
                  <h3>{{ stats.graded }}</h3>
                  <p>Graded</p>
                </div>
              </div>
            </div>

            <!-- Submissions List -->
            <div class="submissions-list">
              <div v-if="filteredSubmissions.length === 0" class="empty-state">
                <svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
                  <polyline points="14 2 14 8 20 8"/>
                </svg>
                <h3>No Submissions Found</h3>
                <p>No student submissions match your current filters.</p>
              </div>

              <div v-else class="submissions-grid">
                <div 
                  v-for="submission in filteredSubmissions" 
                  :key="submission.id"
                  class="submission-card"
                  :class="submission.type"
                >
                  <!-- Student Info -->
                  <div class="submission-header">
                    <div class="student-info">
                      <div class="student-avatar">
                        {{ getInitials(submission.student_name) }}
                      </div>
                      <div>
                        <h3>{{ submission.student_name }}</h3>
                        <p class="student-id">{{ submission.student_number }}</p>
                      </div>
                    </div>
                    <span class="submission-type-badge" :class="submission.type">
                      {{ submission.type === 'quiz' ? 'Quiz' : 'Assignment' }}
                    </span>
                  </div>                  <!-- Submission Details -->
                  <div class="submission-body">
                    <h4 class="submission-title">{{ submission.title }}</h4>
                    
                    <div class="submission-meta">
                      <div class="meta-item">
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                          <circle cx="12" cy="12" r="10"/>
                          <polyline points="12 6 12 12 16 14"/>
                        </svg>
                        <span>{{ formatDate(submission.submitted_at) }}</span>
                      </div>

                      <div class="meta-item" v-if="submission.is_late">
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                          <circle cx="12" cy="12" r="10"/>
                          <line x1="12" y1="8" x2="12" y2="12"/>
                          <line x1="12" y1="16" x2="12.01" y2="16"/>
                        </svg>
                        <span class="late-indicator">Late Submission</span>
                      </div>
                    </div>

                    <!-- Score Display -->
                    <div class="score-section" v-if="submission.status === 'graded'">
                      <div class="score-display">
                        <span class="score">{{ submission.score }}</span>
                        <span class="max-score">/ {{ submission.max_score }}</span>
                      </div>
                      <div class="percentage" :class="getScoreClass(submission.percentage)">
                        {{ submission.percentage }}%
                      </div>
                    </div>

                    <div class="status-badge" v-else :class="submission.status">
                      {{ getStatusText(submission.status) }}
                    </div>
                  </div>                  <!-- Actions -->
                  <div class="submission-footer">
                    <button 
                      v-if="submission.type === 'quiz'"
                      @click="viewQuizDetails(submission)"
                      class="action-button view"
                    >
                      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/>
                        <circle cx="12" cy="12" r="3"/>
                      </svg>
                      View Details
                    </button>

                    <button 
                      v-if="submission.type === 'assignment'"
                      @click="viewAssignmentSubmission(submission)"
                      class="action-button view"
                    >
                      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/>
                        <circle cx="12" cy="12" r="3"/>
                      </svg>
                      View Submission
                    </button>

                    <button 
                      v-if="submission.type === 'assignment' && submission.status === 'submitted'"
                      @click="gradeAssignment(submission)"
                      class="action-button grade"
                    >
                      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"/>
                        <path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"/>
                      </svg>
                      Grade
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </main>
    </div>

    <!-- Grade Assignment Modal -->
    <div v-if="showGradeModal" class="modal-overlay" @click.self="closeGradeModal">
      <div class="modal-content grade-modal">
        <div class="modal-header">
          <h2>Grade Assignment</h2>
          <button @click="closeGradeModal" class="close-button">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <line x1="18" y1="6" x2="6" y2="18"/>
              <line x1="6" y1="6" x2="18" y2="18"/>
            </svg>
          </button>
        </div>

        <div class="modal-body">
          <div class="student-submission-info">
            <h3>{{ selectedSubmission?.student_name }}</h3>
            <p>{{ selectedSubmission?.title }}</p>
          </div>

          <div class="form-group">
            <label>Score (out of {{ selectedSubmission?.max_score }})</label>
            <input 
              type="number" 
              v-model.number="gradeForm.score" 
              :max="selectedSubmission?.max_score"
              min="0"
              class="form-input"
            />
          </div>

          <div class="form-group">
            <label>Feedback</label>
            <textarea 
              v-model="gradeForm.feedback" 
              rows="4"
              placeholder="Provide feedback to the student..."
              class="form-textarea"
            ></textarea>
          </div>
        </div>

        <div class="modal-footer">
          <button @click="closeGradeModal" class="button secondary">Cancel</button>
          <button @click="submitGrade" class="button primary" :disabled="submitting">
            {{ submitting ? 'Submitting...' : 'Submit Grade' }}
          </button>
        </div>
      </div>
    </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { supabase } from '../../supabase.js'; 

const route = useRoute();
const router = useRouter();

// State
const loading = ref(true);
const error = ref('');
const submissions = ref<any[]>([]);
const filterType = ref('all');
const filterStatus = ref('all');
const searchQuery = ref('');
const showGradeModal = ref(false);
const selectedSubmission = ref<any>(null);
const submitting = ref(false);

const gradeForm = ref({
  score: 0,
  feedback: ''
});

// Route params
const subjectId = route.params.subjectId as string;
const sectionId = route.params.sectionId as string;
const subjectName = route.query.subject as string;
const sectionName = route.query.section as string;

// Computed
const stats = computed(() => {
  const quizSubmissions = submissions.value.filter(s => s.type === 'quiz').length;
  const assignmentSubmissions = submissions.value.filter(s => s.type === 'assignment').length;
  const pending = submissions.value.filter(s => s.status === 'submitted').length;
  const graded = submissions.value.filter(s => s.status === 'graded').length;

  return {
    totalQuizSubmissions: quizSubmissions,
    totalAssignmentSubmissions: assignmentSubmissions,
    pendingReview: pending,
    graded: graded
  };
});

const filteredSubmissions = computed(() => {
  let filtered = submissions.value;

  // Filter by type
  if (filterType.value !== 'all') {
    filtered = filtered.filter(s => s.type === filterType.value);
  }

  // Filter by status
  if (filterStatus.value !== 'all') {
    filtered = filtered.filter(s => s.status === filterStatus.value);
  }

  // Search by student name
  if (searchQuery.value) {
    filtered = filtered.filter(s => 
      s.student_name.toLowerCase().includes(searchQuery.value.toLowerCase())
    );
  }

  return filtered;
});

// Methods
const fetchSubmissions = async () => {
  try {
    loading.value = true;
    error.value = '';

    // Fetch quiz submissions with proper join
    const { data: quizData, error: quizError } = await supabase
      .from('quiz_attempts')
      .select(`
        id,
        quiz_id,
        student_id,
        submitted_at,
        total_score,
        max_score,
        percentage,
        status
      `)
      .eq('status', 'submitted');

    if (quizError) throw quizError;

    // Get student details separately - FIXED: Use full_name and student_id instead of first_name, last_name, student_number
    const studentIds = [...new Set(quizData?.map(q => q.student_id) || [])];
    const { data: studentsData, error: studentsError } = await supabase
      .from('students')
      .select('id, full_name, student_id')
      .in('id', studentIds);

    if (studentsError) throw studentsError;

    // Get quiz details separately
    const quizIds = [...new Set(quizData?.map(q => q.quiz_id) || [])];
    const { data: quizzesData, error: quizzesError } = await supabase
      .from('quizzes')
      .select('id, title, section_id')
      .in('id', quizIds)
      .eq('section_id', sectionId);

    if (quizzesError) throw quizzesError;

    // Create lookup maps
    const studentsMap = new Map(studentsData?.map(s => [s.id, s]) || []);
    const quizzesMap = new Map(quizzesData?.map(q => [q.id, q]) || []);

    // Fetch assignment submissions with proper join
    const { data: assignmentData, error: assignmentError } = await supabase
      .from('assignment_submissions')
      .select(`
        id,
        assignment_id,
        student_id,
        submitted_at,
        score,
        status,
        is_late
      `)
      .in('status', ['submitted', 'graded']);

    if (assignmentError) throw assignmentError;

    // Get student details for assignments - FIXED: Use full_name and student_id
    const assignmentStudentIds = [...new Set(assignmentData?.map(a => a.student_id) || [])];
    const { data: assignmentStudentsData, error: assignmentStudentsError } = await supabase
      .from('students')
      .select('id, full_name, student_id')
      .in('id', assignmentStudentIds);

    if (assignmentStudentsError) throw assignmentStudentsError;

    // Get assignment details
    const assignmentIds = [...new Set(assignmentData?.map(a => a.assignment_id) || [])];
    const { data: assignmentsData, error: assignmentsError } = await supabase
      .from('assignments')
      .select('id, title, total_points, section_id')
      .in('id', assignmentIds)
      .eq('section_id', sectionId);

    if (assignmentsError) throw assignmentsError;

    // Create lookup maps for assignments
    const assignmentStudentsMap = new Map(assignmentStudentsData?.map(s => [s.id, s]) || []);
    const assignmentsMap = new Map(assignmentsData?.map(a => [a.id, a]) || []);

    // Format quiz submissions - FIXED: Use full_name and student_id
    const formattedQuizzes = (quizData || [])
      .filter(quiz => quizzesMap.has(quiz.quiz_id))
      .map((quiz: any) => {
        const student = studentsMap.get(quiz.student_id);
        const quizInfo = quizzesMap.get(quiz.quiz_id);
        
        return {
          id: quiz.id,
          type: 'quiz',
          student_id: quiz.student_id,
          student_name: student?.full_name || 'Unknown Student',
          student_number: student?.student_id || 'N/A',
          title: quizInfo?.title || 'Unknown Quiz',
          submitted_at: quiz.submitted_at,
          score: quiz.total_score,
          max_score: quiz.max_score,
          percentage: quiz.percentage,
          status: quiz.status,
          is_late: false
        };
      });

    // Format assignment submissions - FIXED: Use full_name and student_id
    const formattedAssignments = (assignmentData || [])
      .filter(assignment => assignmentsMap.has(assignment.assignment_id))
      .map((assignment: any) => {
        const student = assignmentStudentsMap.get(assignment.student_id);
        const assignmentInfo = assignmentsMap.get(assignment.assignment_id);
        
        return {
          id: assignment.id,
          type: 'assignment',
          student_id: assignment.student_id,
          student_name: student?.full_name || 'Unknown Student',
          student_number: student?.student_id || 'N/A',
          title: assignmentInfo?.title || 'Unknown Assignment',
          submitted_at: assignment.submitted_at,
          score: assignment.score || 0,
          max_score: assignmentInfo?.total_points || 100,
          percentage: assignment.score && assignmentInfo?.total_points 
            ? ((assignment.score / assignmentInfo.total_points) * 100).toFixed(2) 
            : 0,
          status: assignment.status,
          is_late: assignment.is_late
        };
      });

    // Combine and sort by submission date
    submissions.value = [...formattedQuizzes, ...formattedAssignments]
      .sort((a, b) => new Date(b.submitted_at).getTime() - new Date(a.submitted_at).getTime());

  } catch (err: any) {
    console.error('Error fetching submissions:', err);
    error.value = err.message || 'Failed to load submissions';
  } finally {
    loading.value = false;
  }
};

const formatDate = (dateString: string) => {
  const date = new Date(dateString);
  return date.toLocaleDateString('en-US', {
    month: 'short',
    day: 'numeric',
    year: 'numeric',
    hour: '2-digit',
    minute: '2-digit'
  });
};

const getInitials = (name: string) => {
  return name
    .split(' ')
    .map(n => n[0])
    .join('')
    .toUpperCase();
};

const getStatusText = (status: string) => {
  const statusMap: Record<string, string> = {
    submitted: 'Pending Review',
    graded: 'Graded',
    in_progress: 'In Progress'
  };
  return statusMap[status] || status;
};

const getScoreClass = (percentage: number) => {
  if (percentage >= 90) return 'excellent';
  if (percentage >= 80) return 'good';
  if (percentage >= 70) return 'fair';
  return 'poor';
};

const viewQuizDetails = (submission: any) => {
  router.push({
    name: 'QuizResults',
    params: {
      quizId: submission.id
    }
  });
};

const viewAssignmentSubmission = (submission: any) => {
  router.push({
    name: 'AssignmentSubmissionDetail',
    params: {
      submissionId: submission.id
    }
  });
};

const gradeAssignment = (submission: any) => {
  selectedSubmission.value = submission;
  gradeForm.value.score = 0;
  gradeForm.value.feedback = '';
  showGradeModal.value = true;
};

const closeGradeModal = () => {
  showGradeModal.value = false;
  selectedSubmission.value = null;
};

const submitGrade = async () => {
  try {
    submitting.value = true;

    const { error: updateError } = await supabase
      .from('assignment_submissions')
      .update({
        score: gradeForm.value.score,
        feedback: gradeForm.value.feedback,
        status: 'graded',
        graded_at: new Date().toISOString()
      })
      .eq('id', selectedSubmission.value.id);

    if (updateError) throw updateError;

    // Update local data
    const index = submissions.value.findIndex(s => s.id === selectedSubmission.value.id);
    if (index !== -1) {
      submissions.value[index].score = gradeForm.value.score;
      submissions.value[index].status = 'graded';
      submissions.value[index].percentage = ((gradeForm.value.score / selectedSubmission.value.max_score) * 100).toFixed(2);
    }

    closeGradeModal();
    alert('Grade submitted successfully!');

  } catch (err: any) {
    console.error('Error submitting grade:', err);
    alert('Failed to submit grade: ' + err.message);
  } finally {
    submitting.value = false;
  }
};

const goBack = () => {
  router.back();
};

// Lifecycle
onMounted(() => {
  fetchSubmissions();
});
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

/* ===============================================
   MODERN UI SYSTEM - CONSISTENT WITH MYSUBJECTS
   =============================================== */

/* Reset and Base */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.student-submissions {
  min-height: 100vh;
  width: 100vw;
  background: #f8fafc;
  font-family: 'Inter', sans-serif;
  overflow-x: hidden;
}

.dark .student-submissions {
  background: #0f172a;
}

/* Top Navigation Bar */
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

/* Rounded semi-transparent backgrounds */
.rounded-bg {
  background: rgba(255,255,255,0.13);
  border-radius: 16px;
  transition: background 0.2s;
}

.rounded-bg:hover {
  background: rgba(255,255,255,0.22);
}

/* Main Content */
.main-content {
  margin-top: 64px;
  padding: 1.5rem;
  width: 100%;
  min-height: calc(100vh - 64px);
  position: relative;
  overflow-y: auto;
  overflow-x: hidden;
  scroll-behavior: smooth;
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
  background: #1e293b;
  border-color: #334155;
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

.back-btn {
  background: #f3f4f6;
  border: none;
  padding: 0.75rem 1rem;
  border-radius: 8px;
  color: #374151;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s ease;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.back-btn:hover {
  background: #e5e7eb;
}

.dark .back-btn {
  background: #334155;
  color: #e2e8f0;
}

.dark .back-btn:hover {
  background: #475569;
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
  color: #f1f5f9;
}

.header-subtitle {
  font-size: 0.95rem;
  color: #64748b;
}

.dark .header-subtitle {
  color: #94a3b8;
}

.loading-container,
.error-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 4rem 2rem;
  color: #6b7280;
}

.loading-spinner {
  width: 48px;
  height: 48px;
  border: 4px solid #e5e7eb;
  border-top-color: #3D8D7A;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

.error-container svg {
  color: #ef4444;
  margin-bottom: 1rem;
}

.retry-button {
  margin-top: 1rem;
  padding: 0.5rem 1.5rem;
  background: #3D8D7A;
  color: white;
  border: none;
  border-radius: 0.375rem;
  cursor: pointer;
  transition: all 0.2s ease;
}

.retry-button:hover {
  background: #2d6a5a;
}

.submissions-container {
  max-width: 1400px;
  margin: 0 auto;
  padding: 2rem;
}

.filters-section {
  background: white;
  padding: 1.5rem;
  border-radius: 0.75rem;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
  margin-bottom: 2rem;
}

.filter-group {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.filter-group label {
  font-size: 0.875rem;
  font-weight: 500;
  color: #374151;
}

.filter-select,
.search-input {
  padding: 0.625rem;
  border: 1px solid #d1d5db;
  border-radius: 0.375rem;
  font-size: 0.875rem;
  transition: border-color 0.2s;
}

.filter-select:focus,
.search-input:focus {
  outline: none;
  border-color: #3b82f6;
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
}

.content-wrapper {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
}

.submissions-container {
  max-width: 1400px;
  margin: 0 auto;
  padding: 0;
}

.filters-section {
  background: white;
  padding: 1.5rem;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
  margin-bottom: 2rem;
  border: 1px solid #e2e8f0;
}

.dark .filters-section {
  background: #1e293b;
  border-color: #334155;
}

.search-filter-bar {
  display: flex;
  gap: 1rem;
  align-items: center;
}

.search-input-container {
  position: relative;
  flex: 1;
}

.search-icon {
  position: absolute;
  left: 1rem;
  top: 50%;
  transform: translateY(-50%);
  color: #6b7280;
}

.search-input {
  width: 100%;
  padding: 0.75rem 1rem 0.75rem 3rem;
  border: 1px solid #e5e7eb;
  border-radius: 12px;
  font-size: 1rem;
  background: white;
  transition: all 0.2s ease;
}
.search-input:focus {
  outline: none;
  border-color: #3D8D7A;
  box-shadow: 0 0 0 3px rgba(61, 141, 122, 0.1);
}
.dark .search-input {
  background: #1e293b;
  border-color: #334155;
  color: #e2e8f0;
}

.grade-filter, .status-filter {
  padding: 0.75rem 1rem;
  border: 1px solid #e5e7eb;
  border-radius: 12px;
  background: white;
  min-width: 150px;
}
.dark .grade-filter, .dark .status-filter {
  background: #1e293b;
  border-color: #334155;
  color: #e2e8f0;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
  margin-bottom: 2rem;
}

.stat-card {
  background: white;
  padding: 1.5rem;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
  display: flex;
  align-items: center;
  gap: 1rem;
  border: 1px solid #e2e8f0;
}

.dark .stat-card {
  background: #1e293b;
  border-color: #334155;
}

.stat-icon {
  width: 48px;
  height: 48px;
  border-radius: 0.75rem;
  display: flex;
  align-items: center;
  justify-content: center;
}

.stat-icon.quiz {
  background: linear-gradient(135deg, #dbeafe, #bfdbfe);
  color: #3b82f6;
}

.stat-icon.assignment {
  background: linear-gradient(135deg, #fef3c7, #fde68a);
  color: #f59e0b;
}

.stat-icon.pending {
  background: linear-gradient(135deg, #fce7f3, #fbcfe8);
  color: #ec4899;
}

.stat-icon.graded {
  background: linear-gradient(135deg, #d1fae5, #a7f3d0);
  color: #10b981;
}

.stat-info h3 {
  font-size: 1.875rem;
  font-weight: 700;
  color: #111827;
  margin: 0;
}

.dark .stat-info h3 {
  color: #f1f5f9;
}

.stat-info p {
  color: #6b7280;
  font-size: 0.875rem;
  margin: 0;
}

.dark .stat-info p {
  color: #94a3b8;
}

.submissions-list {
  background: white;
  padding: 1.5rem;
  border-radius: 0.75rem;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.empty-state {
  text-align: center;
  padding: 4rem 2rem;
  color: #6b7280;
}

.empty-state svg {
  color: #d1d5db;
  margin-bottom: 1rem;
}

.empty-state h3 {
  font-size: 1.25rem;
  font-weight: 600;
  color: #374151;
  margin: 0.5rem 0;
}

.submissions-grid {
  display: grid;
  gap: 1.5rem;
}

.submission-card {
  border: 1px solid #e5e7eb;
  border-radius: 16px;
  padding: 1.5rem;
  transition: all 0.2s;
  background: white;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
}

.submission-card:hover {
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
  transform: translateY(-2px);
  border-color: #3D8D7A;
}

.dark .submission-card {
  background: #1e293b;
  border-color: #334155;
}

.dark .submission-card:hover {
  border-color: #3D8D7A;
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3);
}

.submission-card.quiz {
  border-left: 4px solid #3b82f6;
}

.submission-card.assignment {
  border-left: 4px solid #f59e0b;
}

.submission-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
  padding-bottom: 1rem;
  border-bottom: 1px solid #e5e7eb;
}

.student-info {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.student-avatar {
  width: 48px;
  height: 48px;
  border-radius: 50%;
  background: linear-gradient(135deg, #3D8D7A 0%, #2d6a5a 100%);
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 600;
  font-size: 1rem;
}

.student-info h3 {
  font-size: 1rem;
  font-weight: 600;
  color: #111827;
  margin: 0;
}

.dark .student-info h3 {
  color: #f1f5f9;
}

.student-id {
  font-size: 0.875rem;
  color: #6b7280;
  margin: 0.25rem 0 0 0;
}

.dark .student-id {
  color: #94a3b8;
}

.submission-type-badge {
  padding: 0.375rem 0.75rem;
  border-radius: 9999px;
  font-size: 0.75rem;
  font-weight: 500;
}

.submission-type-badge.quiz {
  background: #dbeafe;
  color: #1e40af;
}

.submission-type-badge.assignment {
  background: #fef3c7;
  color: #92400e;
}

.submission-body {
  margin-bottom: 1rem;
}

.submission-title {
  font-size: 1.125rem;
  font-weight: 600;
  color: #111827;
  margin: 0 0 1rem 0;
}

.submission-meta {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
  margin-bottom: 1rem;
}

.meta-item {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.875rem;
  color: #6b7280;
}

.late-indicator {
  color: #dc2626;
  font-weight: 500;
}

.score-section {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1rem;
  background: #f9fafb;
  border-radius: 0.5rem;
}

.score-display {
  font-size: 1.5rem;
  font-weight: 700;
  color: #111827;
}

.max-score {
  color: #6b7280;
  font-size: 1.25rem;
}

.percentage {
  padding: 0.5rem 1rem;
  border-radius: 9999px;
  font-weight: 600;
  font-size: 0.875rem;
}

.percentage.excellent {
  background: #d1fae5;
  color: #065f46;
}

.percentage.good {
  background: #dbeafe;
  color: #1e40af;
}

.percentage.fair {
  background: #fef3c7;
  color: #92400e;
}

.percentage.poor {
  background: #fee2e2;
  color: #991b1b;
}

.status-badge {
  display: inline-block;
  padding: 0.5rem 1rem;
  border-radius: 9999px;
  font-size: 0.875rem;
  font-weight: 500;
}

.status-badge.submitted {
  background: #fef3c7;
  color: #92400e;
}

.status-badge.graded {
  background: #d1fae5;
  color: #065f46;
}

.submission-footer {
  display: flex;
  gap: 0.75rem;
  padding-top: 1rem;
  border-top: 1px solid #e5e7eb;
}

.action-button {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  padding: 0.625rem 1rem;
  border: none;
  border-radius: 0.375rem;
  font-size: 0.875rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s;
}

.action-button.view {
  background: #eff6ff;
  color: #1e40af;
}

.action-button.view:hover {
  background: #dbeafe;
}

.action-button.grade {
  background: #3D8D7A;
  color: white;
}

.action-button.grade:hover {
  background: #2d6a5a;
}

/* Modal Styles */
.modal-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 50;
  padding: 1rem;
}

.modal-content {
  background: white;
  border-radius: 0.75rem;
  max-width: 600px;
  width: 100%;
  max-height: 90vh;
  overflow-y: auto;
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.5rem;
  border-bottom: 1px solid #e5e7eb;
}

.modal-header h2 {
  font-size: 1.5rem;
  font-weight: 700;
  color: #111827;
  margin: 0;
}

.close-button {
  background: none;
  border: none;
  cursor: pointer;
  color: #6b7280;
  padding: 0.5rem;
  border-radius: 0.375rem;
  transition: all 0.2s;
}

.close-button:hover {
  background: #f3f4f6;
  color: #374151;
}

.modal-body {
  padding: 1.5rem;
}

.student-submission-info {
  margin-bottom: 1.5rem;
  padding: 1rem;
  background: #f9fafb;
  border-radius: 0.5rem;
}

.student-submission-info h3 {
  font-size: 1.125rem;
  font-weight: 600;
  color: #111827;
  margin: 0 0 0.25rem 0;
}

.student-submission-info p {
  color: #6b7280;
  margin: 0;
}

.form-group {
  margin-bottom: 1.5rem;
}

.form-group label {
  display: block;
  font-size: 0.875rem;
  font-weight: 500;
  color: #374151;
  margin-bottom: 0.5rem;
}

.form-input,
.form-textarea {
  width: 100%;
  padding: 0.625rem;
  border: 1px solid #d1d5db;
  border-radius: 0.375rem;
  font-size: 0.875rem;
  transition: border-color 0.2s;
}

.form-input:focus,
.form-textarea:focus {
  outline: none;
  border-color: #3D8D7A;
  box-shadow: 0 0 0 3px rgba(61, 141, 122, 0.1);
}

.modal-footer {
  display: flex;
  justify-content: flex-end;
  gap: 0.75rem;
  padding: 1.5rem;
  border-top: 1px solid #e5e7eb;
}

.button {
  padding: 0.625rem 1.5rem;
  border: none;
  border-radius: 0.375rem;
  font-size: 0.875rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s;
}

.button.secondary {
  background: #f3f4f6;
  color: #374151;
}

.button.secondary:hover {
  background: #e5e7eb;
}

.button.primary {
  background: #3D8D7A;
  color: white;
}

.button.primary:hover {
  background: #2d6a5a;
}

.button.primary:disabled {
  background: #9ca3af;
  cursor: not-allowed;
}

/* Responsive Design */
@media (max-width: 768px) {
  .page-header {
    padding: 1rem;
  }

  .submissions-container {
    padding: 1rem;
  }

  .filters-section {
    grid-template-columns: 1fr;
  }

  .stats-grid {
    grid-template-columns: 1fr;
  }

  .submission-footer {
    flex-direction: column;
  }

  .action-button {
    width: 100%;
  }
  
  .search-filter-bar {
    flex-direction: column;
    align-items: stretch;
  }
  
  .header-content {
    flex-direction: column;
    align-items: flex-start;
  }
  
  .header-left {
    width: 100%;
  }
  
  .main-content {
    padding: 1rem;
  }
}
</style>