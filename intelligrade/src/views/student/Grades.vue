<template>
  <div class="grades-page">
    <!-- Header Section -->
    <div class="section-header-card">
      <div class="section-header-content">
        <div class="section-header-left">
          <div class="section-header-icon">
            <svg width="36" height="36" viewBox="0 0 24 24" fill="currentColor">
              <path d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
            </svg>
          </div>
          
          <div class="header-text">
            <h1 class="section-header-title">{{ subject.name }} - Grades</h1>
            <p class="section-header-subtitle">{{ section.name }}</p>
            <p class="section-header-description">{{ studentInfo.full_name }} • Grade {{ studentInfo.grade_level }}</p>
          </div>
        </div>
        
        <div class="header-actions">
          <button @click="goBack" class="back-btn">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M20,11V13H8L13.5,18.5L12.08,19.92L4.16,12L12.08,4.08L13.5,5.5L8,11H20Z" />
            </svg>
            Back to Subjects
          </button>
        </div>
      </div>
    </div>

    <!-- Loading State -->
    <div v-if="loading" class="loading-container">
      <div class="spinner-large"></div>
      <p>Loading grades...</p>
    </div>

    <!-- Grades Overview -->
    <div v-else class="main-content">
      <!-- Stats Overview -->
      <div class="stats-grid">
          <div class="stat-card">
            <div class="stat-value">{{ averageGrade }}%</div>
            <div class="stat-label">Average Score</div>
          </div>
          <div class="stat-card">
            <div class="stat-value">{{ completedQuizzes }}</div>
            <div class="stat-label">Completed Quizzes</div>
          </div>
          <div class="stat-card">
            <div class="stat-value">{{ highestGrade }}%</div>
            <div class="stat-label">Highest Score</div>
          </div>
          <div class="stat-card">
            <div class="stat-value">{{ lowestGrade }}%</div>
            <div class="stat-label">Lowest Score</div>
          </div>
      </div>

      <!-- Grades List -->
      <div class="grades-section">
        <!-- Recent Quizzes -->
        <div v-if="recentQuizzes.length > 0" class="quiz-category">
          <div class="category-header">
            <h2 class="category-title">
              <span class="category-icon">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
                </svg>
              </span>
              Recent Submissions
            </h2>
            <span class="category-count">{{ recentQuizzes.length }}</span>
          </div>
          <div class="grades-list">
            <div v-for="quiz in recentQuizzes" :key="quiz.id" class="grade-card recent-grade">
              <div class="grade-header">
                <div class="quiz-info">
                  <h3 class="quiz-title">{{ quiz.title }}</h3>
                  <div class="quiz-code">
                    <span class="code-label">Code:</span>
                    <span class="code-value">{{ quiz.quiz_code }}</span>
                  </div>
                </div>
                <div class="grade-status" :class="getStatusClass(quiz.status)">
                  {{ getStatusText(quiz.status) }}
                </div>
              </div>

              <div class="grade-content">
                <div class="grade-info">
                  <div v-if="quiz.best_percentage !== null" class="score-display">
                    <div class="score-circle" :class="getScoreClass(quiz.best_percentage)">
                      <span class="score-value">{{ quiz.best_percentage }}%</span>
                    </div>
                    <div class="score-details">
                      <div class="score-fraction">{{ calculateScore(quiz.best_percentage, quiz.number_of_questions) }} / {{ quiz.number_of_questions }}</div>
                      <div class="score-label">Questions Correct</div>
                    </div>
                  </div>
                  <div v-else class="score-pending">
                    <div class="pending-icon">
                      <svg width="32" height="32" viewBox="0 0 24 24" fill="currentColor">
                        <path d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
                      </svg>
                    </div>
                    <div class="pending-text">Grade Pending</div>
                  </div>
                </div>

                <div class="submission-info">
                  <div class="info-item">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                      <path d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
                    </svg>
                    <span>Submitted: {{ formatPHTime(quiz.latest_attempt_date) }}</span>
                  </div>
                  <div class="info-item">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                      <path d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"/>
                    </svg>
                    <span>{{ quiz.total_attempts }} attempt(s)</span>
                  </div>
                  <div v-if="quiz.time_taken_minutes" class="info-item">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                      <path d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
                    </svg>
                    <span>{{ quiz.time_taken_minutes }} minutes</span>
                  </div>
                </div>
              </div>

              <div class="grade-actions">
                <button v-if="quiz.status === 'completed' || quiz.status === 'submitted'" @click="viewQuizPreview(quiz)" class="btn btn-view pending">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
                  </svg>
                  View Submitted Quiz
                </button>
                <button v-else-if="quiz.status === 'graded' || quiz.status === 'reviewed'" @click="viewQuizPreview(quiz)" class="btn btn-view graded">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
                  </svg>
                  View Answers & Results
                </button>
              </div>
            </div>
          </div>
        </div>

        <!-- All Grades History -->
        <div v-if="allGrades.length > 0" class="quiz-category">
          <div class="category-header">
            <h2 class="category-title">
              <span class="category-icon">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/>
                </svg>
              </span>
              Grade History
            </h2>
            <span class="category-count">{{ allGrades.length }}</span>
          </div>
          <div class="grades-table-container">
            <table class="grades-table">
              <thead>
                <tr>
                  <th>Quiz</th>
                  <th class="center-header">Score</th>
                  <th class="center-header">Status</th>
                  <th>Submitted</th>
                  <th class="center-header">Attempts</th>
                  <th class="center-header">Action</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="quiz in allGrades" :key="quiz.id" class="grade-row">
                  <td class="quiz-cell">
                    <div class="quiz-name">{{ quiz.title }}</div>
                    <div class="quiz-code-small">{{ quiz.quiz_code }}</div>
                  </td>
                  <td class="score-cell">
                    <div v-if="quiz.best_percentage !== null" class="score-badge" :class="getScoreClass(quiz.best_percentage)">
                      {{ quiz.best_percentage }}%
                    </div>
                    <div v-else class="score-pending-small">Pending</div>
                  </td>
                  <td class="status-cell">
                    <div class="status-badge" :class="getStatusClass(quiz.status)">
                      {{ getStatusText(quiz.status) }}
                    </div>
                  </td>
                  <td class="date-cell">
                    <div v-if="quiz.latest_attempt_date" class="date-text">
                      {{ formatShortDate(quiz.latest_attempt_date) }}
                    </div>
                    <div v-else class="date-text">-</div>
                  </td>
                  <td class="attempts-cell">
                    {{ quiz.total_attempts }}
                  </td>
                  <td class="actions-cell">
                    <button v-if="quiz.status === 'completed' || quiz.status === 'submitted'" @click="viewQuizPreview(quiz)" class="btn-table pending" title="View Submitted Quiz">
                      <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                        <path d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
                      </svg>
                      <span class="btn-text">View Submitted</span>
                    </button>
                    <button v-else-if="quiz.status === 'graded' || quiz.status === 'reviewed'" @click="viewQuizPreview(quiz)" class="btn-table graded" title="View Answers & Results">
                      <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                        <path d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
                      </svg>
                      <span class="btn-text">View Results</span>
                    </button>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

        <!-- Empty State -->
        <div v-if="allGrades.length === 0" class="empty-state">
          <div class="empty-icon">
            <svg width="48" height="48" viewBox="0 0 24 24" fill="currentColor">
              <path d="M9 17H7v-2a3 3 0 013-3h4a3 3 0 013 3v2h-2v-2a1 1 0 00-1-1h-4a1 1 0 00-1 1v2zM6 3h12a3 3 0 013 3v12a3 3 0 01-3 3H6a3 3 0 01-3-3V6a3 3 0 013-3zm0 2a1 1 0 00-1 1v12a1 1 0 001 1h12a1 1 0 001-1V6a1 1 0 00-1-1H6z"/>
            </svg>
          </div>
          <h3>No Grades Yet</h3>
          <p>You haven't submitted any quizzes for this subject yet.</p>
          <button @click="goToQuizzes" class="btn btn-primary">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M12 6v6m0 0v6m0-6h6m-6 0H6"/>
            </svg>
            Take a Quiz
          </button>
        </div>
      </div>
    </div>

    <!-- Quiz Preview Modal -->
    <div v-if="showPreviewModal" class="modal-overlay" @click.self="showPreviewModal = false">
      <div class="preview-modal">
        <div class="modal-header">
          <h3>{{ selectedQuiz?.title }} - {{ modalTitle }}</h3>
          <button @click="showPreviewModal = false" class="modal-close">×</button>
        </div>
        <div class="modal-body">
          <div v-if="loadingPreview" class="loading-answers">
            <div class="spinner"></div>
            <p>Loading quiz preview...</p>
          </div>
          <div v-else class="preview-content">
            <!-- Score Summary -->
            <div class="preview-summary">
              <div class="summary-item">
                <span class="summary-label">Your Score:</span>
                <span class="summary-value" :class="getScoreClass(selectedQuiz.best_percentage)">
                  {{ selectedQuiz.best_percentage !== null ? `${selectedQuiz.best_percentage}% (${calculateScore(selectedQuiz.best_percentage, selectedQuiz.number_of_questions)}/${selectedQuiz.number_of_questions})` : 'Pending' }}
                </span>
              </div>
              <div class="summary-item">
                <span class="summary-label">Status:</span>
                <span class="summary-value">{{ getStatusText(selectedQuiz.status) }}</span>
              </div>
              <div v-if="selectedQuiz.latest_attempt_date" class="summary-item">
                <span class="summary-label">Submitted:</span>
                <span class="summary-value">{{ formatPHTime(selectedQuiz.latest_attempt_date) }}</span>
              </div>
              <div v-if="selectedAttempt?.teacher_feedback" class="summary-item full-width">
                <span class="summary-label">Overall Teacher Feedback:</span>
                <div class="teacher-feedback-box">{{ selectedAttempt.teacher_feedback }}</div>
              </div>
            </div>

            <!-- Questions and Answers -->
            <div v-for="answer in previewAnswers" :key="answer.question_id" class="answer-item">
              <div class="answer-header">
                <div class="question-number">Q{{ answer.question_number }}</div>
                <div v-if="isGraded" class="answer-result" :class="answer.is_correct ? 'correct' : 'incorrect'">
                  {{ answer.is_correct ? '✓ Correct' : '✗ Incorrect' }}
                </div>
              </div>
              <div class="question-text">{{ answer.question_text }}</div>
              
              <!-- Student's Answer -->
              <div class="student-answer">
                <div class="answer-label">Your Answer:</div>
                <div class="answer-content" :class="isGraded ? (answer.is_correct ? 'correct-answer' : 'wrong-answer') : 'submitted-answer'">
                  {{ getStudentAnswerText(answer) }}
                </div>
              </div>

              <!-- Correct Answer (if graded and wrong) -->
              <div v-if="isGraded && !answer.is_correct" class="correct-answer-section">
                <div class="answer-label">Correct Answer:</div>
                <div class="answer-content correct-answer">
                  {{ getCorrectAnswerText(answer) }}
                </div>
              </div>

              <!-- Teacher Comment (if any) -->
              <div v-if="answer.teacher_comment && answer.teacher_comment.trim() !== ''" class="teacher-comment">
                <div class="comment-label">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" style="display: inline-block; margin-right: 0.25rem;">
                    <path d="M8 10h8M8 14h8M6 4h12a2 2 0 012 2v12a2 2 0 01-2 2H6a2 2 0 01-2-2V6a2 2 0 012-2z"/>
                  </svg>
                  Teacher Comment:
                </div>
                <div class="comment-text">{{ answer.teacher_comment }}</div>
              </div>
            </div>

            <!-- No answers message -->
            <div v-if="previewAnswers.length === 0" class="no-answers">
              <p>No answers found for this quiz attempt.</p>
            </div>
          </div>
        </div>
        <div class="modal-actions">
          <button @click="showPreviewModal = false" class="btn btn-secondary">Close</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, computed, onMounted, onUnmounted } from 'vue';
