<template>
  <div class="home-container">
    <!-- Enhanced Header Section -->
    <div class="section-header-card">
      <!-- Background Decorations -->
      <div class="header-bg-decoration"></div>
      <div class="floating-shapes">
        <div class="shape shape-1"></div>
        <div class="shape shape-2"></div>
        <div class="shape shape-3"></div>
      </div>
      
      <div class="section-header-content">
        <div class="section-header-left">
          <div class="section-header-icon">
            <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M14,2H6A2,2 0 0,0 4,4V20A2,2 0 0,0 6,22H18A2,2 0 0,0 20,20V8L14,2M18,20H6V4H13V9H18V20Z" />
            </svg>
          </div>
          <div class="header-text">
            <div class="section-header-title">Create New Quiz</div>
            <div class="section-header-subtitle">{{ subjectName }} (Grade {{ gradeLevel }})</div>
            <div class="section-header-description">Design an assessment for {{ sectionName }} - {{ sectionCode }}</div>
          </div>
        </div>
        
        <button @click="goBack" class="back-button">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
            <path d="M10 19l-7-7 7-7m-7 7h18"></path>
          </svg>
          Back to Subjects
        </button>
      </div>
    </div>

    <div class="main-wrapper">
      <form @submit.prevent="submitQuiz" class="content-card">
        <div class="card-header">
          <h3>Quiz Details</h3>
          <p class="card-subtitle">Set up your assessment parameters and add questions</p>
        </div>
        
        <div class="form-content">
          <div class="quiz-meta">
            <div class="form-group">
              <label for="quiz-title">Quiz Title *</label>
              <input 
                type="text" 
                id="quiz-title" 
                v-model="quizTitle" 
                placeholder="e.g., Chapter 1 Assessment, Midterm Exam"
                required
              >
            </div>
            
            <div class="form-row">
              <div class="form-group">
                <label for="time-limit">Time Limit (minutes)</label>
                <input 
                  type="number" 
                  id="time-limit" 
                  v-model="timeLimit" 
                  min="1" 
                  max="300"
                  placeholder="60"
                >
              </div>
              
              <div class="form-group">
                <label for="total-points">Total Points</label>
                <input 
                  type="number" 
                  id="total-points" 
                  v-model="totalPoints" 
                  min="1"
                  placeholder="100"
                >
              </div>
            </div>
          </div>
        </div>

        <div class="questions-section">
          <div class="questions-header">
            <h3>Questions ({{ questions.length }})</h3>
            <button type="button" class="add-question-btn" @click="addQuestion">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                <path d="M19,13H13V19H11V13H5V11H11V5H13V11H19V13Z" />
              </svg>
              Add Question
            </button>
          </div>

          <div class="questions-list">
            <div v-for="(question, index) in questions" :key="index" class="question-item">
              <div class="question-header">
                <h4>Question {{ index + 1 }}</h4>
                <button 
                  type="button" 
                  class="remove-question-btn" 
                  @click="removeQuestion(index)"
                  v-if="questions.length > 1"
                  title="Remove Question"
                >
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M19,4H15.5L14.5,3H9.5L8.5,4H5V6H19M6,19A2,2 0 0,0 8,21H16A2,2 0 0,0 18,19V7H6V19Z" />
                  </svg>
                </button>
              </div>

              <div class="form-group">
                <label :for="'question-' + index">Question Text *</label>
                <textarea 
                  :id="'question-' + index" 
                  v-model="question.text" 
                  :placeholder="'Enter question ' + (index + 1) + '...'"
                  rows="3"
                  required
                ></textarea>
              </div>

              <div class="form-group">
                <label>Question Type</label>
                <select v-model="question.type" @change="updateQuestionType(question)">
                  <option value="multiple-choice">Multiple Choice</option>
                  <option value="true-false">True/False</option>
                  <option value="short-answer">Short Answer</option>
                </select>
              </div>

              <!-- Multiple Choice Options -->
              <div v-if="question.type === 'multiple-choice'" class="choices-section">
                <label>Answer Choices</label>
                <div class="choices-list">
                  <div v-for="(choice, choiceIndex) in question.choices" :key="choiceIndex" class="choice-item">
                    <input 
                      type="radio" 
                      :name="'correct-' + index" 
                      :value="choiceIndex" 
                      v-model="question.correctAnswer"
                      :id="'choice-' + index + '-' + choiceIndex"
                    >
                    <input 
                      type="text" 
                      v-model="choice.text" 
                      :placeholder="'Choice ' + (choiceIndex + 1)"
                      class="choice-input"
                      required
                    >
                    <button 
                      type="button" 
                      @click="removeChoice(question, choiceIndex)"
                      v-if="question.choices.length > 2"
                      class="remove-choice-btn"
                    >
                      ×
                    </button>
                  </div>
                </div>
                <button type="button" @click="addChoice(question)" class="add-choice-btn" v-if="question.choices.length < 6">
                  + Add Choice
                </button>
              </div>

              <!-- True/False Options -->
              <div v-else-if="question.type === 'true-false'" class="true-false-section">
                <label>Correct Answer</label>
                <div class="radio-group">
                  <label class="radio-option">
                    <input type="radio" :name="'answer-' + index" value="true" v-model="question.correctAnswer">
                    True
                  </label>
                  <label class="radio-option">
                    <input type="radio" :name="'answer-' + index" value="false" v-model="question.correctAnswer">
                    False
                  </label>
                </div>
              </div>

              <!-- Short Answer -->
              <div v-else-if="question.type === 'short-answer'" class="form-group">
                <label :for="'answer-' + index">Sample Answer/Keywords *</label>
                <input 
                  type="text" 
                  :id="'answer-' + index" 
                  v-model="question.correctAnswer" 
                  placeholder="Enter expected answer or keywords..."
                  required
                >
              </div>

              <div class="form-group">
                <label :for="'points-' + index">Points</label>
                <input 
                  type="number" 
                  :id="'points-' + index" 
                  v-model="question.points" 
                  min="1"
                  placeholder="5"
                  class="points-input"
                >
              </div>
            </div>
          </div>
        </div>
        
        <div class="form-actions">
          <button type="button" class="cancel-btn" @click="goBack">
            Cancel
          </button>
          <button type="submit" class="submit-quiz-btn" :disabled="isSubmitting">
            <svg v-if="isSubmitting" width="20" height="20" viewBox="0 0 24 24" fill="currentColor" class="spinner">
              <path d="M12,4V2A10,10 0 0,0 2,12H4A8,8 0 0,1 12,4Z" />
            </svg>
            {{ isSubmitting ? 'Creating Quiz...' : 'Create Quiz' }}
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, computed } from 'vue';
import { useRouter, useRoute } from 'vue-router';
import { supabase } from '../../supabase.js'; // Adjust path as needed

