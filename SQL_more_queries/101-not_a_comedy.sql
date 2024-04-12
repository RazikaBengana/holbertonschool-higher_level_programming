-- This SQL query selects the titles of TV shows from the 'tv_shows' table that are not listed as comedies
-- It begins by selecting the title from the 'tv_shows' table

SELECT title FROM tv_shows

WHERE title NOT IN (
    -- This subquery identifies all titles of TV shows associated with the 'Comedy' genre
    -- It joins three tables: 'tv_genres', 'tv_show_genres', and 'tv_shows'
    -- 'tv_genres' contains genre data. 'tv_show_genres' links shows to their genres, and 'tv_shows' contains the shows
    SELECT s.title FROM tv_genres g, tv_show_genres t, tv_shows s

    WHERE g.id = t.genre_id      -- Matches genre IDs in 'tv_genres' to 'tv_show_genres'
        AND t.show_id = s.id     -- Matches show IDs in 'tv_shows' to 'tv_show_genres'
        AND g.name = "Comedy"    -- Filters for shows categorized as comedies
)
ORDER BY title ASC;  -- Orders the results alphabetically by title
