-- This SQL statement checks if a table named 'id_not_null' exists

-- If it does not exist, it creates the table with two columns:
    -- 'id', which is an integer with a default value of 1, and
    -- 'name', which is a variable character string up to 256 characters long

CREATE TABLE IF NOT EXISTS id_not_null (id INT DEFAULT 1, name VARCHAR(256));
