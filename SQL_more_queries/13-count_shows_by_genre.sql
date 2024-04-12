-- Selects the genre names and counts the number of TV shows for each genre

SELECT tv_genres.name AS "genre",      -- Alias 'genre' is used for the genre name
       count(*) AS "number_of_shows"   -- Counts the number of shows per genre
    FROM tv_show_genres                -- From the table that links shows and genres
LEFT JOIN tv_genres                    -- Left join to include all genres
          ON tv_genres.id = genre_id   -- Join condition on the genre ID
GROUP BY genre_id                      -- Group the results by genre ID
ORDER BY count(*) DESC;                -- Order the results by count, descending
