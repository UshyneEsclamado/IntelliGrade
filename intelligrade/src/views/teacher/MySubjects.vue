<template>
  <div class="subjects-page" :class="{ 'dark-mode': isDarkMode }">
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
              <path d="M12,3L1,9L12,15L21,10.09V17H23V9M5,13.18V17.18L12,21L19,17.18V13.18L12,17L5,13.18Z" />
            </svg>
          </div>
          
          <div class="header-text">
            <h1 class="section-header-title">My Subjects</h1>
            <p class="section-header-subtitle">Create and manage your class subjects with multiple sections</p>
            <p class="section-header-description">Organize your classes and track student progress</p>
          </div>
        </div>
        
        <div class="header-actions">
          <button @click="toggleDarkMode" class="dark-mode-toggle" :title="isDarkMode ? 'Switch to Light Mode' : 'Switch to Dark Mode'">
            <svg v-if="isDarkMode" width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M12,7A5,5 0 0,1 17,12A5,5 0 0,1 12,17A5,5 0 0,1 7,12A5,5 0 0,1 12,7M12,9A3,3 0 0,0 9,12A3,3 0 0,0 12,15A3,3 0 0,0 15,12A3,3 0 0,0 12,9M12,2L14.39,5.42C13.65,5.15 12.84,5 12,5C11.16,5 10.35,5.15 9.61,5.42L12,2M3.34,7L7.5,6.65C6.9,7.16 6.36,7.78 5.94,8.5C5.52,9.22 5.25,10 5.11,10.79L3.34,7M3.36,17L5.12,13.23C5.26,14 5.53,14.78 5.95,15.5C6.37,16.22 6.91,16.84 7.51,17.35L3.36,17M20.65,7L18.88,10.79C18.74,10 18.47,9.22 18.05,8.5C17.63,7.78 17.09,7.15 16.49,6.64L20.65,7M20.64,17L16.5,17.36C17.1,16.85 17.64,16.22 18.06,15.5C18.48,14.78 18.75,14 18.89,13.21L20.64,17M12,22L9.59,18.56C10.33,18.83 11.14,19 12,19C12.86,19 13.67,18.83 14.41,18.56L12,22Z" />
            </svg>
            <svg v-else width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M17.75,4.09L15.22,6.03L16.13,9.09L13.5,7.28L10.87,9.09L11.78,6.03L9.25,4.09L12.44,4L13.5,1L14.56,4L17.75,4.09M21.25,11L19.61,12.25L20.2,14.23L18.5,13.06L16.8,14.23L17.39,12.25L15.75,11L17.81,10.95L18.5,9L19.19,10.95L21.25,11M18.97,15.95C19.8,15.87 20.69,17.05 20.16,17.8C19.84,18.25 19.5,18.67 19.08,19.07C15.17,23 8.84,23 4.94,19.07C1.03,15.17 1.03,8.83 4.94,4.93C5.34,4.53 5.76,4.17 6.21,3.85C6.96,3.32 8.14,4.21 8.06,5.04C7.79,7.9 8.75,10.87 10.95,13.06C13.14,15.26 16.1,16.22 18.97,15.95M17.33,17.97C14.5,17.81 11.7,16.64 9.53,14.5C7.36,12.31 6.2,9.5 6.04,6.68C3.23,9.82 3.34,14.4 6.35,17.41C9.37,20.43 14,20.54 17.33,17.97Z" />
            </svg>
          </button>
          <button @click="showCreateModal = true" class="create-quiz-btn">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M19,13H13V19H11V13H5V11H11V5H13V11H19V13Z" />
            </svg>
            Create New Subject
          </button>
        </div>
      </div>
    </div>

    <div class="subjects-grid" v-if="subjects.length > 0">
      <div v-for="section in subjects" :key="section.section_id" class="section-card">
        <div class="section-header">
          <div class="section-info">
            <h3>{{ section.subject_name }}</h3>
            <p class="section-name">{{ section.section_name }}</p>
            <p class="grade-level">Grade {{ section.grade_level }}</p>
          </div>
          <div class="section-actions">
            <button @click="editSection(section)" class="action-btn edit" title="Edit Section">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                <path d="M20.71,7.04C21.1,6.65 21.1,6 20.71,5.63L18.37,3.29C18,2.9 17.35,2.9 16.96,3.29L15.12,5.12L18.87,8.87M3,17.25V21H6.75L17.81,9.93L14.06,6.18L3,17.25Z" />
              </svg>
            </button>
            <button @click="openDeleteModal('section', section)" class="action-btn delete" title="Delete Section">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                <path d="M19,4H15.5L14.5,3H9.5L8.5,4H5V6H19M6,19A2,2 0 0,0 8,21H16A2,2 0 0,0 18,19V7H6V19Z" />
              </svg>
            </button>
          </div>
        </div>

        <div class="section-stats">
          <div class="stat clickable-stat" @click="viewSectionStudents(section, section.sections[0])">
            <span class="stat-number">{{ section.student_count || 0 }}</span>
            <span class="stat-label">Students</span>
            <small class="view-hint">Click to view roster</small>
          </div>
          <div class="stat">
            <span class="stat-number">{{ section.max_students || 0 }}</span>
            <span class="stat-label">Max Students</span>
          </div>
          <div class="stat">
            <span class="stat-number">{{ section.grade_level }}</span>
            <span class="stat-label">Grade</span>
          </div>
        </div>

        <!-- Section Code Display -->
        <div class="section-code-area">
          <h4>Section Code:</h4>
          <div class="section-code-display">
            <span class="section-code">{{ section.section_code }}</span>
            <button @click.stop="copyCode(section.section_code, section.section_id)" class="copy-code-btn">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor">
                <path d="M19,21H8V7H19M19,5H8A2,2 0 0,0 6,7V21A2,2 0 0,0 8,23H19A2,2 0 0,0 21,21V7A2,2 0 0,0 19,5M16,1H4A2,2 0 0,0 2,3V17H4V3H16V1Z" />
              </svg>
              {{ copiedCodeId === section.section_id ? 'Copied!' : 'Copy' }}
            </button>
          </div>
        </div>
        
        <!-- Section Action Buttons -->
        <div class="section-actions-grid">
          <button 
            @click.stop="viewSectionStudents(section, section.sections[0])"
            class="section-action-btn view-students"
            title="View Students in Section"
          >
            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
              <path d="M16,4C18.21,4 20,5.79 20,8C20,10.21 18.21,12 16,12C13.79,12 12,10.21 12,8C12,5.79 13.79,4 16,4M16,14C20.42,14 24,15.79 24,18V20H8V18C8,15.79 11.58,14 16,14M6,6C7.1,6 8,6.9 8,8C8,9.1 7.1,10 6,10C4.9,10 4,9.1 4,8C4,6.9 4.9,6 6,6M6,12C8.67,12 12,13.34 12,16V18H0V16C0,13.34 3.33,12 6,12Z" />
            </svg>
            View Students
          </button>

          <button 
            @click.stop="navigateToCreateQuiz(section, section.sections[0])"
            class="section-action-btn create-quiz"
            title="Create Quiz/Assessment"
          >
            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
              <path d="M14,2H6A2,2 0 0,0 4,4V20A2,2 0 0,0 6,22H18A2,2 0 0,0 20,20V8L14,2M18,20H6V4H13V9H18V20Z" />
            </svg>
            Create Quiz
          </button>
          
          <button 
            @click.stop="viewQuizzes(section, section.sections[0])"
            class="section-action-btn view-quizzes"
            title="View Past Quizzes"
          >
            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
              <path d="M13,9V3.5L18.5,9M6,2C4.89,2 4,2.89 4,4V20A2,2 0 0,0 6,22H18A2,2 0 0,0 20,20V8L14,2H6Z" />
            </svg>
            View Quizzes
          </button>
          
          <button 
            @click.stop="manageGrades(section, section.sections[0])"
            class="section-action-btn manage-grades"
            title="Grade Management"
          >
            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
              <path d="M9,5A4,4 0 0,1 13,9A4,4 0 0,1 9,13A4,4 0 0,1 5,9A4,4 0 0,1 9,5M9,15C11.67,15 17,16.34 17,19V21H1V19C1,16.34 6.33,15 9,15M16.76,5.36C18.78,7.56 18.78,10.61 16.76,12.63L15.08,10.94C15.92,9.76 15.92,8.23 15.08,7.05L16.76,5.36M20.07,2C24,6.05 23.97,12.11 20.07,16.07L18.44,14.44C21.21,11.19 21.21,6.65 18.44,3.63L20.07,2Z" />
            </svg>
            Grades
          </button>
          
          <button 
            @click.stop="generateReports(section, section.sections[0])"
            class="section-action-btn generate-reports"
            title="Generate Reports"
          >
            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
              <path d="M13,9H18.5L13,3.5V9M6,2H14L20,8V20A2,2 0 0,1 18,22H6C4.89,22 4,21.1 4,20V4C4,2.89 4.89,2 6,2M15,18V16H6V18H15M18,14V12H6V14H18Z" />
            </svg>
            Reports
          </button>
          
          <button 
            @click.stop="viewAssessments(section, section.sections[0])"
            class="section-action-btn view-assessments"
            title="View Assessments"
          >
            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
              <path d="M14,2H6A2,2 0 0,0 4,4V20A2,2 0 0,0 6,22H18A2,2 0 0,0 20,20V8L14,2M18,20H6V4H13V9H18V20Z" />
            </svg>
            Assessments
          </button>
        </div>
      </div>
    </div>

    <div v-else class="empty-state">
      <div class="empty-icon">
        <svg width="64" height="64" viewBox="0 0 24 24" fill="currentColor">
          <path d="M12,3L1,9L12,15L21,10.09V17H23V9M5,13.18V17.18L12,21L19,17.18V13.18L12,17L5,13.18Z" />
        </svg>
      </div>
      <h3>No Subjects Created Yet</h3>
      <p>Create your first subject to start managing your classes and student sections</p>
      <button @click="showCreateModal = true" class="create-first-btn">
        Create Your First Subject
      </button>
    </div>

    <!-- Create/Edit Subject Modal -->
    <div v-if="showCreateModal" class="modal-overlay" @click="closeModal">
      <div class="modal-content" @click.stop>
        <div class="modal-header">
          <h2>{{ isEditing ? 'Edit Subject' : 'Create New Subject' }}</h2>
          <button @click="closeModal" class="close-btn">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
              <path d="M19,6.41L17.59,5L12,10.59L6.41,5L5,6.41L10.59,12L5,17.59L6.41,19L12,13.41L17.59,19L19,17.59L13.41,12L19,6.41Z" />
            </svg>
          </button>
        </div>

        <form @submit.prevent="currentStep === 1 ? nextStep() : saveSubject()" class="subject-form">
          <!-- Step 1: Basic Information -->
          <div v-if="currentStep === 1" class="step-content">
            <h3 class="step-title">Step 1: Subject Information</h3>
            
            <div class="form-group">
              <label for="subjectName">Subject Name *</label>
              <input
                id="subjectName"
                v-model="formData.name"
                type="text"
                placeholder="e.g., English, Mathematics, Science"
                required
              />
            </div>

            <div class="form-group">
              <label for="gradeLevel">Grade Level *</label>
              <select id="gradeLevel" v-model="formData.grade_level" required>
                <option value="">Select Grade Level</option>
                <option value="7">Grade 7</option>
                <option value="8">Grade 8</option>
                <option value="9">Grade 9</option>
                <option value="10">Grade 10</option>
                <option value="11">Grade 11</option>
                <option value="12">Grade 12</option>
              </select>
            </div>

            <div class="form-group">
              <label for="description">Description (Optional)</label>
              <textarea
                id="description"
                v-model="formData.description"
                placeholder="Brief description of the subject"
                rows="3"
              ></textarea>
            </div>

            <div class="form-group">
              <label for="numberOfSections">Number of Sections *</label>
              <select id="numberOfSections" v-model="formData.number_of_sections" required @change="generateSections">
                <option value="">Select Number of Sections</option>
                <option v-for="n in 10" :key="n" :value="n">{{ n }} Section{{ n > 1 ? 's' : '' }}</option>
              </select>
            </div>

            <div class="modal-actions">
              <button type="button" @click="closeModal" class="cancel-btn">Cancel</button>
              <button type="submit" :disabled="!canProceedToStep2" class="next-btn">
                Next: Setup Sections
                <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M4,11V13H16L10.5,18.5L11.92,19.92L19.84,12L11.92,4.08L10.5,5.5L16,11H4Z" />
                </svg>
              </button>
            </div>
          </div>

          <!-- Step 2: Section Setup -->
          <div v-if="currentStep === 2" class="step-content">
            <h3 class="step-title">Step 2: Setup Sections</h3>
            <p class="step-subtitle">Customize section names and unique codes will be generated automatically</p>

            <div class="sections-setup">
              <div v-for="(section, index) in formData.sections" :key="index" class="section-setup-item">
                <div class="section-number">{{ index + 1 }}</div>
                <div class="section-input">
                  <label :for="`section-${index}`">Section {{ index + 1 }} Name</label>
                  <input
                    :id="`section-${index}`"
                    v-model="section.name"
                    type="text"
                    :placeholder="`Section ${index + 1}`"
                    required
                  />
                  <input
                    v-model="section.max_students"
                    type="number"
                    min="1"
                    max="50"
                    placeholder="Max students (default: 40)"
                    style="margin-top: 0.5rem;"
                  />
                  <small class="section-code-preview">Code will be generated automatically</small>
                </div>
              </div>
            </div>

            <div class="modal-actions">
              <button type="button" @click="currentStep = 1" class="back-btn">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M20,11V13H8L13.5,18.5L12.08,19.92L4.16,12L12.08,4.08L13.5,5.5L8,11H20Z" />
                </svg>
                Back
              </button>
              <button type="submit" :disabled="isLoading" class="save-btn">
                {{ isLoading ? 'Creating...' : (isEditing ? 'Update Subject' : 'Create Subject') }}
              </button>
            </div>
          </div>
        </form>
      </div>
    </div>

    <!-- Student Roster Modal -->
    <div v-if="showStudentRosterModal && currentStudentRoster" class="modal-overlay" @click="closeStudentRosterModal">
      <div class="modal-content student-roster-modal" @click.stop>
        <div class="modal-header">
          <div>
            <h2>{{ currentStudentRoster.subject.name }} - Student Roster</h2>
            <p class="roster-subtitle">
              Grade {{ currentStudentRoster.subject.grade_level }} | 
              Total: {{ currentStudentRoster.totalActualStudents }} Students
            </p>
          </div>
          <button @click="closeStudentRosterModal" class="close-btn">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
              <path d="M19,6.41L17.59,5L12,10.59L6.41,5L5,6.41L10.59,12L5,17.59L6.41,19L12,13.41L17.59,19L19,17.59L13.41,12L19,6.41Z" />
            </svg>
          </button>
        </div>

        <div class="roster-content">
          <div v-if="Object.keys(currentStudentRoster.studentsBySection).length === 0" class="no-students">
            <div class="empty-icon">
              <svg width="64" height="64" viewBox="0 0 24 24" fill="currentColor">
                <path d="M16 4C18.2 4 20 5.8 20 8S18.2 12 16 12 12 10.2 12 8 13.8 4 16 4M16 14C20.4 14 24 15.8 24 18V20H8V18C8 15.8 11.6 14 16 14C10.5 14 9.2 14.3 8.5 14.8V11.5Z" />
              </svg>
            </div>
            <h3>No Students Enrolled</h3>
            <p>Students haven't joined any sections yet.</p>
          </div>

          <div v-else class="sections-roster">
            <div v-for="(sectionData, sectionKey) in currentStudentRoster.studentsBySection" :key="sectionKey" class="section-roster">
              <div class="section-roster-header">
                <h3>{{ sectionData.section.name }}</h3>
                <div class="section-details">
                  <span class="section-code">{{ sectionData.section.section_code }}</span>
                  <span class="student-count">{{ sectionData.students.length }} student{{ sectionData.students.length !== 1 ? 's' : '' }}</span>
                </div>
              </div>

              <div class="students-table">
                <div class="table-header">
                  <div class="col-id">Student ID</div>
                  <div class="col-name">Name</div>
                  <div class="col-email">Email</div>
                  <div class="col-grade">Grade</div>
                  <div class="col-date">Enrolled</div>
                </div>
                
                <div class="table-body">
                  <div v-for="student in sectionData.students" :key="student.id" class="student-row">
                    <div class="col-id">{{ student.student_id }}</div>
                    <div class="col-name">{{ student.full_name }}</div>
                    <div class="col-email">{{ student.email }}</div>
                    <div class="col-grade">{{ student.grade_level }}</div>
                    <div class="col-date">{{ formatEnrollmentDate(student.enrollment_date) }}</div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="roster-actions">
          <button @click="exportStudentRoster" class="export-btn">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
              <path d="M14,2H6A2,2 0 0,0 4,4V20A2,2 0 0,0 6,22H18A2,2 0 0,0 20,20V8L14,2M18,20H6V4H13V9H18V20Z" />
            </svg>
            Export List
          </button>
          <button @click="closeStudentRosterModal" class="close-roster-btn">Close</button>
        </div>
      </div>
    </div>

    <!-- Delete Confirmation Modal -->
    <template v-if="showDeleteModal">
      <div class="modal-overlay">
        <div class="modal-card">
          <div class="modal-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
              <path d="M12,2C13.1,2 14,2.9 14,4C14,5.1 13.1,6 12,6C10.9,6 10,5.1 10,4C10,2.9 10.9,2 12,2M21,9V7L15,1H5C3.89,1 3,1.89 3,3V7H9V9H3V19A2,2 0 0,0 5,21H19A2,2 0 0,0 21,19V9M6.5,18L10.5,14L6.5,10L8.5,8L14.5,14L8.5,20L6.5,18Z" />
            </svg>
          </div>
          <h3>Confirm Deletion</h3>
          <div class="item-details">
            <p class="item-name">
              <strong>
                {{ deleteType === 'subject' ? itemToDelete?.subject_name || itemToDelete?.name : 
                   `${itemToDelete?.subject_name} - ${itemToDelete?.section_name}` }}
              </strong>
            </p>
            <p class="item-info">
              {{ deleteType === 'subject' ? 'Subject' : 'Section' }} • 
              Grade {{ itemToDelete?.grade_level }}
              <template v-if="deleteType === 'section'">
                • {{ itemToDelete?.student_count || 0 }} students enrolled
              </template>
            </p>
          </div>
          <p class="warning-text">
            This action cannot be undone. All data will be permanently removed.
          </p>
          <div class="modal-actions">
            <button class="btn-cancel" @click="cancelDelete">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                <path d="M19,6.41L17.59,5L12,10.59L6.41,5L5,6.41L10.59,12L5,17.59L6.41,19L12,13.41L17.59,19L19,17.59L13.41,12L19,6.41Z" />
              </svg>
              Cancel
            </button>
            <button class="btn-delete" @click="confirmDelete">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                <path d="M19,4H15.5L14.5,3H9.5L8.5,4H5V6H19M6,19A2,2 0 0,0 8,21H16A2,2 0 0,0 18,19V7H6V19Z" />
              </svg>
              Delete
            </button>
          </div>
        </div>
      </div>
    </template>

    <!-- Success/Error Toast Notification -->
    <transition name="toast">
      <div v-if="showNotification" class="toast-notification" :class="`toast-${notificationType}`">
        <div class="toast-content">
          <div class="toast-icon">
            <svg v-if="notificationType === 'success'" width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M12,2A10,10 0 0,1 22,12A10,10 0 0,1 12,22A10,10 0 0,1 2,12A10,10 0 0,1 12,2M11,16.5L18,9.5L16.59,8.09L11,13.67L7.41,10.09L6,11.5L11,16.5Z" />
            </svg>
            <svg v-else-if="notificationType === 'error'" width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M12,2A10,10 0 0,1 22,12A10,10 0 0,1 12,22A10,10 0 0,1 2,12A10,10 0 0,1 12,2M12,7A1,1 0 0,0 11,8V16A1,1 0 0,0 12,17A1,1 0 0,0 13,16V8A1,1 0 0,0 12,7M12,19A1,1 0 0,0 11,20A1,1 0 0,0 12,21A1,1 0 0,0 13,20A1,1 0 0,0 12,19Z" />
            </svg>
            <svg v-else width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M13,13H11V7H13M13,17H11V15H13M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2Z" />
            </svg>
          </div>
          <span class="toast-message">{{ notificationMessage }}</span>
          <button @click="hideNotification" class="toast-close">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
              <path d="M19,6.41L17.59,5L12,10.59L6.41,5L5,6.41L10.59,12L5,17.59L6.41,19L12,13.41L17.59,19L19,17.59L13.41,12L19,6.41Z" />
            </svg>
          </button>
        </div>
      </div>
    </transition>

    <!-- Loading Overlay -->
    <div v-if="isLoading" class="loading-overlay">
      <div class="loading-content">
        <div class="loading-spinner"></div>
        <p>{{ loadingMessage }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed, nextTick, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'
import { supabase } from '../../supabase.js'
import { useDarkMode } from '../../composables/useDarkMode.js'

// Dark mode
const { isDarkMode, initDarkMode, toggleDarkMode } = useDarkMode()

// Router
const router = useRouter()

// State
const subjects = ref([])
const showCreateModal = ref(false)
const showStudentRosterModal = ref(false)
const currentStudentRoster = ref(null)
const isEditing = ref(false)
const isLoading = ref(false)
const loadingMessage = ref('')
const currentSubjectId = ref(null)
const currentStep = ref(1)
const copiedCodeId = ref(null)
const currentUser = ref(null)
const teacherInfo = ref(null)
const authListener = ref(null)
const isInitialized = ref(false)
const showDeleteModal = ref(false)
const deleteType = ref('') // 'subject' or 'section'
const itemToDelete = ref(null)
const showNotification = ref(false)
const notificationMessage = ref('')
const notificationType = ref('success') // 'success', 'error', 'warning'

// Form data
const formData = ref({
  name: '',
  grade_level: '',
  description: '',
  number_of_sections: '',
  sections: []
})

// Computed
const canProceedToStep2 = computed(() => {
  return formData.value.name && formData.value.grade_level && formData.value.number_of_sections
})

// Initialize authentication with new database structure
const initializeAuth = async () => {
  try {
    console.log('Initializing authentication...')
    
    // Get current session
    const { data: { session }, error: sessionError } = await supabase.auth.getSession()
    
    if (sessionError) {
      console.error('Session error:', sessionError)
      throw sessionError
    }
    
    if (!session?.user) {
      console.log('No active session found')
      await router.push('/login')
      return false
    }
    
    console.log('Session found for user:', session.user.id)
    currentUser.value = session.user
    
    // Get profile info first
    const { data: profile, error: profileError } = await supabase
      .from('profiles')
      .select('id, role, full_name, email')
      .eq('auth_user_id', session.user.id)
      .single()
    
    if (profileError) {
      console.error('Error getting profile:', profileError)
      
      if (profileError.code === 'PGRST116') {
        console.log('No profile found')
        alert('User profile not found. Please contact support.')
        await router.push('/login')
        return false
      }
      throw profileError
    }

    if (!profile) {
      console.log('No profile data returned')
      alert('User profile not found. Please contact support.')
      await router.push('/login')
      return false
    }

    if (profile.role !== 'teacher') {
      console.log('User is not a teacher:', profile.role)
      alert('Access denied. Teacher account required.')
      await router.push('/login')
      return false
    }

    // Now get the teacher record using the profile_id
    const { data: teacher, error: teacherError } = await supabase
      .from('teachers')
      .select('*')
      .eq('profile_id', profile.id)
      .eq('is_active', true)
      .single()

    if (teacherError) {
      console.error('Error getting teacher info:', teacherError)
      
      if (teacherError.code === 'PGRST116') {
        console.log('No teacher record found')
        alert('Teacher record not found. Please contact support.')
        await router.push('/login')
        return false
      }
      throw teacherError
    }

    teacherInfo.value = teacher
    console.log('Teacher info loaded:', teacherInfo.value.id)
    return true

  } catch (error) {
    console.error('Authentication initialization error:', error)
    alert(`Authentication error: ${error.message}`)
    await router.push('/login')
    return false
  }
}

// Setup auth state listener
const setupAuthListener = () => {
  if (authListener.value) {
    authListener.value.data.subscription.unsubscribe()
  }
  
  authListener.value = supabase.auth.onAuthStateChange(async (event, session) => {
    console.log('Auth state change:', event, session?.user?.id)
    
    if (event === 'SIGNED_OUT' || (event === 'TOKEN_REFRESHED' && !session)) {
      console.log('User signed out or token refresh failed')
      currentUser.value = null
      teacherInfo.value = null
      subjects.value = []
      isInitialized.value = false
      await router.push('/login')
    }
  })
}

// ASSESSMENT METHODS
// Navigation functions
const navigateToSections = async (subject, section, event) => {
  // Prevent navigation if clicking on buttons or other interactive elements
  if (event && (event.target.closest('button') || event.target.closest('.copy-code-btn'))) {
    return
  }
  
  try {
    await router.push({
      name: 'Sections',
      params: {
        subjectId: subject.id,
        sectionId: section.id
      },
      query: {
        subjectName: subject.name,
        sectionName: section.name,
        gradeLevel: subject.grade_level,
        sectionCode: section.section_code,
        studentCount: section.student_count || 0
      }
    })
  } catch (error) {
    console.error('Navigation error:', error)
  }
}

const navigateToCreateQuiz = async (subject, section) => {
  try {
    await router.push({
      name: 'CreateQuiz',
      params: {
        subjectId: subject.id,
        sectionId: section.id
      },
      query: {
        subjectName: subject.name,
        sectionName: section.name,
        gradeLevel: subject.grade_level,
        sectionCode: section.section_code
      }
    })
  } catch (error) {
    console.error('Navigation error:', error)
  }
}

const viewQuizzes = async (subject, section) => {
  try {
    await router.push({
      name: 'ViewQuizzes',
      params: {
        subjectId: subject.id,
        sectionId: section.id
      },
      query: {
        subjectName: subject.name,
        sectionName: section.name,
        gradeLevel: subject.grade_level,
        sectionCode: section.section_code
      }
    })
  } catch (error) {
    console.error('Navigation error:', error)
  }
}

const manageGrades = async (subject, section) => {
  try {
    await router.push({
      name: 'GradeManagement',
      params: {
        subjectId: subject.id,
        sectionId: section.id
      },
      query: {
        subjectName: subject.name,
        sectionName: section.name,
        gradeLevel: subject.grade_level,
        sectionCode: section.section_code
      }
    })
  } catch (error) {
    console.error('Navigation error:', error)
  }
}

const generateReports = async (subject, section) => {
  try {
    await router.push({
      name: 'Reports',
      params: {
        subjectId: subject.id,
        sectionId: section.id
      },
      query: {
        subjectName: subject.name,
        sectionName: section.name,
        gradeLevel: subject.grade_level,
        sectionCode: section.section_code
      }
    })
  } catch (error) {
    console.error('Navigation error:', error)
  }
}

const viewAssessments = async (subject, section) => {
  try {
    await router.push({
      name: 'Assessments',
      params: {
        subjectId: subject.subject_id,
        sectionId: subject.section_id
      },
      query: {
        subjectName: subject.subject_name,
        sectionName: subject.section_name,
        gradeLevel: subject.grade_level,
        sectionCode: subject.section_code
      }
    })
  } catch (error) {
    console.error('Navigation error:', error)
  }
}

// View students in a specific section
const viewSectionStudents = async (subject, section) => {
  try {
    await router.push({
      name: 'ViewStudents',
      params: {
        subjectId: subject.id,
        sectionId: section.id
      },
      query: {
        subjectName: subject.name,
        sectionName: section.name,
        gradeLevel: subject.grade_level,
        sectionCode: section.section_code
      }
    })
  } catch (error) {
    console.error('Navigation error:', error)
  }
}

// Fetch subjects with new database structure
const fetchSubjects = async (retryCount = 0) => {
  const maxRetries = 2
  
  try {
    if (!teacherInfo.value?.id) {
      console.log('No teacher info available, skipping fetch')
      return
    }

    if (retryCount === 0) {
      isLoading.value = true
      loadingMessage.value = 'Loading subjects...'
    }

    console.log('Fetching subjects for teacher:', teacherInfo.value.id)

    if (retryCount > 0) {
      await new Promise(resolve => setTimeout(resolve, 1000 * retryCount))
    }

    // Fetch subjects with sections using the new schema
    const { data: subjectsData, error: subjectsError } = await supabase
      .from('subjects')
      .select(`
        id,
        name,
        grade_level,
        description,
        is_active,
        created_at,
        sections (
          id,
          name,
          section_code,
          max_students,
          is_active
        )
      `)
      .eq('teacher_id', teacherInfo.value.id)
      .eq('is_active', true)
      .order('name')

    if (subjectsError) {
      console.error('Error fetching subjects:', subjectsError)
      
      if (subjectsError.code === 'PGRST301' || subjectsError.message?.includes('JWT')) {
        console.log('JWT error in fetch, trying to refresh session')
        
        const { error: refreshError } = await supabase.auth.refreshSession()
        if (refreshError) {
          console.error('Session refresh failed:', refreshError)
          await router.push('/login')
          return
        }
        
        if (retryCount < maxRetries) {
          console.log('Retrying fetch after session refresh')
          return await fetchSubjects(retryCount + 1)
        }
      }
      
      throw subjectsError
    }

    console.log('Subjects data:', subjectsData)

    // Process sections as individual cards instead of grouping under subjects
    const processedSections = []

    if (subjectsData && subjectsData.length > 0) {
      for (const subject of subjectsData) {
        // Process each section as an individual card
        if (subject.sections && subject.sections.length > 0) {
          for (const section of subject.sections) {
            if (section.is_active) {
              // Get enrollment count for this section
              const { count: enrollmentCount, error: countError } = await supabase
                .from('enrollments')
                .select('id', { count: 'exact' })
                .eq('section_id', section.id)
                .eq('status', 'active')

              if (countError) {
                console.error('Error getting enrollment count:', countError)
              }

              const studentCount = enrollmentCount || 0

              // Create individual section card with subject info
              processedSections.push({
                id: section.id,
                section_id: section.id,
                section_name: section.name,
                section_code: section.section_code,
                max_students: section.max_students,
                student_count: studentCount,
                actualStudentCount: studentCount,
                is_active: section.is_active,
                // Include subject information for each section
                subject_id: subject.id,
                subject_name: subject.name,
                grade_level: subject.grade_level,
                description: subject.description,
                name: `${subject.name} - ${section.name}`, // Combined name for display
                sections: [section] // Keep sections array for compatibility
              })
            }
          }
        }
      }
    }

    subjects.value = [...processedSections]
    console.log('Updated subjects array:', subjects.value.length, 'subjects')

    await nextTick()

  } catch (error) {
    console.error('Error in fetchSubjects:', error)
    
    if (error.code === 'PGRST301' || error.message?.includes('JWT')) {
      console.log('JWT/Auth error in fetchSubjects, redirecting to login')
      await router.push('/login')
      return
    }
    
    if (retryCount < maxRetries && (error.code === 'PGRST000' || error.message?.includes('network'))) {
      console.log(`Network error, retrying... (${retryCount + 1}/${maxRetries})`)
      return await fetchSubjects(retryCount + 1)
    }
    
    const errorMsg = `Unable to load subjects: ${error.message}\n\nPlease try refreshing the page or contact support if the problem persists.`
    alert(errorMsg)
  } finally {
    if (retryCount === 0) {
      isLoading.value = false
    }
  }
}

const getTotalStudents = (subject) => {
  return subject.actualStudentCount || 0
}

// View student roster with new schema
const viewStudentRoster = async (subject) => {
  try {
    if (!teacherInfo.value) {
      console.log('No teacher info available')
      return
    }

    isLoading.value = true
    loadingMessage.value = 'Loading student roster...'
    
    console.log('🔍 Loading student roster for subject:', subject.id)
    console.log('🔍 Teacher ID:', teacherInfo.value.id)

    // Use the new comprehensive view
    const { data: rosterData, error: rosterError } = await supabase
      .from('teacher_student_roster')
      .select('*')
      .eq('subject_id', subject.id)
      .eq('teacher_id', teacherInfo.value.id)

    if (rosterError) {
      console.error('❌ Error fetching roster data:', rosterError)
      throw rosterError
    }

    console.log('📊 Raw roster data from view:', rosterData)
    console.log('📊 Number of enrolled students found:', rosterData?.length || 0)

    // Get all sections for this subject (even empty ones)
    const { data: allSections, error: sectionsError } = await supabase
      .from('sections')
      .select('*')
      .eq('subject_id', subject.id)
      .eq('is_active', true)

    if (sectionsError) {
      console.error('❌ Error fetching sections:', sectionsError)
      throw sectionsError
    }

    console.log('📚 All sections for subject:', allSections)

    // Process the data
    const studentsBySection = {}
    let totalActualStudents = 0

    // Initialize all sections (including empty ones)
    if (allSections && allSections.length > 0) {
      allSections.forEach(section => {
        const sectionKey = `${section.name} (${section.section_code})`
        studentsBySection[sectionKey] = {
          section: section,
          students: []
        }
      })
    }

    // Add students to their respective sections
    if (rosterData && rosterData.length > 0) {
      rosterData.forEach(enrollment => {
        const studentInfo = {
          id: enrollment.student_id,
          student_id: enrollment.student_number || 'N/A',
          full_name: enrollment.student_name,
          email: enrollment.student_email,
          grade_level: enrollment.student_grade,
          enrollment_date: enrollment.enrolled_at
        }

        const sectionKey = `${enrollment.section_name} (${enrollment.section_code})`
        
        // Make sure the section exists in our structure
        if (!studentsBySection[sectionKey]) {
          studentsBySection[sectionKey] = {
            section: {
              id: enrollment.section_id,
              name: enrollment.section_name,
              section_code: enrollment.section_code,
              max_students: enrollment.max_students
            },
            students: []
          }
        }

        studentsBySection[sectionKey].students.push(studentInfo)
        totalActualStudents++
        
        console.log(`✅ Added student ${enrollment.student_name} to section ${sectionKey}`)
      })
    }

    console.log('📋 Final processed data:')
    console.log('- Total sections:', Object.keys(studentsBySection).length)
    console.log('- Total students:', totalActualStudents)
    console.log('- Students by section:', studentsBySection)

    currentStudentRoster.value = {
      subject,
      studentsBySection,
      totalActualStudents
    }
    
    showStudentRosterModal.value = true

  } catch (error) {
    console.error('❌ Error viewing student roster:', error)
    
    if (error.code === 'PGRST301' || error.message?.includes('JWT')) {
      await router.push('/login')
      return
    }
    
    alert(`Unable to load student roster: ${error.message}`)
  } finally {
    isLoading.value = false
  }
}

const generateSections = () => {
  const numSections = parseInt(formData.value.number_of_sections)
  formData.value.sections = []
  
  for (let i = 1; i <= numSections; i++) {
    formData.value.sections.push({
      name: `Section ${i}`,
      max_students: 40
    })
  }
}

const copyCode = async (code, codeId) => {
  try {
    await navigator.clipboard.writeText(code)
    copiedCodeId.value = codeId
    setTimeout(() => {
      copiedCodeId.value = null
    }, 2000)
    console.log('Copied section code:', code)
  } catch (err) {
    console.error('Failed to copy code:', err)
    const textArea = document.createElement('textarea')
    textArea.value = code
    document.body.appendChild(textArea)
    textArea.select()
    document.execCommand('copy')
    document.body.removeChild(textArea)
    copiedCodeId.value = codeId
    setTimeout(() => {
      copiedCodeId.value = null
    }, 2000)
  }
}

const nextStep = () => {
  if (canProceedToStep2.value) {
    generateSections()
    currentStep.value = 2
  }
}

// Save subject with new database structure
const saveSubject = async () => {
  try {
    if (!teacherInfo.value?.id) {
      alert('Please login to continue')
      return
    }

    isLoading.value = true
    loadingMessage.value = isEditing.value ? 'Updating subject...' : 'Creating subject...'

    console.log('Starting subject save process for teacher:', teacherInfo.value.id)

    // Prepare subject data
    const subjectData = {
      name: formData.value.name,
      grade_level: parseInt(formData.value.grade_level),
      teacher_id: teacherInfo.value.id,
      description: formData.value.description || null,
      is_active: true
    }

    let subjectId

    if (isEditing.value) {
      // Update existing subject
      const { data: updatedSubject, error: updateError } = await supabase
        .from('subjects')
        .update(subjectData)
        .eq('id', currentSubjectId.value)
        .eq('teacher_id', teacherInfo.value.id)
        .select()
        .single()

      if (updateError) {
        console.error('Update subject error:', updateError)
        throw updateError
      }
      
      subjectId = currentSubjectId.value
      console.log('Updated subject:', updatedSubject)

      // Delete existing sections for this subject
      const { error: deleteError } = await supabase
        .from('sections')
        .delete()
        .eq('subject_id', subjectId)

      if (deleteError) {
        console.error('Delete sections error:', deleteError)
        throw deleteError
      }

    } else {
      // Create new subject
      const { data: newSubject, error: insertError } = await supabase
        .from('subjects')
        .insert([subjectData])
        .select()
        .single()

      if (insertError) {
        console.error('Insert subject error:', insertError)
        throw insertError
      }
      
      subjectId = newSubject.id
      console.log('Created new subject:', newSubject)
    }

    // Create sections with generated codes
    const sectionsToInsert = []
    const createdSectionCodes = []
    
    // Generate section codes first
    for (let i = 0; i < formData.value.sections.length; i++) {
      const section = formData.value.sections[i]
      
      // Simple section code generation (fallback method)
      const subjectPrefix = formData.value.name.substring(0, 4).toUpperCase().replace(/[^A-Z]/g, '')
      const year = new Date().getFullYear()
      const timestamp = Date.now().toString().slice(-6) // Use 6 digits for more uniqueness
      const sectionCode = `${subjectPrefix}${formData.value.grade_level}-${year}-${timestamp}${String(i + 1).padStart(2, '0')}`
// 
//       console.log(`Generated section code for ${section.name}:`, sectionCode)
//       
      sectionsToInsert.push({
        subject_id: subjectId,
        name: section.name,
        section_code: sectionCode,
        max_students: parseInt(section.max_students) || 40,
        is_active: true
      })
      
      createdSectionCodes.push(`${section.name}: ${sectionCode}`)
    }

    console.log('Sections to insert:', sectionsToInsert)

    // Insert all sections
    const { data: insertedSections, error: sectionsError } = await supabase
      .from('sections')
      .insert(sectionsToInsert)
      .select()

    if (sectionsError) {
      console.error('Error inserting sections:', sectionsError)
      throw sectionsError
    }

    console.log('Successfully inserted sections:', insertedSections)

    closeModal()

    // Success message with section codes
    const sectionCodesText = createdSectionCodes.join('\n')
    alert(`Subject "${formData.value.name}" ${isEditing.value ? 'updated' : 'created'} successfully!\n\nSection Codes:\n${sectionCodesText}\n\nShare these codes with your students so they can join their respective sections.`)

    console.log('Subject saved successfully, refreshing list...')
    await fetchSubjects()

  } catch (error) {
    console.error('Error saving subject:', error)
    
    if (error.code === 'PGRST301' || error.message?.includes('JWT')) {
      alert('Your session has expired. Please log in again.')
      await router.push('/login')
      return
    }
    
    // More specific error handling
    let errorMessage = `Error ${isEditing.value ? 'updating' : 'creating'} subject:\n\n`
    
    if (error.message?.includes('duplicate key')) {
      errorMessage += 'A section with this code already exists. Please try again.'
    } else if (error.message?.includes('foreign key')) {
      errorMessage += 'Invalid teacher or subject reference. Please refresh and try again.'
    } else if (error.message?.includes('null value')) {
      errorMessage += 'Missing required information. Please check all fields are filled.'
    } else {
      errorMessage += error.message || 'An unexpected error occurred.'
    }
    
    alert(errorMessage)
  } finally {
    isLoading.value = false
  }
}

const editSubject = (subject) => {
  if (!teacherInfo.value) return

  isEditing.value = true
  currentSubjectId.value = subject.id
  formData.value = {
    name: subject.name,
    grade_level: subject.grade_level.toString(),
    description: subject.description || '',
    number_of_sections: subject.sections?.length.toString() || '1',
    sections: subject.sections?.map(s => ({ 
      name: s.name, 
      max_students: s.max_students || 40 
    })) || []
  }
  showCreateModal.value = true
  currentStep.value = 1
}

// Modal functions
const showToast = (message, type = 'success') => {
  notificationMessage.value = message
  notificationType.value = type
  showNotification.value = true
  
  // Auto-hide after 4 seconds
  setTimeout(() => {
    showNotification.value = false
  }, 4000)
}

const hideNotification = () => {
  showNotification.value = false
}

const openDeleteModal = (type, item) => {
  deleteType.value = type
  itemToDelete.value = item
  showDeleteModal.value = true
}

const cancelDelete = () => {
  showDeleteModal.value = false
  itemToDelete.value = null
  deleteType.value = ''
}

const confirmDelete = async () => {
  if (deleteType.value === 'subject') {
    await deleteSubjectConfirmed(itemToDelete.value.id)
  } else if (deleteType.value === 'section') {
    await deleteSectionConfirmed(itemToDelete.value.section_id)
  }
  showDeleteModal.value = false
  itemToDelete.value = null
  deleteType.value = ''
}

const deleteSubject = async (subjectId) => {
  try {
    if (!teacherInfo.value) return

    const subject = subjects.value.find(s => s.id === subjectId)
    // Removed confirm dialog - now handled by modal

    isLoading.value = true
    loadingMessage.value = 'Deleting subject...'

    console.log('Deleting subject:', subjectId)

    const { error } = await supabase
      .from('subjects')
      .delete()
      .eq('id', subjectId)
      .eq('teacher_id', teacherInfo.value.id)

    if (error) {
      console.error('Delete subject error:', error)
      throw error
    }

    console.log('Subject deleted successfully, refreshing list...')
    await fetchSubjects()
    alert(`Subject "${subject?.name}" deleted successfully!`)
  } catch (error) {
    console.error('Error deleting subject:', error)
    
    if (error.code === 'PGRST301' || error.message?.includes('JWT')) {
      alert('Your session has expired. Please log in again.')
      await router.push('/login')
      return
    }
    
    alert(`Error deleting subject: ${error.message}`)
  } finally {
    isLoading.value = false
  }
}

const editSection = (section) => {
  // For now, we'll edit by opening the subject edit modal
  // In a more advanced implementation, you could have a separate section edit modal
  const subjectData = {
    id: section.subject_id,
    name: section.subject_name,
    grade_level: section.grade_level,
    description: section.description || '',
    sections: section.sections
  }
  editSubject(subjectData)
}

// Separate confirmed delete functions
const deleteSubjectConfirmed = async (subjectId) => {
  try {
    if (!teacherInfo.value) return

    const subject = subjects.value.find(s => s.id === subjectId)
    isLoading.value = true
    loadingMessage.value = 'Deleting subject...'

    const { error } = await supabase
      .from('subjects')
      .delete()
      .eq('id', subjectId)
      .eq('teacher_id', teacherInfo.value.id)

    if (error) throw error
    await fetchSubjects()
    showToast(`Subject "${subject?.name}" deleted successfully!`, 'success')
  } catch (error) {
    if (error.code === 'PGRST301' || error.message?.includes('JWT')) {
      alert('Your session has expired. Please log in again.')
      await router.push('/login')
      return
    }
    alert(`Error deleting subject: ${error.message}`)
  } finally {
    isLoading.value = false
  }
}

const deleteSection = async (sectionId) => {
  try {
    if (!teacherInfo.value) return

    const section = subjects.value.find(s => s.section_id === sectionId)
    // Removed confirm dialog - now handled by modal

    isLoading.value = true
    loadingMessage.value = 'Deleting section...'

    console.log('Deleting section:', sectionId)

    const { error } = await supabase
      .from('sections')
      .delete()
      .eq('id', sectionId)

    if (error) {
      console.error('Delete section error:', error)
      throw error
    }

    console.log('Section deleted successfully, refreshing list...')
    await fetchSubjects()
    alert(`Section "${section?.section_name}" deleted successfully!`)
  } catch (error) {
    console.error('Error deleting section:', error)
    
    if (error.code === 'PGRST301' || error.message?.includes('JWT')) {
      alert('Your session has expired. Please log in again.')
      await router.push('/login')
      return
    }
    
    alert(`Error deleting section: ${error.message}`)
  } finally {
    isLoading.value = false
  }
}

const deleteSectionConfirmed = async (sectionId) => {
  try {
    if (!teacherInfo.value) return

    const section = subjects.value.find(s => s.section_id === sectionId)
    isLoading.value = true
    loadingMessage.value = 'Deleting section...'

    const { error } = await supabase
      .from('sections')
      .delete()
      .eq('id', sectionId)

    if (error) throw error
    await fetchSubjects()
    showToast(`Section "${section?.section_name}" deleted successfully!`, 'success')
  } catch (error) {
    if (error.code === 'PGRST301' || error.message?.includes('JWT')) {
      alert('Your session has expired. Please log in again.')
      await router.push('/login')
      return
    }
    alert(`Error deleting section: ${error.message}`)
  } finally {
    isLoading.value = false
  }
}

const closeModal = () => {
  showCreateModal.value = false
  isEditing.value = false
  currentSubjectId.value = null
  currentStep.value = 1
  formData.value = {
    name: '',
    grade_level: '',
    description: '',
    number_of_sections: '',
    sections: []
  }
}

const closeStudentRosterModal = () => {
  showStudentRosterModal.value = false
  currentStudentRoster.value = null
}

const formatEnrollmentDate = (dateString) => {
  if (!dateString) return 'N/A'
  try {
    const date = new Date(dateString)
    return date.toLocaleDateString('en-US', {
      year: 'numeric',
      month: 'short',
      day: 'numeric'
    })
  } catch {
    return 'Invalid Date'
  }
}

const exportStudentRoster = () => {
  if (!currentStudentRoster.value) return
  
  try {
    let csvContent = `Subject: ${currentStudentRoster.value.subject.name} (Grade ${currentStudentRoster.value.subject.grade_level})\n`
    csvContent += `Total Students: ${currentStudentRoster.value.totalActualStudents}\n\n`
    
    Object.keys(currentStudentRoster.value.studentsBySection).forEach(sectionKey => {
      const sectionData = currentStudentRoster.value.studentsBySection[sectionKey]
      csvContent += `Section: ${sectionData.section.name} (${sectionData.section.section_code})\n`
      csvContent += `Student ID,Full Name,Email,Grade,Enrollment Date\n`
      
      sectionData.students.forEach(student => {
        csvContent += `"${student.student_id}","${student.full_name}","${student.email}","${student.grade_level}","${formatEnrollmentDate(student.enrollment_date)}"\n`
      })
      csvContent += `\n`
    })
    
    const blob = new Blob([csvContent], { type: 'text/csv' })
    const url = window.URL.createObjectURL(blob)
    const a = document.createElement('a')
    a.href = url
    a.download = `${currentStudentRoster.value.subject.name}_Student_Roster.csv`
    document.body.appendChild(a)
    a.click()
    document.body.removeChild(a)
    window.URL.revokeObjectURL(url)
    
    console.log('Exported student roster successfully')
  } catch (error) {
    console.error('Error exporting roster:', error)
    alert('Error exporting roster. Please try again.')
  }
}

// Lifecycle
onMounted(async () => {
  console.log('Component mounted - My Subjects page')
  
  try {
    // Initialize dark mode
    initDarkMode()
    
    const authSuccess = await initializeAuth()
    
    if (!authSuccess) {
      console.log('Auth initialization failed')
      return
    }
    
    setupAuthListener()
    isInitialized.value = true
    await fetchSubjects()
    
    console.log('Component initialization complete')
    
  } catch (error) {
    console.error('Component mount error:', error)
    await router.push('/login')
  }
})

onUnmounted(() => {
  console.log('Component unmounting - cleaning up')
  if (authListener.value) {
    authListener.value.data.subscription.unsubscribe()
    authListener.value = null
  }
})
</script>

<style scoped>
/* Base Styles */
.subjects-page {
  padding: 2rem;
  max-width: 1400px;
  margin: 0 auto;
  background: var(--bg-primary);
  min-height: 100vh;
  color: var(--primary-text-color);
  transition: all 0.3s ease;
}

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

.dark-mode-toggle {
  background: rgba(255, 255, 255, 0.9);
  border: 2px solid rgba(79, 70, 229, 0.15);
  border-radius: 12px;
  padding: 0.75rem;
  cursor: pointer;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #10b981;
  width: 50px;
  height: 50px;
}

.dark-mode-toggle:hover {
  border-color: #10b981;
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(16, 185, 129, 0.2);
}

.subjects-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(450px, 1fr));
  gap: 2rem;
}

