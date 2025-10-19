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
              <span v-if="!isLoadingName">Hello, {{ fullName }}!</span>
              <span v-else>Hello, Loading...</span>
            </h1>
            <p class="header-subtitle">Welcome to your dashboard</p>
          </div>
        </div>
        
        <!-- Notification Bell -->
        <div class="notif-wrapper">
          <button class="notif-btn" @click="toggleNotifDropdown" aria-label="Notifications">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"></path>
              <path d="M13.73 21a2 2 0 0 1-3.46 0"></path>
            </svg>
            <span v-if="notifications.length" class="notif-badge">{{ notifications.length }}</span>
          </button>
          
          <!-- Notification Dropdown -->
          <div v-if="showNotifDropdown" class="notif-dropdown">
            <div class="notif-header">Notifications</div>
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

    <!-- Stats Cards -->
    <div class="stats-grid">
      <div class="stat-card">
        <div class="stat-icon stat-classes">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
            <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path>
            <circle cx="9" cy="7" r="4"></circle>
            <path d="M23 21v-2a4 4 0 0 0-3-3.87"></path>
            <path d="M16 3.13a4 4 0 0 1 0 7.75"></path>
          </svg>
        </div>
        <div>
          <div class="stat-number">{{ totalClasses }}</div>
          <div class="stat-label">Total Classes</div>
        </div>
      </div>

      <div class="stat-card">
        <div class="stat-icon stat-graded">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
            <path d="M22 11.08V12a10 10 0 1 1-5.93-8.66"></path>
            <path d="M22 4L12 14.01l-3-3"></path>
          </svg>
        </div>
        <div>
          <div class="stat-number">{{ gradedToday }}</div>
          <div class="stat-label">Graded Today</div>
        </div>
      </div>

      <div class="stat-card">
        <div class="stat-icon stat-pending">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
            <circle cx="12" cy="12" r="10"></circle>
            <polyline points="12,6 12,12 16,14"></polyline>
          </svg>
        </div>
        <div>
          <div class="stat-number">{{ pendingReviews }}</div>
          <div class="stat-label">Pending Reviews</div>
        </div>
      </div>
    </div>

    <!-- Content Grid -->
    <div class="content-grid">
      <!-- Assessments to Grade -->
      <div class="content-card">
        <div class="card-header">
          <h3>Assessments to Grade</h3>
          <p class="card-desc">Review pending student submissions</p>
        </div>
        <div class="assessment-list">
          <div v-if="assessmentsToGrade.length === 0" class="empty-state">
            No assessments to grade
          </div>
          <div v-for="assessment in assessmentsToGrade" :key="assessment.id" class="assessment-item">
            <div class="assessment-info">
              <h4>{{ assessment.title }}</h4>
              <p class="assessment-class">{{ assessment.className }}</p>
              <p class="assessment-progress">{{ assessment.studentsSubmitted }} / {{ assessment.totalStudents }} submitted</p>
            </div>
            <button @click="gradeAssessment(assessment)" class="grade-btn">Grade</button>
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
          <router-link to="/teacher/subjects" class="quick-link">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M14,2H6A2,2 0 0,0 4,4V20A2,2 0 0,0 6,22H18A2,2 0 0,0 20,20V8L14,2M18,20H6V4H13V9H18V20Z" />
            </svg>
            <span>Make Quiz</span>
          </router-link>
          
          <router-link to="/teacher/upload-assessment" class="quick-link">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M9,16V10H5L12,3L19,10H15V16H9M5,20V18H19V20H5Z" />
            </svg>
            <span>Upload Assessment</span>
          </router-link>
          
          <router-link to="/teacher/subjects" class="quick-link">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path>
              <circle cx="9" cy="7" r="4"></circle>
              <path d="M23 21v-2a4 4 0 0 0-3-3.87"></path>
              <path d="M16 3.13a4 4 0 0 1 0 7.75"></path>
            </svg>
            <span>My Classes</span>
          </router-link>
          
          <router-link to="/teacher/gradebook" class="quick-link">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M19,3H14.82C14.4,1.84 13.3,1 12,1C10.7,1 9.6,1.84 9.18,3H5A2,2 0 0,0 3,5V19A2,2 0 0,0 5,21H19A2,2 0 0,0 21,19V5A2,2 0 0,0 19,3M12,3A1,1 0 0,1 13,4A1,1 0 0,1 12,5A1,1 0 0,1 11,4A1,1 0 0,1 12,3Z" />
            </svg>
            <span>Gradebook</span>
          </router-link>
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
              
              <p><strong>Classes not loading?</strong></p>
              <ul>
                <li>Check your internet connection</li>
                <li>Try refreshing the page</li>
                <li>Clear your browser cache</li>
              </ul>
            </section>

            <section>
              <h5>💡 Getting Started</h5>
              <p><strong>For Teachers:</strong></p>
              <ul>
                <li>Create classes and sections</li>
                <li>Add students to your classes</li>
                <li>Post assignments and grades</li>
                <li>Track student progress</li>
                <li>Manage class materials</li>
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
              <h5>📚 Resources</h5>
              <ul>
                <li>User Guide: Coming soon</li>
                <li>Video Tutorials: Coming soon</li>
                <li>FAQ: Coming soon</li>
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
import { supabase } from '../../supabase.js';

