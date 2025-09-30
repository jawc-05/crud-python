from mysql.connector import Error
from connection import db_manager
from settings import TABLE_NAME


def delete_user():

    print("\n--- DELETAR USUÁRIO ---")

    cpf = input("Digite o CPF do usuário que deseja DELETAR: ")
    