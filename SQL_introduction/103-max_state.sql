-- This SQL query selects the maximum temperature recorded for each state from the 'temperatures' table
-- It groups the results by state and orders them in ascending order by state


SELECT state, MAX(value) AS "max_temp"  -- 'state' and maximum value aliased as 'max_temp'

FROM temperatures                       -- From the 'temperatures' table

GROUP BY state                          -- Grouping the results by 'state'

ORDER BY state ASC;                     -- Ordering the results by 'state' in ascending order
