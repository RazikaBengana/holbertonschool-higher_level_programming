-- This SQL statement creates a table if it does not already exist

CREATE TABLE IF NOT EXISTS unique_id (
    -- 'id' column as an integer, defaulting to 1, marked as unique
    id INT DEFAULT 1, UNIQUE (ID),
    -- 'name' column to store strings up to 256 characters
    name VARCHAR(256)
);
