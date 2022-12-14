-- Script that lists all genres from tv_shows database displays
-- the number of shows linked to each.
SELECT `tv_genres`.`name` AS 'genre', COUNT(*) AS `number_of_shows`
FROM `tv_genres`
INNER JOIN `tv_show_genres`
ON `tv_show_genres`.`genre_id` =`tv_genres`.`id`
GROUP BY `tv_genres`.`name`
ORDER BY `number_of_shows` DESC;

