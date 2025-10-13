<template>
  <div class="min-h-screen bg-gradient-to-br from-blue-50 via-indigo-50 to-purple-50 p-6">
    <!-- Animated Background Shapes -->
    <div class="fixed inset-0 overflow-hidden pointer-events-none">
      <div class="floating-shape shape-1"></div>
      <div class="floating-shape shape-2"></div>
      <div class="floating-shape shape-3"></div>
    </div>

    <div class="max-w-6xl mx-auto relative z-10">
      <!-- Loading State -->
      <div v-if="isLoading" class="glass-card p-12 text-center slide-up">
        <div class="w-16 h-16 border-4 border-blue-500 border-t-transparent rounded-full animate-spin mx-auto mb-4"></div>
        <p class="text-gray-600 font-semibold">Loading quizzes...</p>
      </div>

      <!-- Quiz History View (Default when not taking quiz) -->
      <div v-else-if="!quizStarted && !isLoading" class="slide-up space-y-6">
        <!-- Header -->
        <div class="glass-card p-6">
          <div class="flex items-center justify-between">
            <div>
              <h2 class="text-3xl font-bold text-gray-800">{{ subjectName }}</h2>
              <p class="text-gray-600">{{ sectionName }}</p>
            </div>
            <button @click="goBackToSubjects" class="btn-secondary">
              <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"/>
              </svg>
              Back to Subjects
            </button>
          </div>
        </div>

        <!-- Available Quizzes -->
        <div v-if="availableQuizzes.length > 0" class="glass-card p-6">
          <h3 class="text-2xl font-bold text-gray-800 mb-4">📝 Available Quizzes</h3>
          <div class="space-y-3">
            <div v-for="quiz in availableQuizzes" :key="quiz.quiz_id" 
                 class="quiz-item available"
                 style="cursor: default;">
              <div class="flex-1">
                <div class="flex items-center gap-3 mb-2">
                  <h4 class="text-xl font-bold text-gray-800">{{ quiz.title }}</h4>
                  <span class="badge badge-new">New</span>
                  <!-- Quiz Code Display -->
                  <span class="quiz-code-badge">
                    🔑 {{ quiz.quiz_code || 'N/A' }}
                  </span>
                </div>
                <p class="text-gray-600 text-sm mb-3">{{ quiz.description }}</p>
                <div class="flex items-center gap-4 text-sm">
                  <span class="quiz-stat">📝 {{ quiz.number_of_questions }} Questions</span>
                  <span v-if="quiz.has_time_limit" class="quiz-stat">⏱️ {{ quiz.time_limit_minutes }} min</span>
                  <span class="quiz-stat">🔁 {{ quiz.attempts_used }}/{{ quiz.attempts_allowed === 999 ? '∞' : quiz.attempts_allowed }} Attempts</span>
                </div>
              </div>
              <button @click="selectQuiz(quiz)" class="btn-take-quiz" style="pointer-events: auto;">
                Start Quiz
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
                </svg>
              </button>
            </div>
          </div>
        </div>

        <!-- Completed Quizzes -->
        <div v-if="completedQuizzes.length > 0" class="glass-card p-6">
          <h3 class="text-2xl font-bold text-gray-800 mb-4">✅ Completed Quizzes</h3>
          <div class="space-y-3">
            <div v-for="quiz in completedQuizzes" :key="quiz.quiz_id" 
                 class="quiz-item completed"
                 @click="viewQuizResult(quiz)">
              <div class="flex-1">
                <div class="flex items-center gap-3 mb-2">
                  <h4 class="text-lg font-bold text-gray-800">{{ quiz.title }}</h4>
                  <span :class="['badge', getScoreBadgeClass(quiz.best_percentage)]">
                    {{ quiz.best_percentage }}%
                  </span>
                  <!-- Quiz Code Display -->
                  <span class="quiz-code-badge">
                    🔑 {{ quiz.quiz_code || 'N/A' }}
                  </span>
                </div>
                <div class="flex items-center gap-4 text-sm text-gray-600">
                  <span>Best Score: {{ quiz.best_score }}/{{ quiz.max_score }} points</span>
                  <span>Attempts: {{ quiz.total_attempts }}</span>
                  <span>Last taken: {{ formatDate(quiz.latest_attempt_date) }}</span>
                </div>
              </div>
              <button class="btn-view-result">
                View Results
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
                </svg>
              </button>
            </div>
          </div>
        </div>

        <!-- No Quizzes Available -->
        <div v-if="availableQuizzes.length === 0 && completedQuizzes.length === 0" class="glass-card p-12 text-center">
          <div class="w-32 h-32 mx-auto mb-6 bg-gradient-to-br from-gray-300 to-gray-400 rounded-full flex items-center justify-center shadow-lg">
            <svg class="w-16 h-16 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/>
            </svg>
          </div>
          <h2 class="text-3xl font-bold text-gray-800 mb-4">No Quizzes Available Yet</h2>
          <p class="text-gray-600 mb-6">Your teacher hasn't published any quizzes for this section yet.</p>
        </div>
      </div>

      <!-- Quiz Start Screen -->
      <div v-else-if="selectedQuiz && !quizStarted" class="slide-up">
        <div class="glass-card p-8">
          <button @click="backToList" class="btn-back mb-6">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"/>
            </svg>
            Back to Quiz List
          </button>

          <h2 class="text-3xl font-bold text-gray-800 mb-2">{{ selectedQuiz.title }}</h2>
          
          <!-- Quiz Code Display in Start Screen -->
          <div class="quiz-code-display-large mb-4">
            <span class="code-icon">🔑</span>
            <div class="code-info">
              <span class="code-label">Quiz Code</span>
              <span class="code-value">{{ selectedQuiz.quiz_code || 'N/A' }}</span>
            </div>
          </div>

          <p class="text-gray-600 mb-6">{{ selectedQuiz.description }}</p>

          <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
            <div class="info-card">
              <div class="text-4xl mb-2">📝</div>
              <div class="text-2xl font-bold text-gray-800">{{ selectedQuiz.number_of_questions }}</div>
              <div class="text-sm text-gray-600">Questions</div>
            </div>
            <div class="info-card">
              <div class="text-4xl mb-2">⏱️</div>
              <div class="text-2xl font-bold text-gray-800">
                {{ selectedQuiz.has_time_limit ? selectedQuiz.time_limit_minutes + ' min' : 'No Limit' }}
              </div>
              <div class="text-sm text-gray-600">Time Limit</div>
            </div>
            <div class="info-card">
              <div class="text-4xl mb-2">🔁</div>
              <div class="text-2xl font-bold text-gray-800">
                {{ attemptsUsed }}/{{ selectedQuiz.attempts_allowed === 999 ? '∞' : selectedQuiz.attempts_allowed }}
              </div>
              <div class="text-sm text-gray-600">Attempts</div>
            </div>
          </div>

          <!-- Previous Attempts -->
          <div v-if="previousAttempts.length > 0" class="mb-6">
            <h3 class="text-lg font-bold text-gray-800 mb-3">Your Previous Attempts</h3>
            <div class="space-y-2">
              <div v-for="attempt in previousAttempts" :key="attempt.id" class="attempt-card">
                <div class="flex items-center justify-between">
                  <div>
                    <span class="font-semibold">Attempt {{ attempt.attempt_number }}</span>
                    <span class="text-gray-600 ml-3">{{ formatDateTime(attempt.submitted_at) }}</span>
                  </div>
                  <div class="text-right">
                    <div :class="['text-2xl font-bold', getScoreColor(attempt.percentage)]">
                      {{ attempt.percentage }}%
                    </div>
                    <div class="text-sm text-gray-600">{{ attempt.total_score }}/{{ attempt.max_score }} points</div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- Warnings -->
          <div v-if="selectedQuiz.attempts_allowed !== 999 && attemptsUsed >= selectedQuiz.attempts_allowed" class="alert-danger mb-6">
            <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 20 20">
              <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" clip-rule="evenodd"/>
            </svg>
            <div>
              <strong>No Attempts Remaining</strong>
              <p>You have used all {{ selectedQuiz.attempts_allowed }} attempts for this quiz.</p>
            </div>
          </div>

          <div v-else-if="selectedQuiz.has_time_limit" class="alert-warning mb-6">
            <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 20 20">
              <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm1-12a1 1 0 10-2 0v4a1 1 0 00.293.707l2.828 2.829a1 1 0 101.415-1.415L11 9.586V6z" clip-rule="evenodd"/>
            </svg>
            <div>
              <strong>Time Limit: {{ selectedQuiz.time_limit_minutes }} minutes</strong>
              <p>Once you start, the timer will begin. Make sure you have enough time to complete the quiz.</p>
            </div>
          </div>

          <button 
            @click="startQuiz" 
            :disabled="selectedQuiz.attempts_allowed !== 999 && attemptsUsed >= selectedQuiz.attempts_allowed"
            class="btn-start"
            :class="{ 'opacity-50 cursor-not-allowed': selectedQuiz.attempts_allowed !== 999 && attemptsUsed >= selectedQuiz.attempts_allowed }">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14.752 11.168l-3.197-2.132A1 1 0 0010 9.87v4.263a1 1 0 001.555.832l3.197-2.132a1 1 0 000-1.664z"/>
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
            </svg>
            Start Quiz
          </button>
        </div>
      </div>

      <!-- Quiz Taking Interface -->
      <div v-else-if="quizStarted && !quizSubmitted" class="slide-up space-y-6">
        <!-- Timer and Progress -->
        <div class="glass-card p-6">
          <div class="flex items-center justify-between mb-4">
            <div>
              <h3 class="text-xl font-bold text-gray-800">{{ selectedQuiz.title }}</h3>
              <p class="text-sm text-gray-600">Question {{ currentQuestionIndex + 1 }} of {{ questions.length }}</p>
            </div>
            <div v-if="selectedQuiz.has_time_limit" class="text-right">
              <div class="text-3xl font-bold" :class="timeRemaining < 60 ? 'text-red-600' : 'text-blue-600'">
                {{ formatTime(timeRemaining) }}
              </div>
              <div class="text-sm text-gray-600">Time Remaining</div>
            </div>
          </div>
          <div class="progress-bar">
            <div class="progress-fill" :style="{ width: progressPercentage + '%' }"></div>
          </div>
        </div>

        <!-- Question Card -->
        <div class="glass-card p-8">
          <div class="flex items-start gap-4 mb-6">
            <div class="question-number">{{ currentQuestionIndex + 1 }}</div>
            <div class="flex-1">
              <h2 class="text-2xl font-bold text-gray-800 mb-4">{{ currentQuestion.question_text }}</h2>

              <!-- Multiple Choice -->
              <div v-if="currentQuestion.question_type === 'multiple_choice'" class="space-y-3">
                <div v-for="(option, index) in currentQuestion.options" :key="option.id"
                     @click="selectAnswer(option.id)"
                     :class="['answer-option', { 'selected': studentAnswers[currentQuestion.id]?.selected_option_id === option.id }]">
                  <div class="option-indicator">{{ String.fromCharCode(65 + index) }}</div>
                  <span class="flex-1">{{ option.option_text }}</span>
                  <svg class="check-icon w-6 h-6" fill="currentColor" viewBox="0 0 20 20">
                    <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/>
                  </svg>
                </div>
              </div>

              <!-- True/False -->
              <div v-else-if="currentQuestion.question_type === 'true_false'" class="grid grid-cols-2 gap-4">
                <div @click="selectTrueFalse('true')"
                     :class="['tf-answer-option', { 'selected': studentAnswers[currentQuestion.id]?.answer_text === 'true' }]">
                  <div class="text-6xl mb-3">✅</div>
                  <div class="text-2xl font-bold">True</div>
                </div>
                <div @click="selectTrueFalse('false')"
                     :class="['tf-answer-option', { 'selected': studentAnswers[currentQuestion.id]?.answer_text === 'false' }]">
                  <div class="text-6xl mb-3">❌</div>
                  <div class="text-2xl font-bold">False</div>
                </div>
              </div>

              <!-- Fill in the Blank -->
              <div v-else-if="currentQuestion.question_type === 'fill_blank'">
                <input 
                  v-model="studentAnswers[currentQuestion.id].answer_text"
                  @input="autoSaveAnswer"
                  type="text" 
                  placeholder="Type your answer here..." 
                  class="fill-input"
                />
              </div>
            </div>
          </div>

          <!-- Navigation -->
          <div class="flex items-center justify-between pt-6 border-t border-gray-200">
            <button 
              @click="previousQuestion" 
              :disabled="currentQuestionIndex === 0"
              class="btn-nav"
              :class="{ 'opacity-50 cursor-not-allowed': currentQuestionIndex === 0 }">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"/>
              </svg>
              Previous
            </button>

            <div class="flex items-center gap-2 flex-wrap justify-center">
              <button 
                v-for="(q, index) in questions" 
                :key="q.id"
                @click="goToQuestion(index)"
                :class="['question-dot', { 
                  'active': index === currentQuestionIndex,
                  'answered': isQuestionAnswered(q.id)
                }]">
                {{ index + 1 }}
              </button>
            </div>

            <button 
              v-if="currentQuestionIndex < questions.length - 1"
              @click="nextQuestion" 
              class="btn-nav-primary">
              Next
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
              </svg>
            </button>

            <button 
              v-else
              @click="showSubmitModal = true" 
              class="btn-nav-primary">
              Submit Quiz
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
              </svg>
            </button>
          </div>
        </div>
      </div>

      <!-- Quiz Submitted -->
      <div v-else-if="quizSubmitted" class="slide-up">
        <div class="glass-card p-12 text-center">
          <div class="w-32 h-32 mx-auto mb-6 bg-gradient-to-br from-green-400 to-green-600 rounded-full flex items-center justify-center shadow-lg animate-bounce-slow">
            <svg class="w-16 h-16 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
            </svg>
          </div>
          
          <h2 class="text-3xl font-bold text-gray-800 mb-4">Quiz Submitted Successfully!</h2>
          <p class="text-gray-600 mb-8">Your answers have been recorded and automatically graded.</p>
          
          <div class="flex justify-center gap-4">
            <button @click="backToQuizList" class="btn-primary">
              <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
              </svg>
              View Quiz List
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Submit Confirmation Modal -->
    <div v-if="showSubmitModal" class="modal-overlay" @click="showSubmitModal = false">
      <div class="modal-content" @click.stop>
        <div class="modal-header">
          <svg class="w-12 h-12 text-yellow-500 mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/>
          </svg>
          <h3 class="text-2xl font-bold text-gray-800">Submit Quiz?</h3>
        </div>
        <div class="modal-body">
          <p class="text-gray-600 mb-4">Are you sure you want to submit? You cannot change your answers after submission.</p>
          <div class="bg-blue-50 rounded-lg p-4 border-l-4 border-blue-500">
            <div class="flex items-center justify-between text-sm">
              <span class="text-gray-700">Answered Questions:</span>
              <span class="font-bold text-blue-600">{{ answeredCount }} / {{ questions.length }}</span>
            </div>
            <div v-if="answeredCount < questions.length" class="flex items-center justify-between text-sm mt-2">
              <span class="text-gray-700">Unanswered:</span>
              <span class="font-bold text-red-600">{{ questions.length - answeredCount }}</span>
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <button @click="showSubmitModal = false" class="btn-secondary-modal flex-1">
            Cancel
          </button>
          <button @click="submitQuiz" :disabled="isSubmitting" class="btn-submit flex-1">
            <div v-if="isSubmitting" class="spinner-small"></div>
            <svg v-else class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
            </svg>
            {{ isSubmitting ? 'Submitting...' : 'Yes, Submit' }}
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, computed, onMounted, onBeforeUnmount } from 'vue';
import { useRouter, useRoute } from 'vue-router';
import { supabase } from '@/supabase';

