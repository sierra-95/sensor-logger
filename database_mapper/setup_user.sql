-- prepares a MySQL server for the project

CREATE USER IF NOT EXISTS 'ubuntu'@'localhost' IDENTIFIED BY 'Michael@92!7'; --or favourable password
GRANT ALL PRIVILEGES ON sensor_logger.* TO 'ubuntu'@'localhost';
FLUSH PRIVILEGES;