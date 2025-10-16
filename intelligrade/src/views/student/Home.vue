<template>
  <div class="home-container">
    <!-- Enhanced Header Section -->
    <div class="section-header-card">
      <!-- Background Decorations -->
      <div class="header-bg-decoration"></div>
      <div class="floating-shapes">
        <div class="shape shape-1"></div>
        <div class="shape shape-2"></div>
        <div class="shape shape-3"></div>
      </div>
      
      <div class="section-header-content">
        <div class="section-header-left">
          <div class="section-header-icon">
            <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
              <circle cx="12" cy="7" r="4"></circle>
            </svg>
          </div>
          <div class="header-text">
            <div class="section-header-title">
              <span v-if="!isLoadingName">Hello, {{ studentName }}!</span>
              <span v-else>Hello, Loading...</span>
            </div>
            <div class="section-header-subtitle">Welcome to your student dashboard</div>
            <div class="section-header-description">Track your academic progress and stay on top of your studies</div>
          </div>
        </div>
        
        <div class="header-actions">
          <!-- Active Student Badge -->
          <div class="header-badge" :class="{ 'active-student': isActive, 'inactive-student': !isActive }">
            <div class="badge-content">
              <div class="badge-icon" v-if="isActive">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M12,2A10,10 0 0,1 22,12A10,10 0 0,1 12,22A10,10 0 0,1 2,12A10,10 0 0,1 12,2M11,16.5L18,9.5L16.59,8.09L11,13.67L7.91,10.59L6.5,12L11,16.5Z" />
                </svg>
              </div>
              <div class="badge-icon" v-else>
                <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M12,2A10,10 0 0,1 22,12A10,10 0 0,1 12,22A10,10 0 0,1 2,12A10,10 0 0,1 12,2M12,4A8,8 0 0,0 4,12A8,8 0 0,0 12,20A8,8 0 0,0 20,12A8,8 0 0,0 12,4M12,6A6,6 0 0,1 18,12A6,6 0 0,1 12,18A6,6 0 0,1 6,12A6,6 0 0,1 12,6M12,8A4,4 0 0,0 8,12A4,4 0 0,0 12,16A4,4 0 0,0 16,12A4,4 0 0,0 12,8Z" />
                </svg>
              </div>
              <div class="badge-text">{{ isActive ? 'Active Student' : 'Inactive Student' }}</div>
            </div>
          </div>
          
          <!-- Bell Icon Dropdown -->
          <div class="notif-bell-wrapper">
            <button class="notif-bell-btn" @click="toggleNotifDropdown" aria-label="Notifications">
              <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#4DBB98" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                <path d="M18 16v-5a6 6 0 0 0-12 0v5a2 2 0 0 1-2 2h16a2 2 0 0 1-2-2z"/>
                <path d="M13.73 21a2 2 0 0 1-3.46 0"/>
              </svg>
              <span v-if="notifications.length" class="notif-bell-dot"></span>
            </button>
            <div v-if="showNotifDropdown" class="notif-dropdown">
              <div class="notif-dropdown-header">Notifications</div>
              <div v-if="notifications.length === 0" class="notif-dropdown-empty">No notifications yet.</div>
              <div v-for="notif in notifications" :key="notif.id" class="notif-dropdown-item">
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
        <div class="stat-icon subjects">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
            <path d="M19,3H5C3.9,3 3,3.9 3,5V19C3,20.1 3.9,21 5,21H19C20.1,21 21,20.1 21,19V5C21,3.9 20.1,3 19,3M5,19V5H19V19H5Z" />
          </svg>
        </div>
        <div class="stat-content">
          <div class="stat-number">{{ totalSubjects }}</div>
          <div class="stat-label">ENROLLED SUBJECTS</div>
        </div>
      </div>

      <div class="stat-card">
        <div class="stat-icon assessments">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
            <path d="M14,2H6A2,2 0 0,0 4,4V20A2,2 0 0,0 6,22H18A2,2 0 0,0 20,20V8L14,2M18,20H6V4H13V9H18V20Z" />
          </svg>
        </div>
        <div class="stat-content">
          <div class="stat-number">{{ pendingAssessments }}</div>
          <div class="stat-label">PENDING ASSESSMENTS</div>
        </div>
      </div>
    </div>

    <!-- Main Content Grid -->
    <div class="content-grid">
      <!-- Recent Assessments -->
      <div class="content-card">
        <div class="card-header">
          <h3>
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M14,2H6A2,2 0 0,0 4,4V20A2,2 0 0,0 6,22H18A2,2 0 0,0 20,20V8L14,2M18,20H6V4H13V9H18V20Z" />
            </svg>
            Recent Assessments
          </h3>
          <p class="card-subtitle">Keep track of your upcoming deadlines.</p>
        </div>
        <div class="assessment-list">
          <div v-for="assessment in recentAssessments" :key="assessment.id" class="assessment-item">
            <div class="assessment-info">
              <h4>{{ assessment.title }}</h4>
              <p class="assessment-subject">{{ assessment.subject }}</p>
            </div>
            <div class="assessment-due">
              <span class="due-date">{{ formatDate(assessment.dueDate) }}</span>
              <span :class="['status', assessment.status]">{{ assessment.status }}</span>
            </div>
          </div>
        </div>
      </div>

      <!-- Quick Links -->
      <div class="content-card">
        <div class="card-header">
          <h3>
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M13,9H18.5L13,3.5V9M6,2H14L20,8V20A2,2 0 0,1 18,22H6C4.89,22 4,21.1 4,20V4C4,2.89 4.89,2 6,2M15,18V16H6V18H15M18,14V12H6V14H18Z" />
            </svg>
            Quick Links
          </h3>
          <p class="card-subtitle">Navigate to key features quickly.</p>
        </div>
        <div class="quick-links-grid">
          <button @click="navigateToSubjects" class="quick-link-btn subjects">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M19,3H5C3.9,3 3,3.9 3,5V19C3,20.1 3.9,21 5,21H19C20.1,21 21,20.1 21,19V5C21,3.9 20.1,3 19,3M5,19V5H19V19H5Z" />
            </svg>
            My Subjects
          </button>
          <button @click="navigateToCalendar" class="quick-link-btn calendar">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M19,19H5V8H19M19,3H18V1H16V3H8V1H6V3H5C3.89,3 3,3.89 3,5V19A2,2 0 0,0 5,21H19A2,2 0 0,0 21,19V5C21,3.89 20.1,3 19,3M16.5,13.5H11V18.5H16.5V13.5Z" />
            </svg>
            Calendar
          </button>
          <button @click="navigateToMessages" class="quick-link-btn messages">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M22 6c0-1.1-.9-2-2-2H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6zM4 6h16v.5l-8 5-8-5V6zm0 13.5V8l8 5 8-5v11.5H4z" />
            </svg>
            Messages
          </button>
          <button @click="navigateToSettings" class="quick-link-btn settings">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M12,15.5A3.5,3.5 0 0,1 8.5,12A3.5,3.5 0 0,1 12,8.5A3.5,3.5 0 0,1 15.5,12A3.5,3.5 0 0,1 12,15.5M19.43,12.97C19.47,12.65 19.5,12.33 19.5,12C19.5,11.67 19.47,11.34 19.43,11.03L21.54,9.37C21.73,9.22 21.78,8.96 21.66,8.74L19.65,5.27C19.54,5.05 19.27,4.96 19.05,5.05L16.56,6.05C16.04,5.66 15.5,5.32 14.9,5.07L14.5,2.42C14.46,2.18 14.25,2 14,2H10C9.75,2 9.54,2.18 9.5,2.42L9.1,5.07C8.5,5.32 7.96,5.66 7.44,6.05L4.95,5.05C4.73,4.96 4.46,5.05 4.34,5.27L2.34,8.74C2.21,8.96 2.27,9.22 2.46,9.37L4.57,11.03C4.53,11.34 4.5,11.67 4.5,12C4.5,12.33 4.53,12.65 4.57,12.97L2.46,14.63C2.27,14.78 2.21,15.04 2.34,15.26L4.34,18.73C4.46,18.95 4.73,19.04 4.95,18.95L7.44,17.94C7.96,18.34 8.5,18.68 9.1,18.93L9.5,21.58C9.54,21.82 9.75,22 10,22H14C14.25,22 14.46,21.82 14.5,21.58L14.9,18.93C15.5,18.68 16.04,18.34 16.56,17.94L19.05,18.95C19.27,19.04 19.54,18.95 19.66,18.73L21.66,15.26C21.78,15.04 21.73,14.78 21.54,14.63L19.43,12.97Z" />
            </svg>
            Settings
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { supabase } from '../../supabase.js';

