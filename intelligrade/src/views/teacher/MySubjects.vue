/* Enhanced dark mode info box styling for section detail view (dashboard style) */
.dark-mode .section-info-grid {
  display: flex;
  gap: 2rem;
  margin-bottom: 1.5rem;
}
.dark-mode .section-info-item {
  background: #111111;
  border: 2px solid #10b981;
  border-radius: 14px;
  padding: 1.2rem 2.5rem;
  min-width: 120px;
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
  box-shadow: none;
}
.dark-mode .section-info-item .info-label {
  color: #10b981;
  font-weight: 700;
  font-size: 1.1rem;
  letter-spacing: 1px;
  margin-bottom: 0.5rem;
  display: block;
}
.dark-mode .section-info-item .info-value {
  color: #e9ecef;
  font-weight: 600;
  font-size: 1.2rem;
  background: rgba(16,185,129,0.08);
  border-radius: 8px;
  padding: 0.35rem 0.8rem;
  margin-top: 0.2rem;
  display: inline-block;
}
.dark-mode .section-code-area {
  background: #111111;
  border: 2px solid #10b981;
  border-radius: 14px;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
  padding: 1.2rem 2.5rem;
  margin-bottom: 2rem;
}
.dark-mode .section-code-area h4 {
  color: #2dd4bf;
  font-weight: 700;
  font-size: 1.1rem;
  letter-spacing: 1px;
  margin-bottom: 0.5rem;
}
.dark-mode .section-code-display {
  background: #111111;
  border: 2px solid #10b981;
  color: #10b981;
  border-radius: 10px;
  padding: 0.7rem 1.2rem;
  display: flex;
  align-items: center;
  gap: 1rem;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
}
.dark-mode .section-code {
  font-family: 'Courier New', Courier, monospace;
  font-size: 1.3rem;
  color: #10b981;
  background: transparent;
  border: none;
  padding: 0;
}
.dark-mode .copy-code-btn {
  background: #2dd4bf;
  color: #111827;
  border-radius: 8px;
  font-weight: 700;
  padding: 0.6rem 1.2rem;
  border: none;
  transition: background 0.2s;
  box-shadow: 0 2px 8px rgba(45,212,191,0.10);
}
.dark-mode .copy-code-btn:hover {
  background: #059669;
  color: #fff;
}
/* Dark mode accent for info labels in section detail view */
.dark-mode .section-info-item .info-label,
.dark-mode .section-code-area h4 {
  color: var(--accent-color);
  font-weight: 600;
  letter-spacing: 1px;
}

.dark-mode .section-info-item .info-value {
  color: var(--primary-text-color);
  font-weight: 500;
}
/* Extra dark mode styles for section-detail view to match other pages */
.dark-mode .section-detail-view {
  background: var(--bg-primary);
  color: var(--primary-text-color);
}

.dark-mode .section-detail-card {
  background: var(--bg-secondary);
  border: 1.5px solid var(--border-color);
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
}

.dark-mode .section-info-container {
  background: var(--bg-card);
  border-radius: 12px;
  box-shadow: 0 4px 16px rgba(0,0,0,0.18);
}

.dark-mode .section-info-grid .info-label {
  color: var(--accent-color);
}
.dark-mode .section-info-grid .info-value {
  color: var(--primary-text-color);
}

.dark-mode .section-code-area h4 {
  color: var(--accent-color);
}
.dark-mode .section-code-display {
  background: var(--bg-accent);
  border: 1px solid var(--border-color);
  color: var(--accent-color);
}
.dark-mode .section-code {
  background: var(--bg-secondary);
  color: var(--accent-color);
  border: 1px solid var(--border-color);
}
.dark-mode .copy-code-btn {
  background: var(--accent-color);
  color: #fff;
}
.dark-mode .copy-code-btn:hover {
  background: var(--accent-hover);
}

