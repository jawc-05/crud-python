from mysql.connector import Error
from database.connection import db_manager
from configs.settings import TABLE_NAME

def read_users():
    #ESSA FUNCAO EXECUTA UM READ DA TABLE INTEIRA(usuarios)
    query = f"SELECT cpf, nome, email FROM {TABLE_NAME}"
    
    #ESTABELE A CONEXAO USANDO A INSTANCIA POO DA CAMADA database
    connection = db_manager.create_connection()
    if not connection: return

    with connection:
        with connection.cursor() as cursor:
            try:
                #EXECUTA A CONSULTA
                cursor.execute(query)

                #RECUPERA TODOS OS DADOS DO BANCO DE DADOS E OS COLOCA EM UMA LISTA
                users = cursor.fetchall()

                if not users:
                    print("\n Nenhum usuário encontrado na tabela '{TABLE_NAME}', cadastre um novo usuário.")

                #EXIBE DE FORMA FORMATADA
                print("\n" + "=" * 77)
                print("--- LISTA DE USUÁRIOS ---")
                print(f"{'CPF':<15} | {'Nome':<30} | {'Email':<30}")
                print("=" * 77)

                for cpf, nome, email in users:
                    print(f"{cpf:<15} | {nome:<30} | {email:<30}")
                print("=" * 77 + "\n")
            
            except Error as e:
                #TRATA OS ERROS DO SQL
                print(f"\n Erro ao ler usuários: {e}")