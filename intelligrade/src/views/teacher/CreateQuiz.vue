<template>
  <div class="page-container">
    <div class="main-wrapper">
      <div class="hero-header card-box">
        <div class="header-content">
          <button @click="goBack" class="back-button">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
              <path d="M10 19l-7-7 7-7m-7 7h18"></path>
            </svg>
            Back to My Subjects
          </button>
          
          <h1>Create New Quiz</h1>
          
          <div class="section-info">
            <div class="info-badge subject">
              <span class="label">Subject:</span>
              <span class="value">{{ subjectName }} (Grade {{ gradeLevel }})</span>
            </div>
            <div class="info-badge section">
              <span class="label">Section:</span>
              <span class="value">{{ sectionName }}</span>
            </div>
            <div class="info-badge code">
              <span class="label">Section Code:</span>
              <span class="value">{{ sectionCode }}</span>
            </div>
          </div>
        </div>
      </div>

      <form @submit.prevent="submitQuiz" class="quiz-form card-box">
        <div class="form-header">
          <h2>Quiz Details</h2>
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
                <select v-model="question.type" @change="updateQuestionType(question, index)">
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

<script setup>
import { ref, onMounted, computed } from 'vue';
import { useRouter, useRoute } from 'vue-router';
import { supabase } from '../../supabase'; // Adjust path as needed

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

const updateQuestionType = (question, index) => {
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

.page-container {
  padding: 2rem 5%;
  font-family: 'Inter', sans-serif;
  min-height: 100vh;
  background: linear-gradient(135deg, #f0f9f6 0%, #e8f5f0 100%);
}

.main-wrapper {
  max-width: 1200px;
  margin: 0 auto;
}

.card-box {
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(20px);
  border: 1px solid rgba(61, 141, 122, 0.1);
  border-radius: 24px;
  padding: 2.5rem;
  box-shadow: 
    0 8px 32px rgba(61, 141, 122, 0.1),
    0 0 0 1px rgba(255, 255, 255, 0.2);
}

.hero-header {
  margin-bottom: 2rem;
}

.back-button {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  background: none;
  border: none;
  color: #3D8D7A;
  font-weight: 600;
  font-size: 1rem;
  cursor: pointer;
  transition: all 0.3s;
  margin-bottom: 1.5rem;
}

.back-button:hover {
  color: #2e6b5c;
  transform: translateX(-5px);
}

.hero-header h1 {
  font-size: 2.5rem;
  font-weight: 800;
  color: #3D8D7A;
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
  color: #666;
}

.info-badge .value {
  font-weight: 700;
  color: #333;
}

.quiz-form {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.form-header h2 {
  color: #3D8D7A;
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
  color: #444;
}

.form-group input,
.form-group select,
.form-group textarea {
  padding: 0.75rem 1rem;
  border: 2px solid rgba(61, 141, 122, 0.1);
  border-radius: 12px;
  font-size: 1rem;
  transition: all 0.3s;
  font-family: inherit;
}

.form-group input:focus,
.form-group select:focus,
.form-group textarea:focus {
  outline: none;
  border-color: #3D8D7A;
  box-shadow: 0 0 0 3px rgba(61, 141, 122, 0.1);
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
  color: #3D8D7A;
  font-size: 1.4rem;
  font-weight: 700;
  margin: 0;
}

.add-question-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  background: linear-gradient(135deg, #10b981 0%, #34d399 100%);
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
  box-shadow: 0 8px 20px rgba(16, 185, 129, 0.3);
}

.questions-list {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.question-item {
  background: #f8fff6;
  padding: 2rem;
  border-radius: 16px;
  border: 2px solid rgba(61, 141, 122, 0.1);
  position: relative;
}

.question-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1.5rem;
}

.question-header h4 {
  color: #3D8D7A;
  margin: 0;
  font-size: 1.2rem;
  font-weight: 700;
}

.remove-question-btn {
  display: flex;
  align-items: center;
  gap: 0.25rem;
  background: #ef4444;
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
  background: #dc2626;
}

.choices-section {
  margin-top: 1rem;
}

.choices-section label {
  display: block;
  margin-bottom: 1rem;
  font-weight: 600;
  color: #444;
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
  accent-color: #3D8D7A;
}

.choice-input {
  flex: 1;
  padding: 0.6rem 1rem;
  border: 1px solid #ddd;
  border-radius: 8px;
  font-size: 0.95rem;
}

.remove-choice-btn {
  background: #ef4444;
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
  background: #A3D1C6;
  color: #3D8D7A;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 8px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s;
}

.add-choice-btn:hover {
  background: #8ec3b2;
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
}

.radio-option input[type="radio"] {
  width: 18px;
  height: 18px;
  accent-color: #3D8D7A;
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
  border-top: 1px solid rgba(61, 141, 122, 0.1);
}

.cancel-btn {
  background: transparent;
  color: #666;
  border: 2px solid #ddd;
  padding: 1rem 2rem;
  border-radius: 16px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s;
}

.cancel-btn:hover {
  background: #f5f5f5;
  border-color: #999;
}

.submit-quiz-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  background: linear-gradient(135deg, #3D8D7A 0%, #A3D1C6 100%);
  color: white;
  border: none;
  padding: 1rem 2rem;
  border-radius: 16px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s;
  box-shadow: 0 8px 32px rgba(61, 141, 122, 0.2);
}

.submit-quiz-btn:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 16px 48px rgba(61, 141, 122, 0.3);
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