export default {
  name: 'StudentHome',
  data() {
    return {
      studentName: 'Student',
      totalSubjects: 0,
      pendingAssessments: 0,
      recentAssessments: [],
      notifications: [],
      pollInterval: null,
      isLoadingName: true,
      userId: null,
      profileId: null,
      studentRecordId: null,
      showNotifDropdown: false,
      subscriptions: [],
      isActive: false
    };
  },
  methods: {
    toggleNotifDropdown() {
      this.showNotifDropdown = !this.showNotifDropdown;
    },

    async loadNotifications() {
      if (!this.studentRecordId) return;
      
      try {
        const notifications = [];
        
        // Get unread direct messages
        const { data: messages, error: msgError } = await supabase
          .from('messages')
          .select('id, message_text, message_type, sent_at, sender_id, section_id')
          .eq('recipient_id', this.studentRecordId)
          .is('read_at', null)
          .order('sent_at', { ascending: false })
          .limit(5);

        if (!msgError && messages && messages.length > 0) {
          for (const msg of messages) {
            try {
              const { data: section } = await supabase
                .from('sections')
                .select('name, subject_id')
                .eq('id', msg.section_id)
                .single();

              let subjectName = 'Unknown Subject';
              if (section && section.subject_id) {
                const { data: subject } = await supabase
                  .from('subjects')
                  .select('name')
                  .eq('id', section.subject_id)
                  .single();
                subjectName = subject?.name || 'Unknown Subject';
              }

              const sectionName = section?.name || 'Unknown Section';
              const messagePreview = msg.message_text.substring(0, 100);
              const messageSuffix = msg.message_text.length > 100 ? '...' : '';
              
              notifications.push({
                id: `msg-${msg.id}`,
                title: msg.message_type === 'announcement' ? 'New Announcement' : 'New Message',
                body: `${subjectName} - ${sectionName}: ${messagePreview}${messageSuffix}`,
                date: new Date(msg.sent_at).toLocaleString(),
                type: 'message'
              });
            } catch (err) {
              console.error('Error processing message:', err);
            }
          }
        }

        // Get broadcast announcements
        const { data: broadcasts, error: broadcastError } = await supabase
          .from('messages')
          .select('id, message_text, sent_at, section_id')
          .eq('message_type', 'announcement')
          .is('recipient_id', null)
          .order('sent_at', { ascending: false })
          .limit(5);

        if (!broadcastError && broadcasts && broadcasts.length > 0) {
          const { data: enrollments } = await supabase
            .from('enrollments')
            .select('section_id')
            .eq('student_id', this.studentRecordId)
            .eq('status', 'active');

          const enrolledSectionIds = enrollments?.map(e => e.section_id) || [];

          for (const msg of broadcasts) {
            if (enrolledSectionIds.includes(msg.section_id)) {
              try {
                const { data: section } = await supabase
                  .from('sections')
                  .select('name, subject_id')
                  .eq('id', msg.section_id)
                  .single();

                let subjectName = 'Unknown Subject';
                if (section && section.subject_id) {
                  const { data: subject } = await supabase
                    .from('subjects')
                    .select('name')
                    .eq('id', section.subject_id)
                    .single();
                  subjectName = subject?.name || 'Unknown Subject';
                }

                const sectionName = section?.name || 'Unknown Section';
                const messagePreview = msg.message_text.substring(0, 100);
                const messageSuffix = msg.message_text.length > 100 ? '...' : '';
                
                notifications.push({
                  id: `broadcast-${msg.id}`,
                  title: 'Class Announcement',
                  body: `${subjectName} - ${sectionName}: ${messagePreview}${messageSuffix}`,
                  date: new Date(msg.sent_at).toLocaleString(),
                  type: 'announcement'
                });
              } catch (err) {
                console.error('Error processing broadcast:', err);
              }
            }
          }
        }

        // Get available quizzes
        const now = new Date().toISOString();
        const { data: availableQuizzes, error: quizError } = await supabase
          .from('quizzes')
          .select('id, title, start_date, end_date, section_id, subject_id')
          .eq('status', 'published')
          .lte('start_date', now)
          .gte('end_date', now);

        if (!quizError && availableQuizzes && availableQuizzes.length > 0) {
          const { data: enrollments } = await supabase
            .from('enrollments')
            .select('section_id')
            .eq('student_id', this.studentRecordId)
            .eq('status', 'active');

          const enrolledSectionIds = enrollments?.map(e => e.section_id) || [];

          for (const quiz of availableQuizzes) {
            if (enrolledSectionIds.includes(quiz.section_id)) {
              const { data: attempts } = await supabase
                .from('quiz_attempts')
                .select('id, status')
                .eq('quiz_id', quiz.id)
                .eq('student_id', this.studentRecordId);

              const hasCompleted = attempts?.some(a => 
                a.status === 'submitted' || a.status === 'graded' || a.status === 'reviewed'
              );
              
              if (!hasCompleted) {
                try {
                  const { data: section } = await supabase
                    .from('sections')
                    .select('name')
                    .eq('id', quiz.section_id)
                    .single();

                  const { data: subject } = await supabase
                    .from('subjects')
                    .select('name')
                    .eq('id', quiz.subject_id)
                    .single();

                  const sectionName = section?.name || 'Unknown Section';
                  const subjectName = subject?.name || 'Unknown Subject';
                  const dueDate = new Date(quiz.end_date).toLocaleDateString();
                  
                  notifications.push({
                    id: `quiz-${quiz.id}`,
                    title: 'New Quiz Available',
                    body: `${subjectName} - ${quiz.title} in ${sectionName}. Due: ${dueDate}`,
                    date: new Date(quiz.start_date).toLocaleString(),
                    type: 'quiz'
                  });
                } catch (err) {
                  console.error('Error processing quiz notification:', err);
                }
              }
            }
          }
        }

        // Sort by date and limit
        this.notifications = notifications
          .sort((a, b) => {
            const dateA = new Date(a.date);
            const dateB = new Date(b.date);
            return dateB.getTime() - dateA.getTime();
          })
          .slice(0, 10);

      } catch (error) {
        console.error('Error loading notifications:', error);
      }
    },

    setupRealtimeSubscriptions() {
      if (!this.userId || !this.studentRecordId) return;

      const profileSubscription = supabase
        .channel('home_profile_changes')
        .on(
          'postgres_changes',
          {
            event: '*',
            schema: 'public',
            table: 'profiles',
            filter: `auth_user_id=eq.${this.userId}`
          },
          () => {
            this.loadStudentProfile();
          }
        )
        .subscribe();

      const studentSubscription = supabase
        .channel('home_student_changes')
        .on(
          'postgres_changes',
          {
            event: '*',
            schema: 'public',
            table: 'students',
            filter: `id=eq.${this.studentRecordId}`
          },
          () => {
            this.loadStudentProfile();
          }
        )
        .subscribe();

      const quizSubscription = supabase
        .channel('home_quiz_changes')
        .on(
          'postgres_changes',
          {
            event: '*',
            schema: 'public',
            table: 'quizzes'
          },
          () => {
            this.loadAvailableQuizzes();
            this.loadNotifications();
          }
        )
        .subscribe();

      const quizAttemptSubscription = supabase
        .channel('home_quiz_attempt_changes')
        .on(
          'postgres_changes',
          {
            event: '*',
            schema: 'public',
            table: 'quiz_attempts',
            filter: `student_id=eq.${this.studentRecordId}`
          },
          () => {
            this.loadAvailableQuizzes();
          }
        )
        .subscribe();

      const messageSubscription = supabase
        .channel('home_message_changes')
        .on(
          'postgres_changes',
          {
            event: 'INSERT',
            schema: 'public',
            table: 'messages'
          },
          () => {
            this.loadNotifications();
          }
        )
        .subscribe();

      const enrollmentSubscription = supabase
        .channel('home_enrollment_changes')
        .on(
          'postgres_changes',
          {
            event: '*',
            schema: 'public',
            table: 'enrollments',
            filter: `student_id=eq.${this.studentRecordId}`
          },
          () => {
            this.loadDashboardStats();
          }
        )
        .subscribe();

      this.subscriptions = [
        profileSubscription,
        studentSubscription,
        quizSubscription,
        quizAttemptSubscription,
        messageSubscription,
        enrollmentSubscription
      ];
    },

    async loadStudentProfile() {
      try {
        this.isLoadingName = true;
        
        const { data: { user }, error: authError } = await supabase.auth.getUser();
        
        if (authError || !user) {
          console.error('Auth error in Home component:', authError);
          this.studentName = 'Student';
          return;
        }

        this.userId = user.id;

        const { data: profile, error: profileError } = await supabase
          .from('profiles')
          .select('id, full_name, email, role')
          .eq('auth_user_id', user.id)
          .single();

        if (profileError) {
          console.error('Profile error in Home component:', profileError);
          
          if (profileError.code === 'PGRST116') {
            this.studentName = user.email?.split('@')[0] || 'Student';
            return;
          }
          
          this.studentName = 'Student';
          return;
        }

        this.profileId = profile.id;

        if (profile.role !== 'student') {
          console.warn('User is not a student in Home component');
          this.studentName = profile.full_name || 'User';
          return;
        }

        const { data: studentData, error: studentError } = await supabase
          .from('students')
          .select('id, student_id, grade_level, full_name, email, is_active')
          .eq('profile_id', profile.id)
          .single();

        if (studentError) {
          console.warn('Student data error in Home component:', studentError);
          this.studentName = profile.full_name || 'Student';
          return;
        }

        this.studentRecordId = studentData.id;
        this.isActive = studentData.is_active || false;
        this.studentName = studentData.full_name || profile.full_name || 'Student';
        
        await this.loadDashboardStats();

      } catch (error) {
        console.error('Error loading student profile in Home component:', error);
        this.studentName = 'Student';
      } finally {
        this.isLoadingName = false;
      }
    },

    async loadDashboardStats() {
      try {
        if (!this.studentRecordId) {
          console.warn('No student record ID available for dashboard stats');
          return;
        }

        const { data: enrollments, error: enrollmentError } = await supabase
          .from('enrollments')
          .select('section_id, subject_id')
          .eq('student_id', this.studentRecordId)
          .eq('status', 'active');

        if (enrollmentError) {
          console.error('Error loading enrollment stats:', enrollmentError);
        } else {
          const uniqueSubjects = new Set(enrollments?.map(e => e.subject_id) || []);
          this.totalSubjects = uniqueSubjects.size;
          console.log('Total enrolled subjects:', this.totalSubjects);
        }

        await this.loadAvailableQuizzes();

      } catch (error) {
        console.error('Error loading dashboard stats:', error);
      }
    },

    async loadAvailableQuizzes() {
      try {
        if (!this.studentRecordId) return;

        const { data: enrollments, error: enrollError } = await supabase
          .from('enrollments')
          .select('section_id, subject_id')
          .eq('student_id', this.studentRecordId)
          .eq('status', 'active');

        if (enrollError || !enrollments || enrollments.length === 0) {
          this.recentAssessments = [];
          this.pendingAssessments = 0;
          return;
        }

        const sectionIds = enrollments.map(e => e.section_id);

        const { data: quizzes, error: quizError } = await supabase
          .from('quizzes')
          .select('id, title, description, start_date, end_date, section_id, subject_id, attempts_allowed')
          .in('section_id', sectionIds)
          .eq('status', 'published')
          .order('end_date', { ascending: true });

        if (quizError) {
          console.error('Error loading quizzes:', quizError);
          this.recentAssessments = [];
          this.pendingAssessments = 0;
          return;
        }

        if (!quizzes || quizzes.length === 0) {
          this.recentAssessments = [];
          this.pendingAssessments = 0;
          return;
        }

        const { data: attempts, error: attemptsError } = await supabase
          .from('quiz_attempts')
          .select('quiz_id, attempt_number, status, submitted_at')
          .eq('student_id', this.studentRecordId);

        if (attemptsError) {
          console.error('Error loading quiz attempts:', attemptsError);
        }

        const attemptMap = {};
        if (attempts) {
          attempts.forEach(attempt => {
            if (!attemptMap[attempt.quiz_id]) {
              attemptMap[attempt.quiz_id] = [];
            }
            attemptMap[attempt.quiz_id].push(attempt);
          });
        }

        const nowDate = new Date();
        let pendingCount = 0;
        const processedQuizzes = [];

        for (const quiz of quizzes) {
          try {
            const { data: subject } = await supabase
              .from('subjects')
              .select('name')
              .eq('id', quiz.subject_id)
              .single();

            const { data: section } = await supabase
              .from('sections')
              .select('name')
              .eq('id', quiz.section_id)
              .single();

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

            if (status === 'available' || status === 'in-progress') {
              pendingCount++;
            }

            processedQuizzes.push({
              id: quiz.id,
              title: quiz.title || 'Untitled Quiz',
              subject: subject?.name || 'Unknown Subject',
              section: section?.name || 'Unknown Section',
              startDate: startDate,
              dueDate: endDate,
              status: status,
              canTake: canTakeQuiz,
              attemptsUsed: completedAttempts,
              attemptsAllowed: quiz.attempts_allowed,
              type: 'quiz'
            });
          } catch (err) {
            console.error('Error processing quiz:', err);
          }
        }

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
            
            // If same status, sort by due date
            if (a.dueDate && b.dueDate) {
              return a.dueDate.getTime() - b.dueDate.getTime();
            }
            return 0;
          })
          .slice(0, 5);

        this.pendingAssessments = pendingCount;
        console.log('Pending assessments:', this.pendingAssessments);

      } catch (error) {
        console.error('Error loading available quizzes:', error);
        this.recentAssessments = [];
        this.pendingAssessments = 0;
      }
    },

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

    navigateToSubjects() {
      const parent = this.$parent as any;
      if (parent && typeof parent.navigateTo === 'function') {
        parent.navigateTo('subjects');
      } else {
        this.$emit('navigate', 'subjects');
      }
    },

    navigateToCalendar() {
      const parent = this.$parent as any;
      if (parent && typeof parent.navigateTo === 'function') {
        parent.navigateTo('calendar');
      } else {
        this.$emit('navigate', 'calendar');
      }
    },

    navigateToMessages() {
      const parent = this.$parent as any;
      if (parent && typeof parent.navigateTo === 'function') {
        parent.navigateTo('messages');
      } else {
        this.$emit('navigate', 'messages');
      }
    },

    navigateToSettings() {
      const parent = this.$parent as any;
      if (parent && typeof parent.navigateTo === 'function') {
        parent.navigateTo('settings');
      } else {
        this.$emit('navigate', 'settings');
      }
    }
  },

  async mounted() {
    console.log('Home component mounted');
    await this.loadStudentProfile();
    await this.loadNotifications();
    this.setupRealtimeSubscriptions();
    
    this.pollInterval = setInterval(() => {
      this.loadDashboardStats();
      this.loadNotifications();
    }, 30000);
  },

  beforeUnmount() {
    console.log('Home component being destroyed');
    
    if (this.pollInterval) {
      clearInterval(this.pollInterval);
    }
    
    if (this.subscriptions && this.subscriptions.length > 0) {
      this.subscriptions.forEach(subscription => {
        if (subscription && typeof subscription.unsubscribe === 'function') {
          subscription.unsubscribe();
        }
      });
    }
  }
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

