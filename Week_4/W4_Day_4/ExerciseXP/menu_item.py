from menu_manager import MenuManager

from connection import Connection

import psycopg2

connection = psycopg2.connect(
    database="Restaurant", 
    user='postgres',
    password='root',
    host='localhost', 
    port='5432'
)

cursor = connection.cursor()

class  MenuItem():
    def __init__(self, name, price=0):
        self.name = name
        self.price = price
        
    def save(self):
        query_user = f"""
        INSERT INTO menu_Items 
        (item_name, item_price)
        VALUES {self.name, self.price}
        """
        cursor.execute(query_user)
        connection.commit() 
    
    def delete(self):
        query = f"""
        DELETE FROM menu_Items WHERE item_name = '{self.name}'
        """
        cursor.execute(query)
        connection.commit()  
    
    def update(self, name, price):     
        query = f"""
        UPDATE menu_Items 
        SET item_name = '{name}', item_price = '{price}'
        WHERE item_name = '{self.name}'
        """
        cursor.execute(query)
        connection.commit() 

item = MenuItem('Burger', 35)
item.save()
item.delete()
item.update('Veggie Burger', 37)
item.update('Roll', 28)
item2 = MenuManager.get_by_name('Beef Stew')
items = MenuManager.all_items()

connection.commit() 
cursor.close()
connection.close()