<template>
  <div class="auth-wrapper">
    <div class="geometric-shapes"></div>
    <div class="floating-elements">
      <div class="floating-circle circle-1"></div>
      <div class="floating-circle circle-2"></div>
      <div class="floating-circle circle-3"></div>
    </div>
    
    <div class="auth-container">
      <div class="auth-box">
        <!-- Header Section -->
        <div class="logo-section">
          <div class="class-icon">
            <svg width="32" height="32" viewBox="0 0 24 24" fill="currentColor">
              <path d="M12,3L1,9L12,15L21,10.09V17H23V9M5,13.18V17.18L12,21L19,17.18V13.18L12,17L5,13.18Z"/>
            </svg>
          </div>
          <h1>Select Section</h1>
          <p class="subtitle" v-if="classData">Choose a section for {{ classData.name }}</p>
          <p class="subtitle" v-else>Choose a section to join</p>
        </div>

        <!-- Loading State -->
        <div v-if="isLoading" class="loading-container">
          <div class="spinner-large"></div>
          <p>Loading sections...</p>
        </div>

        <!-- Error Message -->
        <div v-if="error && !isLoading" class="error-message">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
            <path d="M13,13H11V7H13M13,17H11V15H13M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2Z"/>
          </svg>
          {{ error }}
        </div>

        <!-- Sections List -->
        <div v-if="!isLoading && !error" class="sections-container">
          <!-- No Sections Available -->
          <div v-if="sections.length === 0" class="no-sections">
            <div class="no-sections-icon">
              <svg width="48" height="48" viewBox="0 0 24 24" fill="currentColor">
                <path d="M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2M12,6A1.5,1.5 0 0,1 13.5,7.5A1.5,1.5 0 0,1 12,9A1.5,1.5 0 0,1 10.5,7.5A1.5,1.5 0 0,1 12,6M9.7,14.4L8.8,13.5L11,11.3V16.5H13V11.3L15.2,13.5L14.3,14.4L12,12.1"/>
              </svg>
            </div>
            <h3>No Sections Available</h3>
            <p>There are currently no sections available for this class. Please contact your teacher or try again later.</p>
            <button class="retry-btn" @click="loadSections">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                <path d="M17.65,6.35C16.2,4.9 14.21,4 12,4A8,8 0 0,0 4,12A8,8 0 0,0 12,20C15.73,20 18.84,17.45 19.73,14H17.65C16.83,16.33 14.61,18 12,18A6,6 0 0,1 6,12A6,6 0 0,1 12,6C13.66,6 15.14,6.69 16.22,7.78L13,11H20V4L17.65,6.35Z"/>
              </svg>
              Refresh
            </button>
          </div>

          <!-- Sections Available -->
          <div v-else class="sections-list">
            <div class="section-info">
              <p>Select the section you want to join:</p>
            </div>

            <div 
              v-for="section in sections" 
              :key="section.id"
              class="section-card"
              @click="selectSection(section)"
              :class="{ 'selected': selectedSection && selectedSection.id === section.id }"
            >
              <div class="section-icon">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M19,3H5C3.89,3 3,3.89 3,5V19A2,2 0 0,0 5,21H19A2,2 0 0,0 21,19V5C21,3.89 20.1,3 19,3M19,19H5V5H19V19Z"/>
                </svg>
              </div>
              <div class="section-content">
                <h3>{{ section.name }}</h3>
                <p v-if="section.description">{{ section.description }}</p>
                <p v-else>Section {{ section.name }}</p>
                <div class="section-meta">
                  <span class="student-count">
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor">
                      <path d="M12,4A4,4 0 0,1 16,8A4,4 0 0,1 12,12A4,4 0 0,1 8,8A4,4 0 0,1 12,4M12,14C16.42,14 20,15.79 20,18V20H4V18C4,15.79 7.58,14 12,14Z"/>
                    </svg>
                    {{ section.student_count || 0 }} students
                  </span>
                  <span class="section-code">Code: {{ section.section_code }}</span>
                </div>
              </div>
              <div class="section-arrow">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M4,11V13H16L10.5,18.5L11.92,19.92L19.84,12L11.92,4.08L10.5,5.5L16,11H4Z"/>
                </svg>
              </div>
            </div>

            <!-- Continue Button -->
            <button 
              v-if="selectedSection"
              class="continue-btn"
              @click="proceedToSectionCode"
              :disabled="isProcessing"
            >
              <svg v-if="!isProcessing" width="18" height="18" viewBox="0 0 24 24" fill="currentColor">
                <path d="M4,11V13H16L10.5,18.5L11.92,19.92L19.84,12L11.92,4.08L13.5,5.5L8,11H20Z"/>
              </svg>
              <div v-if="isProcessing" class="spinner"></div>
              {{ isProcessing ? 'Processing...' : 'Continue to Section Code' }}
            </button>
          </div>
        </div>

        <!-- Back Button -->
        <div class="back-section">
          <button class="back-link" @click="goBack">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
              <path d="M20,11V13H8L13.5,18.5L12.08,19.92L4.16,12L12.08,4.08L13.5,5.5L8,11H20Z"/>
            </svg>
            Back to Class Code
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { supabase } from "../supabase.js";

