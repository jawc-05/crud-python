# Importa as funções de cada módulo de operação
from operations.setup_read import setup_database
from operations.read import read_users
from operations.create import create_user
from operations.update import update_user 
from operations.delete import delete_user 

def main():
    #FUNÇÃO PRINCIPAL QUE GERENCIA O PROGRAMA
    
    crud_actions = {
        '1': create_user,
        '2': read_users,
        '3': update_user, 
        '4': delete_user, 
    }

    while True:
        print("\n" + "=" * 50)
        print("  SISTEMA CRUD PYTHON  ")
        print("=" * 50)
        print(" [0] CONFIGURAR/SETUP do Banco de Dados")
        print(" [1] CREATE (Criar Usuário)")
        print(" [2] READ (Listar Usuários)")
        print(" [3] UPDATE (Atualizar Usuário)")
        print(" [4] DELETE (Deletar Usuário)")
        print(" [5] SAIR")
        print("-" * 50)

        choice = input("Escolha uma opção: ")

        if choice == '5':
            print("Encerrando o sistema. Até logo!")
            break
        
        elif choice == '0':
            setup_database()
        
        elif choice in crud_actions:
            action_function = crud_actions[choice]
            action_function()
            
        else:
            print("\nOpção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
