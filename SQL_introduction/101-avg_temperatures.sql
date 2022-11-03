-- Script that computes average temperatures by city
SELECT AVG(value) 'avg_temp'
FROM temperatures
GROUP BY city;
