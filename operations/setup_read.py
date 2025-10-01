from mysql.connector import Error
from database.connection import db_manager 
from configs.settings import TABLE_NAME, DB_NAME 

def setup_database():
    #FUNÇAO INICIAL QUE CONFIGURA O AMBIENTE: CRIANDO O BANCO DE DADOS E A TABELA usuarios


    #USA O 'connect_only_server' PORQUE O BANCO DE DADOS AINDA NAO EXISTE
    connection = db_manager.connect_only_server()
    if not connection:
        print("Não foi possível iniciar o setup. Verifique as credenciais e tente novamente.")
        return
    
    with connection:
        try:
            with connection.cursor() as cursor:
                
                #CRIA O BANCO DE DADOS UTILIZANDO O IF NOT EXISTS PARA EVITAR DUPLICAÇÕES
                cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
                print(f"Banco de dados '{DB_NAME}' verificado/criado.")

                #EQUIVALENTE AO COMANDO 'USE crud_python' NO SQL.
                connection.database = DB_NAME

                #CRIA A TABELA UTILIZANDO O IF NOT EXISTS PARA EVITAR DUPLICAÇÕES
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