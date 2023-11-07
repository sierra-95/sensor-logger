const mysql = require('mysql');

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

    // Query the rfid_data table
    db.query('SELECT * FROM humidity_data', (error, results) => {
      if (error) {
        console.error('Error querying the database: ' + error);
      } else {
        console.log('RFID Data:');
        console.table(results);
      }

      // Close the database connection
      db.end();
    });
  }
});