.dark-mode .section-actions-grid {
  background: var(--bg-card);
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.10);
}
<template>
  <div class="subjects-page" :class="{ 'dark-mode': isDarkMode }">
    <div class="section-header-card">
      <div class="header-bg-decoration"></div>
      <div class="floating-shapes">
        <div class="shape shape-1"></div>
        <div class="shape shape-2"></div>
        <div class="shape shape-3"></div>
        <div class="shape shape-4"></div>
        <div class="shape shape-5"></div>
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
            <svg v-if="isDarkMode" width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M12,7A5,5 0 0,1 17,12A5,5 0 0,1 12,17A5,5 0 0,1 7,12A5,5 0 0,1 12,7M12,9A3,3 0 0,0 9,12A3,3 0 0,0 12,15A3,3 0 0,0 15,12A3,3 0 0,0 12,9M12,2L14.39,5.42C13.65,5.15 12.84,5 12,5C11.16,5 10.35,5.15 9.61,5.42L12,2M3.34,7L7.5,6.65C6.9,7.16 6.36,7.78 5.94,8.5C5.52,9.22 5.25,10 5.11,10.79L3.34,7M3.36,17L5.12,13.23C5.26,14 5.53,14.78 5.95,15.5C6.37,16.22 6.91,16.84 7.51,17.35L3.36,17M20.65,7L18.88,10.79C18.74,10 18.47,9.22 18.05,8.5C17.63,7.78 17.09,7.15 16.49,6.64L20.65,7M20.64,17L16.5,17.36C17.1,16.85 17.64,16.22 18.06,15.5" />
            </svg>
            <svg v-else width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M17.75,4.09L15.22,6.03L16.13,9.09L13.5,7.28L10.87,9.09L11.78,6.03L9.25,4.09L12.44,4L13.5,1L14.56,4L17.75,4.09M21.25,11L19.61,12.25L20.2,14.23L18.5,13.06L16.8,14.23L17.39,12.25L15.75,11L17.81,10.95L18.5,9L19.19,10.95L21.25,11M18.97,15.95C19.8,15.87 20.69,17.05 20.16,17.8C19.84,18.25 19.5,18.67 19.08,19.07C15.17,23 8.84,23 4.94,19.07C1.03,15.17 1.03,8.83 4.94,4.93C5.34,4.53 5.76,4.17 6.21,3.85C6.96,3.32 8.14,4.21 8.06,5.04C7.79,7.9 8.75,10.87 10.95,13.06C13.14,15.26 16.1,16.22 18.97,15.95M17.33,17.97C14.5,17.81 11.7,16.64 9.53,14.5C7.36,12.31 6.2,9.5 6.04,6.68C3.23,9.82 3.34,14.4 6.35,17.41C9.37,20.43 14,20.54 17.33,17.97Z" />
            </svg>
          <!-- End dark mode toggle button -->
          <button @click="showCreateModal = true" class="create-quiz-btn">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M19,13H13V19H11V13H5V11H11V5H13V11H19V13Z" />
            </svg>
            Create New Subject
          </button>
        </div>
      </div>
    </div>

    <!-- Level 1: Subject Names Only -->
    <div v-if="viewMode === 'subjects' && subjects.length > 0" class="subjects-grid">
      <div v-for="subject in subjects" :key="subject.id" class="subject-card simple" @click="selectSubject(subject)">
        <div class="subject-simple-header">
          <div class="subject-info">
            <h3>{{ subject.subject_name }}</h3>
            <p class="grade-level">{{ subject.grade_level_display }}</p>
            <p class="subject-stats-simple">{{ subject.section_count }} sections • {{ subject.total_students }} students</p>
          </div>
          <div class="arrow-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
              <path d="M8.59,16.58L13.17,12L8.59,7.41L10,6L16,12L10,18L8.59,16.58Z" />
            </svg>
          </div>
        </div>
      </div>
    </div>

    <!-- Level 2: Sections List -->
    <div v-if="viewMode === 'sections' && selectedSubject" class="sections-view">
      <div class="breadcrumb">
        <button @click="goBackToSubjects" class="breadcrumb-btn">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
            <path d="M20,11V13H8L13.5,18.5L12.08,19.92L4.16,12L12.08,4.08L13.5,5.5L8,11H20Z" />
          </svg>
          My Subjects
        </button>
        <span class="breadcrumb-separator">/</span>
        <span class="breadcrumb-current">{{ selectedSubject.subject_name }}</span>
      </div>
      
      <!-- Grade Filter Buttons -->
      <div class="grade-filter-container">
        <button 
          @click="setGradeFilter('all')" 
          class="grade-filter-btn"
          :class="{ 'active': selectedGradeFilter === 'all' }"
        >
          All
        </button>
        <button 
          v-for="grade in availableGrades" 
          :key="grade"
          @click="setGradeFilter(grade.toString())" 
          class="grade-filter-btn"
          :class="{ 'active': selectedGradeFilter === grade.toString() }"
        >
          Grade {{ grade }}
        </button>
      </div>
      
      <div class="sections-grid">
        <div v-for="section in filteredSections" :key="section.id" class="section-card simple" @click="selectSection(section)">
          <!-- Decorative corner accent -->
          <div class="card-corner-accent"></div>
          <!-- Decorative icon -->
          <div class="card-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" opacity="0.15">
              <path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-5 14H7v-2h7v2zm3-4H7v-2h10v2zm0-4H7V7h10v2z"/>
            </svg>
          </div>
          <div class="section-simple-header">
            <!-- 3-dots menu at the top -->
            <div class="section-actions-row">
              <div class="section-menu-container">
                <button class="section-action-btn menu" @click.stop="toggleSectionMenu(section.id)" title="More Options">
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor">
                    <circle cx="5" cy="12" r="2" />
                    <circle cx="12" cy="12" r="2" />
                    <circle cx="19" cy="12" r="2" />
                  </svg>
                </button>
                <div v-if="openMenuId === section.id" class="section-dropdown-menu">
                  <button @click.stop="editSection(section)" class="menu-item">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                      <path d="M20.71,7.04C21.1,6.65 21.1,6 20.71,5.63L18.37,3.29C18,2.9 17.35,2.9 16.96,3.29L15.12,5.12L18.87,8.87M3,17.25V21H6.75L17.81,9.93L14.06,6.18L3,17.25Z" />
                    </svg>
                    Edit
                  </button>
                  <button @click.stop="openDeleteModal('section', section)" class="menu-item delete">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                      <path d="M19,4H15.5L14.5,3H9.5L8.5,4H5V6H19M6,19A2,2 0 0,0 8,21H16A2,2 0 0,0 18,19V7H6V19Z" />
                    </svg>
                    Delete
                  </button>
                  <button @click.stop="toggleArchiveSection(section)" class="menu-item">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                      <path d="M3,3H21V7H3V3M4,8H20V21H4V8M9.5,11A0.5,0.5 0 0,0 9,11.5V13H15V11.5A0.5,0.5 0 0,0 14.5,11H9.5Z" />
                    </svg>
                    {{ (section.status === 'archived') ? 'Unarchive' : 'Archive' }}
                  </button>
                </div>
              </div>
            </div>
            
            <!-- Section name and grade in the center -->
            <div class="section-info">
              <h4>{{ section.section_name }} (Grade {{ section.grade_level }})</h4>
              
              <!-- Section Code Display -->
              <div class="section-code-inline">
                <span class="code-label">Code:</span>
                <span class="section-code-text" @click.stop="copyCode(section.section_code, section.id)">
                  {{ section.section_code }}
                </span>
                <button @click.stop="copyCode(section.section_code, section.id)" class="copy-code-mini" :title="copiedCodeId === section.id ? 'Copied!' : 'Copy Code'">
                  <svg width="12" height="12" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M19,21H8V7H19M19,5H8A2,2 0 0,0 6,7V21A2,2 0 0,0 8,23H19A2,2 0 0,0 21,21V7A2,2 0 0,0 19,5M16,1H4A2,2 0 0,0 2,3V17H4V3H16V1Z" />
                  </svg>
                </button>
              </div>
              
              <!-- Student count at the bottom -->
              <p class="section-stats-simple">{{ section.student_count || 0 }} students</p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Level 3: Section Detail (like in the picture) -->
    <div v-if="viewMode === 'section-detail' && selectedSection" class="section-detail-view">
      <div class="breadcrumb">
        <button @click="goBackToSubjects" class="breadcrumb-btn">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
            <path d="M20,11V13H8L13.5,18.5L12.08,19.92L4.16,12L12.08,4.08L13.5,5.5L8,11H20Z" />
          </svg>
          My Subjects
        </button>
        <span class="breadcrumb-separator">/</span>
        <button @click="goBackToSections" class="breadcrumb-btn">{{ selectedSubject.subject_name }}</button>
        <span class="breadcrumb-separator">/</span>
        <span class="breadcrumb-current">{{ selectedSection.section_name }} (Grade {{ selectedSection.grade_level }})</span>
      </div>

      <div class="section-detail-card">
        <div class="section-header">
          <div class="section-info">
          </div>
          <!-- Removed edit and delete buttons -->
          <div class="section-actions"></div>
        </div>

        <!-- Section Info -->
        <div class="section-info-container">
          <div class="section-info-grid">
            <div class="section-info-item">
              <span class="info-label">Subject:</span>
              <span class="info-value">{{ selectedSection.subject_name }}</span>
            </div>
            <div class="section-info-item">
              <span class="info-label">Section:</span>
              <span class="info-value">{{ selectedSection.section_name }}</span>
            </div>
            <div class="section-info-item">
              <span class="info-label">Grade:</span>
              <span class="info-value">{{ selectedSection.grade_level_display || selectedSection.grade_level }}</span>
            </div>
          </div>
          
          <div class="section-code-area">
            <h4>Section Code:</h4>
            <div class="section-code-display">
              <span class="section-code">{{ selectedSection.section_code }}</span>
              <button @click.stop="copyCode(selectedSection.section_code, selectedSection.section_id)" class="copy-code-btn">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M19,21H8V7H19M19,5H8A2,2 0 0,0 6,7V21A2,2 0 0,0 8,23H19A2,2 0 0,0 21,21V7A2,2 0 0,0 19,5M16,1H4A2,2 0 0,0 2,3V17H4V3H16V1Z" />
                </svg>
                {{ copiedCodeId === selectedSection.section_id ? 'Copied!' : 'Copy' }}
              </button>
            </div>
          </div>
        </div>
        
        <!-- Section Action Buttons -->
        <div class="section-actions-grid">
          <button 
            @click.stop="viewSectionStudents(selectedSubject, selectedSection)"
            class="section-action-btn view-students"
            title="View Students in Section"
          >
            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
              <path d="M16,4C18.21,4 20,5.79 20,8C20,10.21 18.21,12 16,12C13.79,12 12,10.21 12,8C12,5.79 13.79,4 16,4M16,14C20.42,14 24,15.79 24,18V20H8V18C8,15.79 11.58,14 16,14M6,6C7.1,6 8,6.9 8,8C8,9.1 7.1,10 6,10C4.9,10 4,9.1 4,8C4,6.9 4.9,6 6,6M6,12C8.67,12 12,13.34 12,16V18H0V16C0,13.34 3.33,12 6,12Z" />
            </svg>
            View Students
          </button>

          <button 
            @click.stop="navigateToCreateQuiz(selectedSubject, selectedSection)"
            class="section-action-btn create-quiz"
            title="Create Quiz/Assessment"
          >
            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
              <path d="M14,2H6A2,2 0 0,0 4,4V20A2,2 0 0,0 6,22H18A2,2 0 0,0 20,20V8L14,2M18,20H6V4H13V9H18V20Z" />
            </svg>
            Create Quiz
          </button>
          
          <button 
            @click.stop="viewQuizzes(selectedSubject, selectedSection)"
            class="section-action-btn view-quizzes"
            title="View Past Quizzes"
          >
            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
              <path d="M13,9V3.5L18.5,9M6,2C4.89,2 4,2.89 4,4V20A2,2 0 0,0 6,22H18A2,2 0 0,0 20,20V8L14,2H6Z" />
            </svg>
            View Quizzes
          </button>
          
          <button 
            @click.stop="manageGrades(selectedSubject, selectedSection)"
            class="section-action-btn manage-grades"
            title="Grade Management"
          >
            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
              <path d="M9,5A4,4 0 0,1 13,9A4,4 0 0,1 9,13A4,4 0 0,1 5,9A4,4 0 0,1 9,5M9,15C11.67,15 17,16.34 17,19V21H1V19C1,16.34 6.33,15 9,15M16.76,5.36C18.78,7.56 18.78,10.61 16.76,12.63L15.08,10.94C15.92,9.76 15.92,8.23 15.08,7.05L16.76,5.36M20.07,2C24,6.05 23.97,12.11 20.07,16.07L18.44,14.44C21.21,11.19 21.21,6.65 18.44,3.63L20.07,2Z" />
            </svg>
            Grades
          </button>
        </div>
      </div>
    </div>

    <!-- Empty State - only show when in subjects view and no subjects exist -->
    <div v-if="viewMode === 'subjects' && subjects.length === 0" class="empty-state">
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
                <path d="M16 4C18.2 4 20 5.8 20 8S18.2 12 16 12 12 10.2 12 8 13.8 4 16 4M16 14C20.42 14 24 15.79 24 18V20H8V18C8,15.79 11.58,14 16,14C10.5 14 9.2 14.3 8.5 14.8V11.5Z" />
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
const selectedSubject = ref(null)
const selectedSection = ref(null)
const viewMode = ref('subjects')
const selectedGradeFilter = ref('all')
const showCreateModal = ref(false)
const showStudentRosterModal = ref(false)
const currentStudentRoster = ref(null)
const isEditing = ref(false)
const currentSubjectId = ref(null)
const currentStep = ref(1)
const copiedCodeId = ref(null)
const currentUser = ref(null)
const teacherInfo = ref(null)
const authListener = ref(null)
const isInitialized = ref(false)
const showDeleteModal = ref(false)
const deleteType = ref('')
const itemToDelete = ref(null)
const showNotification = ref(false)
const notificationMessage = ref('')
const notificationType = ref('success')
const openMenuId = ref(null)

// Cache state
const subjectsCache = ref(null)
const lastFetchTime = ref(0)
const CACHE_DURATION = 30000 // 30 seconds

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

// Initialize authentication
const initializeAuth = async () => {
  try {
    const { data: { session }, error: sessionError } = await supabase.auth.getSession()
    
    if (sessionError) throw sessionError
    if (!session?.user) {
      await router.push('/login')
      return false
    }
    
    currentUser.value = session.user
    
    const { data: profile, error: profileError } = await supabase
      .from('profiles')
      .select('id, role, full_name, email')
      .eq('auth_user_id', session.user.id)
      .single()
    
    if (profileError || !profile) {
      await router.push('/login')
      return false
    }

    if (profile.role !== 'teacher') {
      await router.push('/login')
      return false
    }

    const { data: teacher, error: teacherError } = await supabase
      .from('teachers')
      .select('*')
      .eq('profile_id', profile.id)
      .eq('is_active', true)
      .single()

    if (teacherError || !teacher) {
      await router.push('/login')
      return false
    }

    teacherInfo.value = teacher
    return true

  } catch (error) {
    console.error('Authentication error:', error)
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
    if (event === 'SIGNED_OUT' || (event === 'TOKEN_REFRESHED' && !session)) {
      currentUser.value = null
      teacherInfo.value = null
      subjects.value = []
      subjectsCache.value = null
      isInitialized.value = false
      await router.push('/login')
    }
  })
}

// Navigation methods
const toggleSubjectExpansion = (subject) => {
  subject.expanded = !subject.expanded
}

const selectSubject = (subject) => {
  selectedSubject.value = subject
  selectedSection.value = null
  selectedGradeFilter.value = 'all'
  viewMode.value = 'sections'
}

const selectSection = (section) => {
  selectedSection.value = section
  viewMode.value = 'section-detail'
}

const goBackToSubjects = () => {
  selectedSubject.value = null
  selectedSection.value = null
  selectedGradeFilter.value = 'all'
  viewMode.value = 'subjects'
}

const goBackToSections = () => {
  selectedSection.value = null
  viewMode.value = 'sections'
}

// Grade filtering
const setGradeFilter = (grade) => {
  selectedGradeFilter.value = grade
}

const filteredSections = computed(() => {
  if (!selectedSubject.value || !selectedSubject.value.sections) {
    return []
  }
  
  if (selectedGradeFilter.value === 'all') {
    return selectedSubject.value.sections
  }
  
  return selectedSubject.value.sections.filter(section => 
    section.grade_level.toString() === selectedGradeFilter.value
  )
})

const availableGrades = computed(() => {
  if (!selectedSubject.value || !selectedSubject.value.sections) {
    return []
  }
  
  const grades = [...new Set(selectedSubject.value.sections.map(section => section.grade_level))]
  return grades.sort((a, b) => a - b)
})

