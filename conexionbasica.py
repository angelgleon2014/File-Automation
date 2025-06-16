import psycopg2

def getConnection():    
    try:
        conexion = psycopg2.connect(
            host='localhost',
            database='db',
            user='postgres',
            password='an822237'
        )
        print("Conexión exitosa a la base de datos.")
        return conexion
    except psycopg2.DatabaseError as error:
        print(f"Error al conectar a la base de datos: {error}")
        return None
    
""" def getConnection():
    try:
        conexion = psycopg2.connect(
            host='localhost',
            database='db',
            user='postgres',
            password='an822237'
        )
        print("Conexión exitosa a la base de datos.")
        return conexion
    except psycopg2.DatabaseError as error:
        print(f"Error al conectar a la base de datos: {error}")
        return None """
getConnection()