import { useRouter, useRoute } from 'vue-router';
import { supabase } from '@/supabase.js';

export default {
  name: 'StudentGrades',
  setup() {
    const router = useRouter();
    const route = useRoute();

    const loading = ref(true);
    const studentInfo = ref({ full_name: 'Loading...', grade_level: '', student_id: null });
    const subject = ref({ id: '', name: 'Subject' });
    const section = ref({ id: '', name: '' });
    const grades = ref([]);
    const showPreviewModal = ref(false);
    const selectedQuiz = ref(null);
    const selectedAttempt = ref(null);
    const previewAnswers = ref([]);
    const loadingPreview = ref(false);

    let gradesSubscription = null;

    // Computed
    const recentQuizzes = computed(() => {
      return grades.value
        .filter(g => g.latest_attempt_date)
        .sort((a, b) => new Date(b.latest_attempt_date) - new Date(a.latest_attempt_date))
        .slice(0, 5);
    });

    const allGrades = computed(() => {
      return [...grades.value]
        .sort((a, b) => new Date(b.latest_attempt_date || 0) - new Date(a.latest_attempt_date || 0));
    });

    const completedQuizzes = computed(() => {
      return grades.value.filter(g => g.status === 'completed' || g.status === 'graded').length;
    });

    const averageGrade = computed(() => {
      const completed = grades.value.filter(g => g.best_percentage !== null);
      if (completed.length === 0) return 0;
      const sum = completed.reduce((acc, g) => acc + g.best_percentage, 0);
      return Math.round(sum / completed.length);
    });

    const highestGrade = computed(() => {
      const scores = grades.value.filter(g => g.best_percentage !== null).map(g => g.best_percentage);
      return scores.length > 0 ? Math.max(...scores) : 0;
    });

    const lowestGrade = computed(() => {
      const scores = grades.value.filter(g => g.best_percentage !== null).map(g => g.best_percentage);
      return scores.length > 0 ? Math.min(...scores) : 0;
    });

    const isGraded = computed(() => {
      return selectedQuiz.value && (selectedQuiz.value.status === 'graded' || selectedQuiz.value.status === 'reviewed');
    });

    const modalTitle = computed(() => {
      if (!selectedQuiz.value) return '';
      return isGraded.value ? 'Answers & Results' : 'Submitted Quiz';
    });

    // Utility Functions
    const formatPHTime = (utcDateString) => {
      if (!utcDateString) return 'Not available';
      const date = new Date(utcDateString);
      const options = {
        year: 'numeric',
        month: 'short',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit',
        timeZone: 'Asia/Manila'
      };
      return date.toLocaleString('en-PH', options) + ' PHT';
    };

    const formatShortDate = (utcDateString) => {
      if (!utcDateString) return '-';
      const date = new Date(utcDateString);
      const options = { month: 'short', day: 'numeric', year: 'numeric', timeZone: 'Asia/Manila' };
      return date.toLocaleString('en-PH', options);
    };

    // Helper function to check if answer is correct
    const checkIfAnswerIsCorrect = (answer, studentAnswer, correctAnswerData) => {
      // If points_earned equals points_possible, it's correct
      if (studentAnswer.points_earned >= studentAnswer.points_possible) {
        return true;
      }

      // If points_earned is 0, it's incorrect
      if (studentAnswer.points_earned === 0) {
        return false;
      }

      // Double-check with actual answer comparison
      if (answer.question_type === 'multiple_choice') {
        // For multiple choice, check if selected option is correct
        const selectedOption = answer.options.find(opt => opt.id === studentAnswer.selected_option_id);
        return selectedOption ? selectedOption.is_correct === true : false;
      } else if (answer.question_type === 'true_false' || answer.question_type === 'fill_blank') {
        // For true/false and fill-in-blank, compare with correct answer
        if (!correctAnswerData) return false;
        
        const studentAns = (studentAnswer.answer_text || '').trim();
        const correctAns = correctAnswerData.correct_answer.trim();
        
        if (correctAnswerData.case_sensitive) {
          return studentAns === correctAns;
        } else {
          return studentAns.toLowerCase() === correctAns.toLowerCase();
        }
      }

      // Fallback to is_correct from database
      return studentAnswer.is_correct === true;
    };

    // Load Functions
    const loadStudentInfo = async () => {
      try {
        const { data: { session } } = await supabase.auth.getSession();
        if (!session?.user) {
          router.push('/login');
          return false;
        }

        const { data: profile, error: profileError } = await supabase
          .from('profiles')
          .select('id, role')
          .eq('auth_user_id', session.user.id)
          .single();

        if (profileError) {
          console.error('Profile error:', profileError);
          alert('Failed to load profile');
          return false;
        }

        if (!profile || profile.role !== 'student') {
          alert('Student profile not found');
          return false;
        }

        const { data: student, error: studentError } = await supabase
          .from('students')
          .select('*')
          .eq('profile_id', profile.id)
          .single();

        if (studentError) {
          console.error('Student error:', studentError);
          alert('Student information not found');
          return false;
        }

        if (!student) {
          alert('Student information not found');
          return false;
        }

        studentInfo.value = {
          full_name: student.full_name,
          grade_level: student.grade_level,
          student_id: student.id
        };

        console.log('Loaded student info:', studentInfo.value);
        return true;
      } catch (error) {
        console.error('Error loading student info:', error);
        return false;
      }
    };

    const loadRouteParams = () => {
      const subjectId = route.params.subjectId;
      const sectionId = route.params.sectionId;
      const subjectName = route.query.subjectName || 'Subject';
      const sectionName = route.query.sectionName || '';

      if (!subjectId || !sectionId) {
        console.error('Missing required route parameters');
        return false;
      }

      subject.value = { id: subjectId, name: subjectName };
      section.value = { id: sectionId, name: sectionName };
      
      console.log('Route params loaded:', { subject: subject.value, section: section.value });
      return true;
    };

    const loadGrades = async () => {
      try {
        if (!studentInfo.value.student_id) {
          console.error('No student ID available');
          return;
        }

        if (!section.value.id) {
          console.error('No section ID available');
          return;
        }

        console.log('Loading grades for student:', studentInfo.value.student_id, 'section:', section.value.id);

        // First, get all quizzes for this section
        const { data: sectionQuizzes, error: quizzesError } = await supabase
          .from('quizzes')
          .select('id, title, quiz_code, description, number_of_questions, attempts_allowed, section_id')
          .eq('section_id', section.value.id)
          .eq('status', 'published');

        if (quizzesError) {
          console.error('Error loading quizzes:', quizzesError);
          throw quizzesError;
        }

        console.log('Found quizzes for section:', sectionQuizzes?.length || 0);

        if (!sectionQuizzes || sectionQuizzes.length === 0) {
          grades.value = [];
          console.log('No quizzes found for this section');
          return;
        }

        const quizIds = sectionQuizzes.map(q => q.id);

        // Get ALL attempts for this student for quizzes in this section
        const { data: attempts, error: attemptsError } = await supabase
          .from('quiz_attempts')
          .select('*')
          .eq('student_id', studentInfo.value.student_id)
          .in('quiz_id', quizIds)
          .in('status', ['submitted', 'graded', 'reviewed'])
          .order('submitted_at', { ascending: false });

        if (attemptsError) {
          console.error('Error loading attempts:', attemptsError);
          throw attemptsError;
        }

        console.log('Found attempts:', attempts?.length || 0);

        if (!attempts || attempts.length === 0) {
          grades.value = [];
          console.log('No submitted attempts found');
          return;
        }

        // Build a map of quizzes for quick lookup
        const quizMap = {};
        sectionQuizzes.forEach(quiz => {
          quizMap[quiz.id] = {
            quiz: quiz,
            attempts: []
          };
        });

        // Group attempts by quiz
        attempts.forEach(attempt => {
          if (quizMap[attempt.quiz_id]) {
            quizMap[attempt.quiz_id].attempts.push(attempt);
          }
        });

        // Process each quiz that has attempts
        const processedGrades = [];
        
        Object.values(quizMap).forEach(quizData => {
          if (quizData.attempts.length === 0) return;

          const { quiz, attempts: quizAttempts } = quizData;

          // Find best percentage (handling null values)
          let bestAttempt = quizAttempts[0];
          quizAttempts.forEach(attempt => {
            if (attempt.percentage !== null && attempt.percentage !== undefined) {
              if (bestAttempt.percentage === null || bestAttempt.percentage === undefined) {
                bestAttempt = attempt;
              } else if (attempt.percentage > bestAttempt.percentage) {
                bestAttempt = attempt;
              }
            }
          });

          // Find latest attempt (already sorted by submitted_at descending)
          const latestAttempt = quizAttempts[0];

          // Determine status
          let resultStatus = 'completed';
          if (latestAttempt.status === 'graded' || latestAttempt.status === 'reviewed') {
            resultStatus = 'graded';
          } else if (latestAttempt.status === 'submitted') {
            resultStatus = 'submitted';
          }

          processedGrades.push({
            id: quiz.id,
            title: quiz.title,
            quiz_code: quiz.quiz_code,
            description: quiz.description,
            number_of_questions: quiz.number_of_questions || 1,
            attempts_allowed: quiz.attempts_allowed || 999,
            best_percentage: bestAttempt.percentage !== null ? bestAttempt.percentage : null,
            total_attempts: quizAttempts.length,
            latest_attempt_date: latestAttempt.submitted_at,
            status: resultStatus,
            time_taken_minutes: latestAttempt.time_taken_minutes,
            visible_to_student: true
          });
        });

        grades.value = processedGrades;
        console.log('Processed grades:', grades.value.length, grades.value);

      } catch (error) {
        console.error('Error loading grades:', error);
        alert('Failed to load grades. Please try refreshing the page.');
      }
    };

    const setupRealtimeSubscription = () => {
      if (!studentInfo.value.student_id) return;

      console.log('Setting up realtime subscription for student:', studentInfo.value.student_id);

      gradesSubscription = supabase
        .channel(`student-${studentInfo.value.student_id}-grades`)
        .on('postgres_changes', {
          event: '*',
          schema: 'public',
          table: 'quiz_attempts',
          filter: `student_id=eq.${studentInfo.value.student_id}`
        }, async (payload) => {
          console.log('Quiz attempt changed:', payload);
          await loadGrades();
        })
        .subscribe((status) => {
          console.log('Subscription status:', status);
        });
    };

    // Status & Score Functions
    const getStatusClass = (status) => {
      const classes = {
        'not_taken': 'status-not-taken',
        'in_progress': 'status-in-progress',
        'completed': 'status-completed',
        'submitted': 'status-completed',
        'pending_review': 'status-pending',
        'graded': 'status-graded',
        'reviewed': 'status-graded'
      };
      return classes[status] || 'status-unknown';
    };

    const getStatusText = (status) => {
      const texts = {
        'not_taken': 'Not Taken',
        'in_progress': 'In Progress',
        'completed': 'Submitted',
        'submitted': 'Submitted',
        'pending_review': 'Under Review',
        'graded': 'Graded',
        'reviewed': 'Graded'
      };
      return texts[status] || 'Unknown';
    };

    const getScoreClass = (percentage) => {
      if (percentage >= 90) return 'score-excellent';
      if (percentage >= 80) return 'score-good';
      if (percentage >= 70) return 'score-average';
      if (percentage >= 60) return 'score-below-average';
      return 'score-poor';
    };

    const calculateScore = (percentage, totalQuestions) => {
      return Math.round((percentage / 100) * totalQuestions);
    };

    // Quiz Preview
    const viewQuizPreview = async (quiz) => {
      selectedQuiz.value = quiz;
      selectedAttempt.value = null;
      showPreviewModal.value = true;
      loadingPreview.value = true;

      try {
        // Get latest graded/submitted attempt with ALL fields including teacher feedback
        const { data: attempts, error: attemptsError } = await supabase
          .from('quiz_attempts')
          .select('*')
          .eq('quiz_id', quiz.id)
          .eq('student_id', studentInfo.value.student_id)
          .in('status', ['submitted', 'graded', 'reviewed'])
          .order('attempt_number', { ascending: false })
          .limit(1);

        if (attemptsError) throw attemptsError;

        if (!attempts || attempts.length === 0) {
          throw new Error('No quiz attempt found');
        }

        const attempt = attempts[0];
        selectedAttempt.value = attempt;
        const attemptId = attempt.id;
        
        console.log('Loading preview for attempt:', attemptId);
        console.log('Attempt data (including teacher_feedback):', attempt);
        console.log('Teacher feedback:', attempt.teacher_feedback);

        // Get student answers with ALL fields including teacher comments
        const { data: answers, error: answersError } = await supabase
          .from('student_answers')
          .select('*')
          .eq('attempt_id', attemptId)
          .order('id');

        if (answersError) throw answersError;
        
        console.log('Loaded student answers:', answers);

        if (!answers || answers.length === 0) {
          previewAnswers.value = [];
          loadingPreview.value = false;
          return;
        }

        const questionIds = answers.map(a => a.question_id);

        // Get questions
        const { data: questions, error: questionsError } = await supabase
          .from('quiz_questions')
          .select('id, question_number, question_type, question_text')
          .in('id', questionIds);

        if (questionsError) throw questionsError;

        // Get options for multiple choice questions
        const { data: options, error: optionsError } = await supabase
          .from('question_options')
          .select('id, question_id, option_number, option_text, is_correct')
          .in('question_id', questionIds);

        if (optionsError) throw optionsError;

        // Get correct answers for true/false and fill-in-blank questions
        const { data: correctAnswers, error: correctAnswersError } = await supabase
          .from('question_answers')
          .select('question_id, correct_answer, case_sensitive')
          .in('question_id', questionIds);

        if (correctAnswersError) throw correctAnswersError;

        // Build maps
        const questionsMap = {};
        (questions || []).forEach(q => {
          questionsMap[q.id] = q;
        });

        const optionsMap = {};
        (options || []).forEach(opt => {
          if (!optionsMap[opt.question_id]) {
            optionsMap[opt.question_id] = [];
          }
          optionsMap[opt.question_id].push(opt);
        });

        const correctAnswersMap = {};
        (correctAnswers || []).forEach(ca => {
          correctAnswersMap[ca.question_id] = ca;
        });

        // Build preview with recalculated is_correct values
        previewAnswers.value = answers.map(answer => {
          const question = questionsMap[answer.question_id] || {};
          const questionOptions = optionsMap[answer.question_id] || [];
          const correctAnswerData = correctAnswersMap[answer.question_id];

          // Recalculate is_correct based on points or actual answer
          const isCorrect = checkIfAnswerIsCorrect(
            { question_type: question.question_type, options: questionOptions },
            answer,
            correctAnswerData
          );

          // Log for debugging
          console.log(`Question ${question.question_number}:`, {
            question_type: question.question_type,
            points_earned: answer.points_earned,
            points_possible: answer.points_possible,
            is_correct_from_db: answer.is_correct,
            is_correct_calculated: isCorrect,
            teacher_comment: answer.teacher_comment
          });

          return {
            question_id: answer.question_id,
            question_number: question.question_number || 0,
            question_type: question.question_type || 'multiple_choice',
            question_text: question.question_text || 'Question',
            is_correct: isCorrect,
            selected_option_id: answer.selected_option_id,
            answer_text: answer.answer_text,
            teacher_comment: answer.teacher_comment || '',
            points_earned: answer.points_earned || 0,
            points_possible: answer.points_possible || 1,
            options: questionOptions,
            correct_answer_data: correctAnswerData
          };
        }).sort((a, b) => a.question_number - b.question_number);

        console.log('Preview answers loaded:', previewAnswers.value.length);
        console.log('Answers with teacher comments:', previewAnswers.value.filter(a => a.teacher_comment && a.teacher_comment.trim() !== '').length);
        console.log('Correct answers:', previewAnswers.value.filter(a => a.is_correct).length);
        console.log('Incorrect answers:', previewAnswers.value.filter(a => !a.is_correct).length);

      } catch (error) {
        console.error('Error loading quiz preview:', error);
        alert('Failed to load quiz preview');
        previewAnswers.value = [];
      } finally {
        loadingPreview.value = false;
      }
    };

    const getStudentAnswerText = (answer) => {
      if (answer.selected_option_id && answer.options.length > 0) {
        const option = answer.options.find(opt => opt.id === answer.selected_option_id);
        if (option) {
          return `${String.fromCharCode(65 + option.option_number - 1)}. ${option.option_text}`;
        }
        return 'Unknown option';
      }
      return answer.answer_text || 'No answer provided';
    };

    const getCorrectAnswerText = (answer) => {
      if (answer.question_type === 'multiple_choice' && answer.options.length > 0) {
        const correctOption = answer.options.find(opt => opt.is_correct);
        if (correctOption) {
          return `${String.fromCharCode(65 + correctOption.option_number - 1)}. ${correctOption.option_text}`;
        }
        return 'Unknown';
      }
      
      // For true/false and fill-in-blank, get from correct_answer_data
      if (answer.correct_answer_data) {
        return answer.correct_answer_data.correct_answer;
      }
      
      return 'See correct answer above';
    };

    // Navigation
    const goBack = () => {
      router.push({ name: 'StudentSubjects' });
    };

    const goToQuizzes = () => {
      router.push({
        name: 'TakeQuiz',
        params: { 
          subjectId: subject.value.id, 
          sectionId: section.value.id 
        },
        query: {
          subjectName: subject.value.name,
          sectionName: section.value.name,
          gradeLevel: route.query.gradeLevel
        }
      });
    };

    // Lifecycle
    onMounted(async () => {
      console.log('StudentGrades component mounted');
      
      const studentLoaded = await loadStudentInfo();
      if (!studentLoaded) {
        console.error('Failed to load student info');
        router.push('/login');
        return;
      }

      const paramsLoaded = loadRouteParams();
      if (!paramsLoaded) {
        console.error('Failed to load route params');
        alert('Missing information');
        router.push('/student/subjects');
        return;
      }

      await loadGrades();
      setupRealtimeSubscription();
      loading.value = false;
    });

    onUnmounted(() => {
      if (gradesSubscription) {
        console.log('Removing subscription');
        supabase.removeChannel(gradesSubscription);
      }
    });

    return {
      loading, studentInfo, subject, section, grades, recentQuizzes, allGrades,
      completedQuizzes, averageGrade, highestGrade, lowestGrade, showPreviewModal,
      selectedQuiz, selectedAttempt, previewAnswers, loadingPreview, isGraded, modalTitle,
      formatPHTime, formatShortDate, getStatusClass, getStatusText, getScoreClass, 
      calculateScore, viewQuizPreview, getStudentAnswerText, getCorrectAnswerText,
      goBack, goToQuizzes
    };
  }
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.grades-page {
  min-height: 100vh;
  background: #FBFFE4;
  padding: 1.5rem;
  font-family: 'Inter', sans-serif;
  width: 100%;
  margin: 0;
}

.dark .grades-page {
  background: #181c20;
}

.main-content {
  width: 100%;
}

/* ============================================
   HEADER SECTION
   ============================================ */

.section-header-card {
  background: white;
  border-radius: 16px;
  border: 2px solid #A3D1C6;
  padding: 1.5rem;
  margin-bottom: 1.5rem;
  box-shadow: 0 2px 8px rgba(61, 141, 122, 0.08);
}

.dark .section-header-card {
  background: #23272b;
  border: 1px solid #3D8D7A;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.25);
}

.section-header-content {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.section-header-left {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.section-header-icon {
  width: 56px;
  height: 56px;
  background: #3D8D7A;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
}

.header-text {
  flex: 1;
}

.section-header-title {
  font-size: 1.5rem;
  font-weight: 700;
  color: #1f2937;
  margin-bottom: 0.25rem;
}

.dark .section-header-title {
  color: #A3D1C6;
}

.section-header-subtitle {
  font-size: 0.875rem;
  color: #6b7280;
}

.dark .section-header-subtitle {
  color: #A3D1C6;
}

.section-header-description {
  font-size: 0.813rem;
  color: #94a3b8;
}

.dark .section-header-description {
  color: #A3D1C6;
}

.header-actions {
  display: flex;
  justify-content: flex-end;
}

.back-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem 1.25rem;
  border-radius: 8px;
  font-weight: 500;
  font-size: 0.875rem;
  transition: all 0.2s;
  cursor: pointer;
  border: 2px solid #20c997;
  background: #20c997;
  color: #181c20;
  box-shadow: 0 2px 8px rgba(61, 141, 122, 0.10);
}

.back-btn:hover {
  background: #A3D1C6;
  color: #23272b;
  border-color: #20c997;
  box-shadow: 0 4px 16px rgba(61, 141, 122, 0.18);
}

.dark .back-btn {
  background: #20c997;
  color: #181c20;
  border-color: #A3D1C6;
}

.dark .back-btn:hover {
  background: #A3D1C6;
  color: #23272b;
  border-color: #20c997;
}

/* ============================================
   LOADING STATE
   ============================================ */

.loading-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 50vh;
  gap: 1rem;
}

.spinner-large {
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

/* ============================================
   STATS GRID
   ============================================ */

.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1.5rem;
  margin-bottom: 2rem;
}

.stat-card {
  background: white;
  border: 2px solid #3D8D7A;
  border-radius: 12px;
  padding: 1.5rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.5rem;
  box-shadow: 0 2px 8px rgba(61, 141, 122, 0.10);
}

.stat-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 16px rgba(61, 141, 122, 0.18);
}

