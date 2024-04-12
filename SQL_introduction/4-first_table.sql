-- Creates a new table named 'first_table' if it does not already exist, with two columns:
-- 'id' (integer type)
-- 'name' (string type with a maximum length of 256 characters)

CREATE TABLE IF NOT EXISTS first_table (
  id INT,
  name VARCHAR(256)
);
