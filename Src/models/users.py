import utils.utillities as utilU
from models import stores as storeM, produto as prodM, sales as saleM
import bcrypt
import sqlite3 as sql

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
        utilU.wait_print("| Usuário cadastrado com sucesso!!\n")
    except sql.IntegrityError:
        utilU.wait_print("| ERRO: nome de usuário já cadastrado!!")
    finally:
        connect.close()

# Função que valida o login do usuário
#  executamos essa função na opção 1 do FirstMenu()
#  no menu_controller.py
# Recebemos username e a senha criptografada para
#  validar o login do usuário de acordo com os dados
#  do Banco jvarejao.bd
def database_user_login(username, userPassword):
    connect = sql.connect("jvarejao.db")
    cursor = connect.cursor()

    try:
        cursor.execute(
            """
            SELECT password
            FROM tb_users
            WHERE username = ?
            """, 
            (username,)
        )
    except:
        print("Erro!")

    result = cursor.fetchone()

    if(result):
        hashed_password = result[0]

        if(bcrypt.checkpw(userPassword.encode('utf-8'), hashed_password.encode('utf-8'))):
            utilU.wait_print("Login realizado com sucesso!!")
            connect.close()
            return True

    utilU.wait_print("Falha de autenticação, tente novamente!")
    connect.close()
    return False

# Função para recuperar o ID de um
#  usuário a partir de seu userName
#  isso é utilizado no login para
#  definir globalmente o usuário
#  conectado atualmente
def get_userId(username):
    connect = sql.connect("jvarejao.db")
    cursor = connect.cursor()

    cursor.execute("""
    SELECT id_user
    FROM tb_users
    WHERE username = ?
    """, (username,))

    result = cursor.fetchone()

    if result:
        return result[0]
    return None

# Função para recuperar os dados de 
#  um usuário a partir do seu ID
def get_user(userId):
    connect = sql.connect("jvarejao.db")
    cursor = connect.cursor()

    cursor.execute("""
    SELECT *
    FROM tb_users
    WHERE id_user = ?
    """, (userId,))

    result = cursor.fetchone()

    if result:
        return result
    return None

# Função para deletar um usuário selecionado
#  nesse caso, sempre será o usuário logado
def delete_user(user):
    connect = sql.connect("jvarejao.db")
    cursor = connect.cursor()

    userId = user[0]
    userStoreList = storeM.get_storeList(userId)

    try:
        if userStoreList:
            for store in userStoreList:
                storage = prodM.get_productList(store[0])
                sales = saleM.get_saleList(store)
                if storage:
                    cursor.execute("""
                    DELETE FROM tb_products
                    WHERE id_store = ?
                    """, (store[0],))

                if sales:
                    cursor.execute("""
                    DELETE FROM tb_sales
                    WHERE id_store = ?
                    """, (store[0],))
                    
            cursor.execute("""
            DELETE FROM tb_stores
            WHERE id_user = ?
            """, (userId,))
        
        cursor.execute("""
        DELETE FROM tb_users
        WHERE id_user = ?
        """, (userId,))

        connect.commit()
        utilU.wait_print("| Usuário excluido com sucesso")
    except sql.Error as e:
        utilU.wait_print(f"| Erro ao excluir usuário: {e}")
        return
    finally:
        connect.close()

# Função que recupera os dados de todos
#  os usuários, isso é usado na exportação
#  do JSON com todos os dados do programa
def get_allUserDicts():
    connect = sql.connect("jvarejao.db")
    cursor = connect.cursor()

    cursor.execute("""
    SELECT *
    FROM tb_users
    """)

    userList = cursor.fetchall()

    columns = [desc[0] for desc in cursor.description]
 
    userDicts = []

    for store in userList:
        userDict = dict(zip(columns, store))
        userDicts.append(userDict)

    return userDicts

