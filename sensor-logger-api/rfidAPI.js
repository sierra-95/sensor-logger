const express = require('express');
const mysql = require('mysql');
const router = express.Router();


const db = mysql.createConnection({
  host: 'localhost',
  user: 'ubuntu',
  password: 'Michael@92!7',
  database: 'sensor_data',
});

db.connect((err) => {
  if (err) {
    console.error('Database connection error: ' + err.message);
  } else {
    console.log('Database connection is active.');
  }
});

// Define API endpoint for RFID data
router.get('/', (req, res) => {
  db.query('SELECT * FROM rfid_data', (error, results) => {
    if (error) {
      res.status(500).json({ error: 'Database error' });
    } else {
      res.status(200).json(results);
    }
  });
});

module.exports = router;
