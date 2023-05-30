import random
import requests
import json
import psycopg2

connection=psycopg2.connect(
    database ='countries',
    user = 'postgres',
    password ='root',
    host='localhost',
    port = '5432'    
)

cursor = connection.cursor()

# create_table = ('CREATE TABLE many_countries (id SERIAL PRIMARY KEY, name VARCHAR(100) NOT NULL, capital VARCHAR(100), flag_code VARCHAR(100) NOT NULL, subregion VARCHAR(100) NOT NULL, population INTEGER)')
# cursor.execute(create_table)
# connection.commit()


# delete_table = 'DROP TABLE many_countries'
# cursor.execute(delete_table)

countries_api = requests.get('https://restcountries.com/v3.1/all')
data = countries_api.json()

for i in range(1,11):
    index = random.randint(1, 100)
    name = data[index]['name']['common']
    capital = data[index]['capital'][0]
    flag = data[index]['flag']
    subregion = data[index]['subregion']
    population = data[index]['population']
    quary = (f"INSERT INTO many_countries (name, capital, flag_code, subregion, population) VALUES ('{name}', '{capital}', '{flag}', '{subregion}', '{population}')")
    cursor.execute(quary)
    connection.commit()

select_quary = ('SELECT * FROM many_countries')
cursor.execute(select_quary)
connection.commit()
cursor.close()
connection.close()