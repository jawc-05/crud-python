from mysql.connector import Error
from connection import db_manager 
from settings import TABLE_NAME, DB_NAME 

def setup_database():
    
    connection = db_manager.connect_only_server()
    if not connection:
        print("Não foi possível iniciar o setup. Verifique as credenciais e tente novamente.")
        return