<template>
  <div class="upload-assessment-container">
    <div class="header">
      <h1>Upload Assessment</h1>
      <p class="subtitle">Create and upload assessments for automatic AI grading</p>
    </div>

    <!-- Loading State -->
    <div v-if="isLoading" class="loading-overlay">
      <div class="loader"></div>
      <p>Processing assessment...</p>
    </div>

    <!-- Assessment Details Form -->
    <div class="assessment-form">
      <div class="form-group">
        <label for="assessment-title">Assessment Title:</label>
        <input 
          v-model="assessmentTitle" 
          id="assessment-title" 
          type="text" 
          class="form-control"
          placeholder="Enter assessment title"
          required
        />
      </div>

      <div class="form-row">
        <div class="form-group">
          <label for="template">Assessment Type:</label>
          <select v-model="selectedTemplate" id="template" class="form-control">
            <option value="multiple-choice">Multiple Choice (MCQ)</option>
            <option value="true-false">True/False</option>
            <option value="short-answer">Short Answer</option>
            <option value="essay">Essay Questions</option>
            <option value="mixed">Mixed Format</option>
          </select>
        </div>

        <div class="form-group">
          <label for="subject">Subject:</label>
          <input 
            v-model="subject" 
            id="subject" 
            type="text" 
            class="form-control"
            placeholder="e.g., Mathematics, Science"
          />
        </div>
      </div>

      <div class="form-row">
        <div class="form-group">
          <label for="duration">Duration (minutes):</label>
          <input 
            v-model="duration" 
            id="duration" 
            type="number" 
            class="form-control"
            min="1"
            max="300"
            placeholder="60"
          />
        </div>

        <div class="form-group">
          <label for="total-points">Total Points:</label>
          <input 
            v-model="totalPoints" 
            id="total-points" 
            type="number" 
            class="form-control"
            min="1"
            placeholder="100"
          />
        </div>
      </div>
    </div>

    <!-- File Upload Section -->
    <div class="upload-section">
      <div class="form-group">
        <label for="file-upload">Upload Assessment File:</label>
        <div class="file-upload-area" :class="{ 'drag-over': isDragOver }" 
             @dragover.prevent="handleDragOver" 
             @dragleave.prevent="handleDragLeave"
             @drop.prevent="handleDrop">
          <input 
            type="file" 
            id="file-upload" 
            @change="handleFileUpload" 
            class="file-input"
            accept=".txt,.csv,.json,.docx,.pdf"
            ref="fileInput"
          />
          <div class="upload-content">
            <svg class="upload-icon" viewBox="0 0 24 24" width="48" height="48">
              <path fill="#666" d="M14,2H6A2,2 0 0,0 4,4V20A2,2 0 0,0 6,22H18A2,2 0 0,0 20,20V8L14,2M18,20H6V4H13V9H18V20Z" />
            </svg>
            <p v-if="!assessmentFile">
              Drop your assessment file here or <span class="upload-link">click to browse</span>
            </p>
            <p v-else class="file-selected">
              📄 {{ assessmentFile.name }} ({{ formatFileSize(assessmentFile.size) }})
            </p>
            <small>Supported formats: TXT, CSV, JSON, DOCX, PDF</small>
          </div>
        </div>
      </div>

      <!-- Template Format Guide -->
      <div v-if="selectedTemplate" class="template-guide">
        <h4>{{ getTemplateTitle(selectedTemplate) }} Format Guide:</h4>
        <div class="format-example">
          <pre>{{ getTemplateExample(selectedTemplate) }}</pre>
        </div>
      </div>
    </div>

    <!-- Answer Key Section (for MCQ and True/False) -->
    <div v-if="['multiple-choice', 'true-false'].includes(selectedTemplate)" class="answer-key-section">
      <div class="form-group">
        <label for="answer-key">Answer Key (Optional - for auto-grading):</label>
        <textarea 
          v-model="answerKey" 
          id="answer-key" 
          class="form-control"
          rows="4"
          placeholder="Enter correct answers (e.g., 1:A, 2:B, 3:C, 4:A, 5:D)"
        ></textarea>
        <small>Format: Question Number:Answer (separated by commas)</small>
      </div>
    </div>

    <!-- AI Grading Settings -->
    <div class="ai-settings">
      <h3>AI Grading Configuration</h3>
      <div class="form-row">
        <div class="form-group">
          <label>
            <input type="checkbox" v-model="aiGradingEnabled" />
            Enable AI-powered grading
          </label>
        </div>
        
        <div class="form-group" v-if="aiGradingEnabled">
          <label>
            <input type="checkbox" v-model="provideFeedback" />
            Generate detailed feedback for students
          </label>
        </div>
      </div>

      <div v-if="aiGradingEnabled" class="grading-criteria">
        <label for="grading-rubric">Grading Criteria (Optional):</label>
        <textarea 
          v-model="gradingRubric" 
          id="grading-rubric" 
          class="form-control"
          rows="3"
          placeholder="Specify grading criteria for better AI assessment..."
        ></textarea>
      </div>
    </div>

    <!-- Preview Section -->
    <div v-if="assessmentPreview" class="preview-section">
      <h3>Assessment Preview:</h3>
      <div class="preview-content">
        <div class="preview-meta">
          <span class="badge">{{ selectedTemplate.replace('-', ' ').toUpperCase() }}</span>
          <span class="file-info">{{ assessmentFile?.name }}</span>
        </div>
        <div class="preview-text">
          <pre>{{ assessmentPreview }}</pre>
        </div>
      </div>
    </div>

    <!-- Error Display -->
    <div v-if="error" class="error-message">
      <strong>Error:</strong> {{ error }}
    </div>

    <!-- Action Buttons -->
    <div class="action-buttons">
      <button @click="clearForm" class="btn-secondary">Clear Form</button>
      <button @click="submitAssessment" class="btn-submit" :disabled="!canSubmit || isLoading">
        <span v-if="isLoading">Processing...</span>
        <span v-else>Submit Assessment</span>
      </button>
    </div>
  </div>
