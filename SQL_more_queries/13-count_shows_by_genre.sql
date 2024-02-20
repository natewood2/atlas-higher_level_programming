-- Count Shows By Genre
SELECT DISTINCT g.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows FROM g
INNER JOIN tv_show_genres ON g.id = tv_show_genres.genre_id 
GROUP BY genre 
ORDER BY number_of_shows DESC;