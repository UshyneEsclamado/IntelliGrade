

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

/* Enhanced Student Count Display */
.section-stats-primary {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.5rem;
  padding: 1rem;
  background: linear-gradient(135deg, #f0fdf4, #ecfdf5);
  border-radius: 12px;
  margin-bottom: 1rem;
  text-align: center;
}
.dark .section-stats-primary {
  background: linear-gradient(135deg, #064e3b, #065f46);
}

.student-count-large {
  font-size: 2rem;
  font-weight: 700;
  color: #059669;
  line-height: 1;
}
.dark .student-count-large {
  color: #34d399;
}

.student-label {
  font-size: 0.875rem;
  color: #6b7280;
  font-weight: 500;
}
.dark .student-label {
  color: #9ca3af;
}

/* Section Capacity Info */
.section-capacity-info {
  margin-top: 0.75rem;
}

.capacity-indicator {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.capacity-bar {
  width: 100%;
  height: 6px;
  background: #e5e7eb;
  border-radius: 3px;
  overflow: hidden;
}
.dark .capacity-bar {
  background: #374151;
}

.capacity-fill {
  height: 100%;
  background: linear-gradient(90deg, #10b981, #059669);
  border-radius: 3px;
  transition: width 0.3s ease;
}

.capacity-text {
  font-size: 0.75rem;
  color: #6b7280;
  font-weight: 500;
  text-align: center;
}
.dark .capacity-text {
  color: #9ca3af;
}

/* Subject Description */
.subject-description {
  font-size: 0.8rem;
  color: #6b7280;
  margin: 0.5rem 0 0 0;
  line-height: 1.4;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
.dark .subject-description {
  color: #9ca3af;
}

.subject-description-empty {
  font-size: 0.8rem;
  color: #9ca3af;
  font-style: italic;
  margin: 0.5rem 0 0 0;
}
.dark .subject-description-empty {
  color: #6b7280;
}

/* Subject Content Enhanced */
.subject-summary {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  padding: 1rem 1.25rem;
  background: #f8fafc;
  border-radius: 0 0 16px 16px;
  border-top: 1px solid #e2e8f0;
}
.dark .subject-summary {
  background: #1e293b;
  border-top-color: #475569;
}

.summary-stats {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.stat-group {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.25rem;
}

.stat-number {
  font-size: 1.25rem;
  font-weight: 700;
  color: #1f2937;
  line-height: 1;
}
.dark .stat-number {
  color: #f9fafb;
}

.stat-label {
  font-size: 0.75rem;
  color: #6b7280;
  font-weight: 500;
}
.dark .stat-label {
  color: #9ca3af;
}

.stat-divider {
  width: 1px;
  height: 2rem;
  background: #e2e8f0;
}
.dark .stat-divider {
  background: #475569;
}

.view-sections-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  background: #10b981;
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 8px;
  font-size: 0.875rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s;
}
.view-sections-btn:hover {
  background: #059669;
  transform: translateX(2px);
}

/* Section Metadata */
.section-metadata {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
  margin-top: 1rem;
  padding: 1rem;
  background: #f9fafb;
  border-radius: 8px;
}
.dark .section-metadata {
  background: #374151;
}

.metadata-item {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}

.metadata-label {
  font-size: 0.75rem;
  font-weight: 600;
  color: #6b7280;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}
.dark .metadata-label {
  color: #9ca3af;
}

.metadata-value {
  font-size: 0.875rem;
  font-weight: 500;
  color: #1f2937;
}
.dark .metadata-value {
  color: #f9fafb;
}

/* Clean UI - Section code styles removed */

/* Section Detail View Code Styles */
.section-code-details-expanded {
  margin-top: 1rem;
  border: 1px solid #e5e7eb;
  border-radius: 8px;
  overflow: hidden;
}
.dark .section-code-details-expanded {
  border-color: #374151;
}

.section-code-summary-detail {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0.75rem 1rem;
  background: #f9fafb;
  cursor: pointer;
  list-style: none;
  border-bottom: 1px solid #e5e7eb;
}
.dark .section-code-summary-detail {
  background: #1f2937;
  border-bottom-color: #374151;
}

.code-label-small {
  font-size: 0.875rem;
  color: #6b7280;
  font-weight: 500;
}
.dark .code-label-small {
  color: #9ca3af;
}

.code-value-small {
  font-family: 'Courier New', Courier, monospace;
  font-size: 0.875rem;
  color: #374151;
  background: #ffffff;
  padding: 0.25rem 0.5rem;
  border-radius: 4px;
  border: 1px solid #d1d5db;
}
.dark .code-value-small {
  color: #d1d5db;
  background: #111827;
  border-color: #4b5563;
}

.section-code-expanded-detail {
  padding: 1rem;
  background: #ffffff;
}
.dark .section-code-expanded-detail {
  background: #111827;
}

.code-actions {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
}

.code-description {
  font-size: 0.8rem;
  color: #9ca3af;
  font-style: italic;
}

.copy-btn-detail {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  background: transparent;
  border: 1px solid #d1d5db;
  border-radius: 6px;
  padding: 0.5rem 0.75rem;
  font-size: 0.8rem;
  color: #6b7280;
  cursor: pointer;
  transition: all 0.2s;
}
.copy-btn-detail:hover {
  background: #f3f4f6;
  border-color: #9ca3af;
}
.dark .copy-btn-detail {
  border-color: #4b5563;
  color: #9ca3af;
}
.dark .copy-btn-detail:hover {
  background: #1f2937;
  border-color: #6b7280;
}

/* Organized Section Detail Layout */
.section-detail-enhanced-organized {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.section-header-card {
  background: white;
  border: 1px solid #e5e7eb;
  border-radius: 16px;
  padding: 2rem;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
}
.dark .section-header-card {
  background: #1f2937;
  border-color: #374151;
}

.section-main-info {
  display: flex;
  align-items: center;
  gap: 1.5rem;
  margin-bottom: 1rem;
}

.section-icon-large {
  width: 64px;
  height: 64px;
  background: linear-gradient(135deg, #10b981, #059669);
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  box-shadow: 0 4px 12px rgba(16, 185, 129, 0.3);
}

.section-main-title {
  font-size: 1.75rem;
  font-weight: 700;
  color: #1f2937;
  margin-bottom: 0.5rem;
}
.dark .section-main-title {
  color: #f9fafb;
}

.section-meta {
  display: flex;
  gap: 0.75rem;
}

.subject-badge, .grade-badge {
  padding: 0.25rem 0.75rem;
  border-radius: 20px;
  font-size: 0.875rem;
  font-weight: 500;
}

.subject-badge {
  background: #ecfdf5;
  color: #047857;
  border: 1px solid #d1fae5;
}
.dark .subject-badge {
  background: #064e3b;
  color: #34d399;
  border-color: #065f46;
}

.grade-badge {
  background: #eff6ff;
  color: #1d4ed8;
  border: 1px solid #dbeafe;
}
.dark .grade-badge {
  background: #1e3a8a;
  color: #60a5fa;
  border-color: #1e40af;
}

.section-code-minimal {
  margin-top: 1rem;
  padding-top: 1rem;
  border-top: 1px solid #f3f4f6;
}
.dark .section-code-minimal {
  border-top-color: #374151;
}

.code-summary-minimal {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  cursor: pointer;
  list-style: none;
  font-size: 0.875rem;
  color: #6b7280;
  padding: 0.5rem;
  border-radius: 6px;
  transition: all 0.2s;
}
.code-summary-minimal:hover {
  background: #f9fafb;
}
.dark .code-summary-minimal {
  color: #9ca3af;
}
.dark .code-summary-minimal:hover {
  background: #374151;
}

.code-text {
  font-family: 'Courier New', Courier, monospace;
  font-size: 0.8rem;
}

.code-details-minimal {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0.75rem;
  margin-top: 0.5rem;
  background: #f9fafb;
  border-radius: 6px;
}
.dark .code-details-minimal {
  background: #374151;
}

.code-note {
  font-size: 0.75rem;
  color: #9ca3af;
  font-style: italic;
  margin: 0;
}

.copy-btn-minimal {
  display: flex;
  align-items: center;
  gap: 0.25rem;
  background: transparent;
  border: 1px solid #d1d5db;
  border-radius: 4px;
  padding: 0.25rem 0.5rem;
  font-size: 0.7rem;
  color: #6b7280;
  cursor: pointer;
  transition: all 0.2s;
}
.copy-btn-minimal:hover {
  background: #ffffff;
  border-color: #9ca3af;
}
.dark .copy-btn-minimal {
  border-color: #4b5563;
  color: #9ca3af;
}
.dark .copy-btn-minimal:hover {
  background: #1f2937;
  border-color: #6b7280;
}

/* Student Management Card */
.student-management-card {
  background: white;
  border: 1px solid #e5e7eb;
  border-radius: 16px;
  padding: 1.5rem;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
}
.dark .student-management-card {
  background: #1f2937;
  border-color: #374151;
}

.student-overview {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.student-count-display {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1.5rem;
  background: linear-gradient(135deg, #f0fdf4, #ecfdf5);
  border-radius: 12px;
  border-left: 4px solid #10b981;
}
.dark .student-count-display {
  background: linear-gradient(135deg, #064e3b, #065f46);
}

.count-circle {
  width: 64px;
  height: 64px;
  background: #10b981;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 4px 12px rgba(16, 185, 129, 0.3);
}

.count-number {
  font-size: 1.5rem;
  font-weight: 700;
  color: white;
}

.count-info h4 {
  font-size: 1.125rem;
  font-weight: 600;
  color: #1f2937;
  margin: 0 0 0.25rem 0;
}
.dark .count-info h4 {
  color: #f9fafb;
}

.count-info p {
  font-size: 0.875rem;
  color: #6b7280;
  margin: 0;
}
.dark .count-info p {
  color: #9ca3af;
}

.enrollment-actions {
  display: flex;
  gap: 1rem;
}

.add-students-btn {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  background: linear-gradient(135deg, #10b981, #059669);
  color: white;
  border: none;
  padding: 1rem 1.5rem;
  border-radius: 12px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
  box-shadow: 0 4px 12px rgba(16, 185, 129, 0.3);
}
.add-students-btn:hover {
  background: linear-gradient(135deg, #059669, #047857);
  transform: translateY(-2px);
  box-shadow: 0 6px 16px rgba(16, 185, 129, 0.4);
}

.view-students-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  background: transparent;
  color: #10b981;
  border: 2px solid #10b981;
  padding: 1rem 1.5rem;
  border-radius: 12px;
  font-size: 0.875rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
  white-space: nowrap;
}
.view-students-btn:hover {
  background: #ecfdf5;
  transform: translateY(-1px);
}
.dark .view-students-btn {
  color: #34d399;
  border-color: #34d399;
}
.dark .view-students-btn:hover {
  background: #064e3b;
}

/* Academic Actions Card */
.academic-actions-card {
  background: white;
  border: 1px solid #e5e7eb;
  border-radius: 16px;
  padding: 1.5rem;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
}
.dark .academic-actions-card {
  background: #1f2937;
  border-color: #374151;
}

.actions-title {
  font-size: 1.125rem;
  font-weight: 600;
  color: #1f2937;
  margin-bottom: 1rem;
}
.dark .actions-title {
  color: #f9fafb;
}

.actions-grid-organized {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.action-button.secondary {
  display: flex;
  align-items: center;
  gap: 1rem;
  background: #f8fafc;
  color: #475569;
  border: 1px solid #e2e8f0;
  padding: 1rem 1.25rem;
  border-radius: 8px;
  font-size: 0.875rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s;
  text-align: left;
}
.action-button.secondary:hover {
  background: #f1f5f9;
  border-color: #cbd5e1;
  transform: translateX(4px);
}
.dark .action-button.secondary {
  background: #374151;
  color: #d1d5db;
  border-color: #4b5563;
}
.dark .action-button.secondary:hover {
  background: #4b5563;
  border-color: #6b7280;
}

@media (min-width: 1024px) {
  .section-detail-enhanced-organized {
    display: grid;
    grid-template-columns: 1fr;
    gap: 1.5rem;
  }
  
  .student-management-card {
    order: 2;
  }
  
  .academic-actions-card {
    order: 3;
  }
}

/* Add Students Modal Styles */
.add-students-content {
  padding: 0;
  max-height: calc(95vh - 200px);
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  gap: 0;
}

/* Enroll Student by ID Styles */
.enroll-student-section {
  padding: 1.5rem 2rem;
  background: linear-gradient(135deg, #ecfdf5 0%, #d1fae5 100%);
  border: none;
  border-bottom: 3px solid #10b981;
  border-radius: 0;
  flex-shrink: 0;
  box-shadow: none;
  margin: 0;
}

.dark .enroll-student-section {
  background: linear-gradient(135deg, #064e3b 0%, #065f46 100%);
  border-bottom-color: #10b981;
  box-shadow: none;
}

.enroll-header {
  margin-bottom: 1rem;
}

.header-icon-title {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.icon-circle {
  width: 48px;
  height: 48px;
  border-radius: 12px;
  background: linear-gradient(135deg, #10b981, #059669);
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  flex-shrink: 0;
  box-shadow: 0 4px 12px rgba(16, 185, 129, 0.3);
}

.search-icon-circle {
  background: linear-gradient(135deg, #3b82f6, #2563eb);
  box-shadow: 0 4px 12px rgba(59, 130, 246, 0.3);
}

.enroll-header .section-title {
  color: #065f46;
  margin: 0 0 0.25rem 0;
  font-size: 1.125rem;
  font-weight: 700;
}

.dark .enroll-header .section-title {
  color: #6ee7b7;
}

.enroll-description {
  color: #047857;
  font-size: 0.875rem;
  margin: 0;
  line-height: 1.5;
}

.dark .enroll-description {
  color: #a7f3d0;
}

.enroll-form {
  margin-top: 1rem;
}

.enroll-input-wrapper {
  display: flex;
  gap: 0.75rem;
  align-items: center;
  background: white;
  border: 2px solid #10b981;
  border-radius: 10px;
  padding: 0.5rem 0.75rem;
  transition: all 0.2s;
  box-shadow: 0 2px 8px rgba(16, 185, 129, 0.15);
}

.enroll-student-input {
  flex: 1;
  border: none;
  background: transparent;
  outline: none;
  font-size: 0.9375rem;
  color: #1f2937;
  padding: 0.375rem 0;
  font-weight: 500;
}

.dark .enroll-student-input {
  color: #065f46;
}

.enroll-student-input:focus {
  outline: none;
}

.dark .enroll-student-input:focus {
  outline: none;
}

.enroll-student-input::placeholder {
  color: #9ca3af;
  font-weight: 400;
}

.dark .enroll-student-input::placeholder {
  color: #6b7280;
}

.id-icon {
  color: #10b981;
  flex-shrink: 0;
  width: 20px;
  height: 20px;
}

.dark .id-icon {
  color: #10b981;
}

.enroll-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.625rem 1.25rem;
  background: #10b981;
  color: white;
  border: none;
  border-radius: 8px;
  font-weight: 600;
  font-size: 0.875rem;
  cursor: pointer;
  transition: all 0.2s;
  white-space: nowrap;
  box-shadow: 0 2px 6px rgba(16, 185, 129, 0.3);
}

.enroll-btn:hover:not(:disabled) {
  background: #059669;
  transform: translateY(-1px);
  box-shadow: 0 4px 10px rgba(16, 185, 129, 0.4);
}

.enroll-btn:active:not(:disabled) {
  transform: translateY(0);
}

.enroll-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  white-space: nowrap;
  font-size: 0.875rem;
  box-shadow: 0 2px 4px rgba(13, 148, 136, 0.3);
}

.enroll-btn:hover:not(:disabled) {
  background: linear-gradient(135deg, #0f766e, #134e4a);
  transform: translateY(-1px);
  box-shadow: 0 4px 8px rgba(13, 148, 136, 0.4);
}

.enroll-btn:active:not(:disabled) {
  transform: translateY(0);
}

.enroll-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
  transform: none;
  box-shadow: none;
}

.spinner-icon {
  animation: spin 1s linear infinite;
}

@keyframes spin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}

.enrollment-message {
  padding: 0.625rem 0.875rem;
  border-radius: 8px;
  font-size: 0.875rem;
  font-weight: 600;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  animation: slideIn 0.3s ease-out;
}

@keyframes slideIn {
  from {
    opacity: 0;
    transform: translateY(-10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.enrollment-message.success {
  background: #d1fae5;
  color: #065f46;
  border: 2px solid #10b981;
}

.dark .enrollment-message.success {
  background: rgba(16, 185, 129, 0.15);
  color: #6ee7b7;
  border-color: rgba(110, 231, 183, 0.4);
}

.enrollment-message.error {
  background: #fee2e2;
  color: #991b1b;
  border: 2px solid #ef4444;
}

.dark .enrollment-message.error {
  background: rgba(239, 68, 68, 0.15);
  color: #fca5a5;
  border-color: rgba(252, 165, 165, 0.4);
}

/* Modal Divider */
.modal-divider {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 1.5rem 2rem;
  background: #f9fafb;
}

.modal-divider::before,
.modal-divider::after {
  content: '';
  flex: 1;
  height: 2px;
  background: linear-gradient(90deg, transparent, #d1d5db, transparent);
}

.dark .modal-divider::before,
.dark .modal-divider::after {
  background: linear-gradient(90deg, transparent, #374151, transparent);
}

.modal-divider span {
  padding: 0 1.25rem;
  color: #6b7280;
  font-weight: 600;
  font-size: 0.875rem;
  letter-spacing: 0.05em;
  background: white;
  border: 2px solid #e5e7eb;
  border-radius: 20px;
  padding: 0.375rem 1rem;
}

.dark .modal-divider span {
  color: #9ca3af;
  background: #1f2937;
  border-color: #374151;
}

.student-search-section {
  padding: 2rem;
  background: white;
}

.search-header {
  margin-bottom: 1.25rem;
}

.header-icon-title {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.section-title {
  color: #1f2937;
  margin: 0 0 0.25rem 0;
  font-size: 1.125rem;
  font-weight: 700;
}
.dark .section-title {
  color: #f1f5f9;
}

.search-description {
  color: #6b7280;
  font-size: 0.875rem;
  margin: 0;
}
.dark .search-description {
  color: #9ca3af;
}

.search-filters-enhanced {
  display: grid;
  grid-template-columns: 1fr auto;
  gap: 0.5rem;
  margin-bottom: 0.5rem;
  flex-shrink: 0;
}

.search-input-wrapper {
  position: relative;
  display: flex;
  align-items: center;
}

.search-icon {
  position: absolute;
  left: 0.75rem;
  color: #9ca3af;
  pointer-events: none;
  z-index: 1;
}

.student-search-input-enhanced {
  width: 100%;
  padding: 0.875rem 0.875rem 0.875rem 2.75rem;
  border: 2px solid #e5e7eb;
  border-radius: 12px;
  font-size: 1rem;
  transition: all 0.2s;
  background: white;
}
.student-search-input-enhanced:focus {
  outline: none;
  border-color: #10b981;
  box-shadow: 0 0 0 3px rgba(16, 185, 129, 0.1);
}
.dark .student-search-input-enhanced {
  background: #1f2937;
  border-color: #374151;
  color: #f9fafb;
}
.dark .student-search-input-enhanced:focus {
  border-color: #34d399;
  box-shadow: 0 0 0 3px rgba(52, 211, 153, 0.1);
}

.grade-filter-select-enhanced {
  padding: 0.875rem 1rem;
  border: 2px solid #e5e7eb;
  border-radius: 12px;
  font-size: 0.875rem;
  font-weight: 500;
  background: white;
  cursor: pointer;
  transition: all 0.2s;
  min-width: 140px;
}
.grade-filter-select-enhanced:focus {
  outline: none;
  border-color: #10b981;
  box-shadow: 0 0 0 3px rgba(16, 185, 129, 0.1);
}
.dark .grade-filter-select-enhanced {
  background: #1f2937;
  border-color: #374151;
  color: #f9fafb;
}

.search-hint {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.625rem 0.875rem;
  background: #f0fdf4;
  border: 1px solid #bbf7d0;
  border-radius: 6px;
  font-size: 0.8125rem;
  color: #059669;
  flex-shrink: 0;
}
.dark .search-hint {
  background: #064e3b;
  border-color: #065f46;
  color: #34d399;
}

.students-list-section {
  border-top: 1px solid #e5e7eb;
  padding-top: 0.75rem;
  flex: 1;
  display: flex;
  flex-direction: column;
  min-height: 0;
}
.dark .students-list-section {
  border-top-color: #374151;
}

.students-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 0.5rem;
  flex-shrink: 0;
}

.students-header h4 {
  font-size: 1rem;
  font-weight: 600;
  color: #1f2937;
}
.dark .students-header h4 {
  color: #f9fafb;
}

.batch-actions {
  display: flex;
  gap: 0.5rem;
}

.add-batch-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  background: linear-gradient(135deg, #10b981, #059669);
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 6px;
  font-size: 0.875rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s;
}
.add-batch-btn:hover:not(:disabled) {
  background: linear-gradient(135deg, #059669, #047857);
  transform: translateY(-1px);
}
.add-batch-btn:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.clear-selection-btn {
  background: transparent;
  color: #6b7280;
  border: 1px solid #d1d5db;
  padding: 0.5rem 1rem;
  border-radius: 6px;
  font-size: 0.875rem;
  cursor: pointer;
  transition: all 0.2s;
}
.clear-selection-btn:hover {
  background: #f3f4f6;
  border-color: #9ca3af;
}
.dark .clear-selection-btn {
  color: #9ca3af;
  border-color: #374151;
}
.dark .clear-selection-btn:hover {
  background: #1f2937;
  border-color: #4b5563;
}

.loading-state, .empty-search {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.75rem;
  padding: 1.25rem;
  text-align: center;
  color: #6b7280;
  flex-shrink: 0;
}
.dark .loading-state, .dark .empty-search {
  color: #9ca3af;
}

.students-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
  gap: 0.625rem;
  flex: 1;
  overflow-y: auto;
  min-height: 0;
  max-height: 200px;
  padding-right: 0.25rem;
}

.student-card {
  display: flex;
  align-items: center;
  gap: 0.625rem;
  padding: 0.625rem;
  border: 2px solid #e5e7eb;
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.2s;
  position: relative;
  background: white;
}
.student-card:hover {
  border-color: #10b981;
  background: #f0fdf4;
}
.student-card.selected {
  border-color: #10b981;
  background: #ecfdf5;
}
.dark .student-card {
  border-color: #374151;
  background: #1f2937;
}
.dark .student-card:hover {
  border-color: #10b981;
  background: #064e3b;
}
.dark .student-card.selected {
  background: #065f46;
}

.student-avatar {
  width: 48px;
  height: 48px;
  background: linear-gradient(135deg, #3b82f6, #1d4ed8);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  flex-shrink: 0;
}

.student-info h4 {
  font-size: 0.875rem;
  font-weight: 600;
  color: #1f2937;
  margin-bottom: 0.25rem;
}
.dark .student-info h4 {
  color: #f9fafb;
}

.student-id, .student-grade {
  font-size: 0.75rem;
  color: #6b7280;
  margin: 0;
}
.dark .student-id, .dark .student-grade {
  color: #9ca3af;
}

.selection-indicator {
  position: absolute;
  top: 0.5rem;
  right: 0.5rem;
  width: 24px;
  height: 24px;
  background: #10b981;
  border-radius: 50%;
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  transition: all 0.2s;
}
.student-card.selected .selection-indicator {
  opacity: 1;
}

.btn-outline {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  background: transparent;
  color: #10b981;
  border: 1px solid #10b981;
  padding: 0.75rem 1.25rem;
  border-radius: 8px;
  font-size: 0.875rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
}
.btn-outline:hover {
  background: #ecfdf5;
}
.dark .btn-outline {
  color: #34d399;
  border-color: #34d399;
}
.dark .btn-outline:hover {
  background: #064e3b;
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
  <div class="dashboard-container">
    <!-- Top Navigation Bar (Clean) -->
    <nav class="top-navbar">
      <div class="navbar-content">
        <!-- Left: Logo and Brand -->
        <div class="navbar-left">
          <div class="brand-logo">
            <img src="@/assets/LOGO WAY BG.png" alt="IntelliGrade" class="logo-img" />
            <span class="brand-name">IntelliGrade</span>
          </div>
        </div>
        <!-- Center: Empty space for clean look -->
        <div class="navbar-center">
        </div>
        
        <!-- Right: User Profile and Notifications -->
        <div class="navbar-right">
          <!-- Notification Bell -->
          <div class="notif-wrapper">
            <button class="nav-icon-btn rounded-bg" @click="toggleNotifDropdown" aria-label="Notifications">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                <path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"></path>
                <path d="M13.73 21a2 2 0 0 1-3.46 0"></path>
              </svg>
              <span v-if="notifications.length" class="notification-badge">{{ notifications.length }}</span>
            </button>
            
            <!-- Notification Dropdown -->
            <div v-if="showNotifDropdown" class="notification-dropdown">
              <div class="dropdown-header">
                <h3>Notifications</h3>
              </div>
              <div class="notification-list">
                <div v-if="notifications.length === 0" class="no-notifications">
                  No new notifications
                </div>
                <div v-for="notif in notifications" :key="notif.id" class="notification-item" @click="handleNotificationClick(notif)">
                  <div class="notif-content">
                    <h4>{{ notif.title }}</h4>
                    <p>{{ notif.body }}</p>
                    <span class="notif-time">{{ notif.date }}</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
          
          <!-- User Profile -->
          <div class="user-profile-wrapper">
            <div class="user-profile rounded-bg" @click="toggleProfileDropdown">
              <div class="user-avatar">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
                  <circle cx="12" cy="7" r="4"></circle>
                </svg>
              </div>
              <span class="user-name">{{ fullName }}</span>
              <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" class="dropdown-arrow">
                <path d="M7 10l5 5 5-5z"/>
              </svg>
            </div>
            
            <!-- Profile Dropdown -->
            <div v-if="showProfileDropdown" class="profile-dropdown">
              <div class="dropdown-header">
                <div class="profile-info">
                  <div class="profile-avatar">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                      <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
                      <circle cx="12" cy="7" r="4"></circle>
                    </svg>
                  </div>
                  <div class="profile-details">
                    <h4>{{ fullName }}</h4>
                    <p>Teacher</p>
                  </div>
                </div>
              </div>
              
              <div class="dropdown-menu">
                <router-link to="/teacher/settings" class="dropdown-item">
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M12 2C13.1 2 14 2.9 14 4C14 5.1 13.1 6 12 6C10.9 6 10 5.1 10 4C10 2.9 10.9 2 12 2ZM21 9V7L15 1V3H9V1L3 7V9H5V20A2 2 0 0 0 7 22H17A2 2 0 0 0 19 20V9H21M17 20H7V9H10V12H14V9H17V20Z"/>
                  </svg>
                  <span>Profile & Settings</span>
                </router-link>
                
                <div class="dropdown-divider"></div>
                
                <button @click="logout" class="dropdown-item logout-btn">
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M16 17V14H9V10H16V7L21 12L16 17M14 2A2 2 0 0 1 16 4V6H14V4H5V20H14V18H16V20A2 2 0 0 1 14 22H5A2 2 0 0 1 3 20V4A2 2 0 0 1 5 2H14Z"/>
                  </svg>
                  <span>Logout</span>
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </nav>

    <!-- Sidebar Navigation - Custom Tooltip Labels on Hover -->
    <aside class="sidebar" style="background:#3D8D7A; border-right:none;">
      <nav class="sidebar-nav">
        <router-link to="/teacher/dashboard" class="sidebar-item rounded-bg" :class="{ 'active': $route.path === '/teacher/dashboard' }">
          <div class="sidebar-icon">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M10 20v-6h4v6m5-8h3L12 3 2 12h3v8h5v-6h4v6h5v-8z" />
            </svg>
          </div>
          <span class="sidebar-tooltip">Dashboard</span>
        </router-link>
        <router-link to="/teacher/subjects" class="sidebar-item rounded-bg" :class="{ 'active': $route.path.includes('/teacher/subjects') }">
          <div class="sidebar-icon">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <rect x="3" y="7" width="18" height="13" rx="2" />
              <path d="M3 7l9-4 9 4" />
            </svg>
          </div>
          <span class="sidebar-tooltip">Classes</span>
        </router-link>
        <router-link to="/teacher/gradebook" class="sidebar-item rounded-bg" :class="{ 'active': $route.path === '/teacher/gradebook' }">
          <div class="sidebar-icon">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <rect x="4" y="4" width="16" height="16" rx="2" />
              <path d="M8 2v4M16 2v4" />
            </svg>
          </div>
          <span class="sidebar-tooltip">Gradebook</span>
        </router-link>
        <router-link to="/teacher/upload-assessment" class="sidebar-item rounded-bg" :class="{ 'active': $route.path === '/teacher/upload-assessment' }">
          <div class="sidebar-icon">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M12 19V6M5 12l7-7 7 7" />
              <rect x="5" y="19" width="14" height="2" rx="1" />
            </svg>
          </div>
          <span class="sidebar-tooltip">Upload Assessment</span>
        </router-link>
        <router-link to="/teacher/analytics" class="sidebar-item rounded-bg" :class="{ 'active': $route.path === '/teacher/analytics' }">
          <div class="sidebar-icon">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <rect x="3" y="12" width="4" height="8" />
              <rect x="10" y="8" width="4" height="12" />
              <rect x="17" y="4" width="4" height="16" />
            </svg>
          </div>
          <span class="sidebar-tooltip">Analytics</span>
        </router-link>
        <router-link to="/teacher/messages" class="sidebar-item rounded-bg" :class="{ 'active': $route.path === '/teacher/messages' }">
          <div class="sidebar-icon">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <rect x="3" y="5" width="18" height="14" rx="2" />
              <path d="M3 5l9 7 9-7" />
            </svg>
          </div>
          <span class="sidebar-tooltip">Messages</span>
        </router-link>
      </nav>
    </aside>

    <!-- Main Content Area -->
    <main class="main-content">
      <!-- Scroll to Top Button -->
      <button v-if="showScrollTop" @click="scrollToTop" class="scroll-to-top">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
          <path d="M7 14l5-5 5 5z"/>
        </svg>
      </button>
      <!-- Page Header -->
      <div class="page-header">
        <div class="header-content">
          <div class="header-left">
            <div class="header-icon">
              <svg width="28" height="28" viewBox="0 0 24 24" fill="currentColor">
                <path d="M12,3L1,9L12,15L21,10.09V17H23V9M5,13.18V17.18L12,21L19,17.18V13.18L12,17L5,13.18Z"/>
              </svg>
            </div>
            <div>
              <h1 class="header-title">My Subjects</h1>
              <p class="header-subtitle">Manage your classes and student sections</p>
            </div>
          </div>
          
          <div class="header-actions">
            <button @click="showCreateModal = true" class="create-subject-btn">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                <path d="M19,13H13V19H11V13H5V11H11V5H13V11H19V13Z" />
              </svg>
              Create Subject
            </button>
          </div>
        </div>
      </div>

      <!-- Content Area -->
      <div class="content-wrapper">

    <!-- Subjects Overview -->
    <div v-if="viewMode === 'subjects'" class="subjects-overview">
      <!-- Search and Filter Bar -->
      <div class="search-filter-bar">
        <div class="search-input-container">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" class="search-icon">
            <circle cx="11" cy="11" r="8" stroke="currentColor" stroke-width="2"/>
            <path d="m21 21-4.35-4.35" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
          <input
            v-model="searchQuery"
            class="search-input"
            type="text"
            placeholder="Search subjects..."
          />
        </div>
        <select v-model="subjectDropdown" class="grade-filter">
          <option v-for="option in subjectOptions" :key="option" :value="option.toLowerCase()">{{ option }}</option>
        </select>
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
      <div v-else class="subjects-grid">
        <div v-for="subject in filteredSubjects" :key="subject.id" class="subject-card" @click="selectSubject(subject)">
          <div class="subject-card-header">
            <div 
              class="subject-icon" 
              :style="{
                background: getSubjectIconColor(subject.subject_name || subject.name || 'N').bg
              }"
            >
              <span class="subject-initial">{{ (subject.subject_name || subject.name || 'N').charAt(0) }}</span>
            </div>
            
            <!-- Subject Menu -->
            <div class="subject-menu-container" @click.stop>
              <button class="subject-menu-btn" @click="toggleSubjectMenu(subject.id)" title="More Options">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                  <circle cx="5" cy="12" r="2" />
                  <circle cx="12" cy="12" r="2" />
                  <circle cx="19" cy="12" r="2" />
                </svg>
              </button>
              <div v-if="openSubjectMenuId === subject.id" class="subject-dropdown-menu">
                <button @click="editSubject(subject)" class="menu-item">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M20.71,7.04C21.1,6.65 21.1,6 20.71,5.63L18.37,3.29C18,2.9 17.35,2.9 16.96,3.29L15.12,5.12L18.87,8.87M3,17.25V21H6.75L17.81,9.93L14.06,6.18L3,17.25Z" />
                  </svg>
                  Edit
                </button>
                <button @click="openDeleteModal('subject', subject)" class="menu-item delete">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M19,4H15.5L14.5,3H9.5L8.5,4H5V6H19M6,19A2,2 0 0,0 8,21H16A2,2 0 0,0 18,19V7H6V19Z" />
                  </svg>
                  Delete
                </button>
              </div>
            </div>
          </div>
          
          <div class="subject-card-body">
            <h3 class="subject-title">{{ subject.subject_name || subject.name }}</h3>
            <p class="grade-level">Grade {{ subject.grade_level }}</p>
            <p v-if="subject.description" class="subject-description">{{ subject.description }}</p>
            <p v-else class="subject-description-placeholder">No description provided</p>
            
            <div class="subject-stats">
              <div class="stat-item">
                <span class="stat-number">{{ subject.section_count || 0 }}</span>
                <span class="stat-label">{{ (subject.section_count || 0) === 1 ? 'Section' : 'Sections' }}</span>
              </div>
              <div class="stat-item">
                <span class="stat-number">{{ subject.total_students || 0 }}</span>
                <span class="stat-label">{{ (subject.total_students || 0) === 1 ? 'Student' : 'Students' }}</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Sections View -->
    <div v-if="viewMode === 'sections' && selectedSubject" class="sections-view">
      <!-- Navigation -->
      <div class="view-header">
        <button @click="goBackToSubjects" class="back-btn">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
            <path d="M20,11V13H8L13.5,18.5L12.08,19.92L4.16,12L12.08,4.08L13.5,5.5L8,11H20Z" />
          </svg>
          Back to Subjects
        </button>
        <div class="view-title">
          <h2>{{ selectedSubject.subject_name }}</h2>
          <p>Grade {{ selectedSubject.grade_level }} - Manage sections and students</p>
        </div>
      </div>
      
      <div class="sections-grid">
        <div v-for="section in filteredSections" :key="section.id" class="section-card">
          <div class="section-card-header">
            <div class="section-info" @click="selectSection(section)">
              <h3 class="section-title">{{ section.section_name }}</h3>
              <p class="section-subtitle">Grade {{ section.grade_level }}</p>
            </div>
            
            <div class="section-menu-container" @click.stop>
              <button class="section-menu-btn" @click="toggleSectionMenu(section.id)">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                  <circle cx="5" cy="12" r="2" />
                  <circle cx="12" cy="12" r="2" />
                  <circle cx="19" cy="12" r="2" />
                </svg>
              </button>
              <div v-if="openMenuId === section.id" class="section-dropdown-menu">
                <button @click="editSection(section)" class="menu-item">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M20.71,7.04C21.1,6.65 21.1,6 20.71,5.63L18.37,3.29C18,2.9 17.35,2.9 16.96,3.29L15.12,5.12L18.87,8.87M3,17.25V21H6.75L17.81,9.93L14.06,6.18L3,17.25Z" />
                  </svg>
                  Edit
                </button>
                <button @click="openDeleteModal('section', section)" class="menu-item delete">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M19,4H15.5L14.5,3H9.5L8.5,4H5V6H19M6,19A2,2 0 0,0 8,21H16A2,2 0 0,0 18,19V7H6V19Z" />
                  </svg>
                  Delete
                </button>
              </div>
            </div>
          </div>
          
          <div class="section-card-body" @click="selectSection(section)">
            <div class="enrollment-status">
              <div class="student-count">
                <span class="count-number">{{ section.student_count || 0 }}</span>
                <span class="count-label">Students</span>
              </div>
              <div class="capacity-info">
                <div class="capacity-bar">
                  <div 
                    class="capacity-fill" 
                    :style="{ width: `${Math.min((section.student_count || 0) / (section.max_students || 40) * 100, 100)}%` }"
                  ></div>
                </div>
                <span class="capacity-text">{{ section.student_count || 0 }} / {{ section.max_students || 40 }}</span>
              </div>
            </div>
            
            <div class="section-actions" @click.stop>
              <button class="action-btn primary" @click="manageStudents(selectedSubject, section)">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M19 13h-6v6h-2v-6H5v-2h6V5h2v6h6v2z"/>
                </svg>
                Manage Students
              </button>
              <button class="action-btn secondary" @click="selectSection(section)">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M8.59,16.58L13.17,12L8.59,7.41L10,6L16,12L10,18L8.59,16.58Z" />
                </svg>
                View Details
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Section Detail View -->
    <div v-if="viewMode === 'section-detail' && selectedSection" class="section-detail-view">
      <!-- Navigation -->
      <div class="view-header">
        <button @click="goBackToSections" class="back-btn">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
            <path d="M20,11V13H8L13.5,18.5L12.08,19.92L4.16,12L12.08,4.08L13.5,5.5L8,11H20Z" />
          </svg>
          Back to {{ selectedSubject.subject_name }}
        </button>
        <div class="view-title">
          <h2>{{ selectedSection.section_name }}</h2>
          <p>Grade {{ selectedSection.grade_level }} - {{ selectedSection.subject_name }}</p>
        </div>
      </div>

      <!-- Section Overview -->
      <div class="section-overview-card">
        <div class="overview-stats">
          <div class="stat-box">
            <div class="stat-number">{{ selectedSection.student_count || 0 }}</div>
            <div class="stat-label">Students Enrolled</div>
          </div>
          <div class="stat-box">
            <div class="stat-number">{{ selectedSection.max_students || 40 }}</div>
            <div class="stat-label">Max Capacity</div>
          </div>
          <div class="stat-box">
            <div class="stat-number">{{ Math.round(((selectedSection.student_count || 0) / (selectedSection.max_students || 40)) * 100) }}%</div>
            <div class="stat-label">Filled</div>
          </div>
        </div>
      </div>

      <!-- Quick Actions -->
      <div class="quick-actions-section">
        <h3 class="section-heading">Quick Actions</h3>
        <div class="action-cards-grid">
          <!-- Student Management -->
          <div class="action-card student-management">
            <div class="card-header">
              <div class="card-icon student-icon">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M16,4C18.21,4 20,5.79 20,8C20,10.21 18.21,12 16,12C13.79,12 12,10.21 12,8C12,5.79 13.79,4 16,4M16,14C20.42,14 24,15.79 24,18V20H8V18C8,15.79 11.58,14 16,14" />
                </svg>
              </div>
              <h3>Student Management</h3>
            </div>
            <p class="card-description">Manage student enrollment and view class roster</p>
            <div class="card-actions">
              <button 
                @click="manageStudents(selectedSubject, selectedSection)"
                class="action-btn primary"
              >
                <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M19 13h-6v6h-2v-6H5v-2h6V5h2v6h6v2z"/>
                </svg>
                Add Students
              </button>
              <button 
                @click="viewSectionStudents(selectedSubject, selectedSection)"
                class="action-btn secondary"
              >
                <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M12,4A4,4 0 0,1 16,8A4,4 0 0,1 12,12A4,4 0 0,1 8,8A4,4 0 0,1 12,4M12,14C16.42,14 20,15.79 20,18V20H4V18C4,15.79 7.58,14 12,14Z" />
                </svg>
                View All Students
              </button>
            </div>
          </div>

          <!-- Assessment Management -->
          <div class="action-card assessment-management">
            <div class="card-header">
              <div class="card-icon assessment-icon">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M14,2H6A2,2 0 0,0 4,4V20A2,2 0 0,0 6,22H18A2,2 0 0,0 20,20V8L14,2M18,20H6V4H13V9H18V20Z" />
                </svg>
              </div>
              <h3>Assessment Management</h3>
            </div>
            <p class="card-description">Create and manage quizzes and assignments for your students</p>
            <div class="card-actions">
              <div class="assessment-type-buttons">
                <button 
                  @click="showCreateAssessmentModal(selectedSubject, selectedSection, 'quiz')"
                  class="assessment-type-btn quiz-btn"
                >
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M9,5V9H21V7.5L22.5,6L21,4.5L19.5,6L18,4.5L16.5,6L18,7.5V9H15V5H9M9,19V15H15V19H9M21,15V13.5L19.5,12L18,13.5V15H21Z" />
                  </svg>
                  Create Quiz
                  <span class="btn-subtitle">Multiple-choice, True/False, Fill-in-blank</span>
                </button>
                <button 
                  @click="showCreateAssessmentModal(selectedSubject, selectedSection, 'assignment')"
                  class="assessment-type-btn assignment-btn"
                >
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M14,2H6A2,2 0 0,0 4,4V20A2,2 0 0,0 6,22H18A2,2 0 0,0 20,20V8L14,2M18,20H6V4H13V9H18V20Z" />
                  </svg>
                  Create Assignment
                  <span class="btn-subtitle">Essays, Projects, Research tasks</span>
                </button>
              </div>
              <div class="view-assessments-section">
                <button 
                  @click="viewAllAssessments(selectedSubject, selectedSection)"
                  class="action-btn secondary full-width"
                >
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M13,9V3.5L18.5,9M6,2C4.89,2 4,2.89 4,4V20A2,2 0 0,0 6,22H18A2,2 0 0,0 20,20V8L14,2H6Z" />
                  </svg>
                  View All Assessments
                </button>
              </div>
            </div>
          </div>

          <!-- Grade Management -->
          <div class="action-card grade-management">
            <div class="card-header">
              <div class="card-icon grade-icon">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M16,18H18V16H16M16,14H18V12H16M14,18H16V16H14M12,18H14V16H12M12,14H14V12H12M10,18H12V16H10M8,18H10V16H8M8,14H10V12H8M6,18H8V16H6M14,10H16V8H14M12,10H14V8H12M10,10H12V8H10M8,10H10V8H8M6,10H8V8H6M6,14H8V12H6" />
                </svg>
              </div>
              <h3>Grade Management</h3>
            </div>
            <p class="card-description">Review and manage student grades and performance</p>
            <div class="card-actions">
              <button 
                @click="manageGrades(selectedSubject, selectedSection)"
                class="action-btn primary"
              >
                <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M9,5V9H21V7.5L22.5,6L21,4.5L19.5,6L18,4.5L16.5,6L18,7.5V9H15V5H9M9,19V15H15V19H9M21,15V13.5L19.5,12L18,13.5V15H21Z" />
                </svg>
                Manage Grades
              </button>
              <button 
                @click="viewStudentSubmissions(selectedSubject, selectedSection)"
                class="action-btn secondary"
              >
                <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M14,2H6A2,2 0 0,0 4,4V20A2,2 0 0,0 6,22H18A2,2 0 0,0 20,20V8L14,2M18,20H6V4H13V9H18V20M10,19L12,15L14,19H10M9,13H15V14H9V13M9,10H15V11H9V10Z" />
                </svg>
                Student Submissions
              </button>
            </div>
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
            <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
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
              <button type="submit" :disabled="!canProceedToStep2" class="btn-primary" style="margin-left: auto;">
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
          <div class="delete-item-card">
            <div class="item-icon">
              <svg v-if="deleteType === 'subject'" width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                <path d="M12 2L2 7V17L12 22L22 17V7M12 4.18L19.55 8L12 11.82L4.45 8M4 9.73L11 13.36V20.27L4 16.64M20 16.64L13 20.27V13.36L20 9.73Z"/>
              </svg>
              <svg v-else width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                <path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-5 14H7v-2h7v2zm3-4H7v-2h10v2zm0-4H7V7h10v2z"/>
              </svg>
            </div>
            <div class="item-details">
              <h3 class="item-name">
                <template v-if="deleteType === 'subject'">
                  {{ itemToDelete?.subject_name || itemToDelete?.name }}
                </template>
                <template v-else>
                  {{ itemToDelete?.section_name || itemToDelete?.name }}
                </template>
              </h3>
              <div class="item-meta">
                <span class="item-type">{{ deleteType === 'subject' ? 'Subject' : 'Section' }}</span>
                <span class="separator">•</span>
                <span class="item-grade">Grade {{ itemToDelete?.grade_level }}</span>
                <template v-if="deleteType === 'subject'">
                  <span class="separator">•</span>
                  <span class="item-stats">{{ itemToDelete?.section_count || 0 }} sections</span>
                  <span class="separator">•</span>
                  <span class="item-stats">{{ itemToDelete?.total_students || 0 }} students</span>
                </template>
                <template v-else>
                  <span class="separator">•</span>
                  <span class="item-stats">{{ itemToDelete?.student_count || 0 }} students enrolled</span>
                </template>
              </div>
              <template v-if="deleteType === 'section' && itemToDelete?.subject_name">
                <div class="item-parent">
                  <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M12 2L2 7V17L12 22L22 17V7M12 4.18L19.55 8L12 11.82L4.45 8M4 9.73L11 13.36V20.27L4 16.64M20 16.64L13 20.27V13.36L20 9.73Z"/>
                  </svg>
                  <span>{{ itemToDelete.subject_name }}</span>
                </div>
              </template>
            </div>
          </div>
          
          <div class="delete-warning">
            <div class="warning-header">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                <path d="M13,14H11V10H13M13,18H11V16H13M1,21H23L12,2L1,21Z" />
              </svg>
              <h4>This action cannot be undone!</h4>
            </div>
            <div class="warning-content">
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

<!-- Edit Subject Info Modal - Simple Quick Edit -->
<div v-if="showEditSubjectModal" class="modal-overlay" @click="closeEditSubjectModal">
  <div class="modal-content-enhanced" @click.stop style="max-width: 600px;">
    <!-- Modal Header -->
    <div class="modal-header-enhanced">
      <div class="modal-icon">
        <svg width="32" height="32" viewBox="0 0 24 24" fill="currentColor">
          <path d="M20.71,7.04C21.1,6.65 21.1,6 20.71,5.63L18.37,3.29C18,2.9 17.35,2.9 16.96,3.29L15.12,5.12L18.87,8.87M3,17.25V21H6.75L17.81,9.93L14.06,6.18L3,17.25Z" />
        </svg>
      </div>
      <div class="modal-title-area">
        <h2>Edit Subject Information</h2>
        <p class="modal-subtitle">Update subject name and description</p>
      </div>
      <button @click="closeEditSubjectModal" class="close-btn-enhanced">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
          <path d="M19,6.41L17.59,5L12,10.59L6.41,5L5,6.41L10.59,12L5,17.59L6.41,19L12,13.41L17.59,19L19,17.59L13.41,12L19,6.41Z" />
        </svg>
      </button>
    </div>

    <!-- Edit Form -->
    <form @submit.prevent="saveEditedSubjectInfo" class="subject-form-enhanced">
      <div class="step-content-enhanced">
        <div class="form-grid">
          <div class="form-group-enhanced full-width">
            <label for="editSubjectName">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                <path d="M12,3L1,9L12,15L21,10.09V17H23V9M5,13.18V17.18L12,21L19,17.18V13.18L12,17L5,13.18Z"/>
              </svg>
              Subject Name <span class="required">*</span>
            </label>
            <input
              id="editSubjectName"
              v-model="editSubjectData.name"
              type="text"
              placeholder="e.g., English, Mathematics, Science"
              required
            />
          </div>

          <div class="form-group-enhanced full-width">
            <label for="editDescription">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                <path d="M14,2H6A2,2 0 0,0 4,4V20A2,2 0 0,0 6,22H18A2,2 0 0,0 20,20V8L14,2M18,20H6V4H13V9H18V20Z"/>
              </svg>
              Description <span class="optional">(Optional)</span>
            </label>
            <textarea
              id="editDescription"
              v-model="editSubjectData.description"
              placeholder="Brief description of the subject"
              rows="4"
            ></textarea>
          </div>

          <div class="info-note" style="background: #eff6ff; border-left: 3px solid #3b82f6; padding: 1rem; border-radius: 8px; margin-top: 0.5rem;">
            <div style="display: flex; gap: 0.75rem; align-items: start;">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="#3b82f6" style="flex-shrink: 0; margin-top: 2px;">
                <path d="M13,13H11V7H13M13,17H11V15H13M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2Z" />
              </svg>
              <div>
                <p style="margin: 0; color: #1e40af; font-weight: 600; font-size: 0.875rem;">Quick Edit Mode</p>
                <p style="margin: 0.25rem 0 0 0; color: #3730a3; font-size: 0.8125rem;">This will only update the subject name and description. To modify grade level or sections, please delete and recreate the subject.</p>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="modal-actions-enhanced">
        <button type="button" @click="closeEditSubjectModal" class="btn-secondary">
          Cancel
        </button>
        <button type="submit" class="btn-primary" :disabled="isLoading || !editSubjectData.name">
          <svg v-if="!isLoading" width="18" height="18" viewBox="0 0 24 24" fill="currentColor">
            <path d="M21,7L9,19L3.5,13.5L4.91,12.09L9,16.17L19.59,5.59L21,7Z"/>
          </svg>
          <svg v-else class="spinner-icon" width="18" height="18" viewBox="0 0 24 24" fill="currentColor">
            <path d="M12,4V2A10,10 0 0,0 2,12H4A8,8 0 0,1 12,4Z" />
          </svg>
          {{ isLoading ? 'Updating...' : 'Update Subject' }}
        </button>
      </div>
    </form>
  </div>
</div>

<!-- Replace the Add Students Modal section in your Subjects.vue -->

<!-- Add Students Modal - REDESIGNED -->
<div v-if="showAddStudentsModal" class="modal-overlay" @click="closeAddStudentsModal">
  <div class="modal-content-enhanced add-students-modal" @click.stop>
    <!-- Modal Header -->
    <div class="modal-header-enhanced">
      <div class="modal-icon">
        <svg width="32" height="32" viewBox="0 0 24 24" fill="currentColor">
          <path d="M19 13h-6v6h-2v-6H5v-2h6V5h2v6h6v2z"/>
          <path d="M16,4C18.21,4 20,5.79 20,8C20,10.21 18.21,12 16,12C13.79,12 12,10.21 12,8C12,5.79 13.79,4 16,4M16,14C20.42,14 24,15.79 24,18V20H8V18C8,15.79 11.58,14 16,14" />
        </svg>
      </div>
      <div class="modal-title-area">
        <h2>Add Students to Section</h2>
        <p class="modal-subtitle">{{ selectedSectionForStudents?.section_name }} - {{ selectedSubjectForStudents?.subject_name }}</p>
      </div>
      <button @click="closeAddStudentsModal" class="close-btn-enhanced">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
          <path d="M19,6.41L17.59,5L12,10.59L6.41,5L5,6.41L10.59,12L5,17.59L6.41,19L12,13.41L17.59,19L19,17.59L13.41,12L19,6.41Z" />
        </svg>
      </button>
    </div>

    <div class="add-students-content">
      <!-- Add Student by ID Section - ENHANCED -->
      <div class="enroll-student-section">
        <div class="enroll-header">
          <div class="header-icon-title">
            <div class="icon-circle">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                <path d="M19 13h-6v6h-2v-6H5v-2h6V5h2v6h6v2z"/>
              </svg>
            </div>
            <div>
              <h3 class="section-title">Enroll Student by ID</h3>
              <p class="enroll-description">Quick enrollment using student ID number</p>
            </div>
          </div>
        </div>
        
        <div class="enroll-form">
          <div class="enroll-input-wrapper">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" class="id-icon">
              <path d="M22,18V22H18V19H15V16H12L9.74,13.74C9.19,13.91 8.61,14 8,14A6,6 0 0,1 2,8A6,6 0 0,1 8,2A6,6 0 0,1 14,8C14,8.61 13.91,9.19 13.74,9.74L22,18M7,5A1,1 0 0,0 6,6A1,1 0 0,0 7,7A1,1 0 0,0 8,6A1,1 0 0,0 7,5Z"/>
            </svg>
            <input
              v-model="enrollStudentId"
              type="text"
              placeholder="Enter Student ID (e.g., 2024001)"
              class="enroll-student-input"
              @keyup.enter="enrollStudentById"
            />
            <button 
              @click="enrollStudentById" 
              class="enroll-btn"
              :disabled="!enrollStudentId.trim() || isEnrollingStudent"
            >
              <svg v-if="!isEnrollingStudent" width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                <path d="M19 13h-6v6h-2v-6H5v-2h6V5h2v6h6v2z"/>
              </svg>
              <svg v-else class="spinner-icon" width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                <path d="M12,4V2A10,10 0 0,0 2,12H4A8,8 0 0,1 12,4Z"/>
              </svg>
              {{ isEnrollingStudent ? 'Enrolling...' : 'Enroll Student' }}
            </button>
          </div>
          
          <div v-if="enrollmentMessage" class="enrollment-message" :class="enrollmentMessageType">
            <svg v-if="enrollmentMessageType === 'success'" width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
              <path d="M21,7L9,19L3.5,13.5L4.91,12.09L9,16.17L19.59,5.59L21,7Z"/>
            </svg>
            <svg v-else width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
              <path d="M13,13H11V7H13M13,17H11V15H13M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2Z"/>
            </svg>
            {{ enrollmentMessage }}
          </div>
        </div>
      </div>

      <!-- Divider -->
      <div class="modal-divider">
        <span>OR</span>
      </div>

      <!-- Search Students Section - ENHANCED -->
      <div class="student-search-section">
        <div class="search-header">
          <div class="header-icon-title">
            <div class="icon-circle search-icon-circle">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                <path d="M9.5,3A6.5,6.5 0 0,1 16,9.5C16,11.11 15.41,12.59 14.44,13.73L14.71,14H15.5L20.5,19L19,20.5L14,15.5V14.71L13.73,14.44C12.59,15.41 11.11,16 9.5,16A6.5,6.5 0 0,1 3,9.5A6.5,6.5 0 0,1 9.5,3M9.5,5C7,5 5,7 5,9.5C5,12 7,14 9.5,14C12,14 14,12 14,9.5C14,7 12,5 9.5,5Z"/>
              </svg>
            </div>
            <div>
              <h3 class="section-title">Find Existing Students</h3>
              <p class="search-description">Search by name or ID, then select students to add</p>
            </div>
          </div>
        </div>

        <div class="search-filters-enhanced">
          <div class="search-input-wrapper">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" class="search-icon">
              <path d="M9.5,3A6.5,6.5 0 0,1 16,9.5C16,11.11 15.41,12.59 14.44,13.73L14.71,14H15.5L20.5,19L19,20.5L14,15.5V14.71L13.73,14.44C12.59,15.41 11.11,16 9.5,16A6.5,6.5 0 0,1 3,9.5A6.5,6.5 0 0,1 9.5,3M9.5,5C7,5 5,7 5,9.5C5,12 7,14 9.5,14C12,14 14,12 14,9.5C14,7 12,5 9.5,5Z"/>
            </svg>
            <input
              v-model="studentSearchQuery"
              type="text"
              placeholder="Type student name or ID to search..."
              class="student-search-input-enhanced"
              @input="searchStudents"
            />
          </div>
          <select v-model="gradeFilter" class="grade-filter-select-enhanced" @change="searchStudents">
            <option value="">All Grades</option>
            <option v-for="grade in [7, 8, 9, 10]" :key="grade" :value="grade">Grade {{ grade }}</option>
          </select>
        </div>

        <div class="search-hint" v-if="!studentSearchQuery && !availableStudents.length">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
            <path d="M13,9H11V7H13M13,17H11V11H13M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2Z"/>
          </svg>
          Start typing to search for students to add to this section
        </div>
      </div>

      <!-- Available Students List -->
      <div class="students-list-section">
        <div class="students-header">
          <h4>Available Students</h4>
          <div v-if="selectedStudentsToAdd.length > 0" class="batch-actions">
            <button @click="addSelectedStudents" class="add-batch-btn" :disabled="isAddingStudents">
              <svg v-if="!isAddingStudents" width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                <path d="M19 13h-6v6h-2v-6H5v-2h6V5h2v6h6v2z"/>
              </svg>
              <svg v-else class="spinner-icon" width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                <path d="M12,4V2A10,10 0 0,0 2,12H4A8,8 0 0,1 12,4Z"/>
              </svg>
              {{ isAddingStudents ? 'Adding...' : `Add ${selectedStudentsToAdd.length} Student${selectedStudentsToAdd.length > 1 ? 's' : ''}` }}
            </button>
            <button @click="clearSelection" class="clear-selection-btn">Clear</button>
          </div>
        </div>

        <div v-if="isSearchingStudents" class="loading-state">
          <div class="loading-spinner"></div>
          <span>Searching students...</span>
        </div>

        <div v-else-if="availableStudents.length === 0 && studentSearchQuery" class="empty-search">
          <svg width="48" height="48" viewBox="0 0 24 24" fill="currentColor">
            <path d="M12,2A10,10 0 0,1 22,12A10,10 0 0,1 12,22A10,10 0 0,1 2,12A10,10 0 0,1 12,2M7,13H17V11H7"/>
          </svg>
          <p>No students found matching your search</p>
          <p class="empty-subtitle">Try a different search term or check if all eligible students are already enrolled</p>
        </div>

        <div v-else-if="availableStudents.length === 0 && !isSearchingStudents" class="empty-search">
          <svg width="48" height="48" viewBox="0 0 24 24" fill="currentColor">
            <path d="M16,4C18.21,4 20,5.79 20,8C20,10.21 18.21,12 16,12C13.79,12 12,10.21 12,8C12,5.79 13.79,4 16,4M16,14C20.42,14 24,15.79 24,18V20H8V18C8,15.79 11.58,14 16,14" />
          </svg>
          <p>No available students for this section</p>
          <p class="empty-subtitle">All eligible students for Grade {{ selectedSubjectForStudents?.grade_level }} may already be enrolled in this subject</p>
        </div>

        <div v-else class="students-grid">
          <div 
            v-for="student in availableStudents" 
            :key="student.student_id"
            class="student-card"
            :class="{ 'selected': selectedStudentsToAdd.includes(student.student_id) }"
            @click="toggleStudentSelection(student.student_id)"
          >
            <div class="student-avatar">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                <path d="M12,4A4,4 0 0,1 16,8A4,4 0 0,1 12,12A4,4 0 0,1 8,8A4,4 0 0,1 12,4M12,14C16.42,14 20,15.79 20,18V20H4V18C4,15.79 7.58,14 12,14Z" />
              </svg>
            </div>
            <div class="student-info">
              <h4>{{ student.student_name }}</h4>
              <p class="student-id">ID: {{ student.student_number }}</p>
              <p class="student-grade">Grade {{ student.grade_level }}</p>
            </div>
            <div class="selection-indicator">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                <path d="M21,7L9,19L3.5,13.5L4.91,12.09L9,16.17L19.59,5.59L21,7Z"/>
              </svg>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="modal-actions-enhanced">
      <button @click="viewSectionStudents(selectedSubjectForStudents, selectedSectionForStudents)" class="btn-outline">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
          <path d="M16,4C18.21,4 20,5.79 20,8C20,10.21 18.21,12 16,12C13.79,12 12,10.21 12,8C12,5.79 13.79,4 16,4M16,14C20.42,14 24,15.79 24,18V20H8V18C8,15.79 11.58,14 16,14" />
        </svg>
        View All Students
      </button>
      <button @click="closeAddStudentsModal" class="btn-secondary">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
          <path d="M19,6.41L17.59,5L12,10.59L6.41,5L5,6.41L10.59,12L5,17.59L6.41,19L12,13.41L17.59,19L19,17.59L13.41,12L19,6.41Z"/>
        </svg>
        Cancel
      </button>
    </div>
  </div>
</div>
    </div>

    </main>

    <!-- Loading Overlay -->
    <div v-if="isLoading" class="loading-overlay">
      <div class="loading-content">
        <div class="loading-spinner-container">
          <div class="loading-spinner"></div>
          <div class="loading-progress">{{ Math.round(loadingProgress) }}%</div>
        </div>
        <p class="loading-text">{{ loadingMessage || 'Loading...' }}</p>
        <div class="loading-steps">
          <div class="step" :class="{ active: loadingProgress >= 25 }">Authenticating...</div>
          <div class="step" :class="{ active: loadingProgress >= 50 }">Fetching subjects...</div>
          <div class="step" :class="{ active: loadingProgress >= 75 }">Loading enrollments...</div>
          <div class="step" :class="{ active: loadingProgress >= 100 }">Almost done!</div>
        </div>
      </div>
    </div>

    <!-- Edit Section Modal -->
    <div v-if="showEditSectionModal" class="modal-overlay" @click="closeEditSectionModal">
      <div class="modal-content-enhanced" @click.stop>
        <!-- Modal Header -->
        <div class="modal-header-enhanced">
          <div class="modal-icon">
            <svg width="32" height="32" viewBox="0 0 24 24" fill="currentColor">
              <path d="M20.71,7.04C21.1,6.65 21.1,6 20.71,5.63L18.37,3.29C18,2.9 17.35,2.9 16.96,3.29L15.12,5.12L18.87,8.87M3,17.25V21H6.75L17.81,9.93L14.06,6.18L3,17.25Z" />
            </svg>
          </div>
          <div class="modal-title-area">
            <h2>Edit Section</h2>
            <p class="modal-subtitle">Update section information</p>
          </div>
          <button @click="closeEditSectionModal" class="close-btn-enhanced">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M19,6.41L17.59,5L12,10.59L6.41,5L5,6.41L10.59,12L5,17.59L6.41,19L12,13.41L17.59,19L19,17.59L13.41,12L19,6.41Z" />
            </svg>
          </button>
        </div>

        <form @submit.prevent="saveEditedSection" class="subject-form-enhanced">
          <div class="step-content-enhanced">
            <div class="form-grid">
              <div class="form-group-enhanced">
                <label for="editSectionName">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M19,3H5C3.89,3 3,3.89 3,5V19A2,2 0 0,0 5,21H19A2,2 0 0,0 21,19V5C21,3.89 20.1,3 19,3M19,5V19H5V5H19Z"/>
                  </svg>
                  Section Name <span class="required">*</span>
                </label>
                <input
                  id="editSectionName"
                  v-model="editingSectionData.name"
                  type="text"
                  placeholder="e.g., Section A, Grade 7-A"
                  required
                />
              </div>

              <div class="form-group-enhanced">
                <label for="editMaxStudents">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M16,13C15.71,13 15.38,13 15.03,13.05C16.19,13.89 17,15 17,16.5V19H23V16.5C23,14.17 18.33,13 16,13M8,13C5.67,13 1,14.17 1,16.5V19H15V16.5C15,14.17 10.33,13 8,13M8,11A3,3 0 0,0 11,8A3,3 0 0,0 8,5A3,3 0 0,0 5,8A3,3 0 0,0 8,11M16,11A3,3 0 0,0 19,8A3,3 0 0,0 16,5A3,3 0 0,0 13,8A3,3 0 0,0 16,11Z"/>
                  </svg>
                  Max Students <span class="required">*</span>
                </label>
                <input
                  id="editMaxStudents"
                  v-model="editingSectionData.max_students"
                  type="number"
                  min="1"
                  max="100"
                  placeholder="40"
                  required
                />
              </div>

              <div class="form-group-enhanced full-width">
                <label>
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M9,22A1,1 0 0,1 8,21V18H4A2,2 0 0,1 2,16V4C2,2.89 2.9,2 4,2H20A2,2 0 0,1 22,4V16A2,2 0 0,1 20,18H13.9L10.2,21.71C10,21.9 9.75,22 9.5,22V22H9M10,16V19.08L13.08,16H20V4H4V16H10Z"/>
                  </svg>
                  Section Code (Read-only)
                </label>
                <input
                  v-model="editingSectionData.section_code"
                  type="text"
                  readonly
                  style="background: #f3f4f6; color: #6b7280; cursor: not-allowed;"
                />
                <small style="color: #6b7280; font-size: 0.75rem;">Section codes cannot be changed after creation</small>
              </div>
            </div>

            <div class="modal-actions-enhanced">
              <button type="button" @click="closeEditSectionModal" class="btn-secondary">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M19,6.41L17.59,5L12,10.59L6.41,5L5,6.41L10.59,12L5,17.59L6.41,19L12,13.41L17.59,19L19,17.59L13.41,12L19,6.41Z"/>
                </svg>
                Cancel
              </button>
              <button type="submit" :disabled="isLoading" class="btn-primary">
                <svg v-if="!isLoading" width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M21,7L9,19L3.5,13.5L4.91,12.09L9,16.17L19.59,5.59L21,7Z"/>
                </svg>
                <svg v-else class="spinner-icon" width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M12,4V2A10,10 0 0,0 2,12H4A8,8 0 0,1 12,4Z"/>
                </svg>
                {{ isLoading ? 'Updating...' : 'Update Section' }}
              </button>
            </div>
          </div>
        </form>
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

    <!-- Logout Confirmation Modal -->
    <div v-if="showLogoutModal" class="modal-overlay" @click="closeLogoutModal">
      <div class="modal-content logout-modal" @click.stop>
        <div class="modal-header logout-header">
          <h3>Confirm Logout</h3>
        </div>
        <div class="modal-body">
          <div class="logout-icon">
            <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"/>
              <polyline points="16 17 21 12 16 7"/>
              <line x1="21" y1="12" x2="9" y2="12"/>
            </svg>
          </div>
          <p class="logout-message">Are you sure you want to logout?</p>
          <p class="logout-submessage">You will be redirected to the login page.</p>
        </div>
        <div class="modal-footer logout-footer">
          <button @click="closeLogoutModal" class="btn-cancel" :disabled="isLoggingOut">Cancel</button>
          <button @click="confirmLogout" class="btn-logout" :disabled="isLoggingOut">
            <span v-if="!isLoggingOut">Logout</span>
            <span v-else class="loading-text">
              <div class="logout-spinner"></div>
              Redirecting...
            </span>
          </button>
        </div>
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
const loadingMessage = ref('Initializing...')
const isDeleting = ref(false)
const loadingProgress = ref(0)

// Navbar dropdown states
const showNotifDropdown = ref(false)
const showProfileDropdown = ref(false)
const notifications = ref([])
const fullName = ref('Teacher')
const showScrollTop = ref(false)

// Success modal state
const showSuccessModal = ref(false)
const successMessage = ref('')

// Logout modal states
const showLogoutModal = ref(false)
const isLoggingOut = ref(false)

// Auth ready state - NEW
const isAuthReady = ref(false)

// Add Students Modal States
const showAddStudentsModal = ref(false)
const selectedSubjectForStudents = ref(null)
const selectedSectionForStudents = ref(null)
const availableStudents = ref([])
const selectedStudentsToAdd = ref([])
const studentSearchQuery = ref('')
const gradeFilter = ref('')
const isSearchingStudents = ref(false)
const isAddingStudents = ref(false)

// Enrollment by ID states
const enrollStudentId = ref('')
const isEnrollingStudent = ref(false)
const enrollmentMessage = ref('')
const enrollmentMessageType = ref('success') // 'success' or 'error'

// Edit Subject Modal States
const showEditSubjectModal = ref(false)
const editSubjectData = ref({
  id: null,
  name: '',
  description: ''
})

// Form data
const formData = ref({
  name: '',
  grade_level: '',
  description: '',
  number_of_sections: '',
  sections: []
})

// ============================================================
// WAIT FOR AUTH TO BE READY - NEW FUNCTION
// ============================================================
const waitForAuth = async (maxAttempts = 30, intervalMs = 200) => {
  return new Promise((resolve, reject) => {
    let attempts = 0
    
    const checkAuth = setInterval(() => {
      attempts++
      
      // Check if teacher info is available and has an ID
      if (teacherInfo.value?.id) {
        clearInterval(checkAuth)
        isAuthReady.value = true
        console.log('✅ Auth ready:', { id: teacherInfo.value.id })
        resolve(true)
      } else if (attempts >= maxAttempts) {
        clearInterval(checkAuth)
        console.error('❌ Auth timeout after', attempts * intervalMs, 'ms')
        reject(new Error('Authentication timeout'))
      }
    }, intervalMs)
  })
}

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
// COLOR GENERATION FOR SUBJECT ICONS
// ============================================================
const getSubjectIconColor = (subjectName) => {
  const colors = [
    { bg: 'linear-gradient(135deg, #10b981, #059669)', shadow: 'rgba(16, 185, 129, 0.3)' }, // Green
    { bg: 'linear-gradient(135deg, #3b82f6, #1d4ed8)', shadow: 'rgba(59, 130, 246, 0.3)' }, // Blue
    { bg: 'linear-gradient(135deg, #f59e0b, #d97706)', shadow: 'rgba(245, 158, 11, 0.3)' }, // Orange
    { bg: 'linear-gradient(135deg, #ef4444, #dc2626)', shadow: 'rgba(239, 68, 68, 0.3)' }, // Red
    { bg: 'linear-gradient(135deg, #8b5cf6, #7c3aed)', shadow: 'rgba(139, 92, 246, 0.3)' }, // Purple
    { bg: 'linear-gradient(135deg, #06b6d4, #0891b2)', shadow: 'rgba(6, 182, 212, 0.3)' }, // Cyan
    { bg: 'linear-gradient(135deg, #84cc16, #65a30d)', shadow: 'rgba(132, 204, 22, 0.3)' }, // Lime
    { bg: 'linear-gradient(135deg, #f97316, #ea580c)', shadow: 'rgba(249, 115, 22, 0.3)' }, // Orange
    { bg: 'linear-gradient(135deg, #ec4899, #db2777)', shadow: 'rgba(236, 72, 153, 0.3)' }, // Pink
    { bg: 'linear-gradient(135deg, #6366f1, #4f46e5)', shadow: 'rgba(99, 102, 241, 0.3)' }, // Indigo
  ]
  
  // Generate a consistent index based on subject name
  let hash = 0
  for (let i = 0; i < subjectName.length; i++) {
    const char = subjectName.charCodeAt(i)
    hash = ((hash << 5) - hash) + char
    hash = hash & hash // Convert to 32bit integer
  }
  
  const index = Math.abs(hash) % colors.length
  return colors[index]
}

// ============================================================
// COLOR GENERATION FOR SECTION ICONS
// ============================================================
const getSectionIconColor = (sectionName, gradeLevel) => {
  const colors = [
    { bg: 'linear-gradient(135deg, #10b981, #059669)', shadow: 'rgba(16, 185, 129, 0.3)' }, // Green
    { bg: 'linear-gradient(135deg, #3b82f6, #1d4ed8)', shadow: 'rgba(59, 130, 246, 0.3)' }, // Blue
    { bg: 'linear-gradient(135deg, #f59e0b, #d97706)', shadow: 'rgba(245, 158, 11, 0.3)' }, // Orange
    { bg: 'linear-gradient(135deg, #ef4444, #dc2626)', shadow: 'rgba(239, 68, 68, 0.3)' }, // Red
    { bg: 'linear-gradient(135deg, #8b5cf6, #7c3aed)', shadow: 'rgba(139, 92, 246, 0.3)' }, // Purple
    { bg: 'linear-gradient(135deg, #06b6d4, #0891b2)', shadow: 'rgba(6, 182, 212, 0.3)' }, // Cyan
    { bg: 'linear-gradient(135deg, #84cc16, #65a30d)', shadow: 'rgba(132, 204, 22, 0.3)' }, // Lime
    { bg: 'linear-gradient(135deg, #f97316, #ea580c)', shadow: 'rgba(249, 115, 22, 0.3)' }, // Orange
    { bg: 'linear-gradient(135deg, #ec4899, #db2777)', shadow: 'rgba(236, 72, 153, 0.3)' }, // Pink
    { bg: 'linear-gradient(135deg, #6366f1, #4f46e5)', shadow: 'rgba(99, 102, 241, 0.3)' }, // Indigo
  ]
  
  // Generate a consistent index based on section name and grade level
  const combinedString = `${sectionName}-${gradeLevel}`
  let hash = 0
  for (let i = 0; i < combinedString.length; i++) {
    const char = combinedString.charCodeAt(i)
    hash = ((hash << 5) - hash) + char
    hash = hash & hash // Convert to 32bit integer
  }
  
  const index = Math.abs(hash) % colors.length
  return colors[index]
}

// Navbar dropdown methods
const toggleNotifDropdown = () => {
  showNotifDropdown.value = !showNotifDropdown.value
  showProfileDropdown.value = false
}

const toggleProfileDropdown = () => {
  showProfileDropdown.value = !showProfileDropdown.value
  showNotifDropdown.value = false
}

const handleNotificationClick = (notif) => {
  console.log('Notification clicked:', notif)
}

// Logout confirmation modal functions
const openLogoutModal = () => {
  showLogoutModal.value = true
}

const closeLogoutModal = () => {
  showLogoutModal.value = false
}

const confirmLogout = () => {
  console.log('🚪 Logging out...')
  
  // Clear storage immediately
  localStorage.clear()
  sessionStorage.clear()
  
  // Sign out from Supabase (don't wait)
  supabase.auth.signOut().catch(err => console.log('Signout error:', err))
  
  // Immediate redirect - no waiting!
  setTimeout(() => {
    window.location.assign('/login')
  }, 100)
  
  console.log('✅ Logout initiated')
}

const logout = () => {
  openLogoutModal()
}

const scrollToTop = () => {
  window.scrollTo({ top: 0, behavior: 'smooth' })
}

// ============================================================
// FETCH SUBJECTS - OPTIMIZED FOR SPEED
// ============================================================
const fetchSubjects = async (forceRefresh = false) => {
  try {
    if (!teacherInfo.value?.id) {
      console.warn('Teacher ID not available yet')
      return
    }

    isLoading.value = true
    loadingProgress.value = 0
    loadingMessage.value = 'Fetching subjects...'
    console.time('fetchSubjects')

    // Progress: 25% - Start fetching subjects
    loadingProgress.value = 25

    // Single optimized query with enrollment counts using a view or RPC
    const { data: subjectsData, error: subjectsError } = await supabase
      .from('subjects')
      .select(`
        id,
        name,
        grade_level,
        description,
        is_active,
        created_at,
        sections!inner (
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
      .eq('sections.is_active', true)
      .order('name')

    if (subjectsError) {
      console.error('Supabase error:', subjectsError)
      throw subjectsError
    }

    // Progress: 50% - Subjects fetched
    loadingProgress.value = 50
    loadingMessage.value = 'Loading student enrollments...'

    if (!subjectsData || subjectsData.length === 0) {
      subjects.value = []
      loadingProgress.value = 100
      isLoading.value = false
      console.timeEnd('fetchSubjects')
      return
    }

    // Get all section IDs for batch enrollment counting
    const allSectionIds = subjectsData
      .flatMap(subject => subject.sections || [])
      .map(section => section.id)

    console.log(`Fetching enrollments for ${allSectionIds.length} sections...`)

    // Progress: 75% - Processing enrollments
    loadingProgress.value = 75

    // Single batch query for all enrollment counts
    let enrollmentCounts = {}
    if (allSectionIds.length > 0) {
      const { data: enrollmentData, error: enrollmentError } = await supabase
        .from('enrollments')
        .select('section_id')
        .in('section_id', allSectionIds)
        .eq('status', 'active')

      if (enrollmentError) {
        console.warn('Error fetching enrollments:', enrollmentError)
      } else if (enrollmentData) {
        // Count enrollments per section
        enrollmentCounts = enrollmentData.reduce((acc, enrollment) => {
          acc[enrollment.section_id] = (acc[enrollment.section_id] || 0) + 1
          return acc
        }, {})
      }
    }

    console.log('Enrollment counts:', enrollmentCounts)

    // Progress: 90% - Processing data
    loadingProgress.value = 90
    loadingMessage.value = 'Finalizing...'

    // Process subjects efficiently
    const subjectGroups = new Map()

    subjectsData.forEach(subject => {
      if (subject.sections && subject.sections.length > 0) {
        const subjectName = subject.name

        if (!subjectGroups.has(subjectName)) {
          subjectGroups.set(subjectName, {
            id: subject.id,
            subject_name: subjectName,
            name: subjectName,
            description: subject.description,
            sections: [],
            grade_levels: new Set(),
            total_students: 0,
            section_count: 0,
            expanded: false
          })
        }

        const subjectGroup = subjectGroups.get(subjectName)
        subjectGroup.grade_levels.add(subject.grade_level)

        subject.sections.forEach(section => {
          if (section.is_active) {
            const studentCount = enrollmentCounts[section.id] || 0
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
        })
      }
    })

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
    
    // Progress: 100% - Complete
    loadingProgress.value = 100
    loadingMessage.value = 'Complete!'
    
    console.log('Subjects loaded:', processedSubjects)
    console.timeEnd('fetchSubjects')

    // Small delay to show 100% before hiding
    setTimeout(() => {
      isLoading.value = false
      loadingProgress.value = 0
    }, 300)

  } catch (error) {
    console.error('Error fetching subjects:', error)
    showToast('Error loading subjects. Please try again.', 'error')
    loadingProgress.value = 0
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
      name: 'ViewAssessments',
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

// Assessment Management Methods
const showCreateAssessmentModal = (subject, section, assessmentType) => {
  console.log('Creating assessment:', assessmentType, 'for', subject.name, section.name)
  
  switch (assessmentType) {
    case 'quiz':
      navigateToCreateQuiz(subject, section)
      break
    case 'assignment':
      navigateToCreateAssignment(subject, section)
      break
    default:
      console.warn('Unknown assessment type:', assessmentType)
  }
}

const navigateToCreateAssignment = async (subject, section) => {
  try {
    await router.push({
      name: 'CreateAssignment',
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
    // Fallback to quiz creation for now until assignment route is implemented
    navigateToCreateQuiz(subject, section)
  }
}

const viewAllAssessments = async (subject, section) => {
  try {
    await router.push({
      name: 'ViewAssessments',
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
    // Fallback to quiz view for now until assessments route is implemented
    viewQuizzes(subject, section)
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

const viewStudentSubmissions = async (subject, section) => {
  try {
    await router.push({
      name: 'StudentSubmissions',
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

const manageStudents = async (subject, section) => {
  selectedSubjectForStudents.value = subject
  selectedSectionForStudents.value = section
  showAddStudentsModal.value = true
  // Clear previous search state
  availableStudents.value = []
  selectedStudentsToAdd.value = []
  studentSearchQuery.value = ''
  gradeFilter.value = subject.grade_level.toString()
  
  // Automatically load available students when modal opens
  await searchStudents()
}

// ============================================================
// SUBJECT MANAGEMENT - ENHANCED WITH AUTH CHECKS
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
    // CRITICAL: Check if auth is ready before proceeding
    if (!isAuthReady.value || !teacherInfo.value?.id) {
      console.warn('⚠️ Auth not ready, waiting...')
      showToast('Please wait, authenticating...', 'info')
      
      try {
        await waitForAuth()
      } catch (error) {
        showToast('Authentication failed. Please reload the page.', 'error')
        return
      }
    }
    
    isLoading.value = true
    loadingMessage.value = isEditing.value ? 'Updating subject...' : 'Creating subject...'
    
    console.log('📝 Saving subject with teacher ID:', teacherInfo.value.id)

    const subjectData = {
      name: formData.value.name,
      grade_level: parseInt(formData.value.grade_level),
      teacher_id: teacherInfo.value.id,
      description: formData.value.description || null,
      is_active: true
    }

    let subjectId

    if (isEditing.value) {
      console.log('✏️ Updating existing subject:', currentSubjectId.value)
      
      const { error: updateError } = await supabase
        .from('subjects')
        .update(subjectData)
        .eq('id', currentSubjectId.value)
        .eq('teacher_id', teacherInfo.value.id)

      if (updateError) {
        console.error('❌ Update error:', updateError)
        throw updateError
      }
      
      subjectId = currentSubjectId.value

      // Delete old sections
      const { error: deleteError } = await supabase
        .from('sections')
        .delete()
        .eq('subject_id', subjectId)
      
      if (deleteError) {
        console.error('❌ Delete sections error:', deleteError)
        throw deleteError
      }

    } else {
      console.log('➕ Creating new subject')
      
      const { data: newSubject, error: insertError } = await supabase
        .from('subjects')
        .insert([subjectData])
        .select()
        .single()

      if (insertError) {
        console.error('❌ Insert error:', insertError)
        throw insertError
      }
      
      if (!newSubject || !newSubject.id) {
        throw new Error('Failed to create subject - no ID returned')
      }
      
      subjectId = newSubject.id
      console.log('✅ Subject created with ID:', subjectId)
    }

    // Create sections
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

    console.log('📋 Inserting', sectionsToInsert.length, 'sections')
    
    const { error: sectionsError } = await supabase
      .from('sections')
      .insert(sectionsToInsert)
    
    if (sectionsError) {
      console.error('❌ Sections insert error:', sectionsError)
      throw sectionsError
    }

    console.log('✅ All sections created successfully')

    // Close modal
    closeModal()

    // Show success message - Updated for teacher-managed enrollment
    const sectionsCreatedText = formData.value.sections.map(section => `• ${section.name}`).join('\n')
    
    successMessage.value = `Subject "${formData.value.name}" ${isEditing.value ? 'updated' : 'created'} successfully!\n\nSections Created:\n${sectionsCreatedText}\n\nYou can now add students directly to each section through the "Manage Students" option.`
    showSuccessModal.value = true

    // Refresh subjects list
    console.log('🔄 Refreshing subjects list...')
    await fetchSubjects(true)
    
    isLoading.value = false
    console.log('✅ Save complete!')

  } catch (error) {
    console.error('❌ Save subject error:', error)
    isLoading.value = false
    
    // Show detailed error message with better handling for duplicate key
    let errorMessage = 'Error saving subject. '
    
    if (error.message) {
      // Check for duplicate key constraint violation
      if (error.message.includes('duplicate key') || error.code === '23505') {
        errorMessage = `You already have a subject named "${formData.value.name}" for Grade ${formData.value.grade_level}. `
        errorMessage += 'Please use a different name or edit the existing subject instead.'
      } else {
        errorMessage += error.message
      }
    } else {
      errorMessage += 'Please try again.'
    }
    
    if (error.code && !error.message.includes('duplicate key')) {
      errorMessage += ` (Code: ${error.code})`
    }
    
    showToast(errorMessage, 'error')
  }
}

const editSubject = (subject) => {
  // Open the simple edit modal instead
  editSubjectData.value = {
    id: subject.id,
    name: subject.subject_name || subject.name,
    description: subject.description || ''
  }
  showEditSubjectModal.value = true
  openSubjectMenuId.value = null
}

// Save edited subject info (simple update - name and description only)
const saveEditedSubjectInfo = async () => {
  try {
    if (!editSubjectData.value.name) {
      showToast('Subject name is required', 'error')
      return
    }

    isLoading.value = true

    const { error } = await supabase
      .from('subjects')
      .update({
        name: editSubjectData.value.name,
        description: editSubjectData.value.description || null
      })
      .eq('id', editSubjectData.value.id)
      .eq('teacher_id', teacherInfo.value.id)

    if (error) {
      console.error('Error updating subject:', error)
      throw error
    }

    showToast('Subject updated successfully!', 'success')
    closeEditSubjectModal()
    
    // Refresh subjects list
    await fetchSubjects(true)

    isLoading.value = false
  } catch (error) {
    console.error('Error saving subject info:', error)
    showToast('Error updating subject. Please try again.', 'error')
    isLoading.value = false
  }
}

// Close edit subject modal
const closeEditSubjectModal = () => {
  showEditSubjectModal.value = false
  editSubjectData.value = {
    id: null,
    name: '',
    description: ''
  }
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
// ADD STUDENTS MODAL FUNCTIONS
// ============================================================
const closeAddStudentsModal = () => {
  showAddStudentsModal.value = false
  selectedSubjectForStudents.value = null
  selectedSectionForStudents.value = null
  availableStudents.value = []
  selectedStudentsToAdd.value = []
  studentSearchQuery.value = ''
  gradeFilter.value = ''
  isSearchingStudents.value = false
  isAddingStudents.value = false
  
  // Reset enrollment fields
  enrollStudentId.value = ''
  isEnrollingStudent.value = false
  enrollmentMessage.value = ''
  enrollmentMessageType.value = 'success'
}

// Enroll student by ID function
const enrollStudentById = async () => {
  if (!enrollStudentId.value.trim()) {
    enrollmentMessage.value = 'Please enter a student ID'
    enrollmentMessageType.value = 'error'
    return
  }

  if (!selectedSectionForStudents.value || !selectedSubjectForStudents.value) {
    enrollmentMessage.value = 'No section selected'
    enrollmentMessageType.value = 'error'
    return
  }

  try {
    isEnrollingStudent.value = true
    enrollmentMessage.value = ''

    // Wait for auth to be ready
    if (!isAuthReady.value || !teacherInfo.value?.id) {
      await waitForAuth()
    }

    // Find student by student_id (student_number)
    const { data: existingStudent, error: studentError } = await supabase
      .from('students')
      .select('id, student_id, full_name, grade_level')
      .eq('student_id', enrollStudentId.value.trim())
      .eq('is_active', true)
      .single()

    if (studentError) {
      if (studentError.code === 'PGRST116') {
        enrollmentMessage.value = `Student with ID "${enrollStudentId.value}" not found in the system`
        enrollmentMessageType.value = 'error'
        return
      }
      throw studentError
    }

    // Use the teacher_add_student_to_section database function
    const { data, error: enrollError } = await supabase.rpc('teacher_add_student_to_section', {
      p_teacher_id: teacherInfo.value.id,
      p_student_id: existingStudent.id,
      p_section_id: selectedSectionForStudents.value.id
    })

    if (enrollError) {
      console.error('Enrollment error:', enrollError)
      enrollmentMessage.value = 'Failed to enroll student. Please try again.'
      enrollmentMessageType.value = 'error'
      return
    }

    // Check the result from the function
    const result = data[0]
    
    if (result.success) {
      enrollmentMessage.value = `Successfully enrolled ${existingStudent.full_name} (ID: ${existingStudent.student_id})`
      enrollmentMessageType.value = 'success'
      enrollStudentId.value = ''

      // Clear message after 3 seconds
      setTimeout(() => {
        enrollmentMessage.value = ''
      }, 3000)

      // Refresh the available students list if there's a search query
      if (studentSearchQuery.value.trim()) {
        await searchStudents()
      }
      
      // Refresh the main subjects data to update student counts
      await fetchSubjects()
    } else {
      enrollmentMessage.value = result.message
      enrollmentMessageType.value = 'error'
    }

  } catch (error) {
    console.error('Error enrolling student:', error)
    enrollmentMessage.value = 'Failed to enroll student. Please try again.'
    enrollmentMessageType.value = 'error'
  } finally {
    isEnrollingStudent.value = false
  }
}

const searchStudents = async () => {
  try {
    isSearchingStudents.value = true
    
    // Wait for auth to be ready
    if (!isAuthReady.value || !teacherInfo.value?.id) {
      await waitForAuth()
    }

    // Build query for teacher_available_students view
    let query = supabase
      .from('teacher_available_students')
      .select('*')
      .eq('teacher_id', teacherInfo.value.id)
      .eq('subject_id', selectedSubjectForStudents.value.id)
      .eq('section_id', selectedSectionForStudents.value.id)
      .eq('already_enrolled_in_subject', false)
      .eq('is_active', true)

    // Add search filters
    if (studentSearchQuery.value.trim()) {
      const searchTerm = studentSearchQuery.value.trim()
      query = query.or(`student_name.ilike.%${searchTerm}%,student_number.ilike.%${searchTerm}%,student_email.ilike.%${searchTerm}%`)
    }

    if (gradeFilter.value) {
      query = query.eq('grade_level', parseInt(gradeFilter.value))
    }

    const { data, error } = await query.order('student_name')

    if (error) {
      console.error('Search students error:', error)
      showToast('Failed to search students', 'error')
      return
    }

    availableStudents.value = data || []

  } catch (error) {
    console.error('Search students error:', error)
    showToast('Failed to search students', 'error')
    availableStudents.value = []
  } finally {
    isSearchingStudents.value = false
  }
}

const toggleStudentSelection = (studentId) => {
  const index = selectedStudentsToAdd.value.indexOf(studentId)
  if (index > -1) {
    selectedStudentsToAdd.value.splice(index, 1)
  } else {
    selectedStudentsToAdd.value.push(studentId)
  }
}

const clearSelection = () => {
  selectedStudentsToAdd.value = []
}

const addSelectedStudents = async () => {
  if (selectedStudentsToAdd.value.length === 0) return

  try {
    isAddingStudents.value = true

    // Wait for auth to be ready
    if (!isAuthReady.value || !teacherInfo.value?.id) {
      await waitForAuth()
    }

    // Use the teacher_bulk_add_students function from the database
    const { data, error } = await supabase.rpc('teacher_bulk_add_students', {
      p_teacher_id: teacherInfo.value.id,
      p_section_id: selectedSectionForStudents.value.id,
      p_student_ids: selectedStudentsToAdd.value
    })

    if (error) {
      console.error('Bulk add students error:', error)
      showToast('Failed to add students', 'error')
      return
    }

    const result = data[0] // RPC returns array with single result
    
    if (result.successful > 0) {
      showToast(`Successfully added ${result.successful} student${result.successful > 1 ? 's' : ''} to the section`, 'success')
      
      // Clear selections and refresh the search
      selectedStudentsToAdd.value = []
      await searchStudents()
      
      // Refresh the main subjects data to update student counts
      await fetchSubjects()
    }

    if (result.failed > 0) {
      showToast(`${result.failed} student${result.failed > 1 ? 's' : ''} could not be added. Check the details for more information.`, 'info')
      console.log('Add students details:', result.details)
    }

  } catch (error) {
    console.error('Add students error:', error)
    showToast('Failed to add students', 'error')
  } finally {
    isAddingStudents.value = false
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

// ============================================================
// SECTION EDITING FUNCTIONALITY
// ============================================================
const showEditSectionModal = ref(false)
const editingSectionData = ref({
  id: null,
  name: '',
  max_students: '',
  section_code: ''
})

const editSection = (section) => {
  editingSectionData.value = {
    id: section.id,
    name: section.section_name || section.name,
    max_students: section.max_students,
    section_code: section.section_code
  }
  showEditSectionModal.value = true
  openMenuId.value = null
}

const saveEditedSection = async () => {
  try {
    if (!editingSectionData.value.name?.trim()) {
      showToast('Section name is required', 'error')
      return
    }

    if (!editingSectionData.value.max_students || editingSectionData.value.max_students < 1) {
      showToast('Max students must be at least 1', 'error')
      return
    }

    isLoading.value = true

    const updateData = {
      name: editingSectionData.value.name.trim(),
      max_students: parseInt(editingSectionData.value.max_students)
    }

    const { error } = await supabase
      .from('sections')
      .update(updateData)
      .eq('id', editingSectionData.value.id)

    if (error) throw error

    // Update local data immediately for better UX
    if (selectedSubject.value && selectedSubject.value.sections) {
      const sectionIndex = selectedSubject.value.sections.findIndex(s => s.id === editingSectionData.value.id)
      if (sectionIndex !== -1) {
        selectedSubject.value.sections[sectionIndex] = {
          ...selectedSubject.value.sections[sectionIndex],
          name: updateData.name,
          section_name: updateData.name,
          max_students: updateData.max_students
        }

        // Update in main subjects array as well
        const subjectIndex = subjects.value.findIndex(s => s.id === selectedSubject.value.id)
        if (subjectIndex !== -1) {
          subjects.value[subjectIndex].sections = [...selectedSubject.value.sections]
        }
      }
    }

    showEditSectionModal.value = false
    showToast('Section updated successfully!', 'success')

  } catch (error) {
    console.error('Error updating section:', error)
    showToast('Error updating section. Please try again.', 'error')
  } finally {
    isLoading.value = false
  }
}

const closeEditSectionModal = () => {
  showEditSectionModal.value = false
  editingSectionData.value = {
    id: null,
    name: '',
    max_students: '',
    section_code: ''
  }
}

// ============================================================
// CLICK OUTSIDE HANDLER
// ============================================================
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
      .eq('enrollment_status', 'active')

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
          enrollment_date: enrollment.enrolled_at,
          enrollment_method: enrollment.enrollment_method || 'teacher_added',
          added_by: enrollment.added_by || 'Teacher',
          enrollment_id: enrollment.enrollment_id
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
      csvContent += `Student ID,Full Name,Email,Grade,Enrollment Date,Enrollment Method,Added By\n`
      
      sectionData.students.forEach(student => {
        const enrollMethod = student.enrollment_method === 'teacher_added' ? 'Teacher Added' : 'Self-Enrolled'
        csvContent += `"${student.student_id}","${student.full_name}","${student.email}","${student.grade_level}","${formatEnrollmentDate(student.enrollment_date)}","${enrollMethod}","${student.added_by || 'N/A'}"\n`
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
// REMOVE STUDENT FROM SECTION
// ============================================================
const removeStudentFromSection = async (enrollmentId, studentName) => {
  if (!confirm(`Are you sure you want to remove ${studentName} from this section?`)) {
    return
  }

  try {
    // Wait for auth to be ready
    if (!isAuthReady.value || !teacherInfo.value?.id) {
      await waitForAuth()
    }

    // Use the teacher_remove_student_from_section database function
    const { data, error } = await supabase.rpc('teacher_remove_student_from_section', {
      p_teacher_id: teacherInfo.value.id,
      p_enrollment_id: enrollmentId,
      p_reason: 'Removed by teacher'
    })

    if (error) {
      console.error('Remove student error:', error)
      showToast('Failed to remove student', 'error')
      return
    }

    // Check the result from the function
    const result = data[0]
    
    if (result.success) {
      showToast(`Successfully removed ${studentName} from the section`, 'success')
      
      // Refresh the roster modal
      if (currentStudentRoster.value?.subject) {
        await viewStudentRoster(currentStudentRoster.value.subject)
      }
      
      // Refresh the main subjects data to update student counts
      await fetchSubjects()
    } else {
      showToast(result.message, 'error')
    }

  } catch (error) {
    console.error('Error removing student:', error)
    showToast('Failed to remove student. Please try again.', 'error')
  }
}

// ============================================================
// LIFECYCLE - ENHANCED WITH BETTER AUTH HANDLING
// ============================================================
onMounted(async () => {
  try {
    console.log('🚀 Component mounting...')
    
    // Initialize dark mode immediately
    initDarkMode()
    
    // Initialize auth
    const { initializeAuth, setupAuthListener } = useTeacherAuth()
    setupAuthListener()
    
    // Set up click handler
    document.addEventListener('click', handleClickOutside)
    
    console.log('🔐 Starting authentication...')
    
    // Initialize auth
    const authResult = await initializeAuth()
    
    if (!authResult.success) {
      if (authResult.needsLogin || authResult.wrongRole) {
        console.warn('⚠️ Authentication failed, redirecting to login')
        await router.push('/login')
        return
      }
    }
    
    console.log('✅ Auth initialization complete')
    
    // Wait for teacherInfo to be fully loaded with retry logic
    try {
      await waitForAuth(30, 200) // Wait up to 6 seconds
      
      // Load teacher name
      try {
        const { data: teacher, error } = await supabase
          .from('teachers')
          .select('full_name')
          .eq('id', teacherInfo.value.id)
          .single()
          
        if (!error && teacher) {
          fullName.value = teacher.full_name || 'Teacher'
          console.log('✅ Teacher loaded:', { id: teacherInfo.value.id, name: fullName.value })
        }
      } catch (err) {
        console.warn('⚠️ Failed to load teacher name:', err)
        // Continue anyway - name is not critical
      }
      
      // Fetch subjects only after auth is confirmed ready
      console.log('📚 Fetching subjects...')
      await fetchSubjects()
      
    } catch (authError) {
      console.error('❌ Auth timeout:', authError)
      
      // Show user-friendly error
      showToast('Authentication is taking longer than expected. Please reload the page.', 'error')
      
      // Still try to fetch if we have any auth info
      if (teacherInfo.value?.id) {
        console.log('⚠️ Attempting to fetch with partial auth...')
        await fetchSubjects()
      } else {
        // Redirect to login after delay
        setTimeout(() => {
          router.push('/login')
        }, 3000)
      }
    }
    
  } catch (error) {
    console.error('❌ Component mount error:', error)
    showToast('Failed to initialize page. Please reload.', 'error')
    
    // Try to continue if we have auth
    if (teacherInfo.value?.id) {
      console.log('⚠️ Attempting recovery...')
      isAuthReady.value = true
      await fetchSubjects()
    }
  }
})

onUnmounted(() => {
  document.removeEventListener('click', handleClickOutside)
  console.log('🧹 Component unmounted')
})
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

/* ===============================================
   MODERN UI SYSTEM - ORGANIZED & USER-FRIENDLY
   =============================================== */

/* Reset and Base */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.dashboard-container {
  min-height: 100vh;
  width: 100vw;
  background: #f8fafc;
  font-family: 'Inter', sans-serif;
  overflow-x: hidden;
}
.dark .dashboard-container {
  background: #0f172a;
}

/* Main Layout */
.main-content {
  flex: 1;
  margin-left: 80px;
  padding-top: 70px;
}

.content-wrapper {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
}

/* Search and Filter Bar */
.search-filter-bar {
  display: flex;
  gap: 1rem;
  margin-bottom: 2rem;
  align-items: center;
}

.search-input-container {
  position: relative;
  flex: 1;
}

.search-icon {
  position: absolute;
  left: 1rem;
  top: 50%;
  transform: translateY(-50%);
  color: #6b7280;
}

.search-input {
  width: 100%;
  padding: 0.75rem 1rem 0.75rem 3rem;
  border: 1px solid #e5e7eb;
  border-radius: 12px;
  font-size: 1rem;
  background: white;
  transition: all 0.2s ease;
}
.search-input:focus {
  outline: none;
  border-color: #3b82f6;
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
}
.dark .search-input {
  background: #1e293b;
  border-color: #334155;
  color: #e2e8f0;
}

.grade-filter {
  padding: 0.75rem 1rem;
  border: 1px solid #e5e7eb;
  border-radius: 12px;
  background: white;
  min-width: 150px;
}
.dark .grade-filter {
  background: #1e293b;
  border-color: #334155;
  color: #e2e8f0;
}

/* Subject Cards Grid */
.subjects-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 1.5rem;
}

.subject-card {
  background: white;
  border: 1px solid #e5e7eb;
  border-radius: 16px;
  padding: 1.5rem;
  cursor: pointer;
  transition: all 0.2s ease;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
}
.subject-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
  border-color: #3b82f6;
}
.dark .subject-card {
  background: #1e293b;
  border-color: #334155;
}
.dark .subject-card:hover {
  border-color: #3b82f6;
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3);
}

.subject-card-header {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  margin-bottom: 1rem;
}

.subject-icon {
  width: 60px;
  height: 60px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 1.5rem;
  color: white;
  flex-shrink: 0;
}

.subject-initial {
  font-size: 1.5rem;
  font-weight: 700;
}

.subject-card-body {
  margin-top: 1rem;
}

.subject-title {
  font-size: 1.25rem;
  font-weight: 600;
  color: #1f2937;
  margin-bottom: 0.25rem;
}
.dark .subject-title {
  color: #f1f5f9;
}

.grade-level {
  font-size: 0.875rem;
  color: #6b7280;
  margin-bottom: 0.5rem;
}
.dark .grade-level {
  color: #94a3b8;
}

.subject-description {
  font-size: 0.875rem;
  color: #4b5563;
  line-height: 1.4;
  margin-bottom: 1rem;
}
.dark .subject-description {
  color: #cbd5e1;
}

.subject-description-placeholder {
  font-size: 0.875rem;
  color: #9ca3af;
  font-style: italic;
  margin-bottom: 1rem;
}

.subject-stats {
  display: flex;
  gap: 1rem;
  padding-top: 1rem;
  border-top: 1px solid #f3f4f6;
}
.dark .subject-stats {
  border-top-color: #374151;
}

.stat-item {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.stat-number {
  font-size: 1.5rem;
  font-weight: 700;
  color: #3b82f6;
}
.dark .stat-number {
  color: #60a5fa;
}

.stat-label {
  font-size: 0.75rem;
  color: #6b7280;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}
.dark .stat-label {
  color: #94a3b8;
}

/* Menu System */
.subject-menu-container {
  position: relative;
}

.subject-menu-btn {
  background: none;
  border: none;
  color: #6b7280;
  padding: 0.5rem;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.2s ease;
}
.subject-menu-btn:hover {
  background: #f3f4f6;
  color: #374151;
}
.dark .subject-menu-btn {
  color: #94a3b8;
}
.dark .subject-menu-btn:hover {
  background: #374151;
  color: #f1f5f9;
}

.subject-dropdown-menu {
  position: absolute;
  top: 100%;
  right: 0;
  background: white;
  border: 1px solid #e5e7eb;
  border-radius: 8px;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
  z-index: 1000;
  min-width: 140px;
  overflow: hidden;
}
.dark .subject-dropdown-menu {
  background: #1e293b;
  border-color: #334155;
}

.menu-item {
  background: none;
  border: none;
  width: 100%;
  padding: 0.75rem 1rem;
  text-align: left;
  font-size: 0.875rem;
  color: #374151;
  cursor: pointer;
  transition: all 0.2s ease;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}
.menu-item:hover {
  background: #f3f4f6;
}
.menu-item.delete {
  color: #dc2626;
}
.menu-item.delete:hover {
  background: #fef2f2;
}
.dark .menu-item {
  color: #e2e8f0;
}
.dark .menu-item:hover {
  background: #334155;
}
.dark .menu-item.delete {
  color: #f87171;
}
.dark .menu-item.delete:hover {
  background: #7f1d1d;
}

/* Navigation Headers */
.view-header {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 2rem;
  padding-bottom: 1rem;
  border-bottom: 1px solid #e5e7eb;
}
.dark .view-header {
  border-bottom-color: #334155;
}

.back-btn {
  background: #10b981;
  border: none;
  padding: 0.875rem 1.5rem;
  border-radius: 10px;
  color: white;
  font-weight: 600;
  font-size: 1rem;
  cursor: pointer;
  transition: all 0.2s ease;
  display: flex;
  align-items: center;
  gap: 0.625rem;
  box-shadow: 0 2px 8px rgba(16, 185, 129, 0.2);
}
.back-btn:hover {
  background: #059669;
  transform: translateX(-2px);
  box-shadow: 0 4px 12px rgba(16, 185, 129, 0.3);
}
.dark .back-btn {
  background: #10b981;
  color: white;
}
.dark .back-btn:hover {
  background: #059669;
}

.view-title h2 {
  font-size: 1.875rem;
  font-weight: 700;
  color: #1f2937;
  margin-bottom: 0.25rem;
}
.dark .view-title h2 {
  color: #f1f5f9;
}

.view-title p {
  color: #6b7280;
  font-size: 1rem;
}
.dark .view-title p {
  color: #94a3b8;
}

/* Sections Grid */
.sections-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
  gap: 1.5rem;
}

.section-card {
  background: white;
  border: 1px solid #e5e7eb;
  border-radius: 16px;
  padding: 1.5rem;
  cursor: pointer;
  transition: all 0.2s ease;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
}
.section-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
  border-color: #3b82f6;
}
.dark .section-card {
  background: #1e293b;
  border-color: #334155;
}

.section-card-header {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  margin-bottom: 1rem;
}

.section-info h3 {
  font-size: 1.25rem;
  font-weight: 600;
  color: #1f2937;
  margin-bottom: 0.25rem;
}
.dark .section-info h3 {
  color: #f1f5f9;
}

.section-subtitle {
  color: #6b7280;
  font-size: 0.875rem;
}
.dark .section-subtitle {
  color: #94a3b8;
}

.enrollment-status {
  margin-bottom: 1rem;
}

.student-count {
  text-align: center;
  margin-bottom: 1rem;
}

.count-number {
  font-size: 2rem;
  font-weight: 700;
  color: #3b82f6;
  display: block;
}
.dark .count-number {
  color: #60a5fa;
}

.count-label {
  font-size: 0.875rem;
  color: #6b7280;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}
.dark .count-label {
  color: #94a3b8;
}

.capacity-info {
  margin-top: 0.75rem;
}

.capacity-bar {
  width: 100%;
  height: 6px;
  background: #e5e7eb;
  border-radius: 3px;
  overflow: hidden;
  margin-bottom: 0.5rem;
}
.dark .capacity-bar {
  background: #374151;
}

.capacity-fill {
  height: 100%;
  background: linear-gradient(90deg, #3b82f6, #1d4ed8);
  border-radius: 3px;
  transition: width 0.3s ease;
}

.capacity-text {
  font-size: 0.75rem;
  color: #6b7280;
  text-align: center;
  display: block;
}
.dark .capacity-text {
  color: #94a3b8;
}

.section-actions {
  padding-top: 1rem;
  border-top: 1px solid #f3f4f6;
}
.dark .section-actions {
  border-top-color: #374151;
}

.action-btn {
  background: #3b82f6;
  color: white;
  border: none;
  padding: 0.75rem 1rem;
  border-radius: 8px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s ease;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  width: 100%;
  justify-content: center;
}
.action-btn:hover {
  background: #2563eb;
  transform: translateY(-1px);
}
.action-btn.secondary {
  background: #6b7280;
}
.action-btn.secondary:hover {
  background: #4b5563;
}

/* Assessment Management Styles */
.assessment-type-buttons {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
  margin-bottom: 1rem;
}

.assessment-type-btn {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 1rem;
  border: 2px solid var(--color-border, #e5e7eb);
  border-radius: 8px;
  background: var(--color-background-soft, #f8fafc);
  color: var(--color-text, #374151);
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s ease;
  text-align: left;
  min-height: 60px;
  width: 100%;
}

.dark .assessment-type-btn {
  background: #1f2937;
  border-color: #374151;
  color: #e5e7eb;
}

.assessment-type-btn:hover {
  border-color: var(--color-border-hover, #d1d5db);
  background: var(--color-background-mute, #f1f5f9);
  transform: translateY(-1px);
}

.dark .assessment-type-btn:hover {
  background: #111827;
  border-color: #4b5563;
}

.assessment-type-btn svg {
  flex-shrink: 0;
  width: 20px;
  height: 20px;
}

.assessment-type-btn .btn-subtitle {
  display: block;
  font-size: 0.75rem;
  color: var(--color-text-secondary, #6b7280);
  font-weight: 400;
  margin-top: 0.25rem;
}

.dark .assessment-type-btn .btn-subtitle {
  color: #9ca3af;
}

.quiz-btn:hover {
  border-color: #667eea;
  background: rgba(102, 126, 234, 0.1);
}

.assignment-btn:hover {
  border-color: #f093fb;
  background: rgba(240, 147, 251, 0.1);
}

.view-assessments-section {
  border-top: 1px solid var(--color-border, #e5e7eb);
  padding-top: 1rem;
}

.dark .view-assessments-section {
  border-top-color: #374151;
}

.action-btn.full-width {
  width: 100%;
  justify-content: center;
}

/* Section Detail View */
.section-overview-card {
  background: white;
  border: 1px solid #e5e7eb;
  border-radius: 12px;
  padding: 1.25rem;
  margin-bottom: 1.25rem;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
}
.dark .section-overview-card {
  background: #1e293b;
  border-color: #334155;
}

.overview-stats {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
  gap: 1.25rem;
}

.stat-box {
  text-align: center;
}

.stat-box .stat-number {
  font-size: 2rem;
  font-weight: 800;
  color: #3b82f6;
  display: block;
  margin-bottom: 0.4rem;
}
.dark .stat-box .stat-number {
  color: #60a5fa;
}

.stat-box .stat-label {
  font-size: 0.8rem;
  color: #6b7280;
  font-weight: 500;
}
.dark .stat-box .stat-label {
  color: #94a3b8;
}

/* Quick Actions Section */
.quick-actions-section {
  margin-top: 2rem;
}

.section-heading {
  font-size: 1.5rem;
  font-weight: 700;
  color: #1f2937;
  margin-bottom: 1.5rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}
.dark .section-heading {
  color: #f1f5f9;
}

.section-heading:before {
  content: '';
  width: 4px;
  height: 24px;
  background: #3b82f6;
  border-radius: 2px;
}

/* Action Cards */
.action-cards-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 1.5rem;
  margin-bottom: 2rem;
}

.action-card {
  background: white;
  border: 2px solid #f1f5f9;
  border-radius: 20px;
  padding: 2rem;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
}
.action-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 30px rgba(0, 0, 0, 0.15);
  border-color: #3b82f6;
}
.dark .action-card {
  background: #1e293b;
  border-color: #334155;
}
.dark .action-card:hover {
  border-color: #3b82f6;
  box-shadow: 0 12px 30px rgba(0, 0, 0, 0.3);
}

/* Card Type Styling */
.action-card.student-management {
  border-left: 4px solid #10b981;
}
.action-card.assessment-management {
  border-left: 4px solid #667eea;
}
.action-card.grade-management {
  border-left: 4px solid #f59e0b;
}

.card-header {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 1rem;
}

.card-icon {
  width: 48px;
  height: 48px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.card-icon.student-icon {
  background: linear-gradient(135deg, #10b981, #059669);
  color: white;
}

.card-icon.assessment-icon {
  background: linear-gradient(135deg, #667eea, #764ba2);
  color: white;
}

.card-icon.grade-icon {
  background: linear-gradient(135deg, #f59e0b, #d97706);
  color: white;
}

.card-header h3 {
  font-size: 1.25rem;
  font-weight: 700;
  color: #1f2937;
  margin: 0;
}
.dark .card-header h3 {
  color: #f1f5f9;
}

.card-description {
  color: #6b7280;
  font-size: 0.875rem;
  line-height: 1.6;
  margin-bottom: 1.5rem;
}
.dark .card-description {
  color: #94a3b8;
}

.card-actions {
  display: flex;
  gap: 0.75rem;
  flex-wrap: wrap;
}

.action-btn.primary {
  background: #3b82f6;
  color: white;
}
.action-btn.primary:hover {
  background: #2563eb;
}

/* Empty States */
.empty-state {
  text-align: center;
  padding: 4rem 2rem;
  color: #6b7280;
}
.dark .empty-state {
  color: #94a3b8;
}

.empty-icon {
  margin: 0 auto 1.5rem;
  color: #d1d5db;
}
.dark .empty-icon {
  color: #4b5563;
}

.empty-title {
  font-size: 1.25rem;
  font-weight: 600;
  color: #374151;
  margin-bottom: 0.5rem;
}
.dark .empty-title {
  color: #e5e7eb;
}

.empty-desc {
  margin-bottom: 2rem;
}

.create-quiz-btn {
  background: #3b82f6;
  color: white;
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 8px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s ease;
}
.create-quiz-btn:hover {
  background: #2563eb;
  transform: translateY(-1px);
}

/* Navigation Sidebar */
.sidebar {
  position: fixed;
  top: 64px;
  left: 0;
  width: 80px;
  height: calc(100vh - 64px);
  background: #3D8D7A;
  border-right: none;
  z-index: 900;
  box-shadow: 2px 0 10px rgba(0, 0, 0, 0.05);
  overflow: visible;
}

/* Top Navigation Bar */
.top-navbar {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  height: 64px;
  background: #3D8D7A;
  z-index: 1000;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.navbar-content {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 100%;
  padding: 0 2rem;
}

.brand-logo {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.logo-img {
  height: 36px;
  width: auto;
}

.brand-name {
  color: white;
  font-size: 1.25rem;
  font-weight: 700;
}

.navbar-right {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.nav-icon-btn {
  background: rgba(255, 255, 255, 0.1);
  border: none;
  color: white;
  padding: 0.5rem;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.2s ease;
}
.nav-icon-btn:hover {
  background: rgba(255, 255, 255, 0.2);
}

.user-profile {
  background: rgba(255, 255, 255, 0.1);
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 8px;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  transition: all 0.2s ease;
}
.user-profile:hover {
  background: rgba(255, 255, 255, 0.2);
}

/* Page Header */
.page-header {
  background: white;
  border-bottom: 1px solid #e5e7eb;
  margin-bottom: 2rem;
  padding: 2rem;
  border-radius: 16px 16px 0 0;
}
.dark .page-header {
  background: #1e293b;
  border-color: #334155;
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

.header-icon {
  color: #3b82f6;
}

.header-title {
  font-size: 2rem;
  font-weight: 700;
  color: #1f2937;
  margin-bottom: 0.25rem;
}
.dark .header-title {
  color: #f1f5f9;
}

.header-subtitle {
  color: #6b7280;
  font-size: 1rem;
}
.dark .header-subtitle {
  color: #94a3b8;
}

.create-subject-btn {
  background: #3b82f6;
  color: white;
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 8px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s ease;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}
.create-subject-btn:hover {
  background: #2563eb;
  transform: translateY(-1px);
}

/* Modals */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  z-index: 2000;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 2rem;
}

.modal-content-enhanced {
  background: white;
  border-radius: 16px;
  max-width: 650px;
  width: 100%;
  max-height: 95vh;
  display: flex;
  flex-direction: column;
  box-shadow: 0 25px 50px rgba(0, 0, 0, 0.25);
}
.dark .modal-content-enhanced {
  background: #1e293b;
}

.modal-header-enhanced {
  padding: 1.25rem 1.5rem 0.875rem;
  border-bottom: 1px solid #e5e7eb;
  display: flex;
  align-items: flex-start;
  gap: 1rem;
  flex-shrink: 0;
}
.dark .modal-header-enhanced {
  border-color: #334155;
}

.modal-icon {
  color: #3b82f6;
  flex-shrink: 0;
  width: 40px;
  height: 40px;
}

.modal-title-area h2 {
  font-size: 1.25rem;
  font-weight: 700;
  color: #1f2937;
  margin-bottom: 0.125rem;
}
.dark .modal-title-area h2 {
  color: #f1f5f9;
}

.modal-subtitle {
  color: #6b7280;
  font-size: 0.8125rem;
}
.dark .modal-subtitle {
  color: #94a3b8;
}

.close-btn-enhanced {
  background: linear-gradient(135deg, #10b981, #059669);
  border: none;
  color: white;
  padding: 0.75rem;
  border-radius: 10px;
  cursor: pointer;
  margin-left: auto;
  transition: all 0.2s ease;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 2px 8px rgba(16, 185, 129, 0.3);
}
.close-btn-enhanced:hover {
  background: linear-gradient(135deg, #059669, #047857);
  transform: scale(1.05);
  box-shadow: 0 4px 12px rgba(16, 185, 129, 0.4);
}
.dark .close-btn-enhanced {
  background: linear-gradient(135deg, #10b981, #059669);
  color: white;
}
.dark .close-btn-enhanced:hover {
  background: linear-gradient(135deg, #059669, #047857);
}

/* Scroll to Top Button */
.scroll-to-top {
  position: fixed;
  bottom: 2rem;
  right: 2rem;
  background: #3b82f6;
  color: white;
  border: none;
  width: 48px;
  height: 48px;
  border-radius: 50%;
  cursor: pointer;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  z-index: 1000;
  transition: all 0.2s ease;
}
.scroll-to-top:hover {
  background: #2563eb;
  transform: translateY(-2px);
}

/* Student Management Modal */
.add-students-content {
  padding: 2rem;
  max-height: 70vh;
  overflow-y: auto;
}

.student-search-section {
  margin-bottom: 2rem;
  padding-bottom: 2rem;
  border-bottom: 1px solid #e5e7eb;
}
.dark .student-search-section {
  border-bottom-color: #334155;
}

.search-header .section-title {
  font-size: 1.125rem;
  font-weight: 600;
  color: #1f2937;
  margin: 0 0 0.5rem 0;
}
.dark .search-header .section-title {
  color: #f1f5f9;
}

.search-description {
  color: #6b7280;
  font-size: 0.875rem;
  margin: 0 0 1.5rem 0;
}
.dark .search-description {
  color: #94a3b8;
}

.search-filters-enhanced {
  display: flex;
  gap: 1rem;
  margin-bottom: 1rem;
}

.search-input-wrapper {
  position: relative;
  flex: 1;
}

.search-input-wrapper .search-icon {
  position: absolute;
  left: 1rem;
  top: 50%;
  transform: translateY(-50%);
  color: #6b7280;
}
.dark .search-input-wrapper .search-icon {
  color: #94a3b8;
}

.student-search-input-enhanced {
  width: 100%;
  padding: 0.75rem 1rem 0.75rem 3rem;
  border: 2px solid #e5e7eb;
  border-radius: 12px;
  font-size: 1rem;
  background: white;
  transition: all 0.2s ease;
}
.student-search-input-enhanced:focus {
  outline: none;
  border-color: #3b82f6;
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
}
.dark .student-search-input-enhanced {
  background: #1e293b;
  border-color: #334155;
  color: #e2e8f0;
}

.grade-filter-select-enhanced {
  padding: 0.75rem 1rem;
  border: 2px solid #e5e7eb;
  border-radius: 12px;
  background: white;
  min-width: 150px;
  font-size: 1rem;
}
.dark .grade-filter-select-enhanced {
  background: #1e293b;
  border-color: #334155;
  color: #e2e8f0;
}

.search-hint {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  color: #6b7280;
  font-size: 0.875rem;
  padding: 1rem;
  background: #f9fafb;
  border-radius: 8px;
}
.dark .search-hint {
  background: #374151;
  color: #94a3b8;
}

.students-list-section {
  margin-top: 1rem;
}

.students-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 1rem;
}

.students-header h4 {
  font-size: 1rem;
  font-weight: 600;
  color: #1f2937;
  margin: 0;
}
.dark .students-header h4 {
  color: #f1f5f9;
}

.batch-actions {
  display: flex;
  gap: 0.5rem;
}

.add-batch-btn {
  background: #3b82f6;
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 8px;
  font-size: 0.875rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s ease;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}
.add-batch-btn:hover:not(:disabled) {
  background: #2563eb;
}
.add-batch-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.clear-selection-btn {
  background: #f3f4f6;
  color: #6b7280;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 8px;
  font-size: 0.875rem;
  cursor: pointer;
  transition: all 0.2s ease;
}
.clear-selection-btn:hover {
  background: #e5e7eb;
}

.loading-state {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 1rem;
  padding: 2rem;
  color: #6b7280;
}

.empty-search {
  text-align: center;
  padding: 2rem;
  color: #6b7280;
}
.dark .empty-search {
  color: #94a3b8;
}

.empty-search svg {
  color: #d1d5db;
  margin-bottom: 1rem;
}
.dark .empty-search svg {
  color: #4b5563;
}

.empty-subtitle {
  font-size: 0.875rem;
  margin-top: 0.5rem;
  opacity: 0.7;
  line-height: 1.4;
}

.students-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 1rem;
  max-height: 400px;
  overflow-y: auto;
  padding: 0.5rem;
}

.spinner-icon {
  animation: spin 1s linear infinite;
}

/* Responsive Design */
@media (max-width: 768px) {
  .subjects-grid {
    grid-template-columns: 1fr;
  }
  
  .sections-grid {
    grid-template-columns: 1fr;
  }
  
  .action-cards-grid {
    grid-template-columns: 1fr;
  }
  
  .search-filter-bar {
    flex-direction: column;
    align-items: stretch;
  }
  
  .search-filters-enhanced {
    flex-direction: column;
  }
  
  .students-grid {
    grid-template-columns: 1fr;
  }
}

.sidebar-nav {
  padding: 2rem 0.5rem 1rem 0.5rem;
}

.sidebar-item {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 56px;
  width: 56px;
  margin: 8px 0;
  border-radius: 12px;
  transition: background 0.2s, box-shadow 0.2s;
  cursor: pointer;
  position: relative;
}

.sidebar-item.active {
  background: rgba(255,255,255,0.15);
  border: 2px solid #fff;
}

.sidebar-item:hover {
  background: rgba(255,255,255,0.22);
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
}

.sidebar-icon svg {
  display: block;
}

.sidebar-tooltip {
  position: absolute;
  left: 60px;
  top: 50%;
  transform: translateY(-50%);
  background: #fff;
  color: #3D8D7A;
  padding: 4px 12px;
  border-radius: 6px;
  font-size: 14px;
  font-family: 'Inter', sans-serif;
  white-space: nowrap;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.2s;
  z-index: 10;
}

.sidebar-item:hover .sidebar-tooltip {
  opacity: 1;
  pointer-events: auto;
}.top-navbar {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  height: 64px;
  background: linear-gradient(135deg, #3D8D7A, #2d6a5a);
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  z-index: 1000;
  box-shadow: 0 4px 20px rgba(61, 141, 122, 0.3);
}

.navbar-content {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 100%;
  max-width: 1400px;
  margin: 0 auto;
  padding: 0 1.5rem;
}

.navbar-left {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.brand-logo {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  color: white;
  font-weight: 700;
  text-decoration: none;
}

.logo-img {
  width: 36px;
  height: 36px;
  object-fit: contain;
  filter: brightness(0) invert(1);
}

.brand-name {
  font-size: 1.4rem;
  font-weight: 800;
  color: white;
  letter-spacing: -0.5px;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
}

.navbar-center {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  flex: 1;
  justify-content: center;
  max-width: 600px;
}

.navbar-right {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.nav-icon-btn {
  width: 44px;
  height: 44px;
  background: rgba(255, 255, 255, 0.15);
  border: none;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.2s ease;
  color: rgba(255, 255, 255, 0.9);
  position: relative;
}

.nav-icon-btn:hover {
  background: rgba(255, 255, 255, 0.25);
  color: white;
}

.user-profile-wrapper {
  position: relative;
}

.user-profile {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.5rem 0.75rem;
  border-radius: 12px;
  transition: background 0.2s;
  cursor: pointer;
}

.user-profile:hover {
  background: rgba(255, 255, 255, 0.1);
}

.user-avatar {
  width: 36px;
  height: 36px;
  background: rgba(255, 255, 255, 0.2);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
}

.user-name {
  font-size: 0.9rem;
  font-weight: 600;
  color: white;
}

.dropdown-arrow {
  color: rgba(255, 255, 255, 0.8);
  transition: transform 0.2s;
}

.user-profile:hover .dropdown-arrow {
  transform: rotate(180deg);
}

/* Rounded semi-transparent backgrounds for sidebar and navbar icons/buttons */
.rounded-bg {
  background: rgba(255,255,255,0.13);
  border-radius: 16px;
  transition: background 0.2s;
}
.rounded-bg:hover {
  background: rgba(255,255,255,0.22);
}

/* Notification dropdown styles */
.notif-wrapper {
  position: relative;
}

.notification-badge {
  position: absolute;
  top: -2px;
  right: -2px;
  background: #ef4444;
  color: white;
  border-radius: 50%;
  width: 18px;
  height: 18px;
  font-size: 0.75rem;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 2px solid #3D8D7A;
}

.notification-dropdown {
  position: absolute;
  top: 55px;
  right: 0;
  width: 360px;
  max-height: 480px;
  background: white;
  border-radius: 16px;
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15);
  overflow: hidden;
  z-index: 1001;
  border: 1px solid #e2e8f0;
}

.dropdown-header {
  padding: 1.25rem 1.5rem;
  border-bottom: 1px solid #e2e8f0;
  background: #fafafa;
}

.dropdown-header h3 {
  font-size: 1.1rem;
  font-weight: 600;
  color: #1e293b;
}

.notification-list {
  max-height: 400px;
  overflow-y: auto;
}

.no-notifications {
  padding: 3rem 1.5rem;
  text-align: center;
  color: #94a3b8;
  font-size: 0.9rem;
}

.notification-item {
  padding: 1rem 1.5rem;
  border-bottom: 1px solid #f1f5f9;
  transition: background 0.2s;
  cursor: pointer;
}

.notification-item:hover {
  background: #f8fafc;
}

.notification-item:last-child {
  border-bottom: none;
}

.notif-content h4 {
  font-size: 0.9rem;
  font-weight: 600;
  color: #1e293b;
  margin-bottom: 0.25rem;
}

.notif-content p {
  font-size: 0.8rem;
  color: #64748b;
  margin-bottom: 0.5rem;
}

.notif-time {
  font-size: 0.75rem;
  color: #94a3b8;
}

.profile-dropdown {
  position: absolute;
  top: 55px;
  right: 0;
  width: 280px;
  background: white;
  border-radius: 16px;
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15);
  overflow: hidden;
  z-index: 1001;
  border: 1px solid #e2e8f0;
}

.profile-dropdown .dropdown-header {
  padding: 1.5rem;
  background: linear-gradient(135deg, #3D8D7A, #2d6a5a);
  color: white;
}

.profile-info {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.profile-avatar {
  width: 48px;
  height: 48px;
  background: rgba(255, 255, 255, 0.2);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
}

.profile-details h4 {
  font-size: 1rem;
  font-weight: 600;
  margin-bottom: 0.25rem;
}

.profile-details p {
  font-size: 0.85rem;
  opacity: 0.9;
}

.dropdown-menu {
  padding: 0.5rem;
}

.dropdown-item {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.75rem 1rem;
  border-radius: 8px;
  text-decoration: none;
  color: #1e293b;
  font-size: 0.9rem;
  font-weight: 500;
  transition: all 0.2s;
  cursor: pointer;
  border: none;
  background: none;
  width: 100%;
}

.dropdown-item:hover {
  background: #f1f5f9;
  color: #3D8D7A;
}

.dropdown-item svg {
  color: #64748b;
  transition: color 0.2s;
}

.dropdown-item:hover svg {
  color: #3D8D7A;
}

.dropdown-divider {
  height: 1px;
  background: #e2e8f0;
  margin: 0.5rem 0;
}

.logout-btn {
  color: #ef4444 !important;
}

.logout-btn:hover {
  background: #fef2f2 !important;
  color: #dc2626 !important;
}

.logout-btn svg {
  color: #ef4444 !important;
}

.logout-btn:hover svg {
  color: #dc2626 !important;
}


/* Scroll to Top Button */
.scroll-to-top {
  position: fixed;
  bottom: 2rem;
  right: 2rem;
  width: 48px;
  height: 48px;
  background: #3D8D7A;
  color: white;
  border: none;
  border-radius: 50%;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 4px 12px rgba(61, 141, 122, 0.3);
  transition: all 0.2s ease;
  z-index: 1000;
}

.scroll-to-top:hover {
  background: #2d6a5a;
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(61, 141, 122, 0.4);
}

/* Main Content */
.main-content {
  margin-top: 64px;
  margin-left: 80px;
  padding: 1.5rem;
  width: calc(100% - 80px);
  height: calc(100vh - 64px);
  min-height: calc(100vh - 64px);
  position: relative;
  overflow-y: auto;
  overflow-x: hidden;
  scroll-behavior: smooth;
}

/* Custom scrollbar for main content */
.main-content::-webkit-scrollbar {
  width: 8px;
}

.main-content::-webkit-scrollbar-track {
  background: #f1f5f9;
  border-radius: 8px;
}

.main-content::-webkit-scrollbar-thumb {
  background: #3D8D7A;
  border-radius: 8px;
}

.main-content::-webkit-scrollbar-thumb:hover {
  background: #2d6a5a;
}

/* Page Header */
.page-header {
  background: white;
  border-radius: 16px;
  padding: 1.5rem 2rem;
  margin-bottom: 1.5rem;
  border: 1px solid #e2e8f0;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
}

.header-content {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 1rem;
}

.header-left {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.header-icon {
  width: 56px;
  height: 56px;
  background: linear-gradient(135deg, #3D8D7A, #2d6a5a);
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
}

.header-title {
  font-size: 1.75rem;
  font-weight: 700;
  color: #1e293b;
  margin-bottom: 0.25rem;
}

.header-subtitle {
  font-size: 0.95rem;
  color: #64748b;
}

.header-actions {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.create-subject-btn {
  display: flex;
  align-items: center;
  gap: 0.625rem;
  background: linear-gradient(135deg, #3D8D7A, #2d6a5a);
  color: white;
  border: none;
  padding: 0.875rem 1.5rem;
  border-radius: 10px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
  box-shadow: 0 2px 8px rgba(61, 141, 122, 0.2);
}

.create-subject-btn:hover {
  background: linear-gradient(135deg, #2d6a5a, #1f4d3d);
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(61, 141, 122, 0.3);
}

.dark .create-subject-btn {
  background: linear-gradient(135deg, #20c997, #18a577);
  color: #ffffff;
}

.dark .create-subject-btn:hover {
  background: linear-gradient(135deg, #18a577, #059669);
}

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
  max-height: calc(100vh - 250px);
  overflow-y: auto;
  overflow-x: hidden;
  scroll-behavior: smooth;
}

/* Custom scrollbar for subjects grid */
.subjects-grid.enhanced::-webkit-scrollbar {
  width: 6px;
}

.subjects-grid.enhanced::-webkit-scrollbar-track {
  background: #f1f5f9;
  border-radius: 6px;
}

.subjects-grid.enhanced::-webkit-scrollbar-thumb {
  background: #3D8D7A;
  border-radius: 6px;
}

.subjects-grid.enhanced::-webkit-scrollbar-thumb:hover {
  background: #2d6a5a;
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
  border-radius: 14px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  flex-shrink: 0;
  transition: transform 0.2s ease;
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

/* Enhanced Subject Content Area */
.subject-content-enhanced {
  padding: 16px 20px;
  border-top: 1px solid #e5e7eb;
  background: rgba(249, 250, 251, 0.5);
  margin-top: auto;
  cursor: pointer;
  transition: all 0.2s ease;
}

.dark .subject-content-enhanced {
  border-top-color: #374151;
  background: rgba(31, 41, 55, 0.5);
}

.subject-content-enhanced:hover {
  background: rgba(249, 250, 251, 0.8);
}

.dark .subject-content-enhanced:hover {
  background: rgba(31, 41, 55, 0.8);
}

.subject-stats-row {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 24px;
}

.stat-item {
  text-align: center;
  flex: 1;
}

.stat-number {
  font-size: 1.5rem;
  font-weight: 700;
  color: #1f2937;
  line-height: 1.2;
  margin-bottom: 4px;
}

.dark .stat-number {
  color: #f3f4f6;
}

.stat-label {
  font-size: 0.875rem;
  color: #6b7280;
  font-weight: 500;
  text-transform: capitalize;
}

.dark .stat-label {
  color: #9ca3af;
}

.stat-divider {
  width: 1px;
  height: 32px;
  background: #e5e7eb;
  flex-shrink: 0;
}

.dark .stat-divider {
  background: #374151;
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
  background: #f3f4f6;
  border: none;
  color: #374151;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 0.625rem;
  font-size: 1rem;
  font-weight: 600;
  padding: 0.75rem 1.5rem;
  border-radius: 8px;
  transition: all 0.2s ease;
}
.dark .breadcrumb-btn {
  background: #374151;
  color: #d1d5db;
}

.breadcrumb-btn:hover {
  background: #10b981;
  color: white;
  transform: translateX(-2px);
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
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 1.25rem;
  margin-bottom: 2rem;
  padding: 1rem;
  width: 100%;
  box-sizing: border-box;
  overflow-x: hidden;
  scroll-behavior: smooth;
}

/* Custom scrollbar for sections grid */
.sections-grid::-webkit-scrollbar {
  width: 6px;
}

.sections-grid::-webkit-scrollbar-track {
  background: #f1f5f9;
  border-radius: 6px;
}

.sections-grid::-webkit-scrollbar-thumb {
  background: #3D8D7A;
  border-radius: 6px;
}

.sections-grid::-webkit-scrollbar-thumb:hover {
  background: #2d6a5a;
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
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.06);
  padding: 0;
  margin-bottom: 0;
  transition: all 0.3s ease;
  overflow: hidden;
  cursor: pointer;
  width: 100%;
  min-height: 140px;
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
  padding: 1rem 1.25rem 0.75rem 1.25rem;
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
  width: 40px;
  height: 40px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  transition: all 0.3s ease;
  flex-shrink: 0;
}

.section-title {
  font-size: 1.1rem;
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
  padding: 1rem 1.25rem;
  background: #fff;
}

.dark .section-card-body {
  background: #23272b;
}

.section-code-box {
  background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
  border: 2px solid #e2e8f0;
  border-radius: 10px;
  overflow: hidden;
  margin-bottom: 0.75rem;
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
  padding: 0.5rem 0.875rem;
  border-bottom: 1px solid #d1d5db;
}

.dark .code-box-header {
  background: #181c20 !important;
  border-bottom-color: #374151;
  color: #A3D1C6;
}

.code-label {
  font-size: 0.7rem;
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
  padding: 0.4rem 0.7rem;
  gap: 0.6rem;
}

.section-code-text {
  font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace;
  font-size: 0.9rem;
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
  font-size: 0.8rem;
  font-weight: 500;
  padding-top: 0.5rem;
  border-top: 1px solid #e5e7eb;
}

.dark .section-stats {
  color: #A3D1C6;
  border-color: #374151;
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
  gap: 1.25rem;
  margin-top: 1rem;
}

.section-info-card,
.quick-actions-card {
  background: #ffffff;
  border: 1px solid #e5e7eb;
  border-radius: 12px;
  padding: 1rem;
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
  gap: 0.875rem;
  margin-bottom: 1rem;
}

.section-icon {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 40px;
  height: 40px;
  border-radius: 10px;
  color: white;
}

.section-title-info .section-title {
  font-size: 1.1rem;
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
  gap: 0.5rem;
  margin-bottom: 1rem;
}

.detail-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.4rem 0;
  border-bottom: 1px solid #f3f4f6;
}

.dark .detail-item {
  border-bottom-color: #374151;
}

.detail-label {
  font-weight: 600;
  color: #1f2937;
  font-size: 0.8rem;
}

.dark .detail-label {
  color: #A3D1C6;
}

.detail-value {
  font-weight: 500;
  color: #6b7280;
  font-size: 0.8rem;
}

.dark .detail-value {
  color: #A3D1C6;
}

.section-code-container {
  background: #f8f9fa;
  border: 1px solid #e5e7eb;
  border-radius: 8px;
  padding: 0.875rem;
  display: flex;
  flex-direction: column;
  gap: 0.4rem;
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
  font-size: 1rem;
  font-weight: 700;
  color: #10b981;
  letter-spacing: 0.1em;
  margin-bottom: 0.4rem;
}

.dark .code-value {
  color: #20c997;
}

.copy-btn {
  align-self: flex-start;
  display: flex;
  align-items: center;
  gap: 0.4rem;
  padding: 0.4rem 0.7rem;
  background: #10b981;
  color: white;
  border: none;
  border-radius: 6px;
  font-size: 0.7rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
}

.copy-btn:hover {
  background: #059669;
  transform: translateY(-1px);
}

.actions-title {
  font-size: 1rem;
  font-weight: 700;
  color: #1f2937;
  margin: 0 0 1rem 0;
}

.dark .actions-title {
  color: #A3D1C6;
}

.actions-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0.875rem;
}

.action-button {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 0.625rem;
  padding: 1rem 0.875rem;
  border: none;
  border-radius: 10px;
  cursor: pointer;
  transition: all 0.2s ease;
  text-decoration: none;
  min-height: 95px;
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
  width: 28px;
  height: 28px;
  border-radius: 6px;
  background: rgba(16, 185, 129, 0.1);
  color: #10b981;
}

.dark .btn-icon {
  background: rgba(32, 201, 151, 0.1);
  color: #20c997;
}

.btn-text {
  font-size: 0.8rem;
  font-weight: 600;
  text-align: center;
}

@media (max-width: 1024px) {
  .section-detail-enhanced {
    grid-template-columns: 1fr;
    gap: 1rem;
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

/* Enhanced Loading Overlay - Matches MessagesPage */
.loading-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(251, 255, 228, 0.95);
  backdrop-filter: blur(8px);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 9999;
  animation: fadeIn 0.3s ease;
}

@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

.dark .loading-overlay {
  background: rgba(24, 28, 32, 0.95);
}

.loading-content {
  background: white;
  padding: 3rem 4rem;
  border-radius: 20px;
  text-align: center;
  box-shadow: 0 20px 60px rgba(61, 141, 122, 0.15);
  border: 2px solid #a3d1c6;
  animation: slideUp 0.4s ease;
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

.dark .loading-content {
  background: #23272b;
  border-color: #374151;
}

.loading-spinner-container {
  position: relative;
  width: 80px;
  height: 80px;
  margin: 0 auto 1.5rem;
}

.loading-spinner {
  width: 80px;
  height: 80px;
  border: 5px solid rgba(61, 141, 122, 0.1);
  border-left: 5px solid #3d8d7a;
  border-top: 5px solid #20c997;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin: 0 auto;
  box-shadow: 0 0 20px rgba(61, 141, 122, 0.1);
}

.loading-progress {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-size: 0.875rem;
  font-weight: 700;
  color: #3d8d7a;
}

.dark .loading-progress {
  color: #20c997;
}

.loading-steps {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  margin-top: 1rem;
  text-align: left;
}

.loading-steps .step {
  font-size: 0.875rem;
  color: #9ca3af;
  padding: 0.25rem 0;
  transition: all 0.3s ease;
}

.loading-steps .step.active {
  color: #3d8d7a;
  font-weight: 600;
  transform: translateX(4px);
}

.dark .loading-steps .step.active {
  color: #20c997;
}

@keyframes spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

.dark .loading-spinner {
  border: 5px solid rgba(32, 201, 151, 0.1);
  border-left: 5px solid #20c997;
  border-top: 5px solid #18a577;
  box-shadow: 0 0 20px rgba(32, 201, 151, 0.1);
}

.loading-text {
  font-size: 1.125rem;
  font-weight: 600;
  color: #1f2937;
  margin: 0;
  letter-spacing: 0.025em;
}

.dark .loading-text {
  color: #A3D1C6;
}

/* Delete Modal Styles */
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

.delete-item-card {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1.5rem;
  background: #f8fafc;
  border: 2px solid #e2e8f0;
  border-radius: 12px;
  margin-bottom: 1.5rem;
}

.dark .delete-item-card {
  background: #374151;
  border-color: #4b5563;
}

.item-icon {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 48px;
  height: 48px;
  background: linear-gradient(135deg, #f59e0b, #d97706);
  border-radius: 12px;
  color: white;
  flex-shrink: 0;
}

.item-details {
  flex: 1;
}

.item-name {
  font-size: 1.125rem;
  font-weight: 700;
  color: #1f2937;
  margin: 0 0 0.5rem 0;
  line-height: 1.3;
}

.dark .item-name {
  color: #f3f4f6;
}

.item-meta {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.875rem;
  color: #6b7280;
  margin-bottom: 0.5rem;
}

.dark .item-meta {
  color: #9ca3af;
}

.item-type {
  font-weight: 600;
  color: #10b981;
}

.dark .item-type {
  color: #34d399;
}

.separator {
  color: #d1d5db;
  font-weight: 700;
}

.dark .separator {
  color: #6b7280;
}

.item-stats {
  font-weight: 500;
}

.item-parent {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.75rem;
  color: #9ca3af;
  background: #f1f5f9;
  padding: 0.25rem 0.75rem;
  border-radius: 6px;
  width: fit-content;
}

.dark .item-parent {
  background: #1f2937;
  color: #d1d5db;
}

.item-parent svg {
  color: #6b7280;
}

.dark .item-parent svg {
  color: #9ca3af;
}

.delete-warning {
  background: #fef2f2;
  border: 2px solid #fecaca;
  border-radius: 12px;
  padding: 1.5rem;
}

.dark .delete-warning {
  background: #451a1a;
  border-color: #7f1d1d;
}

.warning-header {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  margin-bottom: 1rem;
}

.warning-header svg {
  color: #ef4444;
  flex-shrink: 0;
}

.dark .warning-header svg {
  color: #f87171;
}

.warning-header h4 {
  font-size: 1rem;
  font-weight: 700;
  color: #991b1b;
  margin: 0;
}

.dark .warning-header h4 {
  color: #fca5a5;
}

.warning-content p {
  font-size: 0.875rem;
  color: #7f1d1d;
  margin: 0;
  line-height: 1.6;
}

.dark .warning-content p {
  color: #fca5a5;
}

.warning-content strong {
  font-weight: 700;
  color: #991b1b;
}

.dark .warning-content strong {
  color: #fef2f2;
}

.delete-modal .modal-actions {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.5rem 2rem 2rem;
  gap: 1rem;
  border-top: 1px solid #f3f4f6;
}

.dark .delete-modal .modal-actions {
  border-top-color: #374151;
}

.cancel-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  background: #f8f9fa;
  color: #6b7280;
  border: 2px solid #e5e7eb;
  padding: 0.875rem 1.5rem;
  border-radius: 10px;
  font-size: 0.875rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
  min-width: 120px;
  flex: 0 0 auto;
}

.cancel-btn:hover {
  background: #f1f5f9;
  border-color: #d1d5db;
  color: #374151;
  transform: translateY(-1px);
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
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
  justify-content: center;
  gap: 0.5rem;
  background: linear-gradient(135deg, #ef4444, #dc2626);
  color: white;
  border: none;
  padding: 0.875rem 1.5rem;
  border-radius: 10px;
  font-size: 0.875rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
  min-width: 140px;
  flex: 1;
  box-shadow: 0 4px 12px rgba(239, 68, 68, 0.3);
}

.delete-confirm-btn:hover:not(:disabled) {
  background: linear-gradient(135deg, #dc2626, #b91c1c);
  transform: translateY(-1px);
  box-shadow: 0 6px 16px rgba(239, 68, 68, 0.4);
}

.delete-confirm-btn:disabled {
  background: #9ca3af;
  cursor: not-allowed;
  transform: none;
  box-shadow: none;
  opacity: 0.7;
}

.dark .delete-confirm-btn {
  background: linear-gradient(135deg, #dc2626, #b91c1c);
}

.dark .delete-confirm-btn:hover:not(:disabled) {
  background: linear-gradient(135deg, #b91c1c, #991b1b);
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
  justify-content: space-between;
  gap: 0.75rem;
  padding: 1.25rem 2rem;
  border-top: 2px solid #e5e7eb;
  flex-shrink: 0;
  background: #f9fafb;
}

.dark .modal-actions-enhanced {
  border-top-color: #374151;
  background: #111827;
}

.btn-primary,
.btn-secondary {
  display: flex;
  align-items: center;
  gap: 0.625rem;
  padding: 0.875rem 1.75rem;
  border-radius: 10px;
  font-size: 0.9375rem;
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
  background: linear-gradient(135deg, #ef4444, #dc2626);
  color: white;
  box-shadow: 0 4px 12px rgba(239, 68, 68, 0.3);
}

.btn-secondary:hover {
  background: linear-gradient(135deg, #dc2626, #b91c1c);
  transform: translateY(-1px);
  box-shadow: 0 6px 16px rgba(239, 68, 68, 0.4);
}

.dark .btn-secondary {
  background: linear-gradient(135deg, #ef4444, #dc2626);
  color: white;
  border: none;
}

.btn-outline {
  background: linear-gradient(135deg, #10b981, #059669);
  color: white;
  border: none;
  box-shadow: 0 4px 12px rgba(16, 185, 129, 0.3);
  display: flex;
  align-items: center;
  gap: 0.625rem;
  padding: 0.875rem 1.75rem;
  border-radius: 10px;
  font-size: 0.9375rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
}

.btn-outline:hover {
  background: linear-gradient(135deg, #059669, #047857);
  transform: translateY(-1px);
  box-shadow: 0 6px 16px rgba(16, 185, 129, 0.4);
}

.dark .btn-outline {
  background: linear-gradient(135deg, #10b981, #059669);
  color: white;
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

/* Responsive Design */
@media (max-width: 1200px) {
  .main-content {
    padding: 1.5rem;
  }
}

@media (max-width: 1024px) {
  .main-content {
    padding: 1rem;
  }
  
  .navbar-center {
    gap: 0.25rem;
  }
  
  .nav-item {
    padding: 0.5rem 1rem;
    font-size: 0.7rem;
  }
}

@media (max-width: 768px) {
  .main-content {
    padding: 1rem;
  }
  
  .page-header {
    padding: 1rem;
    margin-bottom: 1.5rem;
  }
  
  .header-content {
    flex-direction: column;
    align-items: stretch;
    gap: 1rem;
  }
  
  .header-actions {
    align-self: flex-start;
  }
  
  .create-subject-btn {
    padding: 0.6rem 1rem;
    font-size: 0.8rem;
  }
  
  .navbar-content {
    padding: 0 0.5rem;
  }
  
  .brand-name {
    display: none;
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

/* Logout Modal Styles */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  backdrop-filter: blur(5px);
  z-index: 1000;
  display: flex;
  align-items: center;
  justify-content: center;
  animation: fadeIn 0.3s ease;
}

.logout-modal {
  max-width: 400px;
  border-radius: 16px;
  overflow: hidden;
  background: white;
  border: 2px solid #3D8D7A;
  animation: modalSlideIn 0.3s ease-out;
}

@keyframes modalSlideIn {
  from {
    opacity: 0;
    transform: translateY(-20px) scale(0.95);
  }
  to {
    opacity: 1;
    transform: translateY(0) scale(1);
  }
}

.logout-header {
  background: linear-gradient(135deg, #3D8D7A, #2d6a5a);
  color: white;
  padding: 1.5rem;
}

.logout-header h3 {
  font-size: 1.2rem;
  font-weight: 600;
  margin: 0;
}

.modal-body {
  padding: 2rem;
  text-align: center;
}

.logout-icon {
  display: flex;
  justify-content: center;
  margin-bottom: 1rem;
}

.logout-icon svg {
  color: #3D8D7A;
  animation: pulse 2s infinite;
}

@keyframes pulse {
  0%, 100% { transform: scale(1); }
  50% { transform: scale(1.05); }
}

.logout-message {
  font-size: 1rem;
  font-weight: 600;
  color: #1e293b;
  margin-bottom: 0.5rem;
}

.logout-submessage {
  font-size: 0.85rem;
  color: #64748b;
  margin-bottom: 0;
}

.logout-footer {
  display: flex;
  gap: 0.75rem;
  padding: 1.5rem 2rem;
  background: #f8fafc;
}

.btn-cancel {
  flex: 1;
  padding: 0.75rem 1rem;
  background: #f1f5f9;
  color: #64748b;
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  font-size: 0.9rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s;
}

.btn-cancel:hover {
  background: #e2e8f0;
  color: #1e293b;
}

.btn-logout {
  flex: 1;
  padding: 0.75rem 1rem;
  background: #ef4444;
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 0.9rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
}

.btn-logout:hover {
  background: #dc2626;
  transform: translateY(-1px);
}

.btn-logout:disabled {
  opacity: 0.7;
  cursor: not-allowed;
  transform: none;
}

.logout-spinner {
  width: 16px;
  height: 16px;
  border: 2px solid rgba(255, 255, 255, 0.3);
  border-top: 2px solid white;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.btn-logout .loading-text {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

/* ============================================
   ADD STUDENTS MODAL - ENHANCED DESIGN
   ============================================ */

.add-students-modal {
  max-width: 900px;
  max-height: 85vh;
}

.add-students-content {
  padding: 0;
  max-height: calc(85vh - 200px);
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  gap: 0;
}

/* Enroll Student by ID Styles - ENHANCED */
.enroll-student-section {
  padding: 1.5rem 2rem;
  background: linear-gradient(135deg, #ecfdf5 0%, #d1fae5 100%);
  border: none;
  border-bottom: 3px solid #10b981;
  border-radius: 0;
  flex-shrink: 0;
  box-shadow: none;
  margin: 0;
}

.dark .enroll-student-section {
  background: linear-gradient(135deg, #064e3b 0%, #065f46 100%);
  border-bottom-color: #10b981;
  box-shadow: none;
}

.enroll-header {
  margin-bottom: 1rem;
}

.header-icon-title {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.icon-circle {
  width: 48px;
  height: 48px;
  border-radius: 12px;
  background: linear-gradient(135deg, #10b981, #059669);
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  flex-shrink: 0;
  box-shadow: 0 4px 12px rgba(16, 185, 129, 0.3);
}

.search-icon-circle {
  background: linear-gradient(135deg, #3b82f6, #2563eb);
  box-shadow: 0 4px 12px rgba(59, 130, 246, 0.3);
}

.enroll-header .section-title {
  color: #065f46;
  margin: 0 0 0.25rem 0;
  font-size: 1.125rem;
  font-weight: 700;
}

.dark .enroll-header .section-title {
  color: #6ee7b7;
}

.enroll-description {
  color: #047857;
  font-size: 0.875rem;
  margin: 0;
  line-height: 1.5;
}

.dark .enroll-description {
  color: #a7f3d0;
}

.enroll-form {
  margin-top: 1rem;
}

.enroll-input-wrapper {
  display: flex;
  gap: 0.75rem;
  align-items: center;
  background: white;
  border: 2px solid #10b981;
  border-radius: 10px;
  padding: 0.5rem 0.75rem;
  transition: all 0.2s;
  box-shadow: 0 2px 8px rgba(16, 185, 129, 0.15);
}

.enroll-student-input {
  flex: 1;
  border: none;
  background: transparent;
  outline: none;
  font-size: 0.9375rem;
  color: #1f2937;
  padding: 0.375rem 0;
  font-weight: 500;
}

.dark .enroll-student-input {
  color: #065f46;
}

.enroll-student-input:focus {
  outline: none;
}

.dark .enroll-student-input:focus {
  outline: none;
}

.enroll-student-input::placeholder {
  color: #9ca3af;
  font-weight: 400;
}

.dark .enroll-student-input::placeholder {
  color: #6b7280;
}

.id-icon {
  color: #10b981;
  flex-shrink: 0;
  width: 20px;
  height: 20px;
}

.dark .id-icon {
  color: #10b981;
}

.enroll-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.625rem 1.25rem;
  background: #10b981;
  color: white;
  border: none;
  border-radius: 8px;
  font-weight: 600;
  font-size: 0.875rem;
  cursor: pointer;
  transition: all 0.2s;
  white-space: nowrap;
  box-shadow: 0 2px 6px rgba(16, 185, 129, 0.3);
}

.enroll-btn:hover:not(:disabled) {
  background: #059669;
  transform: translateY(-1px);
  box-shadow: 0 4px 10px rgba(16, 185, 129, 0.4);
}

.enroll-btn:active:not(:disabled) {
  transform: translateY(0);
}

.enroll-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.spinner-icon {
  animation: spin 1s linear infinite;
}

@keyframes spin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}

.enrollment-message {
  padding: 0.625rem 0.875rem;
  border-radius: 8px;
  font-size: 0.875rem;
  font-weight: 600;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  animation: slideIn 0.3s ease-out;
}

@keyframes slideIn {
  from {
    opacity: 0;
    transform: translateY(-10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.enrollment-message.success {
  background: #d1fae5;
  color: #065f46;
  border: 2px solid #10b981;
}

.dark .enrollment-message.success {
  background: rgba(16, 185, 129, 0.15);
  color: #6ee7b7;
  border-color: rgba(110, 231, 183, 0.4);
}

.enrollment-message.error {
  background: #fee2e2;
  color: #991b1b;
  border: 2px solid #ef4444;
}

.dark .enrollment-message.error {
  background: rgba(239, 68, 68, 0.15);
  color: #fca5a5;
  border-color: rgba(252, 165, 165, 0.4);
}

/* Modal Divider - ENHANCED */
.modal-divider {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 1.5rem 2rem;
  background: #f9fafb;
}

.modal-divider::before,
.modal-divider::after {
  content: '';
  flex: 1;
  height: 2px;
  background: linear-gradient(90deg, transparent, #d1d5db, transparent);
}

.dark .modal-divider::before,
.dark .modal-divider::after {
  background: linear-gradient(90deg, transparent, #374151, transparent);
}

.modal-divider span {
  padding: 0 1.25rem;
  color: #6b7280;
  font-weight: 600;
  font-size: 0.875rem;
  letter-spacing: 0.05em;
  background: white;
  border: 2px solid #e5e7eb;
  border-radius: 20px;
  padding: 0.375rem 1rem;
}

.dark .modal-divider span {
  color: #9ca3af;
  background: #1f2937;
  border-color: #374151;
}

/* Student Search Section - ENHANCED */
.student-search-section {
  padding: 2rem;
  background: white;
}

.search-header {
  margin-bottom: 1.25rem;
}

.header-icon-title {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.section-title {
  color: #1f2937;
  margin: 0 0 0.25rem 0;
  font-size: 1.125rem;
  font-weight: 700;
}
.dark .section-title {
  color: #f1f5f9;
}

.search-description {
  color: #6b7280;
  font-size: 0.875rem;
  margin: 0;
}
.dark .search-description {
  color: #9ca3af;
}

.search-filters-enhanced {
  display: grid;
  grid-template-columns: 1fr auto;
  gap: 0.5rem;
  margin-bottom: 0.5rem;
  flex-shrink: 0;
}

.search-input-wrapper {
  position: relative;
  display: flex;
  align-items: center;
}

.search-icon {
  position: absolute;
  left: 0.75rem;
  color: #9ca3af;
  pointer-events: none;
  z-index: 1;
}

.student-search-input-enhanced {
  width: 100%;
  padding: 0.875rem 0.875rem 0.875rem 2.75rem;
  border: 2px solid #e5e7eb;
  border-radius: 12px;
  font-size: 1rem;
  transition: all 0.2s;
  background: white;
}
.student-search-input-enhanced:focus {
  outline: none;
  border-color: #10b981;
  box-shadow: 0 0 0 3px rgba(16, 185, 129, 0.1);
}
.dark .student-search-input-enhanced {
  background: #1f2937;
  border-color: #374151;
  color: #f9fafb;
}
.dark .student-search-input-enhanced:focus {
  border-color: #34d399;
  box-shadow: 0 0 0 3px rgba(52, 211, 153, 0.1);
}

.grade-filter-select-enhanced {
  padding: 0.875rem 1rem;
  border: 2px solid #e5e7eb;
  border-radius: 12px;
  font-size: 0.875rem;
  font-weight: 500;
  background: white;
  cursor: pointer;
  transition: all 0.2s;
  min-width: 140px;
}
.grade-filter-select-enhanced:focus {
  outline: none;
  border-color: #10b981;
  box-shadow: 0 0 0 3px rgba(16, 185, 129, 0.1);
}
.dark .grade-filter-select-enhanced {
  background: #1f2937;
  border-color: #374151;
  color: #f9fafb;
}

.search-hint {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.625rem 0.875rem;
  background: #f0fdf4;
  border: 1px solid #bbf7d0;
  border-radius: 6px;
  font-size: 0.8125rem;
  color: #059669;
  flex-shrink: 0;
}
.dark .search-hint {
  background: #064e3b;
  border-color: #065f46;
  color: #34d399;
}

/* Students List Section - ENHANCED */
.students-list-section {
  border-top: 1px solid #e5e7eb;
  padding-top: 0.75rem;
  flex: 1;
  display: flex;
  flex-direction: column;
  min-height: 0;
}
.dark .students-list-section {
  border-top-color: #374151;
}

.students-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 0.5rem;
  flex-shrink: 0;
}

.students-header h4 {
  font-size: 1rem;
  font-weight: 600;
  color: #1f2937;
}
.dark .students-header h4 {
  color: #f9fafb;
}

.batch-actions {
  display: flex;
  gap: 0.5rem;
}

.add-batch-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  background: linear-gradient(135deg, #10b981, #059669);
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 6px;
  font-size: 0.875rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s;
}
.add-batch-btn:hover:not(:disabled) {
  background: linear-gradient(135deg, #059669, #047857);
  transform: translateY(-1px);
}
.add-batch-btn:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.clear-selection-btn {
  background: transparent;
  color: #6b7280;
  border: 1px solid #d1d5db;
  padding: 0.5rem 1rem;
  border-radius: 6px;
  font-size: 0.875rem;
  cursor: pointer;
  transition: all 0.2s;
}
.clear-selection-btn:hover {
  background: #f3f4f6;
  border-color: #9ca3af;
}
.dark .clear-selection-btn {
  color: #9ca3af;
  border-color: #374151;
}
.dark .clear-selection-btn:hover {
  background: #1f2937;
  border-color: #4b5563;
}

.loading-state, .empty-search {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.75rem;
  padding: 1.25rem;
  text-align: center;
  color: #6b7280;
  flex-shrink: 0;
}
.dark .loading-state, .dark .empty-search {
  color: #9ca3af;
}

.students-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
  gap: 0.625rem;
  flex: 1;
  overflow-y: auto;
  min-height: 0;
max-height: 200px;
padding-right: 0.25rem;
}

.student-card {
display: flex;
align-items: center;
gap: 0.625rem;
padding: 0.625rem;
border: 2px solid #e5e7eb;
border-radius: 6px;
cursor: pointer;
transition: all 0.2s;
position: relative;
background: white;
}
.student-card:hover {
border-color: #10b981;
background: #f0fdf4;
}
.student-card.selected {
border-color: #10b981;
background: #ecfdf5;
}
</style>