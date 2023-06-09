-- Part 1
-- 1
-- CREATE TABLE customer (
-- customer_id SERIAL PRIMARY KEY, 
-- first_name VARCHAR(100) NOT NULL,
-- last_name VARCHAR(100) NOT NULL
-- );

-- CREATE TABLE customer_profile (
-- profile_id SERIAL PRIMARY KEY, 
-- isLoggedIn BOOLEAN DEFAULT false,
-- customer_id INTEGER NOT NULL,
-- FOREIGN KEY (customer_id)  UNIQUE REFERENCES customer (customer_id)
-- );
-- 2
-- INSERT INTO customer (first_name, last_name)
-- VALUES
-- ('John', 'Doe'),
-- ('Jerome', 'Lalu'),
-- ('Lea', 'Rive')
-- 3
-- INSERT INTO customer_profile (isLoggedIn, customer_id)
-- VALUES (TRUE, (SELECT customer_id FROM customer WHERE first_name = 'John' AND last_name = 'Doe')),
-- (TRUE, (SELECT customer_id FROM customer WHERE first_name = 'Jerome' AND last_name = 'Lalu'))
-- RETURNING *

-- SELECT * FROM customer_profile

-- SELECT * FROM customer
-- 4.1
-- SELECT first_name FROM customer
-- JOIN customer_profile ON customer.customer_id=customer_profile.customer_id
-- WHERE isLoggedIn
-- 4.2
-- SELECT first_name, isLoggedIn FROM customer
-- LEFT JOIN customer_profile 
-- ON customer.customer_id=customer_profile.customer_id

-- SELECT COUNT(first_name) FROM customer
-- LEFT JOIN customer_profile 
-- ON customer.customer_id=customer_profile.customer_id
-- WHERE isLoggedIn IS NULL

-- Part 2
-- 1
-- CREATE TABLE book (
-- book_id SERIAL PRIMARY KEY, 
-- book_title VARCHAR(100) NOT NULL,
-- author VARCHAR(100) NOT NULL
-- );
-- 2
-- INSERT INTO book (book_title, author)
-- VALUES
-- ('Alice In Wonderland', 'Lewis Carroll'),
-- ('Harry Potter', 'J.K Rowling'),
-- ('To kill a mockingbird', 'Harper Lee')

-- SELECT * FROM book

-- 3
-- CREATE TABLE student (
-- student_id SERIAL PRIMARY KEY, 
-- student_name VARCHAR(100) NOT NULL UNIQUE,
-- student_age INTEGER check (student_age <=15)
-- );
-- 4
-- INSERT INTO student (student_name, student_age)
-- VALUES
-- ('John', 12),
-- ('Lera', 11),
-- ('Patrick', 10),
-- ('Bob', 14)

-- SELECT * FROM student
-- 5
-- CREATE TABLE library (
-- book_fk_id INTEGER,
-- student_fk_id INTEGER,
-- borrowed_date DATE DEFAULT NOW() NOT NULL, 
-- FOREIGN KEY (book_fk_id) REFERENCES book (book_id) ON DELETE CASCADE ON UPDATE CASCADE,
-- FOREIGN KEY (student_fk_id) REFERENCES student (student_id) ON DELETE CASCADE ON UPDATE CASCADE,
-- PRIMARY KEY(book_fk_id, student_fk_id)
-- );
-- 6
-- INSERT INTO library (book_fk_id, student_fk_id, borrowed_date)
-- VALUES
-- ((SELECT book_id FROM book WHERE book_title = 'Alice In Wonderland'),
-- (SELECT student_id FROM student WHERE student_name = 'John'), '15/02/2022'),

-- ((SELECT book_id FROM book WHERE book_title = 'To kill a mockingbird'),
-- (SELECT student_id FROM student WHERE student_name = 'Bob'), '03/03/2021'),

-- ((SELECT book_id FROM book WHERE book_title = 'Alice In Wonderland'),
-- (SELECT student_id FROM student WHERE student_name = 'Lera'), '23/05/2021'),

-- ((SELECT book_id FROM book WHERE book_title = 'Harry Potter'),
-- (SELECT student_id FROM student WHERE student_name = 'Bob'), '12/08/2021')
-- 7.1
-- SELECT student_name, book_title, borrowed_date FROM library
-- INNER JOIN student ON student.student_id = library.student_fk_id
-- INNER JOIN book ON book.book_id= library.book_fk_id
-- 7.2
-- SELECT student_name, book_title FROM student 
-- INNER JOIN library ON student.student_id = library.student_fk_id
-- INNER JOIN book ON book.book_id= library.book_fk_id
-- 7.3
-- SELECT ROUND(AVG(student_age), 1) FROM student 
-- INNER JOIN library ON student.student_id = library.student_fk_id
-- INNER JOIN book ON book.book_id= library.book_fk_id
-- WHERE book_title = 'Alice In Wonderland'
-- 7.4
-- DELETE FROM student WHERE student_name = 'Lera'
-- SELECT * FROM library