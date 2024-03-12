-- lists the `score` and number of occurances with each score with 'number'
-- displays this data sorted by number in descending order
--
-- score   number
-- 10  2
-- 8   1

SELECT score FROM second_table, COUNT(score) AS 'number' GROUP BY score ORDER BY number DESC;