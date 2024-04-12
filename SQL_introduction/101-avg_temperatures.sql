-- This SQL query is designed to calculate the average temperature for each city from the 'temperatures' table


SELECT city, AVG(value) AS "avg_temp" -- Selects the city and the average temperature, labeling it as 'avg_temp'

FROM temperatures -- The data is pulled from the 'temperatures' table

GROUP BY city -- Groups the results by city to calculate averages for each one

ORDER BY avg_temp DESC; -- Orders the results by average temperature in descending order
