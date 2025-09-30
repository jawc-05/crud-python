from getpass import getpass
from settings import DB_NAME
from mysql.connector import connect, Error

def create_connection(action):
    try:
        with connect(
            host = "localhost",
            user = input("Digite o usuário do banco de dados: "),
            password = getpass("Digite a senha do banco de dados: "),
        ) as connection:
            print("Conexão bem sucedida!", connection)
            return action(connection)
    except Error as e:
        print("Ocorreu um erro ao tentar se conectar ao banco de dados.")