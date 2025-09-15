import { createRouter, createWebHistory } from 'vue-router'

// Import all necessary components
import Intro from '@/views/Intro.vue'
import Landing from '@/views/Landing.vue'
import Login from '@/views/Login.vue'
import Signup from '@/views/Signup.vue'
import SignupStudent from '@/views/SignupStudent.vue'
import RoleSelection from '@/views/RoleSelection.vue'
import StudentDashboard from '@/views/StudentDashboard.vue'
import TeacherDashboard from '@/views/TeacherDashboard.vue'

// Teacher Dashboard children components
import DashboardHome from '@/views/teacher/DashboardHome.vue'
import MyClasses from '@/views/teacher/MyClasses.vue'
import ClassDetails from '@/views/teacher/ClassDetails.vue'
import MessagesPage from '@/views/MessagesPage.vue'
import AssessmentResults from '@/views/teacher/AssessmentResults.vue'  // Importing the AssessmentResults component
import CreateClass from '@/views/teacher/CreateClass.vue'
import CreateQuiz from '@/views/teacher/CreateQuiz.vue'
import SettingsPage from '@/views/SettingsPage.vue' // New import for SettingsPage
import UploadAssessment from '@/components/UploadAssessment.vue' // New component for uploading assessments
import EditClass from '@/views/teacher/EditClass.vue' // New import for EditClass
import ClassStudents from '@/views/teacher/ClassStudents.vue' // New import for ClassStudents

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
  { path: '/', name: 'intro', component: Intro },
  { path: '/landing', name: 'landing', component: Landing },
    { path: '/login', name: 'login', component: Login },
    { path: '/signup', name: 'signup', component: Signup },
    { path: '/signup-student', name: 'signupStudent', component: SignupStudent },
    { path: '/role-selection', name: 'roleSelection', component: RoleSelection },
    { path: '/student-dashboard', name: 'studentDashboard', component: StudentDashboard, meta: { requiresAuth: true } },

    {
      path: '/teacher',
      component: TeacherDashboard,
      meta: { requiresAuth: true },
      children: [
        {
          path: '',
          redirect: 'dashboard'
        },
        {
          path: 'dashboard',
          name: 'DashboardHome',
          component: DashboardHome
        },
        {
          path: 'classes',
          name: 'MyClasses',
          component: MyClasses
        },
        {
          path: 'classes/:id',
          name: 'ClassDetails',
          component: ClassDetails,
          props: true
        },
        {
          path: 'edit-class/:id',
          name: 'EditClass',
          component: EditClass,
          props: true
        },
        {
          path: 'class-students/:id',
          name: 'ClassStudents',
          component: ClassStudents,
          props: true
        },
        {
          path: 'messages',
          name: 'MessagesPage',
          component: MessagesPage
        },
        {
          path: 'settings', 
          name: 'SettingsPage',
          component: SettingsPage
        },
        {
          path: 'assessments/:id/results',
          name: 'AssessmentResults',
          component: AssessmentResults,
          props: true
        },
        {
          path: 'create-class',
          name: 'CreateClass',
          component: CreateClass
        },
        {
          path: 'classes/:classId/create-quiz',
          name: 'CreateQuiz',
          component: CreateQuiz,
          props: true
        },
        // New route for uploading assessments
        {
          path: 'upload-assessment',
          name: 'UploadAssessment',
          component: UploadAssessment,
        }
      ]
    }
  ]
})

export default router