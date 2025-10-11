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
  gap: 0.75rem;
  margin-bottom: 1.5rem;
  padding: 0.75rem 1rem;
  background: #ffffff;
  border: 1px solid #e5e7eb;
  border-radius: 10px;
  box-shadow: 0 1px 3px rgba(0,0,0,0.05);
  font-size: 0.875rem;
  color: #6b7280;
}

.dark .breadcrumb {
  background: #1f2937;
  border: 1px solid #374151;
  box-shadow: 0 1px 3px rgba(0,0,0,0.2);
  color: #A3D1C6;
}

.breadcrumb-separator {
  color: #9ca3af;
  font-weight: 300;
  user-select: none;
}

.dark .breadcrumb-separator {
  color: #6b7280;
}

.breadcrumb-current {
  color: #1f2937;
  font-weight: 600;
  padding: 0.25rem 0.5rem;
  background: #f3f4f6;
  border-radius: 6px;
}

.dark .breadcrumb-current {
  color: #ffffff;
  background: #374151;
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
  background: none;
  border: none;
  color: #17815c;
  font-weight: 700;
  text-decoration: underline;
  display: flex;
  align-items: center;
  gap: 0.4rem;
  padding: 0.25rem 0.5rem;
  border-radius: 6px;
  transition: all 0.2s ease;
  cursor: pointer;
  font-size: 0.875rem;
}

.dark .breadcrumb-btn {
  color: #A3D1C6;
}

.breadcrumb-btn:hover {
  background: #A3D1C6;
  color: #ffffff;
  transform: translateX(-1px);
}

.dark .breadcrumb-btn:hover {
  background: #20c997;
  color: #ffffff;
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
  gap: 0.75rem;
  margin-bottom: 1.5rem;
  flex-wrap: wrap;
}

.grade-filter-btn {
  background: #ffffff;
  color: #3D8D7A;
  border: 1.5px solid #A3D1C6;
  border-radius: 8px;
  padding: 0.5rem 1rem;
  font-weight: 500;
  transition: all 0.2s ease;
  cursor: pointer;
  font-size: 0.875rem;
}

.dark .grade-filter-btn {
  background: #23272f;
  color: #20c997;
  border: 1.5px solid #20c997;
  font-weight: 600;
}

.grade-filter-btn.active, .grade-filter-btn:hover {
  background: #A3D1C6;
  color: #ffffff;
  transform: translateY(-1px);
  box-shadow: 0 2px 6px rgba(163, 209, 198, 0.3);
}

.dark .grade-filter-btn.active, .dark .grade-filter-btn:hover {
  background: #20c997;
  color: #ffffff;
  box-shadow: 0 2px 6px rgba(32, 201, 151, 0.3);
}
.sections-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.25rem;
  max-width: 100%;
}

.section-card.simple {
  background: #ffffff;
  border: 1.5px solid #A3D1C6;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  padding: 1.25rem 1rem;
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
  transition: all 0.2s ease;
  cursor: pointer;
  position: relative;
  max-width: 350px;
  min-height: 120px;
}

.dark .section-card.simple {
  background: #23272f;
  border: 1.5px solid #20c997;
  box-shadow: 0 2px 8px rgba(32, 201, 151, 0.15);
}

.section-card.simple:hover {
  box-shadow: 0 4px 16px rgba(163, 209, 198, 0.25);
  border-color: #3D8D7A;
  transform: translateY(-2px);
}

.dark .section-card.simple:hover {
  box-shadow: 0 4px 16px rgba(32, 201, 151, 0.3);
  border-color: #18b087;
}
.section-simple-header {
  display: flex;
  align-items: flex-start;
  gap: 1rem;
}

.section-info h4 {
  color: #3D8D7A;
  font-size: 1rem;
  font-weight: 600;
  margin-bottom: 0.25rem;
  line-height: 1.3;
}

.dark .section-info h4 {
  color: #20c997;
  font-weight: 700;
}

.section-code-inline {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  background: #F8F9FA;
  border: 1px solid #A3D1C6;
  border-radius: 6px;
  padding: 0.25rem 0.6rem;
  font-size: 0.875rem;
  margin-bottom: 0.25rem;
}

.dark .section-code-inline {
  background: #181c1f;
  border: 1px solid #20c997;
}

.code-label {
  color: #3D8D7A;
  font-weight: 600;
  font-size: 0.75rem;
}

.dark .code-label {
  color: #20c997;
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
  color: #3D8D7A;
  font-size: 1.1rem;
  padding: 0.3rem;
  border-radius: 50%;
  transition: all 0.2s ease;
  width: 32px;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.dark .section-action-btn.menu {
  color: #20c997;
}

.section-action-btn.menu:hover {
  background: #A3D1C6;
  color: #ffffff;
  transform: scale(1.1);
}

.dark .section-action-btn.menu:hover {
  background: #20c997;
  color: #ffffff;
}
.section-dropdown-menu {
  position: absolute;
  top: 2rem;
  right: 0;
  background: #ffffff;
  border: 1.5px solid #A3D1C6;
  border-radius: 10px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.15);
  z-index: 10;
  min-width: 140px;
  display: flex;
  flex-direction: column;
  font-size: 0.875rem;
}

