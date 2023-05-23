-- Part 1
-- 1
-- CREATE TABLE customer (
-- customer_id SERIAL PRIMARY KEY, 
-- first_name VARCHAR(100) NOT NULL,
-- last_name VARCHAR(100) NOT NULL
-- );

-- CREATE TABLE customer_profile (
-- profile_id SERIAL PRIMARY KEY, 
-- isLoggedIn BOOL DEFAULT false,
-- last_name VARCHAR(100) NOT NULL,
-- customer_id INTEGER REFERENCES customer (customer_id)
-- );
-- 2
-- INSERT INTO customer (first_name, last_name)
-- VALUES
-- ('John', 'Doe'),
-- ('Jerome', 'Lalu'),
-- ('Lea', 'Rive')
-- 3
-- INSERT INTO customer_profile (last_name, isLoggedIn)
-- VALUES
-- ('Doe', (TRUE)),
-- ('Lalu', (FALSE))

-- INSERT INTO customer_profile (last_name)
-- VALUES('Rive')

-- SELECT * FROM customer_profile

-- SELECT * FROM customer

