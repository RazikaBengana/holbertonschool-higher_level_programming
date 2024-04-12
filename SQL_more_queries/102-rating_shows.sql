-- This SQL query retrieves the title of TV shows and their total ratings from the database
SELECT tv_shows.title, SUM(tv_show_ratings.rate) AS "rating" FROM tv_shows

-- The LEFT JOIN includes all records from the 'tv_shows' table and the matched records from the 'tv_show_ratings' table
LEFT JOIN tv_show_ratings ON tv_show_ratings.show_id = tv_shows.id

-- Groups the results by the title of the TV shows
GROUP BY tv_shows.title

-- Orders the result by the sum of ratings in descending order, so the highest rated shows appear first
ORDER BY SUM(tv_show_ratings.rate) DESC;