export default {
  name: "SectionSelection",
  data() {
    return {
      classData: null,
      sections: [],
      selectedSection: null,
      isLoading: true,
      isProcessing: false,
      error: null,
    };
  },
  methods: {
    async loadSections() {
      this.isLoading = true;
      this.error = null;

      try {
        // Get class data from session storage
        const storedClassData = sessionStorage.getItem('selectedClass');
        if (!storedClassData) {
          this.error = "Class information not found. Please start over.";
          return;
        }

        this.classData = JSON.parse(storedClassData);

        // Fetch sections for this class
        const { data: sectionsData, error: sectionsError } = await supabase
          .from("sections")
          .select(`
            id,
            name,
            description,
            section_code,
            class_id,
            enrollments(count)
          `)
          .eq("class_id", this.classData.id)
          .order("name");

        if (sectionsError) {
          throw sectionsError;
        }

        // Process sections data to include student count
        this.sections = sectionsData.map(section => ({
          ...section,
          student_count: section.enrollments?.[0]?.count || 0
        }));

      } catch (err) {
        console.error("Error loading sections:", err);
        this.error = err.message || "Failed to load sections. Please try again.";
      } finally {
        this.isLoading = false;
      }
    },

    selectSection(section) {
      this.selectedSection = section;
    },

    async proceedToSectionCode() {
      if (!this.selectedSection) return;

      this.isProcessing = true;

      try {
        // Get current user
        const { data: { user } } = await supabase.auth.getUser();
        
        if (!user) {
          this.error = "Please log in first.";
          this.$router.push("/join-class");
          return;
        }

        // Check if student is already enrolled in this section
        const { data: existingEnrollment, error: enrollmentCheckError } = await supabase
          .from("enrollments")
          .select("id")
          .eq("student_id", user.id)
          .eq("section_id", this.selectedSection.id)
          .single();

        if (existingEnrollment) {
          this.error = "You are already enrolled in this section.";
          this.isProcessing = false;
          return;
        }

        if (enrollmentCheckError && enrollmentCheckError.code !== 'PGRST116') {
          throw enrollmentCheckError;
        }

        // Store selected section data
        sessionStorage.setItem('selectedSection', JSON.stringify(this.selectedSection));
        
        // Redirect to section code entry
        this.$router.push("/join-class/enter-section-code");

      } catch (err) {
        console.error("Section selection error:", err);
        this.error = err.message || "Something went wrong. Please try again.";
      } finally {
        this.isProcessing = false;
      }
    },

    goBack() {
      // Clear stored data and go back to class code entry
      sessionStorage.removeItem('selectedClass');
      sessionStorage.removeItem('selectedSection');
      this.$router.push("/join-class/enter-code");
    },
  },

  async mounted() {
    // Check if user is authenticated
    const { data: { user } } = await supabase.auth.getUser();
    if (!user) {
      this.$router.push("/join-class");
      return;
    }

    // Load sections
    await this.loadSections();
  }
};
</script>

<style scoped>
/* Base styles - inherited from previous components */
* { 
  margin: 0; 
  padding: 0; 
  box-sizing: border-box; 
}

.auth-wrapper {
  position: absolute; 
  inset: 0;
  background: transparent !important;
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  padding: 40px;
  font-family: 'Inter', sans-serif;
  overflow-y: auto;
}

