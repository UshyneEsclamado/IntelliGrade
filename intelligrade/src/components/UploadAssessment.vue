  <template>
    <div class="upload-page">
      <!-- Floating Gradient Blobs -->
      <div class="floating-shape shape1"></div>
      <div class="floating-shape shape2"></div>
      <div class="floating-shape shape3"></div>

      <!-- Header -->
      <div class="header-card">
        <div class="header-content">
          <div class="icon-wrapper">📝</div>
          <div>
            <h1>Upload Assessment</h1>
            <p>Create and upload assessments for automatic AI grading</p>
          </div>
        </div>
      </div>

      <!-- Loading Overlay -->
      <div v-if="isLoading" class="loading-overlay">
        <div class="loader"></div>
        <p>Processing assessment...</p>
      </div>

      <!-- Assessment Details -->
      <div class="card">
        <div class="card-header">
          <h2>Assessment Details</h2>
          <p>Start by providing the basic information for your assessment.</p>
        </div>
        <div class="card-body">
          <div class="form-group">
            <label for="assessment-title">Assessment Title</label>
            <input v-model="assessmentTitle" id="assessment-title" type="text" class="form-control"
              placeholder="e.g., Chapter 5 Biology Quiz" required />
          </div>

          <div class="form-row">
            <div class="form-group">
              <label for="template">Assessment Type</label>
              <select v-model="selectedTemplate" id="template" class="form-control">
                <option value="multiple-choice">Multiple Choice (MCQ)</option>
                <option value="true-false">True/False</option>
                <option value="short-answer">Short Answer</option>
                <option value="essay">Essay Questions</option>
                <option value="mixed">Mixed Format</option>
              </select>
            </div>

            <div class="form-group">
              <label for="subject">Subject</label>
              <input v-model="subject" id="subject" type="text" class="form-control"
                placeholder="e.g., Mathematics, Science" />
            </div>
          </div>

          <div class="form-row">
            <div class="form-group">
              <label for="duration">Duration (minutes)</label>
              <input v-model="duration" id="duration" type="number" class="form-control" min="1" max="300"
                placeholder="60" />
            </div>

            <div class="form-group">
              <label for="total-points">Total Points</label>
              <input v-model="totalPoints" id="total-points" type="number" class="form-control" min="1"
                placeholder="100" />
            </div>
          </div>
        </div>
      </div>

      <!-- Upload File -->
      <div class="card">
        <div class="card-header">
          <h2>Upload File</h2>
          <p>Attach the document containing the assessment questions.</p>
        </div>
        <div class="card-body">
          <div class="file-upload-area" :class="{ 'drag-over': isDragOver }" @dragover.prevent="handleDragOver"
            @dragleave.prevent="handleDragLeave" @drop.prevent="handleDrop" @click="$refs.fileInput.click()">
            <input type="file" id="file-upload" @change="handleFileUpload" class="file-input"
              accept=".txt,.csv,.json,.docx,.pdf" ref="fileInput" />
            <div class="upload-content">
              <svg class="upload-icon" fill="currentColor" viewBox="0 0 24 24" width="48" height="48">
                <path
                  d="M19.35 10.04C18.67 6.59 15.64 4 12 4 9.11 4 6.6 5.64 5.35 8.04 2.34 8.36 0 10.91 0 14c0 3.31 2.69 6 6 6h13c2.76 0 5-2.24 5-5 0-2.64-2.05-4.78-4.65-4.96zM14 13v4h-4v-4H7l5-5 5 5h-3z" />
              </svg>
              <p v-if="!assessmentFile">
                Drop your file here or <span class="upload-link">browse</span>
              </p>
              <p v-else class="file-selected">
                📄 {{ assessmentFile.name }} ({{ formatFileSize(assessmentFile.size) }})
              </p>
              <small>Supported formats: TXT, CSV, JSON, DOCX, PDF</small>
            </div>
          </div>

          <div v-if="selectedTemplate" class="template-guide">
            <h4>{{ getTemplateTitle(selectedTemplate) }} Format Guide:</h4>
            <div class="format-example">
              <pre>{{ getTemplateExample(selectedTemplate) }}</pre>
            </div>
          </div>
        </div>
      </div>

      <!-- Grading Configuration -->
      <div class="card">
        <div class="card-header">
          <h2>Grading Configuration</h2>
          <p>Set up the answer key and AI grading preferences.</p>
        </div>
        <div class="card-body grid-container">
          <div v-if="['multiple-choice', 'true-false'].includes(selectedTemplate)">
            <div class="form-group">
              <label for="answer-key">Answer Key (Optional)</label>
              <textarea v-model="answerKey" id="answer-key" class="form-control" rows="4"
                placeholder="e.g., 1:A, 2:B, 3:C"></textarea>
              <small>Format: QuestionNumber:Answer, separated by commas.</small>
            </div>
          </div>

          <div>
            <div class="form-group checkbox-group">
              <label>
                <input type="checkbox" v-model="aiGradingEnabled" />
                Enable AI-powered grading
              </label>
            </div>

            <div class="form-group checkbox-group" v-if="aiGradingEnabled">
              <label>
                <input type="checkbox" v-model="provideFeedback" />
                Generate detailed feedback
              </label>
            </div>

            <div v-if="aiGradingEnabled" class="form-group">
              <label for="grading-rubric">Grading Criteria (Optional)</label>
              <textarea v-model="gradingRubric" id="grading-rubric" class="form-control" rows="3"
                placeholder="e.g., Clarity: 40%, Accuracy: 60%"></textarea>
            </div>
          </div>
        </div>
      </div>

      <!-- Preview -->
      <div v-if="assessmentPreview" class="card">
        <div class="card-header">
          <h2>File Preview</h2>
        </div>
        <div class="card-body">
          <div class="preview-meta">
            <span class="badge">{{ selectedTemplate.replace('-', ' ').toUpperCase() }}</span>
            <span class="file-info">{{ assessmentFile?.name }}</span>
          </div>
          <div class="preview-text">
            <pre>{{ assessmentPreview }}</pre>
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
          <span v-else>Submit Assessment</span>
        </button>
      </div>
    </div>
  </template>

  <script>
  import { ref, computed, watch } from "vue";

  export default {
    name: "UploadAssessment",
    setup() {
      const isLoading = ref(false);
      const isDragOver = ref(false);
      const assessmentTitle = ref("");
      const selectedTemplate = ref("");
      const subject = ref("");
      const duration = ref(null);
      const totalPoints = ref(null);
      const assessmentFile = ref(null);
      const assessmentPreview = ref("");
      const answerKey = ref("");
      const aiGradingEnabled = ref(false);
      const provideFeedback = ref(false);
      const gradingRubric = ref("");
      const error = ref("");

      const handleFileUpload = (event) => {
        const file = event.target.files[0];
        if (file) {
          assessmentFile.value = file;
          readFile(file);
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
          readFile(file);
        }
        isDragOver.value = false;
      };

      const readFile = (file) => {
        const reader = new FileReader();
        reader.onload = (e) => {
          assessmentPreview.value = e.target.result.substring(0, 1000);
        };
        reader.readAsText(file);
      };

      const formatFileSize = (size) => {
        if (size < 1024) return size + " bytes";
        else if (size < 1048576) return (size / 1024).toFixed(1) + " KB";
        else return (size / 1048576).toFixed(1) + " MB";
      };

      const getTemplateTitle = (template) => {
        switch (template) {
          case "multiple-choice":
            return "Multiple Choice (MCQ)";
          case "true-false":
            return "True/False";
          case "short-answer":
            return "Short Answer";
          case "essay":
            return "Essay";
          case "mixed":
            return "Mixed Format";
          default:
            return "";
        }
      };

      const getTemplateExample = (template) => {
        switch (template) {
          case "multiple-choice":
            return "Q1. What is 2+2?\nA) 3\nB) 4\nC) 5\nAnswer: B";
          case "true-false":
            return "Q1. The Earth is flat.\nAnswer: False";
          case "short-answer":
            return "Q1. What is the capital of France?\nAnswer: Paris";
          case "essay":
            return "Q1. Explain the theory of evolution.\n[Student writes essay]";
          case "mixed":
            return "Q1. MCQ: 2+2=?\nA)3 B)4\nAnswer: B\nQ2. Short Answer: Capital of Italy?\nAnswer: Rome";
          default:
            return "";
        }
      };

      const clearForm = () => {
        assessmentTitle.value = "";
        selectedTemplate.value = "";
        subject.value = "";
        duration.value = null;
        totalPoints.value = null;
        assessmentFile.value = null;
        assessmentPreview.value = "";
        answerKey.value = "";
        aiGradingEnabled.value = false;
        provideFeedback.value = false;
        gradingRubric.value = "";
        error.value = "";
      };

      const submitAssessment = () => {
        if (!assessmentTitle.value || !assessmentFile.value || !selectedTemplate.value) {
          error.value = "Please fill all required fields and upload a file.";
          return;
        }
        isLoading.value = true;
        error.value = "";

        setTimeout(() => {
          isLoading.value = false;
          alert("Assessment submitted successfully!");
          clearForm();
        }, 2000);
      };

      const canSubmit = computed(() => {
        return assessmentTitle.value && selectedTemplate.value && assessmentFile.value;
      });

      watch(selectedTemplate, (newVal) => {
        if (newVal === "essay" || newVal === "short-answer") {
          aiGradingEnabled.value = true;
        }
      });

      return {
        isLoading,
        isDragOver,
        assessmentTitle,
        selectedTemplate,
        subject,
        duration,
        totalPoints,
        assessmentFile,
        assessmentPreview,
        answerKey,
        aiGradingEnabled,
        provideFeedback,
        gradingRubric,
        error,
        handleFileUpload,
        handleDragOver,
        handleDragLeave,
        handleDrop,
        formatFileSize,
        getTemplateTitle,
        getTemplateExample,
        clearForm,
        submitAssessment,
        canSubmit,
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


  </style>

