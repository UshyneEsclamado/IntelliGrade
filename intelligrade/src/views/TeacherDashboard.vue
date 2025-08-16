<template>
  <div class="dashboard-wrapper">
    <h1>Teacher Dashboard</h1>
    <p>Welcome, teacher!</p>

    <!-- Core Feature: Assessments to Grade / Auto-Check -->
    <section class="core-feature">
      <h2>Assessments to Grade / Auto-Check</h2>
      <button @click="uploadAssessment">Upload Assessment</button>
      <div class="stats">
        <p>Students graded automatically: {{ stats.autoGradedCount }}</p>
        <p>Average score: {{ stats.averageScore }}</p>
      </div>
      <ul>
        <li v-for="assessment in assessmentsToGrade" :key="assessment.id">
          {{ assessment.title }} - {{ assessment.status }}
          <button @click="gradeAssessment(assessment.id)">Auto-Check</button>
        </li>
      </ul>
    </section>

    <!-- Secondary Features -->
    <section class="secondary-features">
      <h2>Create Online Quiz</h2>
      <button @click="createQuiz">Create Quiz</button>

      <h2>View Results</h2>
      <button @click="viewResults">View Student Results</button>

      <h2>Teacher–Student Chat</h2>
      <button @click="openChat">Open Chat</button>

      <h2>Notifications</h2>
      <ul>
        <li v-for="note in notifications" :key="note.id">{{ note.message }}</li>
      </ul>

      <h2>Performance Analytics</h2>
      <!-- Placeholder for analytics graphs -->
      <div class="analytics-graphs">
        <p>Average scores, missed questions, trends over time...</p>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: "TeacherDashboard",
  data() {
    return {
      assessmentsToGrade: [
        // Example data
        { id: 1, title: "Math Quiz 1", status: "Pending" },
        { id: 2, title: "Science Test", status: "Pending" }
      ],
      stats: {
        autoGradedCount: 0,
        averageScore: 0
      },
      notifications: [
        // Example notifications
        { id: 1, message: "Student A submitted Quiz 1" },
        { id: 2, message: "Upcoming deadline for Science Test" }
      ]
    }
  },
  methods: {
    uploadAssessment() {
      // Logic for uploading assessment
      alert("Upload Assessment clicked");
    },
    gradeAssessment(id) {
      // Logic for auto-checking assessment
      alert(`Auto-Check for assessment ${id}`);
    },
    createQuiz() {
      // Logic for creating quiz
      alert("Create Quiz clicked");
    },
    viewResults() {
      // Logic for viewing results
      alert("View Results clicked");
    },
    openChat() {
      // Logic for opening chat
      alert("Open Chat clicked");
    }
  }
}
</script>

<style scoped>
.dashboard-wrapper {
  max-width: 900px;
  margin: 0 auto;
  padding: 32px;
}
.core-feature {
  background: #f6fff2;
  border-radius: 12px;
  padding: 24px;
  margin-bottom: 32px;
  box-shadow: 0 2px 8px rgba(61,141,122,0.08);
}
.secondary-features > h2 {
  margin-top: 24px;
  color: #3D8D7A;
}
.stats {
  margin: 12px 0;
  color: #3D8D7A;
}
.analytics-graphs {
  background: #fff;
  border-radius: 8px;
  padding: 16px;
  margin-top: 12px;
  box-shadow: 0 1px 4px rgba(61,141,122,0.06);
}
button {
  background: linear-gradient(135deg, #3D8D7A, #A3D1C6);
  color: #fff;
  border: none;
  border-radius: 8px;
  padding: 8px 18px;
  margin: 8px 0;
  cursor: pointer;
  font-weight: 600;
}
button:hover {
  opacity: 0.85;
}
</style>