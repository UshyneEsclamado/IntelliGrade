<template>
  <div class="take-assignment-page">
    <!-- Header Section -->
    <div class="section-header-card">
      <div class="section-header-content">
        <div class="section-header-left">
          <div class="section-header-icon">
            <svg width="36" height="36" viewBox="0 0 24 24" fill="currentColor">
              <path d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/>
            </svg>
          </div>
          
          <div class="header-text">
            <h1 class="section-header-title">{{ subject.name }} - Assignments</h1>
            <p class="section-header-subtitle">{{ section.name }}</p>
            <p class="section-header-description">{{ studentInfo.full_name }} • Grade {{ studentInfo.grade_level }}</p>
          </div>
        </div>
        
        <div class="header-actions">
          <button @click="goBack" class="back-btn">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M20,11V13H8L13.5,18.5L12.08,19.92L4.16,12L12.08,4.08L13.5,5.5L8,11H20Z" />
            </svg>
            <span>Back to Subjects</span>
          </button>
        </div>
      </div>
    </div>

    <!-- Loading State -->
    <div v-if="loading" class="loading-container">
      <div class="spinner-large"></div>
      <p>Loading assignments...</p>
    </div>

    <!-- Assignment List View -->
    <div v-else-if="!selectedAssignment" class="main-content">
      <!-- Stats Overview -->
      <div class="stats-grid">
        <div class="stat-card">
          <div class="stat-value">{{ assignments.length }}</div>
          <div class="stat-label">Available Assignments</div>
        </div>
        <div class="stat-card">
          <div class="stat-value">{{ completedAssignments.length }}</div>
          <div class="stat-label">Completed</div>
        </div>
      </div>

      <!-- Assignments Categories -->
      <div class="assignments-section">
        <!-- New Assignments -->
        <div v-if="newAssignments.length > 0" class="assignment-category">
          <div class="category-header">
            <h2 class="category-title">
              <span class="category-icon">
                <svg width="20" height="20" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
                </svg>
              </span>
              New Assignments
            </h2>
            <span class="category-count">{{ newAssignments.length }}</span>
          </div>
          <div class="assignment-grid">
            <div v-for="assignment in newAssignments" :key="assignment.id" class="assignment-card new-assignment">
              <div class="assignment-badge new-badge">New</div>
              <div class="assignment-header">
                <h3 class="assignment-title">{{ assignment.title }}</h3>
                <div class="assignment-type">
                  <span class="type-icon">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                      <path d="M7 21h10a2 2 0 002-2V9.414a1 1 0 00-.293-.707l-5.414-5.414A1 1 0 0012.586 3H7a2 2 0 00-2 2v14a2 2 0 002 2z"/>
                    </svg>
                  </span>
                  <span>{{ formatAssignmentType(assignment.assignment_type) }}</span>
                </div>
              </div>
              <p class="assignment-description">{{ assignment.description || 'No description provided' }}</p>
              <div class="assignment-meta">
                <div class="meta-item">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
                  </svg>
                  <span>{{ assignment.total_points }} Points</span>
                </div>
                <div class="meta-item">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
                  </svg>
                  <span>{{ formatSubmissionType(assignment.submission_type) }}</span>
                </div>
              </div>
              <div class="assignment-due-date" :class="{ 'overdue': isOverdue(assignment.due_date) }">
                <span class="due-label">Due:</span>
                <span class="due-time">{{ formatPHTime(assignment.due_date) }}</span>
                <span v-if="isOverdue(assignment.due_date)" class="overdue-label">OVERDUE</span>
              </div>
              <div class="assignment-actions">
                <button @click="viewAssignmentDetails(assignment)" class="btn btn-primary">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/>
                    <path d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/>
                  </svg>
                  View Assignment
                </button>
              </div>
            </div>
          </div>
        </div>

        <!-- Past Assignments -->
        <div v-if="pastAssignments.length > 0" class="assignment-category">
          <div class="category-header">
            <h2 class="category-title">
              <span class="category-icon">
                <svg width="20" height="20" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C20.832 18.477 19.247 18 17.5 18c-1.746 0-3.332.477-4.5 1.253" />
                </svg>
              </span>
              Past Assignments
            </h2>
            <span class="category-count">{{ pastAssignments.length }}</span>
          </div>
          <div class="assignment-grid">
            <div v-for="assignment in pastAssignments" :key="assignment.id" class="assignment-card past-assignment">
              <div v-if="getSubmissionStatus(assignment) === 'graded'" class="assignment-badge completed-badge">Completed</div>
              <div v-else-if="getSubmissionStatus(assignment) === 'submitted'" class="assignment-badge submitted-badge">Submitted</div>
              <div v-else-if="isOverdue(assignment.due_date)" class="assignment-badge overdue-badge">Overdue</div>
              <div class="assignment-header">
                <h3 class="assignment-title">{{ assignment.title }}</h3>
                <div class="assignment-type">
                  <span class="type-icon">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                      <path d="M7 21h10a2 2 0 002-2V9.414a1 1 0 00-.293-.707l-5.414-5.414A1 1 0 0012.586 3H7a2 2 0 00-2 2v14a2 2 0 002 2z"/>
                    </svg>
                  </span>
                  <span>{{ formatAssignmentType(assignment.assignment_type) }}</span>
                </div>
              </div>
              <p class="assignment-description">{{ assignment.description || 'No description provided' }}</p>
              <div class="assignment-meta">
                <div class="meta-item">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
                  </svg>
                  <span>{{ assignment.total_points }} Points</span>
                </div>
              </div>
              <div v-if="getSubmission(assignment.id)?.score !== null && getSubmission(assignment.id)?.score !== undefined" class="assignment-result">
                <div class="result-score">
                  <span class="score-label">Your Score:</span>
                  <span class="score-value">{{ calculatePercentage(getSubmission(assignment.id).score, assignment.total_points) }}%</span>
                </div>
                <div class="result-details">
                  <span>{{ getSubmission(assignment.id).score }} / {{ assignment.total_points }} points</span>
                </div>
              </div>
              <div class="assignment-actions">
                <button @click="viewAssignmentDetails(assignment)" class="btn btn-secondary">
                  View Details
                </button>
              </div>
            </div>
          </div>
        </div>

        <!-- Empty State -->
        <div v-if="assignments.length === 0" class="empty-state">
          <div class="empty-icon">
            <svg width="48" height="48" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
            </svg>
          </div>
          <h3>No Assignments Available</h3>
          <p>There are no assignments available for this subject yet.</p>
        </div>
      </div>
    </div>

    <!-- Assignment Details View -->
    <div v-else-if="selectedAssignment" class="assignment-details-view">
      <div class="content-card slide-up">
        <div class="details-header">
          <button @click="selectedAssignment = null" class="back-link">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M15 19l-7-7 7-7"/>
            </svg>
            Back to Assignments
          </button>
          <div class="assignment-status-badge" :class="getAssignmentStatusClass()">
            {{ getAssignmentStatusText() }}
          </div>
        </div>

        <div class="details-content">
          <div class="details-main">
            <div class="assignment-info-card">
              <h1 class="details-title">{{ selectedAssignment.title }}</h1>
              <div class="assignment-type-display">
                <div class="type-icon">
                  <svg width="20" height="20" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 21h10a2 2 0 002-2V9.414a1 1 0 00-.293-.707l-5.414-5.414A1 1 0 0012.586 3H7a2 2 0 00-2 2v14a2 2 0 002 2z" />
                  </svg>
                </div>
                <div class="type-content">
                  <span class="type-label">Assignment Type</span>
                  <span class="type-value">{{ formatAssignmentType(selectedAssignment.assignment_type) }}</span>
                </div>
              </div>
              <p class="details-description">{{ selectedAssignment.description || 'No description provided' }}</p>
              
              <div class="info-grid">
                <div class="info-item">
                  <div class="info-icon">
                    <svg width="20" height="20" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                    </svg>
                  </div>
                  <div class="info-content">
                    <span class="info-label">Total Points</span>
                    <span class="info-value">{{ selectedAssignment.total_points }}</span>
                  </div>
                </div>
                <div class="info-item">
                  <div class="info-icon">
                    <svg width="20" height="20" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
                    </svg>
                  </div>
                  <div class="info-content">
                    <span class="info-label">Due Date</span>
                    <span class="info-value">{{ formatPHTime(selectedAssignment.due_date) }}</span>
                  </div>
                </div>
                <div class="info-item">
                  <div class="info-icon">
                    <svg width="20" height="20" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 21h10a2 2 0 002-2V9.414a1 1 0 00-.293-.707l-5.414-5.414A1 1 0 0012.586 3H7a2 2 0 00-2 2v14a2 2 0 002 2z" />
                    </svg>
                  </div>
                  <div class="info-content">
                    <span class="info-label">Submission Type</span>
                    <span class="info-value">{{ formatSubmissionType(selectedAssignment.submission_type) }}</span>
                  </div>
                </div>
              </div>

              <!-- Teacher Attachments -->
              <div v-if="selectedAssignment.attachments && selectedAssignment.attachments.length > 0" class="attachments-section">
                <h3 class="attachments-title">Assignment Materials</h3>
                <div class="attachments-list">
                  <a 
                    v-for="(attachment, index) in selectedAssignment.attachments" 
                    :key="index"
                    :href="attachment.url"
                    target="_blank"
                    class="attachment-item"
                  >
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                      <path d="M7 21h10a2 2 0 002-2V9.414a1 1 0 00-.293-.707l-5.414-5.414A1 1 0 0012.586 3H7a2 2 0 00-2 2v14a2 2 0 002 2z"/>
                    </svg>
                    <span class="attachment-name">{{ attachment.name }}</span>
                    <span class="attachment-size">{{ formatFileSize(attachment.size) }}</span>
                  </a>
                </div>
              </div>

              <!-- Submission Section -->
              <div class="submission-section">
                <h3 class="submission-title">Your Submission</h3>
                
                <!-- Existing Submission -->
                <div v-if="currentSubmission" class="existing-submission">
                  <div class="submission-status-card" :class="currentSubmission.status">
                    <div class="status-header">
                      <span class="status-label">Status:</span>
                      <span class="status-value">{{ formatSubmissionStatus(currentSubmission.status) }}</span>
                    </div>
                    <div v-if="currentSubmission.submitted_at" class="submission-date">
                      Submitted: {{ formatPHTime(currentSubmission.submitted_at) }}
                    </div>
                    <div v-if="currentSubmission.is_late" class="late-notice">
                      ⚠️ Submitted late - {{ currentSubmission.late_days }} day(s) after deadline
                      <span v-if="currentSubmission.penalty_applied > 0" class="penalty-info">
                        ({{ currentSubmission.penalty_applied }}% penalty applied)
                      </span>
                    </div>
                  </div>

                  <!-- Display submitted content -->
                  <div v-if="currentSubmission.text_content" class="submitted-text">
                    <h4>Your Text Submission:</h4>
                    <div class="text-content">{{ currentSubmission.text_content }}</div>
                  </div>

                  <div v-if="currentSubmission.link_url" class="submitted-link">
                    <h4>Your Link Submission:</h4>
                    <a :href="currentSubmission.link_url" target="_blank" class="link-value">{{ currentSubmission.link_url }}</a>
                  </div>

                  <div v-if="currentSubmission.attachments && currentSubmission.attachments.length > 0" class="submitted-files">
                    <h4>Your Files:</h4>
                    <div class="files-list">
                      <a 
                        v-for="(file, index) in currentSubmission.attachments" 
                        :key="index"
                        :href="file.url"
                        target="_blank"
                        class="file-item"
                      >
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                          <path d="M7 21h10a2 2 0 002-2V9.414a1 1 0 00-.293-.707l-5.414-5.414A1 1 0 0012.586 3H7a2 2 0 00-2 2v14a2 2 0 002 2z"/>
                        </svg>
                        <span>{{ file.name }}</span>
                      </a>
                    </div>
                  </div>

                  <!-- Grading Info -->
                  <div v-if="currentSubmission.status === 'graded'" class="grading-section">
                    <div class="grade-display">
                      <div class="grade-score">
                        <span class="score-label">Your Score:</span>
                        <span class="score-value">{{ currentSubmission.score }} / {{ selectedAssignment.total_points }}</span>
                        <span class="score-percentage">({{ calculatePercentage(currentSubmission.score, selectedAssignment.total_points) }}%)</span>
                      </div>
                    </div>
                    <div v-if="currentSubmission.feedback" class="teacher-feedback">
                      <h4>Teacher's Feedback:</h4>
                      <div class="feedback-content">{{ currentSubmission.feedback }}</div>
                    </div>
                    <div v-if="currentSubmission.graded_at" class="graded-date">
                      Graded on: {{ formatPHTime(currentSubmission.graded_at) }}
                    </div>
                  </div>
                </div>

                <!-- New Submission Form -->
                <div v-else-if="!isOverdue(selectedAssignment.due_date) || selectedAssignment.allow_late_submission" class="submission-form">
                  <!-- Text Entry -->
                  <div v-if="selectedAssignment.submission_type === 'text_entry'" class="form-group">
                    <label>Your Answer:</label>
                    <textarea
                      v-model="submissionData.text_content"
                      rows="8"
                      placeholder="Type your answer here..."
                      class="text-input"
                    ></textarea>
                  </div>

                  <!-- Link Submission -->
                  <div v-if="selectedAssignment.submission_type === 'link'" class="form-group">
                    <label>External Link:</label>
                    <input
                      v-model="submissionData.link_url"
                      type="url"
                      placeholder="https://example.com/your-work"
                      class="link-input"
                    />
                  </div>

                  <!-- File Upload -->
                  <div v-if="selectedAssignment.submission_type === 'file_upload'" class="form-group">
                    <label>Upload Files:</label>
                    <div class="upload-area" @click="triggerFileInput" @dragover.prevent @drop.prevent="handleFileDrop">
                      <input
                        type="file"
                        ref="fileInput"
                        @change="handleFileSelect"
                        multiple
                        accept=".pdf,.doc,.docx,.xls,.xlsx,.ppt,.pptx,.txt,.jpg,.jpeg,.png,.zip,.rar"
                        style="display: none"
                      />
                      <div class="upload-content">
                        <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                          <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path>
                          <polyline points="17 8 12 3 7 8"></polyline>
                          <line x1="12" y1="3" x2="12" y2="15"></line>
                        </svg>
                        <p class="upload-text">Click to upload or drag and drop</p>
                        <p class="upload-hint">PDF, DOC, XLS, PPT, TXT, Images, ZIP (Max 10MB each)</p>
                      </div>
                    </div>

                    <!-- Selected Files -->
                    <div v-if="selectedFiles.length > 0" class="selected-files">
                      <div v-for="(file, index) in selectedFiles" :key="index" class="file-preview">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                          <path d="M7 21h10a2 2 0 002-2V9.414a1 1 0 00-.293-.707l-5.414-5.414A1 1 0 0012.586 3H7a2 2 0 00-2 2v14a2 2 0 002 2z"/>
                        </svg>
                        <div class="file-info">
                          <span class="file-name">{{ file.name }}</span>
                          <span class="file-size">{{ formatFileSize(file.size) }}</span>
                        </div>
                        <button @click="removeFile(index)" class="remove-file">×</button>
                      </div>
                    </div>
                  </div>

                  <!-- Submit Button -->
                  <button 
                    @click="submitAssignment" 
                    :disabled="isSubmitting || !canSubmit"
                    class="btn btn-submit-assignment"
                  >
                    <div v-if="isSubmitting" class="spinner"></div>
                    <svg v-else width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                      <path d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
                    </svg>
                    <span>{{ isSubmitting ? 'Submitting...' : 'Submit Assignment' }}</span>
                  </button>

                  <div v-if="isOverdue(selectedAssignment.due_date) && selectedAssignment.allow_late_submission" class="late-warning">
                    ⚠️ This assignment is past due. Late penalty: {{ selectedAssignment.late_penalty }}% per day
                  </div>
                </div>

                <!-- Overdue Message -->
                <div v-else class="overdue-message">
                  <svg width="48" height="48" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/>
                  </svg>
                  <h3>Assignment Overdue</h3>
                  <p>This assignment is past the due date and late submissions are not allowed.</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { supabase } from '@/supabase.js'

