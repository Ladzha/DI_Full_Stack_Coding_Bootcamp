-- CREATE TABLE FirstTab (
--      id integer, 
--      name VARCHAR(10)
-- )

-- INSERT INTO FirstTab VALUES
-- (5,'Pawan'),
-- (6,'Sharlee'),
-- (7,'Krish'),
-- (NULL,'Avtaar')

-- SELECT * FROM FirstTab

-- CREATE TABLE SecondTab (
--     id integer 
-- )

-- INSERT INTO SecondTab VALUES
-- (5),
-- (NULL)

-- SELECT * FROM SecondTab

-- SELECT COUNT(*) 
-- FROM FirstTab AS ft WHERE ft.id NOT IN (SELECT id FROM SecondTab WHERE id IS NULL )
-- **********=> 4 rows in FirstTab. 1 id = NULL => 3 ids in FirstTab.
-- 2 rows in SecondTab. 1 id = NULL
-- But we get NULL in brackets
-- NULL IS NOT A VALUE, SO WE CAN'T COMPARE WITH NOTHING. Outcome = 0


-- SELECT COUNT(*) 
-- FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id = 5 ) 
-- **********=> 4 rows in FirstTab. 1 id = NULL => 3 ids in FirstTab. 
-- 3 ids - 1 id (= 5 is in SecondTab) = 2 ids

-- SELECT COUNT(*)
-- FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab )
-- **********=> 4 rows in FirstTab. 1 id = NULL => 3 ids in FirstTab.
-- But we get NULL (and 5 ) in brackets
-- NULL IS NOT A VALUE, SO WE CAN'T COMPARE WITH NOTHING. Outcome = 0

-- SELECT COUNT(*)
-- FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NOT NULL)
-- **********=> 4 rows in FirstTab. 1 id = NULL => 3 ids in FirstTab.
-- 2 rows in SecondTab. 1 id != NULL (id = 5)
-- 3 ids (=5,=6,=7) in FirstTab - 1 id = 5 = 2 id