.dark .stat-card {
  background: #23272b;
  border-color: #3D8D7A;
}

.stat-icon {
  font-size: 2.5rem;
}

.stat-value {
  font-size: 2rem;
  font-weight: 700;
  color: #3D8D7A;
  line-height: 1;
}

.dark .stat-value {
  color: #A3D1C6;
}

.stat-label {
  font-size: 0.875rem;
  font-weight: 500;
  color: #6b7280;
}

.dark .stat-label {
  color: #A3D1C6;
}

/* ============================================
   GRADES SECTION
   ============================================ */

.grades-section {
  width: 100%;
}

.quiz-category {
  margin-bottom: 2.5rem;
}

.category-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 1.5rem;
  flex-wrap: wrap;
  gap: 1rem;
}

.category-title {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  font-size: 1.5rem;
  font-weight: 700;
  color: #1f2937;
}

.dark .category-title {
  color: #A3D1C6;
}

.category-icon {
  font-size: 1.75rem;
}

.category-count {
  background: #3D8D7A;
  color: white;
  padding: 0.25rem 0.75rem;
  border-radius: 20px;
  font-size: 0.875rem;
  font-weight: 600;
}

/* ============================================
   GRADES LIST
   ============================================ */

.grades-list {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
  width: 100%;
}

.grade-card {
  background: white;
  border: 2px solid #3D8D7A;
  border-radius: 12px;
  padding: 1.5rem;
  transition: all 0.2s;
  box-shadow: 0 2px 8px rgba(61, 141, 122, 0.10);
}