.dark .section-dropdown-menu {
  background: #23272f;
  border: 1.5px solid #20c997;
  box-shadow: 0 4px 12px rgba(32, 201, 151, 0.2);
}

.section-dropdown-menu .menu-item {
  background: none;
  border: none;
  color: #3D8D7A;
  padding: 0.75rem 1rem;
  text-align: left;
  font-weight: 500;
  border-radius: 6px;
  transition: all 0.2s ease;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  cursor: pointer;
}

.dark .section-dropdown-menu .menu-item {
  color: #20c997;
  font-weight: 600;
}

.section-dropdown-menu .menu-item:hover {
  background: #A3D1C6;
  color: #ffffff;
  transform: translateX(2px);
}

.dark .section-dropdown-menu .menu-item:hover {
  background: #20c997;
  color: #ffffff;
}

.section-dropdown-menu .menu-item.delete {
  color: #dc3545;
}

.dark .section-dropdown-menu .menu-item.delete {
  color: #ff5c5c;
}

.section-dropdown-menu .menu-item.delete:hover {
  background: #dc3545;
  color: #ffffff;
}

.dark .section-dropdown-menu .menu-item.delete:hover {
  background: #ff5c5c;
  color: #ffffff;
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
  background: #ffffff;
  color: #3D8D7A;
  border: 1.5px solid #A3D1C6;
  border-radius: 8px;
  padding: 0.6rem 1.2rem;
  font-weight: 500;
  transition: all 0.2s ease;
  display: flex;
  align-items: center;
  gap: 0.4rem;
  cursor: pointer;
  font-size: 0.875rem;
}

.dark .section-action-btn {
  background: #23272f;
  color: #20c997;
  border: 1.5px solid #20c997;
  font-weight: 600;
}

.section-action-btn:hover {
  background: #A3D1C6;
  color: #ffffff;
  transform: translateY(-1px);
  box-shadow: 0 2px 8px rgba(163, 209, 198, 0.3);
}

.dark .section-action-btn:hover {
  background: #20c997;
  color: #ffffff;
  box-shadow: 0 2px 8px rgba(32, 201, 151, 0.3);
}
.dark-mode .section-actions-grid {
  background: var(--bg-card);
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.10);
}

