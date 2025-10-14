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
            Back to Quizzes
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
          <div class="stat-icon">📊</div>
          <div class="stat-value">{{ averageGrade }}%</div>
          <div class="stat-label">Average Score</div>
        </div>
        <div class="stat-card">
          <div class="stat-icon">🎯</div>
          <div class="stat-value">{{ completedQuizzes }}</div>
          <div class="stat-label">Completed Quizzes</div>
        </div>
        <div class="stat-card">
          <div class="stat-icon">⭐</div>
          <div class="stat-value">{{ highestGrade }}%</div>
          <div class="stat-label">Highest Score</div>
        </div>
        <div class="stat-card">
          <div class="stat-icon">📈</div>
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
              <span class="category-icon">🕒</span>
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
                    <div class="pending-icon">⏳</div>
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
                <button v-if="quiz.status === 'completed' && quiz.visible_to_student" @click="viewAnswerHistory(quiz)" class="btn btn-secondary">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/>
                  </svg>
                  View Answers
                </button>
                <button @click="retakeQuiz(quiz)" :disabled="!canRetake(quiz)" class="btn btn-primary">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"/>
                  </svg>
                  {{ canRetake(quiz) ? 'Retake Quiz' : 'No Retakes' }}
                </button>
              </div>
            </div>
          </div>
        </div>

        <!-- All Grades History -->
        <div v-if="allGrades.length > 0" class="quiz-category">
          <div class="category-header">
            <h2 class="category-title">
              <span class="category-icon">📋</span>
              Grade History
            </h2>
            <span class="category-count">{{ allGrades.length }}</span>
          </div>
          <div class="grades-table-container">
            <table class="grades-table">
              <thead>
                <tr>
                  <th>Quiz</th>
                  <th>Score</th>
                  <th>Status</th>
                  <th>Submitted</th>
                  <th>Attempts</th>
                  <th>Actions</th>
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
                    <div class="table-actions">
                      <button v-if="quiz.status === 'completed' && quiz.visible_to_student" @click="viewAnswerHistory(quiz)" class="btn-icon" title="View Answers">
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                          <path d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/>
                        </svg>
                      </button>
                      <button @click="retakeQuiz(quiz)" :disabled="!canRetake(quiz)" class="btn-icon" title="Retake Quiz">
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                          <path d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"/>
                        </svg>
                      </button>
                    </div>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

        <!-- Empty State -->
        <div v-if="allGrades.length === 0" class="empty-state">
          <div class="empty-icon">📊</div>
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

    <!-- Answer History Modal -->
    <div v-if="showAnswerModal" class="modal-overlay" @click.self="showAnswerModal = false">
      <div class="answer-modal">
        <div class="modal-header">
          <h3>Answer History - {{ selectedQuiz?.title }}</h3>
          <button @click="showAnswerModal = false" class="modal-close">×</button>
        </div>
        <div class="modal-body">
          <div v-if="loadingAnswers" class="loading-answers">
            <div class="spinner"></div>
            <p>Loading answer history...</p>
          </div>
          <div v-else class="answers-content">
            <div v-for="(answer, index) in answerHistory" :key="answer.question_id" class="answer-item">
              <div class="answer-header">
                <div class="question-number">Q{{ answer.question_number }}</div>
                <div class="answer-result" :class="answer.is_correct ? 'correct' : 'incorrect'">
                  {{ answer.is_correct ? '✓ Correct' : '✗ Incorrect' }}
                </div>
              </div>
              <div class="question-text">{{ answer.question_text }}</div>
              
              <!-- Student's Answer -->
              <div class="student-answer">
                <div class="answer-label">Your Answer:</div>
                <div class="answer-content" :class="answer.is_correct ? 'correct-answer' : 'wrong-answer'">
                  {{ getStudentAnswerText(answer) }}
                </div>
              </div>

              <!-- Correct Answer (if wrong) -->
              <div v-if="!answer.is_correct" class="correct-answer">
                <div class="answer-label">Correct Answer:</div>
                <div class="answer-content correct-answer">
                  {{ getCorrectAnswerText(answer) }}
                </div>
              </div>

              <!-- Teacher Comment (if any) -->
              <div v-if="answer.teacher_comment" class="teacher-comment">
                <div class="comment-label">Teacher Comment:</div>
                <div class="comment-text">{{ answer.teacher_comment }}</div>
              </div>
            </div>
          </div>
        </div>
        <div class="modal-actions">
          <button @click="showAnswerModal = false" class="btn btn-secondary">Close</button>
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

    // State
    const loading = ref(true);
    const studentInfo = ref({
      full_name: 'Loading...',
      grade_level: '',
      student_id: null
    });

    const subject = ref({
      id: '',
      name: 'Subject'
    });

    const section = ref({
      id: '',
      name: ''
    });

    const grades = ref([]);
    const showAnswerModal = ref(false);
    const selectedQuiz = ref(null);
    const answerHistory = ref([]);
    const loadingAnswers = ref(false);

    // Real-time subscription
    let gradesSubscription = null;

    // Computed
    const recentQuizzes = computed(() => {
      return grades.value
        .filter(g => g.latest_attempt_date)
        .sort((a, b) => new Date(b.latest_attempt_date) - new Date(a.latest_attempt_date))
        .slice(0, 5);
    });

    const allGrades = computed(() => {
      return grades.value
        .sort((a, b) => new Date(b.latest_attempt_date || 0) - new Date(a.latest_attempt_date || 0));
    });

    const completedQuizzes = computed(() => {
      return grades.value.filter(g => g.status === 'completed' && g.best_percentage !== null).length;
    });

    const averageGrade = computed(() => {
      const completed = grades.value.filter(g => g.best_percentage !== null);
      if (completed.length === 0) return 0;
      const sum = completed.reduce((acc, g) => acc + g.best_percentage, 0);
      return Math.round(sum / completed.length);
    });

    const highestGrade = computed(() => {
      const scores = grades.value
        .filter(g => g.best_percentage !== null)
        .map(g => g.best_percentage);
      return scores.length > 0 ? Math.max(...scores) : 0;
    });

    const lowestGrade = computed(() => {
      const scores = grades.value
        .filter(g => g.best_percentage !== null)
        .map(g => g.best_percentage);
      return scores.length > 0 ? Math.min(...scores) : 0;
    });

    // Methods
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
      const options = {
        month: 'short',
        day: 'numeric',
        timeZone: 'Asia/Manila'
      };
      return date.toLocaleString('en-PH', options);
    };

    const loadStudentInfo = async () => {
      try {
        const { data: { session }, error: sessionError } = await supabase.auth.getSession();
        
        if (sessionError || !session?.user) {
          router.push('/login');
          return false;
        }

        const { data: profile, error: profileError } = await supabase
          .from('profiles')
          .select('id, role, full_name, email')
          .eq('auth_user_id', session.user.id)
          .single();

        if (profileError || !profile || profile.role !== 'student') {
          alert('Student profile not found');
          return false;
        }

        const { data: student, error: studentError } = await supabase
          .from('students')
          .select('*')
          .eq('profile_id', profile.id)
          .single();

        if (studentError || !student) {
          alert('Student information not found');
          return false;
        }

        studentInfo.value = {
          full_name: student.full_name,
          grade_level: student.grade_level,
          student_id: student.id
        };

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

      subject.value = {
        id: subjectId,
        name: subjectName
      };

      section.value = {
        id: sectionId,
        name: sectionName
      };

      return true;
    };

    const loadGrades = async () => {
      try {
        // Get all quizzes for this section first
        const { data: allQuizzes, error: quizzesError } = await supabase
          .from('quizzes')
          .select('id, title, quiz_code, description, number_of_questions, attempts_allowed, status')
          .eq('section_id', section.value.id)
          .eq('status', 'published');

        if (quizzesError) throw quizzesError;

        if (!allQuizzes || allQuizzes.length === 0) {
          grades.value = [];
          return;
        }

        const quizIds = allQuizzes.map(q => q.id);

        // Load quiz results for this student
        const { data: results, error: resultsError } = await supabase
          .from('quiz_results')
          .select(`
            quiz_id,
            best_score,
            best_percentage,
            total_attempts,
            latest_attempt_date,
            status,
            visible_to_student
          `)
          .eq('student_id', studentInfo.value.student_id)
          .in('quiz_id', quizIds);

        if (resultsError) throw resultsError;

        // Merge quiz data with results
        const resultsMap = {};
        (results || []).forEach(r => {
          resultsMap[r.quiz_id] = r;
        });

        // Transform data - include quizzes with or without results
        grades.value = allQuizzes.map(quiz => {
          const result = resultsMap[quiz.id] || {};
          return {
            id: quiz.id,
            title: quiz.title,
            quiz_code: quiz.quiz_code,
            description: quiz.description,
            number_of_questions: quiz.number_of_questions || 1,
            attempts_allowed: quiz.attempts_allowed || 999,
            best_score: result.best_score || null,
            best_percentage: result.best_percentage || null,
            total_attempts: result.total_attempts || 0,
            latest_attempt_date: result.latest_attempt_date || null,
            status: result.status || 'not_taken',
            visible_to_student: result.visible_to_student !== false,
            time_taken_minutes: null
          };
        });

      } catch (error) {
        console.error('Error loading grades:', error);
        alert('Failed to load grades. Please refresh the page.');
      }
    };

    const setupRealtimeSubscription = () => {
      if (!studentInfo.value.student_id) return;

      gradesSubscription = supabase
        .channel(`student-${studentInfo.value.student_id}-grades`)
        .on(
          'postgres_changes',
          {
            event: '*',
            schema: 'public',
            table: 'quiz_results',
            filter: `student_id=eq.${studentInfo.value.student_id}`
          },
          async () => {
            console.log('Grade updated (real-time)');
            await loadGrades();
          }
        )
        .subscribe();
    };

    const getStatusClass = (status) => {
      const classes = {
        'not_taken': 'status-not-taken',
        'in_progress': 'status-in-progress',
        'completed': 'status-completed',
        'pending_review': 'status-pending',
        'graded': 'status-graded'
      };
      return classes[status] || 'status-unknown';
    };

    const getStatusText = (status) => {
      const texts = {
        'not_taken': 'Not Taken',
        'in_progress': 'In Progress',
        'completed': 'Submitted',
        'pending_review': 'Under Review',
        'graded': 'Graded'
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

    const canRetake = (quiz) => {
      if (quiz.attempts_allowed === 999) return true;
      return quiz.total_attempts < quiz.attempts_allowed;
    };

    const retakeQuiz = (quiz) => {
      if (!canRetake(quiz)) {
        alert('You have used all available attempts for this quiz.');
        return;
      }

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

    const viewAnswerHistory = async (quiz) => {
      selectedQuiz.value = quiz;
      showAnswerModal.value = true;
      loadingAnswers.value = true;

      try {
        // Get student answers for this quiz
        const { data: answers, error } = await supabase
          .from('student_answers')
          .select(`
            id,
            question_id,
            selected_option_id,
            answer_text,
            is_correct,
            teacher_comment,
            quiz_questions (
              id,
              question_number,
              question_type,
              question_text,
              question_options (
                id,
                option_number,
                option_text,
                is_correct
              )
            )
          `)
          .eq('quiz_id', quiz.id)
          .eq('student_id', studentInfo.value.student_id)
          .order('quiz_questions(question_number)');

        if (error) throw error;

        answerHistory.value = (answers || []).map(answer => ({
          question_id: answer.question_id,
          question_number: answer.quiz_questions?.question_number || 0,
          question_type: answer.quiz_questions?.question_type || 'multiple_choice',
          question_text: answer.quiz_questions?.question_text || 'Question',
          is_correct: answer.is_correct,
          selected_option_id: answer.selected_option_id,
          answer_text: answer.answer_text,
          teacher_comment: answer.teacher_comment,
          options: answer.quiz_questions?.question_options || []
        }));

      } catch (error) {
        console.error('Error loading answer history:', error);
        alert('Failed to load answer history.');
      } finally {
        loadingAnswers.value = false;
      }
    };

    const getStudentAnswerText = (answer) => {
      if (answer.selected_option_id && answer.options.length > 0) {
        const option = answer.options.find(opt => opt.id === answer.selected_option_id);
        return option ? `${String.fromCharCode(65 + option.option_number - 1)}. ${option.option_text}` : 'Unknown option';
      }
      return answer.answer_text || 'No answer provided';
    };

    const getCorrectAnswerText = (answer) => {
      if (answer.question_type === 'multiple_choice' && answer.options.length > 0) {
        const correctOption = answer.options.find(opt => opt.is_correct);
        return correctOption ? `${String.fromCharCode(65 + correctOption.option_number - 1)}. ${correctOption.option_text}` : 'Unknown';
      }
      return 'See correct answer above';
    };

    const goBack = () => {
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
      console.log('Grades component mounted');

      const studentLoaded = await loadStudentInfo();
      if (!studentLoaded) {
        router.push('/login');
        return;
      }

      const paramsLoaded = loadRouteParams();
      if (!paramsLoaded) {
        alert('Missing subject or section information');
        router.push('/student/subjects');
        return;
      }

      await loadGrades();
      setupRealtimeSubscription();

      loading.value = false;
    });

    onUnmounted(() => {
      if (gradesSubscription) {
        supabase.removeChannel(gradesSubscription);
      }
    });

    return {
      loading,
      studentInfo,
      subject,
      section,
      grades,
      recentQuizzes,
      allGrades,
      completedQuizzes,
      averageGrade,
      highestGrade,
      lowestGrade,
      showAnswerModal,
      selectedQuiz,
      answerHistory,
      loadingAnswers,
      formatPHTime,
      formatShortDate,
      getStatusClass,
      getStatusText,
      getScoreClass,
      calculateScore,
      canRetake,
      retakeQuiz,
      viewAnswerHistory,
      getStudentAnswerText,
      getCorrectAnswerText,
      goBack,
      goToQuizzes
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
}

.dark .grades-page {
  background: #181c20;
}

/* Header */
.section-header-card {
  background: white;
  border-radius: 16px;
  padding: 1.5rem;
  margin-bottom: 1.5rem;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
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

/* Loading */
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

/* Stats Grid */
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

.dark .stat-card {
  background: #23272b;
  border-color: #3D8D7A;
}

.stat-icon {
  font-size: 2rem;
}

.stat-value {
  font-size: 2rem;
  font-weight: 700;
  color: #3D8D7A;
}

.dark .stat-value {
  color: #A3D1C6;
}

.stat-label {
  font-size: 0.875rem;
  color: #6b7280;
  font-weight: 500;
}

.dark .stat-label {
  color: #A3D1C6;
}

/* Quiz Categories */
.quiz-category {
  margin-bottom: 2.5rem;
}

.category-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 1.5rem;
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

/* Grades List */
.grades-list {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
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
  align-items: flex-end;
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
  color: #A3D1C6;
  border: 2px solid #20c997;
}

.btn-secondary:hover {
  background: #23272b;
  color: #20c997;
  border-color: #20c997;
}

.btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

/* Grades Table */
.grades-table-container {
  background: white;
  border-radius: 12px;
  border: 2px solid #3D8D7A;
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(61, 141, 122, 0.10);
}

.dark .grades-table-container {
  background: #23272b;
  border-color: #3D8D7A;
}

.grades-table {
  width: 100%;
  border-collapse: collapse;
}

.grades-table th {
  background: #FBFFE4;
  color: #3D8D7A;
  font-weight: 600;
  padding: 1rem;
  text-align: left;
  border-bottom: 2px solid #3D8D7A;
}

.dark .grades-table th {
  background: #181c20;
  color: #A3D1C6;
  border-bottom-color: #3D8D7A;
}

.grades-table td {
  padding: 1rem;
  border-bottom: 1px solid #e5e7eb;
}

.dark .grades-table td {
  border-bottom-color: #3D8D7A;
}

.grade-row:hover {
  background: #FBFFE4;
}

.dark .grade-row:hover {
  background: #181c20;
}

.quiz-cell .quiz-name {
  font-weight: 600;
  color: #1f2937;
}

.dark .quiz-cell .quiz-name {
  color: #A3D1C6;
}

.quiz-code-small {
  font-size: 0.75rem;
  color: #6b7280;
  font-family: 'Courier New', monospace;
}

.dark .quiz-code-small {
  color: #A3D1C6;
}

.score-badge {
  display: inline-block;
  padding: 0.25rem 0.75rem;
  border-radius: 20px;
  font-weight: 600;
  font-size: 0.875rem;
}

.score-pending-small {
  color: #6b7280;
  font-style: italic;
}

.dark .score-pending-small {
  color: #A3D1C6;
}

.status-badge {
  display: inline-block;
  padding: 0.25rem 0.75rem;
  border-radius: 20px;
  font-size: 0.75rem;
  font-weight: 600;
}

.date-text {
  font-size: 0.875rem;
  color: #6b7280;
}

.dark .date-text {
  color: #A3D1C6;
}

.table-actions {
  display: flex;
  gap: 0.5rem;
}

.btn-icon {
  width: 32px;
  height: 32px;
  border-radius: 6px;
  border: none;
  background: #FBFFE4;
  color: #3D8D7A;
  cursor: pointer;
  transition: all 0.2s;
  display: flex;
  align-items: center;
  justify-content: center;
}

.btn-icon:hover:not(:disabled) {
  background: #3D8D7A;
  color: white;
}

.btn-icon:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.dark .btn-icon {
  background: #181c20;
  color: #A3D1C6;
}

.dark .btn-icon:hover:not(:disabled) {
  background: #A3D1C6;
  color: #181c20;
}

/* Empty State */
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
}

.empty-state h3 {
  font-size: 1.5rem;
  font-weight: 600;
  color: #1f2937;
  margin-bottom: 0.5rem;
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

/* Answer Modal */
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
}

.answer-modal {
  background: white;
  border-radius: 16px;
  max-width: 800px;
  width: 90%;
  max-height: 90vh;
  overflow: hidden;
  box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1);
  animation: modalSlideIn 0.3s ease-out;
}

.dark .answer-modal {
  background: #23272b;
  border: 1px solid #3D8D7A;
  box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.3);
}

@keyframes modalSlideIn {
  from {
    opacity: 0;
    transform: translateY(-20px) scale(0.95);
  }
}

.modal-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1.5rem;
  border-bottom: 1px solid #e5e7eb;
}

