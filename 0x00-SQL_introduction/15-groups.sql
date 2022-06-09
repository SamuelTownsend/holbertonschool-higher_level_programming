-- script that lists the number of records with same score in table named second_table
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score ORDER BY score DESC;