.home-container {
  padding: 2rem;
  max-width: 1200px;
  margin: 0 auto;
  font-family: 'Inter', sans-serif;
  background: var(--bg-primary);
  min-height: 100vh;
}

/* Enhanced Header Design */
.section-header-card {
  position: relative;
  background: var(--bg-secondary);
  backdrop-filter: blur(20px);
  border-radius: 24px;
  padding: 2rem;
  margin-bottom: 1.5rem;
  min-height: 120px;
  box-shadow: 
    0 16px 32px var(--shadow-medium),
    0 8px 16px var(--shadow-light),
    inset 0 1px 0 rgba(255, 255, 255, 0.8);
  border: 2px solid var(--border-color);
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  overflow: visible;
  z-index: 1;
}

.section-header-card:hover {
  transform: translateY(-2px);
  box-shadow: 
    0 32px 64px var(--shadow-strong),
    0 16px 32px var(--shadow-medium),
    inset 0 1px 0 rgba(255, 255, 255, 0.9);
}

.header-bg-decoration {
  position: absolute;
  top: -50%;
  right: -20%;
  width: 120%;
  height: 200%;
  background: radial-gradient(ellipse at center, rgba(77, 187, 152, 0.08) 0%, transparent 70%);
  z-index: 1;
}

.floating-shapes {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 1;
  pointer-events: none;
}

