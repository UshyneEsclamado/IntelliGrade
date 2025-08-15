<template>
  <div class="teacher-home">
    <!-- Header -->
    <Header title="Teacher Dashboard" />

    <!-- Core Feature: Assessments to Grade -->
    <section class="core-feature">
      <h2>Assessments to Grade / Auto-Check</h2>
      <button class="upload-btn">Upload Assessment</button>

      <AssessmentList />
      <div class="stats">
        <div class="stat-card">
          <h3>Students Graded</h3>
          <p>120</p>
        </div>
        <div class="stat-card">
          <h3>Average Score</h3>
          <p>85%</p>
        </div>
      </div>
    </section>

    <!-- Secondary Features -->
    <section class="secondary-features">
      <h2>Quick Actions</h2>
      <div class="feature-cards">
        <DashboardCard title="Create Online Quiz" />
        <DashboardCard title="View Results" />
        <DashboardCard title="Teacher–Student Chat" />
        <DashboardCard title="Notifications" />
        <DashboardCard title="Performance Analytics" />
      </div>
    </section>
  </div>
</template>

<script>
import Header from "../components/Header.vue";
import DashboardCard from "../components/DashboardCard.vue";
import AssessmentList from "../components/AssessmentList.vue";

export default {
  components: { Header, DashboardCard, AssessmentList },
};
</script>

<style scoped>
.teacher-home {
  padding: 20px;
  background-color: #F0F5F9;
  min-height: 100vh;
  font-family: Arial, sans-serif;
}

.core-feature {
  background: white;
  padding: 20px;
  margin-bottom: 30px;
  border-radius: 10px;
  box-shadow: 0 2px 6px rgba(0,0,0,0.1);
}

.core-feature h2 {
  margin-bottom: 15px;
}

.upload-btn {
  padding: 10px 20px;
  background-color: #52616B;
  color: white;
  border: none;
  cursor: pointer;
  border-radius: 5px;
  margin-bottom: 20px;
}

.stats {
  display: flex;
  gap: 20px;
  margin-top: 20px;
}

.stat-card {
  background: #C9D6DF;
  padding: 15px;
  border-radius: 8px;
  flex: 1;
  text-align: center;
}

.secondary-features h2 {
  margin-bottom: 15px;
}

.feature-cards {
  display: flex;
  gap: 15px;
  flex-wrap: wrap;
}
</style>
