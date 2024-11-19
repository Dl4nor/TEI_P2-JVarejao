import collections
import sqlite3 as sql
import utils.utillities as UUtil
import bcrypt

# Função que cria o banco de dados
#  e as tabelas que utilizamos no programa
#  caso as tabeals já existam, nada acontece
#  e tudo bem
def database_create():
    connect = sql.connect("jvarejao.db")
    cursor = connect.cursor()

    ## Criar tabela de usuários
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tb_users(
        id_user INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )
    """)

    ## Criar tabela de produtos
    # cursor.execute("""
        
    # """)

    ## Criar tabela de lojas
    # cursor.execute("""
        
    # """)

    connect.commit()
    connect.close()

# Função que insere o usuário no nosso Banco
#  executamos essa função na opção 2 do FirstMenu()
#  no menu_controller.py
# Recebemos o username e a senha criptografada para
#  inserir ao Banco jvarejao.bd (SQLite)
def database_user_register(username, userPassword):
    connect = sql.connect("jvarejao.db")
    cursor = connect.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO tb_users (username, password) 
            VALUES (?, ?)
            """, 
            (username, userPassword)
        )
        connect.commit()
        print("| Usuário cadastrado com sucesso!!\n")
        input("[ENTER PARA RETORNAR...]")
    except sql.IntegrityError:
        print("ERRO: nome de usuário já cadastrado!!")
        input()
    finally:
        connect.close

# Função que valida o login do usuário
#  executamos essa função na opção 1 do FirstMenu()
#  no menu_controller.py
# Recebemos username e a senha criptografada para
#  validar o login do usuário de acordo com os dados
#  do Banco jvarejao.bd
def database_user_login(username, userPassword):
    connect = sql.connect("jvarejao.db")
    cursor = connect.cursor()

    cursor.execute(
        """
        SELECT password
        FROM tb_users
        WHERE username = ?
        """, 
        (username)
    )
    result = cursor.fetchone()

    if(result):
        hashed_password = result[0]

        if(bcrypt.checkpw(userPassword.encode('utf-8'), hashed_password.encode('utf-8'))):
            UUtil.wait_print("Login realizado com sucesso!!")
            connect.close()
            return True

    UUtil.wait_print("Falha de autenticação, tente novamente!")
    connect.close()
    return False

# Antiga função utilizada para criar o Map
#  dos produtos (vai ser substituída por uma
#  que utiliza SQLite)
def criar_produto_namedtuple():
    """Cria o namedtuple para o modelo Produto."""
    return collections.namedtuple("Produtos", "codigo nome preco_compra preco_venda quantidade")
