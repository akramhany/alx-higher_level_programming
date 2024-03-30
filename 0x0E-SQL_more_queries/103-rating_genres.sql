-- a script that lists all genres in the database hbtn_0d_tvshows_rate by their rating.
SELECT t_g.name AS name, SUM(t_s_r.rate) AS rating
FROM tv_shows t_s INNER JOIN tv_genres t_g INNER JOIN tv_show_genres t_s_g INNER JOIN tv_show_ratings t_s_r
ON t_s.id = t_s_g.show_id AND t_g.id = t_s_g.genre_id AND t_s_r.show_id = t_s.id
GROUP BY name
ORDER BY rating DESC;
