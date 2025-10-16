<template>
  <div class="calendar-container">
    <!-- Loading State -->
    <div v-if="loading" class="loading-container">
      <div class="loading-spinner"></div>
      <p class="loading-text">Loading your calendar...</p>
    </div>

    <!-- Error State -->
    <div v-else-if="error" class="error-container">
      <div class="error-icon">⚠️</div>
      <h3 class="error-title">Unable to load calendar</h3>
      <p class="error-message">{{ error }}</p>
      <button @click="initializeData" class="retry-btn">Try Again</button>
    </div>

    <!-- Main Calendar Content -->
    <div v-else>
      <!-- Minimal Card Header (Subjects style) -->
      <div class="section-header-card minimal-header-card header-flex-align">
        <div class="section-header-left">
          <div class="section-header-icon minimal-header-icon">
            <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M19,3H5C3.9,3 3,3.9 3,5V19C3,20.1 3.9,21 5,21H19C20.1,21 21,20.1 21,19V5C21,3.9 20.1,3 19,3M5,19V5H19V19H5Z" />
            </svg>
          </div>
          <div>
            <div class="section-header-title minimal-header-title">Academic Calendar</div>
            <div class="section-header-sub minimal-header-sub">View and manage your academic events - Real-time updates</div>
          </div>
        </div>
        <div class="section-header-stats align-top">
          <div class="stat-item">
            <span class="stat-number">{{ events.length }}</span>
            <span class="stat-label">Total Events</span>
          </div>
          <div class="stat-item">
            <span class="stat-number live-indicator">🔴</span>
            <span class="stat-label">Live</span>
          </div>
        </div>
      </div>

      <!-- Status Legend -->
      <div class="status-legend">
        <div class="legend-item">
          <div class="legend-color upcoming"></div>
          <span>Upcoming Deadline</span>
        </div>
        <div class="legend-item">
          <div class="legend-color due-today"></div>
          <span>Due Today</span>
        </div>
        <div class="legend-item">
          <div class="legend-color completed"></div>
          <span>Completed</span>
        </div>
        <div class="legend-item">
          <div class="legend-color overdue"></div>
          <span>Overdue</span>
        </div>
      </div>

      <!-- Calendar Navigation -->
      <div class="calendar-nav">
        <div class="nav-controls">
          <button @click="previousMonth" class="nav-btn">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M15.41,16.58L10.83,12L15.41,7.41L14,6L8,12L14,18L15.41,16.58Z" />
            </svg>
          </button>
          <h2 class="current-month">{{ currentMonthYear }}</h2>
          <button @click="nextMonth" class="nav-btn">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M8.59,16.58L13.17,12L8.59,7.41L10,6L16,12L10,18L8.59,16.58Z" />
            </svg>
          </button>
        </div>
        <div class="view-toggle">
          <button 
            v-for="view in views" 
            :key="view.key"
            @click="currentView = view.key"
            :class="['view-btn', { 'active': currentView === view.key }]"
          >
            {{ view.label }}
          </button>
        </div>
      </div>

      <!-- Calendar Grid -->
      <div class="calendar-content">
        <div v-if="currentView === 'month'" class="calendar-grid">
          <!-- Days of Week Header -->
          <div class="calendar-header">
            <div v-for="day in daysOfWeek" :key="day" class="day-header">
              {{ day }}
            </div>
          </div>
          
          <!-- Calendar Days -->
          <div class="calendar-body">
            <div 
              v-for="day in calendarDays" 
              :key="day.date"
              :class="['calendar-day', {
                'other-month': !day.isCurrentMonth,
                'today': day.isToday,
                'has-events': day.events.length > 0,
                'has-due-today': day.hasDueToday,
                'has-overdue': day.hasOverdue,
                'has-upcoming': day.hasUpcoming,
                'clickable': day.events.length > 0
              }]"
              @click="selectDay(day)"
            >
              <span class="day-number">{{ day.day }}</span>
              <div class="day-events">
                <div 
                  v-for="event in day.events.slice(0, 2)" 
                  :key="event.id"
                  :class="['event-dot', getEventStatus(event)]"
                  :title="`${event.title} - ${getEventStatusText(event)}`"
                ></div>
                <span v-if="day.events.length > 2" class="more-events">
                  +{{ day.events.length - 2 }}
                </span>
              </div>
              <div v-if="day.events.length > 0" class="event-count">
                {{ day.events.length }}
              </div>
            </div>
          </div>
        </div>

        <!-- List View -->
        <div v-if="currentView === 'list'" class="events-list">
          <div v-for="(dayEvents, date) in groupedEvents" :key="date" class="day-group">
            <h3 class="day-title">{{ formatDate(date) }}</h3>
            <div class="events-container">
              <div 
                v-for="event in dayEvents" 
                :key="event.id"
                :class="['event-item', event.type, getEventStatus(event)]"
              >
                <div class="event-time">{{ event.time }}</div>
                <div class="event-content">
                  <h4 class="event-title">{{ event.title }}</h4>
                  <p class="event-subject">{{ event.subject }}</p>
                  <p class="event-description">{{ event.description }}</p>
                  <div class="event-status-badge">
                    <span :class="['status-badge', getEventStatus(event)]">
                      {{ getEventStatusText(event) }}
                    </span>
                  </div>
                </div>
                <div class="event-actions">
                  <button v-if="canTakeQuiz(event)" 
                          class="take-quiz-btn" 
                          @click="takeQuiz(event)">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                      <path d="M13,9H18.5L13,3.5V9M6,2H14L20,8V20A2,2 0 0,1 18,22H6C4.89,22 4,21.1 4,20V4C4,2.89 4.89,2 6,2M15,18V16H6V18H15M18,14V12H6V14H18Z" />
                    </svg>
                    Take Quiz
                  </button>
                  <button class="view-btn-small" @click="viewEvent(event)">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                      <path d="M12,9A3,3 0 0,0 9,12A3,3 0 0,0 12,15A3,3 0 0,0 15,12A3,3 0 0,0 12,9M12,17A5,5 0 0,1 7,12A5,5 0 0,1 12,7A5,5 0 0,1 17,12A5,5 0 0,1 12,17M12,4.5C7,4.5 2.73,7.61 1,12C2.73,16.39 7,19.5 12,19.5C17,19.5 21.27,16.39 23,12C21.27,7.61 17,4.5 12,4.5Z" />
                    </svg>
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Day Details Modal -->
      <div v-if="selectedDay" class="modal-overlay" @click="closeDayModal">
        <div class="day-modal-content" @click.stop>
          <div class="day-modal-header">
            <h3>{{ formatSelectedDayDate() }}</h3>
            <button @click="closeDayModal" class="close-btn">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                <path d="M19,6.41L17.59,5L12,10.59L6.41,5L5,6.41L10.59,12L5,17.59L6.41,19L12,13.41L17.59,19L19,17.59L13.41,12L19,6.41Z" />
              </svg>
            </button>
          </div>
          <div class="day-modal-body">
            <div class="day-events-summary">
              <div class="summary-stats">
                <div class="summary-stat">
                  <span class="summary-number">{{ selectedDay.events.length }}</span>
                  <span class="summary-label">Total Events</span>
                </div>
                <div class="summary-stat">
                  <span class="summary-number">{{ getCompletedCount(selectedDay.events) }}</span>
                  <span class="summary-label">Completed</span>
                </div>
                <div class="summary-stat">
                  <span class="summary-number">{{ getPendingCount(selectedDay.events) }}</span>
                  <span class="summary-label">Pending</span>
                </div>
              </div>
            </div>
            
            <div class="day-events-list">
              <h4>Deadlines & Events</h4>
              <div class="day-event-items">
                <div 
                  v-for="event in selectedDay.events" 
                  :key="event.id"
                  :class="['day-event-item', getEventStatus(event)]"
                >
                  <div class="event-status-indicator">
                    <div :class="['status-dot', getEventStatus(event)]"></div>
                  </div>
                  <div class="event-details">
                    <h5 class="event-name">{{ event.title }}</h5>
                    <p class="event-subject-small">{{ event.subject }}</p>
                    <p class="event-time-small">{{ event.time }}</p>
                    <p class="event-desc-small">{{ event.description }}</p>
                  </div>
                  <div class="event-status-text">
                    <span :class="['status-badge-small', getEventStatus(event)]">
                      {{ getEventStatusText(event) }}
                    </span>
                  </div>
                  <div class="event-quick-actions">
                    <button v-if="canTakeQuiz(event)" 
                            class="quick-take-quiz-btn" 
                            @click="takeQuiz(event)"
                            :title="'Take quiz: ' + event.title">
                      <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor">
                        <path d="M13,9H18.5L13,3.5V9M6,2H14L20,8V20A2,2 0 0,1 18,22H6C4.89,22 4,21.1 4,20V4C4,2.89 4.89,2 6,2M15,18V16H6V18H15M18,14V12H6V14H18Z" />
                      </svg>
                    </button>
                    <button class="quick-view-btn" 
                            @click="viewEventFromDay(event)"
                            :title="'View ' + event.title + ' details'">
                      <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor">
                        <path d="M12,9A3,3 0 0,0 9,12A3,3 0 0,0 12,15A3,3 0 0,0 15,12A3,3 0 0,0 12,9M12,17A5,5 0 0,1 7,12A5,5 0 0,1 12,7A5,5 0 0,1 17,12A5,5 0 0,1 12,17M12,4.5C7,4.5 2.73,7.61 1,12C2.73,16.39 7,19.5 12,19.5C17,19.5 21.27,16.39 23,12C21.27,7.61 17,4.5 12,4.5Z" />
                      </svg>
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Event Details Modal -->
      <div v-if="selectedEvent" class="modal-overlay" @click="closeModal">
        <div class="modal-content" @click.stop>
          <div class="modal-header">
            <h3>{{ selectedEvent.title }}</h3>
            <button @click="closeModal" class="close-btn">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                <path d="M19,6.41L17.59,5L12,10.59L6.41,5L5,6.41L10.59,12L5,17.59L6.41,19L12,13.41L17.59,19L19,17.59L13.41,12L19,6.41Z" />
              </svg>
            </button>
          </div>
          <div class="modal-body">
            <div class="event-detail">
              <strong>Subject:</strong> {{ selectedEvent.subject }}
            </div>
            <div class="event-detail">
              <strong>Date:</strong> {{ formatEventDate(selectedEvent.date) }}
            </div>
            <div class="event-detail">
              <strong>Time:</strong> {{ selectedEvent.time }}
            </div>
            <div class="event-detail">
              <strong>Type:</strong> {{ selectedEvent.type }}
            </div>
            <div class="event-detail">
              <strong>Status:</strong> 
              <span :class="['status-badge', getEventStatus(selectedEvent)]">
                {{ getEventStatusText(selectedEvent) }}
              </span>
            </div>
            <div class="event-detail">
              <strong>Description:</strong> {{ selectedEvent.description }}
            </div>
            <div v-if="selectedEvent.quizCode" class="event-detail">
              <strong>Quiz Code:</strong> {{ selectedEvent.quizCode }}
            </div>
            <div v-if="selectedEvent.attemptsAllowed" class="event-detail">
              <strong>Attempts:</strong> {{ selectedEvent.totalAttempts }} / {{ selectedEvent.attemptsAllowed }} used
            </div>
            <div v-if="selectedEvent.isCompleted && selectedEvent.bestScore" class="event-detail">
              <strong>Best Score:</strong> {{ selectedEvent.bestScore.toFixed(1) }}%
            </div>
            <div v-if="canTakeQuiz(selectedEvent)" class="modal-actions">
              <button class="take-quiz-btn-modal" @click="takeQuiz(selectedEvent)">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M13,9H18.5L13,3.5V9M6,2H14L20,8V20A2,2 0 0,1 18,22H6C4.89,22 4,21.1 4,20V4C4,2.89 4.89,2 6,2M15,18V16H6V18H15M18,14V12H6V14H18Z" />
                </svg>
                Take Quiz Now
              </button>
            </div>
            <div v-else-if="selectedEvent.isCompleted" class="modal-info">
              <div class="completed-message">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M21,7L9,19L3.5,13.5L4.91,12.09L9,16.17L19.59,5.59L21,7Z" />
                </svg>
                <span>Quiz Completed!</span>
              </div>
            </div>
            <div v-else-if="getEventStatus(selectedEvent) === 'overdue'" class="modal-info">
              <div class="overdue-message">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M13,14H11V10H13M13,18H11V16H13M1,21H23L12,2L1,21Z" />
                </svg>
                <span>Quiz Deadline Passed</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Notifications Area -->
    <div v-if="notifications.length > 0" class="notifications-container">
      <div 
        v-for="notification in notifications" 
        :key="notification.id"
        :class="['notification', notification.type]"
        @click="removeNotification(notification.id)"
      >
        <div class="notification-content">
          <span class="notification-icon">
            {{ getNotificationIcon(notification.type) }}
          </span>
          <span class="notification-message">{{ notification.message }}</span>
        </div>
        <button class="notification-close">&times;</button>
      </div>
    </div>
  </div>