.grade-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 16px rgba(61, 141, 122, 0.18);
}

.dark .grade-card {
  background: #23272b;
  border-color: #3D8D7A;
}

.grade-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 1rem;
  gap: 1rem;
  flex-wrap: wrap;
}

.quiz-info h3 {
  font-size: 1.25rem;
  font-weight: 600;
  color: #1f2937;
  margin-bottom: 0.5rem;
}

.dark .quiz-info h3 {
  color: #A3D1C6;
}

.quiz-code {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.875rem;
  flex-wrap: wrap;
}

.code-label {
  color: #6b7280;
  font-weight: 500;
}

.dark .code-label {
  color: #A3D1C6;
}

.code-value {
  background: #FBFFE4;
  color: #3D8D7A;
  padding: 0.25rem 0.5rem;
  border-radius: 4px;
  font-weight: 600;
  font-family: 'Courier New', monospace;
}

.dark .code-value {
  background: #181c20;
  color: #A3D1C6;
}

.grade-status {
  padding: 0.5rem 1rem;
  border-radius: 20px;
  font-size: 0.875rem;
  font-weight: 600;
  white-space: nowrap;
}

.status-completed {
  background: #B3D8A8;
  color: #1f2937;
}

.status-pending {
  background: #fbbf24;
  color: #1f2937;
}