// Navigation functions
const navigateToSections = async (subject, section, event) => {
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

const viewSectionStudents = async (subject, section) => {
  try {
    const sec = section || (subject.sections && subject.sections[0]) || subject
    await router.push({
      name: 'ViewStudents',
      params: {
        subjectId: subject.id || subject.subject_id,
        sectionId: sec.id || sec.section_id
      },
      query: {
        subjectName: subject.name || subject.subject_name,
        sectionName: sec.name || sec.section_name,
        gradeLevel: subject.grade_level,
        sectionCode: sec.section_code
      }
    })
  } catch (error) {
    console.error('Navigation error:', error)
  }
}

// Optimized fetch with instant display from cache
const fetchSubjects = async (forceRefresh = false) => {
  try {
    if (!teacherInfo.value?.id) return

    const now = Date.now()
    
    // Always use cache first for instant display
    if (!forceRefresh && subjectsCache.value && (now - lastFetchTime.value) < CACHE_DURATION) {
      subjects.value = subjectsCache.value
      return
    }

    // If we have cache, display it immediately and fetch in background
    if (subjectsCache.value) {
      subjects.value = subjectsCache.value
    }

    // Fetch in background (no loading state)
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

    if (subjectsError) throw subjectsError

    // Process subjects
    const subjectGroups = new Map()

    if (subjectsData && subjectsData.length > 0) {
      // Batch fetch enrollment counts
      const allSectionIds = subjectsData.flatMap(subject => 
        (subject.sections || []).filter(s => s.is_active).map(s => s.id)
      )

      const enrollmentCounts = new Map()
      if (allSectionIds.length > 0) {
        const { data: enrollments } = await supabase
          .from('enrollments')
          .select('section_id')
          .in('section_id', allSectionIds)

        if (enrollments) {
          enrollments.forEach(e => {
            enrollmentCounts.set(e.section_id, (enrollmentCounts.get(e.section_id) || 0) + 1)
          })
        }
      }

      // Process subjects
      for (const subject of subjectsData) {
        if (subject.sections && subject.sections.length > 0) {
          const subjectName = subject.name

          if (!subjectGroups.has(subjectName)) {
            subjectGroups.set(subjectName, {
              subject_name: subjectName,
              name: subjectName,
              sections: [],
              grade_levels: new Set(),
              total_students: 0,
              section_count: 0,
              expanded: false
            })
          }

          const subjectGroup = subjectGroups.get(subjectName)
          subjectGroup.grade_levels.add(subject.grade_level)

          for (const section of subject.sections) {
            if (section.is_active) {
              const studentCount = enrollmentCounts.get(section.id) || 0
              subjectGroup.total_students += studentCount

              subjectGroup.sections.push({
                id: section.id,
                section_id: section.id,
                name: section.name,
                section_name: section.name,
                section_code: section.section_code,
                max_students: section.max_students,
                student_count: studentCount,
                is_active: section.is_active,
                grade_level: subject.grade_level,
                subject_id: subject.id,
                subject_name: subject.name
              })
              
              subjectGroup.section_count++
            }
          }
        }
      }
    }

    // Convert to array
    const processedSubjects = Array.from(subjectGroups.values()).map(group => {
      const gradeLevelsArray = Array.from(group.grade_levels).sort((a, b) => a - b)
      return {
        ...group,
        id: `combined_${group.name}`,
        grade_levels: gradeLevelsArray,
        grade_level_display: gradeLevelsArray.length === 1 
          ? `Grade ${gradeLevelsArray[0]}` 
          : `Grades ${gradeLevelsArray.join(', ')}`
      }
    })

    // Update cache and state
    subjectsCache.value = [...processedSubjects]
    subjects.value = [...processedSubjects]
    lastFetchTime.value = now

    await nextTick()

  } catch (error) {
    console.error('Error fetching subjects:', error)
    
    if (error.code === 'PGRST301' || error.message?.includes('JWT')) {
      await router.push('/login')
    }
  }
}

// Background refresh
const startBackgroundRefresh = () => {
  setInterval(() => {
    if (teacherInfo.value?.id && document.visibilityState === 'visible') {
      fetchSubjects(true)
    }
  }, CACHE_DURATION)
}

const getTotalStudents = (subject) => {
  return subject.actualStudentCount || 0
}

// Student roster viewing (no loading overlay)
const viewStudentRoster = async (subject) => {
  try {
    if (!teacherInfo.value) return

    const { data: rosterData } = await supabase
      .from('teacher_student_roster')
      .select('*')
      .eq('subject_id', subject.id)
      .eq('teacher_id', teacherInfo.value.id)

    const { data: allSections } = await supabase
      .from('sections')
      .select('*')
      .eq('subject_id', subject.id)
      .eq('is_active', true)

    const studentsBySection = {}
    let totalActualStudents = 0

    if (allSections && allSections.length > 0) {
      allSections.forEach(section => {
        const sectionKey = `${section.name} (${section.section_code})`
        studentsBySection[sectionKey] = {
          section: section,
          students: []
        }
      })
    }

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
      })
    }

    currentStudentRoster.value = {
      subject,
      studentsBySection,
      totalActualStudents
    }
    
    showStudentRosterModal.value = true

  } catch (error) {
    console.error('Error viewing student roster:', error)
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
  } catch (err) {
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

// Save subject (no loading overlay)
const saveSubject = async () => {
  try {
    if (!teacherInfo.value?.id) {
      alert('Please login to continue')
      return
    }

    const subjectData = {
      name: formData.value.name,
      grade_level: parseInt(formData.value.grade_level),
      teacher_id: teacherInfo.value.id,
      description: formData.value.description || null,
      is_active: true
    }

    let subjectId

    if (isEditing.value) {
      const { data: updatedSubject, error: updateError } = await supabase
        .from('subjects')
        .update(subjectData)
        .eq('id', currentSubjectId.value)
        .eq('teacher_id', teacherInfo.value.id)
        .select()
        .single()

      if (updateError) throw updateError
      
      subjectId = currentSubjectId.value

      await supabase
        .from('sections')
        .delete()
        .eq('subject_id', subjectId)

    } else {
      const { data: newSubject, error: insertError } = await supabase
        .from('subjects')
        .insert([subjectData])
        .select()
        .single()

      if (insertError) throw insertError
      
      subjectId = newSubject.id
    }

    const sectionsToInsert = []
    const createdSectionCodes = []
    
    for (let i = 0; i < formData.value.sections.length; i++) {
      const section = formData.value.sections[i]
      
      const subjectPrefix = formData.value.name.substring(0, 4).toUpperCase().replace(/[^A-Z]/g, '')
      const year = new Date().getFullYear()
      const timestamp = Date.now().toString().slice(-6)
      const sectionCode = `${subjectPrefix}${formData.value.grade_level}-${year}-${timestamp}${String(i + 1).padStart(2, '0')}`
      
      sectionsToInsert.push({
        subject_id: subjectId,
        name: section.name,
        section_code: sectionCode,
        max_students: parseInt(section.max_students) || 40,
        is_active: true
      })
      
      createdSectionCodes.push(`${section.name}: ${sectionCode}`)
    }

    await supabase
      .from('sections')
      .insert(sectionsToInsert)
      .select()

    closeModal()

    const sectionCodesText = createdSectionCodes.join('\n')
    showToast(`Subject "${formData.value.name}" ${isEditing.value ? 'updated' : 'created'} successfully!`, 'success')
    
    setTimeout(() => {
      alert(`Section Codes:\n${sectionCodesText}\n\nShare these codes with your students so they can join their respective sections.`)
    }, 500)

    // Invalidate cache and refresh
    subjectsCache.value = null
    await fetchSubjects(true)

  } catch (error) {
    console.error('Error saving subject:', error)
    showToast('Error saving subject. Please try again.', 'error')
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

// Toast notifications
const showToast = (message, type = 'success') => {
  notificationMessage.value = message
  notificationType.value = type
  showNotification.value = true
  
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

const deleteSubjectConfirmed = async (subjectId) => {
  try {
    if (!teacherInfo.value) return

    const subject = subjects.value.find(s => s.id === subjectId)

    await supabase
      .from('subjects')
      .delete()
      .eq('id', subjectId)
      .eq('teacher_id', teacherInfo.value.id)
    
    subjectsCache.value = null
    await fetchSubjects(true)
    showToast(`Subject "${subject?.name}" deleted successfully!`, 'success')
  } catch (error) {
    showToast('Error deleting subject', 'error')
  }
}

const deleteSectionConfirmed = async (sectionId) => {
  try {
    if (!teacherInfo.value) return

    const section = subjects.value.find(s => s.section_id === sectionId)

    await supabase
      .from('sections')
      .delete()
      .eq('id', sectionId)
    
    subjectsCache.value = null
    await fetchSubjects(true)
    showToast(`Section "${section?.section_name}" deleted successfully!`, 'success')
  } catch (error) {
    showToast('Error deleting section', 'error')
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
  } catch (error) {
    console.error('Error exporting roster:', error)
  }
}

const toggleSectionMenu = (sectionId) => {
  openMenuId.value = openMenuId.value === sectionId ? null : sectionId
}

const toggleArchiveSection = async (section) => {
  try {
    const newStatus = section.status === 'archived' ? 'in-progress' : 'archived'
    
    await supabase
      .from('sections')
      .update({ status: newStatus })
      .eq('id', section.id)
    
    section.status = newStatus
    openMenuId.value = null
    showToast(`Section "${section.section_name}" has been ${newStatus === 'archived' ? 'archived' : 'unarchived'}.`, 'success')
  } catch (error) {
    showToast('Error updating section status', 'error')
  }
}

const handleClickOutside = (event) => {
  if (!event.target.closest('.section-menu-container')) {
    openMenuId.value = null
  }
}

// Lifecycle
onMounted(async () => {
  try {
    initDarkMode()
    
    const authSuccess = await initializeAuth()
    if (!authSuccess) return
    
    setupAuthListener()
    isInitialized.value = true
    
    // Initial fetch - subjects display instantly from cache after first load
    await fetchSubjects()
    
    // Start background refresh
    startBackgroundRefresh()
    
    document.addEventListener('click', handleClickOutside)
    
    // Refresh when tab becomes visible
    document.addEventListener('visibilitychange', () => {
      if (document.visibilityState === 'visible' && teacherInfo.value?.id) {
        const timeSinceLastFetch = Date.now() - lastFetchTime.value
        if (timeSinceLastFetch > CACHE_DURATION) {
          fetchSubjects(true)
        }
      }
    })
    
  } catch (error) {
    console.error('Component mount error:', error)
    await router.push('/login')
  }
})

onUnmounted(() => {
  if (authListener.value) {
    authListener.value.data.subscription.unsubscribe()
    authListener.value = null
  }
  document.removeEventListener('click', handleClickOutside)
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
  transform: translateY(-4px) scale(1.005);
  box-shadow: 
    0 35px 70px rgba(16, 185, 129, 0.12),
    0 20px 40px rgba(0, 0, 0, 0.08),
    0 12px 24px rgba(16, 185, 129, 0.06),
    inset 0 1px 0 rgba(255, 255, 255, 0.95),
    inset 0 0 0 1px rgba(16, 185, 129, 0.1);
  border-color: rgba(16, 185, 129, 0.15);
}

.header-bg-decoration {
  position: absolute;
  top: -50%;
  right: -20%;
  width: 140%;
  height: 220%;
  background: 
    radial-gradient(ellipse 60% 40% at 70% 30%, rgba(16, 185, 129, 0.12) 0%, transparent 60%),
    radial-gradient(ellipse 40% 60% at 30% 70%, rgba(5, 150, 105, 0.08) 0%, transparent 50%),
    linear-gradient(135deg, rgba(16, 185, 129, 0.05) 0%, transparent 80%);
  z-index: 1;
  opacity: 0.8;
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
  width: 88px;
  height: 88px;
  background: 
    linear-gradient(135deg, #10b981 0%, #059669 50%, #047857 100%),
    linear-gradient(225deg, rgba(255, 255, 255, 0.2) 0%, transparent 50%);
  border-radius: 28px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #fff;
  box-shadow: 
    0 12px 32px rgba(16, 185, 129, 0.35),
    0 6px 16px rgba(16, 185, 129, 0.2),
    inset 0 1px 0 rgba(255, 255, 255, 0.3),
    inset 0 -1px 0 rgba(0, 0, 0, 0.1);
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  position: relative;
  overflow: hidden;
}

.section-header-icon:hover {
  transform: translateY(-3px) scale(1.05);
  box-shadow: 
    0 16px 40px rgba(16, 185, 129, 0.4),
    0 8px 20px rgba(16, 185, 129, 0.25),
    inset 0 1px 0 rgba(255, 255, 255, 0.4),
    inset 0 -1px 0 rgba(0, 0, 0, 0.15);
}

.section-header-icon::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.3), transparent);
  transition: left 0.6s;
}

.section-header-icon:hover::before {
  left: 100%;
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
  background: 
    linear-gradient(135deg, #10b981 0%, #059669 50%, #047857 100%),
    linear-gradient(225deg, rgba(255, 255, 255, 0.15) 0%, transparent 50%);
  color: white;
  border: none;
  padding: 1rem 2rem;
  border-radius: 20px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  box-shadow: 
    0 10px 30px rgba(16, 185, 129, 0.35),
    0 5px 15px rgba(16, 185, 129, 0.2),
    inset 0 1px 0 rgba(255, 255, 255, 0.3),
    inset 0 -1px 0 rgba(0, 0, 0, 0.1);
  position: relative;
  overflow: hidden;
  font-size: 0.95rem;
  letter-spacing: 0.025em;
}

.create-quiz-btn::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.25), transparent);
  transition: left 0.6s;
}

.create-quiz-btn:hover::before {
  left: 100%;
}

.create-quiz-btn:hover:not(:disabled) {
  transform: translateY(-3px) scale(1.02);
  box-shadow: 
    0 15px 40px rgba(16, 185, 129, 0.45),
    0 8px 20px rgba(16, 185, 129, 0.3),
    inset 0 1px 0 rgba(255, 255, 255, 0.4),
    inset 0 -1px 0 rgba(0, 0, 0, 0.15);
}

.create-quiz-btn:active {
  transform: translateY(-1px) scale(0.98);
  transition: all 0.1s ease;
}

.floating-shapes {
  position: absolute;
  top: 0;
  right: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
  z-index: 1;
  overflow: hidden;
}

.shape {
  position: absolute;
  border-radius: 50%;
  filter: blur(0.5px);
  opacity: 0.8;
}

.shape-1 {
  width: 120px;
  height: 120px;
  top: -25px;
  right: 12%;
  background: 
    radial-gradient(circle at 30% 30%, rgba(16, 185, 129, 0.15) 0%, rgba(16, 185, 129, 0.08) 40%, transparent 70%),
    linear-gradient(135deg, rgba(5, 150, 105, 0.12) 0%, rgba(16, 185, 129, 0.06) 50%, transparent 100%);
  animation: float 8s ease-in-out infinite, shimmer 4s ease-in-out infinite alternate;
  box-shadow: 
    0 8px 32px rgba(16, 185, 129, 0.1),
    inset 0 1px 0 rgba(255, 255, 255, 0.2);
}

.shape-2 {
  width: 80px;
  height: 80px;
  bottom: -15px;
  right: 28%;
  background: 
    radial-gradient(circle at 70% 70%, rgba(5, 150, 105, 0.12) 0%, rgba(16, 185, 129, 0.06) 40%, transparent 70%),
    linear-gradient(225deg, rgba(16, 185, 129, 0.1) 0%, rgba(4, 120, 87, 0.05) 50%, transparent 100%);
  animation: float 10s ease-in-out infinite reverse, pulse 6s ease-in-out infinite;
  box-shadow: 
    0 6px 24px rgba(5, 150, 105, 0.08),
    inset 0 1px 0 rgba(255, 255, 255, 0.15);
}

.shape-3 {
  width: 100px;
  height: 100px;
  top: 45%;
  right: 3%;
  background: 
    radial-gradient(circle at 50% 20%, rgba(16, 185, 129, 0.14) 0%, rgba(5, 150, 105, 0.08) 45%, transparent 75%),
    linear-gradient(315deg, rgba(4, 120, 87, 0.1) 0%, rgba(16, 185, 129, 0.05) 60%, transparent 100%);
  animation: float 12s ease-in-out infinite, rotate 20s linear infinite;
  box-shadow: 
    0 10px 30px rgba(16, 185, 129, 0.12),
    inset 0 1px 0 rgba(255, 255, 255, 0.18);
}

/* Enhanced floating shapes with new ones */
.shape-4 {
  width: 60px;
  height: 60px;
  top: 20%;
  right: 40%;
  background: 
    radial-gradient(circle at 60% 40%, rgba(16, 185, 129, 0.1) 0%, transparent 60%);
  animation: float 9s ease-in-out infinite, fade 8s ease-in-out infinite alternate;
  border-radius: 60% 40% 30% 70% / 60% 30% 70% 40%;
}

.shape-5 {
  width: 40px;
  height: 40px;
  bottom: 30%;
  right: 8%;
  background: 
    linear-gradient(135deg, rgba(5, 150, 105, 0.08) 0%, rgba(16, 185, 129, 0.04) 100%);
  animation: float 7s ease-in-out infinite reverse, scale 5s ease-in-out infinite alternate;
  border-radius: 30% 70% 70% 30% / 30% 30% 70% 70%;
}

@keyframes float {
  0%, 100% { transform: translateY(0) translateX(0) rotate(0deg); }
  25% { transform: translateY(-12px) translateX(8px) rotate(5deg); }
  50% { transform: translateY(-20px) translateX(0) rotate(10deg); }
  75% { transform: translateY(-8px) translateX(-6px) rotate(5deg); }
}

@keyframes shimmer {
  0% { opacity: 0.6; filter: blur(0.5px) brightness(1); }
  100% { opacity: 0.9; filter: blur(0.3px) brightness(1.1); }
}

@keyframes pulse {
  0%, 100% { transform: scale(1); opacity: 0.7; }
  50% { transform: scale(1.1); opacity: 0.9; }
}

@keyframes rotate {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

@keyframes fade {
  0% { opacity: 0.4; }
  100% { opacity: 0.8; }
}

@keyframes scale {
  0% { transform: scale(0.8); }
  100% { transform: scale(1.2); }
}

.dark-mode-toggle {
  background: 
    linear-gradient(135deg, rgba(255, 255, 255, 0.95) 0%, rgba(248, 250, 252, 0.9) 100%);
  border: 2px solid rgba(16, 185, 129, 0.2);
  border-radius: 16px;
  padding: 0.875rem;
  cursor: pointer;
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  display: flex;
  align-items: center;
  justify-content: center;
  color: #10b981;
  width: 52px;
  height: 52px;
  box-shadow: 
    0 8px 20px rgba(16, 185, 129, 0.15),
    0 4px 10px rgba(0, 0, 0, 0.08),
    inset 0 1px 0 rgba(255, 255, 255, 0.8);
  backdrop-filter: blur(10px);
  position: relative;
  overflow: hidden;
}

.dark-mode-toggle::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(135deg, rgba(16, 185, 129, 0.1) 0%, transparent 100%);
  opacity: 0;
  transition: opacity 0.3s ease;
}

.dark-mode-toggle:hover::before {
  opacity: 1;
}

.dark-mode-toggle:hover {
  border-color: rgba(16, 185, 129, 0.35);
  transform: translateY(-2px) scale(1.05);
  box-shadow: 
    0 12px 30px rgba(16, 185, 129, 0.25),
    0 6px 15px rgba(0, 0, 0, 0.12),
    inset 0 1px 0 rgba(255, 255, 255, 0.9);
  color: #059669;
}

.subjects-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(450px, 1fr));
  gap: 2rem;
  align-items: stretch;
}

