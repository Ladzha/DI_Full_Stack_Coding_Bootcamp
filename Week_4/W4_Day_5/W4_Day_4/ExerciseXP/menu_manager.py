from connection import Connection #don't work

import psycopg2

connection = psycopg2.connect(
    database="Restaurant", 
    user='postgres',
    password='root',
    host='localhost', 
    port='5432'
)

cursor = connection.cursor()

class MenuManager():

    @classmethod
    def get_by_name(cls, name):
        try:
            connection = psycopg2.connect(
            database="Restaurant", 
            user='postgres',
            password='root',
            host='localhost', 
            port='5432'
        )

            cursor = connection.cursor()
            query = f"SELECT item_name, item_price FROM menu_Items WHERE item_name = '{name}'"
            cursor.execute(query)
            result = cursor.fetchall()
            print(result)
        except:
            print('We don\'t have this in the menu')
        finally:
            if connection:
                cursor.close()
                connection.close()

    @classmethod
    def all_items(cls) :
        connection = psycopg2.connect(
        database="Restaurant", 
        user='postgres',
        password='root',
        host='localhost', 
        port='5432'
        )
        cursor = connection.cursor() 
        query = "SELECT * FROM menu_Items"
        cursor.execute(query)
        result = cursor.fetchall()
        item_list =[]
        for item in result:
            item_list.append(item)
            print(f"We have - {item[1]}. Price - {item[2]}.")
        return item_list
        cursor.close()
        connection.close()
MenuManager.get_by_name('Roll')
# MenuManager.all_items()