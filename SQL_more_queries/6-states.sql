-- Check if the database 'hbtn_0d_usa' does not exist and create it if necessary
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Check if the table 'states' does not exist in the database 'hbtn_0d_usa' and create it if necessary
-- The table includes two fields:
    -- 'id' which is an integer and serves as a unique auto-increment primary key,
    -- 'name' which is a variable character string up to 256 characters long, which cannot be null

CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
  id INT UNIQUE AUTO_INCREMENT PRIMARY KEY NOT NULL,
  name VARCHAR(256) NOT NULL
);
