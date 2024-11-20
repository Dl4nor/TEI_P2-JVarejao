from models.database import bcrypt, sql, utilU, collections
from models.users import get_userId

def database_store_register(username, storeName, storeCNPJ):
    connect = sql.connect("jvarejao.db")
    cursor = connect.cursor()

    idUser = get_userId(username)

    try:
        cursor.execute(
            """
            INSERT INTO tb_stores (id_user, storename, storeCNPJ) 
            VALUES (?, ?, ?)
            """, 
            (idUser, storeName, storeCNPJ)
        )
        connect.commit()
        utilU.wait_print("| Loja cadastrada com sucesso!!")
    except sql.IntegrityError:
        utilU.wait_print("| ERRO: Loja já cadastrada")
    finally:
        connect.close

def get_storeList(userID):
    connect = sql.connect("jvarejao.db")
    cursor = connect.cursor()

    cursor.execute("""
    SELECT *
    FROM tb_stores
    WHERE id_user = ?
    """, (userID,))

    storeList = cursor.fetchall()

    return storeList
    