const router = useRouter()
const route = useRoute()

// State
const loading = ref(true)
const studentInfo = ref({ full_name: 'Loading...', grade_level: '', student_id: null })
const subject = ref({ id: '', name: 'Subject' })
const section = ref({ id: '', name: '' })
const assignments = ref([])
const selectedAssignment = ref(null)
const submissions = ref([])
const currentSubmission = ref(null)

// Submission form data
const submissionData = ref({
  text_content: '',
  link_url: ''
})
const selectedFiles = ref([])
const fileInput = ref(null)
const isSubmitting = ref(false)

// Real-time subscription
let assignmentSubscription = null

// Utility Functions
const formatPHTime = (utcDateString) => {
  if (!utcDateString) return 'Not set'
  try {
    const utcDate = new Date(utcDateString)
    const options = {
      year: 'numeric',
      month: 'short',
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit',
      timeZone: 'Asia/Manila',
      hour12: true
    }
    return utcDate.toLocaleString('en-PH', options) + ' PHT'
  } catch (error) {
    console.error('Error formatting PH time:', error)
    return 'Invalid date'
  }
}

const formatAssignmentType = (type) => {
  const types = {
    'homework': 'Homework',
    'project': 'Project',
    'essay': 'Essay',
    'presentation': 'Presentation',
    'research': 'Research Paper',
    'lab': 'Lab Work',
    'other': 'Other'
  }
  return types[type] || type
}

