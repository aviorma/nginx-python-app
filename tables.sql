CREATE DATABASE IF NOT EXISTS app_db;
USE app_db;
CREATE TABLE IF NOT EXISTS access_log (
    id INT AUTO_INCREMENT PRIMARY KEY,
    date_time DATETIME,
    client_ip VARCHAR(45),
    internal_ip VARCHAR(45)
);
