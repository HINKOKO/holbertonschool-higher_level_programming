-- Script that displays top 3 of cities in temperatures
-- during July and August ordered by descending temperatures
SELECT city, AVG(value) 'avg_temp'
FROM temperatures
WHERE month IN (7, 8)
GROUP BY city ORDER BY avg_temp DESC
LIMIT 3;