.geometric-shapes {
  position: fixed;
  inset: 0;
  z-index: 0;
  overflow: hidden;
  background: linear-gradient(135deg, #A3D1C6 0%, #B3D8A8 50%, #FBFFE4 100%);
}

.geometric-shapes::before {
  content: '';
  position: absolute;
  width: 100%;
  height: 100%;
  background: 
    linear-gradient(45deg, transparent 48%, rgba(255,255,255,0.05) 50%, transparent 52%) 0 0 / 80px 80px,
    linear-gradient(-45deg, transparent 48%, rgba(255,255,255,0.05) 50%, transparent 52%) 0 0 / 80px 80px,
    radial-gradient(circle at 20% 30%, rgba(255,255,255,0.08) 0, transparent 60px),
    radial-gradient(circle at 80% 20%, rgba(255,255,255,0.08) 0, transparent 80px),
    radial-gradient(circle at 10% 80%, rgba(255,255,255,0.08) 0, transparent 70px),
    radial-gradient(circle at 90% 70%, rgba(255,255,255,0.08) 0, transparent 90px);
  animation: moveBackground 40s linear infinite;
}

.geometric-shapes::after {
  content: '';
  position: absolute;
  inset: 0;
  background:
    radial-gradient(circle at 15% 25%, rgba(255,255,255,0.1) 0, transparent 250px),
    radial-gradient(circle at 85% 75%, rgba(255,255,255,0.1) 0, transparent 250px),
    radial-gradient(circle at 50% 50%, rgba(255,255,255,0.05) 0, transparent 400px);
  animation: floatShapes 25s ease-in-out infinite;
}

.floating-circle {
  position: absolute;
  border-radius: 50%;
  opacity: 0.08;
  animation: float 10s ease-in-out infinite;
}

.circle-1 { 
  width: 100px; 
  height: 100px; 
  background: #3D8D7A; 
  top: 15%; 
  left: 10%; 
  animation-delay: 0s; 
}

.circle-2 { 
  width: 140px; 
  height: 140px; 
  background: #A3D1C6; 
  bottom: 20%; 
  right: 15%; 
  animation-delay: 3s; 
}

.circle-3 { 
  width: 120px; 
  height: 120px; 
  background: #B3D8A8; 
  top: 60%; 
  left: 70%; 
  animation-delay: 6s; 
}

.auth-container {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  max-width: 600px;
  z-index: 1;
  position: relative;
}

.auth-box {
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(20px);
  padding: 50px 45px;
  border-radius: 24px;
  border: 1px solid rgba(255, 255, 255, 0.3);
  box-shadow: 
    0 25px 50px rgba(61, 141, 122, 0.08),
    0 10px 30px rgba(0, 0, 0, 0.04),
    inset 0 1px 0 rgba(255, 255, 255, 0.9);
  width: 100%;
  text-align: center;
  position: relative;
}

.logo-section {
  margin-bottom: 40px;
}

.class-icon {
  width: 90px;
  height: 90px;
  margin: 0 auto 25px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(61, 141, 122, 0.08);
  border-radius: 50%;
  color: #3D8D7A;
  box-shadow: 0 8px 20px rgba(61, 141, 122, 0.1);
}

h1 {
  color: #3D8D7A;
  font-size: 32px;
  font-weight: 700;
  margin-bottom: 12px;
  letter-spacing: -0.5px;
}

.subtitle {
  color: #3D8D7A;
  font-size: 17px;
  opacity: 0.75;
  font-weight: 500;
}

/* Loading State */
.loading-container {
  text-align: center;
  padding: 40px 20px;
}

.spinner-large {
  width: 40px;
  height: 40px;
  border: 3px solid rgba(61, 141, 122, 0.2);
  border-top: 3px solid #3D8D7A;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin: 0 auto 20px;
}

.loading-container p {
  color: rgba(61, 141, 122, 0.7);
  font-size: 16px;
}

/* Error Message */
.error-message {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 16px 20px;
  border-radius: 12px;
  font-size: 15px;
  font-weight: 500;
  margin-bottom: 20px;
  background: rgba(239, 68, 68, 0.1);
  color: #dc2626;
  border: 1px solid rgba(239, 68, 68, 0.2);
}

/* Sections Container */
.sections-container {
  text-align: left;
}

/* No Sections State */
.no-sections {
  text-align: center;
  padding: 40px 20px;
}

.no-sections-icon {
  width: 80px;
  height: 80px;
  margin: 0 auto 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(61, 141, 122, 0.08);
  border-radius: 50%;
  color: rgba(61, 141, 122, 0.5);
}

.no-sections h3 {
  color: #3D8D7A;
  font-size: 24px;
  font-weight: 600;
  margin-bottom: 10px;
}

.no-sections p {
  color: rgba(61, 141, 122, 0.7);
  font-size: 16px;
  line-height: 1.5;
  margin-bottom: 25px;
}

.retry-btn {
  background: rgba(61, 141, 122, 0.1);
  color: #3D8D7A;
  border: 1px solid rgba(61, 141, 122, 0.2);
  padding: 12px 20px;
  border-radius: 12px;
  font-size: 14px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s ease;
  display: inline-flex;
  align-items: center;
  gap: 8px;
}

.retry-btn:hover {
  background: rgba(61, 141, 122, 0.15);
  border-color: rgba(61, 141, 122, 0.3);
}

/* Sections List */
.section-info {
  margin-bottom: 20px;
}

.section-info p {
  color: #3D8D7A;
  font-size: 16px;
  font-weight: 500;
}

.sections-list {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.section-card {
  background: rgba(255, 255, 255, 0.8);
  border: 2px solid rgba(61, 141, 122, 0.15);
  border-radius: 16px;
  padding: 20px;
  cursor: pointer;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  gap: 15px;
  position: relative;
}

.section-card:hover {
  border-color: rgba(61, 141, 122, 0.3);
  background: rgba(255, 255, 255, 0.95);
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(61, 141, 122, 0.1);
}

.section-card.selected {
  border-color: #3D8D7A;
  background: rgba(61, 141, 122, 0.05);
  box-shadow: 0 8px 25px rgba(61, 141, 122, 0.15);
}

.section-icon {
  width: 45px;
  height: 45px;
  background: rgba(61, 141, 122, 0.1);
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #3D8D7A;
  flex-shrink: 0;
}

.section-content {
  flex: 1;
}

.section-content h3 {
  color: #3D8D7A;
  font-size: 18px;
  font-weight: 600;
  margin-bottom: 5px;
}

.section-content p {
  color: rgba(61, 141, 122, 0.7);
  font-size: 14px;
  margin-bottom: 10px;
}

.section-meta {
  display: flex;
  align-items: center;
  gap: 15px;
  flex-wrap: wrap;
}

.student-count,
.section-code {
  display: flex;
  align-items: center;
  gap: 5px;
  color: rgba(61, 141, 122, 0.6);
  font-size: 12px;
  font-weight: 500;
}

.section-arrow {
  color: rgba(61, 141, 122, 0.4);
  transition: all 0.3s ease;
}

.section-card:hover .section-arrow,
.section-card.selected .section-arrow {
  color: #3D8D7A;
  transform: translateX(3px);
}

/* Continue Button */
.continue-btn {
  width: 100%;
  background: linear-gradient(135deg, #3D8D7A 0%, #A3D1C6 100%);
  color: white;
  padding: 18px;
  font-size: 17px;
  font-weight: 600;
  border: none;
  border-radius: 16px;
  cursor: pointer;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 12px;
  margin-top: 25px;
  box-shadow: 0 6px 20px rgba(61, 141, 122, 0.2);
}

.continue-btn:hover:not(:disabled) {
  transform: translateY(-3px);
  box-shadow: 0 12px 30px rgba(61, 141, 122, 0.25);
}

.continue-btn:disabled {
  opacity: 0.7;
  cursor: not-allowed;
  transform: none;
}

.spinner {
  width: 18px;
  height: 18px;
  border: 2px solid rgba(255, 255, 255, 0.3);
  border-top: 2px solid white;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

/* Back Section */
.back-section {
  text-align: center;
  margin-top: 25px;
}

.back-link {
  color: rgba(61, 141, 122, 0.7);
  background: none;
  border: none;
  font-size: 16px;
  font-weight: 500;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  transition: all 0.3s ease;
  padding: 8px 16px;
  border-radius: 8px;
  cursor: pointer;
}

.back-link:hover {
  color: #3D8D7A;
  background: rgba(61, 141, 122, 0.05);
}

/* Animations */
@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

@keyframes float {
  0%, 100% { 
    transform: translateY(0) rotate(0deg); 
  }
  50% { 
    transform: translateY(-25px) rotate(180deg); 
  }
}

@keyframes moveBackground {
  0% {
    transform: translate(0, 0) rotate(0deg);
  }
  100% {
    transform: translate(-80px, -80px) rotate(3deg);
  }
}

@keyframes floatShapes {
  0%, 100% {
    transform: translate(0, 0);
  }
  50% {
    transform: translate(30px, 30px);
  }
}

/* Responsive */
@media (max-width: 768px) {
  .auth-wrapper {
    padding: 25px;
  }
  
  .auth-box {
    padding: 40px 30px;
  }

  .class-icon {
    width: 80px;
    height: 80px;
  }

  h1 {
    font-size: 28px;
  }

  .subtitle {
    font-size: 16px;
  }

  .section-card {
    padding: 15px;
    gap: 12px;
  }

  .section-icon {
    width: 40px;
    height: 40px;
  }

  .section-content h3 {
    font-size: 16px;
  }

  .section-meta {
    gap: 10px;
  }

  .continue-btn {
    font-size: 16px;
    padding: 16px;
  }
}

@media (max-height: 700px) {
  .auth-wrapper {
    align-items: flex-start;
    padding-top: 30px;
  }
}
</style>