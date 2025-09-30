from mysql.connector import Error
from connection import db_manager
from settings import TABLE_NAME

def read_user():
    query = f"SELECT cpf, nome, email FROM {TABLE_NAME}"
    
    connection = db_manager.create_connection()
    if not connection: return

    with connection:
        with connection.cursor() as cursor:
            try:
                cursor.execute(query)

                users = cursor.fetchall()

                if not users:
                    print("\n Nenhum usuário encontrado na tabela '{TABLE_NAME}', cadastre um novo usuário.")

                print("\n" + "=" * 77)
                print("--- LISTA DE USUÁRIOS ---")
                print(f"{'CPF':<15} | {'Nome':<30} | {'Email':<30}")
                print("=" * 77)

                for cpf, nome, email in users:
                    print(f"{cpf:<15} | {nome:<30} | {email:<30}")
                print("=" * 77 + "\n")
            
            except Error as e:
                print(f"\n Erro ao ler usuários: {e}")