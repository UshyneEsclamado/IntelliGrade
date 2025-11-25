<template>
  <div class="home-container">
    <!-- Simple Header -->
    <div class="header-card">
      <div class="header-content">
        <div class="header-left">
          <div class="user-icon">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
              <circle cx="12" cy="7" r="4"></circle>
            </svg>
          </div>
          <div>
            <h1 class="header-title">
              <span v-if="!isLoadingName">Hello, {{ studentName }}!</span>
              <span v-else>Hello, Loading...</span>
            </h1>
            <p class="header-subtitle">Welcome to your dashboard</p>
          </div>
        </div>
        
        <!-- Notification Bell -->
        <div class="notif-wrapper" ref="notifWrapper">
          <button class="notif-btn" @click="toggleNotifDropdown" aria-label="Notifications">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"></path>
              <path d="M13.73 21a2 2 0 0 1-3.46 0"></path>
            </svg>
            <span v-if="notifications.length" class="notif-badge">{{ notifications.length }}</span>
          </button>
          
          <!-- Notification Dropdown -->
          <div v-if="showNotifDropdown" class="notif-dropdown">
            <!-- Mobile backdrop overlay -->
            <div class="notif-backdrop" @click="closeNotifDropdown"></div>
            <div class="notif-content">
              <div class="notif-header">
                <span>Notifications</span>
                <button @click="closeNotifDropdown" class="close-notif-btn">
                  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <line x1="18" y1="6" x2="6" y2="18"></line>
                    <line x1="6" y1="6" x2="18" y2="18"></line>
                  </svg>
                </button>
              </div>
              <div v-if="notifications.length === 0" class="notif-empty">No notifications</div>
              <div v-for="notif in notifications" :key="notif.id" class="notif-item">
                <div class="notif-title">{{ notif.title }}</div>
                <div class="notif-body">{{ notif.body }}</div>
                <div class="notif-date">{{ notif.date }}</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Stats Cards -->
    <div class="stats-grid">
      <div class="stat-card">
        <div class="stat-icon stat-subjects">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
            <path d="M19,3H5C3.9,3 3,3.9 3,5V19C3,20.1 3.9,21 5,21H19C20.1,21 21,20.1 21,19V5C21,3.9 20.1,3 19,3M5,19V5H19V19H5Z" />
          </svg>
        </div>
        <div>
          <div class="stat-number">{{ totalSubjects }}</div>
          <div class="stat-label">Enrolled Subjects</div>
        </div>
      </div>

      <div class="stat-card">
        <div class="stat-icon stat-pending">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
            <circle cx="12" cy="12" r="10"></circle>
            <polyline points="12,6 12,12 16,14" />
          </svg>
        </div>
        <div>
          <div class="stat-number">{{ pendingAssessments }}</div>
          <div class="stat-label">Pending Assessments</div>
        </div>
      </div>
    </div>

    <!-- Main Content Grid -->
    <div class="content-grid">
      <!-- Recent Assessments -->
      <div class="content-card">
        <div class="card-header">
          <h3>Recent Assessments</h3>
          <p class="card-desc">Keep track of your upcoming deadlines</p>
        </div>
        <div class="assessment-list">
          <div v-if="recentAssessments.length === 0" class="empty-state">
            No assessments available
          </div>
          <div v-for="assessment in recentAssessments" :key="assessment.id" class="assessment-item">
            <div class="assessment-info">
              <h4>{{ assessment.title }}</h4>
              <p class="assessment-class">{{ assessment.subject }}</p>
            </div>
            <div class="assessment-due">
              <span class="due-date">{{ formatDate(assessment.dueDate) }}</span>
              <span v-if="assessment.status" class="status" :class="getStatusClass(assessment.status)">
                {{ formatStatus(assessment.status) }}
              </span>
            </div>
          </div>
        </div>
      </div>

      <!-- Quick Links -->
      <div class="content-card">
        <div class="card-header">
          <h3>Quick Links</h3>
          <p class="card-desc">Access key features</p>
        </div>
        <div class="quick-links">
          <button @click.prevent="navigateToSubjects" class="quick-link" type="button">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M19,3H5C3.9,3 3,3.9 3,5V19C3,20.1 3.9,21 5,21H19C20.1,21 21,20.1 21,19V5C21,3.9 20.1,3 19,3M5,19V5H19V19H5Z" />
            </svg>
            My Subjects
          </button>
          <button @click.prevent="navigateToCalendar" class="quick-link" type="button">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M19,19H5V8H19M19,3H18V1H16V3H8V1H6V3H5C3.89,3 3,3.89 3,5V19A2,2 0 0,0 5,21H19A2,2 0 0,0 21,19V5C21,3.89 20.1,3 19,3M16.5,13.5H11V18.5H16.5V13.5Z" />
            </svg>
            Calendar
          </button>
          <button @click.prevent="navigateToMessages" class="quick-link" type="button">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M22 6c0-1.1-.9-2-2-2H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6zM4 6h16v.5l-8 5-8-5V6zm0 13.5V8l8 5 8-5v11.5H4z" />
            </svg>
            Messages
          </button>
          <button @click.prevent="navigateToSettings" class="quick-link" type="button">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M12,15.5A3.5,3.5 0 0,1 8.5,12A3.5,3.5 0 0,1 12,8.5A3.5,3.5 0 0,1 15.5,12A3.5,3.5 0 0,1 12,15.5M19.43,12.97C19.47,12.65 19.5,12.33 19.5,12C19.5,11.67 19.47,11.34 19.43,11.03L21.54,9.37C21.73,9.22 21.78,8.96 21.66,8.74L19.65,5.27C19.54,5.05 19.27,4.96 19.05,5.05L16.56,6.05C16.04,5.66 15.5,5.32 14.9,5.07L14.5,2.42C14.46,2.18 14.25,2 14,2H10C9.75,2 9.54,2.18 9.5,2.42L9.1,5.07C8.5,5.32 7.96,5.66 7.44,6.05L4.95,5.05C4.73,4.96 4.46,5.05 4.34,5.27L2.34,8.74C2.21,8.96 2.27,9.22 2.46,9.37L4.57,11.03C4.53,11.34 4.5,11.67 4.5,12C4.5,12.33 4.53,12.65 4.57,12.97L2.46,14.63C2.27,14.78 2.21,15.04 2.34,15.26L4.34,18.73C4.46,18.95 4.73,19.04 4.95,18.95L7.44,17.94C7.96,18.34 8.5,18.68 9.1,18.93L9.5,21.58C9.54,21.82 9.75,22 10,22H14C14.25,22 14.46,21.82 14.5,21.58L14.9,18.93C15.5,18.68 16.04,18.34 16.56,17.94L19.05,18.95C19.27,19.04 19.54,18.95 19.66,18.73L21.66,15.26C21.78,15.04 21.73,14.78 21.54,14.63L19.43,12.97Z" />
            </svg>
            Settings
          </button>
        </div>
      </div>
    </div>
    
    <!-- Floating Help & Support Button -->
    <button @click="openHelpModal" class="floating-help-btn" title="Help & Support">
      <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <circle cx="12" cy="12" r="10"/>
        <path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/>
        <line x1="12" y1="17" x2="12.01" y2="17"/>
      </svg>
    </button>

    <!-- Help & Support Modal -->
    <div v-if="showHelpModal" class="modal-overlay" @click="closeHelpModal">
      <div class="modal-content document-modal" @click.stop>
        <div class="modal-header">
          <h3>Help & Support</h3>
          <button @click="closeHelpModal" class="close-btn">×</button>
        </div>
        <div class="modal-body document-body">
          <div class="document-content">
            <h4>Welcome to IntelliGrade Help Center</h4>
            <p class="document-date">We're here to help you!</p>
            
            <section>
              <h5>📧 Contact Support</h5>
              <p>Have a question or need assistance? Reach out to our support team:</p>
              <ul>
                <li>Email: <strong>support@intelligrade.edu</strong></li>
                <li>Response Time: Within 24 hours</li>
              </ul>
            </section>

            <section>
              <h5>🔧 Common Issues</h5>
              <p><strong>Can't log in?</strong></p>
              <ul>
                <li>Check if your email and password are correct</li>
                <li>Try resetting your password</li>
                <li>Clear your browser cache and cookies</li>
              </ul>
              
              <p><strong>Quizzes not loading?</strong></p>
              <ul>
                <li>Check your internet connection</li>
                <li>Try refreshing the page</li>
                <li>Make sure you're enrolled in the class</li>
              </ul>
            </section>

            <section>
              <h5>💡 Getting Started</h5>
              <p><strong>For Students:</strong></p>
              <ul>
                <li>View your enrolled subjects and classes</li>
                <li>Take quizzes and assessments</li>
                <li>Check your grades and progress</li>
                <li>Communicate with your teachers</li>
                <li>Track assignment deadlines</li>
              </ul>
            </section>

            <section>
              <h5>🔒 Account Security</h5>
              <ul>
                <li>Use a strong, unique password</li>
                <li>Never share your login credentials</li>
                <li>Log out when using shared computers</li>
                <li>Update your password regularly</li>
              </ul>
            </section>

            <section>
              <h5>📱 Technical Requirements</h5>
              <p>For the best experience with IntelliGrade:</p>
              <ul>
                <li>Use a modern web browser (Chrome, Firefox, Safari, Edge)</li>
                <li>Ensure JavaScript is enabled</li>
                <li>Stable internet connection recommended</li>
                <li>Screen resolution: 1280x720 or higher</li>
              </ul>
            </section>

            <section>
              <h5>📚 Taking Quizzes</h5>
              <ul>
                <li>Make sure to read all instructions carefully</li>
                <li>Submit before the deadline</li>
                <li>Check your internet connection before starting</li>
                <li>Contact your teacher if you experience technical issues</li>
              </ul>
            </section>

            <section>
              <h5>🐛 Report a Bug</h5>
              <p>Found a bug? Help us improve IntelliGrade by reporting it:</p>
              <ul>
                <li>Send detailed description to: <strong>bugs@intelligrade.edu</strong></li>
                <li>Include screenshots if possible</li>
                <li>Mention your browser and device type</li>
              </ul>
            </section>

            <section>
              <h5>💬 Feedback</h5>
              <p>We value your feedback! Share your thoughts and suggestions:</p>
              <ul>
                <li>Email: <strong>feedback@intelligrade.edu</strong></li>
                <li>Your input helps us improve the platform</li>
              </ul>
            </section>
          </div>
        </div>
        <div class="modal-footer">
          <button @click="closeHelpModal" class="btn-primary">Close</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { supabase } from '../../Supabase.js';

