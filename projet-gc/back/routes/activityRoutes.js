const express = require("express");
const router = express.Router();
const activityController = require("../controllers/activityController");

// Routes CRUD pour les activités
router.get("/", activityController.getAll);           // Récupérer toutes les activités
router.get("/:id", activityController.getById);       // Récupérer une activité par ID
router.post("/", activityController.create);          // Ajouter une nouvelle activité
router.delete("/:id", activityController.delete);     // Supprimer une activité

module.exports = router;