</template>

<script>
import { ref, computed, onMounted } from 'vue';
import { useRouter } from 'vue-router';

export default {
  name: 'UploadAssessment',
  setup() {
    const router = useRouter();
    
    // Form data
    const assessmentTitle = ref('');
    const selectedTemplate = ref('multiple-choice');
    const subject = ref('');
    const duration = ref(60);
    const totalPoints = ref(100);
    const assessmentFile = ref(null);
    const answerKey = ref('');
    const aiGradingEnabled = ref(true);
    const provideFeedback = ref(true);
    const gradingRubric = ref('');
    
    // UI state
    const assessmentPreview = ref(null);
    const isLoading = ref(false);
    const isDragOver = ref(false);
    const error = ref('');
    const fileInput = ref(null);

    // Computed properties
    const canSubmit = computed(() => {
      return assessmentTitle.value.trim() && 
             assessmentFile.value && 
             !isLoading.value;
    });

    // File handling methods
    const handleFileUpload = (event) => {
      const file = event.target.files[0];
      processFile(file);
    };

    const handleDrop = (event) => {
      isDragOver.value = false;
      const file = event.dataTransfer.files[0];
      processFile(file);
    };

    const handleDragOver = () => {
      isDragOver.value = true;
    };

    const handleDragLeave = () => {
      isDragOver.value = false;
    };

    const processFile = (file) => {
      if (!file) return;
      
      // Validate file type
      const allowedTypes = ['.txt', '.csv', '.json', '.docx', '.pdf'];
      const fileExtension = '.' + file.name.split('.').pop().toLowerCase();
      
      if (!allowedTypes.includes(fileExtension)) {
        error.value = `Unsupported file type. Please use: ${allowedTypes.join(', ')}`;
        return;
      }

      // Validate file size (max 10MB)
      if (file.size > 10 * 1024 * 1024) {
        error.value = 'File size must be less than 10MB';
        return;
      }

      error.value = '';
      assessmentFile.value = file;
      
      // Preview for text files
      if (fileExtension === '.txt' || fileExtension === '.csv') {
        const reader = new FileReader();
        reader.onload = () => {
          assessmentPreview.value = reader.result.substring(0, 500) + '...'; // First 500 chars
        };
        reader.readAsText(file);
      } else {
        assessmentPreview.value = `File uploaded: ${file.name} (${formatFileSize(file.size)})`;
      }
    };

    const formatFileSize = (bytes) => {
      if (bytes === 0) return '0 Bytes';
      const k = 1024;
      const sizes = ['Bytes', 'KB', 'MB', 'GB'];
      const i = Math.floor(Math.log(bytes) / Math.log(k));
      return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
    };

    // Template methods
    const getTemplateTitle = (template) => {
      const titles = {
        'multiple-choice': 'Multiple Choice Questions',
        'true-false': 'True/False Questions',
        'short-answer': 'Short Answer Questions',
        'essay': 'Essay Questions',
        'mixed': 'Mixed Format'
      };
      return titles[template] || 'Assessment';
    };

    const getTemplateExample = (template) => {
      const examples = {
        'multiple-choice': `Question 1: What is 2 + 2?
A) 3
B) 4
C) 5
D) 6

Question 2: Which planet is closest to the sun?
A) Venus
B) Mercury
C) Earth
D) Mars`,
        
        'true-false': `Question 1: The Earth is flat. (False)
Question 2: Python is a programming language. (True)
Question 3: The sun rises in the west. (False)`,
        
        'short-answer': `Question 1: Explain the water cycle in 2-3 sentences.
Question 2: What are the three primary colors?
Question 3: Define photosynthesis.`,
        
        'essay': `Question 1: Discuss the impact of technology on modern education. (500 words)
Question 2: Analyze the causes and effects of climate change. (750 words)`,
        
        'mixed': `Section A: Multiple Choice
Question 1: What is the capital of France?
A) London B) Berlin C) Paris D) Madrid

Section B: Short Answer  
Question 2: Explain democracy in your own words.`
      };
      return examples[template] || 'Please format your questions according to the selected template.';
    };

    // Form methods
    const clearForm = () => {
      assessmentTitle.value = '';
      selectedTemplate.value = 'multiple-choice';
      subject.value = '';
      duration.value = 60;
      totalPoints.value = 100;
      assessmentFile.value = null;
      answerKey.value = '';
      gradingRubric.value = '';
      assessmentPreview.value = null;
      error.value = '';
      if (fileInput.value) {
        fileInput.value.value = '';
      }
    };

    const submitAssessment = async () => {
      if (!canSubmit.value) return;

      isLoading.value = true;
      error.value = '';

      try {
        const formData = new FormData();
        formData.append('title', assessmentTitle.value);
        formData.append('template', selectedTemplate.value);
        formData.append('subject', subject.value);
        formData.append('duration', duration.value.toString());
        formData.append('total_points', totalPoints.value.toString());
        formData.append('file', assessmentFile.value);
        formData.append('answer_key', answerKey.value);
        formData.append('ai_grading_enabled', aiGradingEnabled.value.toString());
        formData.append('provide_feedback', provideFeedback.value.toString());
        formData.append('grading_rubric', gradingRubric.value);

        const response = await fetch('http://127.0.0.1:8000/api/assessments/upload', {
          method: 'POST',
          headers: {
            'Authorization': `Bearer ${localStorage.getItem('auth_token')}`, // Add auth if needed
          },
          body: formData,
        });

        const result = await response.json();

        if (response.ok) {
          alert('Assessment uploaded successfully! AI grading has been initiated.');
          router.push('/teacher/dashboard');
        } else {
          error.value = result.detail || 'Failed to upload assessment';
        }
      } catch (err) {
        console.error('Upload error:', err);
        error.value = 'Network error. Please check your connection and try again.';
      } finally {
        isLoading.value = false;
      }
    };

    return {
      // Form data
      assessmentTitle,
      selectedTemplate,
      subject,
      duration,
      totalPoints,
      assessmentFile,
      answerKey,
      aiGradingEnabled,
      provideFeedback,
      gradingRubric,
      
      // UI state
      assessmentPreview,
      isLoading,
      isDragOver,
      error,
      fileInput,
      
      // Computed
      canSubmit,
      
      // Methods
      handleFileUpload,
      handleDrop,
      handleDragOver,
      handleDragLeave,
      formatFileSize,
      getTemplateTitle,
      getTemplateExample,
      clearForm,
      submitAssessment
    };
  }
};
</script>

