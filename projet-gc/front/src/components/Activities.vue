// Updated frontend with pagination and backend connection.

<template>
  <div class="activities-page">
    <header class="header">
      <h1>Activités à Montpellier</h1>
      <div class="actions">
        <input
          type="text"
          placeholder="Rechercher une activité..."
          v-model="searchTerm"
          @input="fetchActivities"
        />
        <button @click="toggleFilter" class="filter-btn">Filtrer</button>
      </div>
    </header>
    <div class="activities-grid">
      <ActivityCard
        v-for="activity in paginatedActivities"
        :key="activity.id"
        :activity="activity"
      />
    </div>
    <div class="pagination">
      <button @click="previousPage" :disabled="currentPage === 1">Précédent</button>
      <span>Page {{ currentPage }} sur {{ totalPages }}</span>
      <button @click="nextPage" :disabled="currentPage === totalPages">Suivant</button>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import ActivityCard from "@/components/ActivityCard.vue";

export default {
  components: { ActivityCard },
  data() {
    return {
      activities: [],
      searchTerm: "",
      currentPage: 1,
      itemsPerPage: 6,
    };
  },
  computed: {
    totalPages() {
      return Math.ceil(this.activities.length / this.itemsPerPage);
    },
    paginatedActivities() {
      const start = (this.currentPage - 1) * this.itemsPerPage;
      const end = start + this.itemsPerPage;
      return this.activities.slice(start, end);
    },
  },
  created() {
    this.fetchActivities();
  },
  methods: {
    async fetchActivities() {
      try {
        const response = await axios.get("http://localhost:5000/api/activities", {
          params: { search: this.searchTerm },
        });
        this.activities = response.data;
      } catch (error) {
        console.error("Erreur lors de la récupération des activités :", error);
      }
    },
    toggleFilter() {
      alert("Filtrage avancé à implémenter !");
    },
    previousPage() {
      if (this.currentPage > 1) this.currentPage--;
    },
    nextPage() {
      if (this.currentPage < this.totalPages) this.currentPage++;
    },
  },
};
</script>

<style scoped>
.activities-page {
  padding: 16px;
}
.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 16px;
}
.actions input {
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
}
.filter-btn {
  padding: 8px 16px;
  background-color: #6200ea;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
.filter-btn:hover {
  background-color: #4b00b8;
}
.activities-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 16px;
}
.pagination {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 16px;
}
.pagination button {
  padding: 8px 16px;
  background-color: #6200ea;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  margin: 0 8px;
}
.pagination button:disabled {
  background-color: #ddd;
  cursor: not-allowed;
}
</style>