const formatSubmissionType = (type) => {
  const types = {
    'file_upload': 'File Upload',
    'text_entry': 'Text Entry',
    'link': 'External Link',
    'physical': 'Physical Submission'
  }
  return types[type] || type
}

const formatSubmissionStatus = (status) => {
  const statuses = {
    'draft': 'Draft',
    'submitted': 'Submitted',
    'graded': 'Graded',
    'returned': 'Returned'
  }
  return statuses[status] || status
}

const formatFileSize = (bytes) => {
  if (!bytes || bytes === 0) return '0 Bytes'
  const k = 1024
  const sizes = ['Bytes', 'KB', 'MB', 'GB']
  const i = Math.floor(Math.log(bytes) / Math.log(k))
  return Math.round(bytes / Math.pow(k, i) * 100) / 100 + ' ' + sizes[i]
}

const isOverdue = (dueDate) => {
  if (!dueDate) return false
  return new Date(dueDate) < new Date()
}

const calculatePercentage = (score, total) => {
  if (!total || total === 0) return 0
  return Math.round((score / total) * 100)
}

// Helper Methods
const getSubmission = (assignmentId) => {
  return submissions.value.find(s => s.assignment_id === assignmentId)
}

const getSubmissionStatus = (assignment) => {
  const submission = getSubmission(assignment.id)
  if (!submission) return 'not_submitted'
  return submission.status
}

const getAssignmentStatusClass = () => {
  if (!selectedAssignment.value) return 'available'
  
  const submission = getSubmission(selectedAssignment.value.id)
  
  if (submission?.status === 'graded') return 'graded'
  if (submission?.status === 'submitted') return 'submitted'
  if (isOverdue(selectedAssignment.value.due_date)) {
    return selectedAssignment.value.allow_late_submission ? 'overdue-allowed' : 'overdue'
  }
  
  return 'available'
}

const getAssignmentStatusText = () => {
  if (!selectedAssignment.value) return 'Available'
  
  const submission = getSubmission(selectedAssignment.value.id)
  
  if (submission?.status === 'graded') return 'Graded'
  if (submission?.status === 'submitted') return 'Submitted - Awaiting Grade'
  if (isOverdue(selectedAssignment.value.due_date)) {
    return selectedAssignment.value.allow_late_submission 
      ? 'Overdue - Late Submission Allowed' 
      : 'Overdue - Closed'
  }
  
  return 'Available'
}

// Computed Properties
const newAssignments = computed(() => {
  const now = new Date()
  return assignments.value.filter(assignment => {
    const submission = getSubmission(assignment.id)
    const isNotSubmitted = !submission || submission.status === 'draft'
    const isNotOverdue = !assignment.due_date || new Date(assignment.due_date) > now
    return isNotSubmitted && isNotOverdue
  }).sort((a, b) => new Date(b.created_at) - new Date(a.created_at))
})

