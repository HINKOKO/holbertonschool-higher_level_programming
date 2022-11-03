-- Script that lists all records of the table with specified "filters"
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
