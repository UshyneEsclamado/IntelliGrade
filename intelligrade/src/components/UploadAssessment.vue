<template>
  <div class="upload-assessment-container">
    <h1>Upload Assessment</h1>

    <!-- Template Selection -->
    <div class="form-group">
      <label for="template">Select Assessment Template:</label>
      <select v-model="selectedTemplate" id="template" class="form-control">
        <option value="multiple-choice">Multiple Choice</option>
        <option value="true-false">True/False</option>
        <option value="short-answer">Short Answer</option>
      </select>
    </div>

    <!-- File Upload Section -->
    <div class="form-group">
      <label for="file-upload">Upload Assessment File:</label>
      <input type="file" id="file-upload" @change="handleFileUpload" class="form-control" />
    </div>

    <!-- Preview Section -->
    <div v-if="assessmentPreview" class="preview">
      <h3>Assessment Preview:</h3>
      <pre>{{ assessmentPreview }}</pre>
    </div>

    <!-- Submit Button -->
    <button @click="submitAssessment" class="btn-submit">Submit Assessment</button>
  </div>
</template>

<script>
import { ref } from 'vue';
import { useRouter } from 'vue-router';

export default {
  setup() {
    const router = useRouter();
    const selectedTemplate = ref('multiple-choice');
    const assessmentFile = ref(null);
    const assessmentPreview = ref(null);

    const handleFileUpload = (event) => {
      const file = event.target.files[0];
      if (file) {
        assessmentFile.value = file;
        const reader = new FileReader();
        reader.onload = () => {
          assessmentPreview.value = reader.result;
        };
        reader.readAsText(file);
      }
    };

    const submitAssessment = async () => {
      const formData = new FormData();
      formData.append('title', 'Sample Assessment');  // Example title, can be dynamic
      formData.append('template', selectedTemplate.value);
      formData.append('file', assessmentFile.value);

      try {
        const response = await fetch('http://127.0.0.1:8000/upload-assessment/', {
          method: 'POST',
          body: formData,
        });

        if (response.ok) {
          alert('Assessment uploaded and automatically graded!');
          router.push('/teacher/dashboard');  // Navigate back to dashboard after successful upload
        } else {
          alert('Error uploading assessment');
        }
      } catch (error) {
        console.error('Error uploading assessment:', error);
        alert('Error uploading assessment');
      }
    };

    return { selectedTemplate, handleFileUpload, assessmentPreview, submitAssessment };
  }
};
</script>

<style scoped>
/* Styles for the page */
.upload-assessment-container {
  padding: 2rem;
}

.form-group {
  margin-bottom: 1.5rem;
}

.form-control {
  width: 100%;
  padding: 1rem;
  margin-top: 0.5rem;
  border: 1px solid #ccc;
  border-radius: 8px;
}

.btn-submit {
  background-color: #4caf50;
  color: white;
  padding: 1rem 2rem;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  font-size: 1.2rem;
}

.preview {
  margin-top: 1.5rem;
}
</style>