<template>
  <div :class="['subjects-page', isDarkMode ? 'dark' : '']">
    <!-- Header Card -->
    <div class="header-card">
      <div class="header-content">
        <div class="header-left">
          <div class="user-icon">
            <svg width="40" height="40" fill="none" viewBox="0 0 24 24">
              <path fill="currentColor" d="M12 2a2 2 0 0 1 2 2v1h4a2 2 0 0 1 2 2v1H4V7a2 2 0 0 1 2-2h4V4a2 2 0 0 1 2-2Zm8 7v9a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V9h16Zm-2 2H6v7h12v-7Z"/>
            </svg>
          </div>
          <div>
            <h1 class="header-title">My Subjects</h1>
            <p class="header-subtitle">Manage your classes and student sections</p>
          </div>
        </div>
        
        <div class="header-actions">
          <button class="dark-mode-toggle" @click="toggleDarkMode">
            <svg v-if="!isDarkMode" width="24" height="24" fill="none" viewBox="0 0 24 24">
              <path fill="currentColor" d="M12 2a1 1 0 0 1 1 1v2a1 1 0 1 1-2 0V3a1 1 0 0 1 1-1Zm6.364 3.636a1 1 0 0 1 1.414 1.414l-1.414 1.414a1 1 0 1 1-1.414-1.414l1.414-1.414ZM21 11a1 1 0 1 1 0 2h-2a1 1 0 1 1 0-2h2Zm-2.222 7.364a1 1 0 0 1-1.415 1.415l-1.414-1.415a1 1 0 1 1 1.415-1.414l1.414 1.414ZM13 21a1 1 0 1 1-2 0v-2a1 1 0 1 1 2 0v2Zm-7.364-2.222a1 1 0 0 1-1.414-1.415l1.414-1.414a1 1 0 1 1 1.414 1.415l-1.414 1.414ZM3 13a1 1 0 1 1 0-2h2a1 1 0 1 1 0 2H3Zm2.222-7.364a1 1 0 0 1 1.415-1.414l1.414 1.414A1 1 0 1 1 6.05 6.05L4.636 4.636Z"/>
            </svg>
            <svg v-else width="24" height="24" fill="none" viewBox="0 0 24 24">
              <path fill="currentColor" d="M21 12.79A9 9 0 0 1 11.21 3a1 1 0 0 0-1.21 1v.09A9 9 0 1 0 20.91 13a1 1 0 0 0 1-1.21ZM12 21a7 7 0 0 1 0-14V5a7 7 0 0 1 0 14Z"/>
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

    <!-- Empty State -->
    <div v-if="viewMode === 'subjects' && subjects.length === 0" class="empty-state">
      <div class="empty-icon">
        <svg width="48" height="48" fill="none" viewBox="0 0 24 24">
          <path fill="currentColor" d="M12 2a2 2 0 0 1 2 2v1h4a2 2 0 0 1 2 2v1H4V7a2 2 0 0 1 2-2h4V4a2 2 0 0 1 2-2Zm8 7v9a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V9h16Zm-2 2H6v7h12v-7Z"/>
        </svg>
      </div>
      <div class="empty-title">No Subjects Created Yet</div>
      <div class="empty-desc">Create your first subject to start managing your classes and student sections</div>
      <button class="create-quiz-btn" @click="showCreateModal = true">Create Your First Subject</button>
    </div>

    <!-- Subjects Grid -->
    <div v-if="viewMode === 'subjects' && subjects.length > 0" class="subjects-grid enhanced">
      <div v-for="subject in subjects" :key="subject.id" class="subject-card enhanced" @click="selectSubject(subject)">
        <div class="subject-card-header">
          <div class="subject-title-area">
            <div class="subject-icon" :title="subject.subject_name">
              <span class="subject-initial">{{ subject.subject_name.charAt(0) }}</span>
            </div>
            <div class="subject-info">
              <h3 class="subject-title">{{ subject.subject_name }}</h3>
              <p class="grade-level">{{ subject.grade_level_display }}</p>
            </div>
          </div>
          <div class="arrow-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
              <path d="M8.59,16.58L13.17,12L8.59,7.41L10,6L16,12L10,18L8.59,16.58Z" />
            </svg>
          </div>
        </div>
        <div class="subject-divider"></div>
        <div class="subject-stats-container">
          <p class="subject-stats-simple">{{ subject.section_count }} sections • {{ subject.total_students }} students</p>
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
        <div v-for="section in filteredSections" :key="section.id" class="section-card enhanced" @click="selectSection(section)">
          <div class="section-card-header">
            <!-- Section icon and title -->
            <div class="section-title-area">
              <div class="section-icon">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-5 14H7v-2h7v2zm3-4H7v-2h10v2zm0-4H7V7h10v2z"/>
                </svg>
              </div>
              <h4 class="section-title">{{ section.section_name }} (Grade {{ section.grade_level }})</h4>
            </div>
            
            <!-- Always visible 3-dots menu -->
            <div class="section-menu-container">
              <button class="section-menu-btn" @click.stop="toggleSectionMenu(section.id)" title="More Options">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                  <circle cx="5" cy="12" r="2" />
                  <circle cx="12" cy="12" r="2" />
                  <circle cx="19" cy="12" r="2" />
                </svg>
              </button>
              <transition name="dropdown">
                <div v-if="openMenuId === section.id" class="section-dropdown-menu">
                  <button @click.stop="editSection(section)" class="menu-item">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                      <path d="M20.71,7.04C21.1,6.65 21.1,6 20.71,5.63L18.37,3.29C18,2.9 17.35,2.9 16.96,3.29L15.12,5.12L18.87,8.87M3,17.25V21H6.75L17.81,9.93L14.06,6.18L3,17.25Z" />
                    </svg>
                    Edit Section
                  </button>
                  <button @click.stop="openDeleteModal('section', section)" class="menu-item delete">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                      <path d="M19,4H15.5L14.5,3H9.5L8.5,4H5V6H19M6,19A2,2 0 0,0 8,21H16A2,2 0 0,0 18,19V7H6V19Z" />
                    </svg>
                    Delete Section
                  </button>
                  <button @click.stop="toggleArchiveSection(section)" class="menu-item">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                      <path d="M3,3H21V7H3V3M4,8H20V21H4V8M9.5,11A0.5,0.5 0 0,0 9,11.5V13H15V11.5A0.5,0.5 0 0,0 14.5,11H9.5Z" />
                    </svg>
                    {{ (section.status === 'archived') ? 'Unarchive' : 'Archive' }}
                  </button>
                </div>
              </transition>
            </div>
          </div>
          
          <div class="section-card-body">
            <!-- Section Code in distinct box -->
            <div class="section-code-box">
              <div class="code-box-header">
                <span class="code-label">Section Code</span>
              </div>
              <div class="code-box-content">
                <span class="section-code-text">{{ section.section_code }}</span>
                <button @click.stop="copyCode(section.section_code, section.id)" 
                        class="copy-code-btn" 
                        :class="{ 'copied': copiedCodeId === section.id }"
                        :title="copiedCodeId === section.id ? 'Copied!' : 'Copy Code'">
                  <svg v-if="copiedCodeId !== section.id" width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M19,21H8V7H19M19,5H8A2,2 0 0,0 6,7V21A2,2 0 0,0 8,23H19A2,2 0 0,0 21,21V7A2,2 0 0,0 19,5M16,1H4A2,2 0 0,0 2,3V17H4V3H16V1Z" />
                  </svg>
                  <svg v-else width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M21,7L9,19L3.5,13.5L4.91,12.09L9,16.17L19.59,5.59L21,7Z" />
                  </svg>
                  {{ copiedCodeId === section.id ? 'Copied!' : 'Copy' }}
                </button>
              </div>
            </div>
            
            <!-- Student count -->
            <div class="section-stats">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                <path d="M16,4C18.21,4 20,5.79 20,8C20,10.21 18.21,12 16,12C13.79,12 12,10.21 12,8C12,5.79 13.79,4 16,4M16,14C20.42,14 24,15.79 24,18V20H8V18C8,15.79 11.58,14 16,14M6,6H4V4H2V6H0V8H2V10H4V8H6V6Z" />
              </svg>
              <span>{{ section.student_count || 0 }} students</span>
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

      <div class="section-detail-enhanced">
        <!-- Left Section: Section Info -->
        <div class="section-info-card">
          <div class="section-header">
            <div class="section-icon">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                <path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-5 14H7v-2h7v2zm3-4H7v-2h10v2zm0-4H7V7h10v2z"/>
              </svg>
            </div>
            <div class="section-title-info">
              <h3 class="section-title">{{ selectedSection.section_name }} (Grade {{ selectedSection.grade_level }})</h3>
              <p class="section-subtitle">{{ selectedSection.subject_name }}</p>
            </div>
          </div>

          <!-- Section Details -->
          <div class="section-details">
            <div class="detail-item">
              <span class="detail-label">Subject:</span>
              <span class="detail-value">{{ selectedSection.subject_name }}</span>
            </div>
            <div class="detail-item">
              <span class="detail-label">Section:</span>
              <span class="detail-value">{{ selectedSection.section_name }}</span>
            </div>
            <div class="detail-item">
              <span class="detail-label">Grade:</span>
              <span class="detail-value">{{ selectedSection.grade_level }}</span>
            </div>
          </div>
          
          <!-- Section Code -->
          <div class="section-code-container">
            <div class="code-label">Section Code:</div>
            <div class="code-value">{{ selectedSection.section_code }}</div>
            <button @click.stop="copyCode(selectedSection.section_code, selectedSection.section_id)" class="copy-btn">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                <path d="M19,21H8V7H19M19,5H8A2,2 0 0,0 6,7V21A2,2 0 0,0 8,23H19A2,2 0 0,0 21,21V7A2,2 0 0,0 19,5M16,1H4A2,2 0 0,0 2,3V17H4V3H16V1Z" />
              </svg>
              {{ copiedCodeId === selectedSection.section_id ? 'Copied!' : 'Copy' }}
            </button>
          </div>
        </div>

        <!-- Right Section: Quick Actions -->
        <div class="quick-actions-card">
          <h4 class="actions-title">Quick Actions</h4>
          <div class="actions-grid">
            <button 
              @click.stop="viewSectionStudents(selectedSubject, selectedSection)"
              class="action-button primary"
              title="View Students in Section"
            >
              <div class="btn-icon">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M16,4C18.21,4 20,5.79 20,8C20,10.21 18.21,12 16,12C13.79,12 12,10.21 12,8C12,5.79 13.79,4 16,4M16,14C20.42,14 24,15.79 24,18V20H8V18C8,15.79 11.58,14 16,14" />
                </svg>
              </div>
              <span class="btn-text">View Students</span>
            </button>

            <button 
              @click.stop="navigateToCreateQuiz(selectedSubject, selectedSection)"
              class="action-button secondary"
              title="Create Quiz/Assessment"
            >
              <div class="btn-icon">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M14,2H6A2,2 0 0,0 4,4V20A2,2 0 0,0 6,22H18A2,2 0 0,0 20,20V8L14,2M18,20H6V4H13V9H18V20Z" />
                </svg>
              </div>
              <span class="btn-text">Create Quiz</span>
            </button>
            
            <button 
              @click.stop="viewQuizzes(selectedSubject, selectedSection)"
              class="action-button secondary"
              title="View Past Quizzes"
            >
              <div class="btn-icon">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M13,9V3.5L18.5,9M6,2C4.89,2 4,2.89 4,4V20A2,2 0 0,0 6,22H18A2,2 0 0,0 20,20V8L14,2H6Z" />
                </svg>
              </div>
              <span class="btn-text">View Quizzes</span>
            </button>
            
            <button 
              @click.stop="manageGrades(selectedSubject, selectedSection)"
              class="action-button tertiary"
              title="Grade Management"
            >
              <div class="btn-icon">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M16,18H18V16H16M16,14H18V12H16M14,18H16V16H14M12,18H14V16H12M12,14H14V12H12M10,18H12V16H10M8,18H10V16H8M8,14H10V12H8M6,18H8V16H6M14,10H16V8H14M12,10H14V8H12M10,10H12V8H10M8,10H10V8H8M6,10H8V8H6M6,14H8V12H6" />
                </svg>
              </div>
              <span class="btn-text">Grades</span>
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Empty State - only show when in subjects view and no subjects exist -->
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
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.subjects-page {
  min-height: 100vh;
  background: #FBFFE4;
  padding: 1.5rem;
  font-family: 'Inter', sans-serif;
}
.dark .subjects-page {
  background: #181c20;
}

