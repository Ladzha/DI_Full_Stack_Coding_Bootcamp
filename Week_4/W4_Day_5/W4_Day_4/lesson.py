from multiprocessing import connection
import psycopg2
def manage_connection(query): 
    try:
        connection=psycopg2.connect(
            database ='Hollywood',
            user = 'postgres',
            password ='root',
            host='localhost',
            port = '5432'    
        )
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(query)   
                result = cursor.fetchall()   
                return result 
    except Exception:
        print('OH NO!!!')
    finally: 
        connection.close()
    
    
def manage_connection_one(query): 
    try:
        connection=psycopg2.connect(
            database ='Hollywood',
            user = 'postgres',
            password ='root',
            host='localhost',
            port = '5432'    
        )
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(query)   
                result = cursor.fetchone()   
                return result 
    except Exception:
        print('OH NO!!!')
    finally: 
        connection.close()

def get_all_actors(user_answer):
    query = f'SELECT * FROM actor WHERE salary > {user_answer}'
    result = manage_connection(query)
    for actor in result:
        print(f'The actor is {actor[1]} {actor[2]}. He is {actor[-1]}')

get_all_actors(50000)

def get_actor_by_last_name(name):
    query = f'SELECT * FROM actor WHERE last_name={name}'
    result = manage_connection_one(query)
    print(result)
get_actor_by_last_name('Samers')

# def get_alla_actors():
#     query = 'SELECT * FROM actor'
#     cursor.execute(query)
#     result = cursor.fetchall()
#     for actor in result:
#         print(f'The actor is {actor[1]} {actor[2]}. He is {actor[-1]}')
# get_alla_actors()
# query = 'SELECT first_name, last_name FROM actor'
# cursor.execute(query)
# result = cursor.fetchall()

# query = '''SELECT concat(first_name, ' ', last_name) AS "full_name" FROM actor'''
# cursor.execute(query)
# result = cursor.fetchall()

# print(result)
# cursor.close()
# connection.close()
