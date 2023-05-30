-- -- ONE TO ONE -- least frequent

-- -- a customer can have one profile
-- -- and a profile belongs to only one customer 

-- -- ONE TO MANY -- more frequent

-- -- a person can have many passports
-- -- and a passport belongs to only one person 

-- -- MANY TO MANY -- more frequent

-- -- a student can borrow many books
-- -- and a book can be borrowed by many students


-- CREATE TABLE student (
--     student_id	SERIAL PRIMARY KEY,
--     name VARCHAR(100) NOT NULL,
--     age SMALLINT CHECK(age BETWEEN 10 and 15)
-- );

-- CREATE TABLE book (
--     book_id	SERIAL PRIMARY KEY,
--     title VARCHAR(200) NOT NULL,
--     author VARCHAR(100) NOT NULL
-- );

-- CREATE TABLE library (
--     library_id SERIAL PRIMARY KEY,
--     student_id INTEGER REFERENCES student (student_id) ON DELETE CASCADE ON UPDATE CASCADE,
--     book_id INTEGER REFERENCES book (book_id) ON DELETE CASCADE ON UPDATE CASCADE,
--     date_borrowed DATE DEFAULT NOW() NOT NULL
-- );

-- -- INSERT INTO student (name, age)
-- -- VALUES ('John', 12),('Lera', 11), ('Emma', 9), ('Patrick', 10), ('Bob', 10)
-- -- RETURNING *

-- INSERT INTO student (name, age)
-- VALUES ('John', 12),('Lera', 11), ('Patrick', 10), ('Bob', 10)
-- RETURNING *;

-- -- INSERT INTO student (name, age)
-- -- VALUES ('Jane', 12)
-- -- RETURNING *;

-- SELECT * FROM student;


-- INSERT INTO book (title, author)
-- VALUES ('Alice In Wonderland', 'Lewis Carroll'),
-- ('Harry Potter', 'J.K Rowling'), 
-- ('To kill a mockingbird', ' Harper Lee')
-- RETURNING *;

-- INSERT INTO library (student_id, book_id, date_borrowed)
-- VALUES 
-- ((SELECT student_id FROM student WHERE name = 'John'), 
--  (SELECT book_id FROM book WHERE title ILIKE '%Wonderland%'),
--     '2022-02-15'),
-- ((SELECT student_id FROM student WHERE name = 'Bob'), 
--  (SELECT book_id FROM book WHERE title ILIKE '%mokingbird%'),
--     '2023-03-03'),
--  ((SELECT student_id FROM student WHERE name = 'Lera'), 
--  (SELECT book_id FROM book WHERE title ILIKE '%Wonderland%'),
--     '2021-03-15'),
--  ((SELECT student_id FROM student WHERE name = 'Bob'), 
--  (SELECT book_id FROM book WHERE title ILIKE '%Harry%'),
--     DEFAULT)

