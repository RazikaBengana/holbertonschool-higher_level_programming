-- This SQL query retrieves a list of TV show titles from a database where the genre is 'Comedy'
-- It joins three tables: tv_genres, tv_show_genres, and tv_shows to match genre names with show titles
-- The results are ordered alphabetically by the show titles

SELECT s.title -- Selects the title of the TV show
FROM tv_genres g, tv_show_genres t, tv_shows s -- From the joined tables of genres, show-genres, and shows
WHERE g.id = t.genre_id -- Matches genre IDs from genres to show-genres
    AND t.show_id = s.id -- Matches show IDs from show-genres to shows
    AND g.name = "Comedy" -- Filters to only include shows where the genre is Comedy
ORDER BY s.title ASC; -- Orders the results alphabetically by show title
