-- This SQL query retrieves titles from 'tv_shows' and 'genre_id' from 'tv_show_genres'
-- It joins the two tables on the 'show_id' from 'tv_show_genres' and 'id' from 'tv_shows'
-- The results are ordered by the title of the TV shows and the genre ID

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
JOIN tv_show_genres
ON tv_show_genres.show_id = tv_shows.id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
