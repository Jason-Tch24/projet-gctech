const db = require("../config/firebase");

const Activite = {
  // Récupérer toutes les activités
  async getAll() {
    const snapshot = await db.collection("activities").get();
    return snapshot.docs.map(doc => ({ id: doc.id, ...doc.data() }));
  },

  // Récupérer une activité par ID
  async getById(id) {
    const doc = await db.collection("activities").doc(id).get();
    return doc.exists ? { id: doc.id, ...doc.data() } : null;
  },

  // Ajouter une nouvelle activité
  async create(data) {
    const docRef = await db.collection("activities").add(data);
    return { id: docRef.id };
  },

  // Supprimer une activité
  async delete(id) {
    await db.collection("activities").doc(id).delete();
    return { message: "Activité supprimée !" };
  }
};

module.exports = Activite;
