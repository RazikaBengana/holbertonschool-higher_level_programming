-- Selects the 'score' and the count of 'score' from 'second_table'
SELECT score, COUNT('score') as number
FROM second_table

-- Groups the results by 'score'
GROUP BY score

-- Orders the results by 'score' in descending order
ORDER BY score DESC;
