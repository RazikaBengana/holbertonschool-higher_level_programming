-- This SQL query retrieves the genre names associated with the TV show titled "Dexter";
-- It joins three tables: tv_genres, tv_show_genres, and tv_shows;
-- The WHERE clause filters for records where the genre ID and show ID match across the tables,
-- specifically where the tv_show's title is "Dexter";
-- Results are ordered alphabetically by genre name

SELECT g.name
FROM tv_genres g, tv_show_genres t, tv_shows s
WHERE g.id = t.genre_id
    AND t.show_id = s.id
    AND s.title = "Dexter"
ORDER BY g.name ASC;
