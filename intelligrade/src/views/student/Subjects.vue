<template>
  <div class="subjects-container">
    <!-- Header Section (Uniform Card Style) -->
    <div class="section-header-card minimal-header-card">
      <div class="section-header-left">
        <div class="section-header-icon minimal-header-icon">
          <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M19,3H5C3.9,3 3,3.9 3,5V19C3,20.1 3.9,21 5,21H19C20.1,21 21,20.1 21,19V5C21,3.9 20.1,3 19,3M5,19V5H19V19H5Z" />
          </svg>
        </div>
        <div>
          <div class="section-header-title minimal-header-title">My Subjects</div>
          <div class="section-header-sub minimal-header-sub">View and manage your enrolled subjects</div>
        </div>
      </div>
      <div class="section-header-stats">
        <div class="stat-item">
          <span class="stat-number">{{ totalSubjects }}</span>
          <span class="stat-label">Total Subjects</span>
        </div>
      </div>
    </div>

    <!-- Filter and Search -->
    <div class="controls-section">
      <div class="search-box">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
          <path d="M9.5,3A6.5,6.5 0 0,1 16,9.5C16,11.11 15.41,12.59 14.44,13.73L14.71,14H15.5L20.5,19L19,20.5L14,15.5V14.71L13.73,14.44C12.59,15.41 11.11,16 9.5,16A6.5,6.5 0 0,1 3,9.5A6.5,6.5 0 0,1 9.5,3M9.5,5C7,5 5,7 5,9.5C5,12 7,14 9.5,14C12,14 14,12 14,9.5C14,7 12,5 9.5,5Z" />
        </svg>
        <input 
          type="text" 
          v-model="searchQuery" 
          placeholder="Search subjects..."
          class="search-input"
        />
      </div>
      <div class="filter-tabs">
        <button 
          v-for="filter in filters" 
          :key="filter.key"
          @click="activeFilter = filter.key"
          :class="['filter-tab', { 'active': activeFilter === filter.key }]"
        >
          {{ filter.label }}
        </button>
      </div>
    </div>

    <!-- Subjects Grid -->
    <div class="subjects-grid">
      <div 
        v-for="subject in filteredSubjects" 
        :key="subject.id" 
        class="subject-card"
        @click="viewSubjectDetails(subject)"
      >
        <div class="subject-header">
          <div class="subject-icon" :style="{ background: subject.color }">
            <span>{{ subject.code.substring(0, 2) }}</span>
          </div>
          <div class="subject-status">
            <span :class="['status-badge', subject.status]">{{ subject.status }}</span>
          </div>
        </div>
        
        <div class="subject-content">
          <h3 class="subject-title">{{ subject.name }}</h3>
          <p class="subject-code">{{ subject.code }}</p>
          <p class="subject-instructor">{{ subject.instructor }}</p>
        </div>
        
        <div class="subject-stats compact">
          <div class="stat">
            <span class="stat-value">{{ subject.assessments }}</span>
            <span class="stat-text">Assessments</span>
          </div>
        </div>
        <div class="subject-actions compact">
          <button class="action-btn primary" @click.stop="viewAssessments(subject)">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
              <path d="M14,2H6A2,2 0 0,0 4,4V20A2,2 0 0,0 6,22H18A2,2 0 0,0 20,20V8L14,2M18,20H6V4H13V9H18V20Z" />
            </svg>
            Assess
          </button>
        </div>
      </div>
    </div>

    <!-- Empty State -->
    <div v-if="filteredSubjects.length === 0" class="empty-state">
      <div class="empty-icon">
        <svg width="64" height="64" viewBox="0 0 24 24" fill="currentColor">
          <path d="M19,3H5C3.9,3 3,3.9 3,5V19C3,20.1 3.9,21 5,21H19C20.1,21 21,20.1 21,19V5C21,3.9 20.1,3 19,3M5,19V5H19V19H5Z" />
        </svg>
      </div>
      <h3>No subjects found</h3>
      <p>Try adjusting your search or filter criteria</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Subjects',
  data() {
    return {
      searchQuery: '',
      activeFilter: 'all',
      filters: [
        { key: 'all', label: 'All Subjects' },
        { key: 'active', label: 'Active' },
        { key: 'completed', label: 'Completed' },
        { key: 'pending', label: 'Pending' }
      ],
      subjects: [],
      pollingInterval: null,
    };
  },
  computed: {
    totalSubjects() {
      return this.subjects.length;
    },
    filteredSubjects() {
      let filtered = this.subjects;
      
      // Filter by status
      if (this.activeFilter !== 'all') {
        filtered = filtered.filter(subject => subject.status === this.activeFilter);
      }
      
      // Filter by search query
      if (this.searchQuery) {
        filtered = filtered.filter(subject => 
          subject.name.toLowerCase().includes(this.searchQuery.toLowerCase()) ||
          subject.code.toLowerCase().includes(this.searchQuery.toLowerCase()) ||
          subject.instructor.toLowerCase().includes(this.searchQuery.toLowerCase())
        );
      }
      
      return filtered;
    }
  },
  methods: {
    async fetchSubjects() {
      try {
        const response = await fetch('/api/subjects');
        if (!response.ok) throw new Error('Failed to fetch subjects');
        const data = await response.json();
        this.subjects = data;
      } catch (error) {
        console.error('Error fetching subjects:', error);
      }
    },
    viewSubjectDetails(subject) {
      console.log('Viewing subject details:', subject);
      // Navigate to subject details page
    },
    viewAssessments(subject) {
      console.log('Viewing assessments for:', subject);
      // Navigate to assessments for this subject
    }
  },
  mounted() {
    this.fetchSubjects();
    this.pollingInterval = setInterval(this.fetchSubjects, 5000);
  },
  beforeUnmount() {
    if (this.pollingInterval) clearInterval(this.pollingInterval);
  }
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

