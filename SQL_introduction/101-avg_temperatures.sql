-- Script that computes average temperatures by city
SELECT city, AVG(value) 'avg_temp'
FROM temperatures
GROUP BY city ORDER BY avg_temp DESC;
