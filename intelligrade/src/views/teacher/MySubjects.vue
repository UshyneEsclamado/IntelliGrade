/* Section Detail Enhancements */
.section-detail-card .info-label {
  color: #1f2937;
  font-weight: 600;
  display: inline-block;
  min-width: 100px;
.dark .section-detail-card .info-label {
  color: #A3D1C6;

.section-detail-card .info-value {
  color: #6b7280;
  font-weight: 500;
  margin-left: 0.5rem;
.dark .section-detail-card .info-value {
  color: #A3D1C6;

.section-code {
  background: #f8f9fa;
  color: #1f2937;
  border-radius: 8px;
  padding: 0.5rem 1rem;
  font-size: 1rem;
  font-weight: 600;
  display: inline-block;
.dark .section-code {
  background: #181c20;
  color: #A3D1C6;
  border: 1px solid #20c997;

.section-actions-grid {
  display: flex;
  gap: 1rem;
  margin-top: 1.5rem;
  justify-content: center;

/* Stats and Counts */
.section-stats-simple {
  color: #6b7280;
    
  /*
  |--------------------------------------------------------------------------
  | BASE STYLES (Light Mode)
  |--------------------------------------------------------------------------
  | Gi-uniform ug gi-simplify ang card structure ug elements.
  */
  .section-info-grid {
    background-color: #ffffff;
    border: 1px solid #e5e7eb;
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
    padding: 1.5rem;
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 1.5rem;
    transition: all 0.2s ease-in-out;
  }
  .section-info-grid:hover {
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
    border-color: #9ca3af;
    transform: translateY(-2px);
  }
  .section-detail-card {
    padding: 0;
  }
  .section-detail-card .info-label {
    color: #4b5563;
    font-weight: 600;
    display: block;
    margin-bottom: 0.25rem;
    font-size: 0.9rem;
  }
  .section-detail-card .info-value {
    color: #1f2937;
    font-weight: 500;
    margin-left: 0;
    display: block;
    font-size: 1rem;
  }
  .section-code {
    background: #f3f4f6;
    color: #1f2937;
    border-radius: 6px;
    padding: 0.25rem 0.75rem;
    font-size: 0.9rem;
    font-weight: 700;
    display: inline-block;
    font-family: 'Courier New', Courier, monospace;
    border: 1px solid #e5e7eb;
  }
  .section-actions-grid {
    display: flex;
    gap: 1rem;
    margin-top: 1.5rem;
    justify-content: flex-end;
  }
  /*
  |--------------------------------------------------------------------------
  | DARK MODE STYLES
  |--------------------------------------------------------------------------
  | Gamit ang green (#10b981) isip highlight color.
  */
  .dark-mode .section-info-grid {
    background-color: #1f2937;
    border: 1px solid #10b981;
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(16, 185, 129, 0.15);
    color: #e5e7eb;
  }
  .dark-mode .section-info-grid:hover {
    box-shadow: 0 8px 16px rgba(16, 185, 129, 0.3);
    border-color: #059669;
    transform: translateY(-2px);
  }
  .dark-mode .section-detail-card .info-label {
    color: #34d399;
  }
  .dark-mode .section-detail-card .info-value {
    color: #e5e7eb;
  }
  .dark-mode .section-code {
    background: rgba(16, 185, 129, 0.1);
    border: 1px solid #10b981;
    color: #10b981;
    font-family: 'Courier New', Courier, monospace;
  }

.dark .section-header-card {
  background: #23272b;
  border: 1px solid #20c997;
  box-shadow: 0 2px 8px rgba(0,0,0,0.25);

/* Simple, compact card style */
.section-card.simple, .section-detail-card {
  background: #fff;
  border: 1px solid #e0e0e0;
  border-radius: 12px;
  box-shadow: 0 1px 4px rgba(0,0,0,0.04);
  padding: 1rem 1.1rem;
  margin-bottom: 0.7rem;
  transition: box-shadow 0.18s, border 0.18s, background 0.18s;
}
.section-card.simple:hover {
  background: #f6f8fa;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  border-color: var(--color-primary);
}
.dark .section-card.simple, .dark .section-detail-card {
  background: #23272b;
  border: 1px solid #20c997;
  box-shadow: 0 2px 8px rgba(0,0,0,0.13);
}

/* Text Colors */
.section-info h4,
.section-detail-card h4,
.info-label,
.card-header h3 {
  color: #1f2937;
  font-weight: 600;
}
.dark .section-info h4,
.dark .section-detail-card h4,
.dark .info-label,
.dark .card-header h3 {
  color: #A3D1C6;
}

.info-value,
.section-stats-simple {
  color: #6b7280;
}
.dark .info-value,
.dark .section-stats-simple {
  color: #A3D1C6;
}

/* Simple, compact buttons */
.breadcrumb-btn, .grade-filter-btn, .section-action-btn {
  background: var(--color-primary);
  color: #fff;
  border: none;
  border-radius: 7px;
  padding: 0.45rem 1.1rem;
  font-size: 0.97rem;
  font-weight: 600;
  cursor: pointer;
  transition: background 0.18s, box-shadow 0.18s;
  display: flex;
  align-items: center;
  gap: 0.4rem;
  box-shadow: 0 1px 3px rgba(0,0,0,0.03);
}
.breadcrumb-btn:hover, .grade-filter-btn:hover, .section-action-btn:hover {
  background: var(--color-primary-dark);
  box-shadow: 0 2px 6px rgba(0,0,0,0.08);
}

/* Code Area Styling */
.section-code-area,
.section-code-inline {
  background: #f8f9fa;
  border-radius: 8px;
  padding: 1rem;
  margin: 1rem 0;
}
.dark .section-code-area,
.dark .section-code-inline {
  background: #181c20;
  border: 1px solid #20c997;
}
/* Grid Layouts */
.sections-grid {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

/* Section Card Content */
.section-simple-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.section-info {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.section-info h4 {
  color: #1f2937;
  font-size: 1.125rem;
  font-weight: 600;
  margin: 0;
}
.dark .section-info h4 {
  color: #A3D1C6;
}

/* Breadcrumb Styling */
.breadcrumb {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin-bottom: 1.5rem;
  font-size: 0.875rem;
  color: #6b7280;
}
.dark .breadcrumb {
  color: #A3D1C6;
}

.breadcrumb-separator {
  color: #6b7280;
}
.dark .breadcrumb-separator {
  color: #A3D1C6;
}

.breadcrumb-current {
  color: #1f2937;
  font-weight: 600;
}
.dark .breadcrumb-current {
  color: #A3D1C6;
}

/* Grade Filter */
.grade-filter-container {
  display: flex;
  gap: 0.5rem;
  margin-bottom: 1.5rem;
}

.grade-filter-btn.active {
  background: #2a6d5f;
}

/* Empty State */
.empty-state {
  text-align: center;
  padding: 3rem 2rem;
}

.empty-icon svg {
  color: #A3D1C6;
  margin-bottom: 1rem;
}

/* Modal Enhancements */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
}

.modal-content {
  max-width: 600px;
  width: 90%;
  max-height: 90vh;
  overflow-y: auto;
}

.modal-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 1.5rem;
}

.modal-header h2 {
  color: #1f2937;
  font-size: 1.25rem;
  font-weight: 600;
  margin: 0;
}
.dark .modal-header h2 {
  color: #A3D1C6;
}

/* Form Elements */
.form-group {
  margin-bottom: 1.5rem;
}

.form-group label {
  display: block;
  color: #1f2937;
  font-weight: 600;
  margin-bottom: 0.5rem;
}
.dark .form-group label {
  color: #A3D1C6;
}

.form-group input,
.form-group select,
.form-group textarea {
  width: 100%;
  background: white;
  border: 1px solid #d1d5db;
  border-radius: 8px;
  padding: 0.75rem;
  font-size: 0.875rem;
}
.dark .form-group input,
.dark .form-group select,
.dark .form-group textarea {
  background: #181c20;
  border: 1px solid #20c997;
  color: #A3D1C6;
}

.modal-actions {
  display: flex;
  justify-content: flex-end;
  gap: 1rem;
  margin-top: 2rem;
}
.breadcrumb-btn {
  font-weight: 600;
  display: flex;
  align-items: center;
  gap: 0.3rem;
  transition: background 0.2s, color 0.2s;
}
.breadcrumb-btn:hover {
  background: #20c997;
  color: #fff;
}
.breadcrumb-separator {
  color: #20c997;
  font-weight: 700;
}
.breadcrumb-current {
  color: #fff;
  font-weight: 700;
}
.grade-filter-container {
  display: flex;
  gap: 0.5rem;
  margin-bottom: 1.5rem;
}
.grade-filter-btn {
  background: #23272f;
  color: #20c997;
  border: 1.5px solid #20c997;
  border-radius: 8px;
  padding: 0.3rem 1rem;
  font-weight: 600;
  transition: background 0.2s, color 0.2s;
}
.grade-filter-btn.active, .grade-filter-btn:hover {
  background: #20c997;
  color: #fff;
}
.sections-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 1.5rem;
}
.section-card.simple {
  background: #23272f;
  border: 1.5px solid #20c997;
  border-radius: 16px;
  box-shadow: 0 2px 8px 0 #20c99722;
  padding: 1.5rem 1.2rem;
  display: flex;
  flex-direction: column;
  gap: 0.7rem;
  transition: box-shadow 0.2s, border 0.2s;
  cursor: pointer;
}
.section-card.simple:hover {
  box-shadow: 0 4px 16px 0 #20c99744;
  border-color: #18b087;
}
.section-simple-header {
  display: flex;
  align-items: flex-start;
  gap: 1rem;
}
.section-info h4 {
  color: #20c997;
  font-size: 1.1rem;
  font-weight: 700;
  margin-bottom: 0.3rem;
}
.section-code-inline {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  background: #181c1f;
  border-radius: 8px;
  padding: 0.3rem 0.8rem;
  font-size: 1rem;
  margin-bottom: 0.3rem;
}
.code-label {
  color: #20c997;
  font-weight: 600;
}
.section-code-text {
  color: #fff;
  font-weight: 600;
  letter-spacing: 1px;
  cursor: pointer;
}
.copy-code-mini {
  background: #20c997;
  color: #fff;
  border: none;
  border-radius: 6px;
  padding: 0.2rem 0.6rem;
  font-size: 0.95rem;
  font-weight: 600;
  transition: background 0.2s;
}
.copy-code-mini:hover {
  background: #18b087;
}
.section-stats-simple {
  color: #b5b5b5;
  font-size: 0.95rem;
  margin-top: 0.2rem;
}
.section-menu-container {
  position: relative;
}
.section-action-btn.menu {
  background: transparent;
  border: none;
  color: #20c997;
  font-size: 1.2rem;
  padding: 0.2rem;
  border-radius: 50%;
  transition: background 0.2s;
}
.section-action-btn.menu:hover {
  background: #23272f;
}
.section-dropdown-menu {
  position: absolute;
  top: 2rem;
  right: 0;
  background: #23272f;
  border: 1.5px solid #20c997;
  border-radius: 10px;
  box-shadow: 0 2px 8px 0 #20c99722;
  z-index: 10;
  min-width: 120px;
  display: flex;
  flex-direction: column;
}
.section-dropdown-menu .menu-item {
  background: none;
  border: none;
  color: #20c997;
  padding: 0.7rem 1rem;
  text-align: left;
  font-weight: 600;
  border-radius: 8px;
  transition: background 0.2s, color 0.2s;
}
.section-dropdown-menu .menu-item:hover {
  background: #20c997;
  color: #fff;
}
.section-dropdown-menu .menu-item.delete {
  color: #ff5c5c;
}
.section-dropdown-menu .menu-item.delete:hover {
  background: #ff5c5c;
  color: #fff;
}

/* Section Detail View Enhancements */
.section-detail-view {
  padding: 2rem;
  background: #181c1f;
  border-radius: 16px;
  border: 2px solid #20c997;
  box-shadow: 0 0 8px 0 #20c99733;
  color: #f1f1f1;
}
.section-detail-card {
  background: #23272f;
  border-radius: 16px;
  box-shadow: 0 2px 8px 0 #20c99722;
  border: 1.5px solid #20c997;
  padding: 2rem;
}
.section-info-container {
  background: #181c1f;
  border-radius: 12px;
  border: 1.5px solid #20c997;
  padding: 1.5rem 1rem;
  margin-bottom: 2rem;
}
.section-info-grid {
  display: flex;
  gap: 2rem;
  justify-content: center;
  margin-bottom: 1.5rem;
}
.section-info-item {
  text-align: center;
}
.section-actions-grid {
  display: flex;
  gap: 1rem;
  margin-top: 1.5rem;
  justify-content: center;
}
.section-action-btn {
  background: #23272f;
  color: #20c997;
  border: 1.5px solid #20c997;
  border-radius: 8px;
  padding: 0.6rem 1.2rem;
  font-weight: 600;
  transition: background 0.2s, color 0.2s;
  display: flex;
  align-items: center;
  gap: 0.4rem;
}
.section-action-btn:hover {
  background: #20c997;
  color: #fff;
}
.dark-mode .section-actions-grid {
  background: var(--bg-card);
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.10);
}

<template>
  <div class="subjects-page" :class="{ 'dark-mode': isDarkMode }">
    <!-- Simple Header Card -->
    <div class="section-header-card">
      <div class="section-header-content">
        <div class="section-header-left">
          <div class="section-header-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
              <path d="M12,3L1,9L12,15L21,10.09V17H23V9M5,13.18V17.18L12,21L19,17.18V13.18L12,17L5,13.18Z" />
            </svg>
          </div>
          <div class="header-text">
            <h1>My Subjects</h1>
            <p>Create and manage your class subjects with multiple sections</p>
          </div>
        </div>
        
        <div class="header-actions">
          <button @click="toggleDarkMode" class="dark-mode-toggle">
            <svg v-if="isDarkMode" width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M12,7A5,5 0 0,1 17,12A5,5 0 0,1 12,17A5,5 0 0,1 7,12A5,5 0 0,1 12,7M12,9A3,3 0 0,0 9,12A3,3 0 0,0 12,15A3,3 0 0,0 15,12A3,3 0 0,0 12,9M12,2L14.39,5.42C13.65,5.15 12.84,5 12,5C11.16,5 10.35,5.15 9.61,5.42L12,2M3.34,7L7.5,6.65C6.9,7.16 6.36,7.78 5.94,8.5C5.52,9.22 5.25,10 5.11,10.79L3.34,7M3.36,17L5.12,13.23C5.26,14 5.53,14.78 5.95,15.5C6.37,16.22 6.91,16.84 7.51,17.35L3.36,17M20.65,7L18.88,10.79C18.74,10 18.47,9.22 18.05,8.5C17.63,7.78 17.09,7.15 16.49,6.64L20.65,7M20.64,17L16.5,17.36C17.1,16.85 17.64,16.22 18.06,15.5" />
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
              <path d="M16,4C18.21,4 20,5.79 20,8C20,10.21 18.21,12 16,12C13.79,12 12,10.21 12,8C12,5.79 13.79,4 16,4M16,14C20.42,14 24,15.79 24,18V20H8V18C8,15.79 11.58,14 16,14C10.5 14 9.2 14.3 8.5 14.8V11.5Z" />
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
              <div v-for="(section, index) in formData.value.sections" :key="index" class="section-setup-item">
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

    <!-- Success Modal -->
    <div v-if="showSuccessModal" class="success-modal" @click.self="closeSuccessModal">
      <div class="success-modal-content">
        <div class="success-icon">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
            <path d="M9,20.42L2.79,14.21L5.62,11.38L9,14.77L18.88,4.88L21.71,7.71L9,20.42Z" />
          </svg>
        </div>
        <h3>Success!</h3>
        <p>{{ successMessage }}</p>
        <button @click="closeSuccessModal" class="success-close-btn">OK</button>
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

// Success modal state
const showSuccessModal = ref(false)
const successMessage = ref('')

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

// Navigation functions - FIXED
const navigateToSections = async (subject, section, event) => {
  if (event && (event.target.closest('button') || event.target.closest('.copy-code-btn'))) {
    return
  }
  
  try {
    await router.push({
      name: 'Sections',
      params: {
        subjectId: section.subject_id,  // ✅ Use real UUID from section
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
        subjectId: section.subject_id,  // ✅ FIXED: Use real UUID from section
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
        subjectId: section.subject_id,  // ✅ FIXED: Use real UUID from section
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
        subjectId: section.subject_id,  // ✅ FIXED: Use real UUID from section
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
        subjectId: sec.subject_id || subject.id,  // ✅ FIXED: Use real UUID from section
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
                subject_id: subject.id,  // ✅ Store the real UUID here
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
    
    // Show success modal instead of toast and alert
    successMessage.value = `Subject "${formData.value.name}" ${isEditing.value ? 'updated' : 'created'} successfully!\n\nSection Codes:\n${sectionCodesText}\n\nShare these codes with your students so they can join their respective sections.`
    showSuccessModal.value = true

    // Invalidate cache and refresh
    subjectsCache.value = null
    await fetchSubjects(true)

  } catch (error) {
    console.error('Error saving subject:', error)
    showToast('Error saving subject. Please try again.', 'error')
  }
}

const editSection = (section) => {
  console.log('Edit section:', section)
  // Implement edit section logic
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

// Success modal functions
const closeSuccessModal = () => {
  showSuccessModal.value = false
  successMessage.value = ''
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
/* Base Container */
.subjects-page {
  padding: 1.5rem;
  max-width: 1200px;
  margin: 0 auto;
  background: #f8fafc;
  min-height: 100vh;
}

/* Simple Header Card */
.section-header-card {
  background: white;
  border-radius: 16px;
  padding: 1.5rem;
  margin-bottom: 1.5rem;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
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
  width: 60px;
  height: 60px;
  background: #20c997;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-size: 1.5rem;
}

.header-text h1 {
  color: #333;
  font-size: 1.8rem;
  font-weight: 700;
  margin: 0;
}

.header-text p {
  color: #666;
  margin: 0.5rem 0 0 0;
}

.header-actions {
  display: flex;
  gap: 1rem;
}

.create-quiz-btn {
  background: #20c997;
  color: white;
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 8px;
  font-weight: 600;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  transition: all 0.3s ease;
}

.create-quiz-btn:hover {
  background: #1ba085;
  transform: translateY(-1px);
}

.dark-mode-toggle {
  background: white;
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 0.75rem;
  cursor: pointer;
  color: #666;
  transition: all 0.3s ease;
}

.dark-mode-toggle:hover {
  border-color: #20c997;
  color: #20c997;
}

/* Subject Grid */
.subjects-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1.5rem;
}

.subject-card {
  background: white;
  border-radius: 16px;
  padding: 1.5rem;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
  border: 1px solid #e5e7eb;
}

.subject-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  border-color: #20c997;
}

.subject-card.simple {
  background: #f9fafb;
  border: 1px solid #e0e0e0;
  border-radius: 12px;
  box-shadow: 0 1px 4px rgba(0,0,0,0.04);
  padding: 1rem 1.1rem;
  margin-bottom: 0.7rem;
  transition: box-shadow 0.18s, border 0.18s, background 0.18s;
}
.subject-card.simple:hover {
  background: #f6f8fa;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  border-color: var(--color-primary);
}
.dark .subject-card.simple, .dark .section-detail-card {
  background: #23272b;
  border: 1px solid #20c997;
  box-shadow: 0 2px 8px rgba(0,0,0,0.13);
}

/* Text Colors */
.section-info h4,
.section-detail-card h4,
.info-label,
.card-header h3 {
  color: #1f2937;
  font-weight: 600;
}
.dark .section-info h4,
.dark .section-detail-card h4,
.dark .info-label,
.dark .card-header h3 {
  color: #A3D1C6;
}

.info-value,
.section-stats-simple {
  color: #6b7280;
}
.dark .info-value,
.dark .section-stats-simple {
  color: #A3D1C6;
}

/* Simple, compact buttons */
.breadcrumb-btn, .grade-filter-btn, .section-action-btn {
  background: var(--color-primary);
  color: #fff;
  border: none;
  border-radius: 7px;
  padding: 0.45rem 1.1rem;
  font-size: 0.97rem;
  font-weight: 600;
  cursor: pointer;
  transition: background 0.18s, box-shadow 0.18s;
  display: flex;
  align-items: center;
  gap: 0.4rem;
  box-shadow: 0 1px 3px rgba(0,0,0,0.03);
}
.breadcrumb-btn:hover, .grade-filter-btn:hover, .section-action-btn:hover {
  background: var(--color-primary-dark);
  box-shadow: 0 2px 6px rgba(0,0,0,0.08);
}

/* Code Area Styling */
.section-code-area,
.section-code-inline {
  background: #f8f9fa;
  border-radius: 8px;
  padding: 1rem;
  margin: 1rem 0;
}
.dark .section-code-area,
.dark .section-code-inline {
  background: #181c20;
  border: 1px solid #20c997;
}
/* Grid Layouts */
.sections-grid {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

/* Section Card Content */
.section-simple-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.section-info {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.section-info h4 {
  color: #1f2937;
  font-size: 1.125rem;
  font-weight: 600;
  margin: 0;
}
.dark .section-info h4 {
  color: #A3D1C6;
}

/* Breadcrumb Styling */
.breadcrumb {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin-bottom: 1.5rem;
  font-size: 0.875rem;
  color: #6b7280;
}
.dark .breadcrumb {
  color: #A3D1C6;
}

.breadcrumb-separator {
  color: #6b7280;
}
.dark .breadcrumb-separator {
  color: #A3D1C6;
}

.breadcrumb-current {
  color: #1f2937;
  font-weight: 600;
}
.dark .breadcrumb-current {
  color: #A3D1C6;
}

/* Grade Filter */
.grade-filter-container {
  display: flex;
  gap: 0.5rem;
  margin-bottom: 1.5rem;
}

.grade-filter-btn.active {
  background: #2a6d5f;
}

/* Empty State */
.empty-state {
  text-align: center;
  padding: 3rem 2rem;
}

.empty-icon svg {
  color: #A3D1C6;
  margin-bottom: 1rem;
}

/* Modal Enhancements */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
}

.modal-content {
  max-width: 600px;
  width: 90%;
  max-height: 90vh;
  overflow-y: auto;
}

.modal-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 1.5rem;
}

.modal-header h2 {
  color: #1f2937;
  font-size: 1.25rem;
  font-weight: 600;
  margin: 0;
}
.dark .modal-header h2 {
  color: #A3D1C6;
}

/* Form Elements */
.form-group {
  margin-bottom: 1.5rem;
}

.form-group label {
  display: block;
  color: #1f2937;
  font-weight: 600;
  margin-bottom: 0.5rem;
}
.dark .form-group label {
  color: #A3D1C6;
}

.form-group input,
.form-group select,
.form-group textarea {
  width: 100%;
  background: white;
  border: 1px solid #d1d5db;
  border-radius: 8px;
  padding: 0.75rem;
  font-size: 0.875rem;
}
.dark .form-group input,
.dark .form-group select,
.dark .form-group textarea {
  background: #181c20;
  border: 1px solid #20c997;
  color: #A3D1C6;
}

.modal-actions {
  display: flex;
  justify-content: flex-end;
  gap: 1rem;
  margin-top: 2rem;
}
.breadcrumb-btn:hover {
  background: #20c997;
  color: #fff;
}
.breadcrumb-separator {
  color: #20c997;
  font-weight: 700;
}
.breadcrumb-current {
  color: #fff;
  font-weight: 700;
}
.grade-filter-container {
  display: flex;
  gap: 0.5rem;
  margin-bottom: 1.5rem;
}
.grade-filter-btn {
  background: #23272f;
  color: #20c997;
  border: 1.5px solid #20c997;
  border-radius: 8px;
  padding: 0.3rem 1rem;
  font-weight: 600;
  transition: background 0.2s, color 0.2s;
}
.grade-filter-btn.active, .grade-filter-btn:hover {
  background: #20c997;
  color: #fff;
}
.sections-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 1.5rem;
}
.section-card.simple {
  background: #23272f;
  border: 1.5px solid #20c997;
  border-radius: 16px;
  box-shadow: 0 2px 8px 0 #20c99722;
  padding: 1.5rem 1.2rem;
  display: flex;
  flex-direction: column;
  gap: 0.7rem;
  transition: box-shadow 0.2s, border 0.2s;
  cursor: pointer;
}
.section-card.simple:hover {
  box-shadow: 0 4px 16px 0 #20c99744;
  border-color: #18b087;
}
.section-simple-header {
  display: flex;
  align-items: flex-start;
  gap: 1rem;
}
.section-info h4 {
  color: #20c997;
  font-size: 1.1rem;
  font-weight: 700;
  margin-bottom: 0.3rem;
}
.section-code-inline {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  background: #181c1f;
  border-radius: 8px;
  padding: 0.3rem 0.8rem;
  font-size: 1rem;
  margin-bottom: 0.3rem;
}
.code-label {
  color: #20c997;
  font-weight: 600;
}
.section-code-text {
  color: #fff;
  font-weight: 600;
  letter-spacing: 1px;
  cursor: pointer;
}
.copy-code-mini {
  background: #20c997;
  color: #fff;
  border: none;
  border-radius: 6px;
  padding: 0.2rem 0.6rem;
  font-size: 0.95rem;
  font-weight: 600;
  transition: background 0.2s;
}
.copy-code-mini:hover {
  background: #18b087;
}
.section-stats-simple {
  color: #b5b5b5;
  font-size: 0.95rem;
  margin-top: 0.2rem;
}
.section-menu-container {
  position: relative;
}
.section-action-btn.menu {
  background: transparent;
  border: none;
  color: #20c997;
  font-size: 1.2rem;
  padding: 0.2rem;
  border-radius: 50%;
  transition: background 0.2s;
}
.section-action-btn.menu:hover {
  background: #23272f;
}
.section-dropdown-menu {
  position: absolute;
  top: 2rem;
  right: 0;
  background: #23272f;
  border: 1.5px solid #20c997;
  border-radius: 10px;
  box-shadow: 0 2px 8px 0 #20c99722;
  z-index: 10;
  min-width: 120px;
  display: flex;
  flex-direction: column;
}
.section-dropdown-menu .menu-item {
  background: none;
  border: none;
  color: #20c997;
  padding: 0.7rem 1rem;
  text-align: left;
  font-weight: 600;
  border-radius: 8px;
  transition: background 0.2s, color 0.2s;
}
.section-dropdown-menu .menu-item:hover {
  background: #20c997;
  color: #fff;
}
.section-dropdown-menu .menu-item.delete {
  color: #ff5c5c;
}
.section-dropdown-menu .menu-item.delete:hover {
  background: #ff5c5c;
  color: #fff;
}

/* Section Detail View Enhancements */
.section-detail-view {
  padding: 2rem;
  background: #181c1f;
  border-radius: 16px;
  border: 2px solid #20c997;
  box-shadow: 0 0 8px 0 #20c99733;
  color: #f1f1f1;
}
.section-detail-card {
  background: #23272f;
  border-radius: 16px;
  box-shadow: 0 2px 8px 0 #20c99722;
  border: 1.5px solid #20c997;
  padding: 2rem;
}
.section-info-container {
  background: #181c1f;
  border-radius: 12px;
  border: 1.5px solid #20c997;
  padding: 1.5rem 1rem;
  margin-bottom: 2rem;
}
.section-info-grid {
  display: flex;
  gap: 2rem;
  justify-content: center;
  margin-bottom: 1.5rem;
}
.section-info-item {
  text-align: center;
}
.section-actions-grid {
  display: flex;
  gap: 1rem;
  margin-top: 1.5rem;
  justify-content: center;
}
.section-action-btn {
  background: #23272f;
  color: #20c997;
  border: 1.5px solid #20c997;
  border-radius: 8px;
  padding: 0.6rem 1.2rem;
  font-weight: 600;
  transition: background 0.2s, color 0.2s;
  display: flex;
  align-items: center;
  gap: 0.4rem;
}
.section-action-btn:hover {
  background: #20c997;
  color: #fff;
}
.dark-mode .section-actions-grid {
  background: var(--bg-card);
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.10);
}

/* Responsive Design */
@media (max-width: 768px) {
  .subjects-page {
    padding: 1rem;
  }
  .section-header-content {
    flex-direction: column;
    gap: 1rem;
  }
  .header-actions {
    width: 100%;
    justify-content: space-between;
  }
  .subjects-grid,
  .sections-grid {
    grid-template-columns: 1fr;
  }
  .section-actions-grid {
    grid-template-columns: 1fr;
  }
  .section-info-grid {
    grid-template-columns: 1fr;
    gap: 1rem;
  }
  .grade-filter-container {
    overflow-x: auto;
    scrollbar-width: none;
  }
  .grade-filter-container::-webkit-scrollbar {
    display: none;
  }
  .modal-content {
    width: 95%;
    padding: 1.5rem;
  }
  .toast-notification {
    bottom: 1rem;
    right: 1rem;
    left: 1rem;
    min-width: auto;
  }
}

/* Delete Confirmation Modal */
.modal-card {
  background: white;
  color: #1f2937;
  border-radius: 20px;
  box-shadow: 
    0 20px 40px rgba(0, 0, 0, 0.15),
    0 10px 20px rgba(0, 0, 0, 0.1);
  padding: 2.5rem;
  min-width: 380px;
  max-width: 90vw;
  text-align: center;
  border: 1px solid #e5e7eb;
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
  color: #1f2937;
}
.item-details {
  margin-bottom: 1.5rem;
  padding: 1rem;
  background: #FBFFE4;
  border-radius: 12px;
  border: 1px solid #A3D1C6;
}
.item-name {
  margin: 0 0 0.5rem 0;
  font-size: 1.1rem;
  color: #1f2937;
  font-weight: 600;
}
.item-info {
  margin: 0;
  font-size: 0.9rem;
  color: #6b7280;
}
.warning-text {
  margin: 0 0 2rem 0;
  font-size: 0.9rem;
  color: #6b7280;
  font-style: italic;
}
.btn-cancel {
  background: #3D8D7A;
  color: white;
  border: none;
  border-radius: 12px;
  padding: 0.75rem 1.5rem;
  cursor: pointer;
  font-weight: 600;
  font-size: 0.9rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  transition: all 0.2s ease;
}
.btn-cancel:hover {
  background: #2d6d5f;
  box-shadow: 0 4px 12px rgba(61, 141, 122, 0.3);
}
.btn-delete {
  background: linear-gradient(135deg, #ff6b6b, #e74c3c);
  color: white;
  border: none;
  border-radius: 12px;
  padding: 0.75rem 1.5rem;
  cursor: pointer;
  font-weight: 600;
  font-size: 0.9rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  transition: all 0.2s ease;
}
.btn-delete:hover {
  background: linear-gradient(135deg, #e74c3c, #c0392b);
  box-shadow: 0 4px 12px rgba(231, 76, 60, 0.3);
}
.dark-mode .modal-card {
  background: #23272b;
  color: #A3D1C6;
  border-color: #3D8D7A;
}
.dark-mode .modal-card h3 {
  color: #A3D1C6;
}
.dark-mode .item-details {
  background: rgba(61, 141, 122, 0.1);
  border-color: #3D8D7A;
}
.dark-mode .item-name {
  color: #A3D1C6;
}
.dark-mode .item-info,
.dark-mode .warning-text {
  color: #9ca3af;
}

/* Section Menu */
.section-actions-row {
  display: flex;
  justify-content: flex-end;
  margin-bottom: 0.5rem;
}
.section-menu-container {
  position: relative;
}
.section-action-btn.menu {
  background: transparent;
  border: none;
  color: #3D8D7A;
  padding: 0.5rem;
  border-radius: 50%;
  cursor: pointer;
  transition: all 0.2s;
  width: 36px;
  height: 36px;
  display: flex;
  align-items: center;
  justify-content: center;
}
.section-action-btn.menu:hover {
  background: #FBFFE4;
}
.section-dropdown-menu {
  position: absolute;
  top: 40px;
  right: 0;
  background: white;
  border: 1px solid #A3D1C6;
  border-radius: 10px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  z-index: 10;
  min-width: 140px;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}
.section-dropdown-menu .menu-item {
  background: none;
  border: none;
  color: #1f2937;
  padding: 0.75rem 1rem;
  text-align: left;
  font-weight: 600;
  font-size: 0.875rem;
  border-radius: 0;
  transition: all 0.2s;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  cursor: pointer;
}
.section-dropdown-menu .menu-item:hover {
  background: #FBFFE4;
  color: #3D8D7A;
}
.section-dropdown-menu .menu-item.delete {
  color: #ef4444;
}
.section-dropdown-menu .menu-item.delete:hover {
  background: #fef2f2;
  color: #dc2626;
}
.dark-mode .section-action-btn.menu {
  color: #A3D1C6;
}
.dark-mode .section-action-btn.menu:hover {
  background: rgba(61, 141, 122, 0.1);
}
.dark-mode .section-dropdown-menu {
  background: #23272b;
  border-color: #3D8D7A;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
}
.dark-mode .section-dropdown-menu .menu-item {
  color: #A3D1C6;
}
.dark-mode .section-dropdown-menu .menu-item:hover {
  background: rgba(61, 141, 122, 0.1);
}
.dark-mode .section-dropdown-menu .menu-item.delete {
  color: #f87171;
}
.dark-mode .section-dropdown-menu .menu-item.delete:hover {
  background: rgba(239, 68, 68, 0.1);
  color: #fca5a5;
}
/* Student Roster Modal */
.student-roster-modal {
  max-width: 900px;
}
.roster-subtitle {
  color: #6b7280;
  font-size: 0.875rem;
  margin-top: 0.5rem;
}
.roster-content {
  max-height: 60vh;
  overflow-y: auto;
}
.sections-roster {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}
.section-roster {
  background: #FBFFE4;
  border: 1px solid #A3D1C6;
  border-radius: 12px;
  padding: 1.25rem;
}
.section-roster-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
  padding-bottom: 1rem;
  border-bottom: 1px solid #A3D1C6;
}
.section-roster-header h3 {
  color: #1f2937;
  font-size: 1rem;
  font-weight: 600;
  margin: 0;
}
.section-details {
  display: flex;
  gap: 1rem;
  align-items: center;
}
.section-details .section-code {
  background: white;
  padding: 0.375rem 0.75rem;
  font-size: 0.813rem;
}
.section-details .student-count {
  color: #6b7280;
  font-size: 0.875rem;
  font-weight: 600;
}
.students-table {
  background: white;
  border-radius: 8px;
  overflow: hidden;
}
.table-header {
  display: grid;
  grid-template-columns: 100px 1fr 1fr 80px 120px;
  gap: 1rem;
  padding: 0.75rem 1rem;
  background: #f3f4f6;
  font-weight: 600;
  font-size: 0.813rem;
  color: #6b7280;
  border-bottom: 1px solid #e5e7eb;
}
.table-body {
  display: flex;
  flex-direction: column;
}
.student-row {
  display: grid;
  grid-template-columns: 100px 1fr 1fr 80px 120px;
  gap: 1rem;
  padding: 1rem;
  border-bottom: 1px solid #f3f4f6;
  transition: all 0.2s;
  font-size: 0.875rem;
}
.student-row:hover {
  background: #f9fafb;
}
.student-row:last-child {
  border-bottom: none;
}
.col-id,
.col-name,
.col-email,
.col-grade,
.col-date {
  display: flex;
  align-items: center;
  color: #1f2937;
}
.col-id {
  font-family: 'Courier New', monospace;
  font-weight: 600;
}
.no-students {
  text-align: center;
  padding: 3rem 2rem;
}
.no-students .empty-icon {
  margin-bottom: 1rem;
}
.no-students h3 {
  color: #1f2937;
  font-size: 1.125rem;
  font-weight: 600;
  margin-bottom: 0.5rem;
}
.no-students p {
  color: #6b7280;
  font-size: 0.875rem;
}
.roster-actions {
  display: flex;
  justify-content: flex-end;
  gap: 0.75rem;
  margin-top: 1.5rem;
  padding-top: 1.5rem;
  border-top: 1px solid #e5e7eb;
}
.export-btn {
  background: #3D8D7A;
  color: white;
  border: none;
  padding: 0.75rem 1.25rem;
  border-radius: 8px;
  font-weight: 600;
  font-size: 0.875rem;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  transition: all 0.2s;
}
.export-btn:hover {
  background: #2d6d5f;
}
.close-roster-btn {
  background: white;
  color: #6b7280;
  border: 1px solid #d1d5db;
  padding: 0.75rem 1.25rem;
  border-radius: 8px;
  font-weight: 600;
  font-size: 0.875rem;
  cursor: pointer;
  transition: all 0.2s;
}
.close-roster-btn:hover {
  background: #f3f4f6;
  border-color: #9ca3af;
}
.dark-mode .roster-subtitle {
  color: #9ca3af;
}
.dark-mode .section-roster {
  background: rgba(61, 141, 122, 0.1);
  border-color: #3D8D7A;
}
.dark-mode .section-roster-header {
  border-bottom-color: #3D8D7A;
}
.dark-mode .section-roster-header h3,
.dark-mode .no-students h3 {
  color: #A3D1C6;
}
.dark-mode .section-details .student-count,
.dark-mode .no-students p {
  color: #9ca3af;
}
.dark-mode .students-table {
  background: #181c20;
}
.dark-mode .table-header {
  background: #2d3748;
  color: #9ca3af;
  border-bottom-color: #3D8D7A;
}
.dark-mode .student-row {
  border-bottom-color: #2d3748;
}
.dark-mode .student-row:hover {
  background: #23272b;
}
.dark-mode .col-id,
.dark-mode .col-name,
.dark-mode .col-email,
.dark-mode .col-grade,
.dark-mode .col-date {
  color: #A3D1C6;
}
.dark-mode .roster-actions {
  border-top-color: #2d3748;
}
.dark-mode .close-roster-btn {
  background: #181c20;
  color: #A3D1C6;
  border-color: #3D8D7A;
}
.dark-mode .close-roster-btn:hover {
  background: #2d3748;
}
@media (max-width: 768px) {
  .table-header,
  .student-row {
    grid-template-columns: 1fr;
    gap: 0.5rem;
  }
  .col-id,
  .col-name,
  .col-email,
  .col-grade,
  .col-date {
    padding: 0.25rem 0;
  }
  .student-roster-modal {
    max-width: 100%;
  }
}
</style>
