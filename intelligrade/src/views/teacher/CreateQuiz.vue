<template>
  <div class="subjects-page" :class="{ 'dark-mode': isDarkMode }">
    <!-- Enhanced Header Section -->
    <div class="section-header-card">
      <div class="header-bg-decoration"></div>
      <div class="floating-shapes">
        <div class="shape shape-1"></div>
        <div class="shape shape-2"></div>
        <div class="shape shape-3"></div>
      </div>
      
      <div class="section-header-content">
        <div class="section-header-left">
          <div class="section-header-icon">
            <svg width="36" height="36" viewBox="0 0 24 24" fill="currentColor">
              <path d="M14,2H6A2,2 0 0,0 4,4V20A2,2 0 0,0 6,22H18A2,2 0 0,0 20,20V8L14,2M18,20H6V4H13V9H18V20Z" />
            </svg>
          </div>
          
          <div class="header-text">
            <div class="section-header-title">Create New Quiz</div>
            <div class="section-header-subtitle">{{ subjectName }} (Grade {{ gradeLevel }})</div>
            <div class="section-header-description">{{ sectionName }} - {{ sectionCode }}</div>
          </div>
        </div>
        
        <div class="header-actions">
          <button @click="previewQuiz" class="export-btn" :disabled="questions.length === 0 || !quizTitle.trim()">
            <svg v-if="isPreviewing" width="20" height="20" viewBox="0 0 24 24" fill="currentColor" class="spinner">
              <path d="M12,4V2A10,10 0 0,0 2,12H4A8,8 0 0,1 12,4Z" />
            </svg>
            <svg v-else width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M12,9A3,3 0 0,0 9,12A3,3 0 0,0 12,15A3,3 0 0,0 15,12A3,3 0 0,0 12,9M12,17A5,5 0 0,1 7,12A5,5 0 0,1 12,7A5,5 0 0,1 17,12A5,5 0 0,1 12,17M12,4.5C7,4.5 2.73,7.61 1,12C2.73,16.39 7,19.5 12,19.5C17,19.5 21.27,16.39 23,12C21.27,7.61 17,4.5 12,4.5Z" />
            </svg>
            {{ isPreviewing ? 'Previewing...' : 'Preview Quiz' }}
          </button>
          <button @click="goBack" class="back-button">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M20,11V13H8L13.5,18.5L12.08,19.92L4.16,12L12.08,4.08L13.5,5.5L8,11H20Z" />
            </svg>
            Back to Subjects
          </button>
        </div>
      </div>
    </div>

    <div class="main-wrapper">
      <form @submit.prevent="submitQuiz" class="content-card enhanced-card">
        <div class="card-floating-shapes">
          <div class="card-shape shape-1"></div>
          <div class="card-shape shape-2"></div>
        </div>
        <div class="card-header">
          <div class="card-header-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
              <path d="M19,3H5C3.9,3 3,3.9 3,5V19C3,20.1 3.9,21 5,21H19C20.1,21 21,20.1 21,19V5C21,3.9 20.1,3 19,3M9,17H7V10H9V17M13,17H11V7H13V17M17,17H15V13H17V17Z" />
            </svg>
          </div>
          <div class="card-header-content">
            <h3>Quiz Details</h3>
            <p class="card-subtitle">Set up your assessment parameters and add questions</p>
          </div>
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

              <div class="form-group">
                <label for="attempts-allowed">Attempts Allowed</label>
                <input 
                  type="number" 
                  id="attempts-allowed" 
                  v-model="attemptsAllowed" 
                  min="1" 
                  max="10"
                  placeholder="1"
                >
              </div>
            </div>

            <div class="form-row">
              <div class="form-group">
                <label for="start-date">Start Date</label>
                <input 
                  type="date" 
                  id="start-date" 
                  v-model="startDate"
                >
              </div>
              
              <div class="form-group">
                <label for="start-time">Start Time</label>
                <input 
                  type="time" 
                  id="start-time" 
                  v-model="startTime"
                >
              </div>

              <div class="form-group">
                <label for="end-date">End Date</label>
                <input 
                  type="date" 
                  id="end-date" 
                  v-model="endDate"
                >
              </div>

              <div class="form-group">
                <label for="end-time">End Time</label>
                <input 
                  type="time" 
                  id="end-time" 
                  v-model="endTime"
                >
              </div>
            </div>

            <div class="quiz-options">
              <div class="form-group checkbox-group">
                <label>
                  <input 
                    type="checkbox" 
                    v-model="shuffleQuestions"
                  >
                  Shuffle Questions Order
                </label>
              </div>
              
              <div class="form-group checkbox-group">
                <label>
                  <input 
                    type="checkbox" 
                    v-model="shuffleChoices"
                  >
                  Shuffle Answer Choices
                </label>
              </div>
            </div>
          </div>
        </div>

        <div class="questions-section enhanced-questions">
          <div class="questions-header">
            <div class="questions-header-content">
              <div class="questions-header-icon">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M12,3C13.73,3 15.13,4.39 15.13,6.13C15.13,7.86 13.73,9.26 12,9.26C10.27,9.26 8.87,7.86 8.87,6.13C8.87,4.39 10.27,3 12,3M7,9H17V10C17,11.19 16.19,12 15,12H13.5V13.5C13.5,14.33 12.83,15 12,15C11.17,15 10.5,14.33 10.5,13.5V12H9C7.81,12 7,11.19 7,10V9M12,20A8,8 0 0,1 4,12A8,8 0 0,1 12,4A8,8 0 0,1 20,12A8,8 0 0,1 12,20Z" />
                </svg>
              </div>
              <div class="questions-header-text">
                <h3>Questions ({{ questions.length }})</h3>
                <p>Build your assessment with various question types</p>
              </div>
            </div>
            <button type="button" class="add-question-btn enhanced-btn" @click="addQuestion">
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
                  <option value="fill-in-blanks">Fill in the Blanks</option>
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

              <!-- Fill in the Blanks -->
              <div v-else-if="question.type === 'fill-in-blanks'" class="fill-blanks-section">
                <label>Question Text with Blanks</label>
                <div class="blanks-help">
                  <p>Use <code>____</code> (four underscores) to create blanks in your question.</p>
                  <p>Example: "The capital of France is ____."</p>
                </div>
                <textarea 
                  v-model="question.text" 
                  placeholder="Enter your question with ____ for blanks..."
                  rows="3"
                  @input="extractBlanks(question)"
                  required
                ></textarea>
                
                <div v-if="question.blanks && question.blanks.length > 0" class="blanks-answers">
                  <label>Correct Answers for Blanks</label>
                  <div v-for="(blank, blankIndex) in question.blanks" :key="blankIndex" class="blank-answer">
                    <span class="blank-label">Blank {{ blankIndex + 1 }}:</span>
                    <input 
                      type="text" 
                      v-model="question.blanks[blankIndex]" 
                      :placeholder="'Answer for blank ' + (blankIndex + 1)"
                      required
                    >
                  </div>
                </div>
              </div>

              <!-- Short Answer (legacy support) -->
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
        
        <!-- Form Actions -->
        <div class="form-actions">
          <button 
            type="button" 
            class="cancel-btn" 
            @click="goBack"
          >
            Cancel
          </button>
          
          <button 
            type="submit" 
            class="submit-quiz-btn" 
            :disabled="isSubmitting"
          >
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
  type: 'multiple-choice' | 'true-false' | 'fill-in-blanks' | 'short-answer';
  choices: Choice[];
  correctAnswer: number | string | string[];
  points: number;
  blanks?: string[]; // For fill-in-blanks questions
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
const attemptsAllowed = ref<number>(1);
const shuffleQuestions = ref(false);
const shuffleChoices = ref(false);
const startDate = ref('');
const endDate = ref('');
const startTime = ref('');
const endTime = ref('');
const isSubmitting = ref(false);
const isPreviewing = ref(false);

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
  } else if (question.type === 'fill-in-blanks') {
    question.choices = [];
    question.correctAnswer = [];
    question.blanks = [];
  } else if (question.type === 'short-answer') {
    question.choices = [];
    question.correctAnswer = '';
  }
};

