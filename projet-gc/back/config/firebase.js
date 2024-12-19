var admin = require("firebase-admin");

var serviceAccount = require("../../../activity-6cc21-firebase-adminsdk-s3s1g-2c35f96f0c.json");

admin.initializeApp({
  credential: admin.credential.cert(serviceAccount),
  databaseURL: "https://activity-6cc21-default-rtdb.europe-west1.firebasedatabase.app"
});

const db = admin.firestore();
module.exports = db;