-- https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql
-- run this first to import a SQL dump -->
--      echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
--      curl [link] -s | mysql -uroot -p hbtn_0d_tvshows
--
-- script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
-- tv_shows table contains only one record where title = Dexter (but the id can be different)
-- each record should display: tv_genres.name
-- results must be sorted in ascending order by the genre name
-- can use only one SELECT statement
-- the database name will be passed as an argument of the mysql command
USE hbtn_0d_tvshows;
SELECT tv_genres.name WHERE tv_shows.title = Dexter
FROM tv_show 
ORDER BY tv_genres.name ASC;