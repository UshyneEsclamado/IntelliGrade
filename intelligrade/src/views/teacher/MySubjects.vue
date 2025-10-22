/* Section Detail Enhancements */
.section-detail-card .info-label {
  color: #1f2937;
  font-weight: 600;
  display: inline-block;
  min-width: 100px;
}
.dark .section-detail-card .info-label {
  color: #A3D1C6;
}

.section-detail-card .info-value {
  color: #6b7280;
  font-weight: 500;
  margin-left: 0.5rem;
}
.dark .section-detail-card .info-value {
  color: #A3D1C6;
}

.section-code {
  background: #f8f9fa;
  color: #1f2937;
  border-radius: 8px;
  padding: 0.5rem 1rem;
  font-size: 1rem;
  font-weight: 600;
  display: inline-block;
}
.dark .section-code {
  background: #181c20;
  color: #A3D1C6;
  border: 1px solid #20c997;
}

.section-actions-grid {
  display: flex;
  gap: 1rem;
  margin-top: 1.5rem;
  justify-content: center;
}

/* Stats and Counts */
.section-stats-simple {
  color: #6b7280;
}
    
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

    <!-- Search Bar and Subjects Grid -->
    <div v-if="viewMode === 'subjects'">
      <!-- Search Bar with Dropdown -->
      <div class="subject-search-bar enhanced extra">
        <div class="search-group extra">
          <select v-model="subjectDropdown" class="subject-dropdown enhanced extra">
            <option v-for="option in subjectOptions" :key="option" :value="option.toLowerCase()">{{ option }}</option>
          </select>
          <div class="search-divider"></div>
          <input
            v-model="searchQuery"
            class="subject-search-input enhanced extra"
            type="text"
            placeholder="Search subjects..."
            @keyup.enter.prevent
          />
          <button class="search-btn extra" tabindex="0" aria-label="Search" @click.prevent>
            <svg width="20" height="20" fill="none" viewBox="0 0 20 20">
              <circle cx="9" cy="9" r="7" stroke="currentColor" stroke-width="2"/>
              <line x1="14.5" y1="14.5" x2="18" y2="18" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
            </svg>
          </button>
        </div>
      </div>
      
      <!-- Empty State -->
      <div v-if="subjects.length === 0" class="empty-state">
        <div class="empty-icon">
          <svg width="48" height="48" fill="none" viewBox="0 0 24 24">
            <path fill="currentColor" d="M12 2a2 2 0 0 1 2 2v1h4a2 2 0 0 1 2 2v1H4V7a2 2 0 0 1 2-2h4V4a2 2 0 0 1 2-2Zm8 7v9a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V9h16Zm-2 2H6v7h12v-7Z"/>
          </svg>
        </div>
        <div class="empty-title">No Subjects Created Yet</div>
        <div class="empty-desc">Create your first subject to start managing your classes and student sections</div>
        <button class="create-quiz-btn" @click="showCreateModal = true">Create Your First Subject</button>
      </div>
      
      <!-- Filtered Results -->
      <div v-else-if="filteredSubjects.length === 0" class="empty-state">
        <div class="empty-icon">
          <svg width="48" height="48" fill="none" viewBox="0 0 48 48">
            <rect x="8" y="16" width="32" height="24" rx="4" fill="#B3D8A8"/>
            <rect x="8" y="16" width="32" height="24" rx="4" stroke="#3D8D7A" stroke-width="2"/>
            <rect x="14" y="22" width="20" height="8" rx="2" fill="#FBFFE4"/>
            <rect x="14" y="22" width="20" height="8" rx="2" stroke="#3D8D7A" stroke-width="1.5"/>
          </svg>
        </div>
        <div class="empty-title">No subjects found</div>
        <div class="empty-desc">Try adjusting your search or filter.</div>
      </div>

      <!-- Subjects Grid -->
      <div v-else class="subjects-grid enhanced">
        <div v-for="subject in filteredSubjects" :key="subject.id" class="subject-card enhanced">
          <!-- Subject Card Header with Menu -->
          <div class="subject-card-header">
            <div class="subject-title-area" @click="selectSubject(subject)">
              <div class="subject-icon" :title="subject.subject_name">
                <span class="subject-initial">{{ (subject.subject_name || subject.name || 'N').charAt(0) }}</span>
              </div>
              <div class="subject-info">
                <h3 class="subject-title">{{ subject.subject_name || subject.name }}</h3>
                <p class="grade-level">{{ subject.grade_level_display }}</p>
              </div>
            </div>
            
            <!-- Subject Menu (3 dots) -->
            <div class="subject-menu-container">
              <button class="subject-menu-btn" @click.stop="toggleSubjectMenu(subject.id)" title="More Options">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                  <circle cx="5" cy="12" r="2" />
                  <circle cx="12" cy="12" r="2" />
                  <circle cx="19" cy="12" r="2" />
                </svg>
              </button>
              <transition name="dropdown">
                <div v-if="openSubjectMenuId === subject.id" class="subject-dropdown-menu">
                  <button @click.stop="editSubject(subject)" class="menu-item">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                      <path d="M20.71,7.04C21.1,6.65 21.1,6 20.71,5.63L18.37,3.29C18,2.9 17.35,2.9 16.96,3.29L15.12,5.12L18.87,8.87M3,17.25V21H6.75L17.81,9.93L14.06,6.18L3,17.25Z" />
                    </svg>
                    Edit Subject
                  </button>
                  <button @click.stop="openDeleteModal('subject', subject)" class="menu-item delete">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                      <path d="M19,4H15.5L14.5,3H9.5L8.5,4H5V6H19M6,19A2,2 0 0,0 8,21H16A2,2 0 0,0 18,19V7H6V19Z" />
                    </svg>
                    Delete Subject
                  </button>
                </div>
              </transition>
            </div>
            
            <div class="arrow-icon" @click="selectSubject(subject)">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                <path d="M8.59,16.58L13.17,12L8.59,7.41L10,6L16,12L10,18L8.59,16.58Z" />
              </svg>
            </div>
          </div>
          
          <div class="subject-divider"></div>
          <div class="subject-stats-container" @click="selectSubject(subject)">
            <p class="subject-stats-simple">{{ subject.section_count }} sections • {{ subject.total_students }} students</p>
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
        <div v-for="section in filteredSections" :key="section.id" class="section-card enhanced">
          <div class="section-card-header">
            <!-- Section icon and title -->
            <div class="section-title-area" @click="selectSection(section)">
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
          
          <div class="section-card-body" @click="selectSection(section)">
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

    <!-- Level 3: Section Detail -->
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

    <!-- Create/Edit Subject Modal - REDESIGNED -->
    <div v-if="showCreateModal" class="modal-overlay" @click="closeModal">
      <div class="modal-content-enhanced" @click.stop>
        <!-- Modal Header -->
        <div class="modal-header-enhanced">
          <div class="modal-icon">
            <svg width="32" height="32" viewBox="0 0 24 24" fill="currentColor">
              <path d="M12 2L2 7V17L12 22L22 17V7M12 4.18L19.55 8L12 11.82L4.45 8M4 9.73L11 13.36V20.27L4 16.64M20 16.64L13 20.27V13.36L20 9.73Z"/>
            </svg>
          </div>
          <div class="modal-title-area">
            <h2>{{ isEditing ? 'Edit Subject' : 'Create New Subject' }}</h2>
            <p class="modal-subtitle">{{ currentStep === 1 ? 'Enter subject details' : 'Configure your sections' }}</p>
          </div>
          <button @click="closeModal" class="close-btn-enhanced">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M19,6.41L17.59,5L12,10.59L6.41,5L5,6.41L10.59,12L5,17.59L6.41,19L12,13.41L17.59,19L19,17.59L13.41,12L19,6.41Z" />
            </svg>
          </button>
        </div>

        <!-- Progress Indicator -->
        <div class="progress-indicator">
          <div class="progress-step" :class="{ active: currentStep === 1, completed: currentStep === 2 }">
            <div class="step-circle">
              <svg v-if="currentStep === 2" width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                <path d="M21,7L9,19L3.5,13.5L4.91,12.09L9,16.17L19.59,5.59L21,7Z"/>
              </svg>
              <span v-else>1</span>
            </div>
            <span class="step-label">Subject Info</span>
          </div>
          <div class="progress-line" :class="{ active: currentStep === 2 }"></div>
          <div class="progress-step" :class="{ active: currentStep === 2 }">
            <div class="step-circle">
              <span>2</span>
            </div>
            <span class="step-label">Section Setup</span>
          </div>
        </div>

        <form @submit.prevent="currentStep === 1 ? nextStep() : saveSubject()" class="subject-form-enhanced">
          <!-- Step 1: Basic Information -->
          <div v-if="currentStep === 1" class="step-content-enhanced">
            <div class="form-grid">
              <div class="form-group-enhanced full-width">
                <label for="subjectName">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M12,3L1,9L12,15L21,10.09V17H23V9M5,13.18V17.18L12,21L19,17.18V13.18L12,17L5,13.18Z"/>
                  </svg>
                  Subject Name <span class="required">*</span>
                </label>
                <input
                  id="subjectName"
                  v-model="formData.name"
                  type="text"
                  placeholder="e.g., English, Mathematics, Science"
                  required
                />
              </div>

              <div class="form-group-enhanced">
                <label for="gradeLevel">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M12,3L1,9L12,15L21,10.09V17H23V9M5,13.18V17.18L12,21L19,17.18V13.18L12,17L5,13.18Z"/>
                  </svg>
                  Grade Level <span class="required">*</span>
                </label>
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

              <div class="form-group-enhanced">
                <label for="numberOfSections">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M19,3H5C3.89,3 3,3.89 3,5V19A2,2 0 0,0 5,21H19A2,2 0 0,0 21,19V5C21,3.89 20.1,3 19,3M19,5V19H5V5H19Z"/>
                  </svg>
                  Number of Sections <span class="required">*</span>
                </label>
                <select id="numberOfSections" v-model="formData.number_of_sections" required @change="generateSections">
                  <option value="">Select Number</option>
                  <option v-for="n in 10" :key="n" :value="n">{{ n }} Section{{ n > 1 ? 's' : '' }}</option>
                </select>
              </div>

              <div class="form-group-enhanced full-width">
                <label for="description">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M14,2H6A2,2 0 0,0 4,4V20A2,2 0 0,0 6,22H18A2,2 0 0,0 20,20V8L14,2M18,20H6V4H13V9H18V20Z"/>
                  </svg>
                  Description <span class="optional">(Optional)</span>
                </label>
                <textarea
                  id="description"
                  v-model="formData.description"
                  placeholder="Brief description of the subject"
                  rows="3"
                ></textarea>
              </div>
            </div>

            <div class="modal-actions-enhanced">
              <button type="button" @click="closeModal" class="btn-secondary">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M19,6.41L17.59,5L12,10.59L6.41,5L5,6.41L10.59,12L5,17.59L6.41,19L12,13.41L17.59,19L19,17.59L13.41,12L19,6.41Z"/>
                </svg>
                Cancel
              </button>
              <button type="submit" :disabled="!canProceedToStep2" class="btn-primary">
                Next: Setup Sections
                <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M4,11V13H16L10.5,18.5L11.92,19.92L19.84,12L11.92,4.08L10.5,5.5L16,11H4Z"/>
                </svg>
              </button>
            </div>
          </div>

          <!-- Step 2: Section Setup -->
          <div v-if="currentStep === 2" class="step-content-enhanced">
            <div class="sections-info-banner">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                <path d="M13,9H11V7H13M13,17H11V11H13M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2Z"/>
              </svg>
              <p>Customize section names below. Unique section codes will be automatically generated.</p>
            </div>

            <div class="sections-setup-enhanced">
              <div v-for="(section, index) in formData.sections" :key="index" class="section-setup-card">
                <div class="section-badge">{{ index + 1 }}</div>
                <div class="section-fields">
                  <div class="field-wrapper">
                    <label :for="'section-' + index">
                      <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor">
                        <path d="M19,3H5C3.89,3 3,3.89 3,5V19A2,2 0 0,0 5,21H19A2,2 0 0,0 21,19V5C21,3.89 20.1,3 19,3M19,5V19H5V5H19Z"/>
                      </svg>
                      Section Name
                    </label>
                    <input
                      :id="'section-' + index"
                      v-model="section.name"
                      type="text"
                      :placeholder="'Section ' + (index + 1)"
                      required
                    />
                  </div>
                  <div class="field-wrapper">
                    <label :for="'max-students-' + index">
                      <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor">
                        <path d="M16,13C15.71,13 15.38,13 15.03,13.05C16.19,13.89 17,15 17,16.5V19H23V16.5C23,14.17 18.33,13 16,13M8,13C5.67,13 1,14.17 1,16.5V19H15V16.5C15,14.17 10.33,13 8,13M8,11A3,3 0 0,0 11,8A3,3 0 0,0 8,5A3,3 0 0,0 5,8A3,3 0 0,0 8,11M16,11A3,3 0 0,0 19,8A3,3 0 0,0 16,5A3,3 0 0,0 13,8A3,3 0 0,0 16,11Z"/>
                      </svg>
                      Max Students
                    </label>
                    <input
                      :id="'max-students-' + index"
                      v-model="section.max_students"
                      type="number"
                      min="1"
                      max="50"
                      placeholder="Default: 40"
                    />
                  </div>
                </div>
                <div class="auto-code-notice">
                  <svg width="12" height="12" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M9,22A1,1 0 0,1 8,21V18H4A2,2 0 0,1 2,16V4C2,2.89 2.9,2 4,2H20A2,2 0 0,1 22,4V16A2,2 0 0,1 20,18H13.9L10.2,21.71C10,21.9 9.75,22 9.5,22V22H9M10,16V19.08L13.08,16H20V4H4V16H10Z"/>
                  </svg>
                  Code will be auto-generated
                </div>
              </div>
            </div>

            <div class="modal-actions-enhanced">
              <button type="button" @click="currentStep = 1" class="btn-secondary">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M20,11V13H8L13.5,18.5L12.08,19.92L4.16,12L12.08,4.08L13.5,5.5L8,11H20Z"/>
                </svg>
                Back
              </button>
              <button type="submit" :disabled="isLoading" class="btn-primary">
                <svg v-if="!isLoading" width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M21,7L9,19L3.5,13.5L4.91,12.09L9,16.17L19.59,5.59L21,7Z"/>
                </svg>
                <svg v-else class="spinner-icon" width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M12,4V2A10,10 0 0,0 2,12H4A8,8 0 0,1 12,4Z"/>
                </svg>
                {{ isLoading ? 'Creating...' : (isEditing ? 'Update Subject' : 'Create Subject') }}
              </button>
            </div>
          </div>
        </form>
      </div>
    </div>

    <!-- Delete Confirmation Modal -->
    <div v-if="showDeleteModal" class="modal-overlay" @click="cancelDelete">
      <div class="modal-content delete-modal" @click.stop>
        <div class="modal-header">
          <div class="delete-icon-header">
            <svg width="48" height="48" viewBox="0 0 24 24" fill="currentColor">
              <path d="M12,2C17.53,2 22,6.47 22,12C22,17.53 17.53,22 12,22C6.47,22 2,17.53 2,12C2,6.47 6.47,2 12,2M15.59,7L12,10.59L8.41,7L7,8.41L10.59,12L7,15.59L8.41,17L12,13.41L15.59,17L17,15.59L13.41,12L17,8.41L15.59,7Z" />
            </svg>
          </div>
          <h2>Delete {{ deleteType === 'subject' ? 'Subject' : 'Section' }}?</h2>
          <button @click="cancelDelete" class="close-btn">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
              <path d="M19,6.41L17.59,5L12,10.59L6.41,5L5,6.41L10.59,12L5,17.59L6.41,19L12,13.41L17.59,19L19,17.59L13.41,12L19,6.41Z" />
            </svg>
          </button>
        </div>

        <div class="delete-modal-body">
          <div class="delete-item-info">
            <h3 class="delete-item-name">
              {{ deleteType === 'subject' ? itemToDelete?.subject_name || itemToDelete?.name : 
                 `${itemToDelete?.subject_name} - ${itemToDelete?.section_name}` }}
            </h3>
            <p class="delete-item-details">
              {{ deleteType === 'subject' ? 'Subject' : 'Section' }} • Grade {{ itemToDelete?.grade_level }}
              <template v-if="deleteType === 'subject'">
                • {{ itemToDelete?.section_count || 0 }} sections • {{ itemToDelete?.total_students || 0 }} students
              </template>
              <template v-else>
                • {{ itemToDelete?.student_count || 0 }} students enrolled
              </template>
            </p>
          </div>
          
          <div class="delete-warning">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
              <path d="M13,14H11V10H13M13,18H11V16H13M1,21H23L12,2L1,21Z" />
            </svg>
            <div class="delete-warning-text">
              <h4>This action cannot be undone!</h4>
              <p v-if="deleteType === 'subject'">
                Deleting this subject will permanently remove <strong>all {{ itemToDelete?.section_count || 0 }} sections</strong> 
                and <strong>unenroll all {{ itemToDelete?.total_students || 0 }} students</strong>. All associated data, quizzes, and grades will be lost.
              </p>
              <p v-else>
                Deleting this section will permanently <strong>unenroll all {{ itemToDelete?.student_count || 0 }} students</strong>. 
                All section data, quizzes, and grades will be lost.
              </p>
            </div>
          </div>
        </div>

        <div class="modal-actions">
          <button @click="cancelDelete" class="cancel-btn">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
              <path d="M19,6.41L17.59,5L12,10.59L6.41,5L5,6.41L10.59,12L5,17.59L6.41,19L12,13.41L17.59,19L19,17.59L13.41,12L19,6.41Z" />
            </svg>
            Cancel
          </button>
          <button @click="confirmDelete" class="delete-confirm-btn" :disabled="isDeleting">
            <svg v-if="!isDeleting" width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
              <path d="M19,4H15.5L14.5,3H9.5L8.5,4H5V6H19M6,19A2,2 0 0,0 8,21H16A2,2 0 0,0 18,19V7H6V19Z" />
            </svg>
            <svg v-else class="spinner" width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
              <path d="M12,4V2A10,10 0 0,0 2,12H4A8,8 0 0,1 12,4Z" />
            </svg>
            {{ isDeleting ? 'Deleting...' : `Delete ${deleteType === 'subject' ? 'Subject' : 'Section'}` }}
          </button>
        </div>
      </div>
    </div>

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
        <p class="loading-text">{{ loadingMessage || 'Loading...' }}</p>
      </div>
    </div>

    <!-- Success Modal -->
    <div v-if="showSuccessModal" class="success-modal" @click.self="closeSuccessModal">
      <div class="success-modal-content">
        <div class="success-icon">
          <svg width="64" height="64" viewBox="0 0 24 24" fill="currentColor">
            <path d="M12,2A10,10 0 0,1 22,12A10,10 0 0,1 12,22A10,10 0 0,1 2,12A10,10 0 0,1 12,2M11,16.5L18,9.5L16.59,8.09L11,13.67L7.41,10.09L6,11.5L11,16.5Z" />
          </svg>
        </div>
        <h3>Success!</h3>
        <p class="success-message-text">{{ successMessage }}</p>
        <button @click="closeSuccessModal" class="success-close-btn">OK</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'
