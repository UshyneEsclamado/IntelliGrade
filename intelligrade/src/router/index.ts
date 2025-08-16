import { createRouter, createWebHistory } from 'vue-router'

import Intro from '@/views/Intro.vue'
import Login from '@/views/Login.vue'
import Signup from '@/views/Signup.vue'
import SignupStudent from '@/views/SignupStudent.vue'
import RoleSelection from '@/views/RoleSelection.vue'
import StudentDashboard from '@/views/StudentDashboard.vue'
import TeacherDashboard from '@/views/TeacherDashboard.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/', name: 'intro', component: Intro },
    { path: '/login', name: 'login', component: Login },
    { path: '/signup', name: 'signup', component: Signup },
    { path: '/signup-student', name: 'signupStudent', component: SignupStudent },
    { path: '/role-selection', name: 'roleSelection', component: RoleSelection },
    { path: '/student-dashboard', name: 'studentDashboard', component: StudentDashboard, meta: { requiresAuth: true } },
    { path: '/teacher-dashboard', name: 'teacherDashboard', component: TeacherDashboard, meta: { requiresAuth: true } }
  ]
})

export default router