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