const pastAssignments = computed(() => {
  const now = new Date()
  return assignments.value.filter(assignment => {
    const submission = getSubmission(assignment.id)
    const isSubmitted = submission && submission.status !== 'draft'
    const isOverdue = assignment.due_date && new Date(assignment.due_date) <= now
    return isSubmitted || isOverdue
  }).sort((a, b) => new Date(b.created_at) - new Date(a.created_at))
})

const completedAssignments = computed(() => {
  return submissions.value.filter(s => s.status !== 'draft')
})

const canSubmit = computed(() => {
  if (!selectedAssignment.value) return false
  
  if (selectedAssignment.value.submission_type === 'text_entry') {
    return submissionData.value.text_content.trim().length > 0
  }
  if (selectedAssignment.value.submission_type === 'link') {
    return submissionData.value.link_url.trim().length > 0
  }
  if (selectedAssignment.value.submission_type === 'file_upload') {
    return selectedFiles.value.length > 0
  }
  return false
})

// Data Loading Methods
const loadStudentInfo = async () => {
  try {
    const { data: { session } } = await supabase.auth.getSession()
    if (!session?.user) {
      router.push('/login')
      return false
    }

    const { data: profile } = await supabase
      .from('profiles')
      .select('id, role')
      .eq('auth_user_id', session.user.id)
      .single()

    if (!profile || profile.role !== 'student') {
      alert('Student profile not found')
      return false
    }

    const { data: student } = await supabase
      .from('students')
      .select('*')
      .eq('profile_id', profile.id)
      .single()

    if (!student) {
      alert('Student information not found')
      return false
    }

    studentInfo.value = {
      full_name: student.full_name,
      grade_level: student.grade_level,
      student_id: student.id
    }

    return true
  } catch (error) {
    console.error('Error loading student info:', error)
    return false
  }
}

const loadRouteParams = () => {
  const subjectId = route.params.subjectId
  const sectionId = route.params.sectionId
  const subjectName = route.query.subjectName || 'Subject'
  const sectionName = route.query.sectionName || ''

  if (!subjectId || !sectionId) {
    console.error('Missing required route parameters')
    return false
  }

  subject.value = { id: subjectId, name: subjectName }
  section.value = { id: sectionId, name: sectionName }

  return true
}

const loadAssignments = async () => {
  try {
    console.log('📚 Fetching assignments...')
    console.log('🔍 Section ID:', section.value.id)
    console.log('🔍 Student ID:', studentInfo.value.student_id)

    // ✅ Fetch published assignments for this section
    const { data: assignmentsData, error: assignmentsError } = await supabase
      .from('assignments')
      .select('*')
      .eq('section_id', section.value.id)
      .eq('subject_id', subject.value.id)
      .eq('status', 'published')
      .order('created_at', { ascending: false })

    if (assignmentsError) {
      console.error('❌ Error fetching assignments:', assignmentsError)
      throw assignmentsError
    }

    console.log('✅ Assignments fetched:', assignmentsData?.length || 0)
    console.log('📋 Assignments data:', assignmentsData)

    assignments.value = assignmentsData || []
    
    // Load submissions after assignments are loaded
    await loadSubmissions()
    
  } catch (error) {
    console.error('❌ Error loading assignments:', error)
    alert('Failed to load assignments: ' + error.message)
  }
}

const loadSubmissions = async () => {
  try {
    if (assignments.value.length === 0) {
      console.log('⚠️ No assignments to load submissions for')
      submissions.value = []
      return
    }

    if (!studentInfo.value.student_id) {
      console.error('❌ No student ID available')
      return
    }

    console.log('📝 Fetching submissions for student:', studentInfo.value.student_id)
    console.log('📋 Assignment IDs:', assignments.value.map(a => a.id))

    const { data: submissionsData, error: submissionsError } = await supabase
      .from('assignment_submissions')
      .select('*')
      .eq('student_id', studentInfo.value.student_id)
      .in('assignment_id', assignments.value.map(a => a.id))

    if (submissionsError) {
      console.error('❌ Error fetching submissions:', submissionsError)
      throw submissionsError
    }

    console.log('✅ Submissions fetched:', submissionsData?.length || 0)
    console.log('📋 Submissions data:', submissionsData)

    submissions.value = submissionsData || []
    
  } catch (error) {
    console.error('❌ Error loading submissions:', error)
  }
}

// Real-time Subscription
const setupRealtimeSubscription = () => {
  if (!section.value.id || !subject.value.id) {
    console.warn('⚠️ Missing section or subject ID for subscription')
    return
  }

  console.log('📡 Setting up realtime subscription for section:', section.value.id)

  assignmentSubscription = supabase
    .channel(`section-${section.value.id}-assignments`)
    .on('postgres_changes', {
      event: '*',
      schema: 'public',
      table: 'assignments',
      filter: `section_id=eq.${section.value.id}`
    }, async (payload) => {
      console.log('📡 Assignment change detected:', payload.eventType)
      
      if (payload.eventType === 'INSERT') {
        // Only add if published
        if (payload.new.status === 'published') {
          console.log('✅ New published assignment added')
          assignments.value.unshift(payload.new)
        }
      } else if (payload.eventType === 'UPDATE') {
        const index = assignments.value.findIndex(a => a.id === payload.new.id)
        if (payload.new.status === 'published') {
          if (index !== -1) {
            console.log('✅ Assignment updated')
            assignments.value[index] = payload.new
          } else {
            console.log('✅ Assignment published, adding to list')
            assignments.value.unshift(payload.new)
          }
        } else {
          // If unpublished, remove from list
          if (index !== -1) {
            console.log('⚠️ Assignment unpublished, removing from list')
            assignments.value.splice(index, 1)
          }
        }
      } else if (payload.eventType === 'DELETE') {
        console.log('🗑️ Assignment deleted')
        assignments.value = assignments.value.filter(a => a.id !== payload.old.id)
      }
      
      await loadSubmissions()
    })
    .on('postgres_changes', {
      event: '*',
      schema: 'public',
      table: 'assignment_submissions',
      filter: `student_id=eq.${studentInfo.value.student_id}`
    }, async (payload) => {
      console.log('📡 Submission change detected:', payload.eventType)
      await loadSubmissions()
    })
    .subscribe((status) => {
      console.log('📡 Subscription status:', status)
    })
}

// Navigation Methods
const goBack = () => {
  router.push({
    name: 'StudentSubjects'
  })
}

const viewAssignmentDetails = (assignment) => {
  selectedAssignment.value = assignment
  currentSubmission.value = getSubmission(assignment.id)
  
  // Reset submission form
  submissionData.value = {
    text_content: '',
    link_url: ''
  }
  selectedFiles.value = []
}

// File Handling Methods
const triggerFileInput = () => {
  fileInput.value?.click()
}

const handleFileSelect = (event) => {
  const files = Array.from(event.target.files)
  addFiles(files)
}

