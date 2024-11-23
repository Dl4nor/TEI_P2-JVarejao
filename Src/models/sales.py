import main
import utils.utillities as utilU
import sqlite3 as sql

# Inserir dados na tabela de vendas ao
#  efetuar a venda de algum produto
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

# Recupera os dados monetários totais da tabela de
#  vendas para a loja conectada para demonstrar no CAIXA
def get_moneyInfo():
    connect = sql.connect("jvarejao.db")
    cursor = connect.cursor()

    storeId = main.connectedStoreID

    cursor.execute("""
    SELECT SUM(totalsale_value), SUM(profit)
    FROM tb_sales
    WHERE id_store = ?
    """, (storeId,))

    saleData = cursor.fetchone()

    if not saleData:
        utilU.wait_print("| Nenhuma venda encontrada :(")
        return None
    
    return saleData

# Recupera todos os dados de vendas para exportar
#  para JSON
def get_allSales():
    connect = sql.connect("jvarejao.db")
    cursor = connect.cursor()

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

# Recurepa a lista de vendas de uma loja
#  específica
def get_saleList(store):
    connect = sql.connect("jvarejao.db")
    cursor = connect.cursor()

    storeName = store[2]

    cursor.execute("""
    SELECT *
    FROM tb_sales
    WHERE id_store = ?
    """, (store[0],))

    storeList = cursor.fetchall()

    if not storeList:
        utilU.wait_print(f"| Nenhuma venda registrada em {storeName} :(")
        return None

    return storeList