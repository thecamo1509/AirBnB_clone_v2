-- Create the new database if it does not exist already

-- Create DB
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Create USER
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- Add priviliges to user
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- add select to ser
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';