.subjects-container {
  padding: 2rem;
  max-width: 1400px;
  margin: 0 auto;
  font-family: 'Inter', sans-serif;
  background: var(--bg-primary);
  min-height: 100vh;
}


/* Modern section header card style (shared with dashboard/settings) */
.section-header-card {
  display: flex;
  align-items: center;
  background: var(--bg-card);
  border-radius: 24px;
  box-shadow: 0 4px 24px 0 var(--shadow-medium);
  border: 1.5px solid var(--border-color-hover);
  padding: 2.2rem 2.5rem;
  margin-bottom: 2.2rem;
  min-height: 110px;
  gap: 2.2rem;
  justify-content: space-between;
}
.minimal-header-card {
  border-radius: 28px;
  box-shadow: 0 8px 32px 0 var(--shadow-strong);
  background: var(--bg-card);
  border: 1.5px solid var(--border-color-hover);
  padding: 3.5rem 4.5rem;
  min-height: 170px;
  gap: 3.5rem;
}
.minimal-header-icon {
  width: 88px;
  height: 88px;
  background: #4dbb98;
  border-radius: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #fff;
  box-shadow: none;
}
.minimal-header-title {
  font-size: 2.5rem;
  font-weight: 700;
  color: var(--text-primary);
  margin-bottom: 0.12rem;
  letter-spacing: -0.01em;
}
.minimal-header-sub {
  font-size: 1.25rem;
  color: var(--text-secondary);
  font-weight: 400;
  margin-bottom: 0;
}
.section-header-left {
  display: flex;
  align-items: center;
  gap: 1.5rem;
}
.section-header-icon {
  width: 56px;
  height: 56px;
  background: linear-gradient(135deg, #4dbb98 0%, #33806b 100%);
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #fff;
  box-shadow: 0 2px 8px 0 rgba(61, 141, 122, 0.10);
}
.section-header-title {
  font-size: 2rem;
  font-weight: 700;
  color: var(--text-primary);
  margin-bottom: 0.18rem;
  letter-spacing: -0.01em;
}
.section-header-sub {
  font-size: 1.08rem;
  color: var(--text-secondary);
  font-weight: 400;
  margin-bottom: 0;
}
.section-header-stats {
  display: flex;
  align-items: center;
  gap: 1.5rem;
}

.stat-item {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.stat-number {
  font-size: 2.5rem;
  font-weight: 800;
  color: #3D8D7A;
  line-height: 1;
}

.stat-label {
  font-size: 0.875rem;
  font-weight: 600;
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-top: 0.5rem;
}

.controls-section {
  background: var(--bg-card-translucent);
  backdrop-filter: blur(20px);
  border-radius: 20px;
  padding: 2rem;
  margin-bottom: 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 2rem;
  box-shadow: 0 8px 32px var(--shadow-light);
  border: 1px solid var(--border-color-light);
}

.search-box {
  display: flex;
  align-items: center;
  background: var(--bg-input);
  border: 1px solid var(--border-color-light);
  border-radius: 16px;
  padding: 1rem 1.5rem;
  gap: 1rem;
  min-width: 300px;
  transition: all 0.3s ease;
}

.search-box:focus-within {
  border-color: var(--border-color-focus);
  background: var(--bg-input-focus);
}

.search-box svg {
  color: #3D8D7A;
  flex-shrink: 0;
}

.search-input {
  border: none;
  background: transparent;
  outline: none;
  font-size: 1rem;
  color: var(--text-primary);
  width: 100%;
  font-family: 'Inter', sans-serif;
}

.search-input::placeholder {
  color: var(--text-placeholder);
}

.filter-tabs {
  display: flex;
  gap: 0.5rem;
}

.filter-tab {
  background: var(--bg-input);
  border: 1px solid var(--border-color-light);
  border-radius: 12px;
  padding: 0.75rem 1.5rem;
  cursor: pointer;
  transition: all 0.3s ease;
  font-weight: 600;
  color: var(--text-primary);
  font-family: 'Inter', sans-serif;
}

.filter-tab:hover {
  background: var(--bg-hover);
  transform: translateY(-1px);
}

.filter-tab.active {
  background: linear-gradient(135deg, #3D8D7A 0%, #A3D1C6 100%);
  color: white;
  border-color: transparent;
  box-shadow: 0 4px 16px rgba(61, 141, 122, 0.2);
}


.subjects-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
  gap: 1.2rem;
  margin-bottom: 1.2rem;
}

.subject-card {
  background: var(--bg-card-translucent);
  backdrop-filter: blur(20px);
  border-radius: 18px;
  padding: 1.1rem 1rem 1.2rem 1rem;
  box-shadow: 0 4px 16px var(--shadow-light);
  border: 1px solid var(--border-color-light);
  transition: all 0.2s ease;
  cursor: pointer;
  display: flex;
  flex-direction: column;
  gap: 1rem;
  min-width: 0;
  min-height: 0;
}

.subject-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 16px 48px var(--shadow-medium);
}

.subject-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
}