/* Header */
.header-card {
  background: white;
  border-radius: 16px;
  padding: 1.5rem;
  margin-bottom: 1.5rem;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
}
.dark .header-card {
  background: #23272b;
  border: 1px solid #20c997;
  box-shadow: 0 2px 8px rgba(0,0,0,0.25);
}

.header-content {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.header-left {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.user-icon {
  width: 56px;
  height: 56px;
  background: #3D8D7A;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
}

.header-title {
  font-size: 1.5rem;
  font-weight: 700;
  color: #1f2937;
  margin-bottom: 0.25rem;
}
.dark .header-title {
  color: #A3D1C6;
}

.header-subtitle {
  font-size: 0.875rem;
  color: #6b7280;
}
.dark .header-subtitle {
  color: #A3D1C6;
}

.header-actions {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.dark-mode-toggle {
  width: 48px;
  height: 48px;
  background: #FBFFE4;
  border: 2px solid #A3D1C6;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.2s;
  color: #3D8D7A;
}
.dark .dark-mode-toggle {
  background: #23272b;
  border-color: #3D8D7A;
  color: #A3D1C6;
}

.dark-mode-toggle:hover {
  background: #A3D1C6;
  transform: scale(1.05);
}

/* Empty State */
.empty-state {
  background: white;
  border-radius: 16px;
  padding: 2.5rem 1.5rem;
  margin: 2rem auto;
  max-width: 480px;
  box-shadow: 0 1px 3px rgba(0,0,0,0.07);
  text-align: center;
  color: #1f2937;
}
.dark .empty-state {
  background: #23272b;
  color: #A3D1C6;
  border: 1px solid #20c997;
}

.empty-icon {
  margin-bottom: 1rem;
  color: #3D8D7A;
}
.dark .empty-icon {
  color: #A3D1C6;
}

.empty-title {
  font-size: 1.25rem;
  font-weight: 700;
  margin-bottom: 0.5rem;
}

.empty-desc {
  font-size: 0.95rem;
  color: #6b7280;
  margin-bottom: 1.5rem;
}

.dark .empty-desc {
  color: #9ca3af;
}

/* Center button in empty state */
.empty-state .create-quiz-btn {
  margin: 0 auto;
  display: inline-block;
}

/* Enhanced Subjects Grid */
.subjects-grid.enhanced {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 2rem 1.5rem;
  margin-bottom: 2rem;
  padding: 0.5rem;
}

/* Enhanced Subject Card */
.subject-card.enhanced {
  background: #fff;
  border: 1.5px solid #e5e7eb;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.04);
  padding: 0;
  margin-bottom: 1rem;
  transition: all 0.18s ease;
  overflow: hidden;
  cursor: pointer;
  max-width: 380px;
  min-height: 140px;
}

.dark .subject-card.enhanced {
  background: #23272b;
  border: 1.5px solid #374151;
  box-shadow: 0 2px 8px rgba(32, 201, 151, 0.13);
}

.subject-card.enhanced:hover {
  box-shadow: 0 8px 24px rgba(16, 185, 129, 0.12);
  border-color: #10b981;
  background: #f8fdfa;
  transform: translateY(-2px);
}

.dark .subject-card.enhanced:hover {
  border-color: #20c997;
  box-shadow: 0 8px 24px rgba(16, 185, 129, 0.18);
  background: #23272b;
}

/* Subject Card Header */
.subject-card-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1.2rem 1.2rem 0.8rem 1.2rem;
}

.subject-title-area {
  display: flex;
  align-items: center;
  gap: 1rem;
  flex: 1;
}

.subject-icon {
  width: 48px;
  height: 48px;
  background: linear-gradient(135deg, #10b981, #059669);
  border-radius: 14px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  flex-shrink: 0;
  box-shadow: 0 2px 6px rgba(16, 185, 129, 0.3);
}

.subject-initial {
  font-size: 1.2rem;
  font-weight: 700;
  text-transform: uppercase;
}

.subject-info {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}

.subject-title {
  font-size: 1.25rem;
  font-weight: 700;
  color: #1f2937;
  margin: 0;
  line-height: 1.3;
  letter-spacing: -0.01em;
}

.dark .subject-title {
  color: #f9fafb;
}

.grade-level {
  font-size: 0.95rem;
  color: #10b981;
  font-weight: 600;
  margin: 0;
}

.dark .grade-level {
  color: #34d399;
}

/* Arrow Icon */
.arrow-icon {
  color: #9ca3af;
  transition: all 0.18s ease;
  display: flex;
  align-items: center;
  opacity: 0.7;
}

.dark .arrow-icon {
  color: #6b7280;
}

.subject-card.enhanced:hover .arrow-icon {
  color: #10b981;
  transform: translateX(4px);
  opacity: 1;
}

.dark .subject-card.enhanced:hover .arrow-icon {
  color: #34d399;
}

/* Subject Divider */
.subject-divider {
  border-bottom: 1px solid #f3f4f6;
  margin: 0 1.2rem;
}

.dark .subject-divider {
  border-bottom-color: #374151;
}

/* Subject Stats Container */
.subject-stats-container {
  padding: 1rem 1.2rem 1.2rem 1.2rem;
}

.subject-stats-simple {
  color: #6b7280;
  font-size: 0.9rem;
  margin: 0;
  font-weight: 500;
  letter-spacing: 0.01em;
}

.dark .subject-stats-simple {
  color: #9ca3af;
}

/* Buttons */
/* Uniform button style for main actions (matches Analytics.vue and DashboardHome.vue) */
.create-quiz-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  background: #B3D8A8;
  color: #181c20;
  border: 1px solid #A3D1C6;
  padding: 0.5rem 1.25rem;
  border-radius: 8px;
  font-size: 0.875rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s;
  box-shadow: none;
}
.dark .create-quiz-btn {
  background: #B3D8A8;
  color: #181c20;
  border: 1px solid #A3D1C6;
}
.create-quiz-btn:hover {
  background: #A3D1C6;
  color: #23272b;
  border-color: #20c997;
  transform: translateY(-1px);
}
.dark .create-quiz-btn:hover {
  background: #A3D1C6;
  color: #23272b;
  border-color: #20c997;
}

/* Breadcrumb Styling */
.breadcrumb {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin-bottom: 1.5rem;
  font-size: 0.875rem;
}
.dark .breadcrumb {
  color: #A3D1C6;
}

.breadcrumb-btn {
  background: transparent;
  border: none;
  color: #20c997;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 0.25rem;
  font-size: 0.875rem;
  text-decoration: underline;
}
.dark .breadcrumb-btn {
  color: #A3D1C6;
}

.breadcrumb-btn:hover {
  color: #3D8D7A;
}

.breadcrumb-separator {
  color: #6b7280;
}
.dark .breadcrumb-separator {
  color: #A3D1C6;
}

.breadcrumb-current {
  color: #1f2937;
  font-weight: 500;
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

.grade-filter-btn {
  background: white;
  border: 1px solid #A3D1C6;
  color: #3D8D7A;
  padding: 0.5rem 1rem;
  border-radius: 8px;
  font-size: 0.875rem;
  cursor: pointer;
  transition: all 0.2s;
}
.dark .grade-filter-btn {
  background: #23272b;
  border-color: #20c997;
  color: #A3D1C6;
}

.grade-filter-btn.active,
.grade-filter-btn:hover {
  background: #20c997;
  color: #181c20;
}

/* Sections Grid - Enhanced Design */
.sections-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.5rem;
  margin-bottom: 2rem;
  padding: 1rem;
  width: 100%;
  box-sizing: border-box;
}

.section-card {
  background: white;
  border-radius: 12px;
  padding: 1.25rem;
  box-shadow: 0 1px 3px rgba(0,0,0,0.05);
  border: 1px solid #A3D1C6;
  transition: all 0.2s;
  cursor: pointer;
}
.dark .section-card {
  background: #23272b;
  border-color: #20c997;
}

.section-card:hover {
  transform: translateY(-2px);
}

/* Enhanced Responsive Design */
@media (max-width: 1400px) {
  .sections-grid {
    gap: 1.25rem;
    padding: 0.75rem;
  }
}

@media (max-width: 1200px) {
  .sections-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 1rem;
    padding: 0.5rem;
  }
}

@media (max-width: 1024px) {
  .subjects-grid {
    grid-template-columns: 1fr;
  }
  .sections-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 1rem;
    padding: 0.5rem;
  }
}

