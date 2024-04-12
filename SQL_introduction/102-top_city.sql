-- This SQL query selects the top 3 cities with the highest average temperatures for the summer months (July and August)
-- The query aggregates average temperature (avg_temp) from the 'temperatures' table where the month is either 7 (July) or 8 (August)
-- It groups the results by city, orders them in descending order of average temperature, and limits the output to the top 3 cities


-- Selects city names and the average temperature as "avg_temp"
SELECT city, AVG(value) AS "avg_temp"

-- From the "temperatures" table
FROM temperatures

-- Filters records to include only those for the months of July (7) and August (8)
WHERE month = 7 OR month = 8

-- Groups the results by city
GROUP BY city

-- Orders the results by the average temperature in descending order
ORDER BY avg_temp DESC

-- Limits the output to the top 3 cities with the highest average temperature
LIMIT 3;
