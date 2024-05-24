import pymysql

def conectar():
    """Función para establecer una conexión con la base de datos."""
    try:
        conexion = pymysql.connect(
            host='database-gr8.cjw6i8gwoa18.us-east-2.rds.amazonaws.com',
            user='admin',  # Reemplaza con el nombre de usuario de tu base de datos
            password='1000731037',  # Reemplaza con la contraseña de tu base de datos
            database='bd_users',  # Reemplaza con el nombre de tu base de datos
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        print("Conexión establecida con la base de datos.")
        return conexion
    except pymysql.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

def consultar(conexion):
    """Función para consultar datos en la base de datos."""
    try:
        with conexion.cursor() as cursor:
            sql = "SELECT * FROM users"  # Reemplaza 'tabla' con el nombre de tu tabla
            cursor.execute(sql)
            resultados = cursor.fetchall()
            return resultados
    except pymysql.Error as e:
        print(f"Error al consultar datos: {e}")
        return None

def insertar(conexion, documento, nombres, apellidos, correo, edad):
    """Función para insertar datos en la base de datos."""
    try:
        with conexion.cursor() as cursor:
            sql = "INSERT INTO users (documento, nombres, apellidos, correo, edad) VALUES (%s, %s, %s, %s, %s)"  # Reemplaza 'tabla' y 'campo1', 'campo2', 'campo3' con tus nombres de tabla y campos
            cursor.execute(sql, (documento, nombres, apellidos, correo, edad))
        conexion.commit()
        print("Datos insertados correctamente.")
    except pymysql.Error as e:
        print(f"Error al insertar datos: {e}")

def consultar_por_documento(conexion, documento):
    """Función para consultar datos en la base de datos por documento."""
    
    try:
        with conexion.cursor() as cursor:
            sql = "SELECT * FROM users WHERE documento = %s"
            cursor.execute(sql, (documento,))
            resultados = cursor.fetchall()
            return resultados
    except pymysql.Error as e:
        print(f"Error al consultar datos: {e}")
        return None