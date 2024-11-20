from models.database import bcrypt, sql, UUtil, collections

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

    try:
        cursor.execute(
            """
            SELECT password
            FROM tb_users
            WHERE username = ?
            """, 
            (username)
        )
    except:
        print("Erro!")
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