const extractBlanks = (question: Question) => {
  if (question.type === 'fill-in-blanks') {
    // Count the number of ____ in the question text
    const blankCount = (question.text.match(/____/g) || []).length;
    
    // Initialize blanks array to match the number of blanks found
    question.blanks = Array(blankCount).fill('').map((_, index) => 
      question.blanks?.[index] || ''
    );
    
    // Update correct answer to be an array of blank answers
    question.correctAnswer = question.blanks;
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
    } else if (question.type === 'fill-in-blanks') {
      if (!question.blanks || question.blanks.length === 0) {
        alert(`Please add blanks to question ${i + 1} using ____ (four underscores).`);
        return false;
      }
      
      // Check if all blanks have answers
      for (let j = 0; j < question.blanks.length; j++) {
        if (!question.blanks[j].trim()) {
          alert(`Please provide an answer for blank ${j + 1} in question ${i + 1}.`);
          return false;
        }
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
    
    // Prepare start and end dates
    let startDateTime = null;
    let endDateTime = null;
    
    if (startDate.value && startTime.value) {
      startDateTime = new Date(`${startDate.value}T${startTime.value}`).toISOString();
    }
    
    if (endDate.value && endTime.value) {
      endDateTime = new Date(`${endDate.value}T${endTime.value}`).toISOString();
    }
    
    // Prepare quiz data for new schema
    const quizPayload = {
      title: quizTitle.value.trim(),
      section_id: sectionId.value,
      subject_id: sectionData.subjects.id,
      teacher_id: teacherId,
      time_limit: timeLimit.value || null,
      total_points: calculatedTotalPoints.value,
      attempts_allowed: attemptsAllowed.value || 1,
      shuffle_questions: shuffleQuestions.value,
      shuffle_choices: shuffleChoices.value,
      start_date: startDateTime,
      end_date: endDateTime,
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
      } else if (question.type === 'fill-in-blanks') {
        correctAnswerValue = JSON.stringify(question.blanks);
        choicesValue = null;
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
        points: parseInt(String(question.points)) || 5
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

const previewQuiz = async () => {
  isPreviewing.value = true;
  try {
    // Simulate a preview generation delay
    await new Promise(resolve => setTimeout(resolve, 1500));
    
    // Create a preview data object
    const previewData = {
      title: quizTitle.value,
      timeLimit: timeLimit.value,
      totalPoints: calculatedTotalPoints.value,
      questionCount: questions.value.length,
      questions: questions.value.filter(q => q.text.trim() !== '')
    };
    
    console.log('Quiz Preview:', previewData);
    
    // Here you could open a modal or navigate to a preview page
    alert(`Quiz Preview:\n\nTitle: ${previewData.title}\nQuestions: ${previewData.questionCount}\nTotal Points: ${previewData.totalPoints}\nTime Limit: ${previewData.timeLimit} minutes`);
    
  } catch (error) {
    console.error('Preview error:', error);
    alert('Error generating preview. Please try again.');
  } finally {
    isPreviewing.value = false;
  }
};

const goBack = async () => {
  try {
    await router.push({ name: 'MySubjects' });
  } catch (error) {
    console.error('Navigation error:', error);
  }
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

:root {
  --primary-color: #10b981;
  --primary-color-light: #34d399;
  --primary-color-dark: #059669;
  --primary-color-alpha: rgba(16, 185, 129, 0.2);
  --accent-color: #10b981;
  --success-color: #22c55e;
  --warning-color: #f59e0b;
  --error-color: #ef4444;
  --bg-primary: #f8fafc;
  --bg-secondary: #f1f5f9;
  --card-background: rgba(255, 255, 255, 0.95);
  --card-border-color: rgba(16, 185, 129, 0.1);
  --border-color: #e2e8f0;
  --primary-text-color: #1e293b;
  --secondary-text-color: #64748b;
  --shadow-light: rgba(0, 0, 0, 0.04);
  --shadow-medium: rgba(0, 0, 0, 0.1);
  --shadow-strong: rgba(0, 0, 0, 0.15);
}

/* Dark mode variables */
.dark-mode {
  --bg-primary: #0f172a;
  --bg-secondary: #1e293b;
  --card-background: rgba(30, 41, 59, 0.95);
  --card-border-color: rgba(16, 185, 129, 0.2);
  --border-color: #334155;
  --primary-text-color: #f1f5f9;
  --secondary-text-color: #94a3b8;
  --shadow-light: rgba(0, 0, 0, 0.2);
  --shadow-medium: rgba(0, 0, 0, 0.3);
  --shadow-strong: rgba(0, 0, 0, 0.4);
}

/* Enhanced Header Design */
.section-header-card {
  margin-bottom: 2rem;
  position: relative;
  overflow: hidden;
  background: rgba(248, 250, 252, 0.9);
  backdrop-filter: blur(20px);
  border-radius: 32px;
  padding: 3.5rem;
  border: 1px solid rgba(255, 255, 255, 0.8);
  min-height: 180px;
  box-shadow: 
    0 20px 40px rgba(0, 0, 0, 0.06),
    0 10px 20px rgba(0, 0, 0, 0.04),
    inset 0 1px 0 rgba(255, 255, 255, 0.8);
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.section-header-card:hover {
  transform: translateY(-2px);
  box-shadow: 
    0 32px 64px rgba(0, 0, 0, 0.12),
    0 16px 32px rgba(0, 0, 0, 0.1),
    inset 0 1px 0 rgba(255, 255, 255, 0.9);
}

.header-bg-decoration {
  position: absolute;
  top: -50%;
  right: -20%;
  width: 120%;
  height: 200%;
  background: radial-gradient(ellipse at center, rgba(16, 185, 129, 0.08) 0%, transparent 70%);
  z-index: 1;
}

.floating-shapes {
  position: absolute;
  top: 0;
  right: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
  z-index: 1;
}

.shape {
  position: absolute;
  border-radius: 50%;
  background: linear-gradient(135deg, rgba(16, 185, 129, 0.1) 0%, rgba(79, 70, 229, 0.05) 100%);
}

.shape-1 {
  width: 100px;
  height: 100px;
  top: -20px;
  right: 15%;
  animation: float 6s ease-in-out infinite;
}

.shape-2 {
  width: 60px;
  height: 60px;
  bottom: -10px;
  right: 25%;
  animation: float 8s ease-in-out infinite reverse;
}

.shape-3 {
  width: 80px;
  height: 80px;
  top: 50%;
  right: 5%;
  animation: float 7s ease-in-out infinite;
}

@keyframes float {
  0%, 100% { transform: translateY(0) rotate(0deg); }
  50% { transform: translateY(-15px) rotate(10deg); }
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
  gap: 2rem;
}

.section-header-icon {
  width: 80px;
  height: 80px;
  background: linear-gradient(135deg, #10b981 0%, #059669 100%);
  border-radius: 24px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #fff;
  box-shadow: 0 8px 24px rgba(16, 185, 129, 0.3);
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.section-header-icon:hover {
  transform: translateY(-2px);
}

.header-text {
  display: flex;
  flex-direction: column;
  gap: 0.3rem;
}

.section-header-title {
  font-size: 2rem;
  font-weight: 800;
  color: #10b981;
  margin-bottom: 0.25rem;
  letter-spacing: -0.025em;
}

.section-header-subtitle {
  font-size: 1.1rem;
  font-weight: 600;
  color: #64748b;
}

.section-header-description {
  font-size: 0.9rem;
  color: #94a3b8;
}

.header-actions {
  display: flex;
  gap: 1rem;
  align-items: center;
}

.back-button {
  background: rgba(255, 255, 255, 0.8);
  border: 1px solid rgba(203, 213, 225, 0.5);
  border-radius: 16px;
  padding: 0.875rem 1.5rem;
  backdrop-filter: blur(10px);
  display: flex;
  align-items: center;
  gap: 0.5rem;
  color: #64748b;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  text-decoration: none;
}

.back-button:hover {
  background: rgba(255, 255, 255, 0.95);
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1);
}

/* Create Quiz Button */
.create-quiz-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  background: linear-gradient(135deg, #10b981 0%, #059669 100%);
  color: white;
  border: none;
  padding: 0.875rem 1.5rem;
  border-radius: 16px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 8px 24px rgba(16, 185, 129, 0.3);
}

.create-quiz-btn:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 12px 32px rgba(16, 185, 129, 0.4);
}

.create-quiz-btn:disabled {
  opacity: 0.7;
  cursor: not-allowed;
}

.create-quiz-btn .spinner {
  animation: spin 1s linear infinite;
}

/* Export/Preview Button */
.export-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  background: linear-gradient(135deg, var(--accent-color) 0%, var(--primary-color-light) 100%);
  color: white;
  border: none;
  padding: 0.875rem 1.5rem;
  border-radius: 16px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 8px 24px var(--primary-color-alpha);
}

.export-btn:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 12px 32px var(--primary-color-alpha);
}

.export-btn:disabled {
  opacity: 0.7;
  cursor: not-allowed;
}

.export-btn .spinner {
  animation: spin 1s linear infinite;
}

@keyframes spin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
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
  position: relative;
  overflow: hidden;
}

.content-card::before {
  content: '';
  position: absolute;
  top: -50%;
  left: -50%;
  width: 200%;
  height: 200%;
  background: radial-gradient(ellipse at center, rgba(16, 185, 129, 0.03) 0%, transparent 70%);
  z-index: 1;
}

.content-card > * {
  position: relative;
  z-index: 2;
}

.content-card:hover {
  transform: translateY(-2px);
  box-shadow: 
    0 25px 70px var(--shadow-medium),
    0 12px 40px var(--shadow-light),
    0 0 0 1px rgba(255, 255, 255, 0.4);
  border-color: var(--accent-color);
}

/* Enhanced Card Design */
.enhanced-card {
  position: relative;
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(20px);
  border: 1px solid rgba(61, 141, 122, 0.1);
  border-radius: 24px;
  padding: 2.5rem;
  overflow: hidden;
  box-shadow: 
    0 8px 32px rgba(61, 141, 122, 0.1),
    0 0 0 1px rgba(255, 255, 255, 0.2);
}

.enhanced-card:hover {
  transform: translateY(-4px);
  box-shadow: 
    0 12px 48px rgba(61, 141, 122, 0.15),
    0 0 0 1px rgba(255, 255, 255, 0.3);
}

.card-floating-shapes {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  pointer-events: none;
  overflow: hidden;
}

.card-shape {
  position: absolute;
  border-radius: 50%;
  opacity: 0.08;
  animation: floatCard 4s ease-in-out infinite;
}

.card-shape.shape-1 {
  width: 80px;
  height: 80px;
  background: linear-gradient(135deg, var(--accent-color), var(--primary-color-light));
  top: -30px;
  right: -30px;
  animation-delay: 0s;
}

.card-shape.shape-2 {
  width: 60px;
  height: 60px;
  background: linear-gradient(135deg, var(--primary-color-light), var(--success-color));
  bottom: -20px;
  left: -20px;
  animation-delay: 2s;
}

@keyframes floatCard {
  0%, 100% { transform: translateY(0px) scale(1); }
  50% { transform: translateY(-15px) scale(1.05); }
}

.card-header {
  position: relative;
  z-index: 2;
  display: flex;
  align-items: center;
  gap: 1.5rem;
  margin-bottom: 2.5rem;
  text-align: left;
}

.card-header-icon {
  width: 50px;
  height: 50px;
  background: linear-gradient(135deg, var(--accent-color), var(--primary-color-dark));
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  box-shadow: 0 4px 12px rgba(61, 141, 122, 0.3);
  transition: all 0.3s ease;
}

.card-header-icon:hover {
  transform: scale(1.05);
}

.card-header-content {
  flex: 1;
}

.card-header h3 {
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--accent-color);
  margin: 0 0 0.5rem 0;
  letter-spacing: -0.3px;
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
  background: rgba(16, 185, 129, 0.1);
  border: 1px solid rgba(16, 185, 129, 0.2);
}

.info-badge .label {
  font-weight: 600;
  color: var(--secondary-text-color);
}

.info-badge .value {
  font-weight: 700;
  color: var(--primary-text-color);
}

/* Enhanced Header Styles */
.section-header-card {
  background: rgba(255, 255, 255, 0.95);
  border: 1px solid rgba(0, 0, 0, 0.1);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.section-header-card:hover {
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.15);
}

.header-bg-decoration {
  background: radial-gradient(ellipse at center, rgba(16, 185, 129, 0.1) 0%, transparent 70%);
}

.floating-shapes {
  display: none;
}

/* Enhanced Form Styling */
.form-content {
  position: relative;
  z-index: 2;
}

.quiz-meta {
  margin-bottom: 2rem;
}

.form-group {
  margin-bottom: 1.5rem;
}

.form-group label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: 600;
  color: var(--primary-text-color);
  font-size: 0.95rem;
}

.form-group input,
.form-group select,
.form-group textarea {
  width: 100%;
  padding: 0.75rem 1rem;
  border: 1px solid var(--border-color);
  border-radius: 12px;
  font-size: 1rem;
  background: var(--card-background);
  color: var(--primary-text-color);
  transition: all 0.2s ease;
}

.form-group input:focus,
.form-group select:focus,
.form-group textarea:focus {
  outline: none;
  border-color: var(--primary-color);
  box-shadow: 0 0 0 3px var(--primary-color-alpha);
}

.form-row {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1.5rem;
  margin-bottom: 1.5rem;
}

/* Questions Section */
.questions-section {
  margin-top: 3rem;
}

.enhanced-questions {
  background: rgba(255, 255, 255, 0.8);
  border-radius: 20px;
  padding: 2rem;
  border: 1px solid var(--card-border-color);
}

.questions-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
  padding-bottom: 1.5rem;
  border-bottom: 2px solid var(--border-color);
}