const handleFileDrop = (event) => {
  const files = Array.from(event.dataTransfer.files)
  addFiles(files)
}

const addFiles = (files) => {
  const maxSize = 10 * 1024 * 1024 // 10MB
  const validFiles = files.filter(file => {
    if (file.size > maxSize) {
      alert(`${file.name} is too large. Maximum size is 10MB.`)
      return false
    }
    return true
  })
  selectedFiles.value.push(...validFiles)
}

const removeFile = (index) => {
  selectedFiles.value.splice(index, 1)
}

// File Upload Method
const uploadFiles = async () => {
  const uploadedFiles = []
  
  try {
    for (const file of selectedFiles.value) {
      const fileExt = file.name.split('.').pop()
      const fileName = `${studentInfo.value.student_id}/${Date.now()}_${Math.random().toString(36).substring(7)}.${fileExt}`
      
      console.log('📤 Uploading file:', fileName)
      
      const { data, error } = await supabase.storage
        .from('assignment-submissions')
        .upload(fileName, file)
      
      if (error) {
        console.error('❌ File upload error:', error)
        throw error
      }
      
      const { data: urlData } = supabase.storage
        .from('assignment-submissions')
        .getPublicUrl(fileName)
      
      uploadedFiles.push({
        name: file.name,
        url: urlData.publicUrl,
        size: file.size,
        type: file.type
      })
      
      console.log('✅ File uploaded:', fileName)
    }
    
    return uploadedFiles
  } catch (error) {
    console.error('❌ Error uploading files:', error)
    throw error
  }
}

// Assignment Submission Method
const submitAssignment = async () => {
  if (!canSubmit.value || !selectedAssignment.value || !studentInfo.value.student_id) {
    alert('Cannot submit assignment')
    return
  }

  isSubmitting.value = true

  try {
    console.log('📤 Submitting assignment...')

    const submissionPayload = {
      assignment_id: selectedAssignment.value.id,
      student_id: studentInfo.value.student_id,
      submission_type: selectedAssignment.value.submission_type,
      status: 'submitted',
      submitted_at: new Date().toISOString()
    }

    // Add content based on submission type
    if (selectedAssignment.value.submission_type === 'text_entry') {
      submissionPayload.text_content = submissionData.value.text_content.trim()
    } else if (selectedAssignment.value.submission_type === 'link') {
      submissionPayload.link_url = submissionData.value.link_url.trim()
    } else if (selectedAssignment.value.submission_type === 'file_upload') {
      // Upload files and get URLs
      const attachments = await uploadFiles()
      submissionPayload.attachments = attachments
    }

    console.log('📋 Submission payload:', submissionPayload)

    const { data, error } = await supabase
      .from('assignment_submissions')
      .insert([submissionPayload])
      .select()
      .single()

    if (error) {
      console.error('❌ Submission error:', error)
      throw error
    }

    console.log('✅ Submission successful:', data)

    alert('✅ Assignment submitted successfully!')

    // Reload submissions and go back
    await loadSubmissions()
    selectedAssignment.value = null

  } catch (error) {
    console.error('❌ Error submitting assignment:', error)
    alert('Failed to submit assignment: ' + error.message)
  } finally {
    isSubmitting.value = false
  }
}

// Lifecycle Hooks
onMounted(async () => {
  console.log('🔧 Component mounted - initializing...')
  
  const studentLoaded = await loadStudentInfo()
  if (!studentLoaded) {
    console.error('❌ Failed to load student info')
    router.push('/login')
    return
  }

  const paramsLoaded = loadRouteParams()
  if (!paramsLoaded) {
    console.error('❌ Failed to load route params')
    alert('Missing information')
    router.push('/student/subjects')
    return
  }

  console.log('📍 Route params:', {
    subjectId: subject.value.id,
    sectionId: section.value.id,
    subjectName: subject.value.name,
    sectionName: section.value.name
  })

  await loadAssignments()
  setupRealtimeSubscription()
  loading.value = false
  
  console.log('✅ Component initialization complete')
  console.log('📊 Final state:', {
    assignments: assignments.value.length,
    submissions: submissions.value.length
  })
})

onUnmounted(() => {
  console.log('🧹 Component unmounting - cleaning up...')
  
  if (assignmentSubscription) {
    supabase.removeChannel(assignmentSubscription)
    assignmentSubscription = null
  }
  
  console.log('✅ Cleanup complete')
})
</script>


<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

/* Main Container */
.take-assignment-page {
  min-height: 100vh;
  background: #FBFFE4;
  padding: 1.5rem;
  font-family: 'Inter', sans-serif;
}

.dark .take-assignment-page {
  background: #181c20;
}

/* Header Section */
.section-header-card {
  border: 2px solid #A3D1C6;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(61, 141, 122, 0.08);
  background: white;
  padding: 1.5rem;
  margin-bottom: 1.5rem;
}

.dark .section-header-card {
  background: #23272b;
  border: 1px solid #3D8D7A;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.25);
}

.section-header-content {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.section-header-left {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.section-header-icon {
  width: 56px;
  height: 56px;
  background: #3D8D7A;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
}

.section-header-title {
  font-size: 1.5rem;
  font-weight: 700;
  color: #1f2937;
  margin-bottom: 0.25rem;
}

.dark .section-header-title {
  color: #A3D1C6;
}

.section-header-subtitle {
  font-size: 0.875rem;
  color: #6b7280;
}

.dark .section-header-subtitle {
  color: #A3D1C6;
}

.section-header-description {
  font-size: 0.813rem;
  color: #94a3b8;
}

.dark .section-header-description {
  color: #A3D1C6;
}

.back-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem 1.25rem;
  border-radius: 8px;
  font-weight: 500;
  font-size: 0.875rem;
  transition: all 0.2s;
  cursor: pointer;
  border: 2px solid #20c997;
  background: #20c997;
  color: #181c20;
  box-shadow: 0 2px 8px rgba(61, 141, 122, 0.10);
}

.back-btn:hover {
  background: #A3D1C6;
  color: #23272b;
  border-color: #20c997;
  box-shadow: 0 4px 16px rgba(61, 141, 122, 0.18);
}

.dark .back-btn {
  background: #20c997;
  color: #181c20;
  border-color: #A3D1C6;
}

.dark .back-btn:hover {
  background: #A3D1C6;
  color: #23272b;
  border-color: #20c997;
}

/* Loading State */
.loading-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 400px;
  background: white;
  border-radius: 16px;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
}

.spinner-large {
  width: 48px;
  height: 48px;
  border: 4px solid #e5e7eb;
  border-top-color: #3D8D7A;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

.loading-container p {
  color: #718096;
  font-size: 1.1rem;
  margin: 0;
}

/* Main Content */
.main-content {
  background: white;
  border: 2px solid #A3D1C6;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(61, 141, 122, 0.08);
  overflow: hidden;
}

.dark .main-content {
  background: #23272b;
  border: 1px solid #3D8D7A;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.25);
}

/* Stats Grid */
.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1.5rem;
  margin-bottom: 2rem;
}