export default {
  name: 'TakeQuiz',
  setup() {
    const router = useRouter();
    const route = useRoute();

    // State
    const isLoading = ref(true);
    const sectionId = ref(null);
    const sectionName = ref('Loading...');
    const subjectName = ref('Loading...');
    const studentId = ref(null);
    const availableQuizzes = ref([]);
    const completedQuizzes = ref([]);
    const selectedQuiz = ref(null);
    const questions = ref([]);
    const currentQuestionIndex = ref(0);
    const studentAnswers = ref({});
    const quizStarted = ref(false);
    const quizSubmitted = ref(false);
    const showSubmitModal = ref(false);
    const timeRemaining = ref(0);
    const timerInterval = ref(null);
    const attemptsUsed = ref(0);
    const previousAttempts = ref([]);
    const attemptId = ref(null);
    const isSubmitting = ref(false);
    const quizStartTime = ref(null);

    // Computed
    const currentQuestion = computed(() => {
      return questions.value[currentQuestionIndex.value] || {};
    });

    const progressPercentage = computed(() => {
      return ((currentQuestionIndex.value + 1) / questions.value.length) * 100;
    });

    const answeredCount = computed(() => {
      return Object.values(studentAnswers.value).filter(answer => 
        answer.selected_option_id || answer.answer_text
      ).length;
    });

    // Methods
    const fetchCurrentUser = async () => {
      try {
        const { data: { session }, error: sessionError } = await supabase.auth.getSession();
        
        if (sessionError || !session?.user) {
          throw new Error('No active session');
        }

        const { data: profile, error: profileError } = await supabase
          .from('profiles')
          .select('id, role')
          .eq('auth_user_id', session.user.id)
          .single();

        if (profileError || !profile || profile.role !== 'student') {
          throw new Error('Student profile not found');
        }

        const { data: student, error: studentError } = await supabase
          .from('students')
          .select('id')
          .eq('profile_id', profile.id)
          .eq('is_active', true)
          .single();

        if (studentError || !student) {
          throw new Error('Student record not found');
        }

        studentId.value = student.id;
        return true;
      } catch (error) {
        console.error('Error fetching current user:', error);
        alert('Error: Could not identify student. Please log in again.');
        router.push('/login');
        return false;
      }
    };

    const loadAllQuizzes = async () => {
      isLoading.value = true;
      
      try {
        const userSuccess = await fetchCurrentUser();
        if (!userSuccess) return;

        if (!studentId.value || !sectionId.value) {
          throw new Error('Missing student or section information');
        }

        // Fetch quizzes with quiz_code
        const { data: allQuizzes, error: quizError } = await supabase
          .from('quizzes')
          .select('*')
          .eq('section_id', sectionId.value)
          .eq('status', 'published')
          .order('created_at', { ascending: false });

        if (quizError) throw quizError;

        if (!allQuizzes || allQuizzes.length === 0) {
          availableQuizzes.value = [];
          completedQuizzes.value = [];
          isLoading.value = false;
          return;
        }

        const quizIds = allQuizzes.map(q => q.id);
        const { data: results } = await supabase
          .from('quiz_results')
          .select('*')
          .eq('student_id', studentId.value)
          .in('quiz_id', quizIds);

        const resultsMap = {};
        (results || []).forEach(r => {
          resultsMap[r.quiz_id] = r;
        });

        const { data: attempts } = await supabase
          .from('quiz_attempts')
          .select('quiz_id, attempt_number, status')
          .eq('student_id', studentId.value)
          .in('quiz_id', quizIds);

        const attemptsMap = {};
        (attempts || []).forEach(a => {
          if (!attemptsMap[a.quiz_id]) attemptsMap[a.quiz_id] = [];
          attemptsMap[a.quiz_id].push(a);
        });

        const now = new Date();
        const available = [];
        const completed = [];

        allQuizzes.forEach(quiz => {
          const startOk = !quiz.start_date || new Date(quiz.start_date) <= now;
          const endOk = !quiz.end_date || new Date(quiz.end_date) >= now;
          
          if (!startOk || !endOk) return;

          const quizAttempts = (attemptsMap[quiz.id] || []).filter(a =>  
            ['submitted', 'graded', 'reviewed'].includes(a.status)
          );
          const attemptsUsedCount = quizAttempts.length;
          const hasAttemptsRemaining = quiz.attempts_allowed === 999 || attemptsUsedCount < quiz.attempts_allowed;

          const result = resultsMap[quiz.id];

          if (result && result.status === 'completed') {
            completed.push({
              ...quiz,
              quiz_id: quiz.id,
              best_score: result.best_score,
              best_percentage: result.best_percentage,
              max_score: quizAttempts[0]?.max_score || quiz.number_of_questions,
              total_attempts: result.total_attempts,
              latest_attempt_date: result.latest_attempt_date,
              can_retake: hasAttemptsRemaining
            });
          } else if (hasAttemptsRemaining) {
            available.push({
              ...quiz,
              quiz_id: quiz.id,
              attempts_used: attemptsUsedCount,
              is_available: true
            });
          }
        });

        availableQuizzes.value = available;
        completedQuizzes.value = completed;
        
      } catch (error) {
        console.error('Error loading quizzes:', error);
        alert('Failed to load quizzes: ' + error.message);
      } finally {
        isLoading.value = false;
      }
    };
    
    const goBackToSubjects = () => {
      router.push('/student/subjects');
    };

    const backToList = () => {
      selectedQuiz.value = null;
      previousAttempts.value = [];
      attemptsUsed.value = 0;
    };

    const backToQuizList = () => {
      quizSubmitted.value = false;
      quizStarted.value = false;
      selectedQuiz.value = null;
      currentQuestionIndex.value = 0;
      questions.value = [];
      studentAnswers.value = {};
      loadAllQuizzes();
    };
    
    const selectQuiz = async (quiz, event) => {
      if (event && event.target.closest('.btn-take-quiz')) {
        return;
      }
      selectedQuiz.value = quiz;
      await loadQuizDetails();
    };

    const viewQuizResult = (quiz) => {
      alert('View quiz results feature coming soon!');
    };
    
    const loadQuizDetails = async () => {
      if (!selectedQuiz.value) return;
      
      try {
        const { data: attempts, error: attemptsError } = await supabase
          .from('quiz_attempts')
          .select('*')
          .eq('quiz_id', selectedQuiz.value.quiz_id)
          .eq('student_id', studentId.value)
          .in('status', ['submitted', 'graded', 'reviewed'])
          .order('attempt_number', { ascending: false });

        if (attemptsError) {
          console.warn('Error loading attempts:', attemptsError);
        } else {
          previousAttempts.value = attempts || [];
          attemptsUsed.value = previousAttempts.value.length;
        }
      } catch (error) {
        console.error('Error loading quiz details:', error);
      }
    };
    
    const startQuiz = async (event) => {
      if (event) {
        event.stopPropagation();
        event.preventDefault();
      }

      try {
        console.log('🎯 Starting quiz...', selectedQuiz.value);
        
        const canTake = selectedQuiz.value.attempts_allowed === 999 || 
                       attemptsUsed.value < selectedQuiz.value.attempts_allowed;

        if (!canTake) {
          alert('You have no attempts remaining for this quiz.');
          return;
        }

        const quizId = selectedQuiz.value.quiz_id || selectedQuiz.value.id;
        console.log('📝 Fetching questions for quiz_id:', quizId);
        
        const { data: quizQuestions, error: questionsError } = await supabase
          .from('quiz_questions')
          .select(`
            id,
            question_number,
            question_type,
            question_text,
            points,
            question_options (
              id,
              option_number,
              option_text,
              is_correct
            )
          `)
          .eq('quiz_id', quizId)
          .order('question_number', { ascending: true });
        
        console.log('✅ Questions fetched:', quizQuestions);
        
        if (questionsError) {
          throw new Error('Failed to load quiz questions: ' + questionsError.message);
        }

        if (!quizQuestions || quizQuestions.length === 0) {
          throw new Error('This quiz has no questions. Please contact your teacher.');
        }

        questions.value = quizQuestions.map(q => ({
          ...q,
          options: (q.question_options || []).sort((a, b) => a.option_number - b.option_number)
        }));

        const maxScore = questions.value.reduce((sum, q) => sum + (q.points || 1), 0);

        const { data: newAttempt, error: attemptError } = await supabase
          .from('quiz_attempts')
          .insert([{
            quiz_id: quizId,
            student_id: studentId.value,
            attempt_number: attemptsUsed.value + 1,
            max_score: maxScore,
            status: 'in_progress'
          }])
          .select()
          .single();

        if (attemptError) {
          throw new Error('Failed to start quiz attempt: ' + attemptError.message);
        }

        attemptId.value = newAttempt.id;
        quizStartTime.value = Date.now();

        questions.value.forEach(q => {
          studentAnswers.value[q.id] = {
            question_id: q.id,
            selected_option_id: null,
            answer_text: '',
            points_possible: q.points || 1
          };
        });

        quizStarted.value = true;

        if (selectedQuiz.value.has_time_limit) {
          timeRemaining.value = selectedQuiz.value.time_limit_minutes * 60;
          startTimer();
        }

      } catch (error) {
        console.error('💥 Error starting quiz:', error);
        alert(`Failed to start quiz: ${error.message}`);
      }
    };
    
    const startTimer = () => {
      timerInterval.value = setInterval(() => {
        if (timeRemaining.value > 0) {
          timeRemaining.value--;
        } else {
          autoSubmitQuiz();
        }
      }, 1000);
    };
    
    const formatTime = (seconds) => {
      const mins = Math.floor(seconds / 60);
      const secs = seconds % 60;
      return `${mins}:${secs.toString().padStart(2, '0')}`;
    };
    
    const formatDateTime = (dateString) => {
      return new Date(dateString).toLocaleString();
    };

    const formatDate = (dateString) => {
      return new Date(dateString).toLocaleDateString();
    };
    
    const getScoreColor = (percentage) => {
      if (percentage >= 90) return 'text-green-600';
      if (percentage >= 75) return 'text-blue-600';
      if (percentage >= 60) return 'text-yellow-600';
      return 'text-red-600';
    };

    const getScoreBadgeClass = (percentage) => {
      if (percentage >= 90) return 'badge-excellent';
      if (percentage >= 75) return 'badge-good';
      if (percentage >= 60) return 'badge-fair';
      return 'badge-poor';
    };
    
    const selectAnswer = async (optionId) => {
      studentAnswers.value[currentQuestion.value.id].selected_option_id = optionId;
      studentAnswers.value[currentQuestion.value.id].answer_text = null;
      await autoSaveAnswer();
    };

    const selectTrueFalse = async (value) => {
      studentAnswers.value[currentQuestion.value.id].answer_text = value;
      studentAnswers.value[currentQuestion.value.id].selected_option_id = null;
      await autoSaveAnswer();
    };

    const autoSaveAnswer = async () => {
      if (!attemptId.value || !currentQuestion.value.id) return;

      try {
        const answer = studentAnswers.value[currentQuestion.value.id];
        
        const { data: existing } = await supabase
          .from('student_answers')
          .select('id')
          .eq('attempt_id', attemptId.value)
          .eq('question_id', currentQuestion.value.id)
          .maybeSingle();

        if (existing) {
          await supabase
            .from('student_answers')
            .update({
              selected_option_id: answer.selected_option_id,
              answer_text: answer.answer_text,
              points_possible: answer.points_possible
            })
            .eq('id', existing.id);
        } else {
          await supabase
            .from('student_answers')
            .insert([{
              attempt_id: attemptId.value,
              question_id: currentQuestion.value.id,
              selected_option_id: answer.selected_option_id,
              answer_text: answer.answer_text,
              points_possible: answer.points_possible
            }]);
        }
      } catch (error) {
        console.error('Error auto-saving answer:', error);
      }
    };
    
    const nextQuestion = () => {
      if (currentQuestionIndex.value < questions.value.length - 1) {
        currentQuestionIndex.value++;
      }
    };
    
    const previousQuestion = () => {
      if (currentQuestionIndex.value > 0) {
        currentQuestionIndex.value--;
      }
    };
    
    const goToQuestion = (index) => {
      currentQuestionIndex.value = index;
    };
    
    const isQuestionAnswered = (questionId) => {
      const answer = studentAnswers.value[questionId];
      return !!(answer?.selected_option_id || answer?.answer_text);
    };
    
    const submitQuiz = async () => {
      if (isSubmitting.value) return;

      isSubmitting.value = true;
      showSubmitModal.value = false;

      try {
        if (timerInterval.value) {
          clearInterval(timerInterval.value);
        }

        const timeTaken = Math.floor((Date.now() - quizStartTime.value) / 1000);
        const timeTakenMinutes = Math.ceil(timeTaken / 60);

        for (const questionId in studentAnswers.value) {
          const answer = studentAnswers.value[questionId];
          if (answer.selected_option_id || answer.answer_text) {
            const { data: existing } = await supabase
              .from('student_answers')
              .select('id')
              .eq('attempt_id', attemptId.value)
              .eq('question_id', questionId)
              .maybeSingle();

            if (existing) {
              await supabase
                .from('student_answers')
                .update({
                  selected_option_id: answer.selected_option_id,
                  answer_text: answer.answer_text,
                  points_possible: answer.points_possible
                })
                .eq('id', existing.id);
            } else {
              await supabase
                .from('student_answers')
                .insert([{
                  attempt_id: attemptId.value,
                  question_id: questionId,
                  selected_option_id: answer.selected_option_id,
                  answer_text: answer.answer_text,
                  points_possible: answer.points_possible
                }]);
            }
          }
        }

        const { error: submitError } = await supabase
          .from('quiz_attempts')
          .update({
            status: 'submitted',
            submitted_at: new Date().toISOString(),
            time_taken_minutes: timeTakenMinutes
          })
          .eq('id', attemptId.value);

        if (submitError) {
          throw new Error('Failed to submit quiz: ' + submitError.message);
        }

        quizSubmitted.value = true;

      } catch (error) {
        console.error('Error submitting quiz:', error);
        alert(`Failed to submit quiz: ${error.message}. Please try again.`);
        showSubmitModal.value = false;
      } finally {
        isSubmitting.value = false;
      }
    };
    
    const autoSubmitQuiz = () => {
      alert('Time is up! Your quiz will be automatically submitted.');
      submitQuiz();
    };

    onMounted(async () => {
      sectionId.value = route.params.sectionId;
      sectionName.value = route.query.sectionName || 'Section';
      subjectName.value = route.query.subjectName || 'Subject';

      if (!sectionId.value) {
        alert('Error: Missing section information. Redirecting to subjects page.');
        router.push('/student/subjects');
        return;
      }

      await loadAllQuizzes();
    });

    onBeforeUnmount(() => {
      if (timerInterval.value) {
        clearInterval(timerInterval.value);
      }
    });

    return {
      isLoading,
      sectionName,
      subjectName,
      availableQuizzes,
      completedQuizzes,
      selectedQuiz,
      questions,
      currentQuestionIndex,
      studentAnswers,
      quizStarted,
      quizSubmitted,
      showSubmitModal,
      timeRemaining,
      attemptsUsed,
      previousAttempts,
      isSubmitting,
      currentQuestion,
      progressPercentage,
      answeredCount,
      goBackToSubjects,
      backToList,
      backToQuizList,
      selectQuiz,
      viewQuizResult,
      startQuiz,
      formatTime,
      formatDateTime,
      formatDate,
      getScoreColor,
      getScoreBadgeClass,
      selectAnswer,
      selectTrueFalse,
      autoSaveAnswer,
      nextQuestion,
      previousQuestion,
      goToQuestion,
      isQuestionAnswered,
      submitQuiz
    };
  }
};
</script>

