-- CREATE TABLE actor (
-- 	actor_id SERIAL PRIMARY KEY,
-- 	first_name VARCHAR(100),
-- 	last_name VARCHAR(100),
-- 	date_birth DATE NOT NULL,
-- 	number_of_oscar SMALLINT NOT NULL DEFAULT 0
-- )

--SELECT * FROM actor

--SELECT first_name, last_name FROM actor
-- INSERT INTO actor(first_name, last_name, date_birth,number_of_oscar)
-- VALUES ('Jon', 'Jons', '1974-11-04', 2)
--SELECT * FROM actor

-- INSERT INTO actor (first_name, last_name, date_birth, number_of_oscar)
-- VALUES ('Sally', 'Pit', '1944-08-12', 3),
-- ('Sara', 'Gorg', '1932-10-16', 1)
-- SELECT first_name, last_name FROM actor

-- INSERT INTO actor (first_name, last_name, date_birth, number_of_oscar)
-- VALUES ('Mary', 'Donning', '1968-12-05', 3)

-- INSERT INTO actor (first_name, last_name, date_birth, number_of_oscar)
-- VALUES ('Jack', 'Samers', '1928-02-23', 0),
-- ('Gill', 'Popert', '1981-08-29', 0),
-- ('Herbert', 'Kurt', '1998-09-27', 0),

-- SELECT * FROM actor

-- INSERT INTO actor (first_name, last_name, date_birth, number_of_oscar)
-- VALUES ('Jack', 'Samers', '1928-02-23', DEFAULT)



-- SELECT first_name, last_name FROM actor WHERE first_name = 'Jon'OR last_name ='Samers'
-- SELECT first_name, last_name FROM actor WHERE number_of_oscar >= 2
-- SELECT * FROM actor ORDER BY last_name ASC, first_name DESC 

-- SELECT * FROM actor ORDER BY date_birth ASC LIMIT 1

-- SELECT * FROM actor WHERE EXTRACT(YEAR from date_birth) >=1950

-- SELECT * FROM actor WHERE first_name LIKE '%r%'
-- SELECT * FROM actor WHERE first_name ILIKE '%J%'

-- UPDATE actor
-- SET last_name = 'Clooney'
-- WHERE actor_id = 1
-- RETURNING *

-- UPDATE actor
-- SET number_of_oscar = 4
-- RETURNING *



-- UPDATE actor
-- SET number_of_oscar = 3
-- WHERE last_name = 'Pit'
-- RETURNING *

-- SELECT * from actor ORDER BY actor_id

-- DELETE FROM actor
-- WHERE actor_id = 5

--SELECT * from actor ORDER BY actor_id

--ALTER TABLE actor ADD COLUMN salary INTEGER;
--ALTER TABLE actor ADD COLUMN nationality VARCHAR(200);
--SELECT * FROM actor

-- UPDATE actor
-- SET salary = 1000000 * number_of_oscar
-- RETURNING
--SELECT * FROM actor

-- UPDATE actor
-- SET nationality = 'American'
-- WHERE actor_id IN (1,2,3)
-- RETURNING *

-- UPDATE actor
-- SET nationality = 'French'
-- WHERE actor_id NOT IN (1,2,3)
-- RETURNING *

-- UPDATE actor
-- SET nationality = 'Israel'
-- WHERE actor_id BETWEEN 4 AND 5
-- RETURNING *

--SELECT * from actor



-- SELECT * FROM actor WHERE actor_id <=4

--SELECT * FROM actor WHERE actor_id <=4 ORDER BY last_name DESC
--SELECT * FROM actor WHERE last_name LIKE '%e%'
-- UPDATE actor
-- SET number_of_oscar= 5
-- WHERE actor_id = 6
-- RETURNING *
-- SELECT * FROM actor WHERE number_of_oscar >=4

-- ******************EXERCISE******************

-- SELECT * FROM actor
-- SELECT COUNT(first_name) FROM actor;

-- INSERT INTO actor (first_name, last_name, date_birth, number_of_oscar)
-- VALUES ('Brad', 'Rupert', '1977-01-04', DEFAULT)


-- SELECT * FROM actor

-- SELECT COUNT(*) FROM actor

-- SELECT MAX(salary) FROM actor

-- SELECT first_name FROM actor WHERE salary = (MAX(salary) FROM actor)????


-- SELECT * FROM actor

-- SELECT LOWER(nationality) AS nationality, COUNT(*) AS number_of_people --same coloumn
-- FROM actor
-- GROUP BY LOWER(nationality)



-- SELECT LOWER(nationality) AS nationality, COUNT(*) AS number_of_people
-- FROM actor
-- GROUP BY LOWER(nationality)
-- HAVING LOWER(nationality) = 'israel'

-- SELECT salary, COUNT (*)
-- FROM actor
-- GROUP BY salary

-- SELECT COUNT (*) FROM actor
-- SELECT COUNT (nationality) FROM actor
-- SELECT * FROM actor


-- CREATE TABLE movies(
--     movie_id SERIAL PRIMARY KEY, 
--     movie_title VARCHAR (50) NOT NULL, 
--     movie_story TEXT, 
--     actor_playing_id INTEGER REFERENCES actor (actor_id)
-- );



SELECT * FROM movies