.stat-card {
  background: white;
  border: 2px solid #A3D1C6;
  border-radius: 12px;
  padding: 1.5rem;
  text-align: center;
  transition: all 0.2s;
  box-shadow: 0 2px 8px rgba(61, 141, 122, 0.08);
}

.stat-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 16px rgba(61, 141, 122, 0.12);
}

.dark .stat-card {
  background: #23272b;
  border: 1px solid #3D8D7A;
}

.stat-value {
  font-size: 2rem;
  font-weight: 700;
  color: #3D8D7A;
  margin-bottom: 0.5rem;
}

.dark .stat-value {
  color: #A3D1C6;
}

.stat-label {
  font-size: 0.875rem;
  color: #6b7280;
  font-weight: 500;
}

.dark .stat-label {
  color: #A3D1C6;
}

/* Assignments Section */
.assignments-section {
  padding: 32px;
}

.assignment-category {
  margin-bottom: 48px;
}

.assignment-category:last-child {
  margin-bottom: 0;
}

.category-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 24px;
  padding-bottom: 16px;
  border-bottom: 3px solid #e2e8f0;
}

.category-title {
  display: flex;
  align-items: center;
  gap: 12px;
  font-size: 1.5rem;
  font-weight: 700;
  color: #1a202c;
  margin: 0;
}

.category-icon {
  width: 32px;
  height: 32px;
  background: #3D8D7A;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
}

.category-count {
  background: #3D8D7A;
  color: white;
  padding: 8px 16px;
  border-radius: 20px;
  font-weight: 600;
  font-size: 0.875rem;
}

/* Assignment Grid */
.assignment-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(380px, 1fr));
  gap: 24px;
}

.assignment-card {
  background: white;
  border: 2px solid #e2e8f0;
  border-radius: 16px;
  padding: 24px;
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
}

.assignment-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 32px rgba(0, 0, 0, 0.1);
}