.subject-card,
.section-card {
  background: rgba(255, 255, 255, 0.95);
  border-radius: 20px;
  padding: 2rem;
  box-shadow: 0 8px 32px rgba(16, 185, 129, 0.1);
  border: 1px solid rgba(16, 185, 129, 0.1);
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
}

.subject-card::before,
.section-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 4px;
  background: linear-gradient(90deg, #10b981, #059669, #047857);
  border-radius: 20px 20px 0 0;
}

.subject-card:hover,
.section-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 16px 48px rgba(16, 185, 129, 0.2);
  border-color: rgba(16, 185, 129, 0.3);
}

.subject-header,
.section-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 2rem;
}

.subject-info h3,
.section-info h3 {
  color: #10b981;
  font-size: 1.5rem;
  font-weight: 700;
  margin-bottom: 0.5rem;
}

.section-info .section-name {
  color: #059669;
  font-size: 1.1rem;
  font-weight: 600;
  margin-bottom: 0.3rem;
  display: block;
}

.grade-level {
  background: linear-gradient(135deg, #10b981 0%, #059669 100%);
  color: white;
  padding: 0.3rem 1rem;
  border-radius: 20px;
  font-size: 0.85rem;
  font-weight: 600;
  display: inline-block;
  margin-bottom: 0.5rem;
}

.subject-actions,
.section-actions {
  display: flex;
  gap: 0.5rem;
}

.action-btn {
  padding: 0.6rem;
  border: none;
  border-radius: 12px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.action-btn.edit {
  background: rgba(16, 185, 129, 0.1);
  color: #10b981;
}

.action-btn.delete {
  background: rgba(239, 68, 68, 0.1);
  color: #ef4444;
}

.action-btn:hover {
  transform: scale(1.1);
}

.subject-stats,
.section-stats {
  display: flex;
  gap: 2rem;
  margin-bottom: 2rem;
  padding: 1.5rem;
  background: rgba(251, 255, 228, 0.7);
  border-radius: 16px;
}

.stat {
  text-align: center;
  flex: 1;
}

.stat-number {
  display: block;
  font-size: 2rem;
  font-weight: 800;
  color: #10b981;
  margin-bottom: 0.5rem;
}

.stat-label {
  font-size: 0.9rem;
  color: #666;
  font-weight: 600;
}

/* Clickable Student Stats */
.clickable-stat {
  cursor: pointer;
  transition: all 0.3s ease;
  border-radius: 12px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-weight: 600;
  flex-shrink: 0;
  padding: 0.5rem;
  position: relative;
}

.clickable-stat:hover {
  background: rgba(79, 70, 229, 0.1);
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(79, 70, 229, 0.2);
}

.clickable-stat .stat-number {
  font-size: 2rem;
  font-weight: 800;
  color: #10b981;
  margin-bottom: 0.25rem;
  transition: all 0.3s ease;
}

.clickable-stat:hover .stat-number {
  transform: scale(1.1);
}

.clickable-stat .stat-label {
  font-size: 0.9rem;
  color: #666;
  font-weight: 600;
  margin-bottom: 0.25rem;
}

.view-hint {
  display: block;
  color: #10b981;
  font-size: 0.7rem;
  margin-top: 0.2rem;
  font-weight: 500;
  text-align: center;
  opacity: 0;
  transition: opacity 0.3s ease;
}

.clickable-stat:hover .view-hint {
  opacity: 1;
}

.sections-list {
  margin-top: 1.5rem;
}

.sections-list h4 {
  color: #10b981;
  font-size: 1.2rem;
  font-weight: 700;
  margin-bottom: 1rem;
}

.sections {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.section-item {
  padding: 1rem;
  background: rgba(163, 209, 198, 0.1);
  border-radius: 12px;
  border: 1px solid rgba(16, 185, 129, 0.2);
}

/* Enhanced Section Styles */
.enhanced-section {
  background: white;
  border: 2px solid rgba(16, 185, 129, 0.1);
  border-radius: 16px;
  padding: 1.5rem;
  transition: all 0.3s ease;
  box-shadow: 0 2px 8px rgba(16, 185, 129, 0.05);
}

.enhanced-section:hover {
  border-color: rgba(16, 185, 129, 0.3);
  box-shadow: 0 8px 24px rgba(16, 185, 129, 0.15);
  transform: translateY(-2px);
}

.enhanced-section:hover .click-hint {
  opacity: 1;
  color: #10b981;
  font-weight: 500;
}

.section-header-info {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
  margin-bottom: 1rem;
}

.section-code-display {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.75rem;
  background: rgba(79, 70, 229, 0.05);
  border-radius: 10px;
  border: 1px solid rgba(79, 70, 229, 0.1);
}

.code-label {
  font-weight: 600;
  color: #10b981;
  font-size: 0.9rem;
}

.section-code {
  font-family: 'Courier New', monospace;
  font-weight: 700;
  color: #10b981;
  font-size: 1.1rem;
  background: white;
  padding: 0.5rem 0.75rem;
  border-radius: 6px;
  border: 1px solid rgba(79, 70, 229, 0.2);
  flex: 1;
}

.copy-code-btn {
  background: #10b981;
  color: white;
  border: none;
  padding: 0.5rem 0.75rem;
  border-radius: 6px;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 0.3rem;
  font-size: 0.8rem;
  font-weight: 600;
  transition: all 0.3s ease;
}

.copy-code-btn:hover {
  background: #2a6b5f;
  transform: scale(1.05);
}

.section-info {
  width: 100%;
}

.section-name {
  font-weight: 600;
  color: #10b981;
  font-size: 1.1rem;
  margin-bottom: 0.5rem;
  display: block;
}

.section-stats-info {
  margin-bottom: 1rem;
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}

.student-count {
  color: #666;
  font-size: 0.9rem;
}

.click-hint {
  color: #10b981;
  font-size: 0.8rem;
  font-style: italic;
  opacity: 0.7;
  transition: opacity 0.2s ease;
}

.section-code-area {
  margin-bottom: 1.5rem;
}

.section-code-area h4 {
  color: #10b981;
  font-size: 1rem;
  font-weight: 600;
  margin-bottom: 0.75rem;
}

.section-code-display {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1rem;
  background: rgba(16, 185, 129, 0.05);
  border: 1px solid rgba(16, 185, 129, 0.1);
  border-radius: 12px;
}

.section-code {
  font-family: 'Courier New', monospace;
  font-weight: 700;
  font-size: 1.1rem;
  color: #10b981;
  background: white;
  padding: 0.5rem 1rem;
  border-radius: 8px;
  border: 1px solid rgba(16, 185, 129, 0.2);
}

.copy-code-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem 1rem;
  background: #10b981;
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  font-size: 0.8rem;
  font-weight: 600;
  transition: all 0.3s ease;
}

.copy-code-btn:hover {
  background: #059669;
  transform: translateY(-1px);
}

.section-actions-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
  gap: 1rem;
  margin-top: 1rem;
}

.section-actions {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
  gap: 0.75rem;
  margin-bottom: 1rem;
}

.section-action-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  padding: 0.75rem 1rem;
  border: none;
  border-radius: 10px;
  cursor: pointer;
  font-weight: 600;
  font-size: 0.85rem;
  transition: all 0.3s ease;
  text-align: center;
  min-height: 44px;
}

