-- Check if the table 'force_name' does not exist and create it

CREATE TABLE IF NOT EXISTS force_name (
  id INT,                    -- A column 'id' of type INT
  name VARCHAR(256) NOT NULL -- A column 'name' of type VARCHAR which cannot be NULL
);
