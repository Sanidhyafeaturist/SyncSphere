-- db2.sql
CREATE DATABASE IF NOT EXISTS db2;
USE db2;

CREATE TABLE IF NOT EXISTS user_data (
    user_data_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES db1.users(user_id) ON DELETE CASCADE
);
