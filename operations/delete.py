from mysql.connector import Error
from database.connection import db_manager
from configs.settings import TABLE_NAME


def delete_user():
    #ESSA FUNÇÃO EXCLUIR UM USUÁRIO DA TABELA usuario UTILIZANDO O CPF(PK)
    print("\n--- DELETAR USUÁRIO ---")

    cpf = input("Digite o CPF do usuário que deseja DELETAR: ")

    query = f"DELETE FROM {TABLE_NAME} WHERE CPF = %s"
    data=(cpf,)

    #ESTABELECE A CONEXAO USANDO A INSTANCIA POO DA CAMADA database
    connection = db_manager.create_connection()
    if not connection: return

    with connection:
        with connection.cursor() as cursor:
            try:
                #EXECUTA O DELETE
                cursor.execute(query, data)
                connection.commit()

                #VERIFICA cursor.rowcount: SE FOR > 0, O REGISTRO FOI ENCONTRADO E DELETADO.
                if cursor.rowcount > 0:
                    print(f"\n Usuário do {cpf} DELETADO com sucesso")
                else:
                    print(f"\n Nenhum usuário com o CPF: {cpf}. Nada foi DELETADO.")

            #TRATA OS ERROS DO SQL
            except Error as e:
                print(f"\n Erro ao deletar usuário: {e}")