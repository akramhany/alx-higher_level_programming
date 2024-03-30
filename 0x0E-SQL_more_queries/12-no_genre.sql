--  script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
SELECT t_s.title, t_s_g.genre_id
FROM tv_shows t_s LEFT JOIN tv_show_genres t_s_g
ON t_s.id = t_s_g.show_id
WHERE t_s_g.genre_id IS NULL
ORDER BY t_s.title, t_s_g.genre_id ASC;