.subject-icon {
  width: 60px;
  height: 60px;
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-weight: 800;
  font-size: 1.25rem;
  box-shadow: 0 8px 32px rgba(61, 141, 122, 0.2);
}

.status-badge {
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
  padding: 0.5rem 1rem;
  border-radius: 12px;
  letter-spacing: 0.5px;
}

.status-badge.active {
  background: rgba(34, 197, 94, 0.2);
  color: #16a34a;
}

.status-badge.completed {
  background: rgba(59, 130, 246, 0.2);
  color: #2563eb;
}

.status-badge.pending {
  background: rgba(255, 193, 7, 0.2);
  color: #e6b000;
}

.subject-content {
  flex: 1;
}

.subject-title {
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--text-primary);
  margin-bottom: 0.5rem;
  line-height: 1.2;
}

.subject-code {
  font-size: 0.875rem;
  font-weight: 600;
  color: var(--text-muted);
  margin-bottom: 0.5rem;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.subject-instructor {
  font-size: 1rem;
  color: var(--text-secondary);
  margin: 0;
}

.subject-stats {
  background: var(--bg-stats);
  border-radius: 16px;
  padding: 1.5rem;
}

.stat-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
}

.stat {
  text-align: center;
}

.stat-value {
  display: block;
  font-size: 1.5rem;
  font-weight: 800;
  color: #3D8D7A;
  line-height: 1;
}

.stat-text {
  font-size: 0.75rem;
  font-weight: 600;
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-top: 0.5rem;
}

.subject-actions {
  display: flex;
  gap: 1rem;
}

.action-btn {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  padding: 0.875rem 1rem;
  border-radius: 12px;
  cursor: pointer;
  transition: all 0.3s ease;
  font-weight: 600;
  font-size: 0.875rem;
  border: none;
  font-family: 'Inter', sans-serif;
}

.action-btn.primary {
  background: linear-gradient(135deg, #3D8D7A 0%, #A3D1C6 100%);
  color: white;
  box-shadow: 0 4px 16px rgba(61, 141, 122, 0.2);
}

.action-btn.primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(61, 141, 122, 0.3);
}

.action-btn.secondary {
  background: var(--bg-secondary);
  color: #3D8D7A;
  border: 1px solid var(--border-color-light);
}

.action-btn.secondary:hover {
  background: var(--bg-hover);
  transform: translateY(-2px);
}

.empty-state {
  text-align: center;
  padding: 4rem 2rem;
  background: var(--bg-card-translucent);
  backdrop-filter: blur(20px);
  border-radius: 24px;
  box-shadow: 0 8px 32px var(--shadow-light);
  border: 1px solid var(--border-color-light);
}

.empty-icon {
  width: 80px;
  height: 80px;
  background: rgba(61, 141, 122, 0.1);
  border-radius: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #3D8D7A;
  margin: 0 auto 2rem;
}

.empty-state h3 {
  font-size: 1.5rem;
  font-weight: 700;
  color: #3D8D7A;
  margin-bottom: 1rem;
}

.empty-state p {
  color: var(--text-secondary);
  font-size: 1rem;
  margin: 0;
}

@media (max-width: 768px) {
  .subjects-container {
    padding: 1rem;
  }
  
  .page-header {
    flex-direction: column;
    text-align: center;
    gap: 2rem;
    padding: 2rem;
  }
  
  .header-content {
    flex-direction: column;
    text-align: center;
  }
  
  .page-title {
    font-size: 2rem;
  }
  
  .controls-section {
    flex-direction: column;
    gap: 1.5rem;
  }
  
  .search-box {
    min-width: auto;
    width: 100%;
  }
  
  .filter-tabs {
    flex-wrap: wrap;
    justify-content: center;
  }
  
  .subjects-grid {
    grid-template-columns: 1fr;
    gap: 1.5rem;
  }
  
  .subject-actions {
    flex-direction: column;
  }
}
</style>