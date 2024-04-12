-- Selects the title from the 'tv_shows' table and the 'genre_id' from the 'tv_show_genres' table
SELECT tv_shows.title, tv_show_genres.genre_id

FROM tv_shows  -- Specifies the 'tv_shows' table as the main source of data

LEFT JOIN tv_show_genres  -- Performs a left join with the 'tv_show_genres' table

ON tv_show_genres.show_id = tv_shows.id  -- Join condition based on the show ID

ORDER BY tv_shows.title, tv_show_genres.genre_id;  -- Orders the result by show title and genre ID