import { supabase } from '../../supabase.js'
import { useDarkMode } from '../../composables/useDarkMode.js'
import { useTeacherAuth } from '../../composables/useTeacherAuth.js'

// Dark mode
const { isDarkMode, initDarkMode, toggleDarkMode } = useDarkMode()

// Authentication
const { teacherInfo, isAuthenticated } = useTeacherAuth()

// Router
const router = useRouter()

// Local State - Main data
const subjects = ref([])
const selectedSubject = ref(null)
const selectedSection = ref(null)
const viewMode = ref('subjects')
const selectedGradeFilter = ref('all')

// Search and filter states
const searchQuery = ref('')
const subjectDropdown = ref('all')

// Modal states
const showCreateModal = ref(false)
const showStudentRosterModal = ref(false)
const currentStudentRoster = ref(null)
const isEditing = ref(false)
const currentSubjectId = ref(null)
const currentStep = ref(1)

// UI states
const copiedCodeId = ref(null)
const showDeleteModal = ref(false)
const deleteType = ref('')
const itemToDelete = ref(null)
const showNotification = ref(false)
const notificationMessage = ref('')
const notificationType = ref('success')
const openMenuId = ref(null)
const openSubjectMenuId = ref(null)
const isLoading = ref(false)
const loadingMessage = ref('')
const isDeleting = ref(false)

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