.add-question-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  background: linear-gradient(135deg, var(--primary-color) 0%, var(--primary-color-dark) 100%);
  color: white;
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 12px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 4px 12px var(--primary-color-alpha);
}

.add-question-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px var(--primary-color-alpha);
}

.questions-list {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.question-item {
  background: var(--card-background);
  border: 1px solid var(--border-color);
  border-radius: 16px;
  padding: 1.5rem;
  transition: all 0.3s ease;
}

.question-item:hover {
  border-color: var(--primary-color);
  box-shadow: 0 4px 12px var(--shadow-light);
}

.question-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
}

.question-header h4 {
  margin: 0;
  color: var(--primary-color);
  font-weight: 700;
}

.remove-question-btn {
  background: rgba(239, 68, 68, 0.1);
  border: 1px solid rgba(239, 68, 68, 0.2);
  color: #ef4444;
  border-radius: 8px;
  padding: 0.5rem;
  cursor: pointer;
  transition: all 0.2s ease;
}

.remove-question-btn:hover {
  background: rgba(239, 68, 68, 0.2);
}

/* Choice styling */
.choices-section {
  margin-top: 1rem;
}

.choices-list {
  margin-bottom: 1rem;
}

.choice-item {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  margin-bottom: 0.75rem;
}

.choice-input {
  flex: 1;
  padding: 0.6rem 1rem;
  border: 1px solid var(--border-color);
  border-radius: 8px;
  font-size: 0.95rem;
}

