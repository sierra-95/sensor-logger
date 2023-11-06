const express = require('express');
const mysql = require('mysql');
const cors = require('cors');

const app = express();

const corsOptions = {
  origin: 'https://web-01.holb20233m8xq2.tech',
};

app.use(cors(corsOptions));

app.use(express.json());

// MySQL database configuration
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

// Define API endpoints
app.get('/api/humidity', (req, res) => {
  db.query('SELECT * FROM humidity_data', (error, results) => {
    if (error) {
      res.status(500).json({ error: 'Database error' });
    } else {
      res.status(200).json(results);
    }
  });
});

app.get('/api/rfid', (req, res) => {
  db.query('SELECT * FROM rfid_data', (error, results) => {
    if (error) {
      res.status(500).json({ error: 'Database error' });
    } else {
      res.status(200).json(results);
    }
  });
});

app.get('/api/temperature', (req, res) => {
  db.query('SELECT * FROM temperature_data', (error, results) => {
    if (error) {
      res.status(500).json({ error: 'Database error' });
    } else {
      res.status(200).json(results);
    }
  });
});

const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`API server is running on port ${port}`);
});
