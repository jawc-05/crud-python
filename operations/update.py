from mysql.connector import Error
from connection import db_manager
from settings import TABLE_NAME

def update_user():

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

    connection = db.manager.create_connection()
    if not connection: return

    with connection:
        with connection.cursor() as cursor:
            try:
                cursor.execute(query, data)
                connection.commit()