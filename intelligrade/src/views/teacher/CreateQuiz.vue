<template>
  <div class="home-container" :class="{ 'dark-mode': isDarkMode }">
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
        
        <button @click="goBack" class="back-button" type="button">
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
        
        <!-- Fixed Form Actions with inline styles to ensure visibility -->
        <div class="form-actions" style="display: flex !important; justify-content: flex-end !important; gap: 1.5rem !important; margin-top: 2rem !important; padding-top: 2rem !important; border-top: 1px solid #e2e8f0 !important; width: 100% !important; position: relative !important; z-index: 100 !important; background: white !important;">
          <button 
            type="button" 
            class="cancel-btn" 
            @click="goBack"
            style="
              display: flex !important;
              align-items: center !important;
              background: transparent !important;
              color: #6b7280 !important;
              border: 2px solid #d1d5db !important;
              padding: 1rem 2rem !important;
              border-radius: 16px !important;
              font-weight: 600 !important;
              cursor: pointer !important;
              transition: all 0.3s ease !important;
              min-height: 48px !important;
              visibility: visible !important;
              opacity: 1 !important;
            "
          >
            Cancel
          </button>
          
          <button 
            type="submit" 
            class="submit-quiz-btn" 
            :disabled="isSubmitting"
            style="
              display: flex !important;
              align-items: center !important;
              gap: 0.5rem !important;
              background: linear-gradient(135deg, #059669 0%, #34d399 100%) !important;
              color: white !important;
              border: none !important;
              padding: 1rem 2rem !important;
              border-radius: 16px !important;
              font-size: 1rem !important;
              font-weight: 600 !important;
              cursor: pointer !important;
              transition: all 0.3s ease !important;
              box-shadow: 0 8px 32px rgba(5, 150, 105, 0.2) !important;
              min-height: 48px !important;
              min-width: 150px !important;
              position: relative !important;
              z-index: 101 !important;
              visibility: visible !important;
              opacity: 1 !important;
            "
          >
            <svg v-if="isSubmitting" width="20" height="20" viewBox="0 0 24 24" fill="currentColor" class="spinner" style="animation: spin 1s linear infinite;">
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
import { supabase } from '../../supabase'; // Adjust path as needed
import { useDarkMode } from '../../composables/useDarkMode';

const router = useRouter();
const route = useRoute();

// Dark mode setup
const { isDarkMode, initDarkMode } = useDarkMode();

// Interface definitions
interface Choice {
  text: string;
}

interface Question {
  text: string;
  type: 'multiple-choice' | 'true-false' | 'short-answer';
  choices: Choice[];
  correctAnswer: number | string;
  points: number;
}

// Get data passed from MySubjects.vue
const subjectId = ref(route.params.subjectId as string);
const sectionId = ref(route.params.sectionId as string);
const subjectName = ref((route.query.subjectName as string) || '');
const sectionName = ref((route.query.sectionName as string) || '');
const gradeLevel = ref((route.query.gradeLevel as string) || '');
const classCode = ref((route.query.classCode as string) || '');
const sectionCode = ref((route.query.sectionCode as string) || '');

// Quiz form data
const quizTitle = ref('');
const timeLimit = ref<number>(60);
const totalPoints = ref<number>(100);
const isSubmitting = ref(false);

const questions = ref<Question[]>([
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
  return questions.value.reduce((total, question) => total + (question.points || 0), 0);
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

const removeQuestion = (index: number) => {
  if (questions.value.length > 1) {
    questions.value.splice(index, 1);
  } else {
    alert('A quiz must have at least one question.');
  }
};

const updateQuestionType = (question: Question) => {
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

const addChoice = (question: Question) => {
  if (question.choices.length < 6) {
    question.choices.push({ text: '' });
  }
};

const removeChoice = (question: Question, choiceIndex: number) => {
  if (question.choices.length > 2) {
    question.choices.splice(choiceIndex, 1);
    // Adjust correct answer if needed
    if (typeof question.correctAnswer === 'number' && question.correctAnswer >= question.choices.length) {
      question.correctAnswer = question.choices.length - 1;
    }
  }
};

const validateQuiz = (): boolean => {
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
      if (!String(question.correctAnswer).trim()) {
        alert(`Please enter the expected answer for question ${i + 1}.`);
        return false;
      }
    }
  }

  return true;
};

// Diagnostic Functions
const testDatabaseTables = async () => {
  try {
    console.log('Testing database tables...');
    
    // Test quizzes table
    const { data: quizzesTest, error: quizzesError } = await supabase
      .from('quizzes')
      .select('count')
      .limit(1);
    
    if (quizzesError) {
      console.error('Quizzes table error:', quizzesError);
      alert(`Quiz tables missing: ${quizzesError.message}`);
      return false;
    }
    
    // Test quiz_questions table
    const { data: questionsTest, error: questionsError } = await supabase
      .from('quiz_questions')
      .select('count')
      .limit(1);
    
    if (questionsError) {
      console.error('Quiz_questions table error:', questionsError);
      alert(`Quiz_questions table missing: ${questionsError.message}`);
      return false;
    }
    
    alert('All quiz tables exist!');
    return true;
    
  } catch (error: any) {
    console.error('Database test failed:', error);
    alert(`Database test failed: ${error.message}`);
    return false;
  }
};

const testAuthentication = async () => {
  try {
    console.log('Testing authentication...');
    
    // Get current user
    const { data: authData, error: authError } = await supabase.auth.getUser();
    
    if (authError || !authData?.user) {
      alert('Not authenticated');
      return false;
    }
    
    console.log('User ID:', authData.user.id);
    
    // Test teacher lookup
    const { data: teacherData, error: teacherError } = await supabase
      .from('teachers')
      .select(`
        id,
        full_name,
        profile_id,
        profiles!inner(auth_user_id, role)
      `)
      .eq('profiles.auth_user_id', authData.user.id)
      .eq('profiles.role', 'teacher');
    
    if (teacherError) {
      console.error('Teacher lookup error:', teacherError);
      alert(`Teacher lookup failed: ${teacherError.message}`);
      return false;
    }
    
    if (!teacherData || teacherData.length === 0) {
      alert('No teacher profile found. You may need to be set up as a teacher first.');
      return false;
    }
    
    console.log('Teacher data:', teacherData);
    alert(`Authenticated as teacher: ${teacherData[0].full_name}`);
    return teacherData[0];
    
  } catch (error: any) {
    console.error('Auth test failed:', error);
    alert(`Auth test failed: ${error.message}`);
    return false;
  }
};

const testSectionAccess = async (teacherId: string) => {
  try {
    console.log('Testing section access...');
    
    // Check if teacher owns this section
    const { data: sectionData, error: sectionError } = await supabase
      .from('sections')
      .select(`
        id,
        name,
        section_code,
        subjects!inner(
          id,
          name,
          teacher_id
        )
      `)
      .eq('id', sectionId.value)
      .eq('subjects.teacher_id', teacherId);
    
    if (sectionError) {
      console.error('Section lookup error:', sectionError);
      alert(`Section lookup failed: ${sectionError.message}`);
      return false;
    }
    
    if (!sectionData || sectionData.length === 0) {
      alert(`No access to section. Section ID: ${sectionId.value}, Teacher ID: ${teacherId}`);
      return false;
    }
    
    console.log('Section data:', sectionData);
    alert(`Section access confirmed: ${sectionData[0].name}`);
    return sectionData[0];
    
  } catch (error: any) {
    console.error('Section test failed:', error);
    alert(`Section test failed: ${error.message}`);
    return false;
  }
};

const testQuizInsertion = async (teacherId: string, sectionData: any) => {
  try {
    console.log('Testing quiz insertion...');
    
    const testQuizData = {
      title: 'Test Quiz - ' + new Date().toISOString(),
      section_id: sectionId.value,
      subject_id: sectionData.subjects.id,
      teacher_id: teacherId,
      time_limit: 30,
      total_points: 10,
      status: 'draft'
    };
    
    console.log('Test quiz data:', testQuizData);
    
    const { data: insertedQuiz, error: quizError } = await supabase
      .from('quizzes')
      .insert([testQuizData])
      .select()
      .single();
    
    if (quizError) {
      console.error('Quiz insertion error:', quizError);
      alert(`Quiz insertion failed: ${quizError.message}`);
      return false;
    }
    
    console.log('Quiz inserted:', insertedQuiz);
    
    // Clean up test quiz
    await supabase.from('quizzes').delete().eq('id', insertedQuiz.id);
    
    alert('Quiz insertion test successful!');
    return true;
    
  } catch (error: any) {
    console.error('Quiz insertion test failed:', error);
    alert(`Quiz insertion test failed: ${error.message}`);
    return false;
  }
};

const runFullDiagnostic = async () => {
  console.log('=== RUNNING FULL DIAGNOSTIC ===');
  
  // Step 1: Test database tables
  const tablesOk = await testDatabaseTables();
  if (!tablesOk) return;
  
  // Step 2: Test authentication
  const teacherData = await testAuthentication();
  if (!teacherData) return;
  
  // Step 3: Test section access
  const sectionData = await testSectionAccess(teacherData.id);
  if (!sectionData) return;
  
  // Step 4: Test quiz insertion
  const insertionOk = await testQuizInsertion(teacherData.id, sectionData);
  
  if (insertionOk) {
    alert('All tests passed! Your quiz creation should work now.');
  }
};

// Main submit function
const submitQuiz = async () => {
  console.log('=== QUIZ SUBMISSION STARTED ===');
  
  if (!validateQuiz()) {
    console.log('Quiz validation failed');
    return;
  }

  isSubmitting.value = true;

  try {
    console.log('Step 1: Checking authentication...');
    
    // Get current user
    const { data: authData, error: authError } = await supabase.auth.getUser();
    
    if (authError || !authData?.user) {
      throw new Error('Please login to continue');
    }

    console.log('Step 2: Getting user profile...');
    
    // Get teacher profile using your new schema
    const { data: teacherData, error: teacherError } = await supabase
      .from('teachers')
      .select(`
        id,
        full_name,
        profile_id,
        profiles!inner(auth_user_id, role)
      `)
      .eq('profiles.auth_user_id', authData.user.id)
      .eq('profiles.role', 'teacher')
      .single();

    if (teacherError || !teacherData) {
      console.error('Teacher lookup error:', teacherError);
      throw new Error('Teacher profile not found. Please contact support.');
    }

    const teacherId = teacherData.id;
    console.log('Teacher authenticated:', teacherId);

    console.log('Step 3: Validating section access...');
    
    // Verify teacher owns this section
    const { data: sectionData, error: sectionError } = await supabase
      .from('sections')
      .select(`
        id,
        name,
        section_code,
        subjects!inner(
          id,
          name,
          teacher_id
        )
      `)
      .eq('id', sectionId.value)
      .eq('subjects.teacher_id', teacherId)
      .single();

    if (sectionError || !sectionData) {
      console.error('Section validation error:', sectionError);
      throw new Error('You do not have permission to create quizzes for this section.');
    }

    console.log('Section validated:', sectionData);

    console.log('Step 4: Preparing quiz data...');
    
    // Prepare quiz data for new schema
    const quizPayload = {
      title: quizTitle.value.trim(),
      section_id: sectionId.value,
      subject_id: sectionData.subjects.id,
      teacher_id: teacherId,
      time_limit: timeLimit.value || null,
      total_points: calculatedTotalPoints.value,
      status: 'draft'
    };

    console.log('Quiz payload:', quizPayload);

    console.log('Step 5: Inserting quiz...');
    
    // Insert quiz
    const { data: insertedQuiz, error: quizError } = await supabase
      .from('quizzes')
      .insert([quizPayload])
      .select()
      .single();

    if (quizError) {
      console.error('Quiz insertion error:', quizError);
      throw new Error(`Failed to create quiz: ${quizError.message}`);
    }

    console.log('Quiz inserted successfully:', insertedQuiz);

    console.log('Step 6: Preparing questions...');
    
    // Prepare questions data for new schema
    const questionsData = questions.value.map((question, index) => {
      let correctAnswerValue;
      let choicesValue = null;
      
      if (question.type === 'multiple-choice') {
        correctAnswerValue = question.correctAnswer.toString();
        choicesValue = question.choices.map(c => c.text.trim()).filter(text => text.length > 0);
      } else if (question.type === 'true-false') {
        correctAnswerValue = question.correctAnswer === 'true' ? 'true' : 'false';
      } else {
        correctAnswerValue = String(question.correctAnswer).trim();
      }

      return {
        quiz_id: insertedQuiz.id,
        question_number: index + 1,
        question_text: question.text.trim(),
        question_type: question.type,
        choices: choicesValue,
        correct_answer: correctAnswerValue,
        points: parseInt(question.points) || 5
      };
    });

    console.log('Questions data prepared:', questionsData);

    console.log('Step 7: Inserting questions...');
    
    // Insert questions
    const { error: questionsError } = await supabase
      .from('quiz_questions')
      .insert(questionsData);

    if (questionsError) {
      console.error('Questions insertion error:', questionsError);
      
      // Cleanup: delete the quiz if questions failed
      await supabase.from('quizzes').delete().eq('id', insertedQuiz.id);
      
      throw new Error(`Failed to create quiz questions: ${questionsError.message}`);
    }

    console.log('Questions inserted successfully');
    console.log('=== QUIZ CREATION COMPLETED ===');

    alert(`Quiz "${quizPayload.title}" created successfully!`);
    
    // Navigate back
    console.log('Navigating back to MySubjects...');
    await router.push({ name: 'MySubjects' });
    
  } catch (error: any) {
    console.error('=== QUIZ CREATION FAILED ===');
    console.error('Error details:', error);
    
    let errorMessage = 'Failed to create quiz. ';
    
    if (error.message.includes('Teacher profile not found')) {
      errorMessage += 'Your account is not properly set up as a teacher. Please contact support.';
    } else if (error.message.includes('permission')) {
      errorMessage += 'You do not have permission to create quizzes for this section.';
    } else if (error.message.includes('auth')) {
      errorMessage += 'Please log in again.';
    } else if (error.message.includes('network') || error.message.includes('fetch')) {
      errorMessage += 'Please check your internet connection.';
    } else {
      errorMessage += error.message || 'Unknown error occurred.';
    }
    
    alert(errorMessage);
    
  } finally {
    isSubmitting.value = false;
    console.log('Quiz submission process completed');
  }
};

const goBack = () => {
  router.push({ name: 'MySubjects' });
};

onMounted(() => {
  // Initialize dark mode
  initDarkMode();
  
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

/* CSS Variables for better theme support - NEW */
:root {
  --bg-primary: #f8fafc;
  --bg-secondary: #f1f5f9;
  --card-background: #ffffff;
  --card-border-color: #e2e8f0;
  --border-color: #d1d5db;
  --text-accent: #1e293b;
  --text-secondary: #475569;
  --text-muted: #64748b;
  --primary-text-color: #1f2937;
  --secondary-text-color: #6b7280;
  --accent-color: #10b981;
  --primary-color: #059669;
  --primary-color-light: #34d399;
  --primary-color-dark: #047857;
  --primary-color-alpha: rgba(5, 150, 105, 0.2);
  --success-color: #10b981;
  --success-color-alpha: rgba(16, 185, 129, 0.2);
  --error-color: #ef4444;
  --error-color-dark: #dc2626;
  --shadow-light: rgba(0, 0, 0, 0.05);
  --shadow-medium: rgba(0, 0, 0, 0.1);
  --shadow-strong: rgba(0, 0, 0, 0.15);
  --action-btn-bg: rgba(255, 255, 255, 0.8);
  --action-btn-color: #374151;
  --bg-accent-hover: rgba(255, 255, 255, 0.9);
  --hover-background: #f9fafb;
}

/* Fixed back button z-index and positioning - NEW */
.back-button {
  z-index: 10;
  position: relative;
}

/* Fixed main wrapper width - NEW */
.main-wrapper {
  width: 100%;
  max-width: 100%;
}

/* Fixed content card width - NEW */
.content-card {
  width: 100%;
}

/* Fixed form content width - NEW */
.form-content {
  width: 100%;
}

/* Additional incomplete styles from original that needed completion */
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

/* Dark Mode Styles */
.home-container.dark-mode {
  background: var(--bg-primary);
  color: var(--primary-text-color);
}

.dark-mode .section-header-card {
  background: var(--bg-secondary);
  border: 1px solid var(--border-color);
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
}

.dark-mode .header-bg-decoration {
  background: linear-gradient(135deg, var(--accent-color) 0%, rgba(95, 179, 160, 0.3) 100%);
}

.dark-mode .section-header-title {
  color: var(--primary-text-color);
}

.dark-mode .section-header-subtitle {
  color: var(--accent-color);
}

.dark-mode .section-header-description {
  color: var(--secondary-text-color);
}

.dark-mode .back-button {
  background: var(--bg-card);
  border: 2px solid var(--border-color);
  color: var(--secondary-text-color);
}

.dark-mode .back-button:hover {
  border-color: var(--accent-color);
  color: var(--accent-color);
}

.dark-mode .content-card {
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.3);
}

.dark-mode .card-header h3 {
  color: var(--primary-text-color);
}

.dark-mode .card-subtitle {
  color: var(--secondary-text-color);
}

.dark-mode .form-group label {
  color: var(--primary-text-color);
}

.dark-mode .form-input {
  background: var(--input-bg);
  border: 2px solid var(--input-border);
  color: var(--primary-text-color);
}

.dark-mode .form-input:focus {
  border-color: var(--accent-color);
  box-shadow: 0 0 0 3px rgba(95, 179, 160, 0.2);
}

.dark-mode .form-textarea {
  background: var(--input-bg);
  border: 2px solid var(--input-border);
  color: var(--primary-text-color);
}

.dark-mode .form-textarea:focus {
  border-color: var(--accent-color);
  box-shadow: 0 0 0 3px rgba(95, 179, 160, 0.2);
}

.dark-mode .form-select {
  background: var(--input-bg);
  border: 2px solid var(--input-border);
  color: var(--primary-text-color);
}

.dark-mode .form-select:focus {
  border-color: var(--accent-color);
}

.dark-mode .quiz-settings .settings-grid .setting-card {
  background: var(--bg-secondary);
  border: 1px solid var(--border-color);
}

.dark-mode .setting-card h4 {
  color: var(--primary-text-color);
}

.dark-mode .setting-description {
  color: var(--secondary-text-color);
}

.dark-mode .questions-section h3 {
  color: var(--primary-text-color);
}

.dark-mode .question-card {
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2);
}

.dark-mode .question-header {
  background: var(--bg-accent);
  border-bottom: 1px solid var(--border-color);
}

.dark-mode .question-number {
  color: var(--accent-color);
}

.dark-mode .question-type-badge {
  background: var(--accent-color);
  color: white;
}

.dark-mode .delete-question-btn {
  background: var(--error-bg);
  border: 1px solid rgba(217, 83, 79, 0.4);
  color: var(--error-color);
}

.dark-mode .delete-question-btn:hover {
  background: rgba(217, 83, 79, 0.2);
}

.dark-mode .question-content .form-group label {
  color: var(--primary-text-color);
}

.dark-mode .question-text-input {
  background: var(--input-bg);
  border: 2px solid var(--input-border);
  color: var(--primary-text-color);
}

.dark-mode .question-text-input:focus {
  border-color: var(--accent-color);
}

.dark-mode .type-selector select {
  background: var(--input-bg);
  border: 2px solid var(--input-border);
  color: var(--primary-text-color);
}

.dark-mode .choices-container h4 {
  color: var(--primary-text-color);
}

.dark-mode .choice-item {
  background: var(--bg-secondary);
  border: 1px solid var(--border-color);
}

.dark-mode .correct-indicator {
  background: var(--success-bg);
  border: 1px solid rgba(92, 184, 92, 0.4);
}

.dark-mode .correct-indicator input[type="radio"]:checked::after {
  background: var(--success-color);
}

.dark-mode .choice-input {
  background: var(--input-bg);
  border: 1px solid var(--input-border);
  color: var(--primary-text-color);
}

.dark-mode .choice-input:focus {
  border-color: var(--accent-color);
}

.dark-mode .remove-choice-btn {
  background: var(--error-bg);
  border: 1px solid rgba(217, 83, 79, 0.4);
  color: var(--error-color);
}

.dark-mode .add-choice-btn {
  background: var(--bg-secondary);
  border: 2px solid var(--border-color);
  color: var(--secondary-text-color);
}

.dark-mode .add-choice-btn:hover {
  border-color: var(--accent-color);
  color: var(--accent-color);
}

.dark-mode .true-false-container .tf-option {
  background: var(--bg-secondary);
  border: 2px solid var(--border-color);
  color: var(--secondary-text-color);
}

.dark-mode .true-false-container .tf-option.selected {
  background: var(--accent-color);
  border-color: var(--accent-color);
  color: white;
}

.dark-mode .short-answer-container .answer-input {
  background: var(--input-bg);
  border: 2px solid var(--input-border);
  color: var(--primary-text-color);
}

.dark-mode .short-answer-container .answer-input:focus {
  border-color: var(--accent-color);
}

.dark-mode .question-points .points-input {
  background: var(--input-bg);
  border: 2px solid var(--input-border);
  color: var(--primary-text-color);
}

.dark-mode .question-points .points-input:focus {
  border-color: var(--accent-color);
}

.dark-mode .add-question-btn {
  background: var(--bg-secondary);
  border: 2px solid var(--border-color);
  color: var(--secondary-text-color);
}

.dark-mode .add-question-btn:hover {
  border-color: var(--accent-color);
  color: var(--accent-color);
}

.dark-mode .quiz-summary {
  background: var(--bg-card);
  border: 1px solid var(--border-color);
}

.dark-mode .quiz-summary h3 {
  color: var(--primary-text-color);
}

.dark-mode .summary-item {
  border-bottom: 1px solid var(--border-color);
}

.dark-mode .summary-item:last-child {
  border-bottom: none;
}

.dark-mode .summary-label {
  color: var(--secondary-text-color);
}

.dark-mode .summary-value {
  color: var(--accent-color);
}

.dark-mode .action-buttons .btn {
  background: var(--bg-secondary);
  border: 2px solid var(--border-color);
  color: var(--secondary-text-color);
}

.dark-mode .action-buttons .btn:hover {
  border-color: var(--accent-color);
  color: var(--accent-color);
}

.dark-mode .action-buttons .btn.primary {
  background: var(--accent-color);
  border-color: var(--accent-color);
  color: white;
}

.dark-mode .action-buttons .btn.primary:hover {
  background: var(--accent-hover);
}

.dark-mode .action-buttons .btn.secondary {
  background: var(--bg-card);
  border: 2px solid var(--border-color);
}

.dark-mode .action-buttons .btn:disabled {
  background: var(--bg-accent);
  border-color: var(--border-color);
  color: var(--secondary-text-color);
  opacity: 0.5;
}

.dark-mode .loading-spinner {
  border: 4px solid rgba(95, 179, 160, 0.2);
  border-left: 4px solid var(--accent-color);
}
</style>