.subject-card,
.section-card {
  background: 
    linear-gradient(135deg, rgba(255, 255, 255, 0.98) 0%, rgba(248, 250, 252, 0.95) 100%);
  border-radius: 24px;
  padding: 2.5rem;
  box-shadow: 
    0 12px 40px rgba(16, 185, 129, 0.12),
    0 6px 20px rgba(0, 0, 0, 0.08),
    0 3px 10px rgba(16, 185, 129, 0.06),
    inset 0 1px 0 rgba(255, 255, 255, 0.9);
  border: 2px solid rgba(16, 185, 129, 0.08);
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  position: relative;
  overflow: hidden;
  backdrop-filter: blur(10px);
}

.subject-card::before,
.section-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 6px;
  background: 
    linear-gradient(90deg, #10b981 0%, #059669 50%, #047857 100%),
    linear-gradient(180deg, rgba(255, 255, 255, 0.3) 0%, transparent 100%);
  border-radius: 24px 24px 0 0;
}

.subject-card::after,
.section-card::after {
  content: '';
  position: absolute;
  top: 20px;
  right: 20px;
  width: 60px;
  height: 60px;
  border-radius: 50%;
  background: 
    radial-gradient(circle at 30% 30%, rgba(16, 185, 129, 0.08) 0%, transparent 70%);
  opacity: 0;
  transition: opacity 0.3s ease;
}