.dark .modal-header {
  border-bottom-color: #3D8D7A;
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

.answers-content {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.answer-item {
  background: #FBFFE4;
  border-radius: 12px;
  padding: 1.5rem;
  border: 1px solid #A3D1C6;
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
}

.question-number {
  background: #3D8D7A;
  color: white;
  padding: 0.5rem 1rem;
  border-radius: 20px;
  font-weight: 600;
  font-size: 0.875rem;
}

.answer-result {
  padding: 0.5rem 1rem;
  border-radius: 20px;
  font-weight: 600;
  font-size: 0.875rem;
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
.correct-answer,
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
}

.correct-answer .answer-content {
  background: rgba(34, 197, 94, 0.1);
  color: #16a34a;
  border: 1px solid #22c55e;
}

.wrong-answer {
  background: rgba(239, 68, 68, 0.1);
  color: #dc2626;
  border: 1px solid #ef4444;
}

.comment-text {
  background: #f9fafb;
  padding: 0.75rem;
  border-radius: 8px;
  font-size: 0.875rem;
  color: #1f2937;
  border: 1px solid #e5e7eb;
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
  border-top: 1px solid #e5e7eb;
  justify-content: flex-end;
}

.dark .modal-actions {
  border-top-color: #3D8D7A;
}

/* Responsive */
@media (max-width: 768px) {
  .grades-page {
    padding: 1rem;
  }

  .section-header-content {
    flex-direction: column;
    gap: 1rem;
  }

  .stats-grid {
    grid-template-columns: repeat(2, 1fr);
  }

  .grade-content {
    flex-direction: column;
    align-items: flex-start;
    gap: 1rem;
  }

  .submission-info {
    align-items: flex-start;
  }

  .grade-actions {
    justify-content: flex-start;
  }

  .grades-table-container {
    overflow-x: auto;
  }

  .grades-table {
    min-width: 600px;
  }

  .answer-modal {
    width: 95%;
  }

  .modal-actions {
    flex-direction: column-reverse;
  }

  .modal-actions .btn {
    width: 100%;
  }
}

@media (max-width: 480px) {
  .stats-grid {
    grid-template-columns: 1fr;
  }
}
</style>