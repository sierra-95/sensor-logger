<?php
// Database connection parameters
$servername = 'localhost';
$username = 'ubuntu';
$password = 'Michael@92!7';
$database = 'sensor_logger';

// Create a connection
$conn = new mysqli($servername, $username, $password, $database);

// Check the connection
if ($conn->connect_error) {
    die('Connection failed: ' . $conn->connect_error);
}

// Function to fetch and display data
function fetchDataAndDisplay($conn, $tableName, $displayFunction) {
    $sql = "SELECT * FROM $tableName";
    $result = $conn->query($sql);

    if ($result->num_rows > 0) {
        while ($row = $result->fetch_assoc()) {
            $displayFunction($row);
        }
    } else {
        echo 'No data found in ' . $tableName;
    }
}

// Display functions for each data type
function displayRFID($row) {
    echo 'Date: ' . $row['date'] . ', Time: ' . $row['time'] . ', UID: ' . $row['UID'] . ', Message: ' . $row['message'] . '<br>';
}

function displayTemperature($row) {
    echo 'Date: ' . $row['date'] . ', Time: ' . $row['time'] . ', Temperature (°C): ' . $row['temperature_celsius'] . ', Temperature (°F): ' . $row['temperature_fahrenheit'] . ', Heat Index (°C): ' . $row['heat_index_celsius'] . ', Heat Index (°F): ' . $row['heat_index_fahrenheit'] . '<br>';
}

function displayHumidity($row) {
    echo 'Date: ' . $row['date'] . ', Time: ' . $row['time'] . ', Parameter: ' . $row['parameter'] . ', Value: ' . $row['value'] . '<br>';
}

// Display all data
fetchDataAndDisplay($conn, 'rfid_data', 'displayRFID');
fetchDataAndDisplay($conn, 'temperature_data', 'displayTemperature');
fetchDataAndDisplay($conn, 'humidity_data', 'displayHumidity');

$conn->close();
?>
