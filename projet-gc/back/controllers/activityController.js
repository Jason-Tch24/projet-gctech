const Activite = require("../models/activityModel");

const activityController = {
  // Récupérer toutes les activités
  async getAll(req, res) {
    try {
      const activites = await Activite.getAll();
      res.status(200).json(activites);
    } catch (error) {
      res.status(500).json({ error: "Erreur lors de la récupération des activités" });
    }
  },

  // Récupérer une activité par ID
  async getById(req, res) {
    try {
      const activite = await Activite.getById(req.params.id);
      if (activite) {
        res.status(200).json(activite);
      } else {
        res.status(404).json({ error: "Activité non trouvée" });
      }
    } catch (error) {
      res.status(500).json({ error: "Erreur lors de la récupération de l'activité" });
    }
  },

  // Créer une nouvelle activité
  async create(req, res) {
    try {
      const { titre, image, categorie, description, reservation, prix, adresse } = req.body;
      const newActivite = { titre, image, categorie, description, reservation, prix, adresse };
      const result = await Activite.create(newActivite);
      res.status(201).json({ message: "Activité créée avec succès", id: result.id });
    } catch (error) {
      res.status(500).json({ error: "Erreur lors de l'ajout de l'activité" });
    }
  },

  // Supprimer une activité
  async delete(req, res) {
    try {
      await Activite.delete(req.params.id);
      res.status(200).json({ message: "Activité supprimée avec succès" });
    } catch (error) {
      res.status(500).json({ error: "Erreur lors de la suppression de l'activité" });
    }
  }
};

module.exports = activityController;
