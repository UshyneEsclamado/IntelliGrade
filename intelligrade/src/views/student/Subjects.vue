<template>
  <div class="subjects-container">
    <!-- Header Section -->
    <div class="page-header">
      <div class="header-content">
        <div class="header-icon">
          <svg width="40" height="40" viewBox="0 0 24 24" fill="currentColor">
            <path d="M19,3H5C3.9,3 3,3.9 3,5V19C3,20.1 3.9,21 5,21H19C20.1,21 21,20.1 21,19V5C21,3.9 20.1,3 19,3M5,19V5H19V19H5Z" />
          </svg>
        </div>
        <div class="header-text">
          <h1 class="page-title">My Subjects</h1>
          <p class="page-subtitle">View and manage your enrolled subjects</p>
        </div>
      </div>
      <div class="header-stats">
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
        
        <div class="subject-stats">
          <div class="stat-row">
            <div class="stat">
              <span class="stat-value">{{ subject.assessments }}</span>
              <span class="stat-text">Assessments</span>
            </div>
            <div class="stat">
              <span class="stat-value">{{ subject.attendance }}%</span>
              <span class="stat-text">Attendance</span>
            </div>
          </div>
        </div>
        
        <div class="subject-actions">
          <button class="action-btn primary" @click.stop="viewAssessments(subject)">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
              <path d="M14,2H6A2,2 0 0,0 4,4V20A2,2 0 0,0 6,22H18A2,2 0 0,0 20,20V8L14,2M18,20H6V4H13V9H18V20Z" />
            </svg>
            Assessments
          </button>
          <button class="action-btn secondary" @click.stop="viewMaterials(subject)">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
              <path d="M13,9H18.5L13,3.5V9M6,2H14L20,8V20A2,2 0 0,1 18,22H6C4.89,22 4,21.1 4,20V4C4,2.89 4.89,2 6,2M15,18V16H6V18H15M18,14V12H6V14H18Z" />
            </svg>
            Materials
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
      subjects: [
        {
          id: 1,
          name: 'Mathematics 101',
          code: 'MATH101',
          instructor: 'Dr. Smith Johnson',
          status: 'active',
          assessments: 8,
          attendance: 95,
          color: 'linear-gradient(135deg, #3D8D7A 0%, #A3D1C6 100%)'
        },
        {
          id: 2,
          name: 'English Literature',
          code: 'ENG201',
          instructor: 'Prof. Emily Davis',
          status: 'active',
          assessments: 6,
          attendance: 88,
          color: 'linear-gradient(135deg, #B3D8A8 0%, #3D8D7A 100%)'
        },
        {
          id: 3,
          name: 'Chemistry 101',
          code: 'CHEM101',
          instructor: 'Dr. Michael Brown',
          status: 'active',
          assessments: 10,
          attendance: 92,
          color: 'linear-gradient(135deg, #A3D1C6 0%, #B3D8A8 100%)'
        },
        {
          id: 4,
          name: 'Physics 102',
          code: 'PHY102',
          instructor: 'Prof. Sarah Wilson',
          status: 'pending',
          assessments: 0,
          attendance: 0,
          color: 'linear-gradient(135deg, #3D8D7A 0%, #FBFFE4 100%)'
        },
        {
          id: 5,
          name: 'History 101',
          code: 'HIST101',
          instructor: 'Dr. Robert Taylor',
          status: 'completed',
          assessments: 12,
          attendance: 100,
          color: 'linear-gradient(135deg, #B3D8A8 0%, #A3D1C6 100%)'
        },
        {
          id: 6,
          name: 'Computer Science 201',
          code: 'CS201',
          instructor: 'Prof. Lisa Anderson',
          status: 'active',
          assessments: 15,
          attendance: 97,
          color: 'linear-gradient(135deg, #A3D1C6 0%, #3D8D7A 100%)'
        }
      ]
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
    viewSubjectDetails(subject) {
      console.log('Viewing subject details:', subject);
      // Navigate to subject details page
    },
    viewAssessments(subject) {
      console.log('Viewing assessments for:', subject);
      // Navigate to assessments for this subject
    },
    viewMaterials(subject) {
      console.log('Viewing materials for:', subject);
      // Navigate to materials for this subject
    }
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
}

