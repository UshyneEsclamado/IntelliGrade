<template>
  <div class="page-container">
    <div class="main-wrapper">
      <div class="hero-header card-box">
        <div class="header-content">
          <button @click="goBack" class="back-button">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
              <path d="M10 19l-7-7 7-7m-7 7h18"></path>
            </svg>
            Back to Classes
          </button>
          <h1>{{ classData.name || 'Loading...' }}</h1>
          <p>{{ classData.subject || 'Loading...' }}</p>
        </div>
        <button class="create-quiz-btn" @click="goToCreateQuiz">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <line x1="12" y1="5" x2="12" y2="19"></line>
            <line x1="5" y1="12" x2="19" y2="12"></line>
          </svg>
          Create New Quiz
        </button>
      </div>

      <section class="class-details-grid">
        <div class="card-box students-list-section">
          <div class="section-header">
            <h2>Students ({{ students.length }})</h2>
          </div>
          <ul class="students-list" v-if="students.length > 0">
            <li v-for="student in students" :key="student.id">
              {{ student.name }}
            </li>
          </ul>
          <div v-else class="empty-state">
            <p>No students enrolled in this class yet.</p>
          </div>
        </div>
        
        <div class="card-box assessments-list-section">
          <div class="section-header">
            <h2>Assessments ({{ assessments.length }})</h2>
          </div>
          <ul class="assessments-list" v-if="assessments.length > 0">
            <li v-for="assessment in assessments" :key="assessment.id">
              {{ assessment.title }}
            </li>
          </ul>
          <div v-else class="empty-state">
            <p>No assessments created for this class yet.</p>
          </div>
        </div>

        <div class="card-box ai-grading-section full-width">
          <div class="section-header">
            <h2>🤖 AI Grading for this Class</h2>
            <p class="section-subtitle">Grade completed assessments for {{ classData.name }} automatically with AI.</p>
          </div>
          <div class="assessment-grid">
            <div v-for="assessment in assessmentsToGrade" :key="assessment.id" class="assessment-card">
              <div class="card-content">
                <div class="assessment-info">
                  <h3>{{ assessment.title }}</h3>
                  <p class="assessment-progress">
                    Submitted: {{ assessment.studentsSubmitted }} / {{ assessment.totalStudents }}
                  </p>
                </div>
                <div class="grading-actions">
                  <button
                    class="ai-grade-btn"
                    @click="handleAIGrade(assessment.id)"
                    v-if="!assessment.isGraded"
                    :disabled="assessment.isGrading || assessment.studentsSubmitted === 0"
                  >
                    <span v-if="assessment.isGrading">Grading...</span>
                    <span v-else>Grade with AI</span>
                  </button>
                  <div v-else class="grade-status">
                    ✅ Graded!
                    <button @click="viewResults(assessment.id)" class="see-results-btn">See Results</button>
                  </div>
                </div>
              </div>
            </div>
            <div v-if="assessmentsToGrade.length === 0" class="empty-state">
              <p>No new assessments to grade.</p>
            </div>
          </div>
        </div>
      </section>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { supabase } from '../../supabase';

const route = useRoute();
const router = useRouter();
const classId = ref(route.params.id);

const classData = ref({});
const students = ref([]);
const assessments = ref([]);
const assessmentsToGrade = ref([]);
const isLoading = ref(true);

// Fetch class data from Supabase
const fetchClassDetails = async () => {
  try {
    isLoading.value = true;
    
    // Fetch class information
    const { data: classInfo, error: classError } = await supabase
      .from('classes')
      .select('*')
      .eq('id', classId.value)
      .single();
    
    if (classError) {
      console.error('Error fetching class:', classError);
      return;
    }
    
    classData.value = classInfo;
    
    // Fetch students for this class
    await fetchStudents();
    
    // Fetch assessments for this class
    await fetchAssessments();
    
  } catch (error) {
    console.error('Error fetching class details:', error);
  } finally {
    isLoading.value = false;
  }
};

const fetchStudents = async () => {
  try {
    console.log('Fetching students for class_id:', classId.value);
    
    // Option 1: If students have a class_id column
    const { data: studentData, error } = await supabase
      .from('students')
      .select('*')
      .eq('class_id', classId.value); // Adjust column name if different
    
    console.log('Supabase query result:', { data: studentData, error });
    
    if (error) {
      console.error('Error fetching students:', error);
      return;
    }
    
    students.value = studentData || [];
    
    // Debug: Log the fetched data
    console.log('Class ID:', classId.value);
    console.log('Fetched students:', studentData);
    console.log('Students count:', students.value.length);
    
    // Update student count in classes table
    await updateStudentCount();
    
  } catch (error) {
    console.error('Error in fetchStudents:', error);
  }
};

// Fetch assessments for this class
const fetchAssessments = async () => {
  try {
    const { data: assessmentData, error } = await supabase
      .from('assessments')
      .select('*')
      .eq('class_id', classId.value); // Adjust column name if different
    
    if (error) {
      console.error('Error fetching assessments:', error);
      return;
    }
    
    assessments.value = assessmentData || [];
    
    // Create assessments to grade list
    assessmentsToGrade.value = assessmentData?.map(assessment => ({
      ...assessment,
      studentsSubmitted: 0, // You'll need to calculate this based on your submission table
      totalStudents: students.value.length,
      isGrading: false,
      isGraded: false
    })) || [];
    
  } catch (error) {
    console.error('Error in fetchAssessments:', error);
  }
};

