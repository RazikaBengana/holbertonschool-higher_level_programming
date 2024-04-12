-- Select the name of each TV genre and the sum of the ratings for shows in that genre
SELECT tv_genres.name, SUM(tv_show_ratings.rate) AS "rating" FROM tv_shows

 -- Join the tv_show_ratings table to associate each show with its ratings
 JOIN tv_show_ratings ON tv_show_ratings.show_id = tv_shows.id

 -- Join the tv_show_genres table to link shows with their genres
 JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id

 -- Join the tv_genres table to access the names of the genres
 JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id

-- Group the results by genre name to calculate the total ratings per genre
GROUP BY tv_genres.name

-- Order the results by the sum of ratings in descending order
ORDER BY SUM(tv_show_ratings.rate) DESC;