@media (max-width: 768px) {
  .sections-grid {
    grid-template-columns: 1fr;
    gap: 1rem;
    padding: 0.25rem;
  }
  .section-card.enhanced {
    min-height: 160px;
  }
}

/* Enhanced Section Card Styles - Complete Redesign */
.section-card.enhanced {
  background: #fff;
  border: 2px solid #e5e7eb;
  border-radius: 16px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.08);
  padding: 0;
  margin-bottom: 0;
  transition: all 0.3s ease;
  overflow: hidden;
  cursor: pointer;
  width: 100%;
  min-height: 180px;
  position: relative;
}

.section-card.enhanced:hover {
  box-shadow: 0 12px 32px rgba(16, 185, 129, 0.15);
  border-color: #10b981;
  transform: translateY(-4px);
}

.dark .section-card.enhanced {
  background: #181c20;
  border: 1.5px solid #26322c;
  box-shadow: none;
}

.dark .section-card.enhanced:hover {
  border-color: #A3D1C6;
  box-shadow: none;
}

.section-card-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1.5rem 1.5rem 1rem 1.5rem;
  background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
  border-bottom: 1px solid #e2e8f0;
}

.dark .section-card-header {
  background: #23272b;
  border-bottom: 1px solid #26322c;
}

.section-title-area {
  display: flex;
  align-items: center;
  gap: 1rem;
  flex: 1;
}

