import main
import utils.utillities as utilU
import sqlite3 as sql

# Função de cadastro de produtos no banco
def database_product_register(storeId, barcode, productName, productBuyVal, productSellVal, productQnt):
    connect = sql.connect("jvarejao.db")
    cursor = connect.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO tb_products (id_store, barcode, productname, productbuyprice, productsellprice, productqnt) 
            VALUES (?, ?, ?, ?, ?, ?)
            """, 
            (storeId, barcode, productName, productBuyVal, productSellVal, productQnt)
        )
        connect.commit()
        utilU.wait_print("| Produto cadastrado com sucesso!!\n")
    except sql.IntegrityError:
        utilU.wait_print("| ERRO: produto já cadastrado!!")
    finally:
        connect.close

# função para recuperar a lista de produtos da loja
#  atualmente conectada
def get_productList():
    connect = sql.connect("jvarejao.db")
    cursor = connect.cursor()

    storeid = main.connectedStoreID

    cursor.execute("""
    SELECT *
    FROM tb_products
    WHERE id_store = ?
    """, (storeid,))

    productList = cursor.fetchall()

    if not productList:
        utilU.wait_print("| Nenhum produto encontrada :(")
        return None

    return productList

# Função para recuperar produtos que estão quase
#  acabando em estoque (quantidade < 5)
def get_lowProductList():
    connect = sql.connect("jvarejao.db")
    cursor = connect.cursor()

    storeid = main.connectedStoreID

    cursor.execute("""
    SELECT *
    FROM tb_products
    WHERE id_store = ? AND productqnt < 5
    """, (storeid,))

    productList = cursor.fetchall()

    if not productList:
        utilU.wait_print("| Nenhum produto encontrada :(")
        return None

    return productList

# Função para recuperar todos os produtos
#  cadastrados no banco, o resultado dessa
#  função é utilizado na exportação do JSON
def get_allProductDicts():
    connect = sql.connect("jvarejao.db")
    cursor = connect.cursor()

    cursor.execute("""
    SELECT *
    FROM tb_products
    """)

    productList = cursor.fetchall()

    columns = [desc[0] for desc in cursor.description]
    
    productDicts = []

    for product in productList:
        productDict = dict(zip(columns, product))
        productDicts.append(productDict)

    return productDicts

# Função para deletar o produto selecionado
#  do banco
def delete_product(product):
    connect = sql.connect("jvarejao.db")
    cursor = connect.cursor()

    productId = product[0]
    productName = product[2]

    try:
        cursor.execute("""
        DELETE FROM tb_products
        WHERE id_product = ?
        """, (productId,))

        connect.commit()
        utilU.wait_print(f"| Produto {productName} deletado!")
    except sql.Error as e:
        utilU.wait_print(f"| Erro ao deletar produto: {e}")
    finally:
        connect.close()

def sell_product(product, sellqnt):
    connect = sql.connect("jvarejao.db")
    cursor = connect.cursor()

    productId = product[0]
    productName = product[2]
    productQnt = product[6]
    productNewQnt = productQnt-sellqnt

    try:
        cursor.execute("""
        UPDATE tb_products
        SET productqnt = ?
        WHERE id_product = ?
        """, (productNewQnt, productId,))

        connect.commit()
        utilU.wait_print(f"| Produto {productName} vendido!")
    except sql.Error as e:
        utilU.wait_print(f"| Erro ao vender produto: {e}")
    finally:
        connect.close()