const router = useRouter();
const route = useRoute();

// Get data passed from MySubjects.vue
const subjectId = ref(route.params.subjectId);
const sectionId = ref(route.params.sectionId);
const subjectName = ref(route.query.subjectName || '');
const sectionName = ref(route.query.sectionName || '');
const gradeLevel = ref(route.query.gradeLevel || '');
const classCode = ref(route.query.classCode || '');
const sectionCode = ref(route.query.sectionCode || '');

// Quiz form data
const quizTitle = ref('');
const timeLimit = ref(60);
const totalPoints = ref(100);
const isSubmitting = ref(false);

const questions = ref([
  {
    text: '',
    type: 'multiple-choice',
    choices: [
      { text: '' },
      { text: '' }
    ],
    correctAnswer: 0,
    points: 5
  }
]);

// Computed total points from all questions
const calculatedTotalPoints = computed(() => {
  return questions.value.reduce((total, question) => total + (parseInt(question.points) || 0), 0);
});

const addQuestion = () => {
  questions.value.push({
    text: '',
    type: 'multiple-choice',
    choices: [
      { text: '' },
      { text: '' }
    ],
    correctAnswer: 0,
    points: 5
  });
};

const removeQuestion = (index) => {
  if (questions.value.length > 1) {
    questions.value.splice(index, 1);
  } else {
    alert('A quiz must have at least one question.');
  }
};