.status-graded {
  background: #3D8D7A;
  color: white;
}

.status-not-taken {
  background: #e5e7eb;
  color: #6b7280;
}

.grade-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
  gap: 1.5rem;
  flex-wrap: wrap;
}

.grade-info {
  flex: 1;
  min-width: 150px;
}

.score-display {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.score-circle {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  border: 4px solid;
  flex-shrink: 0;
}

.score-excellent {
  background: rgba(34, 197, 94, 0.1);
  border-color: #22c55e;
  color: #16a34a;
}

.score-good {
  background: rgba(59, 130, 246, 0.1);
  border-color: #3b82f6;
  color: #2563eb;
}

.score-average {
  background: rgba(245, 158, 11, 0.1);
  border-color: #f59e0b;
  color: #d97706;
}

.score-below-average {
  background: rgba(249, 115, 22, 0.1);
  border-color: #f97316;
  color: #ea580c;
}

.score-poor {
  background: rgba(239, 68, 68, 0.1);
  border-color: #ef4444;
  color: #dc2626;
}

.score-value {
  font-size: 1.25rem;
}

.score-details {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}

.score-fraction {
  font-size: 1.125rem;
  font-weight: 600;
  color: #3D8D7A;
}

.dark .score-fraction {
  color: #A3D1C6;
}

.score-label {
  font-size: 0.875rem;
  color: #6b7280;
}

.dark .score-label {
  color: #A3D1C6;
}

.score-pending {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.5rem;
}

.pending-icon {
  font-size: 3rem;
}

.pending-text {
  font-size: 1rem;
  font-weight: 600;
  color: #6b7280;
}

.dark .pending-text {
  color: #A3D1C6;
}

.submission-info {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  flex: 1;
  min-width: 150px;
}

.info-item {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.875rem;
  color: #6b7280;
}

.dark .info-item {
  color: #A3D1C6;
}

.grade-actions {
  display: flex;
  gap: 0.75rem;
  justify-content: flex-end;
  flex-wrap: wrap;
  width: 100%;
}

.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  padding: 0.75rem 1.25rem;
  border-radius: 8px;
  font-weight: 600;
  font-size: 0.875rem;
  cursor: pointer;
  transition: all 0.2s;
  border: none;
  white-space: nowrap;
}

.btn-primary {
  background: #20c997;
  color: #181c20;
  border: 2px solid #20c997;
}

.btn-primary:hover:not(:disabled) {
  background: #A3D1C6;
  color: #23272b;
  border-color: #20c997;
}

.btn-secondary {
  background: transparent;
  color: #20c997;
  border: 2px solid #20c997;
}

.btn-secondary:hover {
  background: #e6fcf7;
  color: #20c997;
  border-color: #20c997;
}

.dark .btn-secondary:hover {
  background: #e6fcf7;
  color: #20c997;
  border-color: #20c997;
}

.btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

/* ============================================
   GRADES TABLE
   ============================================ */

.grades-table-container {
  background: white;
  border: 2px solid #3D8D7A;
  border-radius: 12px;
  overflow: auto;
  box-shadow: 0 2px 8px rgba(61, 141, 122, 0.10);
  width: 100%;
  -webkit-overflow-scrolling: touch;
}

.dark .grades-table-container {
  background: #23272b;
  border-color: #3D8D7A;
}

.grades-table {
  width: 100%;
  border-collapse: collapse;
  table-layout: auto;
}

