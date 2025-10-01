from mysql.connector import Error
from database.connection import db_manager
from configs.settings import TABLE_NAME


def delete_user():

    print("\n--- DELETAR USUÁRIO ---")

    cpf = input("Digite o CPF do usuário que deseja DELETAR: ")

    query = f"DELETE FROM {TABLE_NAME} WHERE CPF = %s"
    data=(cpf,)

    connection = db_manager.create_connection()
    if not connection: return

    with connection:
        with connection.cursor() as cursor:
            try:
                cursor.execute(query, data)
                connection.commit()

                if cursor.rowcount > 0:
                    print(f"\n Usuário do {cpf} DELETADO com sucesso")
                else:
                    print(f"\n Nenhum usuário com o CPF: {cpf}. Nada foi DELETADO.")

            except Error as e:
                print(f"\n Erro ao deletar usuário: {e}")