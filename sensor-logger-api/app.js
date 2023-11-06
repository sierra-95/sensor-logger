const express = require('express');
const cors = require('cors');
const app = express();

const corsOptions = {
  origin: 'https://web-01.holb20233m8xq2.tech',
};

app.use(cors(corsOptions));
app.use(express.json());

// Define API endpoints
const humidityAPI = require('./humidityAPI');
const rfidAPI = require('./rfidAPI');
const temperatureAPI = require('./temperatureAPI');

app.use('/api/humidity', humidityAPI);
app.use('/api/rfid', rfidAPI);
app.use('/api/temperature', temperatureAPI);

const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`API server is running on port ${port}`);
});