.grades-table th {
  background: var(--bg-accent, #f9fafb);
  color: var(--text-accent, #3D8D7A);
  font-weight: 700;
  padding: 1rem;
  text-align: left;
  border-bottom: 2px solid var(--border-color, #e5e7eb);
  font-size: 0.875rem;
  vertical-align: middle;
}

.grades-table th.center-header {
  text-align: center;
}

.dark .grades-table th {
  background: rgba(61, 141, 122, 0.1);
  color: #A3D1C6;
  border-bottom-color: #3D8D7A;
}

.grades-table td {
  padding: 1rem;
  border-bottom: 1px solid var(--border-color, #e5e7eb);
  vertical-align: middle;
}

.dark .grades-table td {
  border-bottom-color: rgba(61, 141, 122, 0.2);
}

.grade-row:hover {
  background: rgba(61, 141, 122, 0.05);
}

.dark .grade-row:hover {
  background: rgba(61, 141, 122, 0.08);
}

.quiz-cell {
  font-weight: 500;
  color: #1f2937;
}

.dark .quiz-cell {
  color: #A3D1C6;
}

.quiz-name {
  font-weight: 600;
  margin-bottom: 0.25rem;
}

.quiz-code-small {
  font-size: 0.813rem;
  color: #6b7280;
}

.dark .quiz-code-small {
  color: #A3D1C6;
}

.score-cell {
  text-align: center;
  vertical-align: middle;
}

.score-badge {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  height: 36px;
  min-width: 80px;
  padding: 0 18px;
  border-radius: 18px;
  font-weight: 600;
  font-size: 1rem;
  line-height: 1.2;
  box-sizing: border-box;
}

.score-pending-small {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  height: 36px;
  min-width: 80px;
  padding: 0 18px;
  border-radius: 18px;
  background: #e5e7eb;
  color: #6b7280;
  font-weight: 600;
  font-size: 1rem;
  line-height: 1.2;
  box-sizing: border-box;
}

.status-cell {
  text-align: center;
  vertical-align: middle;
}

.status-badge {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  height: 36px;
  min-width: 80px;
  padding: 0 18px;
  border-radius: 18px;
  font-weight: 600;
  font-size: 1rem;
  line-height: 1.2;
  box-sizing: border-box;
}

.date-cell {
  text-align: center;
  color: #6b7280;
}

.dark .date-cell {
  color: #A3D1C6;
}

.date-text {
  font-size: 0.875rem;
}

.attempts-cell {
  text-align: center;
  font-weight: 600;
  color: #3D8D7A;
}

.dark .attempts-cell {
  color: #A3D1C6;
}

.actions-cell {
  text-align: center;
}

.table-actions {
  display: flex;
  justify-content: center;
  gap: 0.5rem;
}

.btn-icon {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 32px;
  height: 32px;
  border-radius: 6px;
  border: none;
  background: #f0f9f7;
  color: #3D8D7A;
  cursor: pointer;
  transition: all 0.2s;
}

.dark .btn-icon {
  background: rgba(61, 141, 122, 0.1);
  color: #A3D1C6;
}

.btn-icon:hover:not(:disabled) {
  background: #3D8D7A;
  color: white;
}

.dark .btn-icon:hover:not(:disabled) {
  background: #A3D1C6;
  color: #23272b;
}

.btn-icon:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

/* ============================================
   EMPTY STATE
   ============================================ */

.empty-state {
  text-align: center;
  padding: 4rem 2rem;
  background: white;
  border-radius: 12px;
  border: 2px dashed #A3D1C6;
}

.dark .empty-state {
  background: #23272b;
  border-color: #3D8D7A;
}

.empty-icon {
  font-size: 4rem;
  margin-bottom: 1rem;
  display: block;
  margin-left: auto;
  margin-right: auto;
}

.empty-state h3 {
  font-size: 1.5rem;
  font-weight: 600;
  color: #1f2937;
  margin-bottom: 0.5rem;
  text-align: center;
  margin-left: auto;
  margin-right: auto;
}

.dark .empty-state h3 {
  color: #A3D1C6;
}

.empty-state p {
  font-size: 1rem;
  color: #6b7280;
  margin-bottom: 2rem;
}

.dark .empty-state p {
  color: #A3D1C6;
}

/* ============================================
   PREVIEW MODAL
   ============================================ */

.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
  backdrop-filter: blur(4px);
  padding: 1rem;
}

.preview-modal {
  background: white;
  border-radius: 16px;
  max-width: 900px;
  width: 100%;
  max-height: 90vh;
  overflow: hidden;
  box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1);
  animation: modalSlideIn 0.3s ease-out;
  display: flex;
  flex-direction: column;
}

.dark .preview-modal {
  background: #23272b;
  border: 1px solid #3D8D7A;
  box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.3);
}

@keyframes modalSlideIn {
  from {
    opacity: 0;
    transform: translateY(-20px) scale(0.95);
  }
  to {
    opacity: 1;
    transform: translateY(0) scale(1);
  }
}

.modal-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1.5rem;
  border-bottom: 2px solid #3D8D7A;
  flex-wrap: wrap;
  gap: 1rem;
}

.modal-header h3 {
  font-size: 1.25rem;
  font-weight: 600;
  color: #1f2937;
}

.dark .modal-header h3 {
  color: #A3D1C6;
}

.modal-close {
  background: none;
  border: none;
  font-size: 1.5rem;
  color: #6b7280;
  cursor: pointer;
  width: 32px;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 4px;
  transition: all 0.2s;
  flex-shrink: 0;
}

.modal-close:hover {
  background: rgba(107, 114, 128, 0.1);
  color: #374151;
}

.dark .modal-close {
  color: #A3D1C6;
}

.dark .modal-close:hover {
  background: rgba(163, 209, 198, 0.1);
}

.modal-body {
  padding: 1.5rem;
  max-height: 60vh;
  overflow-y: auto;
  flex: 1;
}

.loading-answers {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
  padding: 2rem;
}