<style scoped>
.upload-assessment-container {
  max-width: 900px;
  margin: 0 auto;
  padding: 2rem;
  background: #f8f9fa;
  min-height: 100vh;
}

.header {
  text-align: center;
  margin-bottom: 2rem;
}

.header h1 {
  color: #2c3e50;
  margin-bottom: 0.5rem;
}

.subtitle {
  color: #6c757d;
  font-size: 1.1rem;
}

.assessment-form, .upload-section, .answer-key-section, .ai-settings {
  background: white;
  padding: 2rem;
  border-radius: 12px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.1);
  margin-bottom: 2rem;
}

.form-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
}

.form-group {
  margin-bottom: 1.5rem;
}

.form-group label {
  display: block;
  font-weight: 600;
  margin-bottom: 0.5rem;
  color: #2c3e50;
}

.form-control {
  width: 100%;
  padding: 0.8rem;
  border: 2px solid #e9ecef;
  border-radius: 8px;
  font-size: 1rem;
  transition: border-color 0.3s ease;
}

.form-control:focus {
  outline: none;
  border-color: #4caf50;
  box-shadow: 0 0 0 3px rgba(76, 175, 80, 0.1);
}

.file-upload-area {
  border: 3px dashed #dee2e6;
  border-radius: 12px;
  padding: 3rem;
  text-align: center;
  transition: all 0.3s ease;
  cursor: pointer;
  position: relative;
}

