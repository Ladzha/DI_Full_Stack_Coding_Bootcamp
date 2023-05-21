-- STEP 1
-- CREATE TABLE items (
-- 	item_id SERIAL PRIMARY KEY,
-- 	item_name VARCHAR(100) NOT NULL,
-- 	price SMALLINT NOT NULL DEFAULT 0
-- )

-- SELECT * from items

-- INSERT INTO items(item_name, price)
-- VALUES ('Small Desk', 100),
-- ('Large desk', 300),
-- ('Fan', 80)

--SELECT * from items

-- STEP 2
-- CREATE TABLE customers (
-- 	customers_id SERIAL PRIMARY KEY,
-- 	first_name VARCHAR(100) NOT NULL,
-- 	last_name VARCHAR(100) NOT NULL
-- )

--SELECT * from customers

-- INSERT INTO customers(first_name, last_name)
-- VALUES ('Greg', 'Jones'),
-- ('Sandra', 'Jones'),
-- ('Scott', 'Scott'),
-- ('Trevor ', 'Green'),
-- ('Melanie ', 'Johnson')

--SELECT * from customers

-- STEP 3
-- STEP 3.1
--SELECT * from items
-- STEP 3.2
-- SELECT * FROM items WHERE price > 80
-- STEP 3.3
-- SELECT * FROM items WHERE price < 300
-- STEP 3.4
-- SELECT * FROM customers WHERE last_name ='Smith'
-- STEP 3.5
-- SELECT * FROM customers WHERE last_name ='Jones'
-- STEP 3.6
-- SELECT * FROM customers WHERE first_name !='Scott'