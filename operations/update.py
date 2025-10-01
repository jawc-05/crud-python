from mysql.connector import Error
from database.connection import db_manager
from configs.settings import TABLE_NAME

def update_user():
    #ESSA FUNÇÃO ATUALIZA OS CAMPOS(email/nome) DE UM USUÁRIO, USANDO O CPF COMO IDENTIFICADOR
    print("\n--- ATUALIZAR USUÁRIO ---")

    cpf = input("Digite o CPF do usuário que deseja ATUALIZAR: ")

    new_name = input("Digite o NOVO nome (ou ENTER para manter): ")
    new_email = input("Digite o NOVO email (ou ENTER para manter): ")

    updates=[]
    data=[]

    if new_name.strip():
        updates.append("nome = %s")
        data.append(new_name)

    if new_email.strip():
        updates.append("email = %s")
        data.append(new_email)

    if not updates:
        print("\n Nenhuma alteração fornecida. Operação cancelada.")
        return
    
    data.append(cpf)

    query = f"""
    UPDATE {TABLE_NAME}
    SET {', '.join(updates)}
    WHERE cpf = %s
    """.strip()

    connection = db_manager.create_connection()
    if not connection: return

    with connection:
        with connection.cursor() as cursor:
            try:
                cursor.execute(query, tuple((data)))
                connection.commit()

                if cursor.rowcount > 0:
                    print(f"\n Usuário de CPF {cpf} atualizado com sucesso! (Campos alterados: {cursor.rowcount})")
                else:
                    print(f"\n Nenhum usuário encontrado com o CPF {cpf}. Nada foi atualizado.")
            
            except Error as e:
                #TRATA ERROR COMO TENTAR ATUALIZAR PARA UM EMAIL QUE JÁ EXISTE (1062)
                if e.errno == 1062:
                    print("\n Erro: O novo EMAIL digitado já pertence a outro usuário.")
                else:
                    print(f"\n Erro ao atualizar usuário: {e}")