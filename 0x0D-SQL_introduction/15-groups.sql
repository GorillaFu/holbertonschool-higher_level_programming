-- lists number of records for each score value
SELECT score, count(score) AS number FROM second_table GROUP BY score DESC;
