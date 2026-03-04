-- Script that lists all cities of California found in hbtn_0d_usa
-- The states table contains only one record where name = California
-- Results are sorted in ascending order by cities.id
-- JOIN keyword is not allowed

SELECT id, name 
FROM cities
WHERE state_id = (
    SELECT id FROM states WHERE name = 'California'
)
ORDER BY id ASC;
