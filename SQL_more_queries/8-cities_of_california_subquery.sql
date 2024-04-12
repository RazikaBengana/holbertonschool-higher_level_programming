-- This SQL query retrieves the id and name of cities from the 'cities' table
SELECT id, name
FROM cities

WHERE state_id = (
    -- Subquery to get the id of the state named 'California' from the 'states' table
    SELECT id
    FROM states
    WHERE name = "California"
)

-- The results are ordered by the city id in ascending order
ORDER BY id;
