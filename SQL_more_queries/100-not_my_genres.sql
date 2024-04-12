-- This query retrieves a list of unique genre names from TV shows,
-- excluding the genres associated with the TV show titled "Dexter"

SELECT DISTINCT tv_genres.name  -- Selects unique genre names

FROM tv_shows                  -- From the table of TV shows

LEFT JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id  -- Joins with genres through a junction table
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id    -- Joins genre table to get genre names

WHERE tv_genres.name NOT IN (  -- Filter out genres of a specific show, "Dexter"

    SELECT g.name             -- Subquery to select genre names associated with "Dexter"

    FROM tv_genres g, tv_show_genres t, tv_shows s

    WHERE g.id = t.genre_id   -- Join condition for genres

        AND t.show_id = s.id  -- Join condition for show identifiers
        AND s.title = "Dexter"  -- Condition to filter the show "Dexter"
)
ORDER BY tv_genres.name;  -- Results are ordered alphabetically by genre name