.choice-input:focus {
  outline: none;
  border-color: var(--primary-color);
  box-shadow: 0 0 0 2px var(--primary-color-alpha);
}

.remove-choice-btn {
  background: rgba(239, 68, 68, 0.1);
  border: none;
  color: #ef4444;
  width: 32px;
  height: 32px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  font-size: 1.2rem;
  font-weight: bold;
}

.remove-choice-btn:hover {
  background: rgba(239, 68, 68, 0.2);
}

.add-choice-btn {
  background: rgba(16, 185, 129, 0.1);
  border: 1px solid rgba(16, 185, 129, 0.2);
  color: var(--primary-color);
  padding: 0.5rem 1rem;
  border-radius: 8px;
  cursor: pointer;
  font-weight: 600;
  transition: all 0.2s ease;
}

.add-choice-btn:hover {
  background: rgba(16, 185, 129, 0.2);
}

/* True/False styling */
.true-false-section {
  margin-top: 1rem;
}

.radio-group {
  display: flex;
  gap: 2rem;
  margin-top: 0.5rem;
}

.radio-option {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  cursor: pointer;
}

.radio-option input[type="radio"] {
  width: 18px;
  height: 18px;
  accent-color: var(--primary-color);
}

/* Form Actions */
.form-actions {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 3rem;
  padding-top: 2rem;
  border-top: 2px solid var(--border-color);
}

