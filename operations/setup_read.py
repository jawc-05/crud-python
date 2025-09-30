from mysql.connector import Error
from connection import db_manager 
from settings import TABLE_NAME, DB_NAME 

def setup_database():
    
    connection = db_manager.connect_only_server()
    if not connection:
        print("Não foi possível iniciar o setup. Verifique as credenciais e tente novamente.")
        return
    
    with connection:
        try:
            with connection.cursor() as cursor:

                cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
                print(f"Banco de dados '{DB_NAME}' verificado/criado.")

                connection.database = DB_NAME

                create_table_query = f"""
                CREATE TABLE IF NOT EXISTS {TABLE_NAME}(
                    cpf VARCHAR(14) PRIMARY KEY,
                    nome VARCHAR(100) NOT NULL,
                    email VARCHAR(100) UNIQUE NOT NULL
                )"""
                cursor.execute(create_table_query)
                connection.commit()
                print(f"Table: '{TABLE_NAME}' verificada/criada.")

        except Error as e:
            print(f"\n Erro na configuração do banco de dados: {e}")