.spinner {
  width: 32px;
  height: 32px;
  border: 3px solid #e5e7eb;
  border-top-color: #3D8D7A;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

.preview-content {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.preview-summary {
  background: #f0f9f7;
  border: 2px solid #3D8D7A;
  border-radius: 12px;
  padding: 1rem;
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.dark .preview-summary {
  background: #181c20;
  border-color: #3D8D7A;
}

.summary-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 0.5rem;
}

.summary-label {
  font-weight: 600;
  color: #3D8D7A;
}

.dark .summary-label {
  color: #A3D1C6;
}

.summary-value {
  font-weight: 600;
  color: #1f2937;
}

.dark .summary-value {
  color: #A3D1C6;
}

.answer-item {
  background: #FBFFE4;
  border-radius: 12px;
  padding: 1.5rem;
  border: 1px solid #3D8D7A;
}

.dark .answer-item {
  background: #181c20;
  border-color: #3D8D7A;
}

.answer-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
  gap: 1rem;
  flex-wrap: wrap;
}

.question-number {
  background: #3D8D7A;
  color: white;
  padding: 0.5rem 1rem;
  border-radius: 20px;
  font-weight: 600;
  font-size: 0.875rem;
  white-space: nowrap;
}

.answer-result {
  padding: 0.5rem 1rem;
  border-radius: 20px;
  font-weight: 600;
  font-size: 0.875rem;
  white-space: nowrap;
}

.answer-result.correct {
  background: rgba(34, 197, 94, 0.1);
  color: #16a34a;
}

.answer-result.incorrect {
  background: rgba(239, 68, 68, 0.1);
  color: #dc2626;
}

.question-text {
  font-size: 1rem;
  font-weight: 500;
  color: #1f2937;
  margin-bottom: 1rem;
  line-height: 1.5;
}

.dark .question-text {
  color: #A3D1C6;
}

.student-answer,
.correct-answer-section,
.teacher-comment {
  margin-bottom: 1rem;
}

.answer-label,
.comment-label {
  font-size: 0.875rem;
  font-weight: 600;
  color: #6b7280;
  margin-bottom: 0.5rem;
}

.dark .answer-label,
.dark .comment-label {
  color: #A3D1C6;
}

.answer-content {
  padding: 0.75rem;
  border-radius: 8px;
  font-size: 0.875rem;
  line-height: 1.5;
}

.answer-content.correct-answer {
  background: rgba(34, 197, 94, 0.1);
  color: #16a34a;
  border: 1px solid #22c55e;
}

.answer-content.wrong-answer {
  background: rgba(239, 68, 68, 0.1);
  color: #dc2626;
  border: 1px solid #ef4444;
}

.correct-answer {
  background: rgba(34, 197, 94, 0.1);
  color: #16a34a;
  border: 1px solid #22c55e;
}

.comment-text {
  background: #f9fafb;
  padding: 0.75rem;
  border-radius: 8px;
  font-size: 0.875rem;
  color: #1f2937;
  border: 1px solid #e5e7eb;
  line-height: 1.5;
}

.dark .comment-text {
  background: #23272b;
  color: #A3D1C6;
  border-color: #3D8D7A;
}

.modal-actions {
  display: flex;
  gap: 0.75rem;
  padding: 1.5rem;
  border-top: 2px solid #3D8D7A;
  justify-content: flex-end;
  flex-wrap: wrap;
}

/* ============================================
   RESPONSIVE DESIGN
   ============================================ */

@media (max-width: 480px) {
  .grades-page {
    padding: 0;
    min-height: calc(100vh - 150px);
    width: 100%;
    margin: 0;
  }

  

  .section-header-card {
    margin: 1rem;
    margin-bottom: 1.5rem;
    padding: 1rem;
    border-radius: 12px;
  }

  .section-header-content {
    flex-direction: column;
    gap: 1rem;
    align-items: flex-start;
  }

  .section-header-left {
    flex-direction: row;
    align-items: center;
    width: 100%;
    gap: 0.75rem;
  }

  .section-header-icon {
    width: 50px;
    height: 50px;
    border-radius: 12px;
  }

  .section-header-title {
    font-size: 1.25rem;
    margin-bottom: 0.25rem;
  }

  .section-header-subtitle,
  .section-header-description {
    font-size: 0.9rem;
  }

  .header-actions {
    width: 100%;
    justify-content: center;
    display: flex;
  }

  .back-btn {
    padding: 0.75rem 1rem;
    font-size: 0.9rem;
    border-radius: 10px;
  }

  .stats-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 1rem;
    margin: 0 1rem 1.5rem 1rem;
  }

  .stat-card {
    padding: 1rem;
    border-radius: 12px;
  }

  .stat-value {
    font-size: 1.5rem;
  }

  .stat-label {
    font-size: 0.8rem;
  }

  .grades-section {
    width: 100%;
    margin: 0 1rem;
    box-sizing: border-box;
    padding: 0;
    overflow-x: hidden;
  }

  .quiz-category {
    margin-bottom: 1.5rem;
  }

  .category-header {
    padding: 1rem 0 0.75rem 0;
    margin-bottom: 0.75rem;
  }

  .category-title {
    font-size: 1.1rem;
  }

  .category-count {
    font-size: 0.8rem;
    padding: 0.35rem 0.75rem;
  }

  .grades-list {
    gap: 1rem;
  }

  .grade-card {
    padding: 1rem;
    border-radius: 12px;
  }

  .grade-header {
    margin-bottom: 1rem;
  }

  .quiz-info h3 {
    font-size: 1rem;
    margin-bottom: 0.5rem;
  }

  .quiz-code {
    margin-bottom: 0.75rem;
  }

  .code-label {
    font-size: 0.75rem;
  }

  .code-value {
    font-size: 0.8rem;
    padding: 0.35rem 0.75rem;
  }

  .grade-status {
    padding: 0.4rem 0.8rem;
    font-size: 0.75rem;
    border-radius: 8px;
  }

  .grade-content {
    flex-direction: column;
    align-items: flex-start;
    gap: 1rem;
  }

  .grade-info {
    width: 100%;
  }

  .score-display {
    justify-content: center;
    margin-bottom: 1rem;
  }

  .score-circle {
    width: 80px;
    height: 80px;
  }

  .score-value {
    font-size: 1.5rem;
  }

  .score-details {
    text-align: center;
  }

  .score-fraction {
    font-size: 0.85rem;
  }

  .score-label {
    font-size: 0.75rem;
  }

  .submission-info {
    gap: 0.75rem;
    flex-direction: column;
  }

  .info-item {
    font-size: 0.8rem;
  }

  .grade-actions {
    justify-content: flex-start;
    width: 100%;
    gap: 0.75rem;
    flex-direction: column;
  }

  .btn {
    width: 100%;
    min-width: auto;
    padding: 0.875rem 1.25rem;
    font-size: 0.9rem;
    border-radius: 12px;
    min-height: 48px;
  }

  .grades-table-container {
    margin: 1rem;
    border-radius: 12px;
    overflow: hidden;
  }

  .grades-table {
    font-size: 0.813rem;
  }

  .grades-table th,
  .grades-table td {
    padding: 0.75rem 0.5rem;
  }

  .grades-table th {
    font-size: 0.75rem;
  }

  .quiz-name {
    font-size: 0.85rem;
  }

  .quiz-code-small {
    font-size: 0.7rem;
  }

  .score-badge {
    padding: 0.3rem 0.6rem;
    font-size: 0.7rem;
  }

  .status-badge {
    padding: 0.3rem 0.6rem;
    font-size: 0.7rem;
  }

  .date-text {
    font-size: 0.75rem;
  }

  .btn-icon {
    width: 36px;
    height: 36px;
    border-radius: 8px;
  }

  .empty-state {
    margin: 0 1rem 1.5rem 0;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: center;
    max-width: none;
    width: calc(100% - 2rem);
    box-sizing: border-box;
    padding: 1.5rem;
    border-radius: 16px;
    background: #fff;
    border: 2px solid #A3D1C6;
    box-shadow: 0 2px 8px rgba(61, 141, 122, 0.08);
  }

  .empty-icon {
    width: 80px;
    height: 80px;
  }

  .empty-state h3 {
    font-size: 1.1rem;
  }

  .empty-state p {
    font-size: 0.9rem;
  }

  .modal-overlay {
    padding: 1rem;
  }

  .preview-modal {
    max-height: 85vh;
    width: 100%;
    max-width: none;
    margin: 0;
    border-radius: 16px;
  }

  .modal-header {
    padding: 1rem;
    border-radius: 16px 16px 0 0;
  }

  .modal-header h3 {
    font-size: 1.125rem;
  }

  .modal-close {
    width: 40px;
    height: 40px;
    border-radius: 10px;
  }

  .modal-body {
    padding: 1rem;
    max-height: 60vh;
  }

  .preview-content {
    gap: 1rem;
  }

  .preview-summary {
    padding: 1rem;
    border-radius: 12px;
    gap: 1rem;
  }

  .summary-item {
    text-align: center;
  }

  .summary-value {
    font-size: 1.25rem;
  }

  .summary-label {
    font-size: 0.8rem;
  }

  .answers-section {
    gap: 1rem;
  }

  .answer-item {
    padding: 1rem;
    border-radius: 12px;
  }

  .question-header {
    margin-bottom: 0.75rem;
  }

  .question-number {
    font-size: 0.8rem;
    padding: 0.35rem 0.75rem;
  }

  .question-text {
    font-size: 0.9rem;
  }

  .answer-content {
    gap: 0.75rem;
  }

  .student-answer,
  .correct-answer {
    padding: 0.875rem;
    border-radius: 10px;
  }

  .answer-label {
    font-size: 0.75rem;
  }

  .answer-text {
    font-size: 0.85rem;
  }

  .answer-status {
    padding: 0.35rem 0.75rem;
    font-size: 0.75rem;
  }

  .modal-actions {
    padding: 1rem;
    flex-direction: column-reverse;
    gap: 0.75rem;
  }

  .modal-actions .btn {
    width: 100%;
  }
}