.create-quiz {
  background: linear-gradient(135deg, #10b981 0%, #34d399 100%);
  color: white;
}

.create-quiz:hover {
  background: linear-gradient(135deg, #059669 0%, #10b981 100%);
  transform: translateY(-1px);
  box-shadow: 0 6px 20px rgba(16, 185, 129, 0.4);
}

.view-students {
  background: linear-gradient(135deg, #3b82f6 0%, #60a5fa 100%);
  color: white;
}

.view-students:hover {
  background: linear-gradient(135deg, #2563eb 0%, #3b82f6 100%);
  transform: translateY(-1px);
  box-shadow: 0 6px 20px rgba(59, 130, 246, 0.4);
}

.view-quizzes {
  background: linear-gradient(135deg, #14b8a6 0%, #5eead4 100%);
  color: white;
}

.view-quizzes:hover {
  background: linear-gradient(135deg, #0f766e 0%, #14b8a6 100%);
  transform: translateY(-1px);
  box-shadow: 0 6px 20px rgba(20, 184, 166, 0.4);
}

.manage-grades {
  background: linear-gradient(135deg, #ea580c 0%, #fb923c 100%);
  color: white;
}

.manage-grades:hover {
  background: linear-gradient(135deg, #c2410c 0%, #ea580c 100%);
  transform: translateY(-1px);
  box-shadow: 0 6px 20px rgba(234, 88, 12, 0.4);
}

.generate-reports {
  background: linear-gradient(135deg, #7c3aed 0%, #a855f7 100%);
  color: white;
}

.generate-reports:hover {
  background: linear-gradient(135deg, #5b21b6 0%, #7c3aed 100%);
  transform: translateY(-1px);
  box-shadow: 0 6px 20px rgba(124, 58, 237, 0.4);
}

.view-assessments {
  background: linear-gradient(135deg, #eab308 0%, #facc15 100%);
  color: white;
}

.view-assessments:hover {
  background: linear-gradient(135deg, #ca8a04 0%, #eab308 100%);
  transform: translateY(-1px);
  box-shadow: 0 6px 20px rgba(234, 179, 8, 0.4);
}

/* Empty State */
.empty-state {
  text-align: center;
  padding: 4rem 2rem;
  color: #666;
}

.empty-icon {
  color: #A3D1C6;
  margin-bottom: 2rem;
}

.empty-state h3 {
  color: #10b981;
  font-size: 1.5rem;
  font-weight: 700;
  margin-bottom: 1rem;
}

.empty-state p {
  font-size: 1.1rem;
  margin-bottom: 2rem;
}

.create-first-btn {
  background: linear-gradient(135deg, #10b981 0%, #059669 100%);
  color: white;
  border: none;
  padding: 1rem 2rem;
  border-radius: 16px;
  font-weight: 600;
  cursor: pointer;
  font-size: 1rem;
  transition: all 0.3s ease;
}

.create-first-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 12px 32px rgba(61, 141, 122, 0.3);
}

/* Modal Styles */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.6);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
  padding: 2rem;
  backdrop-filter: blur(4px);
}

.modal-content {
  background: white;
  border-radius: 20px;
  padding: 2rem;
  max-width: 600px;
  width: 100%;
  max-height: 90vh;
  overflow-y: auto;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
  position: relative;
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 2rem;
  padding-bottom: 1rem;
  border-bottom: 2px solid rgba(79, 70, 229, 0.1);
}

.modal-header h2 {
  color: #10b981;
  font-size: 1.8rem;
  font-weight: 700;
  margin: 0;
}

.close-btn {
  background: rgba(239, 68, 68, 0.1);
  color: #ef4444;
  border: none;
  padding: 0.5rem;
  border-radius: 10px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.close-btn:hover {
  background: rgba(239, 68, 68, 0.2);
  transform: scale(1.1);
}

.subject-form {
  width: 100%;
}

.step-content {
  animation: slideIn 0.3s ease;
}

@keyframes slideIn {
  from {
    opacity: 0;
    transform: translateX(20px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

.step-title {
  color: #10b981;
  font-size: 1.4rem;
  font-weight: 700;
  margin-bottom: 0.5rem;
}

.step-subtitle {
  color: #666;
  margin-bottom: 2rem;
}

.form-group {
  margin-bottom: 1.5rem;
}

.form-group label {
  display: block;
  font-weight: 600;
  color: #10b981;
  margin-bottom: 0.5rem;
}

.form-group input,
.form-group select {
  width: 100%;
  padding: 0.75rem;
  border: 2px solid rgba(61, 141, 122, 0.2);
  border-radius: 10px;
  font-size: 1rem;
  transition: all 0.3s ease;
  background: white;
}

.form-group input:focus,
.form-group select:focus {
  outline: none;
  border-color: #3D8D7A;
  box-shadow: 0 0 0 3px rgba(61, 141, 122, 0.1);
}

.sections-setup {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  max-height: 300px;
  overflow-y: auto;
  padding: 1rem;
  background: rgba(251, 255, 228, 0.3);
  border-radius: 12px;
  border: 1px solid rgba(61, 141, 122, 0.1);
}

.section-setup-item {
  display: flex;
  align-items: flex-start;
  gap: 1rem;
  padding: 1rem;
  background: white;
  border-radius: 10px;
  border: 1px solid rgba(61, 141, 122, 0.1);
}

.section-number {
  background: #3D8D7A;
  color: white;
  width: 32px;
  height: 32px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 0.9rem;
  flex-shrink: 0;
}

.section-input {
  flex: 1;
}

.section-input label {
  margin-bottom: 0.5rem;
  font-size: 0.9rem;
}

.section-code-preview {
  color: #666;
  font-size: 0.8rem;
  font-family: 'Courier New', monospace;
  margin-top: 0.5rem;
  display: block;
}

.modal-actions {
  display: flex;
  gap: 1rem;
  justify-content: flex-end;
  margin-top: 2rem;
}

.cancel-btn, .back-btn {
  background: transparent;
  color: #666;
  border: 2px solid #ddd;
  padding: 0.75rem 1.5rem;
  border-radius: 10px;
  cursor: pointer;
  font-weight: 600;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.cancel-btn:hover, .back-btn:hover {
  border-color: #3D8D7A;
  color: #3D8D7A;
}

.next-btn, .save-btn {
  background: linear-gradient(135deg, #3D8D7A 0%, #A3D1C6 100%);
  color: white;
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 10px;
  cursor: pointer;
  font-weight: 600;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.next-btn:hover, .save-btn:hover {
  transform: translateY(-1px);
  box-shadow: 0 6px 20px rgba(61, 141, 122, 0.3);
}

.next-btn:disabled, .save-btn:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

/* Loading Styles */
.loading-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.6);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1100;
  backdrop-filter: blur(4px);
}

.loading-content {
  background: white;
  padding: 2rem;
  border-radius: 16px;
  text-align: center;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
  min-width: 200px;
}

.loading-content p {
  color: #3D8D7A;
  font-weight: 600;
  margin: 0;
}

.loading-spinner {
  width: 40px;
  height: 40px;
  border: 4px solid rgba(61, 141, 122, 0.1);
  border-left: 4px solid #3D8D7A;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin: 0 auto 1rem;
}

@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

/* Student Roster Modal */
.student-roster-modal {
  max-width: 90vw;
  width: 1200px;
  max-height: 90vh;
}

.roster-subtitle {
  color: #666;
  font-size: 0.9rem;
  margin-top: 0.25rem;
}

.roster-content {
  padding: 1.5rem;
  max-height: 70vh;
  overflow-y: auto;
}

.no-students {
  text-align: center;
  padding: 3rem 2rem;
  color: #666;
}

.no-students .empty-icon {
  color: #A3D1C6;
  margin-bottom: 1rem;
}

.no-students h3 {
  color: #3D8D7A;
  margin-bottom: 0.5rem;
}

.sections-roster {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.section-roster {
  background: rgba(251, 255, 228, 0.3);
  border: 1px solid rgba(61, 141, 122, 0.1);
  border-radius: 16px;
  overflow: hidden;
}

.section-roster-header {
  background: rgba(61, 141, 122, 0.1);
  padding: 1.5rem;
  border-bottom: 1px solid rgba(61, 141, 122, 0.1);
}

.section-roster-header h3 {
  color: #3D8D7A;
  font-size: 1.3rem;
  font-weight: 700;
  margin-bottom: 0.5rem;
}

.section-details {
  display: flex;
  gap: 1rem;
  align-items: center;
}

.students-table {
  background: white;
}

.table-header {
  display: grid;
  grid-template-columns: 120px 200px 250px 80px 120px;
  gap: 1rem;
  padding: 1rem 1.5rem;
  background: rgba(61, 141, 122, 0.05);
  border-bottom: 2px solid rgba(61, 141, 122, 0.1);
  font-weight: 700;
  color: #3D8D7A;
  font-size: 0.85rem;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.table-body {
  max-height: 300px;
  overflow-y: auto;
}

.student-row {
  display: grid;
  grid-template-columns: 120px 200px 250px 80px 120px;
  gap: 1rem;
  padding: 1rem 1.5rem;
  border-bottom: 1px solid rgba(61, 141, 122, 0.1);
  transition: all 0.2s ease;
}

.student-row:hover {
  background: rgba(61, 141, 122, 0.05);
}

.student-row:last-child {
  border-bottom: none;
}

.col-id {
  font-family: 'Courier New', monospace;
  font-weight: 600;
  color: #3D8D7A;
  font-size: 0.9rem;
}

.col-name {
  font-weight: 600;
  color: #333;
}

.col-email {
  color: #666;
  font-size: 0.9rem;
}

.col-grade {
  text-align: center;
  font-weight: 600;
  color: #3D8D7A;
}

.col-date {
  font-size: 0.85rem;
  color: #666;
}

.roster-actions {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.5rem;
  border-top: 1px solid rgba(61, 141, 122, 0.1);
  background: rgba(251, 255, 228, 0.2);
}

.export-btn {
  background: linear-gradient(135deg, #10b981 0%, #34d399 100%);
  color: white;
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 10px;
  cursor: pointer;
  font-weight: 600;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  transition: all 0.3s ease;
}

.export-btn:hover {
  background: linear-gradient(135deg, #059669 0%, #10b981 100%);
  transform: translateY(-1px);
  box-shadow: 0 6px 20px rgba(16, 185, 129, 0.4);
}

.close-roster-btn {
  background: transparent;
  color: #666;
  border: 2px solid #ddd;
  padding: 0.75rem 1.5rem;
  border-radius: 10px;
  cursor: pointer;
  font-weight: 600;
  transition: all 0.3s ease;
}

.close-roster-btn:hover {
  border-color: #3D8D7A;
  color: #3D8D7A;
}

/* Error handling styles */
.error-message {
  background: rgba(239, 68, 68, 0.1);
  border: 1px solid rgba(239, 68, 68, 0.3);
  color: #dc2626;
  padding: 1rem;
  border-radius: 10px;
  margin: 1rem 0;
  text-align: center;
}

.error-message h3 {
  margin: 0 0 0.5rem 0;
  font-weight: 600;
}

.error-message p {
  margin: 0;
  font-size: 0.9rem;
}

/* Dark Mode Styles */
.subjects-page.dark-mode {
  background: var(--bg-primary);
  color: var(--primary-text-color);
}

.dark-mode .header-content h1 {
  color: var(--accent-color);
}

.dark-mode .header-subtitle {
  color: var(--secondary-text-color);
}

.dark-mode .create-btn {
  background: linear-gradient(135deg, var(--accent-color) 0%, #4a9b87 100%);
}

.dark-mode .dark-mode-toggle {
  background: var(--bg-card);
  border-color: var(--border-color);
  color: var(--accent-color);
}

.dark-mode .dark-mode-toggle:hover {
  border-color: var(--accent-color);
  box-shadow: 0 8px 24px rgba(95, 179, 160, 0.2);
}

.dark-mode .section-header-card {
  background: var(--bg-secondary);
  border: 1px solid var(--border-color);
}

.dark-mode .section-header-card:hover {
  box-shadow: 
    0 24px 48px rgba(0, 0, 0, 0.4),
    0 12px 24px rgba(0, 0, 0, 0.3),
    inset 0 1px 0 rgba(255, 255, 255, 0.1);
}

.dark-mode .section-header-title {
  color: var(--primary-text-color);
}

.dark-mode .section-header-subtitle {
  color: var(--secondary-text-color);
}

.dark-mode .section-header-description {
  color: var(--text-muted);
}

.dark-mode .subject-card,
.dark-mode .section-card {
  background: var(--card-background);
  border: 1px solid var(--card-border-color);
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
}

.dark-mode .subject-card:hover,
.dark-mode .section-card:hover {
  box-shadow: 0 16px 48px rgba(0, 0, 0, 0.4);
}

.dark-mode .subject-info h3,
.dark-mode .section-info h3 {
  color: var(--primary-text-color);
}

.dark-mode .grade-level {
  background: linear-gradient(135deg, var(--accent-color) 0%, #4a9b87 100%);
}

.dark-mode .action-btn.edit {
  background: rgba(59, 130, 246, 0.2);
  color: #60a5fa;
}

.dark-mode .action-btn.delete {
  background: rgba(239, 68, 68, 0.2);
  color: #f87171;
}

.dark-mode .subject-stats,
.dark-mode .section-stats {
  background: var(--bg-accent);
}

.dark-mode .stat-number {
  color: var(--accent-color);
}

.dark-mode .stat-label {
  color: var(--secondary-text-color);
}

.dark-mode .clickable-stat:hover {
  background: var(--bg-accent-hover);
}

.dark-mode .sections-list h4 {
  color: var(--primary-text-color);
}

.dark-mode .enhanced-section {
  background: var(--bg-card);
  border: 2px solid var(--card-border-color);
}

.dark-mode .enhanced-section:hover {
  border-color: var(--accent-color);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3);
}

.dark-mode .section-name {
  color: var(--primary-text-color);
}

.dark-mode .section-code-display {
  background: var(--bg-accent);
  border: 1px solid var(--border-color);
}

.dark-mode .code-label {
  color: var(--accent-color);
}

.dark-mode .section-code {
  background: var(--bg-secondary);
  color: var(--accent-color);
  border: 1px solid var(--border-color);
}

.dark-mode .copy-code-btn {
  background: var(--accent-color);
}

.dark-mode .copy-code-btn:hover {
  background: var(--accent-hover);
}

.dark-mode .student-count {
  color: var(--secondary-text-color);
}

.dark-mode .click-hint {
  color: var(--accent-color);
}

.dark-mode .enhanced-section:hover .click-hint {
  color: var(--accent-color);
  opacity: 1;
}

.dark-mode .empty-state {
  color: var(--secondary-text-color);
}

.dark-mode .empty-icon {
  color: var(--accent-color);
}

.dark-mode .empty-state h3 {
  color: var(--primary-text-color);
}

.dark-mode .create-first-btn {
  background: linear-gradient(135deg, var(--accent-color) 0%, #4a9b87 100%);
}

.dark-mode .modal-overlay {
  background: rgba(0, 0, 0, 0.8);
}

.dark-mode .modal-content {
  background: var(--bg-secondary);
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.5);
}

.dark-mode .modal-header {
  border-bottom: 2px solid var(--border-color);
}

.dark-mode .modal-header h2 {
  color: var(--primary-text-color);
}

.dark-mode .close-btn {
  background: rgba(239, 68, 68, 0.2);
  color: #f87171;
}

.dark-mode .close-btn:hover {
  background: rgba(239, 68, 68, 0.3);
}

.dark-mode .step-title {
  color: var(--primary-text-color);
}

.dark-mode .step-subtitle {
  color: var(--secondary-text-color);
}

.dark-mode .form-group label {
  color: var(--primary-text-color);
}

.dark-mode .form-group input,
.dark-mode .form-group select,
.dark-mode .form-group textarea {
  background: var(--input-bg);
  border: 2px solid var(--input-border);
  color: var(--primary-text-color);
}

.dark-mode .form-group input:focus,
.dark-mode .form-group select:focus,
.dark-mode .form-group textarea:focus {
  border-color: var(--accent-color);
  box-shadow: 0 0 0 3px rgba(95, 179, 160, 0.2);
}

.dark-mode .form-group input::placeholder,
.dark-mode .form-group textarea::placeholder {
  color: var(--text-muted);
}

.dark-mode .sections-setup {
  background: var(--bg-accent);
  border: 1px solid var(--border-color);
}

.dark-mode .section-setup-item {
  background: var(--bg-card);
  border: 1px solid var(--border-color);
}

.dark-mode .section-number {
  background: var(--accent-color);
}

.dark-mode .section-input label {
  color: var(--primary-text-color);
}

.dark-mode .section-code-preview {
  color: var(--secondary-text-color);
}

.dark-mode .cancel-btn,
.dark-mode .back-btn {
  background: transparent;
  color: var(--secondary-text-color);
  border: 2px solid var(--border-color);
}

.dark-mode .cancel-btn:hover,
.dark-mode .back-btn:hover {
  border-color: var(--accent-color);
  color: var(--accent-color);
}

.dark-mode .next-btn,
.dark-mode .save-btn {
  background: linear-gradient(135deg, var(--accent-color) 0%, #4a9b87 100%);
}

.dark-mode .loading-content {
  background: var(--bg-secondary);
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.5);
}

.dark-mode .loading-content p {
  color: var(--accent-color);
}

.dark-mode .loading-spinner {
  border: 4px solid rgba(95, 179, 160, 0.2);
  border-left: 4px solid var(--accent-color);
}

.dark-mode .student-roster-modal {
  background: var(--bg-secondary);
}

.dark-mode .roster-subtitle {
  color: var(--secondary-text-color);
}

.dark-mode .no-students {
  color: var(--secondary-text-color);
}

.dark-mode .no-students .empty-icon {
  color: var(--accent-color);
}

.dark-mode .no-students h3 {
  color: var(--primary-text-color);
}

.dark-mode .section-roster {
  background: var(--bg-accent);
  border: 1px solid var(--border-color);
}

.dark-mode .section-roster-header {
  background: var(--bg-accent-hover);
  border-bottom: 1px solid var(--border-color);
}

.dark-mode .section-roster-header h3 {
  color: var(--primary-text-color);
}

.dark-mode .students-table {
  background: var(--bg-card);
}

.dark-mode .table-header {
  background: var(--bg-accent);
  border-bottom: 2px solid var(--border-color);
  color: var(--accent-color);
}

.dark-mode .student-row {
  border-bottom: 1px solid var(--border-color);
}

.dark-mode .student-row:hover {
  background: var(--bg-accent);
}

.dark-mode .col-id {
  color: var(--accent-color);
}

.dark-mode .col-name {
  color: var(--primary-text-color);
}

.dark-mode .col-email {
  color: var(--secondary-text-color);
}

.dark-mode .col-grade {
  color: var(--accent-color);
}

.dark-mode .col-date {
  color: var(--secondary-text-color);
}

.dark-mode .roster-actions {
  border-top: 1px solid var(--border-color);
  background: var(--bg-accent);
}

.dark-mode .close-roster-btn {
  background: transparent;
  color: var(--secondary-text-color);
  border: 2px solid var(--border-color);
}

.dark-mode .close-roster-btn:hover {
  border-color: var(--accent-color);
  color: var(--accent-color);
}

.dark-mode .error-message {
  background: var(--error-bg);
  border: 1px solid rgba(217, 83, 79, 0.4);
  color: var(--error-color);
}

/* Delete Confirmation Modal */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background: rgba(0, 0, 0, 0.6);
  backdrop-filter: blur(4px);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
  animation: fadeIn 0.2s ease-out;
}

.modal-card {
  background: var(--bg-card, #fff);
  color: var(--primary-text-color, #222);
  border-radius: 20px;
  box-shadow: 
    0 20px 40px rgba(0, 0, 0, 0.15),
    0 10px 20px rgba(0, 0, 0, 0.1);
  padding: 2.5rem;
  min-width: 380px;
  max-width: 90vw;
  text-align: center;
  border: 1px solid var(--border-color, rgba(0, 0, 0, 0.1));
  transition: all 0.3s ease;
  animation: slideUp 0.3s ease-out;
}

.modal-icon {
  width: 56px;
  height: 56px;
  margin: 0 auto 1.5rem;
  background: linear-gradient(135deg, #ff6b6b, #e74c3c);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
}

.modal-card h3 {
  margin: 0 0 1.5rem 0;
  font-size: 1.4rem;
  font-weight: 600;
  color: var(--primary-text-color);
}

.item-details {
  margin-bottom: 1.5rem;
  padding: 1rem;
  background: var(--bg-secondary, #f8f9fa);
  border-radius: 12px;
  border: 1px solid var(--border-color, rgba(0, 0, 0, 0.1));
}

.item-name {
  margin: 0 0 0.5rem 0;
  font-size: 1.1rem;
  color: var(--primary-text-color);
}

.item-info {
  margin: 0;
  font-size: 0.9rem;
  color: var(--secondary-text-color, #666);
}

.warning-text {
  margin: 0 0 2rem 0;
  font-size: 0.9rem;
  color: var(--secondary-text-color, #666);
  font-style: italic;
}

.modal-actions {
  display: flex;
  gap: 1rem;
  justify-content: center;
}

.btn-cancel {
  background: linear-gradient(135deg, var(--accent-color, #10b981), #059669);
  color: white;
  border: none;
  border-radius: 12px;
  padding: 0.75rem 1.5rem;
  cursor: pointer;
  font-weight: 500;
  font-size: 0.9rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  transition: all 0.2s ease;
}

.btn-cancel:hover {
  background: linear-gradient(135deg, #059669, #047857);
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(16, 185, 129, 0.3);
}

.btn-delete {
  background: linear-gradient(135deg, #ff6b6b, #e74c3c);
  color: white;
  border: none;
  border-radius: 12px;
  padding: 0.75rem 1.5rem;
  cursor: pointer;
  font-weight: 500;
  font-size: 0.9rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  transition: all 0.2s ease;
}

.btn-delete:hover {
  background: linear-gradient(135deg, #e74c3c, #c0392b);
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(231, 76, 60, 0.3);
}

@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

@keyframes slideUp {
  from {
    opacity: 0;
    transform: translateY(20px) scale(0.95);
  }
  to {
    opacity: 1;
    transform: translateY(0) scale(1);
  }
}

@media (prefers-color-scheme: dark) {
  .modal-card {
    background: var(--bg-card, #2d3748);
    color: var(--primary-text-color, #f7fafc);
    border-color: var(--border-color, rgba(255, 255, 255, 0.1));
  }
  
  .item-details {
    background: var(--bg-secondary, #4a5568);
    border-color: var(--border-color, rgba(255, 255, 255, 0.1));
  }
  
  .btn-cancel {
    background: linear-gradient(135deg, var(--accent-color, #10b981), #059669);
    color: white;
    border: none;
  }
  
  .btn-cancel:hover {
    background: linear-gradient(135deg, #059669, #047857);
    box-shadow: 0 4px 12px rgba(16, 185, 129, 0.3);
  }
}

/* Responsive Design */
@media (max-width: 1024px) {
  .subjects-grid {
    grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
  }
  
  .student-roster-modal {
    width: 95vw;
    max-width: none;
  }
  
  .table-header,
  .student-row {
    grid-template-columns: 100px 180px 200px 70px 100px;
    font-size: 0.85rem;
  }
}

@media (max-width: 768px) {
  .subjects-page {
    padding: 1rem;
  }
  
  .subjects-grid {
    grid-template-columns: 1fr;
  }
  
  .page-header {
    flex-direction: column;
    align-items: stretch;
  }
  
  .header-content h1 {
    font-size: 2rem;
  }
  
  .create-btn {
    justify-content: center;
    width: 100%;
  }
  
  .subject-stats {
    gap: 1rem;
  }
  
  .section-actions {
    grid-template-columns: 1fr 1fr;
  }
  
  .modal-overlay {
    padding: 1rem;
  }
  
  .modal-content {
    padding: 1.5rem;
  }
  
  .section-code-display {
    flex-direction: column;
    align-items: stretch;
    gap: 0.5rem;
  }
  
  .table-header,
  .student-row {
    grid-template-columns: 1fr;
    gap: 0.5rem;
    padding: 1rem;
  }
  
  .table-header {
    display: none;
  }
  
  .student-row {
    display: block;
    border-bottom: 2px solid rgba(61, 141, 122, 0.1);
    margin-bottom: 0.5rem;
  }
  
  .student-row > div {
    display: flex;
    justify-content: space-between;
    padding: 0.25rem 0;
       border-bottom: 1px solid rgba(61, 141, 122, 0.05);
  }
  
  .student-row > div:before {
    content: attr(class);
    font-weight: 600;
    color: #3D8D7A;
    text-transform: capitalize;
  }
  
  .col-id:before { content: "Student ID: "; }
  .col-name:before { content: "Name: "; }

  .col-email:before { content: "Email: "; }
  .col-grade:before { content: "Grade: "; }
  .col-date:before { content: "Enrolled: "; }
  
  .section-setup-item {
    flex-direction: column;
    align-items: stretch;
  }
  
  .section-number {
    align-self: flex-start;
  }

  /* Dark mode mobile styles */
  .dark-mode .student-row {
    border-bottom: 2px solid var(--border-color);
  }
  
  .dark-mode .student-row > div {
    border-bottom: 1px solid var(--border-color);
  }
  
  .dark-mode .student-row > div:before {
    color: var(--accent-color);
  }
}

/* Toast Notification System */
.toast-notification {
  position: fixed;
  top: 2rem;
  right: 2rem;
  max-width: 400px;
  z-index: 2000;
  border-radius: 16px;
  box-shadow: 
    0 20px 40px rgba(0, 0, 0, 0.15),
    0 10px 20px rgba(0, 0, 0, 0.1);
  backdrop-filter: blur(20px);
  border: 1px solid rgba(255, 255, 255, 0.2);
}

.toast-success {
  background: linear-gradient(135deg, rgba(16, 185, 129, 0.95), rgba(5, 150, 105, 0.95));
  color: white;
}

.toast-error {
  background: linear-gradient(135deg, rgba(239, 68, 68, 0.95), rgba(220, 38, 38, 0.95));
  color: white;
}

.toast-warning {
  background: linear-gradient(135deg, rgba(245, 158, 11, 0.95), rgba(217, 119, 6, 0.95));
  color: white;
}

.toast-content {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1.25rem 1.5rem;
}

.toast-icon {
  flex-shrink: 0;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.2);
  display: flex;
  align-items: center;
  justify-content: center;
  animation: toastIconPulse 2s ease-in-out infinite;
}

.toast-message {
  flex: 1;
  font-weight: 500;
  font-size: 0.95rem;
  line-height: 1.4;
}

.toast-close {
  background: none;
  border: none;
  color: inherit;
  cursor: pointer;
  padding: 0.25rem;
  border-radius: 6px;
  transition: background 0.2s;
  opacity: 0.8;
}

.toast-close:hover {
  background: rgba(255, 255, 255, 0.2);
  opacity: 1;
}

/* Toast Transitions */
.toast-enter-active {
  transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}

.toast-leave-active {
  transition: all 0.3s ease-in;
}

.toast-enter-from {
  opacity: 0;
  transform: translateX(100%) scale(0.8);
}

.toast-enter-to {
  opacity: 1;
  transform: translateX(0) scale(1);
}

.toast-leave-from {
  opacity: 1;
  transform: translateX(0) scale(1);
}

.toast-leave-to {
  opacity: 0;
  transform: translateX(100%) scale(0.8);
}

@keyframes toastIconPulse {
  0%, 100% {
    transform: scale(1);
  }
  50% {
    transform: scale(1.1);
  }
}

@media (max-width: 768px) {
  .toast-notification {
    top: 1rem;
    right: 1rem;
    left: 1rem;
    max-width: none;
  }
}

@media (prefers-color-scheme: dark) {
  .toast-notification {
    border-color: rgba(255, 255, 255, 0.1);
  }
}
</style>