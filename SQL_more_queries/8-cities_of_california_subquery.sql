-- Script that list all the cities of California in database hbtn_0d_usa using subqueries technic
SELECT id, name
FROM cities
WHERE state_id IN (
	SELECT id
	FROM states
	WHERE name='California'
);
