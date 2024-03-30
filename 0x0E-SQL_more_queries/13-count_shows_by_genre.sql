--  script that lists all shows contained in hbtn_0d_tvshows.
SELECT t_g.name AS genre, COUNT(*) AS number_of_shows
FROM tv_genres t_g INNER JOIN tv_show_genres t_s_g
ON t_g.id = t_s_g.genre_id
GROUP BY t_g.name
ORDER BY number_of_shows DESC;