export default {
  name: 'TeacherHome',
  data() {
    return {
      showHelpModal: false,
      fullName: 'Teacher',
      totalClasses: 0,
      gradedToday: 0,
      pendingReviews: 0,
      assessmentsToGrade: [],
      notifications: [],
      pollInterval: null,
      isLoadingName: true,
      userId: null,
      profileId: null,
      teacherId: null,
      showNotifDropdown: false,
      subscriptions: []
    };
  },
  methods: {
    toggleNotifDropdown() {
      this.showNotifDropdown = !this.showNotifDropdown;
    },
    
    openHelpModal() {
      this.showHelpModal = true;
    },
    
    closeHelpModal() {
      this.showHelpModal = false;
    },

    async loadTeacherProfile() {
      try {
        this.isLoadingName = true;
        
        const { data: { user }, error: authError } = await supabase.auth.getUser();
        
        if (authError || !user) {
          console.error('Auth error in Teacher Home:', authError);
          this.$router.push('/login');
          return;
        }

        this.userId = user.id;
        console.log('Loading teacher profile for user:', user.id);

        const { data: profile, error: profileError } = await supabase
          .from('profiles')
          .select('id, full_name, email, role')
          .eq('auth_user_id', user.id)
          .single();

        if (profileError) {
          console.error('Profile error in Teacher Home:', profileError);
          
          if (profileError.code === 'PGRST116') {
            console.warn('No profile found for user in Teacher Home');
            this.fullName = user.email?.split('@')[0] || 'Teacher';
            return;
          }
          
          this.fullName = 'Teacher';
          return;
        }

        console.log('Profile found in Teacher Home:', profile);
        this.profileId = profile.id;

        if (profile.role !== 'teacher') {
          console.warn('User is not a teacher in Teacher Home');
          this.$router.push('/login');
          return;
        }

        const { data: teacherData, error: teacherError } = await supabase
          .from('teachers')
          .select('id, employee_id, full_name, email, department, is_active')
          .eq('profile_id', profile.id)
          .single();

        if (teacherError) {
          console.warn('Teacher data error in Teacher Home:', teacherError);
          
          if (teacherError.code === 'PGRST116') {
            console.log('No teacher record found, creating one...');
            await this.createMissingTeacherRecord(profile);
            return;
          }
          
          this.fullName = profile.full_name || 'Teacher';
          return;
        }

        console.log('Teacher data found in Teacher Home:', teacherData);
        this.teacherId = teacherData.id;
        
        this.fullName = teacherData.full_name || profile.full_name || 'Teacher';
        
        await this.loadDashboardStats();

      } catch (error) {
        console.error('Error loading teacher profile in Teacher Home:', error);
        this.fullName = 'Teacher';
      } finally {
        this.isLoadingName = false;
      }
    },

    async createMissingTeacherRecord(profile) {
      try {
        console.log('Creating missing teacher record for profile:', profile.id);
        
        const employeeId = await this.generateEmployeeId(profile.id);
        
        const { data, error } = await supabase
          .from('teachers')
          .insert([{
            profile_id: profile.id,
            employee_id: employeeId,
            full_name: profile.full_name,
            email: profile.email,
            department: 'General',
            is_active: true
          }])
          .select()
          .single();

        if (error) {
          console.error('Error creating teacher record:', error);
          this.fullName = profile.full_name || 'Teacher';
          return;
        }

        console.log('Created teacher record:', data);
        this.teacherId = data.id;
        this.fullName = data.full_name;
        
        await this.loadDashboardStats();
        
      } catch (error) {
        console.error('Error in createMissingTeacherRecord:', error);
        this.fullName = profile.full_name || 'Teacher';
      }
    },

    async generateEmployeeId(profileId) {
      try {
        const year = new Date().getFullYear();
        const shortId = profileId.slice(-6).toUpperCase();
        const random = Math.floor(Math.random() * 99).toString().padStart(2, '0');
        const employeeId = `T${year}${shortId}${random}`;
        
        const { data: existingTeacher } = await supabase
          .from('teachers')
          .select('employee_id')
          .eq('employee_id', employeeId)
          .single();
        
        if (existingTeacher) {
          return await this.generateEmployeeId(profileId);
        }
        
        console.log('Generated employee ID:', employeeId);
        return employeeId;
      } catch (error) {
        console.error('Error generating employee ID:', error);
        return `T${Date.now().toString().slice(-8)}`;
      }
    },

    async loadDashboardStats() {
      try {
        if (!this.teacherId) {
          console.warn('No teacher ID available for dashboard stats');
          this.totalClasses = 0;
          this.gradedToday = 0;
          this.pendingReviews = 0;
          return;
        }

        // Get total classes (unique subjects taught by this teacher)
        const { data: subjects, error: subjectsError } = await supabase
          .from('subjects')
          .select('id')
          .eq('teacher_id', this.teacherId)
          .eq('is_active', true);

        if (subjectsError) {
          console.error('Error loading teacher subjects:', subjectsError);
        } else {
          this.totalClasses = subjects?.length || 0;
          console.log('Total classes:', this.totalClasses);
        }

        // Get graded today count (quiz attempts graded today)
        const today = new Date();
        today.setHours(0, 0, 0, 0);
        const todayISO = today.toISOString();

        const { data: gradedToday, error: gradedError } = await supabase
          .from('quiz_attempts')
          .select('id, quiz_id!inner(teacher_id)')
          .eq('quiz_id.teacher_id', this.teacherId)
          .eq('status', 'graded')
          .gte('graded_at', todayISO);

        if (gradedError) {
          console.error('Error loading graded today:', gradedError);
          this.gradedToday = 0;
        } else {
          this.gradedToday = gradedToday?.length || 0;
          console.log('Graded today:', this.gradedToday);
        }

        await this.loadAssessmentsToGrade();

      } catch (error) {
        console.error('Error loading dashboard stats:', error);
        this.totalClasses = 0;
        this.gradedToday = 0;
        this.pendingReviews = 0;
      }
    },

    async loadAssessmentsToGrade() {
      try {
        if (!this.teacherId) {
          console.warn('No teacher ID for assessments');
          this.assessmentsToGrade = [];
          this.pendingReviews = 0;
          return;
        }

        // Get all quizzes by this teacher with submitted attempts
        const { data: quizzes, error: quizzesError } = await supabase
          .from('quizzes')
          .select(`
            id,
            title,
            subject_id,
            section_id,
            status,
            subjects!inner(name),
            sections!inner(name)
          `)
          .eq('teacher_id', this.teacherId)
          .eq('status', 'published');

        if (quizzesError) {
          console.error('Error loading quizzes:', quizzesError);
          this.assessmentsToGrade = [];
          this.pendingReviews = 0;
          return;
        }

        // For each quiz, get attempt counts
        const assessmentsWithCounts = await Promise.all(
          (quizzes || []).map(async (quiz) => {
            // Get total enrolled students in this section
            const { data: enrollments, error: enrollError } = await supabase
              .from('enrollments')
              .select('student_id')
              .eq('section_id', quiz.section_id)
              .eq('status', 'active');

            const totalStudents = enrollments?.length || 0;

            // Get submitted attempts count
            const { data: attempts, error: attemptsError } = await supabase
              .from('quiz_attempts')
              .select('id, student_id')
              .eq('quiz_id', quiz.id)
              .eq('status', 'submitted');

            const studentsSubmitted = attempts?.length || 0;

            // Only include if there are submissions to grade
            if (studentsSubmitted > 0) {
              return {
                id: quiz.id,
                title: quiz.title,
                className: `${quiz.subjects.name} - ${quiz.sections.name}`,
                studentsSubmitted: studentsSubmitted,
                totalStudents: totalStudents,
                sectionId: quiz.section_id,
                subjectId: quiz.subject_id
              };
            }
            return null;
          })
        );

        // Filter out null values and sort by most submissions
        this.assessmentsToGrade = assessmentsWithCounts
          .filter(a => a !== null)
          .sort((a, b) => b.studentsSubmitted - a.studentsSubmitted);

        this.pendingReviews = this.assessmentsToGrade.length;

        console.log('Assessments to grade:', this.assessmentsToGrade);

      } catch (error) {
        console.error('Error loading assessments to grade:', error);
        this.assessmentsToGrade = [];
        this.pendingReviews = 0;
      }
    },

    async fetchDashboardStats() {
      console.log('Dashboard stats refresh triggered');
      await this.loadDashboardStats();
    },

    async fetchAssessmentsToGrade() {
      await this.loadAssessmentsToGrade();
    },

    gradeAssessment(assessment) {
      console.log('Grading assessment:', assessment.title);
      // Navigate to grading page
      this.$router.push({
        path: '/teacher/grade-quiz',
        query: {
          quizId: assessment.id,
          sectionId: assessment.sectionId
        }
      });
    },

    async fetchAllData() {
      await Promise.all([
        this.loadDashboardStats(),
        this.loadAssessmentsToGrade()
      ]);
    },

    async loadNotifications() {
      try {
        if (!this.teacherId || !this.profileId) {
          console.warn('No teacher ID or profile ID for notifications');
          return;
        }

        const notifications = [];

        // 1. Get quiz submission notifications (students who submitted quizzes)
        const { data: submissions, error: submissionsError } = await supabase
          .from('quiz_attempts')
          .select(`
            id,
            submitted_at,
            status,
            student_id,
            quiz_id,
            students!inner(full_name),
            quizzes!inner(title, teacher_id)
          `)
          .eq('quizzes.teacher_id', this.teacherId)
          .eq('status', 'submitted')
          .order('submitted_at', { ascending: false })
          .limit(10);

        if (!submissionsError && submissions) {
          submissions.forEach(sub => {
            notifications.push({
              id: `submission-${sub.id}`,
              title: 'New Quiz Submission',
              body: `${sub.students.full_name} submitted "${sub.quizzes.title}"`,
              date: new Date(sub.submitted_at).toLocaleString(),
              type: 'submission',
              created_at: sub.submitted_at
            });
          });
        }

        // 2. Get message notifications (students who sent messages)
        const { data: messages, error: messagesError } = await supabase
          .from('messages')
          .select(`
            id,
            sent_at,
            message_text,
            sender_id,
            section_id,
            sections!inner(
              subject_id,
              subjects!inner(teacher_id)
            )
          `)
          .eq('sections.subjects.teacher_id', this.teacherId)
          .eq('recipient_id', this.teacherId)
          .is('message_reads.id', null)
          .order('sent_at', { ascending: false })
          .limit(5);

        if (!messagesError && messages) {
          for (const msg of messages) {
            // Get student name
            const { data: student } = await supabase
              .from('students')
              .select('full_name')
              .eq('id', msg.sender_id)
              .single();

            if (student) {
              notifications.push({
                id: `message-${msg.id}`,
                title: 'New Message',
                body: `${student.full_name}: ${msg.message_text.substring(0, 50)}${msg.message_text.length > 50 ? '...' : ''}`,
                date: new Date(msg.sent_at).toLocaleString(),
                type: 'message',
                created_at: msg.sent_at
              });
            }
          }
        }

        // 3. Get quiz deadline reminders (quizzes ending in next 24 hours)
        const tomorrow = new Date();
        tomorrow.setHours(tomorrow.getHours() + 24);
        const tomorrowISO = tomorrow.toISOString();

        const { data: endingQuizzes, error: endingError } = await supabase
          .from('quizzes')
          .select(`
            id,
            title,
            end_date,
            sections!inner(name)
          `)
          .eq('teacher_id', this.teacherId)
          .eq('status', 'published')
          .lte('end_date', tomorrowISO)
          .gte('end_date', new Date().toISOString());

        if (!endingError && endingQuizzes) {
          endingQuizzes.forEach(quiz => {
            notifications.push({
              id: `deadline-${quiz.id}`,
              title: 'Quiz Deadline Approaching',
              body: `"${quiz.title}" ends soon in ${quiz.sections.name}`,
              date: new Date(quiz.end_date).toLocaleString(),
              type: 'deadline',
              created_at: quiz.end_date
            });
          });
        }

        // Sort all notifications by date (newest first)
        notifications.sort((a, b) => new Date(b.created_at) - new Date(a.created_at));

        this.notifications = notifications.slice(0, 15); // Keep only 15 most recent

        console.log('Loaded notifications:', this.notifications.length);

      } catch (error) {
        console.error('Error loading notifications:', error);
        this.notifications = [];
      }
    },

    setupRealtimeSubscriptions() {
      if (!this.userId || !this.teacherId) {
        console.warn('Cannot setup subscriptions without user/teacher ID');
        return;
      }

      // Subscribe to profile changes (name updates)
      const profileSubscription = supabase
        .channel('teacher_home_profile_changes')
        .on(
          'postgres_changes',
          {
            event: '*',
            schema: 'public',
            table: 'profiles',
            filter: `auth_user_id=eq.${this.userId}`
          },
          (payload) => {
            console.log('Profile updated in Teacher Home:', payload);
            this.loadTeacherProfile();
          }
        )
        .subscribe();

      // Subscribe to teacher table changes (name updates)
      const teacherSubscription = supabase
        .channel('teacher_home_teacher_changes')
        .on(
          'postgres_changes',
          {
            event: '*',
            schema: 'public',
            table: 'teachers',
            filter: `id=eq.${this.teacherId}`
          },
          (payload) => {
            console.log('Teacher data updated in Teacher Home:', payload);
            if (payload.eventType === 'UPDATE' && payload.new.full_name) {
              this.fullName = payload.new.full_name;
            }
          }
        )
        .subscribe();

      // Subscribe to quiz attempts (new submissions)
      const attemptsSubscription = supabase
        .channel('teacher_home_attempts')
        .on(
          'postgres_changes',
          {
            event: '*',
            schema: 'public',
            table: 'quiz_attempts'
          },
          (payload) => {
            console.log('Quiz attempt change:', payload);
            this.loadDashboardStats();
            this.loadNotifications();
          }
        )
        .subscribe();

      // Subscribe to messages (new messages from students)
      const messagesSubscription = supabase
        .channel('teacher_home_messages')
        .on(
          'postgres_changes',
          {
            event: 'INSERT',
            schema: 'public',
            table: 'messages',
            filter: `recipient_id=eq.${this.teacherId}`
          },
          (payload) => {
            console.log('New message received:', payload);
            this.loadNotifications();
          }
        )
        .subscribe();

      // Subscribe to quizzes changes
      const quizzesSubscription = supabase
        .channel('teacher_home_quizzes')
        .on(
          'postgres_changes',
          {
            event: '*',
            schema: 'public',
            table: 'quizzes',
            filter: `teacher_id=eq.${this.teacherId}`
          },
          (payload) => {
            console.log('Quiz updated:', payload);
            this.loadDashboardStats();
          }
        )
        .subscribe();

      // Subscribe to subjects changes
      const subjectsSubscription = supabase
        .channel('teacher_home_subjects')
        .on(
          'postgres_changes',
          {
            event: '*',
            schema: 'public',
            table: 'subjects',
            filter: `teacher_id=eq.${this.teacherId}`
          },
          (payload) => {
            console.log('Subjects updated:', payload);
            this.loadDashboardStats();
          }
        )
        .subscribe();

      this.subscriptions = [
        profileSubscription,
        teacherSubscription,
        attemptsSubscription,
        messagesSubscription,
        quizzesSubscription,
        subjectsSubscription
      ];

      console.log('Real-time subscriptions setup complete');
    }
  },

  async mounted() {
    console.log('Teacher Home component mounted');
    await this.loadTeacherProfile();
    await this.loadNotifications();
    this.setupRealtimeSubscriptions();
    
    // Poll for updates every 30 seconds as backup
    this.pollInterval = setInterval(() => {
      this.fetchAllData();
      this.loadNotifications();
    }, 30000);
  },

  beforeDestroy() {
    console.log('Teacher Home component being destroyed');
    
    if (this.pollInterval) {
      clearInterval(this.pollInterval);
    }
    
    if (this.subscriptions && this.subscriptions.length > 0) {
      this.subscriptions.forEach(subscription => {
        supabase.removeChannel(subscription);
      });
    }
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

.notif-header {
  padding: 1rem 1.25rem;
  font-weight: 600;
  color: #1f2937;
  border-bottom: 1px solid #e5e7eb;
  position: sticky;
  top: 0;
  background: white;
  border-radius: 12px 12px 0 0;
  z-index: 10;
}
.dark .notif-header {
  color: #A3D1C6;
  background: #23272b;
  border-bottom: 1px solid #3D8D7A;
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
  grid-template-columns: repeat(3, 1fr);
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

.stat-classes { background: #3D8D7A; }
.stat-graded { background: #B3D8A8; }
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
  max-height: 500px;
}
.dark .content-card {
  background: #23272b;
  border: 1px solid #20c997;
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

.assessment-list::-webkit-scrollbar-thumb {
  background: #A3D1C6;
  border-radius: 3px;
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
  gap: 0.75rem;
  overflow-y: auto;
  flex: 1;
}

.quick-links::-webkit-scrollbar {
  width: 6px;
}

.quick-links::-webkit-scrollbar-track {
  background: #f3f4f6;
  border-radius: 3px;
}

.quick-links::-webkit-scrollbar-thumb {
  background: #A3D1C6;
  border-radius: 3px;
}

.quick-link {
  background: #FBFFE4;
  border: 1px solid #A3D1C6;
  border-radius: 10px;
  padding: 1rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.5rem;
  cursor: pointer;
  transition: all 0.2s;
  text-decoration: none;
  color: #1f2937;
  font-weight: 500;
  font-size: 0.875rem;
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
  }
}

@media (max-width: 768px) {
  .stats-grid {
    grid-template-columns: 1fr;
  }
  
  .quick-links {
    grid-template-columns: 1fr;
  }
  
  .header-content {
    flex-direction: column;
    gap: 1rem;
  }
  
  .header-left {
    width: 100%;
  }
  
  .notif-wrapper {
    align-self: flex-end;
  }
  
  .notif-dropdown {
    right: 0;
    left: auto;
    width: calc(100vw - 3rem);
    max-width: 320px;
  }
}
</style>