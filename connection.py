from getpass import getpass
from mysql.connector import connect, Error
from settings import DB_NAME


class ConnectionManager:
    #NESSA CLASSE GERENCIAMOS A CONEXÃO COM O BANCO DE DADOS#

    def __init__(self, host="localhost"):
        self.host = host
        self.user = None
        self.password = None
        self.database = DB_NAME



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