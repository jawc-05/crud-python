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
