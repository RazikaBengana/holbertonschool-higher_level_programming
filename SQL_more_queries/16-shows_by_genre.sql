-- This SQL query selects the title of TV shows and their associated genre names
-- It retrieves data from the 'tv_shows' table and joins it with 'tv_show_genres' and 'tv_genres' tables

SELECT tv_shows.title, tv_genres.name
FROM tv_shows

-- Left join on 'tv_show_genres' table to match each show with its genres by show ID.
LEFT JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id

-- Left join on 'tv_genres' table to get the genre names by genre ID
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id

-- The results are ordered by the title of the TV shows and the names of their genres
ORDER BY tv_shows.title, tv_genres.name;
