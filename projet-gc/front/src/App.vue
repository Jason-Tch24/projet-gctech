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
        <button @click="toggleForm" class="add-activity-btn">Ajouter une activité</button>
      </div>
    </header>

    <div v-if="showForm" class="activity-form">
      <h2>Ajouter une activité</h2>
      <form @submit.prevent="addActivity">
        <div class="form-group">
          <label for="title">Titre</label>
          <input type="text" id="title" v-model="newActivity.title" required />
        </div>
        <div class="form-group">
          <label for="category">Catégorie</label>
          <input type="text" id="category" v-model="newActivity.category" required />
        </div>
        <div class="form-group">
          <label for="location">Adresse</label>
          <input type="text" id="location" v-model="newActivity.location" required />
        </div>
        <div class="form-group">
          <label for="image">Image (URL)</label>
          <input type="url" id="image" v-model="newActivity.image" required />
        </div>
        <div class="form-group">
          <label for="price">Prix</label>
          <input type="number" id="price" v-model="newActivity.price" required />
        </div>
        <div class="form-group">
          <label for="description">Description</label>
          <textarea id="description" v-model="newActivity.description" required></textarea>
        </div>
        <button type="submit" class="submit-btn">Enregistrer</button>
      </form>
    </div>

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
      showForm: false,
      newActivity: {
        title: "",
        category: "",
        location: "",
        image: "",
        price: 0,
        description: "",
      },
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
        const response = await axios.get("http://localhost:3000/activites", {
          params: { search: this.searchTerm },
        });
        this.activities = response.data;
      } catch (error) {
        console.error("Erreur lors de la récupération des activités :", error);
      }
    },
    async addActivity() {
      try {
        const response = await axios.post("http://localhost:3000/activites", this.newActivity);
        this.activities.push(response.data);
        this.newActivity = { title: "", category: "", location: "", image: "", price: 0, description: "" };
        this.showForm = false;
      } catch (error) {
        console.error("Erreur lors de l'ajout de l'activité :", error);
      }
    },
    toggleFilter() {
      alert("Filtrage avancé à implémenter !");
    },
    toggleForm() {
      this.showForm = !this.showForm;
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
.filter-btn,
.add-activity-btn {
  padding: 8px 16px;
  background-color: #6200ea;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  margin-left: 8px;
}
.filter-btn:hover,
.add-activity-btn:hover {
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
.activity-form {
  margin: 16px 0;
  padding: 16px;
  border: 1px solid #ddd;
  border-radius: 8px;
  background-color: #f9f9f9;
}
.form-group {
  margin-bottom: 16px;
}
.form-group label {
  display: block;
  margin-bottom: 8px;
  font-weight: bold;
  color: #000;
}
.form-group input,
.form-group textarea {
  width: 100%;
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
}
.submit-btn {
  padding: 8px 16px;
  background-color: #6200ea;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
.submit-btn:hover {
  background-color: #4b00b8;
}
</style>
