import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

def get_db_engine():
    """
    Lee las variables de entorno y devuelve el motor de conexión SQLAlchemy.
    """
    # 1. Cargar variables del archivo .env
    load_dotenv(override=True) 

    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    host = os.getenv('DB_HOST')
    port = os.getenv('DB_PORT', '5432')
    dbname = os.getenv('DB_NAME')

    if not user or not password or not dbname:
        raise ValueError("Error: Faltan variables en el archivo .env (DB_USER, DB_PASSWORD o DB_NAME).")
    connection_string = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}"

    # 3. Crear y retornar el engine
    try:
        engine = create_engine(connection_string)
        return engine
    except Exception as e:
        print(f"Error al configurar el engine: {e}")
        return None

def test_connection():
    print(f"\n{'='*40}")
    print(" 🔌 PRUEBA DE CONEXIÓN A POSTGRESQL")
    print(f"{'='*40}")

    try:
        engine = get_db_engine()
    
        with engine.connect() as connection:
            result = connection.execute(text("SELECT version();"))
            version = result.fetchone()[0]
            
            print("¡CONEXIÓN EXITOSA!")
            print(f"Base de Datos: {os.getenv('DB_NAME')}")
            print(f"Versión: {version}")
            print("\nTodo listo para cargar los datos.")
            return True

    except Exception as e:
        print("\nFALLO LA CONEXIÓN.")
        print(f"Error técnico: {e}")
        print("\nPosibles causas:")
        print("1. El archivo .env no esta en la misma carpeta.")
        print("2. La contraseña o usuario son incorrectos.")
        print("3. La base de datos 'ventas' no existe en DBeaver todavia.")
        print("4. El puerto 5432 está ocupado o es incorrecto.")
        return False

if __name__ == "__main__":
    test_connection()