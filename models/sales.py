import main
import utils.utillities as utilU
import sqlite3 as sql

def insert_sale(product, sellQnt):
    connect = sql.connect("jvarejao.db")
    cursor = connect.cursor()

    storeId = main.connectedStoreID
    productId = product[0]
    quantitySold = sellQnt
    saleValue = product[5]*sellQnt
    profit = saleValue-product[4]*sellQnt

    try:
        cursor.execute("""
        INSERT INTO tb_sales (id_store, id_product, quantity_sold, totalsale_value, profit)
        values (?, ?, ?, ?, ?)
        """, (storeId, productId, quantitySold, saleValue, profit))

        connect.commit()
        utilU.wait_print("| Venda registada com sucesso")
    except sql.IntegrityError:
        utilU.wait_print("| Erro ao registrar venda!")
        return None
    finally:
        cursor.close()

def get_moneyInfo():
    connect = sql.connect("jvarejao.db")
    cursor = connect.cursor()

    storeId = main.connectedStoreID

    cursor.execute("""
    SELECT totalsale_value, profit
    FROM tb_sales
    WHERE id_store = ?
    """, (storeId,))

    saleList = cursor.fetchall()

    if not saleList:
        utilU.wait_print("| Nenhuma venda encontrada :(")
        return None
    
    return saleList
    
def get_allSales():
    connect = sql.connect("jvarejao.db")
    cursor = connect.cursor()

    storeId = main.connectedStoreID

    cursor.execute("""
    SELECT *
    FROM tb_sales
    """)

    salesList = cursor.fetchall()

    columns = [desc[0] for desc in cursor.description]
    
    saleDicts = []

    for sale in salesList:
        saleDict = dict(zip(columns, sale))
        saleDicts.append(saleDict)

    return saleDicts