.assignment-card.new-assignment {
  border-color: #20c997;
  background: linear-gradient(135deg, #e6fffa, #b3f5e0);
}

.assignment-card.new-assignment:hover {
  border-color: #3D8D7A;
  box-shadow: 0 8px 32px rgba(61, 141, 122, 0.2);
}

.assignment-card.past-assignment {
  border-color: #A3D1C6;
  background: linear-gradient(135deg, #f8fdfc, #e6fffa);
}

.assignment-card.past-assignment:hover {
  border-color: #3D8D7A;
  box-shadow: 0 8px 32px rgba(61, 141, 122, 0.15);
}

.assignment-badge {
  position: absolute;
  top: 16px;
  right: 16px;
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 0.75rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.new-badge {
  background: #20c997;
  color: white;
}

.submitted-badge {
  background: #3D8D7A;
  color: white;
}

.graded-badge {
  background: #20c997;
  color: white;
}

.completed-badge {
  background: #20c997;
  color: white;
}

.overdue-badge {
  background: #dc3545;
  color: white;
}

.assignment-header {
  margin-bottom: 16px;
  padding-right: 80px;
}

.assignment-title {
  font-size: 1.25rem;
  font-weight: 700;
  color: #1a202c;
  margin: 0 0 8px 0;
  line-height: 1.3;
}

.assignment-type {
  display: flex;
  align-items: center;
  gap: 8px;
  color: #667eea;
  font-weight: 600;
  font-size: 0.875rem;
}

.type-icon {
  width: 20px;
  height: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.assignment-description {
  color: #718096;
  font-size: 0.9rem;
  line-height: 1.5;
  margin-bottom: 16px;
}

.assignment-meta {
  display: flex;
  gap: 20px;
  margin-bottom: 16px;
}

.meta-item {
  display: flex;
  align-items: center;
  gap: 6px;
  color: #4a5568;
  font-size: 0.875rem;
  font-weight: 500;
}

.assignment-due-date {
  padding: 12px;
  background: #f8fdfc;
  border-radius: 8px;
  border-left: 4px solid #3D8D7A;
  margin-bottom: 20px;
}

.assignment-due-date.overdue {
  background: #ffe6e6;
  border-left-color: #dc3545;
}

.due-label {
  font-weight: 600;
  color: #4a5568;
  margin-right: 8px;
}

.due-time {
  color: #1a202c;
  font-weight: 600;
}

.overdue-label {
  background: #dc3545;
  color: white;
  padding: 4px 8px;
  border-radius: 4px;
  font-size: 0.75rem;
  font-weight: 700;
  margin-left: 8px;
}

.assignment-score {
  background: #e6fffa;
  border: 2px solid #A3D1C6;
  border-radius: 8px;
  padding: 12px;
  margin-bottom: 20px;
}

.score-display {
  display: flex;
  align-items: center;
  gap: 12px;
  font-weight: 600;
}

.score-label {
  color: #4a5568;
}

.score-value {
  color: #3D8D7A;
  font-size: 1.1rem;
}

.score-percentage {
  color: #718096;
  font-size: 0.9rem;
}

.assignment-result {
  background: #e6fffa;
  border: 2px solid #A3D1C6;
  border-radius: 8px;
  padding: 12px;
  margin-bottom: 20px;
}

.result-score {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 4px;
  font-weight: 600;
}

.result-score .score-label {
  color: #4a5568;
}

.result-score .score-value {
  color: #3D8D7A;
  font-size: 1.1rem;
}

.result-details {
  color: #718096;
  font-size: 0.9rem;
}

.assignment-actions {
  display: flex;
  gap: 12px;
}

.btn {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 12px 20px;
  border-radius: 12px;
  font-weight: 600;
  font-size: 0.875rem;
  transition: all 0.2s ease;
  cursor: pointer;
  border: none;
  text-decoration: none;
}

.btn-primary {
  background: #20c997;
  color: white;
  border: 2px solid #20c997;
}

.btn-primary:hover {
  background: #3D8D7A;
  border-color: #3D8D7A;
  transform: translateY(-2px);
  box-shadow: 0 4px 16px rgba(61, 141, 122, 0.3);
}

.btn-secondary {
  background: white;
  color: #3D8D7A;
  border: 2px solid #A3D1C6;
}

.btn-secondary:hover {
  background: #A3D1C6;
  border-color: #3D8D7A;
  color: white;
  transform: translateY(-2px);
}

/* Empty State */
.empty-state {
  text-align: center;
  padding: 80px 40px;
  color: #718096;
}

.empty-icon {
  margin-bottom: 24px;
  opacity: 0.5;
}

.empty-state h3 {
  font-size: 1.5rem;
  color: #4a5568;
  margin-bottom: 12px;
}

.empty-state p {
  font-size: 1rem;
  margin: 0;
}

/* Assignment Details View */
.assignment-details-view {
  background: white;
  border-radius: 16px;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
  overflow: hidden;
}

.content-card {
  min-height: 100%;
}

.slide-up {
  animation: slideUp 0.3s ease-out;
}

@keyframes slideUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.details-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 24px 32px;
  border-bottom: 1px solid #e2e8f0;
  background: #f8fafc;
}

.back-link {
  display: flex;
  align-items: center;
  gap: 8px;
  color: #667eea;
  font-weight: 600;
  padding: 8px 16px;
  border-radius: 8px;
  transition: all 0.2s ease;
  cursor: pointer;
  background: none;
  border: none;
}

.back-link:hover {
  background: #edf2f7;
  transform: translateX(-4px);
}

.assignment-status-badge {
  padding: 8px 16px;
  border-radius: 20px;
  font-weight: 700;
  font-size: 0.875rem;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.assignment-status-badge.available {
  background: #c6f6d5;
  color: #22543d;
}

.assignment-status-badge.submitted {
  background: #bee3f8;
  color: #1a365d;
}

.assignment-status-badge.graded {
  background: #e9d8fd;
  color: #44337a;
}

.assignment-status-badge.overdue {
  background: #fed7d7;
  color: #742a2a;
}

.assignment-status-badge.overdue-allowed {
  background: #feebc8;
  color: #7b341e;
}

.details-content {
  padding: 32px;
}

.assignment-info-card {
  max-width: 800px;
  margin: 0 auto;
}

.details-title {
  font-size: 2rem;
  font-weight: 700;
  color: #1a202c;
  margin-bottom: 16px;
  line-height: 1.2;
}

.assignment-type-display {
  display: flex;
  align-items: center;
  gap: 16px;
  margin-bottom: 24px;
  padding: 20px;
  background: #f8fafc;
  border-radius: 12px;
  border: 2px solid #e2e8f0;
}

.assignment-type-display .type-icon {
  width: 40px;
  height: 40px;
  background: #3D8D7A;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  flex-shrink: 0;
}

.type-content {
  flex: 1;
}

.type-label {
  display: block;
  font-size: 0.875rem;
  color: #718096;
  font-weight: 500;
  margin-bottom: 4px;
}

.type-value {
  display: block;
  font-size: 1.1rem;
  color: #1a202c;
  font-weight: 600;
}

.details-description {
  font-size: 1.1rem;
  color: #4a5568;
  line-height: 1.6;
  margin-bottom: 32px;
  padding: 20px;
  background: #f8fafc;
  border-radius: 12px;
  border: 1px solid #e2e8f0;
}

.info-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 20px;
  margin-bottom: 32px;
}

.info-item {
  display: flex;
  align-items: center;
  gap: 16px;
  padding: 20px;
  background: #f8fafc;
  border-radius: 12px;
  border: 2px solid #e2e8f0;
  transition: all 0.2s ease;
}

.info-item:hover {
  border-color: #cbd5e0;
  transform: translateY(-2px);
}

.info-icon {
  width: 40px;
  height: 40px;
  background: #3D8D7A;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  flex-shrink: 0;
}

.info-content {
  flex: 1;
}

.info-label {
  display: block;
  font-size: 0.875rem;
  color: #6b7280;
  font-weight: 500;
  margin-bottom: 4px;
}

.dark .info-label {
  color: #A3D1C6;
}

.info-value {
  display: block;
  font-size: 1.1rem;
  color: #1f2937;
  font-weight: 600;
}

.dark .info-value {
  color: #A3D1C6;
}

/* Attachments Section */
.attachments-section {
  margin-bottom: 32px;
  padding: 24px;
  background: #f8fafc;
  border-radius: 12px;
  border: 2px solid #e2e8f0;
}

.attachments-title {
  font-size: 1.25rem;
  font-weight: 700;
  color: #1a202c;
  margin-bottom: 16px;
  display: flex;
  align-items: center;
  gap: 8px;
}

.attachments-title::before {
  content: '📎';
  font-size: 1.2rem;
}

.attachments-list {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.attachment-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px 16px;
  background: white;
  border: 2px solid #e2e8f0;
  border-radius: 8px;
  text-decoration: none;
  color: #4a5568;
  transition: all 0.2s ease;
}

.attachment-item:hover {
  border-color: #667eea;
  color: #667eea;
  transform: translateX(4px);
}

.attachment-name {
  font-weight: 600;
  flex: 1;
}

.attachment-size {
  font-size: 0.875rem;
  color: #718096;
}

/* Submission Section */
.submission-section {
  margin-top: 32px;
  padding: 32px;
  background: #f8fafc;
  border-radius: 16px;
  border: 3px solid #e2e8f0;
}

.submission-title {
  font-size: 1.5rem;
  font-weight: 700;
  color: #1a202c;
  margin-bottom: 24px;
  display: flex;
  align-items: center;
  gap: 12px;
}

.submission-title::before {
  content: '📝';
  font-size: 1.3rem;
}

/* Existing Submission */
.existing-submission {
  background: white;
  border-radius: 12px;
  padding: 24px;
  border: 2px solid #e2e8f0;
}

.submission-status-card {
  padding: 16px 20px;
  border-radius: 8px;
  margin-bottom: 20px;
}

.submission-status-card.submitted {
  background: #bee3f8;
  border: 2px solid #4299e1;
}

.submission-status-card.graded {
  background: #e9d8fd;
  border: 2px solid #9f7aea;
}

.status-header {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 8px;
}

.status-label {
  font-weight: 600;
  color: #4a5568;
}

.status-value {
  font-weight: 700;
  color: #1a202c;
}

.submission-date {
  font-size: 0.9rem;
  color: #718096;
  margin-bottom: 8px;
}

.late-notice {
  color: #d69e2e;
  font-weight: 600;
  font-size: 0.9rem;
}

.penalty-info {
  color: #e53e3e;
  font-weight: 700;
}

.submitted-text h4,
.submitted-link h4,
.submitted-files h4 {
  color: #4a5568;
  margin-bottom: 12px;
  font-size: 1.1rem;
}

.text-content {
  background: #f7fafc;
  padding: 16px;
  border-radius: 8px;
  border: 1px solid #e2e8f0;
  line-height: 1.6;
  color: #2d3748;
  white-space: pre-wrap;
}

.link-value {
  color: #667eea;
  text-decoration: none;
  font-weight: 600;
  padding: 8px 12px;
  background: #edf2f7;
  border-radius: 6px;
  display: inline-block;
}

.link-value:hover {
  background: #e2e8f0;
  text-decoration: underline;
}

.files-list {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.file-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px 16px;
  background: #f7fafc;
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  text-decoration: none;
  color: #4a5568;
  transition: all 0.2s ease;
}

.file-item:hover {
  background: #edf2f7;
  border-color: #cbd5e0;
  color: #667eea;
}

/* Grading Section */
.grading-section {
  margin-top: 24px;
  padding: 20px;
  background: #f0fff4;
  border: 2px solid #c6f6d5;
  border-radius: 12px;
}

.grade-display {
  margin-bottom: 16px;
}

.grade-score {
  display: flex;
  align-items: center;
  gap: 12px;
  font-size: 1.1rem;
  font-weight: 600;
}

.score-label {
  color: #4a5568;
}

.score-value {
  color: #38a169;
  font-size: 1.3rem;
  font-weight: 700;
}

.score-percentage {
  color: #718096;
}

.teacher-feedback {
  margin-bottom: 16px;
}

.teacher-feedback h4 {
  color: #4a5568;
  margin-bottom: 8px;
}

.feedback-content {
  background: white;
  padding: 16px;
  border-radius: 8px;
  border-left: 4px solid #38a169;
  color: #2d3748;
  line-height: 1.6;
  font-style: italic;
}

.graded-date {
  font-size: 0.9rem;
  color: #718096;
}

/* Submission Form */
.submission-form {
  background: white;
  border-radius: 12px;
  padding: 24px;
  border: 2px solid #e2e8f0;
}

.form-group {
  margin-bottom: 24px;
}

.form-group label {
  display: block;
  font-weight: 600;
  color: #4a5568;
  margin-bottom: 8px;
  font-size: 1rem;
}

.text-input,
.link-input {
  width: 100%;
  padding: 12px 16px;
  border: 2px solid #e2e8f0;
  border-radius: 8px;
  font-size: 1rem;
  transition: border-color 0.2s ease;
  font-family: inherit;
}

.text-input:focus,
.link-input:focus {
  outline: none;
  border-color: #667eea;
  box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
}

.text-input {
  resize: vertical;
  min-height: 120px;
  line-height: 1.5;
}

/* Upload Area */
.upload-area {
  border: 3px dashed #cbd5e0;
  border-radius: 12px;
  padding: 40px 20px;
  text-align: center;
  cursor: pointer;
  transition: all 0.2s ease;
  background: #f7fafc;
}

.upload-area:hover {
  border-color: #667eea;
  background: #edf2f7;
}

.upload-area.dragover {
  border-color: #667eea;
  background: #e6fffa;
}

.upload-content svg {
  margin-bottom: 16px;
  color: #718096;
}

.upload-text {
  font-size: 1.1rem;
  font-weight: 600;
  color: #4a5568;
  margin-bottom: 8px;
}

.upload-hint {
  font-size: 0.9rem;
  color: #718096;
  margin: 0;
}

/* Selected Files */
.selected-files {
  margin-top: 16px;
  background: #f8fafc;
  border-radius: 8px;
  padding: 16px;
  border: 1px solid #e2e8f0;
}

.file-preview {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px;
  background: white;
  border-radius: 8px;
  margin-bottom: 8px;
  border: 1px solid #e2e8f0;
}

.file-preview:last-child {
  margin-bottom: 0;
}

.file-info {
  flex: 1;
}

.file-name {
  font-weight: 600;
  color: #2d3748;
  display: block;
}

.file-size {
  font-size: 0.875rem;
  color: #718096;
}

.remove-file {
  width: 24px;
  height: 24px;
  background: #fed7d7;
  color: #e53e3e;
  border: none;
  border-radius: 50%;
  cursor: pointer;
  font-weight: 700;
  transition: all 0.2s ease;
}

.remove-file:hover {
  background: #feb2b2;
  transform: scale(1.1);
}

/* Submit Button */
.btn-submit-assignment {
  background: #20c997;
  color: white;
  padding: 16px 32px;
  font-size: 1.1rem;
  font-weight: 700;
  border: 2px solid #20c997;
  border-radius: 12px;
  cursor: pointer;
  transition: all 0.2s ease;
  display: flex;
  align-items: center;
  gap: 8px;
  justify-content: center;
  width: 100%;
  margin-bottom: 16px;
}

.btn-submit-assignment:hover:not(:disabled) {
  background: #3D8D7A;
  border-color: #3D8D7A;
  transform: translateY(-2px);
  box-shadow: 0 4px 16px rgba(61, 141, 122, 0.3);
}

.btn-submit-assignment:disabled {
  opacity: 0.6;
  cursor: not-allowed;
  transform: none;
}

.spinner {
  width: 20px;
  height: 20px;
  border: 2px solid rgba(255, 255, 255, 0.3);
  border-top: 2px solid white;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

.late-warning {
  background: #feebc8;
  border: 2px solid #f6ad55;
  border-radius: 8px;
  padding: 12px 16px;
  color: #7b341e;
  font-weight: 600;
  font-size: 0.9rem;
}

/* Overdue Message */
.overdue-message {
  text-align: center;
  padding: 40px;
  background: #fed7d7;
  border: 2px solid #fc8181;
  border-radius: 12px;
  color: #742a2a;
}

.overdue-message svg {
  margin-bottom: 16px;
  color: #e53e3e;
}

.overdue-message h3 {
  font-size: 1.5rem;
  font-weight: 700;
  margin-bottom: 8px;
}

.overdue-message p {
  font-size: 1rem;
  margin: 0;
}

/* Animations */
@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

/* Responsive Design */
@media (max-width: 768px) {
  .take-assignment-page {
    padding: 12px;
  }

  .section-header-content {
    flex-direction: column;
    gap: 20px;
    text-align: center;
    padding: 24px 20px;
  }

  .section-header-left {
    flex-direction: column;
    text-align: center;
  }

  .section-header-title {
    font-size: 1.5rem;
  }

  .stats-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 16px;
    padding: 20px;
  }

  .stat-card {
    padding: 16px;
  }

  .stat-value {
    font-size: 2rem;
  }

  .assignments-section {
    padding: 20px;
  }

  .assignment-grid {
    grid-template-columns: 1fr;
    gap: 16px;
  }

  .assignment-card {
    padding: 20px;
  }

  .assignment-header {
    padding-right: 70px;
  }

  .assignment-title {
    font-size: 1.1rem;
  }

  .details-content {
    padding: 20px;
  }

  .details-title {
    font-size: 1.5rem;
  }

  .info-grid {
    grid-template-columns: 1fr;
    gap: 16px;
  }

  .submission-section {
    padding: 20px;
  }

  .upload-area {
    padding: 30px 15px;
  }

  .details-header {
    padding: 20px;
    flex-direction: column;
    gap: 16px;
    text-align: center;
  }
}

@media (max-width: 480px) {
  .section-header-title {
    font-size: 1.25rem;
  }

  .stats-grid {
    grid-template-columns: 1fr;
    padding: 16px;
  }

  .assignment-grid {
    gap: 12px;
  }

  .assignment-card {
    padding: 16px;
  }

  .assignment-badge {
    position: static;
    display: inline-block;
    margin-bottom: 12px;
  }

  .assignment-header {
    padding-right: 0;
  }

  .details-content {
    padding: 16px;
  }

  .submission-section {
    padding: 16px;
  }
}
</style>