from mysql.connector import Error
from connection import db_manager
from settings import TABLE_NAME

def create_user():

    print("\n ---CADASTRAR NOVO USUÁRIO---")
    cpf = input("Digite o CPF (PK): ")
    nome = input("Digite o nome: ")
    email = input("Digite o email: ")

    query = f""""
    INSERT INTO {TABLE_NAME} (cpf, nome, email)
    VALUES (%s, %s, %s)
    """
    data = (cpf, nome, email)