.cancel-btn {
  background: rgba(100, 116, 139, 0.1);
  border: 1px solid rgba(100, 116, 139, 0.2);
  color: #64748b;
  padding: 0.875rem 2rem;
  border-radius: 12px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
}

.cancel-btn:hover {
  background: rgba(100, 116, 139, 0.2);
}

.submit-quiz-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  background: linear-gradient(135deg, var(--primary-color) 0%, var(--primary-color-dark) 100%);
  color: white;
  border: none;
  padding: 0.875rem 2rem;
  border-radius: 12px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 4px 12px var(--primary-color-alpha);
}

.submit-quiz-btn:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px var(--primary-color-alpha);
}

.submit-quiz-btn:disabled {
  opacity: 0.7;
  cursor: not-allowed;
}

.submit-quiz-btn .spinner {
  animation: spin 1s linear infinite;
}

/* Responsive Design */
@media (max-width: 768px) {
  .section-header-content {
    flex-direction: column;
    gap: 1.5rem;
    text-align: center;
  }
  
  .section-header-left {
    flex-direction: column;
    gap: 1rem;
  }
  
  .header-actions {
    flex-direction: column;
    gap: 1rem;
    width: 100%;
  }
  
  .form-row {
    grid-template-columns: 1fr;
  }
  
  .quiz-options {
    flex-direction: column;
    gap: 1rem;
  }
  
  .questions-header {
    flex-direction: column;
    gap: 1rem;
  }
  
  .form-actions {
    flex-direction: column;
    gap: 1rem;
  }
}

/* ...existing code... */
</style>