from multiprocessing import connection
import psycopg2
class Connection():
    def __init__(self):
        pass

    def manage_connection_fetchall(self, query): 
        try:
            connection=psycopg2.connect(
                database ='Restaurant',
                user = 'postgres',
                password ='root',
                host='localhost',
                port = '5432'    
            )
            with connection:
                with connection.cursor() as cursor:
                    cursor.executese(query)   
                    result = cursor.fetchall()   
                    return result 
        except Exception:
            print('OH NO!!!')
        finally: 
            connection.close()

    def manage_connection_fetchone(self, query): 
        try:
            connection=psycopg2.connect(
                database ='Restaurant',
                user = 'postgres',
                password ='root',
                host='localhost',
                port = '5432'    
            )
            with connection:
                with connection.cursor() as cursor:
                    cursor.executese(query)   
                    result = cursor.fetchone()   
                    return result 
        except Exception:
            print('OH NO!!!')
        finally: 
            connection.close()
            