const updateQuestionType = (question) => {
  if (question.type === 'multiple-choice') {
    question.choices = [{ text: '' }, { text: '' }];
    question.correctAnswer = 0;
  } else if (question.type === 'true-false') {
    question.choices = [];
    question.correctAnswer = 'true';
  } else if (question.type === 'short-answer') {
    question.choices = [];
    question.correctAnswer = '';
  }
};

const addChoice = (question) => {
  if (question.choices.length < 6) {
    question.choices.push({ text: '' });
  }
};

const removeChoice = (question, choiceIndex) => {
  if (question.choices.length > 2) {
    question.choices.splice(choiceIndex, 1);
    // Adjust correct answer if needed
    if (question.correctAnswer >= question.choices.length) {
      question.correctAnswer = question.choices.length - 1;
    }
  }
};

const validateQuiz = () => {
  if (!quizTitle.value.trim()) {
    alert('Please enter a quiz title.');
    return false;
  }

  for (let i = 0; i < questions.value.length; i++) {
    const question = questions.value[i];
    
    if (!question.text.trim()) {
      alert(`Please enter text for question ${i + 1}.`);
      return false;
    }

    if (question.type === 'multiple-choice') {
      // Check if all choices have text
      for (let j = 0; j < question.choices.length; j++) {
        if (!question.choices[j].text.trim()) {
          alert(`Please enter text for all choices in question ${i + 1}.`);
          return false;
        }
      }
      
      // Check if a correct answer is selected
      if (question.correctAnswer === null || question.correctAnswer === undefined) {
        alert(`Please select the correct answer for question ${i + 1}.`);
        return false;
      }
    } else if (question.type === 'true-false') {
      if (!question.correctAnswer) {
        alert(`Please select the correct answer for question ${i + 1}.`);
        return false;
      }
    } else if (question.type === 'short-answer') {
      if (!question.correctAnswer.trim()) {
        alert(`Please enter the expected answer for question ${i + 1}.`);
        return false;
      }
    }
  }

  return true;
};

const submitQuiz = async () => {
  if (!validateQuiz()) {
    return;
  }

  isSubmitting.value = true;

  try {
    const { data: { user } } = await supabase.auth.getUser();
    if (!user) {
      throw new Error('Please login to continue');
    }

    // Prepare quiz data
    const quizData = {
      title: quizTitle.value.trim(),
      subject_id: subjectId.value,
      section_id: sectionId.value,
      teacher_id: user.id,
      time_limit: timeLimit.value || null,
      total_points: calculatedTotalPoints.value,
      questions: questions.value.map((question, index) => ({
        question_number: index + 1,
        question_text: question.text.trim(),
        question_type: question.type,
        choices: question.type === 'multiple-choice' ? question.choices.map(c => c.text.trim()) : null,
        correct_answer: question.correctAnswer,
        points: parseInt(question.points) || 5
      })),
      status: 'draft', // Can be 'draft', 'published', 'archived'
      created_at: new Date().toISOString()
    };

    console.log('Submitting quiz data:', quizData);

    // Insert quiz into Supabase (you'll need to create the quizzes table)
    const { data: insertedQuiz, error: quizError } = await supabase
      .from('quizzes')
      .insert([{
        title: quizData.title,
        subject_id: quizData.subject_id,
        section_id: quizData.section_id,
        teacher_id: quizData.teacher_id,
        time_limit: quizData.time_limit,
        total_points: quizData.total_points,
        status: quizData.status
      }])
      .select()
      .single();

    if (quizError) throw quizError;

    // Insert questions
    const questionsToInsert = quizData.questions.map(q => ({
      quiz_id: insertedQuiz.id,
      question_number: q.question_number,
      question_text: q.question_text,
      question_type: q.question_type,
      choices: q.choices,
      correct_answer: q.correct_answer,
      points: q.points
    }));

    const { error: questionsError } = await supabase
      .from('quiz_questions')
      .insert(questionsToInsert);

    if (questionsError) throw questionsError;

    alert(`Quiz "${quizData.title}" created successfully!`);
    
    // Navigate back to MySubjects
    router.push({ name: 'MySubjects' });

  } catch (error) {
    console.error('Error creating quiz:', error);
    alert(`Error creating quiz: ${error.message}`);
  } finally {
    isSubmitting.value = false;
  }
};

