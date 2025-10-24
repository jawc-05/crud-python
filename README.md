# 🐍 CRUD PYTHON + MYSQL: Projeto Modular em Camadas

## 🚀 Visão Geral do Projeto 

Este projeto é uma implementação completa das operações CRUD (Create, Read, Update, Delete) usando Python 3 e MySQL. O principal objetivo é demonstrar uma arquitetura de código modular e profissional, onde as responsabilidades são estritamente separadas em camadas.

O código prova o domínio das boas práticas:

- **POO:** Uso de classes (`ConnectionManager`) para isolar a infraestrutura.
- **Modularidade:** Separação de lógica por arquivos (`create.py`, `read.py`, etc.).
- **Robustez:** Tratamento de erros específicos do MySQL (ex: duplicidade de CPF/Email).

## 📂 Estrutura Modular (Por Camadas)

O projeto é organizado por pastas, seguindo o princípio da Separação de Preocupações (SoC):

| Pasta         | Responsabilidade                                                        |
|---------------|------------------------------------------------------------------------|
| `main.py`     | Interface/Fluxo: Ponto de entrada e Menu Principal.                    |
| `configs/`     | Configurações: Constantes e variáveis globais (`DB_NAME`).             |
| `database/`   | Infraestrutura: Lógica de conexão, credenciais e tratamento de erro.   |
| `operations/` | Lógica de Negócio: Funções específicas do CRUD (INSERT, SELECT, etc.). |
| `sql_scripts/`| Documentação: Scripts para setup manual e carga de dados de teste.      |

## 🛠️ Como Rodar o Projeto Localmente

### Pré-requisitos

- Python 3.x instalado.
- MySQL Server instalado e em execução.
- Um usuário MySQL com permissões para criar bancos de dados.

### 1. Clonar e Criar o Ambiente Virtual (venv)

Clone o projeto, entre no diretório e crie/ative o ambiente virtual para isolar as dependências.

| Sistema Operacional | Criar venv               | Ativar venv                |
|---------------------|-------------------------|----------------------------|
| macOS/Linux         | `python3 -m venv venv`  | `source venv/bin/activate` |
| Windows             | `python -m venv venv`   | `venv\Scripts\activate`    |

### 2. Instalar Dependências

Com o ambiente virtual ativado, instale todas as bibliotecas necessárias listadas no `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 3. Executar o Programa e Configurar o Banco

O programa é iniciado pelo `main.py`. Na primeira execução, o sistema pedirá suas credenciais do MySQL.

```bash
python main.py
```

**Passo Essencial:** Escolha a opção `[0] CONFIGURAR/SETUP` na primeira vez! Isso criará o banco de dados `crud_python` e a tabela `usuarios`.

## 4. (Opcional) Carregar Dados de Teste

Para popular a tabela com dados iniciais e testar as operações CRUD, use o script de seed (carga de dados):

```bash
# Executa o script de seed manualmente
mysql -u [SEU_USUARIO] -p crud_python < sql_scripts/seed_data.sql
```

## 🔑 Detalhes da Tabela

- **Banco de Dados:** `crud_python`
- **Tabela:** `usuarios`
- **Schema:**
  - `cpf` (VARCHAR(14)): PRIMARY KEY
  - `nome` (VARCHAR(100)): NOT NULL
  - `email` (VARCHAR(100)): UNIQUE NOT NULL

## 📝 Licença

Este projeto está sob a licença [MIT License](LICENSE) (ou outra licença de sua escolha).

---