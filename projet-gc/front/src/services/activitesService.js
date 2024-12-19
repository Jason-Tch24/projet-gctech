import axios from "axios";

const apiClient = axios.create({
  baseURL: "http://localhost:3000/activites", // URL de ton backend
  headers: {
    "Content-Type": "application/json",
  },
});

export default {
  // Récupérer toutes les activités
  getAllActivites() {
    return apiClient.get("/");
  },

  // Ajouter une nouvelle activité
  createActivite(data) {
    return apiClient.post("/", data);
  },

  // Supprimer une activité
  deleteActivite(id) {
    return apiClient.delete(`/${id}`);
  },
};
