-- Script that lists all genres and the number of shows linked to each
-- First column: genre, Second column: number_of_shows
-- Don't display genres without shows
-- Sorted in descending order by the number of shows

SELECT tv_genres.name AS genre, COUNT(tv_show_genres.genre_id) AS number_of_shows
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.id
ORDER BY number_of_shows DESC;
