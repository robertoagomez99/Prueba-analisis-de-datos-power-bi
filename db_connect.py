import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

def get_db_engine():
    # Cargar variables del archivo .env
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
    print(" Try out to get connection to POSTGRESQL")
    print(f"{'='*40}")
    try:
        engine = get_db_engine()
        with engine.connect() as connection:
            result = connection.execute(text("SELECT version();"))
            version = result.fetchone()[0]
            print("Succesfully connection")
            print(f"Database: {os.getenv('DB_NAME')}")
            return True
    except Exception as e:
        print("\nFailed the connection")
        print(f"The mistake is: {e}")
        return False
if __name__ == "__main__":
    test_connection()