.section-icon {
  width: 48px;
  height: 48px;
  background: linear-gradient(135deg, #3D8D7A, #B3D8A8);
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  box-shadow: 0 4px 12px rgba(61, 141, 122, 0.3);
  transition: all 0.3s ease;
  flex-shrink: 0;
}

.section-title {
  font-size: 1.25rem;
  font-weight: 700;
  color: #1f2937;
  margin: 0;
  line-height: 1.3;
}

.dark .section-title {
  color: #A3D1C6;
}

.section-menu-container {
  position: relative;
}

.section-menu-btn {
  width: 40px;
  height: 40px;
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.2s ease;
  color: #6b7280;
}

.section-menu-btn:hover {
  background: #10b981;
  border-color: #10b981;
  color: white;
  transform: scale(1.05);
}

.dark .section-menu-btn {
  background: #374151;
  border-color: #4b5563;
  color: #9ca3af;
}

.dark .section-menu-btn:hover {
  background: #10b981;
  border-color: #10b981;
  color: white;
}

.section-dropdown-menu {
  position: absolute;
  top: 100%;
  right: 0;
  background: white;
  border: 1px solid #e5e7eb;
  border-radius: 12px;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.15);
  z-index: 50;
  min-width: 180px;
  overflow: hidden;
  margin-top: 0.5rem;
}

