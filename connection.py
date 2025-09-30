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

    def get_credentials_if_needed(self):
        #AQUI PEGAMOS AS CREDENCIAIS DO USUÁRIO#

        if not self.user:
            # ESSE * 50 SERVE PARA FAZER UMA LINHA DE SEPARAÇÃO#
            print("\n" + "=" * 50)
            print("  CONFIGURAÇÃO DE ACESSO AO BANCO DE DADOS")
            print("=" * 50)
            self.user = input("Digite o usuário do banco de dados: ")
            self.password = getpass("Digite a senha do banco de dados: ")
            print("-" * 50)

    def create_connection(self):
        self.get_credentials_if_needed()
        db_to_connect= self.database

        try:
            return connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=db_to_connect
            )
        except Error as e:
            print(f"\n Erro ao conectar ao MySQL (DB: {db_to_connect}): {e}")
            self.password = None 
            return None
        
    def connect_only_server(self):
        self.get_credentials_if_needed()
        db_to_connect= None

        # Conecta sem especificar o banco de dados, útil para criar o banco se não existir #

        try:
            return connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=db_to_connect 
            )
        except Error as e:
            print(f"\n Erro ao conectar ao MySQL Server: {e}")
            return None
        
db_manager = ConnectionManager()