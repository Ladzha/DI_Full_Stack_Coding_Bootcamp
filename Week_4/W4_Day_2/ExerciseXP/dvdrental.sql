-- 1
-- SELECT * FROM customer
-- 2
-- SELECT concat(first_name, ' ',  last_name) AS "full_name" FROM customer 
-- 3
-- SELECT DISTINCT create_date FROM customer
-- 4
-- SELECT * FROM customer ORDER BY first_name DESC
-- 5
-- SELECT film_id, title, description, release_year, rental_rate 
-- FROM film ORDER BY rental_rate ASC
-- 6
-- SELECT address, phone FROM address WHERE district = 'Texas'
-- 7
-- SELECT * FROM film WHERE film_id =15 OR film_id =150

-- 8
-- SELECT film_id, title, description, length, rental_rate 
-- FROM film WHERE title='Mumia'

-- 9
-- SELECT film_id, title, description, length, rental_rate 
-- FROM film WHERE title ILIKE  'mu%'
-- 10
-- SELECT film_id, title, replacement_cost 
-- FROM film ORDER BY replacement_cost ASC LIMIT 10
-- 11
-- SELECT film_id, title, replacement_cost 
-- FROM film ORDER BY replacement_cost ASC LIMIT 10 OFFSET 10
-- 12
-- SELECT first_name, last_name, amount, payment_date FROM customer 
-- INNER JOIN payment ON customer.customer_id = payment.customer_id 
-- ORDER BY customer.customer_id 

-- 13
-- SELECT film.title FROM film WHERE film.film_id NOT IN(SELECT inventory.film_id FROM inventory)

-- 14
-- SELECT city, country FROM city INNER JOIN country ON city_id = city_id 

-- 15
-- SELECT  customer.customer_id, concat(first_name, ' ',  last_name) AS "full_name", amount, payment_date, payment.staff_id
-- FROM customer INNER JOIN payment ON customer.customer_id = payment.customer_id
-- ORDER BY payment.staff_id ASC