<style scoped>
.glass-card {
  background: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(20px);
  border-radius: 24px;
  border: 1px solid rgba(255, 255, 255, 0.3);
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
}

.floating-shape {
  position: absolute;
  border-radius: 50%;
  filter: blur(60px);
  opacity: 0.3;
  animation: float 20s infinite ease-in-out;
}

.shape-1 {
  width: 400px;
  height: 400px;
  background: linear-gradient(135deg, #3b82f6 0%, #8b5cf6 100%);
  top: -100px;
  right: -100px;
}

.shape-2 {
  width: 350px;
  height: 350px;
  background: linear-gradient(135deg, #06b6d4 0%, #3b82f6 100%);
  bottom: -100px;
  left: -50px;
}

.shape-3 {
  width: 300px;
  height: 300px;
  background: linear-gradient(135deg, #8b5cf6 0%, #ec4899 100%);
  top: 50%;
  left: 30%;
}

@keyframes float {
  0%, 100% { transform: translateY(0) rotate(0deg); }
  25% { transform: translateY(-30px) rotate(5deg); }
  50% { transform: translateY(0) rotate(0deg); }
  75% { transform: translateY(30px) rotate(-5deg); }
}

@keyframes slideUp {
  from { opacity: 0; transform: translateY(30px); }
  to { opacity: 1; transform: translateY(0); }
}

.slide-up { animation: slideUp 0.5s ease-out; }

@keyframes pulse-slow {
  0%, 100% { transform: scale(1); }
  50% { transform: scale(1.05); }
}

.animate-pulse-slow { animation: pulse-slow 3s ease-in-out infinite; }

@keyframes bounce-slow {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-20px); }
}

.animate-bounce-slow { animation: bounce-slow 2s ease-in-out infinite; }

@keyframes spin {
  to { transform: rotate(360deg); }
}

.animate-spin { animation: spin 1s linear infinite; }

.quiz-selection-card {
  background: white;
  border: 3px solid #e5e7eb;
  border-radius: 16px;
  padding: 1.5rem;
  cursor: pointer;
  transition: all 0.3s ease;
}

.quiz-selection-card:hover {
  border-color: #3b82f6;
  background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%);
  transform: translateX(8px);
  box-shadow: 0 8px 25px rgba(59, 130, 246, 0.3);
}

