-- ******** Exercise 1 *********
-- 1
-- SELECT name FROM language
-- 2
-- SELECT title, description, language.name FROM film JOIN language ON film.language_id = language.language_id
-- SELECT title, description, language.name FROM film RIGHT JOIN language ON film.language_id = language.language_id
-- 3
-- CREATE TABLE new_film
-- (
--    film_id      INTEGER PRIMARY KEY,
--    film_name    TEXT NOT NULL
-- )

-- SELECT * FROM new_film
-- INSERT INTO new_film (film_id, film_name) 
-- VALUES 
-- ('1', 'Beaty and the Beast'),
-- ('2', 'Angel'),
-- ('3', 'Mummy'),
-- ('4', 'Ful')

-- SELECT * FROM new_film
-- 4

-- SELECT * FROM language 

-- CREATE TABLE customer_review
-- (
-- review_id SERIAL PRIMARY KEY,
-- film_id   INTEGER REFERENCES new_film(film_id),
-- language_id INTEGER REFERENCES language (language_id),
-- title TEXT NOT NULL,
-- score INTEGER check (score BETWEEN 1 AND 10),
-- review_text TEXT,
-- last_update DATE
-- )

-- SELECT * FROM customer_review

-- INSERT INTO customer_review (film_id, language_id, title, score, review_text, last_update) 
-- VALUES 
-- (1, 1, 'Good movie', 9, 'Oh, I like it, but it was too long', '1970-10-10'),
-- (1, 1, 'Not bad', 9, 'Not recomanded, if you have no time', '1999-05-09') RETURNING *

-- SELECT film.title, customer_review.title FROM film INNER JOIN customer_review ON film.film_id = customer_review.film_id
-- SELECT new_film.film_name, customer_review.title FROM new_film INNER JOIN customer_review ON new_film.film_id = customer_review.film_id
-- DELETE FROM new_film WHERE film_name = ''

-- ******** Exercise 2 : DVD Rental ********
-- 1
-- UPDATE film SET language_id = 2 WHERE film_id BETWEEN 3 and 7
-- 2
-- SELECT * FROM customer
-- INSERT INTO customer (first_name, last_name, store_id, address_id) 
-- VALUES ('Banny','Waste', 1, 45)

-- 3
-- DROP TABLE customer_review 
-- 4
-- SELECT * FROM rental WHERE (return_date IS NULL)
-- 5 
-- SELECT film.title, payment.amount, rental.return_date FROM film 
-- INNER JOIN inventory ON film.film_id = inventory.film_id
-- INNER JOIN rental ON inventory.inventory_id = rental.inventory_id 
-- INNER JOIN payment ON rental.rental_id = payment.rental_id
-- WHERE rental.return_date IS NULL
-- ORDER BY amount DESC LIMIT 30
-- 6.1
-- SELECT film.title, film.description, actor.first_name, actor.last_name FROM film 
-- INNER JOIN film_actor ON film.film_id = film_actor.film_id
-- INNER JOIN actor ON film_actor.actor_id = actor.actor_id
-- WHERE film.description ILIKE '%sumo%' AND film.description 
-- ILIKE '%wrestler%' AND actor.first_name = 'Penelope' AND actor.last_name = 'Monroe'
-- 6.2
-- SELECT * FROM film
-- WHERE film.length <= 60 AND rating = 'R'
-- 6.3
-- SELECT film.title, customer.first_name, customer.last_name, payment.amount, rental.return_date FROM film 
-- INNER JOIN inventory ON film.film_id = inventory.film_id
-- INNER JOIN rental ON inventory.inventory_id = rental.inventory_id 
-- INNER JOIN payment ON rental.rental_id = payment.rental_id
-- INNER JOIN customer ON customer.customer_id = payment.customer_id
-- WHERE customer.first_name = 'Matthew' AND customer.last_name = 'Mahan'
-- AND payment.amount > 4
-- AND return_date BETWEEN '2005-07-28' AND '2005-08-01'
-- 6.4
-- SELECT film.title, film.description, concat(customer.first_name, ' ',  customer.last_name) AS "full_name", film.replacement_cost FROM film 
-- INNER JOIN inventory ON film.film_id = inventory.film_id
-- INNER JOIN rental ON inventory.inventory_id = rental.inventory_id 
-- INNER JOIN payment ON rental.rental_id = payment.rental_id
-- INNER JOIN customer ON customer.customer_id = payment.customer_id
-- WHERE customer.first_name = 'Matthew' AND customer.last_name = 'Mahan'
-- AND (film.description ILIKE '%boat%' OR film.title ILIKE '%boat%')
-- ORDER BY film.replacement_cost DESC LIMIT 1















