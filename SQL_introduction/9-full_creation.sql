-- This SQL script creates a table and inserts data into it


-- Check if the table 'second_table' exists and create it if it doesn't.
-- The table includes three columns: id, name, and score

CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);

-- Insert a row into 'second_table' with id as 1, name as 'John', and score as 10
INSERT INTO second_table(id, name, score) VALUES (1, 'John', 10);

-- Insert a row into 'second_table' with id as 2, name as 'Alex', and score as 3
INSERT INTO second_table(id, name, score) VALUES (2, 'Alex', 3);

-- Insert a row into 'second_table' with id as 3, name as 'Bob', and score as 14
INSERT INTO second_table(id, name, score) VALUES (3, 'Bob', 14);

-- Insert a row into 'second_table' with id as 4, name as 'George', and score as 8
INSERT INTO second_table(id, name, score) VALUES (4, 'George', 8);