.page-header {
  background: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(20px);
  border-radius: 24px;
  padding: 2.5rem;
  margin-bottom: 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  box-shadow: 0 8px 32px rgba(61, 141, 122, 0.1);
  border: 1px solid rgba(61, 141, 122, 0.1);
}

.header-content {
  display: flex;
  align-items: center;
  gap: 1.5rem;
}

.header-icon {
  width: 80px;
  height: 80px;
  background: linear-gradient(135deg, #3D8D7A 0%, #A3D1C6 100%);
  border-radius: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  box-shadow: 0 8px 32px rgba(61, 141, 122, 0.3);
}

.page-title {
  font-size: 2.5rem;
  font-weight: 800;
  color: #3D8D7A;
  margin-bottom: 0.5rem;
  text-shadow: 0 2px 4px rgba(61, 141, 122, 0.1);
}

.page-subtitle {
  font-size: 1.1rem;
  color: #666;
  margin: 0;
}

.header-stats {
  text-align: center;
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
  color: #777;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-top: 0.5rem;
}

.controls-section {
  background: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(20px);
  border-radius: 20px;
  padding: 2rem;
  margin-bottom: 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 2rem;
  box-shadow: 0 8px 32px rgba(61, 141, 122, 0.1);
  border: 1px solid rgba(61, 141, 122, 0.1);
}

.search-box {
  display: flex;
  align-items: center;
  background: rgba(251, 255, 228, 0.5);
  border: 1px solid rgba(61, 141, 122, 0.1);
  border-radius: 16px;
  padding: 1rem 1.5rem;
  gap: 1rem;
  min-width: 300px;
  transition: all 0.3s ease;
}

.search-box:focus-within {
  border-color: rgba(61, 141, 122, 0.3);
  background: rgba(251, 255, 228, 0.8);
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
  color: #3D8D7A;
  width: 100%;
  font-family: 'Inter', sans-serif;
}

.search-input::placeholder {
  color: #999;
}

.filter-tabs {
  display: flex;
  gap: 0.5rem;
}

.filter-tab {
  background: rgba(251, 255, 228, 0.5);
  border: 1px solid rgba(61, 141, 122, 0.1);
  border-radius: 12px;
  padding: 0.75rem 1.5rem;
  cursor: pointer;
  transition: all 0.3s ease;
  font-weight: 600;
  color: #3D8D7A;
  font-family: 'Inter', sans-serif;
}

.filter-tab:hover {
  background: rgba(61, 141, 122, 0.1);
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
  grid-template-columns: repeat(auto-fill, minmax(380px, 1fr));
  gap: 2rem;
  margin-bottom: 2rem;
}

.subject-card {
  background: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(20px);
  border-radius: 24px;
  padding: 2rem;
  box-shadow: 0 8px 32px rgba(61, 141, 122, 0.1);
  border: 1px solid rgba(61, 141, 122, 0.1);
  transition: all 0.3s ease;
  cursor: pointer;
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.subject-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 16px 48px rgba(61, 141, 122, 0.15);
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
  color: #3D8D7A;
  margin-bottom: 0.5rem;
  line-height: 1.2;
}

.subject-code {
  font-size: 0.875rem;
  font-weight: 600;
  color: #777;
  margin-bottom: 0.5rem;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.subject-instructor {
  font-size: 1rem;
  color: #666;
  margin: 0;
}

.subject-stats {
  background: rgba(251, 255, 228, 0.5);
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
  color: #777;
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
  background: rgba(251, 255, 228, 0.8);
  color: #3D8D7A;
  border: 1px solid rgba(61, 141, 122, 0.2);
}

.action-btn.secondary:hover {
  background: rgba(61, 141, 122, 0.1);
  transform: translateY(-2px);
}

.empty-state {
  text-align: center;
  padding: 4rem 2rem;
  background: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(20px);
  border-radius: 24px;
  box-shadow: 0 8px 32px rgba(61, 141, 122, 0.1);
  border: 1px solid rgba(61, 141, 122, 0.1);
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
  color: #666;
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