.subject-card:hover::after,
.section-card:hover::after {
  opacity: 1;
}

.subject-card:hover,
.section-card:hover {
  transform: translateY(-6px) scale(1.02);
  border-color: rgba(16, 185, 129, 0.2);
  box-shadow: 
    0 20px 60px rgba(16, 185, 129, 0.18),
    0 10px 30px rgba(0, 0, 0, 0.12),
    0 5px 15px rgba(16, 185, 129, 0.1),
    inset 0 1px 0 rgba(255, 255, 255, 0.95);
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
  background: 
    linear-gradient(135deg, #10b981 0%, #059669 50%, #047857 100%),
    linear-gradient(225deg, rgba(255, 255, 255, 0.2) 0%, transparent 50%);
  color: white;
  padding: 0.5rem 1.25rem;
  border-radius: 25px;
  font-size: 0.85rem;
  font-weight: 700;
  display: inline-block;
  margin-bottom: 0.5rem;
  box-shadow: 
    0 6px 20px rgba(16, 185, 129, 0.3),
    0 3px 10px rgba(16, 185, 129, 0.2),
    inset 0 1px 0 rgba(255, 255, 255, 0.25),
    inset 0 -1px 0 rgba(0, 0, 0, 0.1);
  letter-spacing: 0.025em;
  transition: all 0.3s ease;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
}

.grade-level:hover {
  transform: translateY(-1px) scale(1.05);
  box-shadow: 
    0 8px 25px rgba(16, 185, 129, 0.4),
    0 4px 12px rgba(16, 185, 129, 0.25),
    inset 0 1px 0 rgba(255, 255, 255, 0.3);
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
  gap: 0.3rem;
  padding: 0.4rem 0.7rem;
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
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 0.75rem;
  flex: 1;
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
  margin: 0;
  padding: 1.5rem;
  background: 
    linear-gradient(135deg, rgba(240, 253, 244, 0.8) 0%, rgba(255, 255, 255, 0.9) 100%);
  border-radius: 18px;
  border: 2px solid rgba(16, 185, 129, 0.15);
  position: relative;
  overflow: hidden;
  transition: all 0.3s ease;
}

.section-code-area::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 4px;
  background: linear-gradient(90deg, #10b981 0%, #059669 50%, #047857 100%);
  border-radius: 18px 18px 0 0;
}

.section-code-area:hover {
  transform: translateY(-1px);
  box-shadow: 
    0 8px 25px rgba(16, 185, 129, 0.15),
    0 4px 12px rgba(16, 185, 129, 0.1);
  border-color: rgba(16, 185, 129, 0.25);
}

.section-code-area h4 {
  color: #047857;
  font-size: 1.1rem;
  font-weight: 700;
  margin-bottom: 1rem;
  letter-spacing: 0.5px;
  text-transform: uppercase;
  text-shadow: 0 1px 2px rgba(16, 185, 129, 0.1);
}

.section-info-container {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.section-info-grid {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  align-items: center;
  gap: 1.2rem;
  background: linear-gradient(135deg, rgba(16, 185, 129, 0.08) 0%, rgba(240, 253, 244, 0.6) 100%);
  border-radius: 10px;
  padding: 0.7rem 1.2rem;
  border: 2px solid rgba(16, 185, 129, 0.15);
  position: relative;
  overflow: hidden;
  backdrop-filter: blur(2px);
  transition: all 0.3s ease;
}

.section-info-grid::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 3px;
  background: linear-gradient(90deg, #10b981 0%, #059669 50%, #047857 100%);
  border-radius: 20px 20px 0 0;
}

.section-info-grid:hover {
  transform: translateY(-2px);
  box-shadow: 
    0 12px 30px rgba(16, 185, 129, 0.2),
    0 6px 15px rgba(16, 185, 129, 0.1);
  border-color: rgba(16, 185, 129, 0.25);
}

.section-info-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 0.3rem;
  min-width: 0;
  position: relative;
}

.info-label {
  font-size: 0.9rem;
  font-weight: 700;
  color: #047857;
  text-transform: uppercase;
  letter-spacing: 1px;
  margin-bottom: 0.25rem;
  text-shadow: 0 1px 2px rgba(16, 185, 129, 0.1);
}

.info-value {
  font-size: 1.1rem;
  font-weight: 600;
  color: #065f46;
  word-break: break-word;
  text-align: center;
  padding: 0.25rem 0.5rem;
  background: rgba(255, 255, 255, 0.6);
  border-radius: 12px;
  border: 1px solid rgba(16, 185, 129, 0.1);
  border-radius: 6px;
  padding: 0.3rem 0.7rem;
}

.info-value:hover {
  background: rgba(255, 255, 255, 0.8);
  transform: scale(1.05);
  box-shadow: 0 4px 12px rgba(16, 185, 129, 0.15);
}

.section-code-display {
  display: flex;
  align-items: center;
  gap: 1.5rem;
  padding: 1rem 1.5rem;
  background: 
    linear-gradient(135deg, rgba(255, 255, 255, 0.95) 0%, rgba(240, 253, 244, 0.8) 100%);
  border-radius: 16px;
  border: 2px solid rgba(16, 185, 129, 0.2);
    border-radius: 6px;
    padding: 0.15rem 0.4rem;
  transition: all 0.3s ease;
  box-shadow: 
    0 6px 20px rgba(16, 185, 129, 0.1),
    inset 0 1px 0 rgba(255, 255, 255, 0.8);
}

.section-code-display:hover {
  transform: translateY(-1px);
  box-shadow: 
    0 10px 30px rgba(16, 185, 129, 0.15),
    0 5px 15px rgba(16, 185, 129, 0.08),
    inset 0 1px 0 rgba(255, 255, 255, 0.9);
  border-color: rgba(16, 185, 129, 0.3);
}

.section-code {
  font-family: 'Courier New', 'Monaco', 'Menlo', monospace;
  font-weight: 800;
  font-size: 1.3rem;
  color: #047857;
  background: 
    linear-gradient(135deg, #ffffff 0%, #f0fdf4 100%);
  padding: 0.75rem 1.5rem;
  border-radius: 12px;
  border: 2px solid rgba(16, 185, 129, 0.2);
  letter-spacing: 2px;
  text-align: center;
  min-width: 200px;
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
  box-shadow: 
    0 4px 12px rgba(16, 185, 129, 0.15),
    inset 0 1px 0 rgba(255, 255, 255, 0.8);
}

.section-code::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(16, 185, 129, 0.1), transparent);
  transition: left 0.6s;
}

.section-code:hover {
  transform: scale(1.02);
  color: #065f46;
  border-color: rgba(16, 185, 129, 0.4);
  box-shadow: 
    0 6px 18px rgba(16, 185, 129, 0.2),
    inset 0 1px 0 rgba(255, 255, 255, 0.9);
}

.section-code:hover::before {
  left: 100%;
}

.copy-code-btn {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.875rem 1.5rem;
  background: 
    linear-gradient(135deg, #10b981 0%, #059669 50%, #047857 100%),
    linear-gradient(225deg, rgba(255, 255, 255, 0.15) 0%, transparent 50%);
  color: white;
  border: none;
  border-radius: 14px;
  cursor: pointer;
  font-size: 0.9rem;
  font-weight: 700;
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  position: relative;
  overflow: hidden;
  box-shadow: 
    0 6px 20px rgba(16, 185, 129, 0.3),
    0 3px 10px rgba(16, 185, 129, 0.2),
    inset 0 1px 0 rgba(255, 255, 255, 0.25);
  letter-spacing: 0.5px;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
}

.copy-code-btn::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.25), transparent);
  transition: left 0.6s;
}

.copy-code-btn:hover::before {
  left: 100%;
}

.copy-code-btn:hover {
  background: 
    linear-gradient(135deg, #059669 0%, #047857 50%, #065f46 100%),
    linear-gradient(225deg, rgba(255, 255, 255, 0.2) 0%, transparent 50%);
  transform: translateY(-2px) scale(1.02);
  box-shadow: 
    0 10px 30px rgba(16, 185, 129, 0.4),
    0 5px 15px rgba(16, 185, 129, 0.25),
    inset 0 1px 0 rgba(255, 255, 255, 0.3);
}

.copy-code-btn:active {
  transform: translateY(-1px) scale(0.98);
  transition: all 0.1s ease;
}

.section-actions-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
  gap: 0.4rem;
    gap: 0.15rem;
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
  padding: 1rem 1.5rem;
  border: none;
  border-radius: 16px;
  cursor: pointer;
    border-radius: 6px;
    padding: 0.15rem 0.4rem;
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  text-align: center;
  min-height: 48px;
  position: relative;
  overflow: hidden;
  box-shadow: 
    0 6px 20px rgba(0, 0, 0, 0.1),
    0 3px 10px rgba(0, 0, 0, 0.05),
    inset 0 1px 0 rgba(255, 255, 255, 0.2);
  letter-spacing: 0.025em;
}

.section-action-btn::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.25), transparent);
  transition: left 0.6s;
}

.section-action-btn:hover::before {
  left: 100%;
}

.section-action-btn:hover {
  transform: translateY(-2px) scale(1.02);
  box-shadow: 
    0 10px 30px rgba(0, 0, 0, 0.15),
    0 5px 15px rgba(0, 0, 0, 0.08),
    inset 0 1px 0 rgba(255, 255, 255, 0.3);
}

