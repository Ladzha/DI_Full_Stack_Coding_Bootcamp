-- CREATE TABLE city_info 
-- ( event_datetime timestamp NOT NULL, 
-- city VARCHAR(50) NOT NULL, 
-- temperature decimal NOT NULL, 
-- light decimal NOT NULL,
-- airquality_raw decimal NOT NULL, 
-- sound decimal NOT NULL, 
-- humidity decimal NOT NULL, 
-- dust decimal NOT NULL )

-- SELECT * FROM city_info

-- COPY city_info(event_datetime, city, temperature,light, airquality_raw, sound, humidity, dust) 
-- FROM 'C:\Users\Public\city_info.csv' DELIMITER ',' CSV HEADER;

-- SELECT * FROM city_info
-- SELECT COUNT (*) FROM city_info
-- 2
-- SELECT temperature FROM city_info WHERE event_datetime = '2015-03-01 11:00:00'AND city ='Boston'
-- 3
-- SELECT ROUND(temperature), EXTRACT(DAY FROM event_datetime) AS day, EXTRACT(HOUR FROM event_datetime) AS hour FROM city_info WHERE temperature BETWEEN 28 AND 30 AND city ='San Francisco' 
-- 4
-- SELECT city, event_datetime, sound FROM city_info ORDER BY  sound ASC LIMIT 1
-- 5
-- SELECT city, event_datetime, sound FROM city_info ORDER BY  sound DESC LIMIT 1
-- 6
--***********************
-- SELECT dust, event_datetime FROM city_info WHERE city ='San Francisco' AND DATE(event_datetime) = '2015-03-26 20:00:00' AND EXTRACT (HOUR FROM event_datetime) > 20
--***********************
-- 7 
-- SELECT city, event_datetime FROM city_info WHERE (humidity <40 OR humidity>60) AND city = 'Geneva'
-- 8
-- SELECT city, TO_CHAR(event_datetime, 'day') FROM city_info ORDER BY light ASC LIMIT 1
-- or 
-- SELECT city, TO_CHAR(event_datetime, 'day') FROM city_info WHERE light = (SELECT MAX(light) FROM city_info)
-- 9
-- SELECT DISTINCT city FROM city_info WHERE city ILIKE 'S%' 
-- 10
-- INSERT INTO city_info
-- (event_datetime, city, temperature, light, airquality_raw, sound, humidity, dust)
-- VALUES ('2015-03-01 11:00:00', 'Tel-Aviv', 24, 3, 4, 4, 30, 5)
-- RETURNING (event_datetime, city, temperature, light, airquality_raw, sound, humidity, dust)


-- 10. Add to the table, todays information in Israel - of this very hour. (event_datetime,city,temperature,light,airquality_raw,sound,humidity,dust) -- - Use the return statement to see what you just inserted:
-- INSERT INTO city_info (event_datetime,city,temperature,light,airquality_raw,sound,humidity,dust) 
-- VALUES (NOW(), 'Israel', '10', 10,10,10,10,10) RETURNING *
