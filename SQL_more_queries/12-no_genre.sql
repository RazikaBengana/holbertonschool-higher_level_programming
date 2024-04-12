-- This SQL query retrieves titles of TV shows and their corresponding genre IDs
-- from the 'tv_shows' table and the 'tv_show_genres' table;
-- The query performs a LEFT JOIN on 'tv_show_genres' based on the show's ID;
-- It specifically looks for TV shows that have no associated genre (genre_id IS NULL),
-- which suggests they are unclassified or belong to no specific genre;
-- The results are ordered by the title of the TV shows and their genre IDs

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_show_genres.show_id = tv_shows.id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title, tv_show_genres.genre_id;
