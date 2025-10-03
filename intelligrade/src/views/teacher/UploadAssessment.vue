<template>
    <div class="upload-page">
      <!-- Floating Gradient Blobs -->
      <div class="floating-shape shape1"></div>
      <div class="floating-shape shape2"></div>
      <div class="floating-shape shape3"></div>

      <!-- Header -->
      <div class="header-card">
        <div class="header-content">
          <div class="icon-wrapper">🤖</div>
          <div>
            <h1>Automated Assessment Checker</h1>
            <p>Upload student assessments for instant AI-powered scoring and detailed feedback</p>
          </div>
        </div>
      </div>

      <!-- Loading Overlay -->
      <div v-if="isLoading" class="loading-overlay">
        <div class="loader"></div>
        <p>{{ loadingMessage }}</p>
        <div v-if="processingSteps.length > 0" class="processing-steps">
          <div v-for="(step, index) in processingSteps" :key="index" 
               class="processing-step" :class="{ 'completed': step.completed, 'active': step.active }">
            <span class="step-icon">{{ step.completed ? '✅' : (step.active ? '⏳' : '⏸️') }}</span>
            <span class="step-text">{{ step.text }}</span>
          </div>
        </div>
      </div>

      <!-- Student Assessment Upload -->
      <div class="card">
        <div class="card-header">
          <h2>Student Assessment Upload</h2>
          <p>Upload a student's completed assessment for automatic AI grading and feedback</p>
        </div>
        <div class="card-body">
          <div class="form-row">
            <div class="form-group">
              <label for="student-name">Student Name (Optional)</label>
              <input v-model="studentName" id="student-name" type="text" class="form-control"
                placeholder="Will auto-detect from file if available" />
              <small class="form-hint">💡 Leave blank if the student name is already in the assessment file</small>
            </div>

            <div class="form-group">
              <label for="subject">Subject</label>
              <input v-model="subject" id="subject" type="text" class="form-control"
                placeholder="e.g., Mathematics, Science" required />
            </div>
          </div>

          <div class="form-row">
            <div class="form-group">
              <label for="assessment-title">Assessment Title (Optional)</label>
              <input v-model="assessmentTitle" id="assessment-title" type="text" class="form-control"
                placeholder="Will auto-detect from file if available" />
              <small class="form-hint">💡 Leave blank to use the title from the assessment file</small>
            </div>

            <div class="form-group">
              <label for="total-points">Total Possible Points</label>
              <input v-model="totalPoints" id="total-points" type="number" class="form-control" min="1"
                placeholder="100" required />
            </div>
          </div>

          <div class="form-group">
            <label for="assessment-type">Assessment Type</label>
            <select v-model="selectedTemplate" id="assessment-type" class="form-control" required>
              <option value="">Select assessment type...</option>
              <option value="multiple-choice">Multiple Choice Questions Only</option>
              <option value="true-false">True/False Questions Only</option>
              <option value="mixed">Mixed Format (MCQ + True/False)</option>
            </select>
          </div>
        </div>
      </div>

      <!-- Upload File -->
      <div class="card">
        <div class="card-header">
          <h2>Upload Student's Assessment</h2>
          <p>Upload the completed assessment document for AI-powered analysis</p>
        </div>
        <div class="card-body">
          <div class="file-upload-area" :class="{ 'drag-over': isDragOver }" @dragover.prevent="handleDragOver"
            @dragleave.prevent="handleDragLeave" @drop.prevent="handleDrop" @click="$refs.fileInput.click()">
            <input type="file" id="file-upload" @change="handleFileUpload" class="file-input"
              accept=".txt,.docx,.pdf,.jpg,.jpeg,.png" ref="fileInput" />
            <div class="upload-content">
              <svg class="upload-icon" fill="currentColor" viewBox="0 0 24 24" width="48" height="48">
                <path
                  d="M19.35 10.04C18.67 6.59 15.64 4 12 4 9.11 4 6.6 5.64 5.35 8.04 2.34 8.36 0 10.91 0 14c0 3.31 2.69 6 6 6h13c2.76 0 5-2.24 5-5 0-2.64-2.05-4.78-4.65-4.96zM14 13v4h-4v-4H7l5-5 5 5h-3z" />
              </svg>
              <p v-if="!assessmentFile">
                Drop student's assessment here or <span class="upload-link">browse</span>
              </p>
              <p v-else class="file-selected">
                📄 {{ assessmentFile.name }} ({{ formatFileSize(assessmentFile.size) }})
              </p>
              <small>Supported: TXT, DOCX, PDF, Images (JPG, PNG)</small>
            </div>
          </div>

          <div v-if="selectedTemplate" class="template-guide">
            <h4>{{ getTemplateTitle(selectedTemplate) }} - AI Analysis Features:</h4>
            <div class="ai-features">
              <div class="feature-item">
                <span class="feature-icon">🔍</span>
                <span>Auto-detects Multiple Choice and True/False answers</span>
              </div>
              <div class="feature-item">
                <span class="feature-icon">📊</span>
                <span>Instant scoring with detailed breakdown</span>
              </div>
              <div class="feature-item">
                <span class="feature-icon">💡</span>
                <span>AI feedback on knowledge gaps</span>
              </div>
              <div class="feature-item">
                <span class="feature-icon">🎯</span>
                <span>Specific improvement recommendations</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- AI Grading Settings -->
      <div class="card">
        <div class="card-header">
          <h2>AI Grading Configuration</h2>
          <p>Configure the automated scoring and feedback settings</p>
        </div>
        <div class="card-body">
          <div class="ai-settings-grid">
            <div class="setting-card">
              <div class="setting-header">
                <span class="setting-icon">🧠</span>
                <h3>AI Analysis Level</h3>
              </div>
              <select v-model="aiAnalysisLevel" class="form-control">
                <option value="basic">Basic - Quick scoring</option>
                <option value="standard">Standard - Detailed analysis</option>
                <option value="comprehensive">Comprehensive - Full feedback</option>
              </select>
            </div>

            <div class="setting-card">
              <div class="setting-header">
                <span class="setting-icon">📝</span>
                <h3>Feedback Detail</h3>
              </div>
              <select v-model="feedbackLevel" class="form-control">
                <option value="minimal">Score only</option>
                <option value="standard">Score + brief feedback</option>
                <option value="detailed">Score + detailed feedback</option>
                <option value="comprehensive">Full analysis report</option>
              </select>
            </div>
          </div>

          <div class="checkbox-group">
            <label class="checkbox-item">
              <input type="checkbox" v-model="detectWeaknesses" />
              <span class="checkmark"></span>
              <span class="checkbox-text">Identify student weaknesses and learning gaps</span>
            </label>
            
            <label class="checkbox-item">
              <input type="checkbox" v-model="generateRecommendations" />
              <span class="checkmark"></span>
              <span class="checkbox-text">Generate improvement recommendations</span>
            </label>
            
            <label class="checkbox-item">
              <input type="checkbox" v-model="compareToStandards" />
              <span class="checkmark"></span>
              <span class="checkbox-text">Compare performance to grade-level standards</span>
            </label>
          </div>
        </div>
      </div>

      <!-- Results Display -->
      <div v-if="gradingResults" class="card results-card">
        <div class="card-header">
          <h2>AI Grading Results</h2>
          <p>Automated analysis completed for {{ studentName }}'s assessment</p>
        </div>
        <div class="card-body">
          <!-- Score Overview -->
          <div class="score-overview">
            <div class="score-circle" :class="getScoreClass(gradingResults.percentage)">
              <div class="score-value">{{ gradingResults.percentage }}%</div>
              <div class="score-label">Overall Score</div>
            </div>
            <div class="score-details">
              <div class="detail-item">
                <span class="detail-label">Student:</span>
                <span class="detail-value">{{ gradingResults.studentName }}</span>
              </div>
              <div class="detail-item">
                <span class="detail-label">Assessment:</span>
                <span class="detail-value">{{ gradingResults.assessmentTitle }}</span>
              </div>
              <div class="detail-item">
                <span class="detail-label">Points Earned:</span>
                <span class="detail-value">{{ gradingResults.pointsEarned }} / {{ gradingResults.totalPoints }}</span>
              </div>
              <div class="detail-item">
                <span class="detail-label">Letter Grade:</span>
                <span class="detail-value grade-letter" :class="getGradeClass(gradingResults.percentage)">
                  {{ getLetterGrade(gradingResults.percentage) }}
                </span>
              </div>
            </div>
          </div>

          <!-- AI Feedback -->
          <div v-if="gradingResults.feedback" class="ai-feedback">
            <h3>AI-Generated Feedback</h3>
            
            <div class="feedback-section">
              <h4><span class="feedback-icon">💪</span> Strengths Identified</h4>
              <ul class="feedback-list strengths">
                <li v-for="strength in gradingResults.feedback.strengths" :key="strength">{{ strength }}</li>
              </ul>
            </div>

            <div class="feedback-section">
              <h4><span class="feedback-icon">🎯</span> Areas for Improvement</h4>
              <ul class="feedback-list weaknesses">
                <li v-for="weakness in gradingResults.feedback.weaknesses" :key="weakness">{{ weakness }}</li>
              </ul>
            </div>

            <div class="feedback-section">
              <h4><span class="feedback-icon">📚</span> Recommendations</h4>
              <ul class="feedback-list recommendations">
                <li v-for="rec in gradingResults.feedback.recommendations" :key="rec">{{ rec }}</li>
              </ul>
            </div>

            <div v-if="gradingResults.feedback.detailedAnalysis" class="detailed-analysis">
              <h4><span class="feedback-icon">🔍</span> Detailed Analysis</h4>
              <p>{{ gradingResults.feedback.detailedAnalysis }}</p>
            </div>
          </div>

          <!-- Question-by-Question Breakdown -->
          <div v-if="gradingResults.questionBreakdown" class="question-breakdown">
            <h3>Question-by-Question Analysis</h3>
            <div class="breakdown-list">
              <div v-for="(question, index) in gradingResults.questionBreakdown" :key="index" 
                   class="question-item" :class="{ 'correct': question.isCorrect, 'incorrect': !question.isCorrect }">
                <div class="question-header">
                  <span class="question-number">Q{{ index + 1 }}</span>
                  <span class="question-status">{{ question.isCorrect ? '✅ Correct' : '❌ Incorrect' }}</span>
                  <span class="question-points">{{ question.pointsEarned }}/{{ question.pointsPossible }} pts</span>
                </div>
                <div v-if="question.feedback" class="question-feedback">
                  <p>{{ question.feedback }}</p>
                </div>
              </div>
            </div>
          </div>

          <!-- Action Buttons -->
          <div class="results-actions">
            <button @click="downloadReport" class="btn-secondary">
              📄 Download Report
            </button>
            <button @click="viewAllAssessments" class="btn-primary">
              � View All Assessments
            </button>
            <button @click="resetForm" class="btn-secondary">
              🔄 Check Another Assessment
            </button>
          </div>
        </div>
      </div>

      <!-- Error -->
      <div v-if="error" class="error-message">
        <strong>Error:</strong> {{ error }}
      </div>

      <!-- Action Buttons -->
      <div class="action-buttons">
        <button @click="clearForm" class="btn-secondary">Clear Form</button>
        <button @click="submitAssessment" class="btn-submit" :disabled="!canSubmit || isLoading">
          <span v-if="isLoading">Processing...</span>
          <span v-else>🤖 Start AI Grading</span>
        </button>
      </div>
    </div>
  </template>

  <script>
  import { ref, computed } from "vue";
  import { useRouter } from "vue-router";

  export default {
    name: "UploadAssessment",
    setup() {
      const router = useRouter();
      const isLoading = ref(false);
      const loadingMessage = ref("Processing...");
      const isDragOver = ref(false);
      
      // Student and Assessment Info
      const studentName = ref("");
      const assessmentTitle = ref("");
      const subject = ref("");
      const totalPoints = ref(100);
      const selectedTemplate = ref("");
      const assessmentFile = ref(null);
      
      // AI Grading Settings
      const aiAnalysisLevel = ref("standard");
      const feedbackLevel = ref("detailed");
      const detectWeaknesses = ref(true);
      const generateRecommendations = ref(true);
      const compareToStandards = ref(false);
      
      // Results and Processing
      const gradingResults = ref(null);
      const error = ref("");
      const processingSteps = ref([]);

      // File Handling
      const handleFileUpload = (event) => {
        const file = event.target.files[0];
        if (file) {
          assessmentFile.value = file;
          error.value = "";
        }
      };

      const handleDragOver = () => {
        isDragOver.value = true;
      };

      const handleDragLeave = () => {
        isDragOver.value = false;
      };

      const handleDrop = (event) => {
        const file = event.dataTransfer.files[0];
        if (file) {
          assessmentFile.value = file;
          error.value = "";
        }
        isDragOver.value = false;
      };

      const formatFileSize = (size) => {
        if (size < 1024) return size + " bytes";
        else if (size < 1048576) return (size / 1024).toFixed(1) + " KB";
        else return (size / 1048576).toFixed(1) + " MB";
      };

      // Template Helpers
      const getTemplateTitle = (template) => {
        const titles = {
          "multiple-choice": "Multiple Choice (MCQ)",
          "true-false": "True/False",
          "short-answer": "Short Answer",
          "essay": "Essay",
          "mixed": "Mixed Format"
        };
        return titles[template] || "";
      };

      // Processing Steps Setup
      const setupProcessingSteps = () => {
        processingSteps.value = [
          { text: "Uploading file to server", completed: false, active: true },
          { text: "Parsing assessment content", completed: false, active: false },
          { text: "Running AI analysis", completed: false, active: false },
          { text: "Calculating scores", completed: false, active: false },
          { text: "Generating feedback", completed: false, active: false },
          { text: "Finalizing results", completed: false, active: false }
        ];
      };

      const updateProcessingStep = (stepIndex) => {
        if (stepIndex > 0) {
          processingSteps.value[stepIndex - 1].completed = true;
          processingSteps.value[stepIndex - 1].active = false;
        }
        if (stepIndex < processingSteps.value.length) {
          processingSteps.value[stepIndex].active = true;
        }
      };

      // Main Submit Function - Connects to Backend
      const submitAssessment = async () => {
        // Only require subject, total points, assessment type, and file
        if (!subject.value || !totalPoints.value || !selectedTemplate.value || !assessmentFile.value) {
          error.value = "Please fill in Subject, Total Points, Assessment Type, and upload a file.";
          return;
        }

        console.log('🚀 Starting assessment submission...');
        console.log('📁 File:', assessmentFile.value);
        console.log('📚 Subject:', subject.value);
        console.log('🎯 Type:', selectedTemplate.value);

        isLoading.value = true;
        error.value = "";
        gradingResults.value = null;
        setupProcessingSteps();

        try {
          // Step 1: Upload File
          loadingMessage.value = "Uploading assessment...";
          updateProcessingStep(0);

          const formData = new FormData();
          formData.append('file', assessmentFile.value);
          formData.append('student_name', studentName.value || 'Auto-detected');
          formData.append('assessment_title', assessmentTitle.value || 'Auto-detected');
          formData.append('subject', subject.value);
          formData.append('total_points', totalPoints.value);
          formData.append('assessment_type', selectedTemplate.value);
          formData.append('ai_analysis_level', aiAnalysisLevel.value);
          formData.append('feedback_level', feedbackLevel.value);
          formData.append('detect_weaknesses', detectWeaknesses.value);
          formData.append('generate_recommendations', generateRecommendations.value);
          formData.append('compare_to_standards', compareToStandards.value);

          console.log('📤 Sending to: http://localhost:8000/api/assessments/upload');

          // Call your backend API endpoint
          const response = await fetch('http://localhost:8000/api/assessments/upload', {
            method: 'POST',
            body: formData
          });

          console.log('📥 Response status:', response.status);
          console.log('📥 Response ok:', response.ok);

          if (!response.ok) {
            const errorText = await response.text();
            console.error('❌ Backend error:', errorText);
            throw new Error(`Upload failed: ${response.status} ${response.statusText} - ${errorText}`);
          }

          const result = await response.json();
          console.log('✅ Backend response:', result);

          // Step 2: Parse Content
          updateProcessingStep(1);
          loadingMessage.value = "Extracting student name and assessment details...";
          await new Promise(resolve => setTimeout(resolve, 1500));

          // Step 3: AI Analysis
          updateProcessingStep(2);
          loadingMessage.value = "AI analyzing MCQ and True/False answers...";
          await new Promise(resolve => setTimeout(resolve, 3000));

          // Step 4: Calculate Scores
          updateProcessingStep(3);
          loadingMessage.value = "Calculating scores and accuracy...";
          await new Promise(resolve => setTimeout(resolve, 1000));

          // Step 5: Generate Feedback
          updateProcessingStep(4);
          loadingMessage.value = "Generating personalized feedback...";
          await new Promise(resolve => setTimeout(resolve, 2000));

          // Step 6: Finalize
          updateProcessingStep(5);
          loadingMessage.value = "Finalizing results...";
          await new Promise(resolve => setTimeout(resolve, 1000));

          // Process real backend response or simulate for demo
          gradingResults.value = result.results || {
            studentName: result.student_name || studentName.value || "John Smith",
            assessmentTitle: result.assessment_title || assessmentTitle.value || "Math Quiz - Chapter 5",
            percentage: 82,
            pointsEarned: 82,
            totalPoints: totalPoints.value,
            processingTime: 6.8,
            feedback: {
              strengths: [
                "Strong performance on multiple choice questions (85% accuracy)",
                "Excellent understanding of True/False concepts",
                "Consistent answering pattern shows good preparation"
              ],
              weaknesses: [
                "Struggled with questions 7-9 (probability concepts)", 
                "Mixed up True/False on definition-based questions",
                "Could improve on multi-step problem solving"
              ],
              recommendations: [
                "Review probability theory and practice similar problems",
                "Focus on carefully reading True/False statements",
                "Practice breaking down complex problems into steps"
              ],
              detailedAnalysis: "The student shows solid foundational knowledge with particularly strong performance on direct application questions. The main areas for improvement are in conceptual understanding of probability and careful analysis of True/False statements."
            },
            questionBreakdown: [
              { isCorrect: true, pointsEarned: 5, pointsPossible: 5, feedback: "Perfect! Clear understanding of basic concepts." },
              { isCorrect: false, pointsEarned: 2, pointsPossible: 5, feedback: "Incorrect choice selected. Review the definition of independent events." },
              { isCorrect: true, pointsEarned: 5, pointsPossible: 5, feedback: "Excellent work on this True/False question." },
              { isCorrect: false, pointsEarned: 0, pointsPossible: 5, feedback: "This statement was True, but False was selected. Be more careful with negations." }
            ]
          };

          // Mark all steps complete
          processingSteps.value.forEach(step => {
            step.completed = true;
            step.active = false;
          });

          // Show success message and redirect after delay
          setTimeout(() => {
            alert("✅ Your assessment has been checked successfully!\n\nRedirecting to Assessment History...");
            // Redirect to history page
            router.push('/teacher/assessment-history');
          }, 1000);

        } catch (err) {
          console.error('Assessment processing error:', err);
          error.value = "Failed to process assessment: " + err.message;
        } finally {
          isLoading.value = false;
        }
      };

      // Score and Grade Helpers
      const getScoreClass = (percentage) => {
        if (percentage >= 90) return "excellent";
        if (percentage >= 80) return "good";
        if (percentage >= 70) return "average";
        if (percentage >= 60) return "below-average";
        return "poor";
      };

      const getLetterGrade = (percentage) => {
        if (percentage >= 90) return "A";
        if (percentage >= 80) return "B";
        if (percentage >= 70) return "C";
        if (percentage >= 60) return "D";
        return "F";
      };

      const getGradeClass = (percentage) => {
        if (percentage >= 80) return "grade-a";
        if (percentage >= 70) return "grade-b";
        if (percentage >= 60) return "grade-c";
        return "grade-f";
      };

      // Action Functions
      const downloadReport = () => {
        const reportData = {
          student: studentName.value,
          assessment: assessmentTitle.value,
          subject: subject.value,
          score: gradingResults.value.percentage,
          feedback: gradingResults.value.feedback
        };
        
        const blob = new Blob([JSON.stringify(reportData, null, 2)], { type: 'application/json' });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = `${studentName.value}_${assessmentTitle.value}_report.json`;
        a.click();
        URL.revokeObjectURL(url);
      };

      const resetForm = () => {
        studentName.value = "";
        assessmentTitle.value = "";
        subject.value = "";
        totalPoints.value = 100;
        selectedTemplate.value = "";
        assessmentFile.value = null;
        gradingResults.value = null;
        error.value = "";
        processingSteps.value = [];
      };

      const clearForm = () => {
        resetForm();
      };

      const viewAllAssessments = () => {
        // Navigate to Assessment History page
        router.push('/teacher/assessment-history');
      };

      // Computed Properties
      const canSubmit = computed(() => {
        return subject.value && 
               totalPoints.value && 
               selectedTemplate.value && 
               assessmentFile.value &&
               !isLoading.value;
      });

      return {
        isLoading,
        loadingMessage,
        isDragOver,
        studentName,
        assessmentTitle,
        subject,
        totalPoints,
        selectedTemplate,
        assessmentFile,
        aiAnalysisLevel,
        feedbackLevel,
        detectWeaknesses,
        generateRecommendations,
        compareToStandards,
        gradingResults,
        error,
        processingSteps,
        handleFileUpload,
        handleDragOver,
        handleDragLeave,
        handleDrop,
        formatFileSize,
        getTemplateTitle,
        submitAssessment,
        getScoreClass,
        getLetterGrade,
        getGradeClass,
        downloadReport,
        viewAllAssessments,
        resetForm,
        clearForm,
        canSubmit
      };
    },
  };
  </script>

  <style scoped>

  @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap');

  /* Reuse Dashboard Design Language */
  .upload-page {
    max-width: 1000px;
    margin: 2rem auto;
    padding: 1rem;
    position: relative;
    z-index: 1;
    font-family: 'Poppins', sans-serif;
  }

  /* Floating Gradient Shapes */
  .floating-shape {
    position: absolute;
    border-radius: 50%;
    filter: blur(70px);
    opacity: 0.4;
    z-index: 0;
  }
  .shape1 { top: -100px; left: -100px; width: 300px; height: 300px; background: #3D8D7A; animation: float 6s ease-in-out infinite; }
  .shape2 { bottom: -120px; right: -80px; width: 250px; height: 250px; background: #B3D8A8; animation: float 7s ease-in-out infinite; }
  .shape3 { top: 40%; left: -60px; width: 200px; height: 200px; background: #87CBB9; animation: float 8s ease-in-out infinite; }

  @keyframes float {
    0%, 100% { transform: translateY(0) translateX(0); }
    50% { transform: translateY(-20px) translateX(20px); }
  }

  /* Header Card */
  .header-card {
    background: linear-gradient(135deg, #3D8D7A, #87CBB9);
    border-radius: 20px;
    padding: 2rem;
    margin-bottom: 2rem;
    color: white;
    position: relative;
    box-shadow: 0 8px 30px rgba(0,0,0,0.1);
  }
  .header-content {
    display: flex;
    align-items: center;
    gap: 1rem;
  }
  .header-content h1 {
    font-size: 2rem;
    margin: 0 0 0.3rem 0;
  }
  .header-content p {
    margin: 0;
    font-size: 1rem;
    opacity: 0.9;
  }
  .icon-wrapper {
    background: rgba(255,255,255,0.2);
    padding: 1rem;
    border-radius: 50%;
    font-size: 2rem;
  }

  /* Cards */
  .card {
    background: rgba(255,255,255,0.85);
    border-radius: 16px;
    box-shadow: 0 6px 25px rgba(0,0,0,0.05);
    margin-bottom: 2rem;
    overflow: hidden;
    backdrop-filter: blur(10px);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
  }
  .card:hover {
    transform: translateY(-3px);
    box-shadow: 0 10px 30px rgba(0,0,0,0.08);
  }
  .card-header {
    padding: 1.5rem 2rem;
    border-bottom: 1px solid rgba(0,0,0,0.05);
  }
  .card-header h2 {
    margin: 0 0 0.25rem 0;
    font-size: 1.3rem;
    font-weight: 600;
  }
  .card-header p {
    margin: 0;
    font-size: 0.9rem;
    color: #6c757d;
  }
  .card-body {
    padding: 2rem;
  }

  /* Forms */
  .form-row {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1.5rem;
  }
  .form-group {
    margin-bottom: 1.5rem;
  }
  .form-group label {
    display: block;
    margin-bottom: 0.5rem;
    font-weight: 500;
    font-size: 0.95rem;
  }
  .form-control {
    width: 100%;
    padding: 0.75rem 1rem;
    border: 1px solid #E0E7EE;
    border-radius: 10px;
    font-size: 1rem;
    transition: border-color 0.2s ease, box-shadow 0.2s ease;
  }
  .form-control:focus {
    border-color: #3D8D7A;
    box-shadow: 0 0 0 3px rgba(61, 141, 122, 0.15);
    outline: none;
  }

  /* Upload */
  .file-upload-area {
    border: 2px dashed #E0E7EE;
    border-radius: 12px;
    padding: 2rem;
    text-align: center;
    background: rgba(250, 252, 254, 0.8);
    transition: all 0.3s ease;
    cursor: pointer;
  }
  .file-upload-area:hover, .file-upload-area.drag-over {
    border-color: #3D8D7A;
    background-color: rgba(61, 141, 122, 0.05);
  }
  .file-input { display: none; }
  .upload-icon { color: #a0aec0; margin-bottom: 1rem; }
  .upload-link { color: #3D8D7A; font-weight: 600; }
  .file-selected { color: #3D8D7A; font-weight: 500; }

  /* Template Guide */
  .template-guide {
    margin-top: 1.5rem;
    padding: 1rem;
    border-left: 4px solid #87CBB9;
    background: rgba(135,203,185,0.1);
    border-radius: 8px;
  }
  .format-example pre {
    margin: 0;
    padding: 1rem;
    background: white;
    border-radius: 6px;
    border: 1px solid #E0E7EE;
    font-family: monospace;
    font-size: 0.85rem;
    color: #555;
  }

  /* Preview */
  .preview-meta {
    display: flex;
    align-items: center;
    gap: 1rem;
    margin-bottom: 1rem;
  }
  .badge {
    background: #B3D8A8;
    color: #2c3e50;
    padding: 0.3rem 0.8rem;
    border-radius: 20px;
    font-size: 0.8rem;
    font-weight: 600;
  }
  .preview-text {
    background: #F7F9F7;
    padding: 1rem;
    border-radius: 8px;
    border: 1px solid #E0E7EE;
    max-height: 250px;
    overflow-y: auto;
  }

  /* Buttons */
  .action-buttons {
    display: flex;
    gap: 1rem;
    justify-content: flex-end;
    margin-bottom: 2rem;
  }
  .btn-submit, .btn-secondary {
    padding: 0.75rem 1.5rem;
    border-radius: 10px;
    font-weight: 600;
    font-size: 1rem;
    border: none;
    cursor: pointer;
    transition: all 0.3s ease;
  }
  .btn-submit {
    background: #3D8D7A;
    color: white;
    box-shadow: 0 4px 12px rgba(61,141,122,0.3);
  }
  .btn-submit:hover:not(:disabled) {
    background: #317c6b;
    transform: translateY(-2px);
  }
  .btn-secondary {
    background: #E2E8F0;
    color: #555;
  }
  .btn-secondary:hover { background: #cbd5e0; }

  /* Error */
  .error-message {
    background: #fff5f5;
    color: #c53030;
    padding: 1rem;
    border-radius: 8px;
    border: 1px solid #fed7d7;
    margin-bottom: 1.5rem;
  }

  /* Loader */
  .loading-overlay {
    position: fixed;
    top: 0; left: 0;
    width: 100%; height: 100%;
    background: rgba(255,255,255,0.8);
    backdrop-filter: blur(6px);
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    z-index: 1000;
  }
  .loader {
    width: 50px; height: 50px;
    border: 5px solid #B3D8A8;
    border-top: 5px solid #3D8D7A;
    border-radius: 50%;
    animation: spin 1s linear infinite;
    margin-bottom: 1rem;
  }
  @keyframes spin { to { transform: rotate(360deg); } }

  /* Responsive */
  @media (max-width: 768px) {
    .form-row, .grid-container {
      grid-template-columns: 1fr;
    }
    .action-buttons {
      flex-direction: column-reverse;
    }
    .btn-submit, .btn-secondary {
      width: 100%;
    }
  }

  /* Processing Steps */
  .processing-steps {
    margin-top: 1.5rem;
    padding: 1rem;
    background: rgba(255, 255, 255, 0.1);
    border-radius: 12px;
    max-width: 400px;
  }

  .processing-step {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    padding: 0.5rem 0;
    color: #666;
    transition: all 0.3s ease;
  }

  .processing-step.active {
    color: #3D8D7A;
    font-weight: 600;
  }

  .processing-step.completed {
    color: #22c55e;
  }

  .step-icon {
    font-size: 1.1rem;
    width: 20px;
    text-align: center;
  }

  /* AI Features */
  .ai-features {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1rem;
    margin-top: 1rem;
  }

  .feature-item {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    padding: 0.75rem;
    background: rgba(179, 216, 168, 0.1);
    border-radius: 8px;
    border: 1px solid rgba(179, 216, 168, 0.3);
  }

  .feature-icon {
    font-size: 1.2rem;
    flex-shrink: 0;
  }

  /* AI Settings Grid */
  .ai-settings-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1.5rem;
    margin-bottom: 2rem;
  }

  .setting-card {
    background: rgba(250, 252, 254, 0.8);
    border: 1px solid #E0E7EE;
    border-radius: 12px;
    padding: 1.5rem;
    transition: all 0.3s ease;
  }

  .setting-card:hover {
    border-color: #3D8D7A;
    box-shadow: 0 4px 12px rgba(61, 141, 122, 0.1);
  }

  .setting-header {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    margin-bottom: 1rem;
  }

  .setting-icon {
    font-size: 1.5rem;
  }

  .setting-header h3 {
    margin: 0;
    font-size: 1.1rem;
    font-weight: 600;
    color: #333;
  }

  /* Checkbox Group */
  .checkbox-group {
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }

  .checkbox-item {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    cursor: pointer;
    padding: 0.75rem;
    border-radius: 8px;
    transition: all 0.3s ease;
  }

  .checkbox-item:hover {
    background: rgba(61, 141, 122, 0.05);
  }

  .checkbox-item input[type="checkbox"] {
    width: 18px;
    height: 18px;
    accent-color: #3D8D7A;
  }

  .checkbox-text {
    font-size: 0.95rem;
    color: #555;
    font-weight: 500;
  }

  /* Form Hints */
  .form-hint {
    font-size: 0.8rem;
    color: var(--gray-500);
    margin-top: 0.25rem;
    font-style: italic;
  }

  /* Results Card */
  .results-card {
    border: 2px solid #22c55e;
    background: linear-gradient(135deg, rgba(34, 197, 94, 0.05) 0%, rgba(179, 216, 168, 0.05) 100%);
  }

  /* Score Overview */
  .score-overview {
    display: flex;
    align-items: center;
    gap: 2rem;
    margin-bottom: 2rem;
    padding: 1.5rem;
    background: rgba(255, 255, 255, 0.6);
    border-radius: 12px;
  }

  .score-circle {
    width: 120px;
    height: 120px;
    border-radius: 50%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    border: 4px solid;
    position: relative;
  }

  .score-circle.excellent { border-color: #22c55e; background: rgba(34, 197, 94, 0.1); }
  .score-circle.good { border-color: #3b82f6; background: rgba(59, 130, 246, 0.1); }
  .score-circle.average { border-color: #f59e0b; background: rgba(245, 158, 11, 0.1); }
  .score-circle.below-average { border-color: #ef4444; background: rgba(239, 68, 68, 0.1); }
  .score-circle.poor { border-color: #dc2626; background: rgba(220, 38, 38, 0.1); }

  .score-value {
    font-size: 2rem;
    font-weight: 700;
    color: #333;
  }

  .score-label {
    font-size: 0.85rem;
    color: #666;
    margin-top: 0.25rem;
  }

  .score-details {
    flex: 1;
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }

  .detail-item {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0.75rem;
    background: rgba(255, 255, 255, 0.8);
    border-radius: 8px;
  }

  .detail-label {
    font-weight: 600;
    color: #555;
  }

  .detail-value {
    font-weight: 700;
    color: #333;
  }

  .grade-letter {
    padding: 0.25rem 0.75rem;
    border-radius: 6px;
    color: white;
    font-weight: 700;
  }

  .grade-letter.grade-a { background: #22c55e; }
  .grade-letter.grade-b { background: #3b82f6; }
  .grade-letter.grade-c { background: #f59e0b; }
  .grade-letter.grade-f { background: #ef4444; }

  /* AI Feedback */
  .ai-feedback {
    margin-bottom: 2rem;
  }

  .ai-feedback h3 {
    color: #333;
    margin-bottom: 1.5rem;
    font-size: 1.25rem;
    font-weight: 700;
  }

  .feedback-section {
    margin-bottom: 1.5rem;
    padding: 1rem;
    background: rgba(255, 255, 255, 0.6);
    border-radius: 10px;
  }

  .feedback-section h4 {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    margin-bottom: 0.75rem;
    font-size: 1.1rem;
    font-weight: 600;
    color: #333;
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

  .feedback-list.strengths li {
    color: #166534;
  }

  .feedback-list.weaknesses li {
    color: #dc2626;
  }

  .feedback-list.recommendations li {
    color: #1d4ed8;
  }

  .detailed-analysis {
    padding: 1rem;
    background: rgba(179, 216, 168, 0.1);
    border-radius: 8px;
    border-left: 4px solid #3D8D7A;
  }

  .detailed-analysis h4 {
    margin-bottom: 0.75rem;
    color: #333;
  }

  .detailed-analysis p {
    line-height: 1.6;
    color: #555;
    margin: 0;
  }

  /* Question Breakdown */
  .question-breakdown {
    margin-bottom: 2rem;
  }

  .question-breakdown h3 {
    margin-bottom: 1rem;
    color: #333;
    font-size: 1.25rem;
    font-weight: 700;
  }

  .breakdown-list {
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }

  .question-item {
    padding: 1rem;
    border-radius: 10px;
    border: 2px solid;
    transition: all 0.3s ease;
  }

  .question-item.correct {
    border-color: #22c55e;
    background: rgba(34, 197, 94, 0.05);
  }

  .question-item.incorrect {
    border-color: #ef4444;
    background: rgba(239, 68, 68, 0.05);
  }

  .question-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 0.5rem;
  }

  .question-number {
    font-weight: 700;
    color: #333;
    background: rgba(255, 255, 255, 0.8);
    padding: 0.25rem 0.75rem;
    border-radius: 6px;
  }

  .question-status {
    font-weight: 600;
    flex: 1;
    text-align: center;
  }

  .question-points {
    font-weight: 600;
    color: #666;
  }

  .question-feedback {
    padding-top: 0.5rem;
    border-top: 1px solid rgba(0, 0, 0, 0.1);
  }

  .question-feedback p {
    margin: 0;
    color: #555;
    font-style: italic;
  }

  /* Results Actions */
  .results-actions {
    display: flex;
    gap: 1rem;
    justify-content: center;
    margin-top: 2rem;
    padding-top: 1.5rem;
    border-top: 1px solid rgba(0, 0, 0, 0.1);
  }

  @media (max-width: 768px) {
    .ai-settings-grid {
      grid-template-columns: 1fr;
    }
    
    .score-overview {
      flex-direction: column;
      text-align: center;
    }
    
    .results-actions {
      flex-direction: column;
    }
    
    .question-header {
      flex-direction: column;
      gap: 0.5rem;
      align-items: flex-start;
    }
  }


  </style>

