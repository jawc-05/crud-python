from mysql.connector import Error
from connection import db_manager
from settings import TABLE_NAME

def create_user():

    print("\n ---CADASTRAR NOVO USUÁRIO---")
    cpf = input("Digite o CPF (PK): ")
    nome = input("Digite o nome: ")
    email = input("Digite o email: ")

    query = f"""
    INSERT INTO {TABLE_NAME} (cpf, nome, email)
    VALUES (%s, %s, %s)
    """
    data = (cpf, nome, email)

    connection = db_manager.create_connection()
    if not connection: return

    with connection:
        with connection.cursor() as cursor:
            try:
                #AQUI TERA O INSERT
                cursor.execute(query, data)
                connection.commit()
                print(f"\n Usuário '{nome}'(CPF: {cpf}) cadastrado com sucesso!")

            except Error as e:
                # TRATA O ERRO DE CHAVE DUPLICADA (CPF OU EMAIL JÁ CADASTRADO) #
                if e.errno == 1062:
                    print("\n Erro: CPF ou EMAIL já cadastrado. Tente novamente.")
                else:
                    print(f"\n Erro ao criar usuário: {e}")