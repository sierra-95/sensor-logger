const mysql = require('mysql');
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
module.exports = db;