.quiz-badge {
  display: inline-flex;
  align-items: center;
  padding: 0.375rem 0.75rem;
  background: linear-gradient(135deg, #dbeafe 0%, #bfdbfe 100%);
  color: #1e40af;
  font-size: 0.875rem;
  font-weight: 600;
  border-radius: 8px;
}

.info-card {
  background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%);
  border: 2px solid #bae6fd;
  border-radius: 16px;
  padding: 1.25rem;
  text-align: center;
  transition: all 0.3s ease;
}

.info-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 25px rgba(59, 130, 246, 0.2);
}

.alert-warning {
  display: flex;
  align-items: start;
  background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);
  border: 2px solid #fbbf24;
  border-radius: 12px;
  padding: 1rem;
  color: #92400e;
}

.alert-danger {
  display: flex;
  align-items: start;
  background: linear-gradient(135deg, #fee2e2 0%, #fecaca 100%);
  border: 2px solid #f87171;
  border-radius: 12px;
  padding: 1rem;
  color: #991b1b;
}

.btn-start {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  padding: 1.25rem 2rem;
  background: linear-gradient(135deg, #3b82f6 0%, #8b5cf6 100%);
  color: white;
  font-weight: 700;
  font-size: 1.125rem;
  border-radius: 16px;
  border: none;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 8px 25px rgba(59, 130, 246, 0.5);
}

.btn-start:hover {
  transform: translateY(-3px);
  box-shadow: 0 12px 35px rgba(59, 130, 246, 0.7);
}

.btn-primary {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 0.875rem 2rem;
  background: linear-gradient(135deg, #3b82f6 0%, #8b5cf6 100%);
  color: white;
  font-weight: 600;
  border-radius: 12px;
  border: none;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 4px 15px rgba(59, 130, 246, 0.4);
}

.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(59, 130, 246, 0.6);
}

.btn-secondary {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 0.875rem 1.5rem;
  background: white;
  color: #4b5563;
  font-weight: 600;
  border-radius: 12px;
  border: 2px solid #e5e7eb;
  cursor: pointer;
  transition: all 0.3s ease;
}

.btn-secondary:hover {
  background: #f9fafb;
  border-color: #cbd5e1;
  transform: translateY(-2px);
}

.btn-nav {
  display: flex;
  align-items: center;
  padding: 0.75rem 1.5rem;
  background: white;
  color: #4b5563;
  font-weight: 600;
  border-radius: 10px;
  border: 2px solid #e5e7eb;
  cursor: pointer;
  transition: all 0.3s ease;
}

.btn-nav:hover:not(:disabled) {
  background: #f9fafb;
  border-color: #cbd5e1;
  transform: translateY(-1px);
}

.btn-nav-primary {
  display: flex;
  align-items: center;
  padding: 0.75rem 1.5rem;
  background: linear-gradient(135deg, #3b82f6 0%, #8b5cf6 100%);
  color: white;
  font-weight: 600;
  border-radius: 10px;
  border: none;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 4px 15px rgba(59, 130, 246, 0.4);
}

.btn-nav-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(59, 130, 246, 0.6);
}

.btn-submit {
  display: flex;
  align-items: center;
  padding: 0.875rem 2rem;
  background: linear-gradient(135deg, #10b981 0%, #059669 100%);
  color: white;
  font-weight: 700;
  border-radius: 12px;
  border: none;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 4px 15px rgba(16, 185, 129, 0.4);
}

.btn-submit:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(16, 185, 129, 0.6);
}

.question-number {
  width: 48px;
  height: 48px;
  background: linear-gradient(135deg, #3b82f6 0%, #8b5cf6 100%);
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-weight: 700;
  font-size: 1.25rem;
  margin-right: 1rem;
  flex-shrink: 0;
  box-shadow: 0 4px 15px rgba(59, 130, 246, 0.4);
}

.answer-option {
  display: flex;
  align-items: center;
  padding: 1.25rem;
  background: white;
  border: 3px solid #e5e7eb;
  border-radius: 16px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.answer-option:hover {
  border-color: #c7d2fe;
  background: #f9fafb;
  transform: translateX(4px);
}

.answer-option.selected {
  border-color: #3b82f6;
  background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%);
  box-shadow: 0 4px 15px rgba(59, 130, 246, 0.3);
}

.option-indicator {
  width: 36px;
  height: 36px;
  background: linear-gradient(135deg, #e0e7ff 0%, #ddd6fe 100%);
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  color: #4c1d95;
  margin-right: 1rem;
  flex-shrink: 0;
  transition: all 0.3s ease;
}

.answer-option.selected .option-indicator {
  background: linear-gradient(135deg, #3b82f6 0%, #8b5cf6 100%);
  color: white;
}

.check-icon {
  width: 32px;
  height: 32px;
  margin-left: 1rem;
  color: transparent;
  transition: all 0.3s ease;
}

.answer-option.selected .check-icon {
  color: #10b981;
}

.tf-answer-option {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 2rem;
  background: white;
  border: 3px solid #e5e7eb;
  border-radius: 20px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.tf-answer-option:hover {
  border-color: #c7d2fe;
  background: #f9fafb;
  transform: translateY(-4px);
  box-shadow: 0 8px 25px rgba(59, 130, 246, 0.2);
}

.tf-answer-option.selected {
  border-color: #3b82f6;
  background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%);
  box-shadow: 0 8px 25px rgba(59, 130, 246, 0.4);
  transform: scale(1.05);
}

.fill-input {
  width: 100%;
  padding: 1rem 1.25rem;
  border: 3px solid #e5e7eb;
  border-radius: 12px;
  font-size: 1rem;
  transition: all 0.3s ease;
  background: white;
}

.fill-input:focus {
  outline: none;
  border-color: #3b82f6;
  box-shadow: 0 0 0 4px rgba(59, 130, 246, 0.1);
}

.progress-bar {
  width: 100%;
  height: 8px;
  background: #e5e7eb;
  border-radius: 10px;
  overflow: hidden;
}

.progress-fill {
  height: 100%;
  background: linear-gradient(90deg, #3b82f6 0%, #8b5cf6 100%);
  border-radius: 10px;
  transition: width 0.3s ease;
}

.question-dot {
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 10px;
  border: 2px solid #e5e7eb;
  background: white;
  color: #6b7280;
  font-weight: 600;
  font-size: 0.875rem;
  cursor: pointer;
  transition: all 0.3s ease;
}

.question-dot:hover {
  border-color: #c7d2fe;
  transform: scale(1.1);
}

.question-dot.active {
  background: linear-gradient(135deg, #3b82f6 0%, #8b5cf6 100%);
  border-color: #3b82f6;
  color: white;
  box-shadow: 0 4px 15px rgba(59, 130, 246, 0.4);
}

.question-dot.answered {
  background: #d1fae5;
  border-color: #10b981;
  color: #065f46;
}

.question-dot.answered.active {
  background: linear-gradient(135deg, #10b981 0%, #059669 100%);
  border-color: #10b981;
  color: white;
}

.attempt-card {
  background: white;
  border: 2px solid #e5e7eb;
  border-radius: 12px;
  padding: 1rem;
  transition: all 0.3s ease;
}

.attempt-card:hover {
  border-color: #c7d2fe;
  box-shadow: 0 4px 15px rgba(59, 130, 246, 0.1);
  transform: translateY(-2px);
}

.modal-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.6);
  backdrop-filter: blur(4px);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 50;
  animation: fadeIn 0.3s ease;
}

.modal-content {
  background: white;
  border-radius: 24px;
  max-width: 500px;
  width: 90%;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
  animation: slideUp 0.3s ease;
}

.modal-header {
  padding: 2rem 2rem 1rem;
  text-align: center;
}

.modal-body {
  padding: 0 2rem 1.5rem;
}

.modal-footer {
  padding: 1.5rem 2rem;
  border-top: 1px solid #e5e7eb;
  display: flex;
  gap: 1rem;
}

@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

@media (max-width: 768px) {
  .glass-card { padding: 1.5rem; }
  .btn-start, .btn-primary, .btn-secondary, .btn-submit { width: 100%; }
  .info-card { padding: 1rem; }
  .question-dot { width: 36px; height: 36px; font-size: 0.75rem; }
  .modal-content { margin: 1rem; }
  .floating-shape { display: none; }
}

::-webkit-scrollbar { width: 10px; }
::-webkit-scrollbar-track { background: #f1f5f9; border-radius: 10px; }
::-webkit-scrollbar-thumb { background: linear-gradient(135deg, #3b82f6 0%, #8b5cf6 100%); border-radius: 10px; }
::-webkit-scrollbar-thumb:hover { background: linear-gradient(135deg, #8b5cf6 0%, #3b82f6 100%); }

.quiz-item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1.5rem;
  background: white;
  border: 2px solid #e5e7eb;
  border-radius: 16px;
  transition: all 0.3s ease;
  cursor: pointer;
}

.quiz-item:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
}

.quiz-item.available {
  border-left: 4px solid #3b82f6;
}

.quiz-item.available:hover {
  border-color: #3b82f6;
  background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%);
}

.quiz-item.completed {
  border-left: 4px solid #10b981;
}

.quiz-item.completed:hover {
  border-color: #10b981;
  background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%);
}

.quiz-stat {
  display: inline-flex;
  align-items: center;
  padding: 0.25rem 0.75rem;
  background: #f3f4f6;
  border-radius: 8px;
  font-weight: 600;
  color: #6b7280;
}

.badge {
  padding: 0.25rem 0.75rem;
  border-radius: 8px;
  font-size: 0.875rem;
  font-weight: 700;
}

.badge-new {
  background: linear-gradient(135deg, #3b82f6 0%, #8b5cf6 100%);
  color: white;
}

.badge-excellent {
  background: #10b981;
  color: white;
}

.badge-good {
  background: #3b82f6;
  color: white;
}

.badge-fair {
  background: #f59e0b;
  color: white;
}

.badge-poor {
  background: #ef4444;
  color: white;
}

.btn-take-quiz {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1.5rem;
  background: linear-gradient(135deg, #3b82f6 0%, #8b5cf6 100%);
  color: white;
  font-weight: 600;
  border-radius: 12px;
  border: none;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 4px 15px rgba(59, 130, 246, 0.4);
}

.btn-take-quiz:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(59, 130, 246, 0.6);
}

.btn-view-result {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1.5rem;
  background: white;
  color: #10b981;
  font-weight: 600;
  border-radius: 12px;
  border: 2px solid #10b981;
  cursor: pointer;
  transition: all 0.3s ease;
}

.btn-view-result:hover {
  background: #10b981;
  color: white;
  transform: translateY(-2px);
}

.btn-back {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1.25rem;
  background: white;
  color: #6b7280;
  font-weight: 600;
  border-radius: 12px;
  border: 2px solid #e5e7eb;
  cursor: pointer;
  transition: all 0.3s ease;
}

.btn-back:hover {
  background: #f9fafb;
  border-color: #cbd5e1;
  color: #3b82f6;
}

.btn-secondary-modal {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 0.875rem 1.5rem;
  background: white;
  color: #4b5563;
  font-weight: 600;
  border-radius: 12px;
  border: 2px solid #e5e7eb;
  cursor: pointer;
  transition: all 0.3s ease;
}

.btn-secondary-modal:hover {
  background: #f9fafb;
  border-color: #cbd5e1;
}

.spinner-small {
  width: 20px;
  height: 20px;
  border: 3px solid rgba(255, 255, 255, 0.3);
  border-top-color: white;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

.quiz-item {
  pointer-events: none;
}

.btn-take-quiz {
  pointer-events: auto;
}

.quiz-code-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.25rem;
  padding: 0.35rem 0.75rem;
  background: linear-gradient(135deg, rgba(59, 130, 246, 0.15) 0%, rgba(139, 92, 246, 0.15) 100%);
  border: 2px solid rgba(59, 130, 246, 0.4);
  border-radius: 8px;
  font-family: 'Courier New', monospace;
  font-weight: 700;
  font-size: 0.85rem;
  color: #3b82f6;
  letter-spacing: 1px;
}

.quiz-code-display-large {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1.25rem 1.5rem;
  background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%);
  border: 3px solid #3b82f6;
  border-radius: 16px;
  box-shadow: 0 4px 15px rgba(59, 130, 246, 0.25);
}

.code-icon {
  font-size: 2rem;
}

.code-info {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}

.code-label {
  font-size: 0.85rem;
  font-weight: 600;
  color: #6b7280;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.code-value {
  font-family: 'Courier New', monospace;
  font-size: 1.75rem;
  font-weight: 800;
  color: #3b82f6;
  letter-spacing: 2px;
}

/* All your existing styles below - keeping them exactly as they are */
.glass-card {
  background: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(20px);
  border-radius: 24px;
  border: 1px solid rgba(255, 255, 255, 0.3);
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
}

.floating-shape {
  position: absolute;
  border-radius: 50%;
  filter: blur(60px);
  opacity: 0.3;
  animation: float 20s infinite ease-in-out;
}

.shape-1 {
  width: 400px;
  height: 400px;
  background: linear-gradient(135deg, #3b82f6 0%, #8b5cf6 100%);
  top: -100px;
  right: -100px;
}

.shape-2 {
  width: 350px;
  height: 350px;
  background: linear-gradient(135deg, #06b6d4 0%, #3b82f6 100%);
  bottom: -100px;
  left: -50px;
}

.shape-3 {
  width: 300px;
  height: 300px;
  background: linear-gradient(135deg, #8b5cf6 0%, #ec4899 100%);
  top: 50%;
  left: 30%;
}

@keyframes float {
  0%, 100% { transform: translateY(0) rotate(0deg); }
  25% { transform: translateY(-30px) rotate(5deg); }
  50% { transform: translateY(0) rotate(0deg); }
  75% { transform: translateY(30px) rotate(-5deg); }
}

@keyframes slideUp {
  from { opacity: 0; transform: translateY(30px); }
  to { opacity: 1; transform: translateY(0); }
}

.slide-up { animation: slideUp 0.5s ease-out; }

@keyframes pulse-slow {
  0%, 100% { transform: scale(1); }
  50% { transform: scale(1.05); }
}

.animate-pulse-slow { animation: pulse-slow 3s ease-in-out infinite; }

@keyframes bounce-slow {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-20px); }
}

.animate-bounce-slow { animation: bounce-slow 2s ease-in-out infinite; }

@keyframes spin {
  to { transform: rotate(360deg); }
}

.animate-spin { animation: spin 1s linear infinite; }

.quiz-item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1.5rem;
  background: white;
  border: 2px solid #e5e7eb;
  border-radius: 16px;
  transition: all 0.3s ease;
  cursor: pointer;
  pointer-events: none;
}

.quiz-item:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
}

.quiz-item.available {
  border-left: 4px solid #3b82f6;
}

.quiz-item.available:hover {
  border-color: #3b82f6;
  background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%);
}

.quiz-item.completed {
  border-left: 4px solid #10b981;
}

.quiz-item.completed:hover {
  border-color: #10b981;
  background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%);
}

.quiz-stat {
  display: inline-flex;
  align-items: center;
  padding: 0.25rem 0.75rem;
  background: #f3f4f6;
  border-radius: 8px;
  font-weight: 600;
  color: #6b7280;
}

.badge {
  padding: 0.25rem 0.75rem;
  border-radius: 8px;
  font-size: 0.875rem;
  font-weight: 700;
}

.badge-new {
  background: linear-gradient(135deg, #3b82f6 0%, #8b5cf6 100%);
  color: white;
}

.badge-excellent {
  background: #10b981;
  color: white;
}

.badge-good {
  background: #3b82f6;
  color: white;
}

.badge-fair {
  background: #f59e0b;
  color: white;
}

.badge-poor {
  background: #ef4444;
  color: white;
}

.btn-take-quiz {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1.5rem;
  background: linear-gradient(135deg, #3b82f6 0%, #8b5cf6 100%);
  color: white;
  font-weight: 600;
  border-radius: 12px;
  border: none;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 4px 15px rgba(59, 130, 246, 0.4);
  pointer-events: auto;
}

.btn-take-quiz:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(59, 130, 246, 0.6);
}

.btn-view-result {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1.5rem;
  background: white;
  color: #10b981;
  font-weight: 600;
  border-radius: 12px;
  border: 2px solid #10b981;
  cursor: pointer;
  transition: all 0.3s ease;
}

.btn-view-result:hover {
  background: #10b981;
  color: white;
  transform: translateY(-2px);
}

.btn-back {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1.25rem;
  background: white;
  color: #6b7280;
  font-weight: 600;
  border-radius: 12px;
  border: 2px solid #e5e7eb;
  cursor: pointer;
  transition: all 0.3s ease;
}

.btn-back:hover {
  background: #f9fafb;
  border-color: #cbd5e1;
  color: #3b82f6;
}

.btn-secondary {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 0.875rem 1.5rem;
  background: white;
  color: #4b5563;
  font-weight: 600;
  border-radius: 12px;
  border: 2px solid #e5e7eb;
  cursor: pointer;
  transition: all 0.3s ease;
}

.btn-secondary:hover {
  background: #f9fafb;
  border-color: #cbd5e1;
  transform: translateY(-2px);
}

.btn-primary {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 0.875rem 2rem;
  background: linear-gradient(135deg, #3b82f6 0%, #8b5cf6 100%);
  color: white;
  font-weight: 600;
  border-radius: 12px;
  border: none;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 4px 15px rgba(59, 130, 246, 0.4);
}

.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(59, 130, 246, 0.6);
}

.btn-start {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  padding: 1.25rem 2rem;
  background: linear-gradient(135deg, #3b82f6 0%, #8b5cf6 100%);
  color: white;
  font-weight: 700;
  font-size: 1.125rem;
  border-radius: 16px;
  border: none;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 8px 25px rgba(59, 130, 246, 0.5);
}

.btn-start:hover {
  transform: translateY(-3px);
  box-shadow: 0 12px 35px rgba(59, 130, 246, 0.7);
}

.btn-nav {
  display: flex;
  align-items: center;
  padding: 0.75rem 1.5rem;
  background: white;
  color: #4b5563;
  font-weight: 600;
  border-radius: 10px;
  border: 2px solid #e5e7eb;
  cursor: pointer;
  transition: all 0.3s ease;
}

.btn-nav:hover:not(:disabled) {
  background: #f9fafb;
  border-color: #cbd5e1;
  transform: translateY(-1px);
}

.btn-nav-primary {
  display: flex;
  align-items: center;
  padding: 0.75rem 1.5rem;
  background: linear-gradient(135deg, #3b82f6 0%, #8b5cf6 100%);
  color: white;
  font-weight: 600;
  border-radius: 10px;
  border: none;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 4px 15px rgba(59, 130, 246, 0.4);
}

.btn-nav-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(59, 130, 246, 0.6);
}

.btn-submit {
  display: flex;
  align-items: center;
  padding: 0.875rem 2rem;
  background: linear-gradient(135deg, #10b981 0%, #059669 100%);
  color: white;
  font-weight: 700;
  border-radius: 12px;
  border: none;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 4px 15px rgba(16, 185, 129, 0.4);
}

.btn-submit:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(16, 185, 129, 0.6);
}

.btn-secondary-modal {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 0.875rem 1.5rem;
  background: white;
  color: #4b5563;
  font-weight: 600;
  border-radius: 12px;
  border: 2px solid #e5e7eb;
  cursor: pointer;
  transition: all 0.3s ease;
}

.btn-secondary-modal:hover {
  background: #f9fafb;
  border-color: #cbd5e1;
}

.info-card {
  background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%);
  border: 2px solid #bae6fd;
  border-radius: 16px;
  padding: 1.25rem;
  text-align: center;
  transition: all 0.3s ease;
}

.info-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 25px rgba(59, 130, 246, 0.2);
}

.alert-warning {
  display: flex;
  align-items: start;
  background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);
  border: 2px solid #fbbf24;
  border-radius: 12px;
  padding: 1rem;
  color: #92400e;
}

.alert-danger {
  display: flex;
  align-items: start;
  background: linear-gradient(135deg, #fee2e2 0%, #fecaca 100%);
  border: 2px solid #f87171;
  border-radius: 12px;
  padding: 1rem;
  color: #991b1b;
}

.question-number {
  width: 48px;
  height: 48px;
  background: linear-gradient(135deg, #3b82f6 0%, #8b5cf6 100%);
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-weight: 700;
  font-size: 1.25rem;
  margin-right: 1rem;
  flex-shrink: 0;
  box-shadow: 0 4px 15px rgba(59, 130, 246, 0.4);
}

.answer-option {
  display: flex;
  align-items: center;
  padding: 1.25rem;
  background: white;
  border: 3px solid #e5e7eb;
  border-radius: 16px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.answer-option:hover {
  border-color: #c7d2fe;
  background: #f9fafb;
  transform: translateX(4px);
}

.answer-option.selected {
  border-color: #3b82f6;
  background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%);
  box-shadow: 0 4px 15px rgba(59, 130, 246, 0.3);
}

</style>