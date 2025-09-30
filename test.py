from connection import create_connection

def list_databases(connection):
    with connection.cursor() as cursor:
        cursor.execute("SHOW DATABASES")
        for db in cursor:
            print(db[0])

create_connection(list_databases)