const goBack = () => {
  router.push({ name: 'MySubjects' });
};

onMounted(() => {
  // Update total points when component mounts
  totalPoints.value = calculatedTotalPoints.value;
  
  console.log('CreateQuiz loaded with:', {
    subjectId: subjectId.value,
    sectionId: sectionId.value,
    subjectName: subjectName.value,
    sectionName: sectionName.value,
    gradeLevel: gradeLevel.value,
    sectionCode: sectionCode.value
  });
});
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

.home-container {
  padding: 2rem;
  max-width: 1200px;
  margin: 0 auto;
  font-family: 'Inter', sans-serif;
  background: var(--bg-primary);
  min-height: 100vh;
}

/* Enhanced Header Design */
.section-header-card {
  position: relative;
  background: linear-gradient(135deg, var(--bg-primary) 0%, var(--bg-secondary) 100%);
  border-radius: 32px;
  padding: 3.5rem;
  margin-bottom: 2.5rem;
  min-height: 180px;
  box-shadow: 
    0 24px 48px var(--shadow-medium),
    0 12px 24px var(--shadow-light),
    inset 0 1px 0 rgba(255, 255, 255, 0.8);
  border: 2px solid var(--border-color);
  overflow: hidden;
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}

.section-header-card:hover {
  transform: translateY(-2px);
  box-shadow: 
    0 32px 64px var(--shadow-strong),
    0 16px 32px var(--shadow-medium),
    inset 0 1px 0 rgba(255, 255, 255, 0.9);
}

.header-bg-decoration {
  position: absolute;
  top: -50%;
  right: -20%;
  width: 120%;
  height: 200%;
  background: radial-gradient(ellipse at center, rgba(77, 187, 152, 0.08) 0%, transparent 70%);
  z-index: 1;
}

.floating-shapes {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 1;
  pointer-events: none;
}

.shape {
  position: absolute;
  border-radius: 50%;
  background: linear-gradient(135deg, rgba(77, 187, 152, 0.1) 0%, rgba(51, 128, 107, 0.05) 100%);
}

.shape-1 {
  width: 120px;
  height: 120px;
  top: -30px;
  right: 10%;
  animation: float 6s ease-in-out infinite;
}

.shape-2 {
  width: 80px;
  height: 80px;
  bottom: -20px;
  right: 25%;
  animation: float 8s ease-in-out infinite reverse;
}

.shape-3 {
  width: 60px;
  height: 60px;
  top: 50%;
  right: 5%;
  animation: float 7s ease-in-out infinite;
}

@keyframes float {
  0%, 100% { transform: translateY(0) rotate(0deg); }
  50% { transform: translateY(-20px) rotate(10deg); }
}

.section-header-content {
  position: relative;
  z-index: 2;
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
}

.section-header-left {
  display: flex;
  align-items: center;
  gap: 2.5rem;
}

