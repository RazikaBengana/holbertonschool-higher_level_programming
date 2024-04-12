-- Selects the 'score' and 'name' fields from the 'second_table'
SELECT score, name
FROM second_table

-- Filters the results to include only rows where the 'name' field is not NULL
WHERE name IS NOT NULL

-- Orders the results by 'score' in descending order
ORDER BY score DESC;
