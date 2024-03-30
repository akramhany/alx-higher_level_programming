-- a script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
SELECT t_s.title AS title, t_g.name AS name
FROM tv_shows t_s LEFT JOIN (tv_show_genres t_s_g INNER JOIN tv_genres t_g)
ON t_s.id = t_s_g.show_id AND t_g.id = t_s_g.genre_id
ORDER BY title, name ASC;