.dark .section-dropdown-menu {
  background: #1f2937;
  border-color: #374151;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.5);
}

.menu-item {
  width: 100%;
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.875rem 1rem;
  background: none;
  border: none;
  text-align: left;
  font-size: 0.875rem;
  font-weight: 500;
  color: #374151;
  cursor: pointer;
  transition: all 0.15s ease;
}

.menu-item:hover {
  background: #f3f4f6;
  color: #10b981;
}

.menu-item.delete {
  color: #ef4444;
}

.menu-item.delete:hover {
  background: #fef2f2;
  color: #dc2626;
}

.dark .menu-item {
  color: #d1d5db;
}

.dark .menu-item:hover {
  background: #374151;
  color: #10b981;
}

.dark .menu-item.delete {
  color: #f87171;
}

.dark .menu-item.delete:hover {
  background: #451a1a;
  color: #ef4444;
}

.section-card-body {
  padding: 1.5rem;
  background: #fff;
}

.dark .section-card-body {
  background: #23272b;
}

.section-code-box {
  background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
  border: 2px solid #e2e8f0;
  border-radius: 12px;
  overflow: hidden;
  margin-bottom: 1rem;
  transition: all 0.3s ease;
}

.section-code-box:hover {
  border-color: #10b981;
  box-shadow: 0 4px 12px rgba(16, 185, 129, 0.1);
}

.dark .section-code-box {
  background: #181c20 !important;
  border: 1.5px solid #374151 !important;
  box-shadow: none !important;
}

.dark .section-code-box:hover {
  border-color: #20c997;
  background: #181c20 !important;
}

