-- This query retrieves the ID and name of cities, along with the name of their corresponding states
SELECT cities.id, cities.name, states.name
FROM states

-- Joins the 'states' table with the 'cities' table where the 'id' of states matches the 'state_id' of cities
JOIN cities ON states.id = cities.state_id

-- Orders the results by the 'id' of cities in ascending order
ORDER BY cities.id;
