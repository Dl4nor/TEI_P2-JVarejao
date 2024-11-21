import utils.utillities as utilU
import sqlite3 as sql

# Cadastro de loja no banco de dados
def database_store_register(userID, storeName, storeCNPJ):
    connect = sql.connect("jvarejao.db")
    cursor = connect.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO tb_stores (id_user, storename, storeCNPJ) 
            VALUES (?, ?, ?)
            """, 
            (userID, storeName, storeCNPJ)
        )
        connect.commit()
        utilU.wait_print("| Loja cadastrada com sucesso!!")
    except sql.IntegrityError:
        utilU.wait_print("| ERRO: Loja já cadastrada")
    finally:
        connect.close()

# Pega a lista de lojas de um usuário
def get_storeList(userID):
    connect = sql.connect("jvarejao.db")
    cursor = connect.cursor()

    cursor.execute("""
    SELECT *
    FROM tb_stores
    WHERE id_user = ?
    """, (userID,))

    storeList = cursor.fetchall()

    if not storeList:
        utilU.wait_print("| Nenhuma loja encontrada :(")
        return None

    return storeList

# Deleta a loja e os produtos dentro dela
def delete_store(store):
    connect = sql.connect("jvarejao.db")
    cursor = connect.cursor()

    storeId = store[0]
    storename = store[2]

    try:
        cursor.execute("""
        DELETE FROM tb_products
        WHERE id_store = ?
        """, (storeId,))

        cursor.execute("""
        DELETE FROM tb_stores
        WHERE id_store = ?
        """, (storeId,))

        connect.commit()
        utilU.wait_print(f"| Loja {storename} deletada!")
    except sql.Error as e:
        utilU.wait_print(f"| Erro ao deletar loja: {e}")
    finally:
        connect.close()

# Pega a lista de todas as lojas do app
#  Usado para a exportação em JSON
def get_allStoreDicts():
    connect = sql.connect("jvarejao.db")
    cursor = connect.cursor()

    cursor.execute("""
    SELECT *
    FROM tb_stores
    """)

    storeList = cursor.fetchall()

    columns = [desc[0] for desc in cursor.description]
    
    storeDicts = []

    for store in storeList:
        storeDict = dict(zip(columns, store))
        storeDicts.append(storeDict)

    return storeDicts



    