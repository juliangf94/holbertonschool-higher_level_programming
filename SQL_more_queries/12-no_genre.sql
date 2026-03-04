-- Script that lists all shows in hbtn_0d_tvshows without a genre linked
-- Displays: tv_shows.title - tv_show_genres.genre_id
-- Results are sorted by tv_shows.title and tv_show_genres.genre_id ASC

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC
