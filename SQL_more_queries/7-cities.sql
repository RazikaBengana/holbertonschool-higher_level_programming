-- Check if the database hbtn_0d_usa exists, create it if it doesn't
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Check if the table 'cities' exists in the database 'hbtn_0d_usa', create it if it doesn't
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
    id INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY, -- Define a primary key with auto-increment
    state_id INT NOT NULL,                             -- Define a foreign key that references a state
    FOREIGN KEY(state_id) REFERENCES hbtn_0d_usa.states(id),
    name VARCHAR(256) NOT NULL                         -- Define a 'name' field that must be non-null
);
