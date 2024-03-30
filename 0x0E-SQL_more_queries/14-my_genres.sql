-- a script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
SELECT t_g.name AS name
FROM tv_shows t_s INNER JOIN tv_genres t_g INNER JOIN tv_show_genres t_s_g
ON t_s.id = t_s_g.show_id AND t_g.id = t_s_g.genre_id AND t_s.title = 'Dexter'
ORDER BY name ASC;
