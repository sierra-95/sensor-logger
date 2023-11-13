-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS sensor_logger;
USE sensor_logger;

CREATE TABLE IF NOT EXISTS rfid_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    date DATE,
    time TIME,
    parameter1 VARCHAR(255),
    UID VARCHAR(255), 
    parameter2 VARCHAR(255),
    message VARCHAR(255) 
);
CREATE TABLE IF NOT EXISTS temperature_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    date DATE,
    time TIME,
    temperature_celsius FLOAT,
    temperature_fahrenheit FLOAT,
    heat_index_celsius FLOAT,
    heat_index_fahrenheit FLOAT
);
CREATE TABLE IF NOT EXISTS humidity_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    date DATE,
    time TIME,
    parameter VARCHAR(255),
    value FLOAT
);