.code-box-header {
  background: linear-gradient(135deg, #e2e8f0 0%, #cbd5e1 100%);
  padding: 0.75rem 1rem;
  border-bottom: 1px solid #d1d5db;
}

.dark .code-box-header {
  background: #181c20 !important;
  border-bottom-color: #374151;
  color: #A3D1C6;
}

.code-label {
  font-size: 0.75rem;
  font-weight: 600;
  color: #7ca3c7;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.dark .code-label {
  color: #A3D1C6 !important;
  background: #181c20 !important;
}

.code-box-content {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0.5rem 0.8rem;
  gap: 0.7rem;
}

.section-code-text {
  font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace;
  font-size: 0.98rem;
  font-weight: 700;
  color: #1e293b;
  letter-spacing: 0.05em;
  flex: 1;
}

.dark .section-code-text {
  color: #FBFFE4;
}

.copy-code-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  background: var(--color-primary, #10b981);
  color: #fff;
  border: none;
  border-radius: 7px;
  padding: 0.45rem 1.1rem;
  font-size: 0.97rem;
  font-weight: 600;
  cursor: pointer;
  transition: background 0.18s, box-shadow 0.18s;
  box-shadow: 0 1px 3px rgba(0,0,0,0.03);
}

.copy-code-btn:hover {
  background: var(--color-primary-dark, #059669);
  box-shadow: 0 2px 6px rgba(0,0,0,0.08);
}

.copy-code-btn.copied {
  background: #20c997;
}

.copy-code-btn.copied:hover {
  background: #059669;
}

.section-stats {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  color: #6b7280;
  font-size: 0.875rem;
  font-weight: 500;
}

.dark .section-stats {
  color: #A3D1C6;
}

/* Dropdown transition */
.dropdown-enter-active,
.dropdown-leave-active {
  transition: all 0.2s ease;
}

.dropdown-enter-from,
.dropdown-leave-to {
  opacity: 0;
  transform: translateY(-10px) scale(0.95);
}

.dropdown-enter-to,
.dropdown-leave-from {
  opacity: 1;
  transform: translateY(0) scale(1);
}

@media (max-width: 768px) {
  .header-content {
    flex-direction: column;
    gap: 1rem;
  }
  
  .header-left {
    width: 100%;
  }
  
  .header-actions {
    align-self: flex-end;
  }
}

/* Enhanced Section Detail Styles */
.section-detail-enhanced {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2rem;
  margin-top: 1.5rem;
}

.section-info-card,
.quick-actions-card {
  background: #ffffff;
  border: 1px solid #e5e7eb;
  border-radius: 12px;
  padding: 1.5rem;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.dark .section-info-card,
.dark .quick-actions-card {
  background: #23272b;
  border: 1px solid #20c997;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.13);
}

.section-header {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 1.5rem;
}

.section-icon {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 48px;
  height: 48px;
  background: linear-gradient(135deg, #10b981, #059669);
  border-radius: 12px;
  color: white;
}

.section-title-info .section-title {
  font-size: 1.25rem;
  font-weight: 700;
  color: #1f2937;
  margin: 0 0 0.25rem 0;
}

.dark .section-title-info .section-title {
  color: #A3D1C6;
}

.section-title-info .section-subtitle {
  font-size: 0.875rem;
  color: #6b7280;
  margin: 0;
}

.dark .section-title-info .section-subtitle {
  color: #A3D1C6;
}

.section-details {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
  margin-bottom: 1.5rem;
}

.detail-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.5rem 0;
  border-bottom: 1px solid #f3f4f6;
}

.dark .detail-item {
  border-bottom-color: #374151;
}

.detail-label {
  font-weight: 600;
  color: #1f2937;
  font-size: 0.875rem;
}

.dark .detail-label {
  color: #A3D1C6;
}

.detail-value {
  font-weight: 500;
  color: #6b7280;
  font-size: 0.875rem;
}

.dark .detail-value {
  color: #A3D1C6;
}

.section-code-container {
  background: #f8f9fa;
  border: 1px solid #e5e7eb;
  border-radius: 8px;
  padding: 1rem;
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.dark .section-code-container {
  background: #181c20;
  border: 1px solid #20c997;
}

.code-label {
  font-size: 0.75rem;
  font-weight: 600;
  color: #6b7280;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.dark .code-label {
  color: #9ca3af;
}

.code-value {
  font-family: 'Monaco', 'Menlo', monospace;
  font-size: 1.125rem;
  font-weight: 700;
  color: #10b981;
  letter-spacing: 0.1em;
  margin-bottom: 0.5rem;
}

.dark .code-value {
  color: #20c997;
}

.copy-btn {
  align-self: flex-start;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem 0.75rem;
  background: #10b981;
  color: white;
  border: none;
  border-radius: 6px;
  font-size: 0.75rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
}

.copy-btn:hover {
  background: #059669;
  transform: translateY(-1px);
}

.actions-title {
  font-size: 1.125rem;
  font-weight: 700;
  color: #1f2937;
  margin: 0 0 1.5rem 0;
}

.dark .actions-title {
  color: #A3D1C6;
}

.actions-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
}

.action-button {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 0.75rem;
  padding: 1.5rem 1rem;
  border: none;
  border-radius: 12px;
  cursor: pointer;
  transition: all 0.2s ease;
  text-decoration: none;
  min-height: 120px;
  background: #ffffff;
  color: #1f2937;
  border: 1px solid #e5e7eb;
}

.dark .action-button {
  background: #23272b;
  color: #A3D1C6;
  border: 1px solid #20c997;
}

.action-button.primary {
  border: 2px solid #10b981;
}

.action-button:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
}

.dark .action-button:hover {
  box-shadow: 0 8px 25px rgba(32, 201, 151, 0.2);
}

.btn-icon {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 32px;
  height: 32px;
  border-radius: 8px;
  background: rgba(16, 185, 129, 0.1);
  color: #10b981;
}

.dark .btn-icon {
  background: rgba(32, 201, 151, 0.1);
  color: #20c997;
}

.btn-text {
  font-size: 0.875rem;
  font-weight: 600;
  text-align: center;
}

@media (max-width: 1024px) {
  .section-detail-enhanced {
    grid-template-columns: 1fr;
    gap: 1.5rem;
  }
}

@media (max-width: 640px) {
  .actions-grid {
    grid-template-columns: 1fr;
  }
  
  .section-detail-enhanced {
    gap: 1rem;
  }
  
  .section-info-card,
  .quick-actions-card {
    padding: 1rem;
  }
}
</style>
