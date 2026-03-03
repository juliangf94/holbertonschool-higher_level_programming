-- Script that lists the number of records with the same score in second_table
-- Results display the score and the count labeled as 'number'
-- Sorted by the count of records in descending order

SELECT score, COUNT(*) AS number 
FROM second_table
GROUP BY score
ORDER BY number DESC;