.shape {
  position: absolute;
  border-radius: 50%;
  background: linear-gradient(135deg, rgba(77, 187, 152, 0.1) 0%, rgba(51, 128, 107, 0.05) 100%);
}

.shape-1 {
  width: 120px;
  height: 120px;
  top: -30px;
  right: 10%;
  animation: float 6s ease-in-out infinite;
}

.shape-2 {
  width: 80px;
  height: 80px;
  bottom: -20px;
  right: 25%;
  animation: float 8s ease-in-out infinite reverse;
}

.shape-3 {
  width: 60px;
  height: 60px;
  top: 50%;
  right: 5%;
  animation: float 7s ease-in-out infinite;
}

@keyframes float {
  0%, 100% { transform: translateY(0) rotate(0deg); }
  50% { transform: translateY(-20px) rotate(10deg); }
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
  gap: 1.5rem;
}

.section-header-icon {
  width: 60px;
  height: 60px;
  background: linear-gradient(135deg, var(--accent-color) 0%, #A3D1C6 100%);
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #fff;
  box-shadow: 
    0 8px 16px var(--shadow-light),
    inset 0 1px 0 rgba(255, 255, 255, 0.2);
  transition: all 0.3s ease;
}

.section-header-icon:hover {
  transform: scale(1.05);
}

.header-text {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}

.section-header-title {
  font-size: 1.75rem;
  font-weight: 800;
  color: var(--text-accent);
  letter-spacing: -0.02em;
  background: linear-gradient(135deg, var(--accent-color) 0%, #A3D1C6 100%);
  background-clip: text;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  margin-bottom: 0.1rem;
}

.section-header-subtitle {
  font-size: 1rem;
  font-weight: 600;
  color: var(--text-secondary);
  margin-bottom: 0.1rem;
}

.section-header-description {
  font-size: 0.875rem;
  color: var(--text-muted);
  font-weight: 400;
  opacity: 0.9;
}

.header-badge {
  background: rgba(77, 187, 152, 0.1);
  border: 2px solid rgba(77, 187, 152, 0.2);
  border-radius: 20px;
  padding: 1rem 1.5rem;
  backdrop-filter: blur(10px);
  transition: all 0.3s ease;
}

.header-badge.active-student {
  background: rgba(77, 187, 152, 0.15);
  border-color: rgba(77, 187, 152, 0.4);
  box-shadow: 0 4px 12px rgba(77, 187, 152, 0.2);
}

.header-badge.inactive-student {
  background: rgba(255, 71, 87, 0.1);
  border-color: rgba(255, 71, 87, 0.3);
  box-shadow: 0 4px 12px rgba(255, 71, 87, 0.2);
}

.header-badge.active-student .badge-text {
  color: #33806b;
  font-weight: 700;
}

.header-badge.inactive-student .badge-text {
  color: #e74c3c;
  font-weight: 700;
}

.header-badge .badge-icon {
  display: flex;
  align-items: center;
  justify-content: center;
}

.header-badge.active-student .badge-icon {
  color: #33806b;
}

.header-badge.inactive-student .badge-icon {
  color: #e74c3c;
}

.badge-content {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.badge-icon {
  font-size: 1.2rem;
}

.badge-text {
  font-size: 0.75rem;
  font-weight: 600;
  color: var(--text-accent);
  text-transform: uppercase;
  letter-spacing: 0.3px;
}

/* Notification Bell Styles */
.header-actions {
  display: flex;
  align-items: center;
  gap: 1.25rem;
  position: relative;
  z-index: 9999;
}

.notif-bell-wrapper {
  position: relative;
  display: flex;
  align-items: center;
  z-index: 9999;
}

.notif-bell-btn {
  background: var(--bg-accent);
  border: 2px solid var(--accent-color);
  cursor: pointer;
  position: relative;
  padding: 0.25rem;
  border-radius: 50%;
  transition: background 0.2s, box-shadow 0.2s;
  outline: none;
  box-shadow: 0 2px 8px var(--shadow-light);
}

.notif-bell-btn:focus {
  box-shadow: 0 0 0 3px var(--accent-color);
}

.notif-bell-btn:hover {
  background: var(--accent-hover);
}

.notif-bell-dot {
  position: absolute;
  top: 8px;
  right: 8px;
  width: 8px;
  height: 8px;
  background: #ff4757;
  border-radius: 50%;
  border: 2px solid white;
  animation: pulse 2s infinite;
}

@keyframes pulse {
  0% { transform: scale(1); opacity: 1; }
  50% { transform: scale(1.2); opacity: 0.8; }
  100% { transform: scale(1); opacity: 1; }
}

.notif-dropdown {
  position: absolute;
  top: 56px;
  right: 0;
  min-width: 320px;
  max-width: 400px;
  max-height: 350px;
  background: var(--bg-secondary);
  border: 1.5px solid var(--border-color);
  border-radius: 16px;
  box-shadow: 0 20px 64px rgba(0, 0, 0, 0.2), 0 8px 24px rgba(0, 0, 0, 0.15), 0 4px 8px rgba(0, 0, 0, 0.1);
  z-index: 999999;
  padding: 1rem;
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
  overflow-y: auto;
  overflow-x: hidden;
  backdrop-filter: blur(30px);
  transform-origin: top right;
  animation: dropdownSlide 0.2s cubic-bezier(0.4, 0, 0.2, 1) forwards;
  will-change: transform;
  isolation: isolate;
}

@keyframes dropdownSlide {
  from {
    opacity: 0;
    transform: translateY(-10px) scale(0.95);
  }
  to {
    opacity: 1;
    transform: translateY(0) scale(1);
  }
}

.notif-dropdown::before {
  content: '';
  position: absolute;
  top: -8px;
  right: 25px;
  width: 0;
  height: 0;
  border-left: 8px solid transparent;
  border-right: 8px solid transparent;
  border-bottom: 8px solid var(--border-color);
  z-index: 1;
}

.notif-dropdown::after {
  content: '';
  position: absolute;
  top: -6px;
  right: 26px;
  width: 0;
  height: 0;
  border-left: 7px solid transparent;
  border-right: 7px solid transparent;
  border-bottom: 7px solid var(--bg-secondary);
  z-index: 2;
}

.notif-dropdown::-webkit-scrollbar {
  width: 6px;
}

.notif-dropdown::-webkit-scrollbar-track {
  background: var(--bg-accent);
  border-radius: 10px;
}

.notif-dropdown::-webkit-scrollbar-thumb {
  background: var(--accent-color);
  border-radius: 10px;
  opacity: 0.7;
}

.notif-dropdown::-webkit-scrollbar-thumb:hover {
  background: var(--accent-hover);
  opacity: 1;
}

.notif-dropdown-header {
  font-weight: 700;
  color: var(--text-accent);
  font-size: 1.1rem;
  margin-bottom: 0.5rem;
  padding-bottom: 0.5rem;
  border-bottom: 1px solid var(--border-color);
  text-align: center;
}

.notif-dropdown-empty {
  color: var(--text-muted);
  font-size: 0.9rem;
  text-align: center;
  padding: 2rem 1rem;
  font-style: italic;
}

.notif-dropdown-item {
  background: var(--bg-accent);
  border-radius: 12px;
  padding: 0.875rem;
  border: 1px solid var(--border-color);
  display: flex;
  flex-direction: column;
  gap: 0.375rem;
  transition: all 0.2s ease;
  cursor: pointer;
}

.notif-dropdown-item:hover {
  background: var(--bg-accent-hover);
  transform: translateX(2px);
  border-color: var(--accent-color);
}

.notif-title {
  font-weight: 600;
  color: var(--text-accent);
  font-size: 0.95rem;
  line-height: 1.3;
}

.notif-body {
  font-size: 0.85rem;
  color: var(--text-secondary);
  line-height: 1.4;
}

.notif-date {
  font-size: 0.75rem;
  color: var(--text-muted);
  align-self: flex-end;
  margin-top: 0.25rem;
}

/* Stats Grid */
.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1.5rem;
  margin-bottom: 2rem;
}

.stat-card {
  background: var(--bg-card);
  backdrop-filter: blur(20px);
  border-radius: 20px;
  padding: 2rem;
  display: flex;
  align-items: center;
  gap: 1.5rem;
  box-shadow: 0 8px 32px var(--shadow-medium);
  border: 1px solid var(--border-color);
  transition: all 0.3s ease;
}

.stat-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 40px var(--shadow-strong);
}

.stat-icon {
  width: 60px;
  height: 60px;
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
}

.stat-icon.subjects {
  background: linear-gradient(135deg, #3D8D7A 0%, #A3D1C6 100%);
}

.stat-icon.assessments {
  background: linear-gradient(135deg, #B3D8A8 0%, #3D8D7A 100%);
}

.stat-number {
  font-size: 2.5rem;
  font-weight: 800;
  color: var(--text-accent);
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

.content-grid {
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: 2rem;
}

.content-card {
  background: var(--bg-card);
  backdrop-filter: blur(20px);
  border-radius: 24px;
  padding: 2rem;
  box-shadow: 0 8px 32px var(--shadow-medium);
  border: 1px solid var(--border-color);
}

.card-header {
  margin-bottom: 2rem;
}

.card-header h3 {
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--text-accent);
  display: flex;
  align-items: center;
  gap: 0.75rem;
  margin-bottom: 0.5rem;
}

.card-subtitle {
  color: var(--text-secondary);
  font-size: 0.95rem;
}

.assessment-list {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.assessment-item {
  background: var(--bg-accent);
  border-radius: 16px;
  padding: 1.5rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  border: 1px solid var(--border-color);
  transition: all 0.3s ease;
}

.assessment-item:hover {
  background: var(--bg-accent-hover);
  transform: translateX(4px);
}

.assessment-info h4 {
  font-weight: 600;
  color: var(--text-accent);
  margin-bottom: 0.25rem;
}

.assessment-subject {
  font-size: 0.875rem;
  color: var(--text-muted);
}

.assessment-due {
  text-align: right;
}

.due-date {
  display: block;
  font-weight: 600;
  color: var(--text-accent);
  margin-bottom: 0.25rem;
}

.status {
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
  padding: 0.25rem 0.75rem;
  border-radius: 12px;
  letter-spacing: 0.5px;
}

.status.pending {
  background: rgba(255, 193, 7, 0.2);
  color: #e6b000;
}

.status.in-progress {
  background: rgba(61, 141, 122, 0.2);
  color: var(--text-accent);
}

.quick-links-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
}

.quick-link-btn {
  background: var(--bg-accent);
  border: 1px solid var(--border-color);
  border-radius: 16px;
  padding: 1.5rem 1rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.75rem;
  cursor: pointer;
  transition: all 0.3s ease;
  font-weight: 600;
  color: var(--text-accent);
  text-decoration: none;
}

.quick-link-btn:hover {
  background: var(--bg-accent-hover);
  transform: translateY(-2px);
  box-shadow: 0 8px 25px var(--shadow-strong);
}

@media (max-width: 768px) {
  .home-container {
    padding: 1rem;
  }
  
  .section-header-card {
    padding: 2.5rem 2rem;
    min-height: 140px;
  }
  
  .section-header-left {
    flex-direction: column;
    text-align: center;
    gap: 1.5rem;
  }
  
  .section-header-content {
    flex-direction: column;
    gap: 2rem;
  }
  
  .section-header-title {
    font-size: 2rem;
  }
  
  .content-grid {
    grid-template-columns: 1fr;
    gap: 1.5rem;
  }
  
  .stats-grid {
    grid-template-columns: 1fr;
  }
  
  .quick-links-grid {
    grid-template-columns: 1fr;
  }
}</style>