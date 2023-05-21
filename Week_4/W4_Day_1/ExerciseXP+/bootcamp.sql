-- CREATE TABLE students (
-- 	students_id SERIAL PRIMARY KEY,
-- 	first_name VARCHAR(100) NOT NULL,
-- 	last_name VARCHAR(100) NOT NULL,
-- 	birth_date DATE NOT NULL
-- )

-- SELECT * FROM students

-- INSERT INTO students (first_name, last_name,birth_date)
-- VALUES 
-- ('Marc', 'Benichou', '02/11/1998'),
-- ('Yoan', 'Cohen', '03/12/2010'),
-- ('Lea', 'Benichou', '27/07/1987'),
-- ('Amelia', 'Dux', '07/04/1996'),
-- ('David', 'Grez', '14/06/2003'),
-- ('Omer', 'Simpson', '03/10/1980')

-- SELECT * FROM students

-- INSERT INTO students (first_name, last_name,birth_date)
-- VALUES 
-- ('Alla', 'Nudelman', '18/10/1986')


-- Select 1
-- SELECT * FROM students
-- Select 2
-- SELECT first_name, last_name FROM students
-- Select 3.1
-- SELECT first_name, last_name FROM students WHERE students_id =2
-- Select 3.2
-- SELECT first_name, last_name FROM students WHERE last_name='Benichou' AND  first_name='Marc'
-- Select 3.3
-- SELECT first_name, last_name FROM students WHERE last_name='Benichou' OR  first_name='Marc'
-- Select 3.4
-- SELECT first_name, last_name FROM students WHERE first_name LIKE '%a%'
-- Select 3.5
-- SELECT first_name, last_name FROM students WHERE first_name ILIKE 'a%'
-- Select 3.6
-- SELECT first_name, last_name FROM students WHERE first_name ILIKE '%a'
-- Select 3.7
-- SELECT first_name, last_name FROM students WHERE first_name LIKE '%a_' 
-- Select 3.8
-- SELECT first_name, last_name FROM students WHERE students_id =1 OR students_id =3
-- Select 4
-- SELECT * FROM students WHERE birth_date >= '1/01/2000' 