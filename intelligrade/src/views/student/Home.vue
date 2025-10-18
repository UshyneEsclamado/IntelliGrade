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
          <button @click="navigateToSubjects" class="quick-link">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M19,3H5C3.9,3 3,3.9 3,5V19C3,20.1 3.9,21 5,21H19C20.1,21 21,20.1 21,19V5C21,3.9 20.1,3 19,3M5,19V5H19V19H5Z" />
            </svg>
            My Subjects
          </button>
          <button @click="navigateToCalendar" class="quick-link">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M19,19H5V8H19M19,3H18V1H16V3H8V1H6V3H5C3.89,3 3,3.89 3,5V19A2,2 0 0,0 5,21H19A2,2 0 0,0 21,19V5C21,3.89 20.1,3 19,3M16.5,13.5H11V18.5H16.5V13.5Z" />
            </svg>
            Calendar
          </button>
          <button @click="navigateToMessages" class="quick-link">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M22 6c0-1.1-.9-2-2-2H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6zM4 6h16v.5l-8 5-8-5V6zm0 13.5V8l8 5 8-5v11.5H4z" />
            </svg>
            Messages
          </button>
          <button @click="navigateToSettings" class="quick-link">
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
      isActive: false,
      enrolledSectionIds: []
    };
  },
  methods: {
    toggleNotifDropdown() {
      this.showNotifDropdown = !this.showNotifDropdown;
    },

    async loadEnrolledSections() {
      if (!this.studentRecordId) return [];
      
      try {
        const { data: enrollments } = await supabase
          .from('enrollments')
          .select('section_id')
          .eq('student_id', this.studentRecordId)
          .eq('status', 'active');

        this.enrolledSectionIds = enrollments?.map(e => e.section_id) || [];
        console.log('Enrolled section IDs:', this.enrolledSectionIds);
        return this.enrolledSectionIds;
      } catch (error) {
        console.error('Error loading enrolled sections:', error);
        return [];
      }
    },

    async loadNotifications() {
      if (!this.studentRecordId) {
        console.log('Cannot load notifications: no studentRecordId');
        return;
      }
      
      try {
        console.log('Loading notifications for student:', this.studentRecordId);
        const notifications = [];
        
        // Ensure we have enrolled sections
        if (this.enrolledSectionIds.length === 0) {
          await this.loadEnrolledSections();
        }

        // 1. Get unread direct messages
        const { data: messages, error: msgError } = await supabase
          .from('messages')
          .select('id, message_text, message_type, sent_at, sender_id, section_id')
          .eq('recipient_id', this.studentRecordId)
          .is('read_at', null)
          .order('sent_at', { ascending: false })
          .limit(10);

        if (msgError) {
          console.error('Error loading direct messages:', msgError);
        } else if (messages && messages.length > 0) {
          console.log('Found', messages.length, 'unread direct messages');
          for (const msg of messages) {
            try {
              const { data: section } = await supabase
                .from('sections')
                .select('name, subject_id')
                .eq('id', msg.section_id)
                .maybeSingle();

              let subjectName = 'Unknown Subject';
              if (section?.subject_id) {
                const { data: subject } = await supabase
                  .from('subjects')
                  .select('name')
                  .eq('id', section.subject_id)
                  .maybeSingle();
                subjectName = subject?.name || 'Unknown Subject';
              }

              const sectionName = section?.name || 'Unknown Section';
              const messagePreview = msg.message_text?.substring(0, 100) || '';
              const messageSuffix = msg.message_text?.length > 100 ? '...' : '';
              
              notifications.push({
                id: `msg-${msg.id}`,
                title: msg.message_type === 'announcement' ? 'New Announcement' : 'New Message',
                body: `${subjectName} - ${sectionName}: ${messagePreview}${messageSuffix}`,
                date: new Date(msg.sent_at).toLocaleString(),
                type: 'message',
                rawDate: new Date(msg.sent_at)
              });
            } catch (err) {
              console.error('Error processing message:', err);
            }
          }
        }

        // 2. Get broadcast announcements from enrolled sections
        if (this.enrolledSectionIds.length > 0) {
          const { data: broadcasts, error: broadcastError } = await supabase
            .from('messages')
            .select('id, message_text, sent_at, section_id, created_at')
            .eq('message_type', 'announcement')
            .is('recipient_id', null)
            .in('section_id', this.enrolledSectionIds)
            .order('sent_at', { ascending: false })
            .limit(10);

          if (broadcastError) {
            console.error('Error loading broadcasts:', broadcastError);
          } else if (broadcasts && broadcasts.length > 0) {
            console.log('Found', broadcasts.length, 'broadcast announcements');
            for (const msg of broadcasts) {
              try {
                const { data: section } = await supabase
                  .from('sections')
                  .select('name, subject_id')
                  .eq('id', msg.section_id)
                  .maybeSingle();

                let subjectName = 'Unknown Subject';
                if (section?.subject_id) {
                  const { data: subject } = await supabase
                    .from('subjects')
                    .select('name')
                    .eq('id', section.subject_id)
                    .maybeSingle();
                  subjectName = subject?.name || 'Unknown Subject';
                }

                const sectionName = section?.name || 'Unknown Section';
                const messagePreview = msg.message_text?.substring(0, 100) || '';
                const messageSuffix = msg.message_text?.length > 100 ? '...' : '';
                
                notifications.push({
                  id: `broadcast-${msg.id}`,
                  title: 'Class Announcement',
                  body: `${subjectName} - ${sectionName}: ${messagePreview}${messageSuffix}`,
                  date: new Date(msg.sent_at).toLocaleString(),
                  type: 'announcement',
                  rawDate: new Date(msg.sent_at)
                });
              } catch (err) {
                console.error('Error processing broadcast:', err);
              }
            }
          }
        }

        // 3. Get available quizzes (published and within date range)
        const now = new Date().toISOString();
        
        if (this.enrolledSectionIds.length > 0) {
          const { data: availableQuizzes, error: quizError } = await supabase
            .from('quizzes')
            .select('id, title, start_date, end_date, section_id, subject_id, created_at')
            .eq('status', 'published')
            .in('section_id', this.enrolledSectionIds)
            .lte('start_date', now)
            .gte('end_date', now);

          if (quizError) {
            console.error('Error loading available quizzes:', quizError);
          } else if (availableQuizzes && availableQuizzes.length > 0) {
            console.log('Found', availableQuizzes.length, 'available quizzes');
            
            // Get all attempts for this student
            const { data: allAttempts } = await supabase
              .from('quiz_attempts')
              .select('quiz_id, status')
              .eq('student_id', this.studentRecordId)
              .in('status', ['submitted', 'graded', 'reviewed']);

            const completedQuizIds = new Set(allAttempts?.map(a => a.quiz_id) || []);

            for (const quiz of availableQuizzes) {
              if (!completedQuizIds.has(quiz.id)) {
                try {
                  const { data: section } = await supabase
                    .from('sections')
                    .select('name')
                    .eq('id', quiz.section_id)
                    .maybeSingle();

                  const { data: subject } = await supabase
                    .from('subjects')
                    .select('name')
                    .eq('id', quiz.subject_id)
                    .maybeSingle();

                  const sectionName = section?.name || 'Unknown Section';
                  const subjectName = subject?.name || 'Unknown Subject';
                  const dueDate = new Date(quiz.end_date).toLocaleDateString();
                  
                  notifications.push({
                    id: `quiz-${quiz.id}`,
                    title: 'Quiz Available',
                    body: `${subjectName} - ${quiz.title} in ${sectionName}. Due: ${dueDate}`,
                    date: new Date(quiz.start_date).toLocaleString(),
                    type: 'quiz',
                    rawDate: new Date(quiz.start_date)
                  });
                } catch (err) {
                  console.error('Error processing quiz notification:', err);
                }
              }
            }
          }
        }

        // Sort by date (most recent first) and limit
        this.notifications = notifications
          .sort((a, b) => b.rawDate.getTime() - a.rawDate.getTime())
          .slice(0, 15);

        console.log('Total notifications loaded:', this.notifications.length);

      } catch (error) {
        console.error('Error loading notifications:', error);
      }
    },

    setupRealtimeSubscriptions() {
      if (!this.userId || !this.studentRecordId) {
        console.warn('Cannot setup subscriptions: missing userId or studentRecordId');
        return;
      }

      console.log('Setting up real-time subscriptions for student:', this.studentRecordId);

      // Unsubscribe from any existing subscriptions first
      this.cleanupSubscriptions();

      // 1. Profile changes
      const profileSub = supabase
        .channel('student_home_profile')
        .on(
          'postgres_changes',
          {
            event: '*',
            schema: 'public',
            table: 'profiles',
            filter: `auth_user_id=eq.${this.userId}`
          },
          (payload) => {
            console.log('🔔 Profile changed:', payload);
            this.loadStudentProfile();
          }
        )
        .subscribe((status) => {
          console.log('Profile subscription status:', status);
        });

      // 2. Student record changes
      const studentSub = supabase
        .channel('student_home_student')
        .on(
          'postgres_changes',
          {
            event: '*',
            schema: 'public',
            table: 'students',
            filter: `id=eq.${this.studentRecordId}`
          },
          (payload) => {
            console.log('🔔 Student record changed:', payload);
            this.loadStudentProfile();
          }
        )
        .subscribe((status) => {
          console.log('Student subscription status:', status);
        });

      // 3. All messages (we'll filter in the handler)
      const messageSub = supabase
        .channel('student_home_messages')
        .on(
          'postgres_changes',
          {
            event: '*',
            schema: 'public',
            table: 'messages'
          },
          (payload) => {
            console.log('🔔 Message event:', payload.eventType, payload);
            const msg = payload.new || payload.old;
            
            // Check if message is relevant to this student
            const isDirectMessage = msg.recipient_id === this.studentRecordId;
            const isBroadcast = !msg.recipient_id && this.enrolledSectionIds.includes(msg.section_id);
            
            if (isDirectMessage || isBroadcast) {
              console.log('Message is relevant, reloading notifications');
              this.loadNotifications();
            }
          }
        )
        .subscribe((status) => {
          console.log('Messages subscription status:', status);
        });

      // 4. All quizzes
      const quizSub = supabase
        .channel('student_home_quizzes')
        .on(
          'postgres_changes',
          {
            event: '*',
            schema: 'public',
            table: 'quizzes'
          },
          (payload) => {
            console.log('🔔 Quiz event:', payload.eventType, payload);
            const quiz = payload.new || payload.old;
            
            // Check if quiz is in student's sections
            if (this.enrolledSectionIds.includes(quiz.section_id)) {
              console.log('Quiz is relevant, reloading data');
              this.loadAvailableQuizzes();
              this.loadNotifications();
            }
          }
        )
        .subscribe((status) => {
          console.log('Quizzes subscription status:', status);
        });

      // 5. Quiz attempts for this student
      const attemptSub = supabase
        .channel('student_home_attempts')
        .on(
          'postgres_changes',
          {
            event: '*',
            schema: 'public',
            table: 'quiz_attempts',
            filter: `student_id=eq.${this.studentRecordId}`
          },
          (payload) => {
            console.log('🔔 Quiz attempt event:', payload.eventType, payload);
            this.loadAvailableQuizzes();
            this.loadNotifications();
          }
        )
        .subscribe((status) => {
          console.log('Quiz attempts subscription status:', status);
        });

      // 6. Enrollments for this student
      const enrollmentSub = supabase
        .channel('student_home_enrollments')
        .on(
          'postgres_changes',
          {
            event: '*',
            schema: 'public',
            table: 'enrollments',
            filter: `student_id=eq.${this.studentRecordId}`
          },
          (payload) => {
            console.log('🔔 Enrollment event:', payload.eventType, payload);
            // Reload enrolled sections and then reload everything
            this.loadEnrolledSections().then(() => {
              this.loadDashboardStats();
              this.loadNotifications();
            });
          }
        )
        .subscribe((status) => {
          console.log('Enrollments subscription status:', status);
        });

      // 7. Subjects
      const subjectSub = supabase
        .channel('student_home_subjects')
        .on(
          'postgres_changes',
          {
            event: '*',
            schema: 'public',
            table: 'subjects'
          },
          (payload) => {
            console.log('🔔 Subject event:', payload.eventType);
            this.loadDashboardStats();
            this.loadNotifications();
          }
        )
        .subscribe((status) => {
          console.log('Subjects subscription status:', status);
        });

      // 8. Sections
      const sectionSub = supabase
        .channel('student_home_sections')
        .on(
          'postgres_changes',
          {
            event: '*',
            schema: 'public',
            table: 'sections'
          },
          (payload) => {
            console.log('🔔 Section event:', payload.eventType);
            this.loadDashboardStats();
            this.loadNotifications();
          }
        )
        .subscribe((status) => {
          console.log('Sections subscription status:', status);
        });

      this.subscriptions = [
        profileSub,
        studentSub,
        messageSub,
        quizSub,
        attemptSub,
        enrollmentSub,
        subjectSub,
        sectionSub
      ];

      console.log('✅ Real-time subscriptions established:', this.subscriptions.length);
    },

    cleanupSubscriptions() {
      if (this.subscriptions && this.subscriptions.length > 0) {
        console.log('Cleaning up', this.subscriptions.length, 'subscriptions');
        this.subscriptions.forEach(sub => {
          if (sub && typeof sub.unsubscribe === 'function') {
            sub.unsubscribe();
          }
        });
        this.subscriptions = [];
      }
    },

    async loadStudentProfile() {
      try {
        this.isLoadingName = true;
        
        const { data: { user }, error: authError } = await supabase.auth.getUser();
        
        if (authError || !user) {
          console.error('Auth error:', authError);
          this.studentName = 'Student';
          return;
        }

        this.userId = user.id;

        const { data: profile, error: profileError } = await supabase
          .from('profiles')
          .select('id, full_name, email, role')
          .eq('auth_user_id', user.id)
          .maybeSingle();

        if (profileError || !profile) {
          console.error('Profile error:', profileError);
          this.studentName = user.email?.split('@')[0] || 'Student';
          return;
        }

        this.profileId = profile.id;

        if (profile.role !== 'student') {
          console.warn('User is not a student');
          this.studentName = profile.full_name || 'User';
          return;
        }

        const { data: studentData, error: studentError } = await supabase
          .from('students')
          .select('id, student_id, grade_level, full_name, email, is_active')
          .eq('profile_id', profile.id)
          .maybeSingle();

        if (studentError || !studentData) {
          console.warn('Student data error:', studentError);
          this.studentName = profile.full_name || 'Student';
          return;
        }

        this.studentRecordId = studentData.id;
        this.isActive = studentData.is_active || false;
        this.studentName = studentData.full_name || profile.full_name || 'Student';
        
        console.log('✅ Student profile loaded:', {
          studentRecordId: this.studentRecordId,
          studentName: this.studentName,
          isActive: this.isActive
        });

        // Load enrolled sections first
        await this.loadEnrolledSections();
        
        // Then load dashboard stats
        await this.loadDashboardStats();

      } catch (error) {
        console.error('Error loading student profile:', error);
        this.studentName = 'Student';
      } finally {
        this.isLoadingName = false;
      }
    },

    async loadDashboardStats() {
      try {
        if (!this.studentRecordId) {
          console.warn('No student record ID available');
          return;
        }

        const { data: enrollments, error: enrollmentError } = await supabase
          .from('enrollments')
          .select('section_id, subject_id')
          .eq('student_id', this.studentRecordId)
          .eq('status', 'active');

        if (enrollmentError) {
          console.error('Error loading enrollments:', enrollmentError);
        } else {
          const uniqueSubjects = new Set(enrollments?.map(e => e.subject_id) || []);
          this.totalSubjects = uniqueSubjects.size;
          console.log('Total subjects:', this.totalSubjects);
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
          console.error('Error loading attempts:', attemptsError);
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
              .maybeSingle();

            const { data: section } = await supabase
              .from('sections')
              .select('name')
              .eq('id', quiz.section_id)
              .maybeSingle();

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
            
            if (a.dueDate && b.dueDate) {
              return a.dueDate.getTime() - b.dueDate.getTime();
            }
            return 0;
          })
          .slice(0, 5);

        this.pendingAssessments = pendingCount;
        console.log('Assessments loaded - Pending:', pendingCount, 'Total:', processedQuizzes.length);

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
    console.log('🚀 Home component mounted');
    
    // Load initial data
    await this.loadStudentProfile();
    await this.loadNotifications();
    
    // Setup real-time subscriptions after profile is loaded
    if (this.userId && this.studentRecordId) {
      console.log('Setting up real-time subscriptions...');
      this.setupRealtimeSubscriptions();
    } else {
      console.warn('Cannot setup subscriptions - missing user data');
    }
    
    // Backup polling (less frequent since we have real-time)
    this.pollInterval = setInterval(() => {
      console.log('🔄 Polling update...');
      this.loadNotifications();
    }, 120000); // Every 2 minutes
  },

  watch: {
    $route() {
      // Reload dashboard data when route changes
      this.loadStudentProfile();
      this.loadNotifications();
    }
  },

  beforeUnmount() {
    console.log('🛑 Home component unmounting');
    
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
  max-height: 500px;
  border: 2px solid #A3D1C6;
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