.file-upload-area:hover, .file-upload-area.drag-over {
  border-color: #4caf50;
  background-color: #f8fff9;
}

.file-input {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  opacity: 0;
  cursor: pointer;
}

.upload-content {
  pointer-events: none;
}

.upload-icon {
  margin-bottom: 1rem;
  opacity: 0.5;
}

.upload-link {
  color: #4caf50;
  text-decoration: underline;
}

.file-selected {
  color: #4caf50;
  font-weight: 600;
}

.template-guide {
  margin-top: 2rem;
  padding: 1rem;
  background: #f8f9fa;
  border-radius: 8px;
  border-left: 4px solid #4caf50;
}

.format-example {
  background: white;
  padding: 1rem;
  border-radius: 6px;
  margin-top: 1rem;
}

.format-example pre {
  margin: 0;
  white-space: pre-wrap;
  font-family: 'Courier New', monospace;
  font-size: 0.9rem;
  color: #495057;
}

.ai-settings h3 {
  margin-bottom: 1rem;
  color: #2c3e50;
}

.grading-criteria {
  margin-top: 1rem;
}

.preview-section {
  background: white;
  padding: 2rem;
  border-radius: 12px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.1);
  margin-bottom: 2rem;
}

.preview-meta {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 1rem;
}

.badge {
  background: #4caf50;
  color: white;
  padding: 0.3rem 0.8rem;
  border-radius: 20px;
  font-size: 0.8rem;
  font-weight: 600;
}

.file-info {
  color: #6c757d;
  font-style: italic;
}

.preview-text {
  background: #f8f9fa;
  padding: 1rem;
  border-radius: 6px;
  max-height: 300px;
  overflow-y: auto;
}

.preview-text pre {
  margin: 0;
  white-space: pre-wrap;
  font-family: 'Courier New', monospace;
  font-size: 0.9rem;
}

.error-message {
  background: #f8d7da;
  color: #721c24;
  padding: 1rem;
  border-radius: 8px;
  margin-bottom: 1rem;
  border: 1px solid #f5c6cb;
}

.action-buttons {
  display: flex;
  gap: 1rem;
  justify-content: flex-end;
  margin-top: 2rem;
}

.btn-submit, .btn-secondary {
  padding: 0.8rem 2rem;
  border: none;
  border-radius: 8px;
  font-size: 1.1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
}

.btn-submit {
  background: #4caf50;
  color: white;
}

.btn-submit:hover:not(:disabled) {
  background: #45a049;
  transform: translateY(-2px);
}

.btn-submit:disabled {
  background: #cccccc;
  cursor: not-allowed;
}

.btn-secondary {
  background: #6c757d;
  color: white;
}

.btn-secondary:hover {
  background: #5a6268;
}

.loading-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0,0,0,0.5);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  z-index: 1000;
  color: white;
}

.loader {
  width: 50px;
  height: 50px;
  border: 5px solid #f3f3f3;
  border-top: 5px solid #4caf50;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin-bottom: 1rem;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

/* Mobile Responsive */
@media (max-width: 768px) {
  .upload-assessment-container {
    padding: 1rem;
  }
  
  .form-row {
    grid-template-columns: 1fr;
  }
  
  .action-buttons {
    flex-direction: column;
  }
  
  .file-upload-area {
    padding: 2rem 1rem;
  }
}
</style>