// Update student count in the classes table
const updateStudentCount = async () => {
  try {
    const { error } = await supabase
      .from('classes')
      .update({ student_count: students.value.length })
      .eq('id', classId.value);
    
    if (error) {
      console.error('Error updating student count:', error);
    }
  } catch (error) {
    console.error('Error in updateStudentCount:', error);
  }
};

const goBack = () => {
  router.push({ name: 'MyClasses' });
};

const goToCreateQuiz = () => {
  router.push({ name: 'CreateQuiz', params: { classId: classId.value } });
};

const gradeAssessmentWithAI = async (assessmentId) => {
  const assessment = assessmentsToGrade.value.find(a => a.id === assessmentId);
  if (!assessment) return;
  
  assessment.isGrading = true;
  console.log(`Starting AI grading for assessment ID: ${assessmentId} in class ${classId.value}`);
  
  // Simulate AI grading process - replace with actual AI grading logic
  await new Promise(resolve => setTimeout(resolve, 3000));
  
  assessment.isGrading = false;
  assessment.isGraded = true;
  console.log(`AI grading complete for assessment ID: ${assessmentId}.`);
};

const handleAIGrade = (assessmentId) => {
  gradeAssessmentWithAI(assessmentId);
};

const viewResults = (assessmentId) => {
  router.push({ name: 'AssessmentResults', params: { id: assessmentId } });
};

onMounted(() => {
  fetchClassDetails();
});
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

.page-container {
  padding: 2rem 5%;
  font-family: 'Inter', sans-serif;
  min-height: 100vh;
}

.main-wrapper {
  max-width: 1400px;
  margin: 0 auto;
}

.card-box {
  background: rgba(255, 255, 255, 0.85);
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
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 1.5rem;
}

.header-content {
  flex: 1;
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
  margin-bottom: 1rem;
}

.back-button:hover {
  color: #2e6b5c;
  transform: translateX(-5px);
}

.hero-header h1 {
  font-size: 2.5rem;
  font-weight: 800;
  color: #3D8D7A;
  margin: 0;
}

.hero-header p {
  font-size: 1.1rem;
  color: #666;
  margin: 0;
}

.create-quiz-btn {
  background: linear-gradient(135deg, #A3D1C6 0%, #3D8D7A 100%);
  color: #fff;
  border: none;
  padding: 1rem 2rem;
  border-radius: 16px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  box-shadow: 0 8px 32px rgba(61, 141, 122, 0.2);
  display: flex;
  align-items: center;
  gap: 0.5rem;
  white-space: nowrap;
}

.create-quiz-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 16px 48px rgba(61, 141, 122, 0.3);
}

.create-quiz-btn svg {
  color: #fff;
}

.class-details-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
}

.full-width {
  grid-column: 1 / -1;
}

.section-header h2 {
  font-size: 1.8rem;
  font-weight: 700;
  color: #3D8D7A;
  margin-bottom: 0.5rem;
}

.section-subtitle {
  color: #777;
  font-size: 1rem;
  font-weight: 500;
  margin-bottom: 1.5rem;
}

ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

li {
  padding: 1rem;
  background-color: #f0f8f5;
  border-radius: 12px;
  margin-bottom: 1rem;
  font-weight: 500;
  color: #444;
  border: 1px solid rgba(61, 141, 122, 0.1);
}

.ai-grading-section {
  margin-top: 2rem;
}

.assessment-grid {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.assessment-card {
  background: rgba(251, 255, 228, 0.7);
  border: 1px solid rgba(61, 141, 122, 0.15);
  border-radius: 20px;
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  position: relative;
  overflow: hidden;
  box-shadow: 0 4px 16px rgba(61, 141, 122, 0.1);
}

.assessment-card .card-content {
  padding: 2rem;
  position: relative;
  z-index: 1;
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 1.5rem;
}

.assessment-info h3 {
  font-size: 1.4rem;
  font-weight: 700;
  color: #3D8D7A;
  margin-bottom: 0.5rem;
}

.assessment-info p {
  color: #777;
  font-size: 0.95rem;
}

.assessment-progress {
  font-weight: 600;
  color: #3D8D7A;
}

.grading-actions {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.ai-grade-btn {
  background: linear-gradient(135deg, #3D8D7A 0%, #A3D1C6 100%);
  color: #fff;
  border: none;
  padding: 1rem 2rem;
  border-radius: 16px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  box-shadow: 0 8px 32px rgba(61, 141, 122, 0.2);
}

.ai-grade-btn:hover:enabled {
  transform: translateY(-2px);
  box-shadow: 0 16px 48px rgba(61, 141, 122, 0.3);
}

.ai-grade-btn:disabled {
  background: #ccc;
  cursor: not-allowed;
  opacity: 0.7;
  box-shadow: none;
}

.grade-status {
  display: flex;
  align-items: center;
  gap: 1rem;
  font-weight: 700;
  color: #3D8D7A;
  font-size: 1rem;
}

.see-results-btn {
  background: linear-gradient(135deg, #A3D1C6 0%, #3D8D7A 100%);
  color: white;
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 12px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s;
  white-space: nowrap;
}

.see-results-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(61, 141, 122, 0.2);
}

.empty-state {
  text-align: center;
  color: #888;
  padding: 2rem;
  font-style: italic;
  font-weight: 500;
}
</style>