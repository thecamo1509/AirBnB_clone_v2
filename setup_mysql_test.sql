-- Create the new database if it does not exist already TEST

-- Create DB
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Create USER
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- Add priviliges to user
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
-- add select to ser
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';