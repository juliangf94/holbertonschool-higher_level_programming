-- Script that lists all cities in hbtn_0d_usa
-- Display: cities.id - cities.name - states.name
-- Sorted by cities.id ASC
-- Only one SELECT statement allowed

SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