</template>

<script>
import { supabase } from '@/supabase.js'

export default {
  name: 'StudentCalendar',
  data() {
    return {
      currentDate: new Date(),
      currentView: 'month',
      selectedEvent: null,
      selectedDay: null,
      currentTime: new Date(),
      statusUpdateInterval: null,
      fastUpdateInterval: null,
      realTimeSubscription: null,
      loading: true,
      error: null,
      notifications: [],
      views: [
        { key: 'month', label: 'Month' },
        { key: 'list', label: 'List' }
      ],
      daysOfWeek: ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'],
      events: [],
      user: null,
      studentId: null
    };
  },
  computed: {
    currentMonthYear() {
      return this.currentDate.toLocaleDateString('en-US', {
        month: 'long',
        year: 'numeric'
      });
    },
    upcomingDeadlines() {
      return this.events.filter(event => 
        this.getEventStatus(event) === 'upcoming' || this.getEventStatus(event) === 'due-today'
      ).length;
    },
    overdueCount() {
      return this.events.filter(event => this.getEventStatus(event) === 'overdue').length;
    },
    calendarDays() {
      const year = this.currentDate.getFullYear();
      const month = this.currentDate.getMonth();
      const today = new Date(this.currentTime);
      today.setHours(0, 0, 0, 0);
      
      const firstDay = new Date(year, month, 1);
      const startDate = new Date(firstDay);
      startDate.setDate(startDate.getDate() - firstDay.getDay());
      
      const days = [];
      for (let i = 0; i < 42; i++) {
        const date = new Date(startDate);
        date.setDate(startDate.getDate() + i);
        date.setHours(0, 0, 0, 0);
        
        const dayEvents = this.events.filter(event => {
          const eventDate = new Date(event.date);
          eventDate.setHours(0, 0, 0, 0);
          return eventDate.getTime() === date.getTime();
        });
        
        const hasDueToday = dayEvents.some(event => this.getEventStatus(event) === 'due-today');
        const hasOverdue = dayEvents.some(event => this.getEventStatus(event) === 'overdue');
        const hasUpcoming = dayEvents.some(event => this.getEventStatus(event) === 'upcoming');
        
        days.push({
          date: date.toDateString(),
          day: date.getDate(),
          fullDate: new Date(date),
          isCurrentMonth: date.getMonth() === month,
          isToday: date.getTime() === today.getTime(),
          events: dayEvents,
          hasDueToday,
          hasOverdue,
          hasUpcoming
        });
      }
      
      return days;
    },
    groupedEvents() {
      const grouped = {};
      const sortedEvents = [...this.events].sort((a, b) => a.date - b.date);
      
      sortedEvents.forEach(event => {
        const dateKey = event.date.toDateString();
        if (!grouped[dateKey]) {
          grouped[dateKey] = [];
        }
        grouped[dateKey].push(event);
      });
      return grouped;
    }
  },
  watch: {
    events: {
      handler() {
        this.$forceUpdate();
      },
      deep: true
    }
  },
  methods: {
    async initializeData() {
      try {
        this.loading = true;
        this.error = null;
        
        // Get current user
        const { data: { user }, error: userError } = await supabase.auth.getUser();
        if (userError) throw userError;
        
        this.user = user;
        console.log('Current user:', user.id);
        
        // Get student ID from profile
        const { data: profileData, error: profileError } = await supabase
          .from('profiles')
          .select('id, role')
          .eq('auth_user_id', user.id)
          .single();
          
        if (profileError) throw profileError;
        
        console.log('Profile data:', profileData);
        
        if (profileData.role !== 'student') {
          throw new Error('This calendar is only available for students');
        }
        
        // Get student details
        const { data: studentData, error: studentError } = await supabase
          .from('students')
          .select('id, full_name, grade_level')
          .eq('profile_id', profileData.id)
          .single();
          
        if (studentError) throw studentError;
        
        this.studentId = studentData.id;
        console.log('Student ID:', this.studentId);
        console.log('Student grade level:', studentData.grade_level);
        
        // Load initial events
        await this.loadEvents();
        
        // Setup real-time subscription
        this.setupRealTimeSubscription();
        
      } catch (error) {
        console.error('Error initializing calendar:', error);
        this.error = error.message || 'Failed to load calendar data';
        this.showNotification('Error loading calendar data: ' + error.message, 'error');
      } finally {
        this.loading = false;
      }
    },

    async loadEvents() {
      try {
        if (!this.studentId) {
          console.error('Student ID not found');
          return;
        }

        console.log('Loading events for student:', this.studentId);

        // STEP 1: Get all section IDs the student is enrolled in
        const { data: enrollments, error: enrollError } = await supabase
          .from('enrollments')
          .select('section_id')
          .eq('student_id', this.studentId)
          .eq('status', 'active');

        if (enrollError) {
          console.error('Enrollment error:', enrollError);
          throw enrollError;
        }

        console.log('Total enrolled subjects:', enrollments?.length || 0);

        if (!enrollments || enrollments.length === 0) {
          console.log('Student is not enrolled in any sections');
          this.events = [];
          this.showNotification('You are not enrolled in any subjects yet.', 'info');
          return;
        }

        const sectionIds = enrollments.map(e => e.section_id);
        console.log('Enrolled section IDs:', sectionIds);

        // STEP 2: Get all published quizzes for those sections
        const { data: quizzesData, error: quizzesError } = await supabase
          .from('quizzes')
          .select(`
            id,
            title,
            description,
            start_date,
            end_date,
            status,
            number_of_questions,
            time_limit_minutes,
            attempts_allowed,
            quiz_code,
            subject_id,
            section_id
          `)
          .in('section_id', sectionIds)
          .eq('status', 'published')
          .order('end_date', { ascending: true });

        if (quizzesError) {
          console.error('Quizzes error:', quizzesError);
          throw quizzesError;
        }

        console.log('Published quizzes found:', quizzesData?.length || 0);

        if (!quizzesData || quizzesData.length === 0) {
          this.events = [];
          this.showNotification('No quizzes available yet. Check back later!', 'info');
          return;
        }

        // STEP 3: Get subject details for each quiz
        const subjectIds = [...new Set(quizzesData.map(q => q.subject_id))];
        const { data: subjectsData, error: subjectsError } = await supabase
          .from('subjects')
          .select('id, name, grade_level')
          .in('id', subjectIds);

        if (subjectsError) {
          console.error('Subjects error:', subjectsError);
          throw subjectsError;
        }

        const subjectsMap = {};
        subjectsData?.forEach(subj => {
          subjectsMap[subj.id] = subj;
        });

        // STEP 4: Get section details
        const { data: sectionsData, error: sectionsError } = await supabase
          .from('sections')
          .select('id, name, section_code')
          .in('id', sectionIds);

        if (sectionsError) {
          console.error('Sections error:', sectionsError);
          throw sectionsError;
        }

        const sectionsMap = {};
        sectionsData?.forEach(sec => {
          sectionsMap[sec.id] = sec;
        });

        // STEP 5: Get student's quiz results
        const quizIds = quizzesData.map(q => q.id);
        const { data: resultsData, error: resultsError } = await supabase
          .from('quiz_results')
          .select('quiz_id, status, best_percentage, total_attempts')
          .eq('student_id', this.studentId)
          .in('quiz_id', quizIds);

        if (resultsError) {
          console.error('Results error:', resultsError);
        }

        const resultsMap = {};
        resultsData?.forEach(result => {
          resultsMap[result.quiz_id] = result;
        });

        console.log('Quiz results found:', resultsData?.length || 0);

        // STEP 6: Transform data for calendar
        this.events = quizzesData.map(quiz => {
          const result = resultsMap[quiz.id];
          const subject = subjectsMap[quiz.subject_id];
          const section = sectionsMap[quiz.section_id];
          const isCompleted = result && (result.status === 'completed' || result.status === 'graded');
          
          const deadlineDate = quiz.end_date ? new Date(quiz.end_date) : null;
          
          return {
            id: quiz.id,
            title: quiz.title,
            subject: subject?.name || 'Unknown Subject',
            subjectCode: `Grade ${subject?.grade_level || '?'}`,
            date: deadlineDate || new Date(),
            time: deadlineDate ? deadlineDate.toLocaleTimeString('en-US', { 
              hour: '2-digit', 
              minute: '2-digit' 
            }) : '11:59 PM',
            type: 'quiz',
            description: quiz.description || `${quiz.number_of_questions} questions${quiz.time_limit_minutes ? ` • ${quiz.time_limit_minutes} minutes` : ''} • ${quiz.attempts_allowed} attempt${quiz.attempts_allowed > 1 ? 's' : ''} allowed`,
            isCompleted: isCompleted,
            submittedAt: isCompleted ? new Date() : null,
            quizCode: quiz.quiz_code,
            sectionName: section?.name || '',
            sectionCode: section?.section_code || '',
            numberOfQuestions: quiz.number_of_questions,
            timeLimit: quiz.time_limit_minutes,
            attemptsAllowed: quiz.attempts_allowed,
            totalAttempts: result?.total_attempts || 0,
            bestScore: result?.best_percentage || 0,
            startDate: quiz.start_date ? new Date(quiz.start_date) : null
          };
        }).filter(event => event.date);

        console.log('Events loaded successfully:', this.events.length);
        
        if (this.events.length > 0) {
          this.showNotification(`Loaded ${this.events.length} quiz${this.events.length > 1 ? 'zes' : ''}`, 'success');
        }
        
      } catch (error) {
        console.error('Error loading events:', error);
        this.showNotification('Failed to load quizzes: ' + error.message, 'error');
      }
    },

    setupRealTimeSubscription() {
      if (!this.studentId) return;

      console.log('Setting up real-time subscription...');

      // Subscribe to changes in quizzes table
      this.realTimeSubscription = supabase
        .channel('calendar-quiz-changes')
        .on('postgres_changes', {
          event: '*',
          schema: 'public',
          table: 'quizzes',
          filter: `status=eq.published`
        }, (payload) => {
          console.log('Real-time quiz update:', payload);
          this.handleQuizUpdate(payload);
        })
        .on('postgres_changes', {
          event: '*',
          schema: 'public',
          table: 'quiz_results',
          filter: `student_id=eq.${this.studentId}`
        }, (payload) => {
          console.log('Real-time quiz result update:', payload);
          this.handleQuizResultUpdate(payload);
        })
        .subscribe((status) => {
          console.log('Real-time subscription status:', status);
        });
    },

    async handleQuizUpdate(payload) {
      const { eventType, new: newRecord, old: oldRecord } = payload;
      
      switch (eventType) {
        case 'INSERT':
          await this.loadEvents();
          if (newRecord?.title) {
            this.showNotification(`New quiz available: ${newRecord.title}`, 'info');
          }
          break;
        case 'UPDATE':
          await this.loadEvents();
          if (newRecord?.title) {
            this.showNotification(`Quiz updated: ${newRecord.title}`, 'info');
          }
          break;
        case 'DELETE':
          if (oldRecord?.id) {
            this.events = this.events.filter(e => e.id !== oldRecord.id);
            this.showNotification('A quiz has been removed', 'warning');
          }
          break;
      }
    },

    async handleQuizResultUpdate(payload) {
      const { new: newRecord } = payload;
      
      if (!newRecord?.quiz_id) return;
      
      const eventIndex = this.events.findIndex(e => e.id === newRecord.quiz_id);
      if (eventIndex !== -1) {
        const isCompleted = newRecord.status === 'completed' || newRecord.status === 'graded';
        this.events[eventIndex].isCompleted = isCompleted;
        this.events[eventIndex].totalAttempts = newRecord.total_attempts || 0;
        this.events[eventIndex].bestScore = newRecord.best_percentage || 0;
        
        if (isCompleted) {
          this.showNotification(`Quiz completed: ${this.events[eventIndex].title}`, 'success');
        }
      }
    },

    canTakeQuiz(event) {
      if (!event) return false;
      
      // Can't take if already completed
      if (event.isCompleted) return false;
      
      // Can't take if no more attempts left
      if (event.totalAttempts >= event.attemptsAllowed) return false;
      
      // Can't take if overdue (past deadline)
      const status = this.getEventStatus(event);
      if (status === 'overdue') return false;
      
      // Can take if it's upcoming or due today
      return status === 'upcoming' || status === 'due-today';
    },

    takeQuiz(event) {
      // Close any open modals
      this.selectedEvent = null;
      this.selectedDay = null;
      
      console.log('Current route:', this.$route.path);
      console.log('Attempting to navigate to subjects page for quiz:', {
        id: event.id,
        code: event.quizCode,
        title: event.title
      });
      
      // Check if we're already on subjects page
      if (this.$route.path === '/student/subjects' || this.$route.name === 'StudentSubjects') {
        console.log('Already on subjects page, reloading...');
        // Force a reload of the current page
        this.$router.go(0);
        this.showNotification(`Refreshing Subjects page - ${event.title}`, 'info');
      } else {
        // Navigate to subjects page
        this.$router.push('/student/subjects')
          .then(() => {
            console.log('Successfully navigated to subjects page');
            this.showNotification(`Opening Subjects page - ${event.title}`, 'info');
          })
          .catch(err => {
            console.error('Navigation error:', err);
            // Try with name-based navigation as fallback
            this.$router.push({ name: 'StudentSubjects' })
              .catch(err2 => {
                console.error('Fallback navigation also failed:', err2);
                this.showNotification('Unable to navigate to subjects page', 'error');
              });
          });
      }
    },

    showNotification(message, type = 'info') {
      const notification = {
        id: Date.now(),
        message,
        type,
        timestamp: new Date()
      };

      this.notifications.push(notification);
      
      setTimeout(() => {
        this.removeNotification(notification.id);
      }, 5000);
      
      console.log(`[${type.toUpperCase()}] ${message}`);
    },

    removeNotification(notificationId) {
      const index = this.notifications.findIndex(n => n.id === notificationId);
      if (index !== -1) {
        this.notifications.splice(index, 1);
      }
    },

    getNotificationIcon(type) {
      switch (type) {
        case 'success': return '✅';
        case 'error': return '❌';
        case 'warning': return '⚠️';
        case 'info': return 'ℹ️';
        default: return 'ℹ️';
      }
    },

    getEventStatus(event) {
      if (!event.date) return 'unknown';
      
      const eventDate = new Date(event.date);
      const today = new Date(this.currentTime);
      today.setHours(0, 0, 0, 0);
      eventDate.setHours(0, 0, 0, 0);
      
      if (event.isCompleted) {
        return 'completed';
      }
      
      if (eventDate.getTime() < today.getTime()) {
        return 'overdue';
      }
      
      if (eventDate.getTime() === today.getTime()) {
        return 'due-today';
      }
      
      return 'upcoming';
    },

    getEventStatusText(event) {
      const status = this.getEventStatus(event);
      switch (status) {
        case 'completed':
          return `Completed (${event.bestScore.toFixed(0)}%)`;
        case 'overdue':
          return `Overdue (${event.totalAttempts}/${event.attemptsAllowed} attempts)`;
        case 'due-today':
          return 'Due Today!';
        case 'upcoming':
          return 'Upcoming';
        default:
          return 'Unknown';
      }
    },

    getCompletedCount(events) {
      return events.filter(event => this.getEventStatus(event) === 'completed').length;
    },

    getPendingCount(events) {
      return events.filter(event => 
        this.getEventStatus(event) === 'upcoming' || 
        this.getEventStatus(event) === 'due-today' || 
        this.getEventStatus(event) === 'overdue'
      ).length;
    },

    updateCurrentTime() {
      this.currentTime = new Date();
      this.checkDeadlineReminders();
    },

    checkDeadlineReminders() {
      const now = new Date();
      const oneHour = 60 * 60 * 1000;
      const oneDay = 24 * oneHour;

      this.events.forEach(event => {
        if (event.isCompleted || !event.date) return;

        const eventDateTime = new Date(event.date);
        const timeDiff = eventDateTime.getTime() - now.getTime();

        if (timeDiff > 0 && timeDiff <= oneHour) {
          this.showNotification(
            `⏰ ${event.title} is due in less than 1 hour!`,
            'warning'
          );
        } else if (timeDiff > oneHour && timeDiff <= oneDay) {
          this.showNotification(
            `📅 ${event.title} is due today!`,
            'info'
          );
        }
      });
    },

    previousMonth() {
      this.currentDate = new Date(this.currentDate.getFullYear(), this.currentDate.getMonth() - 1, 1);
    },

    nextMonth() {
      this.currentDate = new Date(this.currentDate.getFullYear(), this.currentDate.getMonth() + 1, 1);
    },

    goToToday() {
      this.currentDate = new Date();
    },

    selectDay(day) {
      if (day.events.length > 0) {
        this.selectedDay = day;
      }
    },

    closeDayModal() {
      this.selectedDay = null;
    },

    viewEvent(event) {
      this.selectedEvent = event;
    },

    viewEventFromDay(event) {
      this.selectedDay = null;
      this.selectedEvent = event;
    },

    closeModal() {
      this.selectedEvent = null;
    },

    formatSelectedDayDate() {
      if (!this.selectedDay) return '';
      return this.selectedDay.fullDate.toLocaleDateString('en-US', {
        weekday: 'long',
        year: 'numeric',
        month: 'long',
        day: 'numeric'
      });
    },

    formatDate(dateString) {
      const date = new Date(dateString);
      return date.toLocaleDateString('en-US', {
        weekday: 'long',
        year: 'numeric',
        month: 'long',
        day: 'numeric'
      });
    },

    formatEventDate(date) {
      if (!date) return 'No deadline set';
      return date.toLocaleDateString('en-US', {
        weekday: 'long',
        year: 'numeric',
        month: 'long',
        day: 'numeric'
      });
    },

    cleanup() {
      if (this.statusUpdateInterval) {
        clearInterval(this.statusUpdateInterval);
      }
      if (this.fastUpdateInterval) {
        clearInterval(this.fastUpdateInterval);
      }
      if (this.realTimeSubscription) {
        this.realTimeSubscription.unsubscribe();
      }
    }
  },
  mounted() {
    this.initializeData();
    
    this.statusUpdateInterval = setInterval(() => {
      this.updateCurrentTime();
    }, 60000);
    
    this.fastUpdateInterval = setInterval(() => {
      this.updateCurrentTime();
    }, 30000);
  },

  beforeUnmount() {
    this.cleanup();
  }
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

/* === NEW STYLES FOR TAKE QUIZ BUTTONS === */
.take-quiz-btn {
  background: linear-gradient(135deg, #3D8D7A 0%, #4dbb98 100%);
  color: var(--text-inverse);
  border: none;
  border-radius: 8px;
  padding: 0.5rem 1rem;
  cursor: pointer;
  transition: all 0.3s ease;
  font-weight: 600;
  font-size: 0.875rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-family: 'Inter', sans-serif;
}

.take-quiz-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(61, 141, 122, 0.3);
}

.take-quiz-btn:disabled {
  background: #ccc;
  cursor: not-allowed;
  opacity: 0.6;
}

.take-quiz-btn-modal {
  background: linear-gradient(135deg, #3D8D7A 0%, #4dbb98 100%);
  color: var(--text-inverse);
  border: none;
  border-radius: 12px;
  padding: 0.875rem 1.5rem;
  cursor: pointer;
  transition: all 0.3s ease;
  font-weight: 600;
  font-size: 0.875rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-family: 'Inter', sans-serif;
  width: 100%;
  justify-content: center;
}

.take-quiz-btn-modal:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(61, 141, 122, 0.3);
}

.quick-take-quiz-btn {
  background: linear-gradient(135deg, #3D8D7A 0%, #4dbb98 100%);
  color: var(--text-inverse);
  border: none;
  border-radius: 8px;
  width: 32px;
  height: 32px;
  cursor: pointer;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  justify-content: center;
}

.quick-take-quiz-btn:hover {
  transform: scale(1.1);
  box-shadow: 0 4px 12px rgba(61, 141, 122, 0.3);
}

.modal-info {
  padding-top: 1rem;
  border-top: 1px solid rgba(61, 141, 122, 0.1);
}

.completed-message {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 1rem;
  background: rgba(34, 197, 94, 0.1);
  border-radius: 12px;
  color: #16a34a;
  font-weight: 600;
}

.completed-message svg {
  color: #16a34a;
}

.overdue-message {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 1rem;
  background: rgba(245, 158, 11, 0.1);
  border-radius: 12px;
  color: #d97706;
  font-weight: 600;
}

.overdue-message svg {
  color: #d97706;
}

/* === EXISTING STYLES === */
.header-flex-align {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
}
.section-header-stats.align-top {
  align-items: flex-start;
  margin-top: 0.1rem;
}
.minimal-header-card {
  border-radius: 28px;
  box-shadow: 0 8px 32px 0 var(--shadow-strong);
  background: var(--bg-card);
  border: 1.5px solid var(--border-color-hover);
  padding: 3.5rem 4.5rem;
  min-height: 170px;
  gap: 3.5rem;
  margin-bottom: 2.2rem;
}
.minimal-header-icon {
  width: 88px;
  height: 88px;
  background: #4dbb98;
  border-radius: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--text-inverse);
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
  color: var(--text-inverse);
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

* {
  box-sizing: border-box;
}

.loading-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 60vh;
  gap: 2rem;
}

.loading-spinner {
  width: 60px;
  height: 60px;
  border: 4px solid rgba(61, 141, 122, 0.1);
  border-left: 4px solid #3D8D7A;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

.loading-text {
  font-size: 1.25rem;
  color: #3D8D7A;
  font-weight: 600;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.error-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 60vh;
  gap: 1.5rem;
  text-align: center;
}

.error-icon {
  font-size: 4rem;
}

.error-title {
  font-size: 1.75rem;
  color: #dc2626;
  font-weight: 700;
  margin: 0;
}

.error-message {
  font-size: 1.1rem;
  color: var(--text-secondary);
  margin: 0;
}

.retry-btn {
  background: linear-gradient(135deg, #3D8D7A 0%, #A3D1C6 100%);
  color: var(--text-inverse);
  border: none;
  border-radius: 12px;
  padding: 1rem 2rem;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  font-family: 'Inter', sans-serif;
}

.retry-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(61, 141, 122, 0.3);
}

.notifications-container {
  position: fixed;
  top: 2rem;
  right: 2rem;
  z-index: 2000;
  display: flex;
  flex-direction: column;
  gap: 1rem;
  max-width: 400px;
}

.notification {
  background: var(--bg-card);
  border-radius: 12px;
  padding: 1rem 1.5rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  box-shadow: 0 8px 32px var(--shadow-medium);
  border-left: 4px solid;
  cursor: pointer;
  transition: all 0.3s ease;
  animation: slideIn 0.3s ease;
}

.notification:hover {
  transform: translateY(-2px);
  box-shadow: 0 12px 40px rgba(0, 0, 0, 0.2);
}

.notification.success {
  border-left-color: #22c55e;
  background: linear-gradient(135deg, rgba(34, 197, 94, 0.05) 0%, rgba(255, 255, 255, 1) 100%);
}

.notification.error {
  border-left-color: #dc2626;
  background: linear-gradient(135deg, rgba(220, 38, 38, 0.05) 0%, rgba(255, 255, 255, 1) 100%);
}

.notification.warning {
  border-left-color: #f59e0b;
  background: linear-gradient(135deg, rgba(245, 158, 11, 0.05) 0%, rgba(255, 255, 255, 1) 100%);
}

.notification.info {
  border-left-color: #3D8D7A;
  background: linear-gradient(135deg, rgba(61, 141, 122, 0.05) 0%, rgba(255, 255, 255, 1) 100%);
}

.notification-content {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  flex: 1;
}

.notification-icon {
  font-size: 1.25rem;
}

.notification-message {
  font-size: 0.9rem;
  font-weight: 600;
  color: #333;
}

.notification-close {
  background: none;
  border: none;
  font-size: 1.5rem;
  color: #666;
  cursor: pointer;
  padding: 0.25rem;
  transition: color 0.3s ease;
}

.notification-close:hover {
  color: #333;
}

@keyframes slideIn {
  from {
    transform: translateX(100%);
    opacity: 0;
  }
  to {
    transform: translateX(0);
    opacity: 1;
  }
}

.live-indicator {
  animation: pulse 2s infinite;
}

@keyframes pulse {
  0%, 100% {
    opacity: 1;
  }
  50% {
    opacity: 0.5;
  }
}

.calendar-container {
  padding: 2rem;
  max-width: 1400px;
  margin: 0 auto;
  font-family: 'Inter', sans-serif;
  background: var(--bg-primary);
  min-height: 100vh;
}

.status-legend {
  background: var(--bg-card);
  backdrop-filter: blur(20px);
  border-radius: 20px;
  padding: 1.5rem 2rem;
  margin-bottom: 2rem;
  margin-top: 1.5rem;
  display: flex;
  justify-content: center;
  gap: 4.5rem;
  box-shadow: 0 8px 32px var(--shadow-light);
  border: 1px solid var(--border-color);
}

.legend-item {
  display: flex;
  align-items: center;
  gap: 0.9rem;
  font-size: 0.95rem;
  font-weight: 600;
  color: var(--text-secondary);
}

.legend-color {
  width: 18px;
  height: 18px;
  border-radius: 50%;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.legend-color.upcoming {
  background: linear-gradient(135deg, #3D8D7A 0%, #A3D1C6 100%);
}

.legend-color.due-today {
  background: linear-gradient(135deg, #ff6b6b 0%, #ee5a52 100%);
}

.legend-color.completed {
  background: linear-gradient(135deg, #22c55e 0%, #16a34a 100%);
}

.legend-color.overdue {
  background: linear-gradient(135deg, #fbbf24 0%, #f59e0b 100%);
}

.calendar-nav {
  background: var(--bg-card);
  backdrop-filter: blur(20px);
  border-radius: 20px;
  padding: 2rem;
  margin-bottom: 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  box-shadow: 0 8px 32px var(--shadow-light);
  border: 1px solid var(--border-color);
}

.nav-controls {
  display: flex;
  align-items: center;
  gap: 2rem;
}

.nav-btn {
  background: rgba(251, 255, 228, 0.8);
  border: 1px solid rgba(61, 141, 122, 0.1);
  border-radius: 12px;
  width: 44px;
  height: 44px;
  cursor: pointer;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #3D8D7A;
}

.nav-btn:hover {
  background: rgba(61, 141, 122, 0.1);
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(61, 141, 122, 0.15);
}

.current-month {
  font-size: 1.75rem;
  font-weight: 700;
  color: #3D8D7A;
  margin: 0;
  min-width: 220px;
  text-align: center;
}

.view-toggle {
  display: flex;
  gap: 0.5rem;
  background: var(--bg-accent);
  padding: 0.5rem;
  border-radius: 16px;
}

.view-btn {
  background: transparent;
  border: none;
  border-radius: 12px;
  padding: 0.75rem 1.5rem;
  cursor: pointer;
  transition: all 0.3s ease;
  font-weight: 600;
  color: #3D8D7A;
  font-family: 'Inter', sans-serif;
}

.view-btn:hover {
  background: rgba(61, 141, 122, 0.1);
}

.view-btn.active {
  background: linear-gradient(135deg, #3D8D7A 0%, #A3D1C6 100%);
  color: var(--text-inverse);
  box-shadow: 0 4px 16px rgba(61, 141, 122, 0.2);
}

.calendar-content {
  background: var(--bg-card);
  backdrop-filter: blur(20px);
  border-radius: 24px;
  padding: 2.5rem;
  box-shadow: 0 12px 40px var(--shadow-medium);
  border: 1px solid var(--border-color);
}

.calendar-grid {
  width: 100%;
}

.calendar-header {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  gap: 2px;
  margin-bottom: 1.5rem;
}

.day-header {
  padding: 1.25rem;
  text-align: center;
  font-weight: 700;
  color: var(--text-accent);
  background: var(--bg-secondary);
  border-radius: 12px;
  font-size: 0.9rem;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.calendar-body {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  gap: 2px;
}

.calendar-day {
  min-height: 130px;
  padding: 1rem;
  background: var(--input-bg);
  border-radius: 12px;
  transition: all 0.3s ease;
  display: flex;
  flex-direction: column;
  position: relative;
  border: 2px solid transparent;
}

.calendar-day.clickable {
  cursor: pointer;
}

.calendar-day.clickable:hover {
  background: var(--input-bg);
  transform: translateY(-2px);
  box-shadow: 0 8px 25px var(--shadow-medium);
}

.calendar-day.other-month {
  opacity: 0.4;
}

.calendar-day.today {
  background: linear-gradient(135deg, rgba(61, 141, 122, 0.15) 0%, rgba(163, 209, 198, 0.15) 100%);
  border-color: #3D8D7A;
  box-shadow: 0 4px 16px rgba(61, 141, 122, 0.2);
}

.calendar-day.has-due-today {
  border-color: #ff6b6b;
  background: linear-gradient(135deg, rgba(255, 107, 107, 0.15) 0%, rgba(238, 90, 82, 0.1) 100%);
}

.calendar-day.has-overdue {
  border-color: #fbbf24;
  background: linear-gradient(135deg, rgba(251, 191, 36, 0.15) 0%, rgba(245, 158, 11, 0.1) 100%);
}

.calendar-day.has-upcoming {
  border-color: #3D8D7A;
}

.day-number {
  font-weight: 700;
  color: #3D8D7A;
  margin-bottom: 0.75rem;
  font-size: 1.1rem;
}

.day-events {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.event-dot {
  width: 100%;
  height: 8px;
  border-radius: 4px;
  margin-bottom: 2px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.event-dot.upcoming {
  background: linear-gradient(135deg, #3D8D7A 0%, #A3D1C6 100%);
}

.event-dot.due-today {
  background: linear-gradient(135deg, #ff6b6b 0%, #ee5a52 100%);
}

.event-dot.completed {
  background: linear-gradient(135deg, #22c55e 0%, #16a34a 100%);
}

.event-dot.overdue {
  background: linear-gradient(135deg, #fbbf24 0%, #f59e0b 100%);
}

.more-events {
  font-size: 0.7rem;
  color: #666;
  font-weight: 600;
  text-align: center;
  margin-top: 0.5rem;
  padding: 0.25rem;
  background: rgba(61, 141, 122, 0.1);
  border-radius: 6px;
}

.event-count {
  position: absolute;
  top: 0.5rem;
  right: 0.5rem;
  background: linear-gradient(135deg, #3D8D7A 0%, #A3D1C6 100%);
  color: var(--text-inverse);
  border-radius: 50%;
  width: 24px;
  height: 24px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.75rem;
  font-weight: 700;
  box-shadow: 0 2px 8px rgba(61, 141, 122, 0.3);
}

.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
  backdrop-filter: blur(4px);
}

.day-modal-content {
  background: var(--card-background);
  border-radius: 24px;
  padding: 0;
  max-width: 600px;
  width: 90%;
  max-height: 80vh;
  overflow: hidden;
  box-shadow: 0 20px 60px rgba(61, 141, 122, 0.25);
  border: 1px solid rgba(61, 141, 122, 0.1);
}

.day-modal-header {
  background: linear-gradient(135deg, #3D8D7A 0%, #A3D1C6 100%);
  color: var(--text-inverse);
  padding: 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.day-modal-header h3 {
  font-size: 1.5rem;
  font-weight: 700;
  margin: 0;
}

.close-btn {
  background: none;
  border: none;
  cursor: pointer;
  color: rgba(255, 255, 255, 0.8);
  padding: 0.5rem;
  border-radius: 8px;
  transition: all 0.3s ease;
}

.close-btn:hover {
  background: rgba(255, 255, 255, 0.1);
  color: var(--text-inverse);
}

.day-modal-body {
  padding: 2rem;
  overflow-y: auto;
  max-height: 60vh;
}

.day-events-summary {
  margin-bottom: 2rem;
}

.summary-stats {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1rem;
}

.summary-stat {
  background: rgba(251, 255, 228, 0.5);
  border-radius: 16px;
  padding: 1.5rem;
  text-align: center;
  border: 1px solid rgba(61, 141, 122, 0.1);
}

.summary-number {
  display: block;
  font-size: 2rem;
  font-weight: 800;
  color: #3D8D7A;
  line-height: 1;
}

.summary-label {
  font-size: 0.75rem;
  font-weight: 600;
  color: #777;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-top: 0.5rem;
}

.day-events-list h4 {
  font-size: 1.25rem;
  font-weight: 700;
  color: #3D8D7A;
  margin-bottom: 1.5rem;
}

.day-event-items {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.day-event-item {
  background: rgba(251, 255, 228, 0.3);
  border-radius: 16px;
  padding: 1.5rem;
  display: flex;
  align-items: flex-start;
  gap: 1rem;
  transition: all 0.3s ease;
  border-left: 4px solid;
}

.day-event-item:hover {
  background: rgba(251, 255, 228, 0.6);
  transform: translateX(4px);
}

.day-event-item.upcoming {
  border-left-color: #3D8D7A;
}

.day-event-item.due-today {
  border-left-color: #ff6b6b;
  background: rgba(255, 107, 107, 0.1);
}

.day-event-item.completed {
  border-left-color: #22c55e;
  background: rgba(34, 197, 94, 0.1);
}

.day-event-item.overdue {
  border-left-color: #fbbf24;
  background: rgba(251, 191, 36, 0.1);
}

.event-status-indicator {
  margin-top: 0.25rem;
}

.status-dot {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
}

.status-dot.upcoming {
  background: #3D8D7A;
}

.status-dot.due-today {
  background: #ff6b6b;
}

.status-dot.completed {
  background: #22c55e;
}

.status-dot.overdue {
  background: #fbbf24;
}

.event-details {
  flex: 1;
}

.event-name {
  font-size: 1.1rem;
  font-weight: 700;
  color: #3D8D7A;
  margin-bottom: 0.25rem;
}

.event-subject-small {
  font-size: 0.875rem;
  color: #777;
  margin-bottom: 0.25rem;
}

.event-time-small {
  font-size: 0.875rem;
  font-weight: 600;
  color: #3D8D7A;
  margin-bottom: 0.5rem;
}

.event-desc-small {
  font-size: 0.875rem;
  color: #666;
  margin: 0;
}

.event-status-text {
  display: flex;
  align-items: center;
  margin-top: 0.25rem;
}

.status-badge-small {
  font-size: 0.7rem;
  font-weight: 600;
  text-transform: uppercase;
  padding: 0.25rem 0.75rem;
  border-radius: 8px;
  letter-spacing: 0.5px;
}

.status-badge-small.upcoming {
  background: rgba(61, 141, 122, 0.2);
  color: #3D8D7A;
}

.status-badge-small.due-today {
  background: rgba(255, 107, 107, 0.2);
  color: #dc2626;
}

.status-badge-small.completed {
  background: rgba(34, 197, 94, 0.2);
  color: #16a34a;
}

.status-badge-small.overdue {
  background: rgba(251, 191, 36, 0.2);
  color: #d97706;
}

.event-quick-actions {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.quick-view-btn {
  background: rgba(61, 141, 122, 0.1);
  border: 1px solid rgba(61, 141, 122, 0.2);
  border-radius: 8px;
  width: 32px;
  height: 32px;
  cursor: pointer;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #3D8D7A;
}

.quick-view-btn:hover {
  background: rgba(61, 141, 122, 0.2);
  transform: scale(1.1);
}

.events-list {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.day-group {
  border-bottom: 1px solid rgba(61, 141, 122, 0.1);
  padding-bottom: 1.5rem;
}

.day-title {
  font-size: 1.25rem;
  font-weight: 700;
  color: #3D8D7A;
  margin-bottom: 1rem;
}

.events-container {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.event-item {
  background: var(--input-bg);
  border-radius: 16px;
  padding: 1.5rem;
  display: flex;
  align-items: center;
  gap: 1.5rem;
  transition: all 0.3s ease;
  border-left: 4px solid;
}

.event-item:hover {
  background: var(--input-bg);
  transform: translateX(4px);
}

.event-item.upcoming {
  border-left-color: #3D8D7A;
}

.event-item.due-today {
  border-left-color: #ff6b6b;
  background: rgba(255, 107, 107, 0.1);
}

.event-item.completed {
  border-left-color: #22c55e;
  background: rgba(34, 197, 94, 0.1);
}

.event-item.overdue {
  border-left-color: #fbbf24;
  background: rgba(251, 191, 36, 0.1);
}

.event-time {
  font-weight: 700;
  color: #3D8D7A;
  min-width: 80px;
}

.event-content {
  flex: 1;
}

.event-title {
  font-size: 1.1rem;
  font-weight: 700;
  color: var(--text-primary);
  margin-bottom: 0.25rem;
}

.event-subject {
  font-size: 0.875rem;
  color: #777;
  margin-bottom: 0.25rem;
}

.event-description {
  font-size: 0.875rem;
  color: #666;
  margin-bottom: 0.5rem;
}

.event-status-badge {
  display: inline-block;
}

.status-badge {
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
  padding: 0.25rem 0.75rem;
  border-radius: 12px;
  letter-spacing: 0.5px;
}

.status-badge.upcoming {
  background: rgba(61, 141, 122, 0.2);
  color: #3D8D7A;
}

.status-badge.due-today {
  background: rgba(255, 107, 107, 0.2);
  color: #dc2626;
}

.status-badge.completed {
  background: rgba(34, 197, 94, 0.2);
  color: #16a34a;
}

.status-badge.overdue {
  background: rgba(251, 191, 36, 0.2);
  color: #d97706;
}

.event-actions {
  display: flex;
  gap: 0.5rem;
  align-items: center;
}

.view-btn-small {
  background: rgba(61, 141, 122, 0.1);
  border: 1px solid rgba(61, 141, 122, 0.2);
  border-radius: 8px;
  width: 32px;
  height: 32px;
  cursor: pointer;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #3D8D7A;
}

.view-btn-small:hover {
  background: rgba(61, 141, 122, 0.2);
  transform: scale(1.1);
}

.modal-content {
  background: var(--card-background);
  border-radius: 24px;
  padding: 2rem;
  max-width: 500px;
  width: 90%;
  max-height: 80vh;
  overflow-y: auto;
  box-shadow: 0 20px 60px rgba(61, 141, 122, 0.25);
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1.5rem;
  padding-bottom: 1rem;
  border-bottom: 1px solid rgba(61, 141, 122, 0.1);
}

.modal-header h3 {
  font-size: 1.5rem;
  font-weight: 700;
  color: #3D8D7A;
  margin: 0;
}

.modal-header .close-btn {
  color: #666;
}

.modal-header .close-btn:hover {
  background: rgba(61, 141, 122, 0.1);
  color: #3D8D7A;
}

.modal-body {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.event-detail {
  display: flex;
  gap: 1rem;
  padding: 0.75rem 0;
  border-bottom: 1px solid rgba(61, 141, 122, 0.05);
  align-items: center;
}

.event-detail strong {
  min-width: 100px;
  color: #3D8D7A;
  font-weight: 600;
}

.modal-actions {
  padding-top: 1rem;
  border-top: 1px solid rgba(61, 141, 122, 0.1);
}

@media (max-width: 768px) {
  .calendar-container {
    padding: 1rem;
  }
  
  .minimal-header-card {
    flex-direction: column;
    text-align: center;
    gap: 2rem;
    padding: 2rem;
  }
  
  .section-header-left {
    flex-direction: column;
    text-align: center;
  }
  
  .section-header-stats {
    flex-direction: row;
    justify-content: center;
  }
  
  .minimal-header-title {
    font-size: 2rem;
  }
  
  .status-legend {
    flex-wrap: wrap;
    gap: 1rem;
  }
  
  .calendar-nav {
    flex-direction: column;
    gap: 1.5rem;
  }
  
  .nav-controls {
    justify-content: center;
  }
  
  .calendar-day {
    min-height: 100px;
    padding: 0.75rem;
  }
  
  .day-header {
    padding: 0.75rem;
    font-size: 0.8rem;
  }
  
  .event-item {
    flex-direction: column;
    align-items: flex-start;
    gap: 1rem;
  }
  
  .event-time {
    min-width: auto;
  }
  
  .event-actions {
    width: 100%;
    justify-content: space-between;
  }
  
  .day-modal-content {
    max-width: 95%;
  }
  
  .summary-stats {
    grid-template-columns: 1fr;
  }
  
  .day-event-item {
    flex-direction: column;
    align-items: flex-start;
    gap: 1rem;
  }
  
  .event-quick-actions {
    flex-direction: row;
    width: 100%;
    justify-content: flex-end;
  }
}
</style>