export default {
  name: 'StudentHome',
  data() {
    return {
      // UI States
      showHelpModal: false,
      showNotifDropdown: false,
      
      // User Data
      studentName: 'Student',
      userId: null,
      profileId: null,
      studentRecordId: null,
      
      // Loading States
      isLoadingName: true,
      isLoadingStats: false,
      isLoadingAssessments: false,
      isLoadingNotifications: false,
      
      // Dashboard Data
      totalSubjects: 0,
      pendingAssessments: 0,
      recentAssessments: [],
      notifications: [],
      unreadNotifications: 0,
      
      // Real-time
      subscriptions: [],
      pollInterval: null,
      enrolledSectionIds: [],
      
      // Cache
      assessmentCache: new Map(),
      subjectMap: new Map(),
      sectionMap: new Map()
    };
  },
  
  methods: {
    // ==================== UI Methods ====================
    toggleNotifDropdown() {
      this.showNotifDropdown = !this.showNotifDropdown;
      
      // Mark notifications as read when dropdown opens
      if (this.showNotifDropdown && this.unreadNotifications > 0) {
        this.markNotificationsAsRead();
      }
    },

    closeNotifDropdown() {
      this.showNotifDropdown = false;
    },

    markNotificationsAsRead() {
      console.log('📖 Marking notifications as read');
      // Reset unread count
      this.unreadNotifications = 0;
      
      // Save to localStorage
      if (this.studentRecordId) {
        const readKey = `notif_read_${this.studentRecordId}`;
        const timestamp = new Date().toISOString();
        localStorage.setItem(readKey, timestamp);
      }
    },

    handleClickOutside(event) {
      const notifWrapper = this.$refs.notifWrapper;
      if (notifWrapper && !notifWrapper.contains(event.target)) {
        this.closeNotifDropdown();
      }
    },
    
    openHelpModal() {
      this.showHelpModal = true;
    },
    
    closeHelpModal() {
      this.showHelpModal = false;
    },

    // ==================== Navigation Methods (FIXED) ====================
    navigateToSubjects() {
      console.log('🔗 Navigating to subjects...');
      this.$router.push('/student/subjects');
    },

    navigateToCalendar() {
      console.log('🔗 Navigating to calendar...');
      this.$router.push('/student/calendar');
    },

    navigateToMessages() {
      console.log('🔗 Navigating to messages...');
      this.$router.push('/student/messages');
    },

    navigateToSettings() {
      console.log('🔗 Navigating to settings...');
      this.$router.push('/student/settings');
    },

    // ==================== Data Loading Methods ====================
    
    async loadStudentProfile() {
      try {
        this.isLoadingName = true;
        console.log('📝 Loading student profile...');
        
        const { data: { user }, error: authError } = await supabase.auth.getUser();
        
        if (authError || !user) {
          console.error('❌ Auth error:', authError);
          this.studentName = 'Student';
          return false;
        }

        this.userId = user.id;
        console.log('✅ Auth user found:', user.id);

        // Get profile
        const { data: profile, error: profileError } = await supabase
          .from('profiles')
          .select('id, full_name, email, role')
          .eq('auth_user_id', user.id)
          .maybeSingle();

        if (profileError || !profile) {
          console.error('❌ Profile error:', profileError);
          this.studentName = user.email?.split('@')[0] || 'Student';
          return false;
        }

        this.profileId = profile.id;

        if (profile.role !== 'student') {
          console.warn('⚠️ User is not a student');
          this.studentName = profile.full_name || 'User';
          return false;
        }

        // Get student data
        const { data: studentData, error: studentError } = await supabase
          .from('students')
          .select('id, student_id, grade_level, full_name, email, is_active')
          .eq('profile_id', profile.id)
          .maybeSingle();

        if (studentError || !studentData) {
          console.warn('⚠️ Student data error:', studentError);
          this.studentName = profile.full_name || 'Student';
          return false;
        }

        this.studentRecordId = studentData.id;
        this.studentName = studentData.full_name || profile.full_name || 'Student';
        
        console.log('✅ Student profile loaded:', {
          name: this.studentName,
          id: this.studentRecordId,
          gradeLevel: studentData.grade_level
        });

        return true;

      } catch (error) {
        console.error('❌ Error loading student profile:', error);
        this.studentName = 'Student';
        return false;
      } finally {
        this.isLoadingName = false;
      }
    },

    async loadEnrolledSections() {
      if (!this.studentRecordId) {
        console.warn('⚠️ No student record ID');
        return [];
      }
      
      try {
        console.log('📚 Loading enrolled sections...');
        
        const { data: enrollments, error } = await supabase
          .from('enrollments')
          .select('section_id')
          .eq('student_id', this.studentRecordId)
          .eq('status', 'active');

        if (error) {
          console.error('❌ Enrollments error:', error);
          return [];
        }

        this.enrolledSectionIds = enrollments?.map(e => e.section_id) || [];
        console.log('✅ Enrolled sections loaded:', this.enrolledSectionIds.length, 'sections');
        
        return this.enrolledSectionIds;
      } catch (error) {
        console.error('❌ Error loading enrolled sections:', error);
        return [];
      }
    },

    async loadDashboardStats() {
      if (!this.studentRecordId) {
        console.warn('⚠️ Cannot load stats: no student record ID');
        return;
      }

      try {
        this.isLoadingStats = true;
        console.log('📊 Loading dashboard stats...');

        // Ensure we have enrolled sections
        if (this.enrolledSectionIds.length === 0) {
          await this.loadEnrolledSections();
        }

        if (this.enrolledSectionIds.length === 0) {
          console.log('ℹ️ Student has no enrolled sections');
          this.totalSubjects = 0;
          this.pendingAssessments = 0;
          return;
        }

        // Get unique subjects from enrolled sections
        const { data: sections, error: sectionsError } = await supabase
          .from('sections')
          .select('id, subject_id, name')
          .in('id', this.enrolledSectionIds);

        if (sectionsError) {
          console.error('❌ Sections error:', sectionsError);
          return;
        }

        // Cache section data
        sections?.forEach(sec => {
          this.sectionMap.set(sec.id, sec.name);
        });

        // Get unique subjects
        const uniqueSubjectIds = [...new Set(sections?.map(s => s.subject_id) || [])];
        this.totalSubjects = uniqueSubjectIds.length;
        console.log('✅ Total subjects:', this.totalSubjects);

        // Get subject names for cache
        if (uniqueSubjectIds.length > 0) {
          const { data: subjects } = await supabase
            .from('subjects')
            .select('id, name')
            .in('id', uniqueSubjectIds);

          subjects?.forEach(subj => {
            this.subjectMap.set(subj.id, subj.name);
          });
        }

      } catch (error) {
        console.error('❌ Error loading dashboard stats:', error);
      } finally {
        this.isLoadingStats = false;
      }
    },

    async loadAvailableQuizzes() {
      if (!this.studentRecordId) {
        console.warn('⚠️ Cannot load quizzes: no student record ID');
        return;
      }

      try {
        this.isLoadingAssessments = true;
        console.log('📋 Loading available quizzes...');

        // Ensure we have enrolled sections
        if (this.enrolledSectionIds.length === 0) {
          await this.loadEnrolledSections();
        }

        if (this.enrolledSectionIds.length === 0) {
          console.log('ℹ️ No enrolled sections for quizzes');
          this.recentAssessments = [];
          this.pendingAssessments = 0;
          return;
        }

        // Get all published quizzes for enrolled sections
        const { data: quizzes, error: quizError } = await supabase
          .from('quizzes')
          .select('id, title, description, start_date, end_date, section_id, subject_id, attempts_allowed, status')
          .in('section_id', this.enrolledSectionIds)
          .eq('status', 'published')
          .order('end_date', { ascending: true });

        if (quizError) {
          console.error('❌ Quizzes error:', quizError);
          this.recentAssessments = [];
          this.pendingAssessments = 0;
          return;
        }

        if (!quizzes || quizzes.length === 0) {
          console.log('ℹ️ No published quizzes');
          this.recentAssessments = [];
          this.pendingAssessments = 0;
          return;
        }

        console.log('✅ Quizzes found:', quizzes.length);

        // Get quiz attempts for this student
        const { data: attempts, error: attemptsError } = await supabase
          .from('quiz_attempts')
          .select('quiz_id, attempt_number, status, submitted_at')
          .eq('student_id', this.studentRecordId);

        if (attemptsError) {
          console.error('❌ Attempts error:', attemptsError);
        }

        // Build attempt map
        const attemptMap = {};
        if (attempts) {
          attempts.forEach(attempt => {
            if (!attemptMap[attempt.quiz_id]) {
              attemptMap[attempt.quiz_id] = [];
            }
            attemptMap[attempt.quiz_id].push(attempt);
          });
        }

        // Process quizzes
        const nowDate = new Date();
        let pendingCount = 0;
        const processedQuizzes = [];

        for (const quiz of quizzes) {
          try {
            const startDate = quiz.start_date ? new Date(quiz.start_date) : null;
            const endDate = quiz.end_date ? new Date(quiz.end_date) : null;
            const quizAttempts = attemptMap[quiz.id] || [];
            
            const isAvailable = (!startDate || startDate <= nowDate) && (!endDate || endDate >= nowDate);
            
            let status = 'pending';
            let canTakeQuiz = false;

            const completedAttempts = quizAttempts.filter(a => 
              a.status === 'submitted' || a.status === 'graded' || a.status === 'reviewed'
            ).length;

            const hasInProgress = quizAttempts.some(a => a.status === 'in_progress');

            // Determine status
            if (hasInProgress) {
              status = 'in-progress';
              canTakeQuiz = true;
            } else if (completedAttempts >= quiz.attempts_allowed) {
              status = 'completed';
              canTakeQuiz = false;
            } else if (endDate && endDate < nowDate) {
              status = 'overdue';
              canTakeQuiz = false;
            } else if (isAvailable) {
              status = 'available';
              canTakeQuiz = true;
            } else if (startDate && startDate > nowDate) {
              status = 'upcoming';
              canTakeQuiz = false;
            }

            // Count pending
            if (status === 'available' || status === 'in-progress') {
              pendingCount++;
            }

            processedQuizzes.push({
              id: quiz.id,
              title: quiz.title || 'Untitled Quiz',
              subject: this.subjectMap.get(quiz.subject_id) || 'Unknown Subject',
              section: this.sectionMap.get(quiz.section_id) || 'Unknown Section',
              startDate: startDate,
              dueDate: endDate,
              status: status,
              canTake: canTakeQuiz,
              attemptsUsed: completedAttempts,
              attemptsAllowed: quiz.attempts_allowed,
              type: 'quiz'
            });

          } catch (err) {
            console.error('⚠️ Error processing quiz:', err);
          }
        }

        // Sort and limit to 5
        this.recentAssessments = processedQuizzes
          .sort((a, b) => {
            const statusPriority = {
              'in-progress': 1,
              'available': 2,
              'upcoming': 3,
              'overdue': 4,
              'completed': 5
            };
            
            if (statusPriority[a.status] !== statusPriority[b.status]) {
              return statusPriority[a.status] - statusPriority[b.status];
            }
            
            if (a.dueDate && b.dueDate) {
              return a.dueDate.getTime() - b.dueDate.getTime();
            }
            return 0;
          })
          .slice(0, 5);

        this.pendingAssessments = pendingCount;
        console.log('✅ Assessments loaded - Pending:', pendingCount, 'Total:', processedQuizzes.length);

      } catch (error) {
        console.error('❌ Error loading available quizzes:', error);
        this.recentAssessments = [];
        this.pendingAssessments = 0;
      } finally {
        this.isLoadingAssessments = false;
      }
    },

    async loadNotifications() {
      if (!this.studentRecordId || this.isLoadingNotifications) {
        return;
      }

      try {
        this.isLoadingNotifications = true;
        console.log('🔔 Loading notifications...');

        if (this.enrolledSectionIds.length === 0) {
          this.notifications = [];
          this.unreadNotifications = 0;
          return;
        }

        const notifications = [];
        
        // Check last read timestamp
        const readKey = `notif_read_${this.studentRecordId}`;
        const lastReadTime = localStorage.getItem(readKey);
        const lastRead = lastReadTime ? new Date(lastReadTime) : new Date(0);
        
        // Get recent messages
        const { data: messages } = await supabase
          .from('messages')
          .select('id, message_text, message_type, sent_at, section_id')
          .eq('recipient_id', this.studentRecordId)
          .order('sent_at', { ascending: false })
          .limit(5);

        // Process messages
        if (messages?.length > 0) {
          for (const msg of messages) {
            const sentAt = new Date(msg.sent_at);
            notifications.push({
              id: `msg-${msg.id}`,
              title: msg.message_type === 'announcement' ? '📢 New Announcement' : '💬 New Message',
              body: msg.message_text?.substring(0, 80) + (msg.message_text?.length > 80 ? '...' : ''),
              date: sentAt.toLocaleString(),
              type: 'message',
              rawDate: sentAt,
              isUnread: sentAt > lastRead
            });
          }
        }

        // Get urgent quizzes (due within 3 days)
        const in3Days = new Date(Date.now() + 3 * 24 * 60 * 60 * 1000).toISOString();
        
        const { data: urgentQuizzes } = await supabase
          .from('quizzes')
          .select('id, title, end_date, section_id, created_at')
          .in('section_id', this.enrolledSectionIds)
          .eq('status', 'published')
          .gte('end_date', new Date().toISOString())
          .lte('end_date', in3Days)
          .limit(5);

        if (urgentQuizzes?.length > 0) {
          // Get completed quiz IDs
          const { data: completedAttempts } = await supabase
            .from('quiz_attempts')
            .select('quiz_id')
            .eq('student_id', this.studentRecordId)
            .in('status', ['submitted', 'graded', 'reviewed']);

          const completedIds = new Set(completedAttempts?.map(a => a.quiz_id) || []);

          for (const quiz of urgentQuizzes) {
            if (!completedIds.has(quiz.id)) {
              const createdAt = new Date(quiz.created_at);
              const endDate = new Date(quiz.end_date);
              notifications.push({
                id: `quiz-${quiz.id}`,
                title: '⏰ Quiz Due Soon',
                body: `${quiz.title} - Due: ${endDate.toLocaleDateString()}`,
                date: endDate.toLocaleString(),
                type: 'quiz',
                rawDate: endDate,
                isUnread: createdAt > lastRead
              });
            }
          }
        }

        // Sort by date and take top 10
        this.notifications = notifications
          .sort((a, b) => b.rawDate.getTime() - a.rawDate.getTime())
          .slice(0, 10);

        // Count unread
        this.unreadNotifications = this.notifications.filter(n => n.isUnread).length;

        console.log('✅ Notifications loaded:', this.notifications.length, 'Unread:', this.unreadNotifications);

      } catch (error) {
        console.error('❌ Error loading notifications:', error);
        this.notifications = [];
        this.unreadNotifications = 0;
      } finally {
        this.isLoadingNotifications = false;
      }
    },

    // ==================== Formatting Methods ====================
    
    formatDate(date) {
      if (!date) return '';
      const d = typeof date === 'string' ? new Date(date) : date;
      
      if (isNaN(d.getTime())) return '';
      
      const now = new Date();
      const diffMs = d.getTime() - now.getTime();
      const diffDays = Math.ceil(diffMs / (1000 * 60 * 60 * 24));

      if (diffDays === 0) {
        return 'Today';
      } else if (diffDays === 1) {
        return 'Tomorrow';
      } else if (diffDays === -1) {
        return 'Yesterday';
      } else if (diffDays > 1 && diffDays <= 7) {
        return `In ${diffDays} days`;
      } else if (diffDays < -1 && diffDays >= -7) {
        return `${Math.abs(diffDays)} days ago`;
      }
      
      return d.toLocaleDateString('en-US', {
        month: 'short',
        day: 'numeric',
        year: d.getFullYear() !== now.getFullYear() ? 'numeric' : undefined
      });
    },

    formatStatus(status) {
      if (!status) return '';
      return status
        .replace(/([a-z])([A-Z])/g, '$1 $2')
        .replace(/-/g, ' ')
        .toLowerCase()
        .replace(/\b\w/g, l => l.toUpperCase());
    },

    getStatusClass(status) {
      if (!status) return '';
      const lowerStatus = status.toLowerCase();
      
      if (lowerStatus.includes('progress') || lowerStatus.includes('available') || lowerStatus.includes('pending')) {
        return 'actionable';
      } else if (lowerStatus.includes('completed') || lowerStatus.includes('finished')) {
        return 'completed';
      }
      return 'default';
    },

    // ==================== Real-time Subscriptions ====================

    setupRealtimeSubscriptions() {
      if (!this.userId || !this.studentRecordId) {
        console.warn('⚠️ Cannot setup subscriptions: missing userId or studentRecordId');
        return;
      }

      console.log('🔄 Setting up real-time subscriptions...');
      this.cleanupSubscriptions();

      try {
        // Messages subscription
        const messagesSub = supabase
          .channel('student_messages')
          .on(
            'postgres_changes',
            {
              event: '*',
              schema: 'public',
              table: 'messages'
            },
            (payload) => {
              const msg = payload.new || payload.old;
              if (msg.recipient_id === this.studentRecordId) {
                console.log('📨 New message received');
                this.loadNotifications();
              }
            }
          )
          .subscribe((status) => {
            console.log('Messages subscription status:', status);
          });

        // Quizzes subscription
        const quizSub = supabase
          .channel('student_quizzes')
          .on(
            'postgres_changes',
            {
              event: '*',
              schema: 'public',
              table: 'quizzes'
            },
            (payload) => {
              const quiz = payload.new || payload.old;
              if (this.enrolledSectionIds.includes(quiz.section_id)) {
                console.log('📝 Quiz updated');
                this.loadAvailableQuizzes();
              }
            }
          )
          .subscribe((status) => {
            console.log('Quizzes subscription status:', status);
          });

        this.subscriptions = [messagesSub, quizSub];
        console.log('✅ Real-time subscriptions established');

      } catch (error) {
        console.error('❌ Error setting up subscriptions:', error);
      }
    },

    cleanupSubscriptions() {
      if (this.subscriptions && this.subscriptions.length > 0) {
        console.log('🧹 Cleaning up subscriptions');
        this.subscriptions.forEach(sub => {
          if (sub && typeof sub.unsubscribe === 'function') {
            sub.unsubscribe();
          }
        });
        this.subscriptions = [];
      }
    }
  },

  // ==================== Lifecycle Hooks ====================

  async mounted() {
    console.log('🚀 StudentHome component mounted');
    
    // Add click outside listener
    document.addEventListener('click', this.handleClickOutside);
    
    try {
      // Step 1: Load student profile (critical path)
      const profileLoaded = await this.loadStudentProfile();
      
      if (!profileLoaded || !this.studentRecordId) {
        console.error('❌ Failed to load student profile');
        return;
      }

      // Step 2: Load enrolled sections in parallel with stats
      await Promise.all([
        this.loadEnrolledSections(),
        this.loadDashboardStats()
      ]);

      // Step 3: Load assessments and notifications
      await Promise.all([
        this.loadAvailableQuizzes(),
        this.loadNotifications()
      ]);

      // Step 4: Setup real-time subscriptions
      if (this.userId && this.studentRecordId) {
        this.setupRealtimeSubscriptions();
      }

      // Step 5: Setup polling for notifications (every 5 minutes)
      this.pollInterval = setInterval(() => {
        if (this.studentRecordId) {
          this.loadNotifications();
        }
      }, 300000);

      console.log('✅ Dashboard fully loaded and ready');

    } catch (error) {
      console.error('❌ Critical error during mount:', error);
    }
  },

  beforeUnmount() {
    console.log('🛑 StudentHome component unmounting');
    
    document.removeEventListener('click', this.handleClickOutside);
    
    if (this.pollInterval) {
      clearInterval(this.pollInterval);
    }
    
    this.cleanupSubscriptions();
  }
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

/* Floating Help & Support Button */
.floating-help-btn {
  position: fixed;
  bottom: 2rem;
  right: 2rem;
  width: 60px;
  height: 60px;
  border-radius: 50%;
  background: linear-gradient(135deg, #3D8D7A 0%, #2f6b5c 100%);
  color: white;
  border: none;
  box-shadow: 0 4px 20px rgba(61, 141, 122, 0.3);
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease;
  z-index: 999;
  animation: pulse-help 2s ease-in-out infinite;
}

.dark .floating-help-btn {
  background: linear-gradient(135deg, #20c997 0%, #3D8D7A 100%);
  box-shadow: 0 4px 20px rgba(32, 201, 151, 0.4);
}

@keyframes pulse-help {
  0%, 100% {
    transform: scale(1);
    box-shadow: 0 4px 20px rgba(61, 141, 122, 0.3);
  }
  50% {
    transform: scale(1.05);
    box-shadow: 0 6px 30px rgba(61, 141, 122, 0.5);
  }
}

.floating-help-btn:hover {
  transform: scale(1.1) !important;
  box-shadow: 0 6px 30px rgba(61, 141, 122, 0.5);
}

.dark .floating-help-btn:hover {
  box-shadow: 0 6px 30px rgba(32, 201, 151, 0.6);
}

.floating-help-btn:active {
  transform: scale(0.95) !important;
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
  justify-content: center;
  align-items: center;
  z-index: 1000;
  padding: 20px;
  backdrop-filter: blur(4px);
}

.modal-content {
  background: white;
  border-radius: 16px;
  width: 100%;
  max-width: 500px;
  max-height: 90vh;
  overflow-y: auto;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
  color: #1f2937;
  border: 1px solid #A3D1C6;
}

.modal-content::-webkit-scrollbar {
  width: 6px;
}

.modal-content::-webkit-scrollbar-track {
  background: #f3f4f6;
  border-radius: 3px;
}
.dark .modal-content::-webkit-scrollbar-track {
  background: #374151;
}

.modal-content::-webkit-scrollbar-thumb {
  background: #3D8D7A;
  border-radius: 3px;
}
.dark .modal-content::-webkit-scrollbar-thumb {
  background: #20c997;
}

.dark .modal-content {
  background: #23272b;
  border: 1px solid #20c997;
  box-shadow: 0 2px 8px rgba(0,0,0,0.25);
  color: #A3D1C6;
}

.document-modal {
  max-width: 700px;
}

.modal-header {
  padding: 1.5rem;
  border-bottom: 1px solid #A3D1C6;
  display: flex;
  justify-content: space-between;
  align-items: center;
  position: sticky;
  top: 0;
  background: white;
  border-radius: 12px 12px 0 0;
  z-index: 10;
}

.dark .modal-header {
  background: #2a2e36;
  border-bottom: 1px solid #3D8D7A;
}

.modal-header h3 {
  margin: 0;
  font-size: 1.2rem;
  color: #3D8D7A;
  font-weight: 600;
}

.dark .modal-header h3 {
  color: #A3D1C6;
}

.close-btn {
  background: none;
  border: none;
  font-size: 1.5rem;
  color: #6b7280;
  cursor: pointer;
  line-height: 1;
  padding: 0;
  width: 30px;
  height: 30px;
  transition: color 0.2s;
}

.close-btn:hover {
  color: #1f2937;
}

.dark .close-btn:hover {
  color: #A3D1C6;
}

.modal-body {
  padding: 1.5rem;
}

.document-body {
  max-height: 60vh;
  overflow-y: auto;
}

.document-body::-webkit-scrollbar {
  width: 6px;
}

.document-body::-webkit-scrollbar-track {
  background: #f3f4f6;
  border-radius: 3px;
}
.dark .document-body::-webkit-scrollbar-track {
  background: #374151;
}

.document-body::-webkit-scrollbar-thumb {
  background: #3D8D7A;
  border-radius: 3px;
}
.dark .document-body::-webkit-scrollbar-thumb {
  background: #20c997;
}

.document-content {
  line-height: 1.6;
}

.document-content h4 {
  font-size: 1.4rem;
  color: #3D8D7A;
  margin: 0 0 0.5rem 0;
  font-weight: 600;
}

.dark .document-content h4 {
  color: #A3D1C6;
}

.document-date {
  color: #6b7280;
  font-style: italic;
  margin: 0 0 2rem 0;
  font-size: 0.875rem;
}

.dark .document-date {
  color: #9ca3af;
}

.document-content section {
  margin-bottom: 1.5rem;
}

.document-content h5 {
  font-size: 1.1rem;
  color: #1f2937;
  margin: 1rem 0 0.5rem 0;
  font-weight: 600;
}

.dark .document-content h5 {
  color: #e5e7eb;
}

.document-content p {
  margin: 0 0 1rem 0;
  color: #1f2937;
  font-size: 0.9rem;
}

.dark .document-content p {
  color: #e5e7eb;
}

.document-content ul {
  margin: 0 0 1rem 1.5rem;
}

.document-content li {
  margin-bottom: 0.5rem;
  color: #1f2937;
  font-size: 0.9rem;
}

.dark .document-content li {
  color: #e5e7eb;
}

.modal-footer {
  padding: 1.5rem;
  border-top: 1px solid #A3D1C6;
  display: flex;
  justify-content: flex-end;
  gap: 1rem;
  position: sticky;
  bottom: 0;
  background: white;
  border-radius: 0 0 12px 12px;
}

.dark .modal-footer {
  background: #2a2e36;
  border-top: 1px solid #3D8D7A;
}

.btn-primary {
  padding: 0.75rem 1.5rem;
  border-radius: 8px;
  font-size: 0.9rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s;
  border: none;
  background: #3D8D7A;
  color: white;
}

.btn-primary:hover {
  background: #2f6b5c;
  transform: translateY(-1px);
}

.home-container {
  min-height: 100vh;
  background: #FBFFE4;
  padding: 1.5rem;
  font-family: 'Inter', sans-serif;
}
.dark .home-container {
  background: #181c20;
}

/* Header */
.header-card {
  background: white;
  border-radius: 16px;
  border: 2px solid #A3D1C6;
  padding: 1.5rem;
  margin-bottom: 1.5rem;
  box-shadow: 0 2px 8px rgba(61, 141, 122, 0.08);
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

/* Notification */
.notif-wrapper {
  position: relative;
}

.notif-btn {
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
  position: relative;
  color: #3D8D7A;
}
.dark .notif-btn {
  background: #23272b;
  border-color: #3D8D7A;
  color: #A3D1C6;
}

.notif-btn:hover {
  background: #A3D1C6;
  transform: scale(1.05);
}

.notif-badge {
  position: absolute;
  top: -4px;
  right: -4px;
  background: #ef4444;
  color: white;
  font-size: 0.75rem;
  font-weight: 600;
  padding: 0.125rem 0.375rem;
  border-radius: 999px;
  min-width: 20px;
  text-align: center;
}

.notif-dropdown {
  position: absolute;
  top: 60px;
  right: 0;
  width: 320px;
  max-height: 400px;
  background: white;
  border-radius: 12px;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
  overflow-y: auto;
  z-index: 1000;
  border: 1px solid #e5e7eb;
}
.dark .notif-dropdown {
  background: #23272b;
  border-color: #3D8D7A;
  box-shadow: 0 8px 24px rgba(0,0,0,0.35);
}

.notif-dropdown::-webkit-scrollbar {
  width: 6px;
}

.notif-dropdown::-webkit-scrollbar-track {
  background: #f3f4f6;
  border-radius: 3px;
}
.dark .notif-dropdown::-webkit-scrollbar-track {
  background: #374151;
}

.notif-dropdown::-webkit-scrollbar-thumb {
  background: #3D8D7A;
  border-radius: 3px;
}
.dark .notif-dropdown::-webkit-scrollbar-thumb {
  background: #20c997;
}

.notif-backdrop {
  display: none;
}

.notif-content {
  position: relative;
  z-index: 1001;
}

.notif-header {
  padding: 1rem 1.25rem;
  font-weight: 600;
  color: #1f2937;
  border-bottom: 1px solid #e5e7eb;
  position: sticky;
  top: 0;
  background: white;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.dark .notif-header {
  color: #A3D1C6;
  background: #23272b;
  border-bottom: 1px solid #3D8D7A;
}

.close-notif-btn {
  background: none;
  border: none;
  color: #6b7280;
  cursor: pointer;
  padding: 0.25rem;
  border-radius: 4px;
  transition: all 0.2s ease;
  display: flex;
  align-items: center;
  justify-content: center;
}

.close-notif-btn:hover {
  background: #f3f4f6;
  color: #1f2937;
}

.dark .close-notif-btn {
  color: #9ca3af;
}

.dark .close-notif-btn:hover {
  background: #374151;
  color: #e5e7eb;
}

.notif-empty {
  padding: 2rem 1.25rem;
  text-align: center;
  color: #9ca3af;
  font-size: 0.875rem;
}
.dark .notif-empty {
  color: #A3D1C6;
}

.notif-item {
  padding: 1rem 1.25rem;
  border-bottom: 1px solid #f3f4f6;
  transition: background 0.2s;
  cursor: pointer;
}
.dark .notif-item {
  border-bottom: 1px solid #232a2f;
}

.notif-item:hover {
  background: #f9fafb;
}
.dark .notif-item:hover {
  background: #23272b;
}

.notif-item:last-child {
  border-bottom: none;
}

.notif-title {
  font-weight: 600;
  color: #1f2937;
  font-size: 0.875rem;
  margin-bottom: 0.25rem;
}
.dark .notif-title {
  color: #A3D1C6;
}

.notif-body {
  font-size: 0.813rem;
  color: #6b7280;
  margin-bottom: 0.375rem;
}
.dark .notif-body {
  color: #A3D1C6;
}

.notif-date {
  font-size: 0.75rem;
  color: #9ca3af;
}
.dark .notif-date {
  color: #A3D1C6;
}

/* Stats Grid */
.stats-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1rem;
  margin-bottom: 1.5rem;
}

.stat-card {
  background: white;
  border-radius: 12px;
  padding: 1.25rem;
  display: flex;
  align-items: center;
  gap: 1rem;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
}
.dark .stat-card {
  background: #23272b;
  border: 1px solid #20c997;
  box-shadow: 0 2px 8px rgba(0,0,0,0.25);
}

.stat-icon {
  width: 48px;
  height: 48px;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  flex-shrink: 0;
}

.stat-subjects { background: #3D8D7A; }
.stat-pending { background: #A3D1C6; }

.stat-number {
  font-size: 1.875rem;
  font-weight: 700;
  color: #1f2937;
  line-height: 1;
}
.dark .stat-number {
  color: #A3D1C6;
}

.stat-label {
  font-size: 0.813rem;
  color: #6b7280;
  margin-top: 0.25rem;
  font-weight: 500;
}
.dark .stat-label {
  color: #A3D1C6;
}

/* Content Grid */
.content-grid {
  display: grid;
  grid-template-columns: 1.5fr 1fr;
  gap: 1.5rem;
}


.content-card {
  background: white;
  border-radius: 12px;
  padding: 1.5rem;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
  display: flex;
  flex-direction: column;
  border: 2px solid #A3D1C6;
}

.content-card:first-child {
  max-height: 500px;
}

.content-card:last-child {
  height: fit-content;
  max-height: 280px;
}
.dark .content-card {
  background: #23272b;
  border: 2px solid #20c997;
  box-shadow: 0 2px 8px rgba(0,0,0,0.25);
}

.card-header {
  margin-bottom: 1.25rem;
}

.card-header h3 {
  font-size: 1.125rem;
  font-weight: 600;
  color: #1f2937;
  margin-bottom: 0.25rem;
}
.dark .card-header h3 {
  color: #A3D1C6;
}

.card-desc {
  font-size: 0.813rem;
  color: #6b7280;
}
.dark .card-desc {
  color: #A3D1C6;
}

/* Assessment List */
.assessment-list {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
  overflow-y: auto;
  flex: 1;
}

.assessment-list::-webkit-scrollbar {
  width: 6px;
}

.assessment-list::-webkit-scrollbar-track {
  background: #f3f4f6;
  border-radius: 3px;
}
.dark .assessment-list::-webkit-scrollbar-track {
  background: #374151;
}

.assessment-list::-webkit-scrollbar-thumb {
  background: #3D8D7A;
  border-radius: 3px;
}
.dark .assessment-list::-webkit-scrollbar-thumb {
  background: #20c997;
}

.assessment-item {
  background: #FBFFE4;
  border-radius: 10px;
  padding: 1rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  transition: all 0.2s;
  border: 1px solid #A3D1C6;
}
.dark .assessment-item {
  background: #23272b;
  border-color: #20c997;
}

.assessment-item:hover {
  background: #A3D1C6;
  border-color: #3D8D7A;
}
.dark .assessment-item:hover {
  background: #23272b;
  border-color: #A3D1C6;
}

.assessment-info h4 {
  font-size: 0.938rem;
  font-weight: 600;
  color: #1f2937;
  margin-bottom: 0.25rem;
}
.dark .assessment-info h4 {
  color: #A3D1C6;
}

.assessment-class {
  font-size: 0.813rem;
  color: #6b7280;
  margin-bottom: 0.25rem;
}
.dark .assessment-class {
  color: #A3D1C6;
}

.assessment-progress {
  font-size: 0.75rem;
  color: #3D8D7A;
  font-weight: 500;
}
.dark .assessment-progress {
  color: #A3D1C6;
}

/* Assessment Due and Status */
.assessment-due {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  justify-content: flex-end;
}

.due-date {
  font-size: 0.875rem;
  font-weight: 600;
  color: #1f2937;
}
.dark .due-date {
  color: #A3D1C6;
}

.status {
  padding: 0.25rem 0.75rem;
  border-radius: 6px;
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  white-space: nowrap;
}

.status.actionable {
  background: #fef3c7;
  color: #d97706;
  border: 1px solid #fbbf24;
}
.dark .status.actionable {
  background: #451a03;
  color: #fbbf24;
  border-color: #d97706;
}

.status.completed {
  background: #d1fae5;
  color: #059669;
  border: 1px solid #10b981;
}
.dark .status.completed {
  background: #022c22;
  color: #34d399;
  border-color: #059669;
}

.status.default {
  background: #f3f4f6;
  color: #6b7280;
  border: 1px solid #d1d5db;
}
.dark .status.default {
  background: #374151;
  color: #9ca3af;
  border-color: #4b5563;
}

.grade-btn {
  background: #20c997;
  color: #181c20;
  border: 1px solid #A3D1C6;
  padding: 0.5rem 1.25rem;
  border-radius: 8px;
  font-size: 0.875rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s;
}
.dark .grade-btn {
  background: #20c997;
  color: #181c20;
  border: 1px solid #A3D1C6;
}

.grade-btn:hover {
  background: #A3D1C6;
  color: #23272b;
  border-color: #20c997;
  transform: translateY(-1px);
}
.dark .grade-btn:hover {
  background: #A3D1C6;
  color: #23272b;
  border-color: #20c997;
}

.empty-state {
  text-align: center;
  color: #9ca3af;
  padding: 2rem;
  font-size: 0.875rem;
}
.dark .empty-state {
  color: #A3D1C6;
}

/* Quick Links */

.quick-links {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0.5rem;
}

.quick-links::-webkit-scrollbar {
  width: 6px;
}

.quick-links::-webkit-scrollbar-track {
  background: #f3f4f6;
  border-radius: 3px;
}
.dark .quick-links::-webkit-scrollbar-track {
  background: #374151;
}

.quick-links::-webkit-scrollbar-thumb {
  background: #3D8D7A;
  border-radius: 3px;
}
.dark .quick-links::-webkit-scrollbar-thumb {
  background: #20c997;
}

.quick-link {
  background: #FBFFE4;
  border: 1px solid #A3D1C6;
  border-radius: 10px;
  padding: 0.75rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.4rem;
  cursor: pointer;
  transition: all 0.2s;
  text-decoration: none;
  color: #1f2937;
  font-weight: 500;
  font-size: 0.8rem;
  height: fit-content;
  min-height: 80px;
}
.dark .quick-link {
  background: #23272b;
  border-color: #20c997;
  color: #A3D1C6;
}

.quick-link:hover {
  background: #A3D1C6;
  color: #181c20;
  border-color: #3D8D7A;
  transform: translateY(-2px);
}
.dark .quick-link:hover {
  background: #A3D1C6;
  color: #23272b;
  border-color: #20c997;
}

.quick-link svg {
  color: #20c997;
}
.dark .quick-link svg {
  color: #A3D1C6;
}

/* Quick Actions */
.quick-actions {
  margin-top: 1.5rem;
}

.actions-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
  gap: 1rem;
}

.action-card {
  background: #FBFFE4;
  border: 1px solid #A3D1C6;
  border-radius: 10px;
  padding: 1.25rem;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  transition: all 0.2s;
  text-decoration: none;
  color: #1f2937;
  font-weight: 500;
}
.dark .action-card {
  background: #23272b;
  border-color: #20c997;
  color: #A3D1C6;
}

.action-card:hover {
  background: #20c997;
  color: #181c20;
  border-color: #A3D1C6;
  transform: translateY(-2px);
}
.dark .action-card:hover {
  background: #A3D1C6;
  color: #23272b;
  border-color: #20c997;
}

.action-icon {
  width: 36px;
  height: 36px;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  flex-shrink: 0;
  margin-bottom: 0.5rem;
}

.action-icon i {
  font-size: 1.5rem;
}
.dark .action-icon i {
  color: #A3D1C6;
}

.action-content h3 {
  font-size: 1rem;
  font-weight: 600;
  margin-bottom: 0.25rem;
}
.dark .action-content h3 {
  color: #A3D1C6;
}

.action-content p {
  font-size: 0.875rem;
  color: #6b7280;
}
.dark .action-content p {
  color: #A3D1C6;
}

/* Responsive */
@media (max-width: 1024px) {
  .content-grid {
    grid-template-columns: 1fr;
    gap: 1.5rem;
  }
}

@media (max-width: 768px) {
  .home-container {
    padding: 0;
    min-height: calc(100vh - 150px);
    margin-bottom: 0;
  }

  /* Header adjustments for mobile */
  .header-card {
    margin: 1rem;
    margin-bottom: 1.5rem;
    padding: 1rem;
    border-radius: 12px;
  }

  .header-content {
    flex-direction: column;
    align-items: flex-start;
    gap: 1rem;
  }

  .header-left {
    width: 100%;
  }

  .user-icon {
    width: 50px;
    height: 50px;
  }

  .header-title {
    font-size: 1.25rem;
    margin-bottom: 0.25rem;
  }

  .header-subtitle {
    font-size: 0.9rem;
  }

  /* Notification improvements for mobile */
  .notif-wrapper {
    width: 100%;
    display: flex;
    justify-content: flex-end;
  }

  .notif-btn {
    padding: 0.75rem;
    border-radius: 12px;
  }

  .notif-dropdown {
    position: fixed;
    top: 120px;
    right: 1rem;
    left: 1rem;
    width: auto;
    max-height: 60vh;
    overflow-y: auto;
    border-radius: 16px;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.15);
    z-index: 1001;
  }

  .notif-backdrop {
    display: block;
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(0, 0, 0, 0.3);
    z-index: 999;
    backdrop-filter: blur(2px);
  }

  .notif-content {
    position: relative;
    z-index: 1001;
    background: white;
    border-radius: 16px;
    border: 1px solid #e5e7eb;
    overflow: hidden;
  }

  .dark .notif-content {
    background: #23272b;
    border-color: #3D8D7A;
  }

  /* Stats grid mobile optimization */
  .stats-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 1rem;
    margin: 0 1rem 1.5rem 1rem;
  }

  .stat-card {
    padding: 1rem;
    border-radius: 12px;
    min-height: 80px;
  }

  .stat-icon {
    width: 40px;
    height: 40px;
    margin-bottom: 0.5rem;
  }

  .stat-number {
    font-size: 1.5rem;
    margin-bottom: 0.25rem;
  }

  .stat-label {
    font-size: 0.8rem;
  }

  /* Content grid mobile layout */
  .content-grid {
    grid-template-columns: 1fr;
    gap: 1.5rem;
    margin: 0 1rem;
  }

  .content-card {
    border-radius: 16px;
    padding: 1.25rem;
  }

  .card-header h3 {
    font-size: 1.1rem;
    margin-bottom: 0.5rem;
  }

  .card-desc {
    font-size: 0.85rem;
  }

  /* Assessment list mobile optimization */
  .assessment-list {
    max-height: 300px;
    gap: 0.75rem;
  }

  .assessment-item {
    padding: 1rem;
    border-radius: 12px;
    flex-direction: column;
    align-items: flex-start;
    gap: 0.75rem;
  }

  .assessment-info {
    width: 100%;
  }

  .assessment-info h4 {
    font-size: 1rem;
    margin-bottom: 0.25rem;
  }

  .assessment-class {
    font-size: 0.8rem;
  }

  .assessment-progress {
    font-size: 0.75rem;
  }

  .assessment-due {
    width: 100%;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
  }

  .due-date {
    font-size: 0.8rem;
  }

  .status {
    padding: 0.4rem 0.8rem;
    font-size: 0.75rem;
    border-radius: 8px;
  }

  .grade-btn {
    padding: 0.5rem 1rem;
    font-size: 0.8rem;
    border-radius: 8px;
    margin-top: 0.5rem;
    width: 100%;
  }

  /* Quick links mobile optimization */
  .quick-links {
    gap: 0.75rem;
    padding: 0.5rem 0;
  }

  .quick-link {
    min-width: 140px;
    padding: 1rem;
    border-radius: 12px;
    flex-direction: column;
    gap: 0.5rem;
    text-align: center;
  }

  .quick-link svg {
    width: 24px;
    height: 24px;
  }

  .quick-link span {
    font-size: 0.8rem;
  }

  /* Quick actions mobile layout */
  .actions-grid {
    grid-template-columns: 1fr;
    gap: 1rem;
  }

  .action-card {
    padding: 1.25rem;
    border-radius: 12px;
    flex-direction: row;
    align-items: center;
    gap: 1rem;
  }

  .action-icon {
    width: 50px;
    height: 50px;
    flex-shrink: 0;
  }

  .action-content {
    flex: 1;
    text-align: left;
  }

  .action-content h3 {
    font-size: 1rem;
    margin-bottom: 0.25rem;
  }

  .action-content p {
    font-size: 0.85rem;
  }

  /* Empty state mobile adjustments */
  .empty-state {
    padding: 2rem 1rem;
  }

  .empty-state h3 {
    font-size: 1.1rem;
  }

  .empty-state p {
    font-size: 0.9rem;
  }

  /* Modal adjustments for mobile */
  .modal-overlay {
    padding: 1rem;
  }

  .modal-content {
    margin: 0;
    border-radius: 16px;
    max-height: 80vh;
    overflow-y: auto;
  }

  .document-modal {
    max-width: none;
    width: 100%;
  }

  .modal-header {
    padding: 1.25rem;
    border-radius: 16px 16px 0 0;
  }

  .modal-header h3 {
    font-size: 1.1rem;
  }

  .modal-body {
    padding: 1.25rem;
  }

  .document-content h4 {
    font-size: 1.1rem;
  }

  .document-content h5 {
    font-size: 1rem;
  }

  .document-content p {
    font-size: 0.9rem;
    line-height: 1.6;
  }

  /* Floating help button mobile position */
  .floating-help-btn {
    bottom: 10rem;
    right: 1rem;
    width: 52px;
    height: 52px;
  }
}

@media (max-width: 480px) {
  /* Extra small mobile optimizations */
  .header-card {
    margin: 0.75rem;
    padding: 0.875rem;
  }

  .header-title {
    font-size: 1.125rem;
  }

  .stats-grid {
    margin: 0 0.75rem 1.25rem 0.75rem;
    gap: 0.75rem;
  }

  .stat-card {
    padding: 0.875rem;
    min-height: 70px;
  }

  .stat-number {
    font-size: 1.25rem;
  }

  .stat-label {
    font-size: 0.75rem;
  }

  .content-grid {
    margin: 0 0.75rem;
    gap: 1.25rem;
  }

  .content-card {
    padding: 1rem;
  }

  .assessment-item {
    padding: 0.875rem;
  }

  .quick-link {
    min-width: 120px;
    padding: 0.875rem;
  }

  .action-card {
    padding: 1rem;
  }

  .action-icon {
    width: 45px;
    height: 45px;
  }

  .notif-dropdown {
    top: 75px;
    right: 0.75rem;
    left: 0.75rem;
  }

  /* Notification items mobile touch optimization */
  .notif-item {
    padding: 1rem;
    border-radius: 12px;
    min-height: 60px;
  }

  .notif-title {
    font-size: 0.9rem;
  }

  .notif-body {
    font-size: 0.8rem;
  }

  .floating-help-btn {
    bottom: 10rem;
    right: 0.75rem;
    width: 48px;
    height: 48px;
  }

  .floating-help-btn svg {
    width: 20px;
    height: 20px;
  }
}
</style>