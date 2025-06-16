import psycopg2
DATABASE_CONFIG = {
    'dbname': 'bd',
    'user': 'postgres',
    'password': 'an822237',
    'host': 'localhost',
    'port': '5432',
    'options': '-c client_encoding=UTF8'  # Forzar la conexión en UTF-8
}
def getConnection():
    try:
        conexion = psycopg2.connect(
            host='localhost',
            database='db',
            user='postgres',
            password='an822237'
        )
        return conexion
    except psycopg2.DatabaseError as error:
        print(f"Error al conectar a la base de datos: {error}")
        return None
    
def guardar_usuario_en_bd():
    """Guarda el usuario en la base de datos PostgreSQL."""
    # password_encriptado = encriptar_password(usuario['CardNo'])
    # full_name = f"{usuario['name']} {usuario['lastname']}"
    full_name = "JAMILET CHICHANDE"
    # date_joined = usuario['acc_startdate'][:10]  # Extraer solo la fecha sin los últimos 9 caracteres
    date_joined = "2024-11-25"
    last_login = '2024-11-25'
    is_superuser = False
    image = ''
    is_active = True
    is_staff = False
    is_change_password = False
    email_reset_token = ''
    email = "jamiletchichande@gmail.com"

    connection = None  # Definir la conexión antes del bloque try

    try:
        # connection = psycopg2.connect(**DATABASE_CONFIG)
        connection = getConnection()
        cursor = connection.cursor()
        print("antes de la query")
        # Insertar en la tabla `atlasfitnessclub.user_user`
        query = """
        INSERT INTO atlasfitnessclub.user_user (
            last_login, is_superuser, names, image, email,
            is_active, is_staff, date_joined, is_change_password, email_reset_token
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (
            # password_encriptado,
            last_login,     
            is_superuser,
            full_name,
            image,
            email,
            # usuario['email'],
            is_active,
            is_staff,
            date_joined,
            is_change_password,
            email_reset_token
        ))

        connection.commit()
        print(f"Usuario {full_name} guardado exitosamente.")

    except Exception as e:
        print(f"Error al guardar el usuario {full_name}: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()
guardar_usuario_en_bd()