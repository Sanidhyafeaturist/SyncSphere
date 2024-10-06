-- db1.sql
CREATE DATABASE IF NOT EXISTS db1;
USE db1;

CREATE TABLE IF NOT EXISTS users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


DELIMITER //

CREATE TRIGGER after_user_insert
AFTER INSERT ON db1.users
FOR EACH ROW
BEGIN
    INSERT INTO db2.additional_data (username, email)
    VALUES (NEW.username, NEW.email);
END; //

DELIMITER ;