.section-header-icon {
  width: 80px;
  height: 80px;
  background: linear-gradient(135deg, var(--accent-color) 0%, #A3D1C6 100%);
  border-radius: 24px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #fff;
  box-shadow: 
    0 12px 24px var(--shadow-light),
    inset 0 1px 0 rgba(255, 255, 255, 0.2);
  transition: all 0.3s ease;
}

.section-header-icon:hover {
  transform: scale(1.05);
}

.header-text {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.section-header-title {
  font-size: 2.5rem;
  font-weight: 800;
  color: var(--text-accent);
  letter-spacing: -0.02em;
  background: linear-gradient(135deg, var(--accent-color) 0%, #A3D1C6 100%);
  background-clip: text;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  margin-bottom: 0.25rem;
}

.section-header-subtitle {
  font-size: 1.25rem;
  font-weight: 600;
  color: var(--text-secondary);
  margin-bottom: 0.25rem;
}

.section-header-description {
  font-size: 1rem;
  color: var(--text-muted);
  font-weight: 400;
  opacity: 0.9;
}

.back-button {
  background: var(--action-btn-bg);
  border: 2px solid var(--border-color);
  border-radius: 20px;
  padding: 1rem 1.5rem;
  backdrop-filter: blur(10px);
  display: flex;
  align-items: center;
  gap: 0.5rem;
  color: var(--action-btn-color);
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  text-decoration: none;
}

.back-button:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 16px var(--shadow-light);
  background: var(--bg-accent-hover);
}

/* Content Cards */
.content-card {
  background: var(--card-background);
  border-radius: 28px;
  padding: 2.5rem;
  margin-bottom: 2rem;
  box-shadow: 
    0 20px 60px var(--shadow-light),
    0 8px 32px var(--shadow-light),
    0 0 0 1px rgba(255, 255, 255, 0.3);
  border: 1px solid var(--card-border-color);
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
  margin: 0;
  margin-bottom: 0.5rem;
}

.card-subtitle {
  color: var(--secondary-text-color);
  font-size: 1rem;
  margin: 0;
}

.back-button:hover {
  color: var(--primary-color-dark);
  transform: translateX(-5px);
}

.hero-header h1 {
  font-size: 2.5rem;
  font-weight: 800;
  color: var(--primary-color);
  margin: 0 0 1.5rem 0;
}

.section-info {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
}

.info-badge {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1.25rem;
  border-radius: 12px;
  font-size: 0.9rem;
}

.info-badge.subject {
  background: rgba(16, 185, 129, 0.1);
  border: 1px solid rgba(16, 185, 129, 0.2);
}

.info-badge.section {
  background: rgba(59, 130, 246, 0.1);
  border: 1px solid rgba(59, 130, 246, 0.2);
}

.info-badge.code {
  background: rgba(139, 92, 246, 0.1);
  border: 1px solid rgba(139, 92, 246, 0.2);
}

.info-badge .label {
  font-weight: 600;
  color: var(--secondary-text-color);
}

.info-badge .value {
  font-weight: 700;
  color: var(--primary-text-color);
}

.quiz-form {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.form-header h2 {
  color: var(--primary-color);
  margin-bottom: 1.5rem;
  font-size: 1.5rem;
  font-weight: 700;
}

.quiz-meta {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.form-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.5rem;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.form-group label {
  font-weight: 600;
  color: var(--primary-text-color);
}

.form-group input,
.form-group select,
.form-group textarea {
  padding: 0.75rem 1rem;
  border: 2px solid var(--border-color);
  border-radius: 12px;
  font-size: 1rem;
  transition: all 0.3s;
  font-family: inherit;
  background: var(--card-background);
  color: var(--primary-text-color);
}

.form-group input:focus,
.form-group select:focus,
.form-group textarea:focus {
  outline: none;
  border-color: var(--primary-color);
  box-shadow: 0 0 0 3px var(--primary-color-alpha);
}

.questions-section {
  margin-top: 2rem;
}

.questions-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
}

.questions-header h3 {
  color: var(--primary-color);
  font-size: 1.4rem;
  font-weight: 700;
  margin: 0;
}

.add-question-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  background: linear-gradient(135deg, var(--accent-color) 0%, var(--success-color) 100%);
  color: white;
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 12px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s;
}

.add-question-btn:hover {
  transform: translateY(-1px);
  box-shadow: 0 8px 20px var(--success-color-alpha);
}

.questions-list {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.question-item {
  background: var(--card-background);
  padding: 2rem;
  border-radius: 16px;
  border: 2px solid var(--border-color);
  position: relative;
  box-shadow: var(--shadow-light);
}

.question-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1.5rem;
}

.question-header h4 {
  color: var(--primary-color);
  margin: 0;
  font-size: 1.2rem;
  font-weight: 700;
}

.remove-question-btn {
  display: flex;
  align-items: center;
  gap: 0.25rem;
  background: var(--error-color);
  color: white;
  border: none;
  border-radius: 8px;
  padding: 0.5rem 0.75rem;
  font-size: 0.85rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s;
}

.remove-question-btn:hover {
  background: var(--error-color-dark);
}

.choices-section {
  margin-top: 1rem;
}

.choices-section label {
  display: block;
  margin-bottom: 1rem;
  font-weight: 600;
  color: var(--primary-text-color);
}

.choices-list {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
  margin-bottom: 1rem;
}

.choice-item {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.choice-item input[type="radio"] {
  width: 18px;
  height: 18px;
  accent-color: var(--primary-color);
}

.choice-input {
  flex: 1;
  padding: 0.6rem 1rem;
  border: 1px solid var(--border-color);
  border-radius: 8px;
  font-size: 0.95rem;
  background: var(--card-background);
  color: var(--primary-text-color);
}

.remove-choice-btn {
  background: var(--error-color);
  color: white;
  border: none;
  border-radius: 6px;
  width: 28px;
  height: 28px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  font-size: 1.2rem;
  font-weight: bold;
}

.add-choice-btn {
  background: var(--primary-color-light);
  color: var(--primary-color);
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 8px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s;
}

.add-choice-btn:hover {
  background: var(--primary-color-dark);
  color: white;
}

.true-false-section,
.radio-group {
  margin-top: 1rem;
}

.radio-group {
  display: flex;
  gap: 2rem;
}

.radio-option {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  cursor: pointer;
  font-weight: 500;
  color: var(--primary-text-color);
}

.radio-option input[type="radio"] {
  width: 18px;
  height: 18px;
  accent-color: var(--primary-color);
}

.points-input {
  max-width: 120px;
}

.form-actions {
  display: flex;
  gap: 1.5rem;
  justify-content: flex-end;
  margin-top: 2rem;
  padding-top: 2rem;
  border-top: 1px solid var(--border-color);
}

.cancel-btn {
  background: transparent;
  color: var(--secondary-text-color);
  border: 2px solid var(--border-color);
  padding: 1rem 2rem;
  border-radius: 16px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s;
}

.cancel-btn:hover {
  background: var(--hover-background);
  border-color: var(--secondary-text-color);
}

.submit-quiz-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  background: linear-gradient(135deg, var(--primary-color) 0%, var(--primary-color-light) 100%);
  color: white;
  border: none;
  padding: 1rem 2rem;
  border-radius: 16px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s;
  box-shadow: 0 8px 32px var(--primary-color-alpha);
}

.submit-quiz-btn:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 16px 48px var(--primary-color-alpha);
}

.submit-quiz-btn:disabled {
  opacity: 0.7;
  cursor: not-allowed;
  transform: none;
}

.spinner {
  animation: spin 1s linear infinite;
}

@keyframes spin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}

/* Responsive */
@media (max-width: 768px) {
  .page-container {
    padding: 1rem 3%;
  }

  .card-box {
    padding: 1.5rem;
  }

  .hero-header h1 {
    font-size: 2rem;
  }

  .section-info {
    flex-direction: column;
    gap: 0.75rem;
  }

  .form-row {
    grid-template-columns: 1fr;
  }

  .questions-header {
    flex-direction: column;
    align-items: stretch;
    gap: 1rem;
  }

  .question-item {
    padding: 1.5rem;
  }

  .form-actions {
    flex-direction: column;
  }

  .radio-group {
    flex-direction: column;
    gap: 1rem;
  }
}
</style>