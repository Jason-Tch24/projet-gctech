const express = require ("express")
const cors = require ("cors")
const activityRoutes = require ("./routes/activityRoutes")
const port = process.env.PORT || 3000

const app = express();

app.get("/", (req, res) => {
    res.json({message: "Bienvenue"})
})

// Middleware
app.use(cors());
app.use(express.json());

// Routes
app.use("/activites", activityRoutes);

app.listen(port, () => {
    console.log("serveur marche");
})