@media (min-width: 481px) and (max-width: 768px) {
  .grades-page {
    padding: 0;
    min-height: calc(100vh - 150px);
  }

  .section-header-card {
    margin: 1.5rem;
    margin-bottom: 2rem;
    padding: 1.25rem;
    border-radius: 14px;
  }

  .section-header-content {
    gap: 1.25rem;
  }

  .section-header-left {
    gap: 1rem;
  }

  .section-header-icon {
    width: 55px;
    height: 55px;
    border-radius: 14px;
  }

  .section-header-title {
    font-size: 1.375rem;
  }

  .stats-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 1.25rem;
    margin: 0 1.5rem 2rem 1.5rem;
  }

  .stat-card {
    padding: 1.25rem;
    border-radius: 14px;
  }

  .grades-section {
    margin: 0 1.5rem;
  }

  .grade-content {
    flex-direction: column;
    gap: 1.25rem;
  }

  .grade-card {
    padding: 1.25rem;
    border-radius: 14px;
  }

  .grade-actions {
    flex-direction: row;
    gap: 1rem;
  }

  .btn {
    flex: 1;
    min-width: 140px;
    padding: 0.875rem 1.25rem;
    border-radius: 12px;
  }

  .grades-table-container {
    margin: 1.5rem;
    border-radius: 14px;
  }

  .empty-state {
    margin: 1.5rem;
    padding: 2.5rem 1.5rem;
    border-radius: 16px;
  }

  .modal-overlay {
    padding: 1.5rem;
  }

  .preview-modal {
    max-width: 90vw;
    border-radius: 16px;
  }

  .modal-header,
  .modal-body,
  .modal-actions {
    padding: 1.25rem;
  }
}

@media (min-width: 769px) {
  .grades-page {
    padding: 2rem;
  }

  .stats-grid {
    grid-template-columns: repeat(4, 1fr);
  }

  .grades-list {
    gap: 2rem;
  }

  .grade-content {
    flex-direction: row;
  }

  .preview-modal {
    max-width: 900px;
  }
}

@media (min-width: 1200px) {
  .grades-page {
    padding: 2rem 3%;
  }

  .stats-grid {
    gap: 2rem;
  }

  .grades-list {
    gap: 2.5rem;
  }
}

@media (min-width: 1400px) {
  .section-header-title {
    font-size: 2rem;
  }

  .stats-grid {
    grid-template-columns: repeat(4, 1fr);
    gap: 2.5rem;
  }
}

/* ============================================
   NEW BUTTON STYLES FOR VIEW ACTIONS
   ============================================ */

/* View Button Styles - Card Actions */
.btn-view {
  width: 100%;
  justify-content: center;
}

.btn-view.pending {
  background: #fbbf24;
  color: #1f2937;
  border: 2px solid #fbbf24;
}

.btn-view.pending:hover {
  background: #f59e0b;
  border-color: #f59e0b;
  color: #1f2937;
}

.btn-view.graded {
  background: #3D8D7A;
  color: white;
  border: 2px solid #3D8D7A;
}

.btn-view.graded:hover {
  background: #2d6b5e;
  border-color: #2d6b5e;
  color: white;
}

.dark .btn-view.pending {
  background: #fbbf24;
  color: #1f2937;
  border-color: #fbbf24;
}

.dark .btn-view.pending:hover {
  background: #f59e0b;
  border-color: #f59e0b;
}

.dark .btn-view.graded {
  background: #3D8D7A;
  color: white;
  border-color: #3D8D7A;
}

.dark .btn-view.graded:hover {
  background: #A3D1C6;
  color: #23272b;
  border-color: #A3D1C6;
}

/* Table Button Styles */
.btn-table {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  padding: 0.5rem 1rem;
  border-radius: 6px;
  border: none;
  font-weight: 600;
  font-size: 0.813rem;
  cursor: pointer;
  transition: all 0.2s;
  white-space: nowrap;
}

.btn-table.pending {
  background: #fef3c7;
  color: #92400e;
  border: 1px solid #fbbf24;
}

.btn-table.pending:hover {
  background: #fbbf24;
  color: #1f2937;
}

.btn-table.graded {
  background: #d1fae5;
  color: #065f46;
  border: 1px solid #3D8D7A;
}

.btn-table.graded:hover {
  background: #3D8D7A;
  color: white;
}

.dark .btn-table.pending {
  background: rgba(251, 191, 36, 0.1);
  color: #fbbf24;
  border-color: #fbbf24;
}

.dark .btn-table.pending:hover {
  background: #fbbf24;
  color: #1f2937;
}

.dark .btn-table.graded {
  background: rgba(61, 141, 122, 0.1);
  color: #A3D1C6;
  border-color: #3D8D7A;
}

.dark .btn-table.graded:hover {
  background: #3D8D7A;
  color: white;
}

.btn-table svg {
  flex-shrink: 0;
}

/* Submitted Answer Style (for non-graded) */
.submitted-answer {
  background: #f3f4f6;
  color: #1f2937;
  border: 1px solid #d1d5db;
}

.dark .submitted-answer {
  background: #374151;
  color: #e5e7eb;
  border-color: #4b5563;
}

/* ============================================
   RESPONSIVE UPDATES FOR NEW BUTTONS
   ============================================ */

@media (max-width: 480px) {
  .btn-table {
    padding: 0.625rem 0.875rem;
    font-size: 0.75rem;
    width: 100%;
  }

  .btn-text {
    display: inline;
  }

  .actions-cell {
    min-width: 140px;
  }
}

@media (min-width: 481px) and (max-width: 768px) {
  .btn-table {
    padding: 0.5rem 1rem;
    font-size: 0.813rem;
  }
}

@media (max-width: 768px) {
  .btn-view {
    padding: 0.875rem 1.25rem;
    font-size: 0.9rem;
  }
}

/* Teacher Feedback Styles */
.summary-item.full-width {
  flex-direction: column;
  align-items: flex-start;
  gap: 0.5rem;
}

.teacher-feedback-box {
  width: 100%;
  background: #fff7ed;
  border: 2px solid #fb923c;
  border-radius: 8px;
  padding: 1rem;
  color: #1f2937;
  font-size: 0.875rem;
  line-height: 1.6;
  margin-top: 0.5rem;
}

.dark .teacher-feedback-box {
  background: rgba(251, 146, 60, 0.1);
  border-color: #fb923c;
  color: #A3D1C6;
}

.teacher-comment {
  background: #fef3c7;
  border: 2px solid #fbbf24;
  border-radius: 10px;
  padding: 1rem;
  margin-top: 1rem;
}

.dark .teacher-comment {
  background: rgba(251, 191, 36, 0.1);
  border-color: #fbbf24;
}

.comment-label {
  font-size: 0.875rem;
  font-weight: 700;
  color: #92400e;
  margin-bottom: 0.5rem;
  display: flex;
  align-items: center;
}

.dark .comment-label {
  color: #fbbf24;
}

.comment-text {
  background: white;
  padding: 0.875rem;
  border-radius: 8px;
  font-size: 0.875rem;
  color: #1f2937;
  border: 1px solid #fde68a;
  line-height: 1.6;
  white-space: pre-wrap;
  word-wrap: break-word;
}

.dark .comment-text {
  background: #23272b;
  color: #e5e7eb;
  border-color: rgba(251, 191, 36, 0.3);
}

/* No answers state */
.no-answers {
  text-align: center;
  padding: 3rem 1rem;
  color: #6b7280;
}

.dark .no-answers {
  color: #9ca3af;
}

.no-answers p {
  font-size: 1rem;
  font-style: italic;
}

/* Responsive adjustments for feedback */
@media (max-width: 480px) {
  .teacher-feedback-box {
    padding: 0.875rem;
    font-size: 0.813rem;
  }

  .teacher-comment {
    padding: 0.875rem;
    margin-top: 0.875rem;
  }

  .comment-label {
    font-size: 0.813rem;
  }

  .comment-text {
    padding: 0.75rem;
    font-size: 0.813rem;
  }
}

@media (min-width: 481px) and (max-width: 768px) {
  .teacher-feedback-box {
    padding: 0.95rem;
  }

  .teacher-comment {
    padding: 0.95rem;
  }
}
</style>