// Subject filtering and search
const subjectOptions = computed(() => {
  const names = subjects.value.map(s => s.subject_name || s.name)
  const unique = Array.from(new Set(names.filter(Boolean)))
  unique.sort((a, b) => a.localeCompare(b))
  return ['All', ...unique]
})

const filteredSubjects = computed(() => {
  let filtered = subjects.value
  
  if (subjectDropdown.value && subjectDropdown.value.toLowerCase() !== 'all') {
    filtered = filtered.filter(s => {
      const subjectName = (s.subject_name || s.name || '').toLowerCase()
      return subjectName === subjectDropdown.value.toLowerCase()
    })
  }
  
  if (searchQuery.value.trim()) {
    const query = searchQuery.value.trim().toLowerCase()
    filtered = filtered.filter(s => {
      const subjectName = (s.subject_name || s.name || '').toLowerCase()
      return subjectName.includes(query)
    })
  }
  
  return filtered
})

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

// ============================================================
// FETCH SUBJECTS - MAIN FUNCTION
// ============================================================
const fetchSubjects = async (forceRefresh = false) => {
  try {
    if (!teacherInfo.value?.id) {
      console.warn('Teacher ID not available yet')
      return
    }

    isLoading.value = true
    loadingMessage.value = 'Loading your subjects...'

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
          is_active,
          subject_id
        )
      `)
      .eq('teacher_id', teacherInfo.value.id)
      .eq('is_active', true)
      .order('name')

    if (subjectsError) {
      console.error('Supabase error:', subjectsError)
      throw subjectsError
    }

    if (!subjectsData || subjectsData.length === 0) {
      subjects.value = []
      isLoading.value = false
      return
    }

    const subjectGroups = new Map()

    for (const subject of subjectsData) {
      if (subject.sections && subject.sections.length > 0) {
        const subjectName = subject.name

        if (!subjectGroups.has(subjectName)) {
          subjectGroups.set(subjectName, {
            id: subject.id,
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
            const { count, error: countError } = await supabase
              .from('enrollments')
              .select('*', { count: 'exact', head: true })
              .eq('section_id', section.id)
              .eq('status', 'active')

            const studentCount = !countError && count ? count : 0
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

    const processedSubjects = Array.from(subjectGroups.values()).map(group => {
      const gradeLevelsArray = Array.from(group.grade_levels).sort((a, b) => a - b)
      return {
        ...group,
        grade_levels: gradeLevelsArray,
        grade_level: gradeLevelsArray[0],
        grade_level_display: gradeLevelsArray.length === 1 
          ? `Grade ${gradeLevelsArray[0]}` 
          : `Grades ${gradeLevelsArray.join(', ')}`
      }
    })

    subjects.value = processedSubjects
    console.log('Subjects loaded:', processedSubjects)

  } catch (error) {
    console.error('Error fetching subjects:', error)
    showToast('Error loading subjects. Please try again.', 'error')
  } finally {
    isLoading.value = false
  }
}

// ============================================================
// NAVIGATION FUNCTIONS
// ============================================================
const selectSubject = (subject) => {
  selectedSubject.value = subject
  selectedSection.value = null
  selectedGradeFilter.value = 'all'
  viewMode.value = 'sections'
  openSubjectMenuId.value = null
}

const selectSection = (section) => {
  selectedSection.value = section
  viewMode.value = 'section-detail'
  openMenuId.value = null
}

const goBackToSubjects = () => {
  selectedSubject.value = null
  selectedSection.value = null
  selectedGradeFilter.value = 'all'
  viewMode.value = 'subjects'
  openSubjectMenuId.value = null
  openMenuId.value = null
}

const goBackToSections = () => {
  selectedSection.value = null
  viewMode.value = 'sections'
  openMenuId.value = null
}

const setGradeFilter = (grade) => {
  selectedGradeFilter.value = grade
}

// ============================================================
// NAVIGATION TO OTHER ROUTES
// ============================================================
const navigateToCreateQuiz = async (subject, section) => {
  try {
    await router.push({
      name: 'CreateQuiz',
      params: {
        subjectId: section.subject_id,
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
        subjectId: section.subject_id,
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
        subjectId: section.subject_id,
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
        subjectId: sec.subject_id || subject.id,
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

// ============================================================
// SUBJECT MANAGEMENT
// ============================================================
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

const nextStep = () => {
  if (canProceedToStep2.value) {
    generateSections()
    currentStep.value = 2
  }
}

const saveSubject = async () => {
  try {
    isLoading.value = true
    loadingMessage.value = isEditing.value ? 'Updating subject...' : 'Creating subject...'
    
    if (!teacherInfo.value?.id) {
      isLoading.value = false
      showToast('Please login to continue', 'error')
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
      const { error: updateError } = await supabase
        .from('subjects')
        .update(subjectData)
        .eq('id', currentSubjectId.value)
        .eq('teacher_id', teacherInfo.value.id)

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

    closeModal()

    const sectionCodesText = createdSectionCodes.join('\n')
    
    successMessage.value = `Subject "${formData.value.name}" ${isEditing.value ? 'updated' : 'created'} successfully!\n\nSection Codes:\n${sectionCodesText}\n\nShare these codes with your students so they can join their respective sections.`
    showSuccessModal.value = true

    await fetchSubjects(true)
    
    isLoading.value = false

  } catch (error) {
    console.error('Error saving subject:', error)
    isLoading.value = false
    showToast('Error saving subject. Please try again.', 'error')
  }
}

const editSubject = (subject) => {
  isEditing.value = true
  currentSubjectId.value = subject.id
  formData.value = {
    name: subject.subject_name || subject.name,
    grade_level: subject.grade_level.toString(),
    description: subject.description || '',
    number_of_sections: subject.section_count.toString(),
    sections: subject.sections.map(s => ({
      name: s.name,
      max_students: s.max_students
    }))
  }
  currentStep.value = 1
  showCreateModal.value = true
  openSubjectMenuId.value = null
}

// ============================================================
// COPY CODE
// ============================================================
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

// ============================================================
// MODALS
// ============================================================
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

const closeSuccessModal = () => {
  showSuccessModal.value = false
  successMessage.value = ''
}

// ============================================================
// DELETE FUNCTIONALITY
// ============================================================
const openDeleteModal = (type, item) => {
  deleteType.value = type
  itemToDelete.value = item
  showDeleteModal.value = true
  openMenuId.value = null
  openSubjectMenuId.value = null
}

const cancelDelete = () => {
  showDeleteModal.value = false
  itemToDelete.value = null
  deleteType.value = ''
  isDeleting.value = false
}

const confirmDelete = async () => {
  if (deleteType.value === 'subject') {
    await deleteSubjectConfirmed(itemToDelete.value.id)
  } else if (deleteType.value === 'section') {
    await deleteSectionConfirmed(itemToDelete.value.section_id || itemToDelete.value.id)
  }
  showDeleteModal.value = false
  itemToDelete.value = null
  deleteType.value = ''
  isDeleting.value = false
}

const deleteSubjectConfirmed = async (subjectId) => {
  try {
    if (!teacherInfo.value) return

    isDeleting.value = true
    const subject = subjects.value.find(s => s.id === subjectId)

    const sectionIds = subject.sections.map(s => s.id)
    
    if (sectionIds.length > 0) {
      const { error: enrollmentError } = await supabase
        .from('enrollments')
        .delete()
        .in('section_id', sectionIds)
      
      if (enrollmentError) {
        console.error('Error deleting enrollments:', enrollmentError)
        throw enrollmentError
      }
    }

    const { error: sectionsError } = await supabase
      .from('sections')
      .delete()
      .eq('subject_id', subjectId)
    
    if (sectionsError) {
      console.error('Error deleting sections:', sectionsError)
      throw sectionsError
    }

    const { error: subjectError } = await supabase
      .from('subjects')
      .delete()
      .eq('id', subjectId)
      .eq('teacher_id', teacherInfo.value.id)
    
    if (subjectError) {
      console.error('Error deleting subject:', subjectError)
      throw subjectError
    }
    
    subjects.value = subjects.value.filter(s => s.id !== subjectId)
    
    showToast(`Subject "${subject?.name}" and all its sections deleted successfully!`, 'success')
    
  } catch (error) {
    console.error('Delete subject error:', error)
    showToast('Error deleting subject. Please try again.', 'error')
  } finally {
    isDeleting.value = false
  }
}

const deleteSectionConfirmed = async (sectionId) => {
  try {
    isDeleting.value = true

    const { error: enrollmentError } = await supabase
      .from('enrollments')
      .delete()
      .eq('section_id', sectionId)
    
    if (enrollmentError) {
      console.error('Error deleting enrollments:', enrollmentError)
      throw enrollmentError
    }

    const { error: sectionError } = await supabase
      .from('sections')
      .delete()
      .eq('id', sectionId)
    
    if (sectionError) {
      console.error('Error deleting section:', sectionError)
      throw sectionError
    }
    
    if (selectedSubject.value) {
      selectedSubject.value.sections = selectedSubject.value.sections.filter(s => s.id !== sectionId)
      selectedSubject.value.section_count = selectedSubject.value.sections.length
      
      selectedSubject.value.total_students = selectedSubject.value.sections.reduce((sum, s) => sum + (s.student_count || 0), 0)
      
      const subjectIndex = subjects.value.findIndex(s => s.id === selectedSubject.value.id)
      if (subjectIndex !== -1) {
        subjects.value[subjectIndex] = { ...selectedSubject.value }
      }
    }
    
    if (viewMode.value === 'section-detail' && selectedSection.value?.id === sectionId) {
      goBackToSections()
    }
    
    showToast('Section deleted successfully!', 'success')
    
  } catch (error) {
    console.error('Delete section error:', error)
    showToast('Error deleting section. Please try again.', 'error')
  } finally {
    isDeleting.value = false
  }
}

// ============================================================
// NOTIFICATIONS & TOAST
// ============================================================
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

// ============================================================
// SECTION MENU
// ============================================================
const toggleSectionMenu = (sectionId) => {
  if (openMenuId.value === sectionId) {
    openMenuId.value = null
  } else {
    openMenuId.value = sectionId
    openSubjectMenuId.value = null
  }
}

const toggleSubjectMenu = (subjectId) => {
  if (openSubjectMenuId.value === subjectId) {
    openSubjectMenuId.value = null
  } else {
    openSubjectMenuId.value = subjectId
    openMenuId.value = null
  }
}

const editSection = (section) => {
  console.log('Edit section:', section)
  showToast('Edit section feature coming soon!', 'info')
  openMenuId.value = null
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
    showToast(`Section has been ${newStatus === 'archived' ? 'archived' : 'unarchived'}.`, 'success')
  } catch (error) {
    showToast('Error updating section status', 'error')
  }
}

const handleClickOutside = (event) => {
  const targetElement = event.target
  const isOutsideSectionMenu = !targetElement.closest('.section-menu-container')
  const isOutsideSubjectMenu = !targetElement.closest('.subject-menu-container')
  
  if (isOutsideSectionMenu && isOutsideSubjectMenu) {
    openMenuId.value = null
    openSubjectMenuId.value = null
  }
}

// ============================================================
// STUDENT ROSTER
// ============================================================
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

// ============================================================
// LIFECYCLE
// ============================================================
onMounted(async () => {
  try {
    initDarkMode()
    
    const { initializeAuth, setupAuthListener } = useTeacherAuth()
    setupAuthListener()
    
    const authResult = await initializeAuth()
    
    if (!authResult.success) {
      if (authResult.needsLogin || authResult.wrongRole) {
        console.warn('Authentication failed, redirecting to login')
        await router.push('/login')
        return
      }
      console.warn('Auth initialization had issues, but continuing...')
    }
    
    const checkTeacherInfo = setInterval(async () => {
      if (teacherInfo.value?.id) {
        clearInterval(checkTeacherInfo)
        await fetchSubjects()
      } else if (authResult.success === false && authResult.needsLogin) {
        clearInterval(checkTeacherInfo)
      }
    }, 200)

    setTimeout(() => {
      clearInterval(checkTeacherInfo)
      if (!teacherInfo.value?.id && isAuthenticated.value) {
        console.warn('Timeout waiting for teacher info, but authenticated - trying to fetch anyway')
        fetchSubjects()
      }
    }, 10000)
    
    document.addEventListener('click', handleClickOutside)
    
  } catch (error) {
    console.error('Component mount error:', error)
  }
})

onUnmounted(() => {
  document.removeEventListener('click', handleClickOutside)
})
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

/* Further Enhanced Search Bar Styles */
.subject-search-bar.enhanced.extra {
  display: flex;
  align-items: center;
  justify-content: flex-start;
  margin: 1.5rem 0 1.5rem 0;
  padding: 0.75rem 1.5rem;
  background: linear-gradient(90deg, #fbffe4 80%, #e6f7f1 100%);
  border-radius: 16px;
  box-shadow: 0 4px 16px rgba(61, 141, 122, 0.10);
  border: 1.5px solid #a3d1c6;
  transition: box-shadow 0.18s, background 0.18s;
}
.dark .subject-search-bar.enhanced.extra {
  background: #232c2d;
  box-shadow: 0 1.5px 6px rgba(0,0,0,0.10);
  border: 1.5px solid #2a3c36;
  border-radius: 18px;
}
.search-group.extra {
  display: flex;
  align-items: center;
  width: 100%;
  gap: 0;
  background: #fff;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(61, 141, 122, 0.08);
  border: 1.5px solid #a3d1c6;
  overflow: hidden;
  position: relative;
  transition: box-shadow 0.18s;
}
.dark .search-group.extra {
  background: transparent;
  border: none;
  box-shadow: none;
}
.subject-dropdown.enhanced.extra {
  border: none;
  border-radius: 12px 0 0 12px;
  background: transparent;
  color: #3d8d7a;
  font-weight: 500;
  font-size: 1rem;
  min-width: 120px;
  padding: 0.7rem 1.2rem 0.7rem 1.1rem;
  outline: none;
  transition: background 0.18s, color 0.18s, box-shadow 0.18s;
  z-index: 2;
  appearance: none;
  -webkit-appearance: none;
  -moz-appearance: none;
  background-image: url('data:image/svg+xml;utf8,<svg fill="%233d8d7a" height="20" viewBox="0 0 20 20" width="20" xmlns="http://www.w3.org/2000/svg"><path d="M5.516 7.548a.75.75 0 0 1 1.06 0L10 10.97l3.424-3.423a.75.75 0 1 1 1.06 1.06l-3.954 3.954a.75.75 0 0 1-1.06 0L5.516 8.608a.75.75 0 0 1 0-1.06z"/></svg>');
  background-repeat: no-repeat;
  background-position: right 0.5rem center;
  background-size: 1.1em;
  padding-right: 2em;
}
.dark .subject-dropdown.enhanced.extra {
  color: #b3d8a8;
  background-color: #232c2d;
  background-image: url('data:image/svg+xml;utf8,<svg fill="%23b3d8a8" height="20" viewBox="0 0 20 20" width="20" xmlns="http://www.w3.org/2000/svg"><path d="M5.516 7.548a.75.75 0 0 1 1.06 0L10 10.97l3.424-3.423a.75.75 0 1 1 1.06 1.06l-3.954 3.954a.75.75 0 0 1-1.06 0L5.516 8.608a.75.75 0 0 1 0-1.06z"/></svg>');
  color-scheme: dark;
}
.subject-dropdown.enhanced.extra:focus {
  background: #e6f7f1;
  box-shadow: 0 0 0 2px #a3d1c6;
}
.dark .subject-dropdown.enhanced.extra:focus {
  background-color: #232c2d;
  box-shadow: none;
}
.dark .subject-dropdown.enhanced.extra option {
  background-color: #232c2d;
  color: #b3d8a8;
}
.search-divider {
  width: 1.5px;
  height: 2.2rem;
  background: #e6f7f1;
  margin: 0 0.1rem;
  align-self: stretch;
  z-index: 1;
}
.dark .search-divider {
  background: #23332d;
}
.subject-search-input.enhanced.extra {
  flex: 1;
  border: none;
  border-radius: 0;
  background: transparent;
  color: #3d8d7a;
  font-size: 1rem;
  padding: 0.7rem 1.2rem 0.7rem 0.9rem;
  outline: none;
  transition: background 0.18s, color 0.18s, box-shadow 0.18s;
  z-index: 2;
}
.dark .subject-search-input.enhanced.extra {
  color: #b3d8a8;
  background: transparent;
}
.subject-search-input.enhanced.extra:focus {
  background: #e6f7f1;
  box-shadow: 0 0 0 2px #a3d1c6;
}
.dark .subject-search-input.enhanced.extra:focus {
  background: #23332d;
  box-shadow: 0 0 0 2px #3d8d7a;
}
.search-btn.extra {
  background: none;
  border: none;
  border-radius: 0 12px 12px 0;
  color: #3d8d7a;
  padding: 0.7rem 1.1rem 0.7rem 0.7rem;
  cursor: pointer;
  display: flex;
  align-items: center;
  transition: background 0.18s, color 0.18s, transform 0.15s;
  outline: none;
  z-index: 2;
  box-shadow: none;
}
.search-btn.extra:focus, .search-btn.extra:hover {
  background: #e6f7f1;
  color: #17815c;
  transform: scale(1.08);
  box-shadow: 0 2px 8px rgba(61, 141, 122, 0.10);
}
.dark .search-btn.extra {
  color: #b3d8a8;
  background: transparent;
}
.dark .search-btn.extra:focus, .dark .search-btn.extra:hover {
  background: #23332d;
  color: #a3d1c6;
  transform: scale(1.08);
  box-shadow: 0 2px 8px rgba(163, 209, 198, 0.18);
}
@media (max-width: 768px) {
  .subject-search-bar.enhanced.extra {
    flex-direction: column;
    gap: 1rem;
    padding: 0.75rem 0.5rem;
  }
  .search-group.extra {
    flex-direction: column;
    border-radius: 12px;
    box-shadow: none;
    border: none;
    gap: 0.5rem;
  }
  .subject-dropdown.enhanced.extra, .subject-search-input.enhanced.extra {
    border-radius: 12px;
    width: 100%;
    min-width: 0;
    padding: 0.7rem 1.2rem;
  }
  .search-divider {
    display: none;
  }
  .search-btn.extra {
    border-radius: 12px;
    width: 100%;
    justify-content: center;
  }
}

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
  border: 1.5px solid #3D8D7A;
  border-radius: 16px;
  padding: 1.5rem;
  margin-bottom: 1.5rem;
  box-shadow: 0 2px 8px rgba(61, 141, 122, 0.1);
}
.dark .header-card {
  background: #23272b;
  border: 1.5px solid #A3D1C6;
  box-shadow: 0 2px 8px rgba(163, 209, 198, 0.1);
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
.create-quiz-btn {
  background: #20c997;
  color: #181c20;
  border: 1px solid #A3D1C6;
  padding: 0.5rem 1.25rem;
  border-radius: 8px;
  font-size: 0.875rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}
.dark .create-quiz-btn {
  background: #20c997;
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

/* Simple Loading Overlay */
.loading-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 9999;
}

.loading-content {
  background: white;
  padding: 2rem;
  border-radius: 8px;
  text-align: center;
  min-width: 200px;
}

.dark .loading-content {
  background: #232c2d;
  color: #b3d8a8;
}

.loading-spinner {
  width: 40px;
  height: 40px;
  border: 3px solid #e5e7eb;
  border-top: 3px solid #3d8d7a;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin: 0 auto 1rem;
}

.dark .loading-spinner {
  border: 3px solid #2a3c36;
  border-top: 3px solid #b3d8a8;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.loading-text {
  font-size: 1rem;
  font-weight: 500;
  color: #374151;
  margin: 0;
}

.dark .loading-text {
  color: #b3d8a8;
}

/* ============================================
   DELETE MODAL STYLES - Add to your <style scoped>
   ============================================ */

/* Delete Modal Specific Styles */
.delete-modal {
  background: white;
  border-radius: 16px;
  padding: 0;
  max-width: 500px;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
}

.dark .delete-modal {
  background: #1f2937;
  border: 1px solid #374151;
}

.delete-icon-header {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 80px;
  height: 80px;
  margin: 0 auto 1rem;
  background: #fef2f2;
  border-radius: 50%;
  color: #ef4444;
}

.dark .delete-icon-header {
  background: #451a1a;
  color: #f87171;
}

.delete-modal .modal-header {
  flex-direction: column;
  text-align: center;
  padding: 2rem 2rem 1rem;
  border-bottom: 1px solid #f3f4f6;
}

.dark .delete-modal .modal-header {
  border-bottom-color: #374151;
}

.delete-modal .modal-header h2 {
  font-size: 1.5rem;
  color: #1f2937;
  margin: 0;
}

.dark .delete-modal .modal-header h2 {
  color: #f3f4f6;
}

.delete-modal .modal-header .close-btn {
  position: absolute;
  top: 1rem;
  right: 1rem;
  background: transparent;
  border: none;
  color: #9ca3af;
  cursor: pointer;
  padding: 0.5rem;
  border-radius: 8px;
  transition: all 0.2s;
}

.delete-modal .modal-header .close-btn:hover {
  background: #f3f4f6;
  color: #1f2937;
}

.dark .delete-modal .modal-header .close-btn:hover {
  background: #374151;
  color: #f3f4f6;
}

.delete-modal-body {
  padding: 1.5rem 2rem;
}

.delete-item-info {
  text-align: center;
  margin-bottom: 1.5rem;
}

.delete-item-name {
  font-size: 1.125rem;
  font-weight: 700;
  color: #1f2937;
  margin: 0 0 0.5rem 0;
}

.dark .delete-item-name {
  color: #f3f4f6;
}

.delete-item-details {
  font-size: 0.875rem;
  color: #6b7280;
  margin: 0;
}

.dark .delete-item-details {
  color: #9ca3af;
}

.delete-warning {
  display: flex;
  gap: 1rem;
  padding: 1rem;
  background: #fef2f2;
  border: 1px solid #fecaca;
  border-radius: 12px;
  margin-top: 1rem;
}

.dark .delete-warning {
  background: #451a1a;
  border-color: #7f1d1d;
}

.delete-warning svg {
  flex-shrink: 0;
  color: #ef4444;
  margin-top: 0.25rem;
}

.dark .delete-warning svg {
  color: #f87171;
}

.delete-warning-text h4 {
  font-size: 0.875rem;
  font-weight: 700;
  color: #991b1b;
  margin: 0 0 0.5rem 0;
}

.dark .delete-warning-text h4 {
  color: #fca5a5;
}

.delete-warning-text p {
  font-size: 0.875rem;
  color: #7f1d1d;
  margin: 0;
  line-height: 1.5;
}

.dark .delete-warning-text p {
  color: #fca5a5;
}

.delete-warning-text strong {
  font-weight: 700;
  color: #991b1b;
}

.dark .delete-warning-text strong {
  color: #fef2f2;
}

.delete-modal .modal-actions {
  padding: 1rem 2rem 2rem;
  justify-content: center;
  gap: 1rem;
}

.cancel-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  background: white;
  color: #6b7280;
  border: 1px solid #d1d5db;
  padding: 0.75rem 1.5rem;
  border-radius: 8px;
  font-size: 0.875rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
}

.cancel-btn:hover {
  background: #f9fafb;
  border-color: #9ca3af;
  color: #1f2937;
}

.dark .cancel-btn {
  background: #374151;
  color: #d1d5db;
  border-color: #4b5563;
}

.dark .cancel-btn:hover {
  background: #4b5563;
  border-color: #6b7280;
  color: #f3f4f6;
}

.delete-confirm-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  background: #ef4444;
  color: white;
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 8px;
  font-size: 0.875rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
}

.delete-confirm-btn:hover {
  background: #dc2626;
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(239, 68, 68, 0.3);
}

.delete-confirm-btn:disabled {
  background: #9ca3af;
  cursor: not-allowed;
  transform: none;
  box-shadow: none;
}

.dark .delete-confirm-btn {
  background: #dc2626;
}

.dark .delete-confirm-btn:hover {
  background: #b91c1c;
}

.delete-confirm-btn .spinner {
  animation: spin 0.8s linear infinite;
}

/* Subject Menu Styles */
.subject-menu-container {
  position: relative;
}

.subject-menu-btn {
  width: 40px;
  height: 40px;
  background: transparent;
  border: 1px solid transparent;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.2s ease;
  color: #6b7280;
}

.subject-menu-btn:hover {
  background: #f3f4f6;
  border-color: #e5e7eb;
  color: #1f2937;
}

.dark .subject-menu-btn {
  color: #9ca3af;
}

.dark .subject-menu-btn:hover {
  background: #374151;
  border-color: #4b5563;
  color: #f3f4f6;
}

.subject-dropdown-menu {
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

.dark .subject-dropdown-menu {
  background: #1f2937;
  border-color: #374151;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.5);
}

/* Toast Notification Styles */
.toast-notification {
  position: fixed;
  bottom: 2rem;
  right: 2rem;
  background: white;
  border-radius: 12px;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.15);
  z-index: 9999;
  min-width: 320px;
  max-width: 500px;
  overflow: hidden;
  animation: slideInRight 0.3s ease;
}

@keyframes slideInRight {
  from {
    transform: translateX(100%);
    opacity: 0;
  }
  to {
    transform: translateX(0);
    opacity: 1;
  }
}

.toast-success {
  border-left: 4px solid #10b981;
}

.toast-error {
  border-left: 4px solid #ef4444;
}

.toast-info {
  border-left: 4px solid #3b82f6;
}

.dark .toast-notification {
  background: #1f2937;
  border: 1px solid #374151;
}

.toast-content {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1rem 1.25rem;
}

.toast-icon {
  flex-shrink: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 32px;
  height: 32px;
  border-radius: 50%;
}

.toast-success .toast-icon {
  background: #d1fae5;
  color: #10b981;
}

.toast-error .toast-icon {
  background: #fee2e2;
  color: #ef4444;
}

.toast-info .toast-icon {
  background: #dbeafe;
  color: #3b82f6;
}

.dark .toast-success .toast-icon {
  background: #064e3b;
  color: #34d399;
}

.dark .toast-error .toast-icon {
  background: #7f1d1d;
  color: #f87171;
}

.dark .toast-info .toast-icon {
  background: #1e3a8a;
  color: #60a5fa;
}

.toast-message {
  flex: 1;
  font-size: 0.875rem;
  font-weight: 500;
  color: #1f2937;
  line-height: 1.5;
}

.dark .toast-message {
  color: #f3f4f6;
}

.toast-close {
  flex-shrink: 0;
  background: transparent;
  border: none;
  color: #9ca3af;
  cursor: pointer;
  padding: 0.25rem;
  border-radius: 6px;
  transition: all 0.2s;
}

.toast-close:hover {
  background: #f3f4f6;
  color: #1f2937;
}

.dark .toast-close:hover {
  background: #374151;
  color: #f3f4f6;
}

/* Toast transition */
.toast-enter-active,
.toast-leave-active {
  transition: all 0.3s ease;
}

.toast-enter-from {
  transform: translateX(100%);
  opacity: 0;
}

.toast-leave-to {
  transform: translateX(100%);
  opacity: 0;
}

/* Success Modal Styles */
.success-modal {
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
  animation: fadeIn 0.2s ease;
}

.success-modal-content {
  background: white;
  border-radius: 16px;
  padding: 2.5rem 2rem;
  max-width: 500px;
  width: 90%;
  text-align: center;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
  animation: scaleIn 0.3s ease;
}

@keyframes scaleIn {
  from {
    transform: scale(0.9);
    opacity: 0;
  }
  to {
    transform: scale(1);
    opacity: 1;
  }
}

.dark .success-modal-content {
  background: #1f2937;
  border: 1px solid #374151;
}

.success-icon {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 80px;
  height: 80px;
  margin: 0 auto 1.5rem;
  background: #d1fae5;
  border-radius: 50%;
  color: #10b981;
}

.dark .success-icon {
  background: #064e3b;
  color: #34d399;
}

.success-modal-content h3 {
  font-size: 1.5rem;
  font-weight: 700;
  color: #1f2937;
  margin: 0 0 1rem 0;
}

.dark .success-modal-content h3 {
  color: #f3f4f6;
}

.success-message-text {
  font-size: 0.875rem;
  color: #6b7280;
  margin: 0 0 2rem 0;
  line-height: 1.6;
  white-space: pre-line;
}

.dark .success-message-text {
  color: #d1d5db;
}

.success-close-btn {
  background: #10b981;
  color: white;
  border: none;
  padding: 0.75rem 2rem;
  border-radius: 8px;
  font-size: 0.875rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
}

.success-close-btn:hover {
  background: #059669;
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(16, 185, 129, 0.3);
}

.dark .success-close-btn {
  background: #059669;
}

.dark .success-close-btn:hover {
  background: #047857;
}

/* ============================================
   ENHANCED MODAL STYLES - Modern Design
   ============================================ */

.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.6);
  backdrop-filter: blur(4px);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
  animation: fadeIn 0.2s ease;
}

.modal-content-enhanced {
  background: white;
  border-radius: 20px;
  max-width: 700px;
  width: 95%;
  max-height: 90vh;
  overflow-y: auto;
  box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
  animation: slideUp 0.3s ease;
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

.dark .modal-content-enhanced {
  background: #1f2937;
  border: 1px solid #374151;
}

/* Modal Header Enhanced */
.modal-header-enhanced {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 2rem 2rem 1.5rem;
  border-bottom: 1px solid #f3f4f6;
  position: relative;
}

.dark .modal-header-enhanced {
  border-bottom-color: #374151;
}

.modal-icon {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 56px;
  height: 56px;
  background: linear-gradient(135deg, #10b981, #059669);
  border-radius: 16px;
  color: white;
  box-shadow: 0 4px 12px rgba(16, 185, 129, 0.3);
  flex-shrink: 0;
}

.modal-title-area {
  flex: 1;
}

.modal-title-area h2 {
  font-size: 1.5rem;
  font-weight: 700;
  color: #1f2937;
  margin: 0 0 0.25rem 0;
}

.dark .modal-title-area h2 {
  color: #f9fafb;
}

.modal-subtitle {
  font-size: 0.875rem;
  color: #6b7280;
  margin: 0;
}

.dark .modal-subtitle {
  color: #9ca3af;
}

.close-btn-enhanced {
  position: absolute;
  top: 1.5rem;
  right: 1.5rem;
  width: 36px;
  height: 36px;
  background: #f3f4f6;
  border: none;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #6b7280;
  cursor: pointer;
  transition: all 0.2s;
}

.close-btn-enhanced:hover {
  background: #e5e7eb;
  color: #1f2937;
  transform: rotate(90deg);
}

.dark .close-btn-enhanced {
  background: #374151;
  color: #9ca3af;
}

.dark .close-btn-enhanced:hover {
  background: #4b5563;
  color: #f3f4f6;
}

/* Progress Indicator */
.progress-indicator {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 2rem 2rem 1.5rem;
  gap: 1rem;
}

.progress-step {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.5rem;
}

.step-circle {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: #f3f4f6;
  border: 2px solid #e5e7eb;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 0.875rem;
  color: #9ca3af;
  transition: all 0.3s;
}

.progress-step.active .step-circle {
  background: linear-gradient(135deg, #10b981, #059669);
  border-color: #10b981;
  color: white;
  box-shadow: 0 4px 12px rgba(16, 185, 129, 0.3);
}

.progress-step.completed .step-circle {
  background: #10b981;
  border-color: #10b981;
  color: white;
}

.dark .step-circle {
  background: #374151;
  border-color: #4b5563;
  color: #6b7280;
}

.dark .progress-step.active .step-circle {
  background: linear-gradient(135deg, #10b981, #059669);
  border-color: #10b981;
  color: white;
}

.step-label {
  font-size: 0.75rem;
  font-weight: 600;
  color: #9ca3af;
  text-align: center;
}

.progress-step.active .step-label {
  color: #10b981;
}

.progress-step.completed .step-label {
  color: #10b981;
}

.dark .step-label {
  color: #6b7280;
}

.dark .progress-step.active .step-label,
.dark .progress-step.completed .step-label {
  color: #34d399;
}

.progress-line {
  width: 80px;
  height: 2px;
  background: #e5e7eb;
  transition: all 0.3s;
}

.progress-line.active {
  background: #10b981;
}

.dark .progress-line {
  background: #4b5563;
}

.dark .progress-line.active {
  background: #10b981;
}

/* Form Enhanced */
.subject-form-enhanced {
  padding: 0 2rem 2rem;
}

.step-content-enhanced {
  animation: fadeIn 0.3s ease;
}

.form-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.5rem;
}

.form-group-enhanced {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.form-group-enhanced.full-width {
  grid-column: 1 / -1;
}

.form-group-enhanced label {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.875rem;
  font-weight: 600;
  color: #374151;
}

.dark .form-group-enhanced label {
  color: #d1d5db;
}

.form-group-enhanced label svg {
  color: #10b981;
}

.required {
  color: #ef4444;
  font-weight: 700;
}

.optional {
  color: #9ca3af;
  font-weight: 500;
  font-size: 0.75rem;
}

.form-group-enhanced input,
.form-group-enhanced select,
.form-group-enhanced textarea {
  width: 100%;
  background: white;
  border: 2px solid #e5e7eb;
  border-radius: 10px;
  padding: 0.75rem 1rem;
  font-size: 0.875rem;
  font-family: 'Inter', sans-serif;
  color: #1f2937;
  transition: all 0.2s;
}

.form-group-enhanced input:focus,
.form-group-enhanced select:focus,
.form-group-enhanced textarea:focus {
  outline: none;
  border-color: #10b981;
  box-shadow: 0 0 0 3px rgba(16, 185, 129, 0.1);
}

.dark .form-group-enhanced input,
.dark .form-group-enhanced select,
.dark .form-group-enhanced textarea {
  background: #374151;
  border-color: #4b5563;
  color: #f3f4f6;
}

.dark .form-group-enhanced input:focus,
.dark .form-group-enhanced select:focus,
.dark .form-group-enhanced textarea:focus {
  border-color: #10b981;
  box-shadow: 0 0 0 3px rgba(16, 185, 129, 0.1);
}

/* Sections Info Banner */
.sections-info-banner {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  background: linear-gradient(135deg, #ecfdf5, #d1fae5);
  border: 1px solid #a7f3d0;
  border-radius: 12px;
  padding: 1rem 1.25rem;
  margin-bottom: 1.5rem;
}

.dark .sections-info-banner {
  background: linear-gradient(135deg, #064e3b, #065f46);
  border-color: #047857;
}

.sections-info-banner svg {
  color: #10b981;
  flex-shrink: 0;
}

.sections-info-banner p {
  font-size: 0.875rem;
  color: #065f46;
  margin: 0;
  line-height: 1.5;
}

.dark .sections-info-banner p {
  color: #d1fae5;
}

/* Sections Setup Enhanced */
.sections-setup-enhanced {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  max-height: 400px;
  overflow-y: auto;
  padding-right: 0.5rem;
}

/* Custom Scrollbar */
.sections-setup-enhanced::-webkit-scrollbar {
  width: 8px;
}

.sections-setup-enhanced::-webkit-scrollbar-track {
  background: #f3f4f6;
  border-radius: 10px;
}

.dark .sections-setup-enhanced::-webkit-scrollbar-track {
  background: #374151;
}

.sections-setup-enhanced::-webkit-scrollbar-thumb {
  background: #10b981;
  border-radius: 10px;
}

.sections-setup-enhanced::-webkit-scrollbar-thumb:hover {
  background: #059669;
}

.section-setup-card {
  background: #f9fafb;
  border: 2px solid #e5e7eb;
  border-radius: 16px;
  padding: 1.25rem;
  display: flex;
  gap: 1rem;
  transition: all 0.2s;
  position: relative;
}

.section-setup-card:hover {
  border-color: #10b981;
  box-shadow: 0 4px 12px rgba(16, 185, 129, 0.1);
}

.dark .section-setup-card {
  background: #374151;
  border-color: #4b5563;
}

.dark .section-setup-card:hover {
  border-color: #10b981;
}

.section-badge {
  width: 40px;
  height: 40px;
  background: linear-gradient(135deg, #10b981, #059669);
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  color: white;
  font-size: 1rem;
  flex-shrink: 0;
  box-shadow: 0 4px 12px rgba(16, 185, 129, 0.3);
}

.section-fields {
  flex: 1;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
}

.field-wrapper {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.field-wrapper label {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.75rem;
  font-weight: 600;
  color: #6b7280;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.dark .field-wrapper label {
  color: #9ca3af;
}

.field-wrapper label svg {
  color: #10b981;
}

.field-wrapper input {
  width: 100%;
  background: white;
  border: 1px solid #e5e7eb;
  border-radius: 8px;
  padding: 0.625rem 0.875rem;
  font-size: 0.875rem;
  color: #1f2937;
  transition: all 0.2s;
}

.field-wrapper input:focus {
  outline: none;
  border-color: #10b981;
  box-shadow: 0 0 0 3px rgba(16, 185, 129, 0.1);
}

.dark .field-wrapper input {
  background: #1f2937;
  border-color: #374151;
  color: #f3f4f6;
}

.auto-code-notice {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.75rem;
  color: #10b981;
  font-weight: 500;
  margin-top: 0.5rem;
  padding: 0.5rem 0.75rem;
  background: #ecfdf5;
  border-radius: 8px;
}

.dark .auto-code-notice {
  background: #064e3b;
  color: #34d399;
}

/* Modal Actions Enhanced */
.modal-actions-enhanced {
  display: flex;
  justify-content: flex-end;
  gap: 1rem;
  margin-top: 2rem;
  padding-top: 1.5rem;
  border-top: 1px solid #f3f4f6;
}

.dark .modal-actions-enhanced {
  border-top-color: #374151;
}

.btn-primary,
.btn-secondary {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1.5rem;
  border-radius: 10px;
  font-size: 0.875rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
  border: none;
}

.btn-primary {
  background: linear-gradient(135deg, #10b981, #059669);
  color: white;
  box-shadow: 0 4px 12px rgba(16, 185, 129, 0.3);
}

.btn-primary:hover:not(:disabled) {
  background: linear-gradient(135deg, #059669, #047857);
  transform: translateY(-1px);
  box-shadow: 0 6px 16px rgba(16, 185, 129, 0.4);
}

.btn-primary:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.btn-secondary {
  background: white;
  color: #6b7280;
  border: 2px solid #e5e7eb;
}

.btn-secondary:hover {
  background: #f9fafb;
  border-color: #d1d5db;
  color: #1f2937;
}

.dark .btn-secondary {
  background: #374151;
  color: #d1d5db;
  border-color: #4b5563;
}

.dark .btn-secondary:hover {
  background: #4b5563;
  border-color: #6b7280;
  color: #f3f4f6;
}

.spinner-icon {
  animation: spin 0.8s linear infinite;
}

@keyframes spin {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}

/* Responsive */
@media (max-width: 640px) {
  .form-grid {
    grid-template-columns: 1fr;
  }
  
  .section-fields {
    grid-template-columns: 1fr;
  }
  
  .modal-content-enhanced {
    width: 100%;
    max-height: 95vh;
  }
  
  .modal-header-enhanced {
    padding: 1.5rem 1rem 1rem;
  }
  
  .subject-form-enhanced {
    padding: 0 1rem 1.5rem;
  }
  
  .progress-indicator {
    padding: 1.5rem 1rem 1rem;
  }
}
</style>