.create-quiz {
  background: 
    linear-gradient(135deg, #10b981 0%, #059669 50%, #047857 100%),
    linear-gradient(225deg, rgba(255, 255, 255, 0.15) 0%, transparent 50%);
  color: white;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
}

.create-quiz:hover {
  background: 
    linear-gradient(135deg, #059669 0%, #047857 50%, #065f46 100%),
    linear-gradient(225deg, rgba(255, 255, 255, 0.2) 0%, transparent 50%);
  box-shadow: 
    0 12px 35px rgba(16, 185, 129, 0.35),
    0 6px 18px rgba(16, 185, 129, 0.2),
    inset 0 1px 0 rgba(255, 255, 255, 0.3);
}

.view-students {
  background: 
    linear-gradient(135deg, #3b82f6 0%, #2563eb 50%, #1d4ed8 100%),
    linear-gradient(225deg, rgba(255, 255, 255, 0.15) 0%, transparent 50%);
  color: white;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
}

.view-students:hover {
  background: 
    linear-gradient(135deg, #2563eb 0%, #1d4ed8 50%, #1e40af 100%),
    linear-gradient(225deg, rgba(255, 255, 255, 0.2) 0%, transparent 50%);
  box-shadow: 
    0 12px 35px rgba(59, 130, 246, 0.35),
    0 6px 18px rgba(59, 130, 246, 0.2),
    inset 0 1px 0 rgba(255, 255, 255, 0.3);
}

.view-quizzes {
  background: 
    linear-gradient(135deg, #14b8a6 0%, #0f766e 50%, #0d9488 100%),
    linear-gradient(225deg, rgba(255, 255, 255, 0.15) 0%, transparent 50%);
  color: white;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
}

.view-quizzes:hover {
  background: 
    linear-gradient(135deg, #0f766e 0%, #0d9488 50%, #0f766e 100%),
    linear-gradient(225deg, rgba(255, 255, 255, 0.2) 0%, transparent 50%);
  box-shadow: 
    0 12px 35px rgba(20, 184, 166, 0.35),
    0 6px 18px rgba(20, 184, 166, 0.2),
    inset 0 1px 0 rgba(255, 255, 255, 0.3);
}

.manage-grades {
  background: 
    linear-gradient(135deg, #ea580c 0%, #dc2626 50%, #b91c1c 100%),
    linear-gradient(225deg, rgba(255, 255, 255, 0.15) 0%, transparent 50%);
  color: white;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
}

.manage-grades:hover {
  background: 
    linear-gradient(135deg, #dc2626 0%, #b91c1c 50%, #991b1b 100%),
    linear-gradient(225deg, rgba(255, 255, 255, 0.2) 0%, transparent 50%);
  box-shadow: 
    0 12px 35px rgba(234, 88, 12, 0.35),
    0 6px 18px rgba(234, 88, 12, 0.2),
    inset 0 1px 0 rgba(255, 255, 255, 0.3);
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

/* Subject-specific styles */
.subject-card {
  background: rgba(255, 255, 255, 0.95);
  border-radius: 20px;
  padding: 0;
  box-shadow: 0 8px 32px rgba(16, 185, 129, 0.1);
  border: 1px solid rgba(16, 185, 129, 0.1);
  transition: all 0.3s ease;
  overflow: hidden;
}

.subject-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 2rem;
  cursor: pointer;
  transition: all 0.3s ease;
  background: linear-gradient(135deg, rgba(16, 185, 129, 0.05) 0%, rgba(5, 150, 105, 0.02) 100%);
}

.subject-header:hover {
  background: linear-gradient(135deg, rgba(16, 185, 129, 0.1) 0%, rgba(5, 150, 105, 0.05) 100%);
}

.subject-info h3 {
  color: #10b981;
  font-size: 1.8rem;
  font-weight: 700;
  margin-bottom: 0.5rem;
}

.subject-description {
  color: #666;
  font-size: 1rem;
  margin-top: 0.5rem;
  font-style: italic;
}

.expand-icon {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: rgba(16, 185, 129, 0.1);
  color: #10b981;
  transition: all 0.3s ease;
}

.expand-icon svg {
  transition: transform 0.3s ease;
}

.expand-icon svg.rotated {
  transform: rotate(180deg);
}

.sections-container {
  border-top: 1px solid rgba(16, 185, 129, 0.1);
  background: rgba(255, 255, 255, 0.5);
}

.sections-container .section-card {
  margin: 1rem;
  padding: 1.5rem;
  border-radius: 15px;
  background: white;
  border: 1px solid rgba(16, 185, 129, 0.08);
  box-shadow: 0 4px 16px rgba(16, 185, 129, 0.08);
}

.sections-container .section-card:last-child {
  margin-bottom: 1rem;
}

.section-info h4 {
  color: #059669;
  font-size: 1.3rem;
  font-weight: 600;
  margin-bottom: 0.5rem;
}

.section-code-display {
  color: #666;
  font-size: 0.9rem;
  margin-bottom: 1rem;
}

/* Responsive adjustments for new layout */
@media (max-width: 768px) {
  .subject-header {
    flex-direction: column;
    align-items: flex-start;
    gap: 1rem;
  }
  
  .subject-stats {
    flex-direction: column;
    gap: 1rem;
  }
  
  .expand-icon {
    align-self: flex-end;
  }
}

/* Three-level hierarchy styles */
.subject-card.simple {
  padding: 2rem;
  cursor: pointer;
  background: rgba(255, 255, 255, 0.95);
  border-radius: 20px;
  box-shadow: 0 8px 32px rgba(16, 185, 129, 0.1);
  border: 2px solid #10b981;
  box-sizing: border-box;
  transition: all 0.3s ease;
  min-height: 160px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.dark-mode .subject-card.simple {
  background: rgba(30, 35, 34, 0.95) !important;
  color: #e0e0e0 !important;
  border: 2px solid #10b981 !important;

}


.subject-card.simple:hover {
  transform: translateY(-4px);
  box-shadow: 0 0 0 4px #10b981, 0 16px 48px rgba(16, 185, 129, 0.35);
  border-color: #10b981;
}

.subject-simple-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.subject-simple-header h3 {
  color: #10b981;
  font-size: 1.8rem;
  font-weight: 700;
  margin-bottom: 0.5rem;
}

.subject-stats-simple {
  color: #666;
  font-size: 1rem;
  margin-top: 0.5rem;
}

.arrow-icon {
  color: #10b981;
  transition: all 0.3s ease;
}

.subject-card.simple:hover .arrow-icon {
  transform: translateX(4px);
}

.breadcrumb {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 2rem;
  padding: 0;
}

.breadcrumb-btn {
  background: linear-gradient(135deg, rgba(16, 185, 129, 0.05), rgba(5, 150, 105, 0.05));
  border: 2px solid rgba(16, 185, 129, 0.15);
  border-radius: 12px;
  padding: 0.7rem 1.4rem;
  color: #10b981;
  font-weight: 700;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 0.6rem;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  font-size: 0.95rem;
  position: relative;
  overflow: hidden;
  box-shadow: 0 2px 6px rgba(16, 185, 129, 0.06);
}

.breadcrumb-btn::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(16, 185, 129, 0.1), transparent);
  transition: left 0.4s ease;
}

.breadcrumb-btn:hover {
  background: linear-gradient(135deg, #f0fdf4, #dcfce7);
  border-color: #10b981;
  color: #065f46;
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(16, 185, 129, 0.15);
}

.breadcrumb-btn:hover::before {
  left: 100%;
}

.breadcrumb-separator {
  color: #94a3b8;
  font-weight: 500;
  font-size: 1.2rem;
  margin: 0 0.3rem;
}

.breadcrumb-current {
  color: #1e293b;
  font-weight: 800;
  font-size: 1rem;
  background: linear-gradient(135deg, #10b981, #059669);
  background-clip: text;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  padding: 0.2rem 0;
}

.sections-view,
.section-detail-view {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 1rem;
}

.grade-filter-container {
  display: flex;
  gap: 0.8rem;
  margin-bottom: 2rem;
  padding: 0;
  flex-wrap: wrap;
}

.grade-filter-btn {
  background: linear-gradient(135deg, rgba(255,255,255,0.7), rgba(248,250,252,0.7)); /* less intense glass effect */
  border: 2px solid rgba(16,185,129,0.10); /* softer border */
  border-radius: 12px;
  padding: 0.5rem 1rem;
  cursor: pointer;
  font-weight: 600;
  font-size: 0.8rem;
  color: #475569;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  white-space: nowrap;
  position: relative;
  overflow: hidden;
  box-shadow: 0 1.5px 6px rgba(16,185,129,0.04); /* softer shadow */
  text-transform: uppercase;
  letter-spacing: 0.3px;
}

.grade-filter-btn::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(16, 185, 129, 0.1), transparent);
  transition: left 0.5s ease;
}

.grade-filter-btn:hover {
  border-color: #10b981;
  color: #065f46;
  background: linear-gradient(135deg, #f0fdf4, #dcfce7);
  transform: translateY(-3px);
  box-shadow: 
    0 4px 12px rgba(16,185,129,0.12),
    0 2px 6px rgba(16,185,129,0.08); /* softer hover shadow */
}

.grade-filter-btn:hover::before {
  left: 100%;
}

.grade-filter-btn.active {
  background: linear-gradient(135deg, #10b981 0%, #059669 100%);
  border-color: #10b981;
  color: white;
  transform: translateY(-2px);
  box-shadow: 
    0 4px 16px rgba(16,185,129,0.18),
    0 2px 8px rgba(16,185,129,0.12),
    inset 0 1px 0 rgba(255,255,255,0.15); /* softer active shadow */
}

.grade-filter-btn.active::before {
  display: none;
}

.sections-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 2rem;
  justify-items: center;
}

.section-card.simple {
  padding: 0.75rem 1.5rem 1.5rem 1.5rem; /* Reduce top padding to make the top area less tall */
  cursor: pointer;
  background: rgba(255, 255, 255, 0.95);
  border-radius: 15px;
  box-shadow: 0 4px 16px rgba(16, 185, 129, 0.08);
  border: 2px solid #10b981;
  box-sizing: border-box;
  transition: all 0.3s ease;
  /* aspect-ratio removed to make card rectangular */
  width: 100%;
  max-width: 350px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.section-card.simple:hover {
  transform: translateY(-4px) scale(1.02);
  box-shadow: 0 12px 32px rgba(16, 185, 129, 0.15), 0 4px 12px rgba(0, 0, 0, 0.1);
  border-color: #10b981;
  background: linear-gradient(135deg, #ecfdf5 0%, #d1fae5 50%, #a7f3d0 100%);
}

.card-corner-accent {
  position: absolute;
  top: 0;
  right: 0;
  width: 32px;
  height: 32px;
  background: linear-gradient(45deg, transparent 50%, rgba(16, 185, 129, 0.1) 50%);
  border-radius: 0 16px 0 100%;
}

.card-icon {
  position: absolute;
  top: 12px;
  left: 12px;
  color: #10b981;
  opacity: 0.8;
  transition: all 0.3s ease;
}

.section-card.simple:hover .card-icon {
  opacity: 1;
  transform: scale(1.1);
}

.section-simple-header {
  display: flex;
  flex-direction: column;
  width: 100%;
  gap: 1rem;
  z-index: 2;
  position: relative;
  flex: 1;
}

.section-simple-header h4 {
  color: #047857;
  font-size: 1.15rem;
  font-weight: 700;
  margin-bottom: 0.1rem;
  text-align: center;
  line-height: 1.3;
  letter-spacing: -0.025em;
}

.section-info {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 0.75rem;
  flex: 1;
}

.section-stats-simple {
  color: #666;
  font-size: 0.9rem;
}

/* Section Code Inline Display */
.section-code-inline {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  margin: 0.5rem 0;
  padding: 0.25rem 0.5rem;
  background: rgba(16, 185, 129, 0.05);
  border-radius: 8px;
  border: 1px solid rgba(16, 185, 129, 0.15);
}

.code-label {
  font-size: 0.75rem;
  color: #065f46;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.section-code-text {
  font-family: 'Courier New', monospace;
  font-size: 0.8rem;
  color: #047857;
  font-weight: 700;
  cursor: pointer;
  padding: 0.125rem 0.25rem;
  border-radius: 4px;
  transition: all 0.2s ease;
}

.section-code-text:hover {
  background: rgba(16, 185, 129, 0.1);
  color: #10b981;
}

.copy-code-mini {
  background: none;
  border: none;
  color: #10b981;
  cursor: pointer;
  padding: 0.125rem;
  border-radius: 4px;
  transition: all 0.2s ease;
  display: flex;
  align-items: center;
  justify-content: center;
}

.copy-code-mini:hover {
  background: rgba(16, 185, 129, 0.1);
  transform: scale(1.1);
}

/* Section actions row for horizontal alignment */
.section-actions-row {
  display: flex;
  align-items: center;
  justify-content: flex-end;
  gap: 0.5rem;
  width: 100%;
  margin-bottom: 0.5rem;
}

.section-action-btn {
  background: none;
  border: none;
  padding: 0.3rem 0.5rem;
  border-radius: 6px;
  cursor: pointer;
  color: #10b981;
  display: flex;
  align-items: center;
  transition: background 0.2s;
}

.section-action-btn.view-students {
  background: linear-gradient(135deg, #3b82f6, #2563eb);
  color: #fff;
}
.section-action-btn.view-students:hover {
  background: linear-gradient(135deg, #2563eb, #1d4ed8);
  box-shadow: 0 8px 24px rgba(59, 130, 246, 0.3);
}
.section-action-btn.create-quiz {
  background: linear-gradient(135deg, #10b981, #059669);
  color: #fff;
}
.section-action-btn.create-quiz:hover {
  background: linear-gradient(135deg, #059669, #047857);
  box-shadow: 0 8px 24px rgba(16, 185, 129, 0.3);
}
.section-action-btn.view-quizzes {
  background: linear-gradient(135deg, #06b6d4, #0891b2);
  color: #fff;
}
.section-action-btn.view-quizzes:hover {
  background: linear-gradient(135deg, #0891b2, #0e7490);
  box-shadow: 0 8px 24px rgba(6, 182, 212, 0.3);
}
.section-action-btn.manage-grades {
  background: linear-gradient(135deg, #f59e0b, #d97706);
  color: #fff;
}
.section-action-btn.manage-grades:hover {
  background: linear-gradient(135deg, #d97706, #b45309);
  box-shadow: 0 8px 24px rgba(245, 158, 11, 0.3);
}

.section-action-btn:hover {
  background: rgba(16,185,129,0.1);
}

.section-action-btn.delete {
  color: #ef4444;
}

.section-action-btn.delete:hover {
  background: rgba(239,68,68,0.1);
}

.section-action-btn.menu {
  color: #64748b;
}

.section-action-btn.menu:hover {
  background: rgba(100,116,139,0.1);
}

.section-status {
  font-size: 0.8rem;
  font-weight: 500;
  padding: 0.2rem 0.6rem;
  border-radius: 12px;
  background: #dcfce7;
  color: #16a34a;
  margin-right: 0.5rem;
}

.section-status.archived {
  background: #fef2f2;
  color: #dc2626;
}

/* Section menu dropdown */
.section-menu-container {
  position: relative;
}

.section-dropdown-menu {
  position: absolute;
  top: 110%;
  right: -16px;
  background: white;
  border: 1px solid #e5e7eb;
  border-radius: 12px;
  box-shadow: 0 8px 24px rgba(0,0,0,0.18), 0 1.5px 6px rgba(0,0,0,0.10);
  z-index: 2000;
  min-width: 150px;
  padding: 0.75rem 0;
  opacity: 1;
  pointer-events: auto;
  box-sizing: border-box;
  /* Visually floats outside the card */
}

.menu-item {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  width: 100%;
  padding: 0.5rem 1rem;
  background: none;
  border: none;
  color: #374151;
  font-size: 0.9rem;
  cursor: pointer;
  transition: background 0.2s;
}

.menu-item:hover {
  background: #f3f4f6;
}

.menu-item.delete {
  color: #ef4444;
}

.menu-item.delete:hover {
  background: #fef2f2;
}

.section-detail-card {
  background: 
    linear-gradient(135deg, rgba(255, 255, 255, 0.98) 0%, rgba(240, 253, 244, 0.95) 50%, rgba(236, 253, 245, 0.9) 100%),
    linear-gradient(225deg, rgba(16, 185, 129, 0.03) 0%, transparent 60%);
  border-radius: 6px;
  padding: 0.4rem 0.6rem 0.7rem 0.6rem;
  box-shadow: 
    0 12px 30px rgba(16, 185, 129, 0.12),
    0 6px 15px rgba(0, 0, 0, 0.06),
    0 3px 8px rgba(16, 185, 129, 0.06),
    inset 0 1px 0 rgba(255, 255, 255, 0.9),
    inset 0 0 0 2px rgba(16, 185, 129, 0.08);
  border: 2px solid rgba(16, 185, 129, 0.12);
  position: relative;
  overflow: hidden;
  backdrop-filter: blur(6px);
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  color: #1f2937;
  font-size: 1rem;
  margin-bottom: 1.2rem;
  min-height: auto;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.section-detail-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 6px;
  background: 
    linear-gradient(90deg, #10b981 0%, #059669 50%, #047857 100%),
    linear-gradient(180deg, rgba(255, 255, 255, 0.3) 0%, transparent 100%);
  border-radius: 28px 28px 0 0;
}

.section-detail-card::after {
  content: '';
  position: absolute;
  top: 36px;
  right: 36px;
  width: 38px;
  height: 38px;
  border-radius: 50%;
  background: 
    radial-gradient(circle at 30% 30%, rgba(16, 185, 129, 0.12) 0%, transparent 70%);
  opacity: 0.6;
  transition: opacity 0.3s ease;
}

.section-detail-card:hover {
  transform: translateY(-4px) scale(1.01);
  box-shadow: 
    0 30px 70px rgba(16, 185, 129, 0.2),
    0 15px 35px rgba(0, 0, 0, 0.12),
    0 8px 18px rgba(16, 185, 129, 0.15),
    inset 0 1px 0 rgba(255, 255, 255, 0.95),
    inset 0 0 0 2px rgba(16, 185, 129, 0.12);
  border-color: rgba(16, 185, 129, 0.2);
}

.section-detail-card:hover::after {
  opacity: 1;
}

@media (max-width: 768px) {
  .sections-grid {
    grid-template-columns: 1fr;
  }
  
  .subject-simple-header,
  .section-simple-header {
    flex-direction: column;
    align-items: flex-start;
    gap: 1rem;
  }
  
  .arrow-icon {
    align-self: flex-end;
  }
  
  .grade-filter-container {
    justify-content: center;
    gap: 0.5rem;
  }
  
  .grade-filter-btn {
    padding: 0.5rem 1rem;
    font-size: 0.8rem;
  }
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
  gap: 0.5rem;
  margin-bottom: 0.5rem;
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
  background: #111111;
  border: 2px solid #10b981;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
  color: #e9ecef;
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

/* Additional Dark Mode Styles for Section Detail View */
.dark-mode .breadcrumb {
  color: var(--secondary-text-color);
}

.dark-mode .breadcrumb-btn {
  background: linear-gradient(135deg, rgba(95, 179, 160, 0.08), rgba(74, 155, 135, 0.08));
  color: var(--accent-color);
  border: 2px solid var(--border-color);
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.15);
}

.dark-mode .breadcrumb-btn::before {
  background: linear-gradient(90deg, transparent, rgba(95, 179, 160, 0.2), transparent);
}

.dark-mode .breadcrumb-btn:hover {
  background: linear-gradient(135deg, var(--bg-accent-hover), rgba(95, 179, 160, 0.15));
  color: var(--accent-color);
  border-color: var(--accent-color);
  box-shadow: 0 6px 20px rgba(95, 179, 160, 0.2);
}

.dark-mode .breadcrumb-separator {
  color: var(--secondary-text-color);
}

.dark-mode .breadcrumb-current {
  color: var(--primary-text-color);
  background: linear-gradient(135deg, var(--accent-color), #4a9b87);
  background-clip: text;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.dark-mode .grade-filter-btn {
  background: linear-gradient(135deg, var(--bg-card), var(--bg-accent));
  color: var(--secondary-text-color);
  border: 2px solid var(--border-color);
  box-shadow: 0 1.5px 6px rgba(0,0,0,0.10); /* softer shadow for dark mode */
}

.dark-mode .grade-filter-btn::before {
  background: linear-gradient(90deg, transparent, rgba(95, 179, 160, 0.2), transparent);
}

.dark-mode .grade-filter-btn:hover {
  background: linear-gradient(135deg, var(--bg-accent-hover), rgba(95,179,160,0.10)); /* less intense hover */
  color: var(--accent-color);
  border-color: var(--accent-color);
  box-shadow: 
    0 4px 12px rgba(95,179,160,0.12),
    0 2px 6px rgba(0,0,0,0.10); /* softer hover shadow for dark mode */
}

.dark-mode .grade-filter-btn.active {
  background: linear-gradient(135deg, var(--accent-color), #4a9b87);
  color: white;
  border-color: var(--accent-color);
  box-shadow: 
    0 4px 16px rgba(95,179,160,0.18),
    0 2px 8px rgba(95,179,160,0.12),
    inset 0 1px 0 rgba(255,255,255,0.15); /* softer active shadow for dark mode */
}

.dark-mode .section-detail-card {
  background: var(--bg-secondary);
  border: 1px solid var(--border-color);
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
}

.dark-mode .section-detail-header h2 {
  color: var(--primary-text-color);
}

.dark-mode .section-code-text {
  color: var(--secondary-text-color);
}

.dark-mode .section-stats-simple {
  color: var(--secondary-text-color);
}

/* Dark mode styles for section actions */
.dark-mode .section-action-btn {
  color: var(--accent-color);
}

.dark-mode .section-action-btn:hover {
  background: rgba(95,179,160,0.1);
}

.dark-mode .section-action-btn.delete {
  color: #f87171;
}

.dark-mode .section-action-btn.delete:hover {
  background: rgba(248,113,113,0.1);
}

.dark-mode .section-action-btn.menu {
  color: var(--secondary-text-color);
}

.dark-mode .section-action-btn.menu:hover {
  background: rgba(100,116,139,0.1);
}

.dark-mode .section-status {
  background: var(--bg-accent);
  color: var(--accent-color);
}

.dark-mode .section-status.archived {
  background: rgba(248,113,113,0.1);
  color: #f87171;
}

/* Dark mode dropdown menu */
.dark-mode .section-dropdown-menu {
  background: var(--bg-card);
  border-color: var(--border-color);
  box-shadow: 0 8px 24px rgba(0,0,0,0.38), 0 1.5px 6px rgba(0,0,0,0.20);
}

.dark-mode .menu-item {
  color: var(--primary-text-color);
}

.dark-mode .menu-item:hover {
  background: var(--bg-accent);
}

.dark-mode .menu-item.delete {
  color: #f87171;
}

.dark-mode .menu-item.delete:hover {
  background: rgba(248,113,113,0.1);
}

.dark-mode .subject-simple-header h3,
.dark-mode .section-simple-header h4 {
  color: #f9fafb;
}

.dark-mode .subject-simple-header p,
.dark-mode .section-simple-header p {
  color: #d1d5db;
}

.dark-mode .section-card.simple {
  background: rgba(30, 35, 34, 0.95) !important;
  border: 2px solid #10b981 !important;
  color: #e0e0e0 !important;
}

.dark-mode .section-card.simple:hover {
  background: rgba(30, 35, 34, 0.95) !important;
  border-color: #10b981 !important;
}

.dark-mode .card-corner-accent {
  background: linear-gradient(45deg, transparent 50%, rgba(16, 185, 129, 0.2) 50%);
}

.dark-mode .card-icon {
  color: #10b981;
}

.dark-mode .section-stats-simple {
  background: rgba(16, 185, 129, 0.2);
  border-color: rgba(16, 185, 129, 0.3);
    background: rgba(16, 185, 129, 0.18);
    box-shadow: 0 0 0 4px rgba(16, 185, 129, 0.18), 0 16px 48px rgba(16, 185, 129, 0.25);
  }
  .dark-mode .subject-card:active,
  .dark-mode .section-card:active {
    background: rgba(16, 185, 129, 0.18);
    box-shadow: 0 0 0 4px rgba(16, 185, 129, 0.18), 0 16px 48px rgba(16, 185, 129, 0.25);
  }

/* Dark mode for inline section code */
.dark-mode .section-code-inline {
  background: rgba(16, 185, 129, 0.1);
  border-color: rgba(16, 185, 129, 0.25);
}

.dark-mode .code-label {
  color: #a7f3d0;
}

.dark-mode .section-code-text {
  color: #10b981;
}

.dark-mode .section-code-text:hover {
  background: rgba(16, 185, 129, 0.2);
  color: #6ee7b7;
}

.dark-mode .copy-code-mini {
  color: #10b981;
}

.dark-mode .copy-code-mini:hover {
  background: rgba(16, 185, 129, 0.2);
}

.dark-mode .section-action-btn {
  color: white;
  border: none;
}

.dark-mode .section-action-btn.view-students {
  background: linear-gradient(135deg, #3b82f6, #2563eb);
}

.dark-mode .section-action-btn.view-students:hover {
  background: linear-gradient(135deg, #2563eb, #1d4ed8);
  box-shadow: 0 8px 24px rgba(59, 130, 246, 0.3);
}

.dark-mode .section-action-btn.create-quiz {
  background: linear-gradient(135deg, #10b981, #059669);
}

.dark-mode .section-action-btn.create-quiz:hover {
  background: linear-gradient(135deg, #059669, #047857);
  box-shadow: 0 8px 24px rgba(16, 185, 129, 0.3);
}

.dark-mode .section-action-btn.view-quizzes {
  background: linear-gradient(135deg, #06b6d4, #0891b2);
}

.dark-mode .section-action-btn.view-quizzes:hover {
  background: linear-gradient(135deg, #0891b2, #0e7490);
  box-shadow: 0 8px 24px rgba(6, 182, 212, 0.3);
}

.dark-mode .section-action-btn.manage-grades {
  background: linear-gradient(135deg, #f59e0b, #d97706);
}

.dark-mode .section-action-btn.manage-grades:hover {
  background: linear-gradient(135deg, #d97706, #b45309);
  box-shadow: 0 8px 24px rgba(245, 158, 11, 0.3);
}

.dark-mode .arrow-icon {
  color: var(--accent-color);
}

.dark-mode .create-quiz-btn {
  background: linear-gradient(135deg, var(--accent-color), #4a9b87);
  border-color: var(--accent-color);
}

.dark-mode .create-quiz-btn:hover {
  background: linear-gradient(135deg, #4a9b87, #3d8b78);
  box-shadow: 0 8px 24px rgba(95, 179, 160, 0.3);
}

/* Enhanced Dark Mode Styles for Section Detail View */
.dark-mode .section-detail-header {
  color: var(--primary-text-color);
}

.dark-mode .section-detail-header h2 {
  color: var(--accent-color);
}

.dark-mode .section-stats {
  background: var(--bg-card);
  border: 1px solid var(--border-color);
}

.dark-mode .section-stats .stat {
  background: var(--bg-accent);
  border: 1px solid var(--border-color);
}

.dark-mode .section-stats .stat:hover {
  background: var(--bg-accent-hover);
  border-color: var(--accent-color);
}

.dark-mode .section-stats .stat-number {
  color: var(--accent-color);
  font-weight: 700;
}

.dark-mode .section-stats .stat-label {
  color: var(--secondary-text-color);
}

.dark-mode .view-hint {
  color: var(--accent-color);
}

.dark-mode .clickable-link {
  color: var(--accent-color);
}

.dark-mode .section-code-area h4 {
  color: var(--primary-text-color);
}

.dark-mode .section-actions-grid {
  background: transparent;
}

/* Better contrast for action buttons in dark mode */
.dark-mode .action-btn.edit:hover {
  background: rgba(59, 130, 246, 0.3);
  color: #93c5fd;
}

.dark-mode .action-btn.delete:hover {
  background: rgba(239, 68, 68, 0.3);
  color: #fca5a5;
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

/* Dark Mode Styles for Section Detail Components */
.dark-mode .section-code-area {
  background: 
    linear-gradient(135deg, rgba(17, 24, 39, 0.8) 0%, rgba(31, 41, 55, 0.9) 100%) !important;
  border: 2px solid rgba(16, 185, 129, 0.25) !important;
  box-shadow: 
    0 4px 12px rgba(0, 0, 0, 0.3),
    0 2px 6px rgba(0, 0, 0, 0.2) !important;
  color: #e5e7eb !important;
}

.dark-mode .section-code-area:hover {
  box-shadow: 
    0 8px 25px rgba(0, 0, 0, 0.4),
    0 4px 12px rgba(0, 0, 0, 0.25) !important;
  border-color: rgba(16, 185, 129, 0.35) !important;
}

.dark-mode .section-code-area h4 {
  color: #10b981 !important;
}

.dark-mode .section-info-grid {
  background: 
    linear-gradient(135deg, rgba(17, 24, 39, 0.8) 0%, rgba(31, 41, 55, 0.9) 100%) !important;
  border: 2px solid rgba(16, 185, 129, 0.25) !important;
  box-shadow: 
    0 4px 12px rgba(0, 0, 0, 0.3),
    0 2px 6px rgba(0, 0, 0, 0.2) !important;
  color: #e5e7eb !important;
}

.dark-mode .section-info-grid:hover {
  box-shadow: 
    0 12px 30px rgba(0, 0, 0, 0.4),
    0 6px 15px rgba(0, 0, 0, 0.3) !important;
  border-color: rgba(16, 185, 129, 0.35) !important;
}

.dark-mode .section-code-display {
  background: 
    linear-gradient(135deg, rgba(17, 24, 39, 0.95) 0%, rgba(31, 41, 55, 0.8) 100%) !important;
  border: 2px solid rgba(16, 185, 129, 0.25) !important;
  box-shadow: 
    0 4px 12px rgba(0, 0, 0, 0.3),
    0 2px 6px rgba(0, 0, 0, 0.2) !important;
}

.dark-mode .section-code-display:hover {
  box-shadow: 
    0 8px 25px rgba(0, 0, 0, 0.4),
    0 4px 12px rgba(0, 0, 0, 0.25) !important;
  border-color: rgba(16, 185, 129, 0.35) !important;
}

.dark-mode .section-code {
  background: rgba(31, 41, 55, 0.9) !important;
  border: 2px solid rgba(16, 185, 129, 0.3) !important;
  color: #10b981 !important;
}

.dark-mode .info-label {
  color: #10b981 !important;
}

.dark-mode .info-value {
  color: #e5e7eb !important;
  background: rgba(31, 41, 55, 0.6) !important;
  border: 1px solid rgba(16, 185, 129, 0.2) !important;
}

.dark-mode .section-info-item {
  background: rgba(31, 41, 55, 0.4) !important;
  border: 1px solid rgba(16, 185, 129, 0.15) !important;
  border-radius: 8px !important;
  padding: 0.5rem !important;
}

.dark-mode .copy-code-btn {
  background: rgba(16, 185, 129, 0.8) !important;
  color: #fff !important;
  border: 1px solid rgba(16, 185, 129, 0.9) !important;
}

.dark-mode .copy-code-btn:hover {
  background: rgba(16, 185, 129, 1) !important;
  border-color: rgba(16, 185, 129, 1) !important;
}
</style>