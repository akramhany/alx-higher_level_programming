-- a script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
SELECT t_g.name AS name
FROM tv_genres t_g
WHERE name NOT IN (
	SELECT t_v.name
	FROM tv_genres t_v INNER JOIN tv_shows t_s INNER JOIN tv_show_genres t_s_g
	ON t_v.id = t_s_g.genre_id AND t_s.id = t_s_g.show_id AND t_s.title = 'Dexter'
)
ORDER BY name ASC;
