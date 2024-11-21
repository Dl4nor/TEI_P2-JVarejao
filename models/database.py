import sqlite3 as sql

# Função que cria o banco de dados
#  e as tabelas que utilizamos no programa
#  caso as tabeals já existam, nada acontece
#  e tudo bem
def database_create():
    connect = sql.connect("jvarejao.db")
    cursor = connect.cursor()

    cursor.execute("PRAGMA foreign_keys = ON")

    ## Criar tabela de usuários
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tb_users(
        id_user  INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
    """)

    # Criar tabela de produtos
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tb_stores(
        id_store   INTEGER PRIMARY KEY AUTOINCREMENT,
        id_user    INTEGER NOT NULL,
        storename  TEXT NOT NULL,
        storeCNPJ  CHAR(14) NOT NULL UNIQUE,
        FOREIGN KEY (id_user) REFERENCES tb_users(id_user)
    )
    """)

    # Criar tabela de lojas
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tb_products(
        id_product       INTEGER PRIMARY KEY AUTOINCREMENT,
        id_store         INTEGER NOT NULL,
        barcode          TEXT NOT NULL UNIQUE,
        productname      TEXT NOT NULL,
        productbuyprice  NUMERIC NOT NULL,
        productsellprice NUMERIC NOT NULL,
        productqnt       INTEGER NOT NULL,
        FOREIGN KEY (id_store) REFERENCES tb_stores(id_store)
    )
    """)

    # Criar tabela de vendas
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tb_sales(
        id_sell         INTEGER PRIMARY KEY AUTOINCREMENT,
        id_store        INTEGER NOT NULL,
        id_product      INTEGER NOT NULL,
        quantity_sold   INTEGER NOT NULL,
        totalsale_value NUMERIC NOT NULL,
        profit          NUMERIC NOT NULL,
        FOREIGN KEY (id_store) REFERENCES tb_stores(id_store),
        FOREIGN KEY (id_product) REFERENCES tb_product(id_product)
    )
    """)

    connect.commit()
    connect.close()

    """
        "|------------------------------------|\n"
       f"| {selectedStore[2]}\n"
       f"| {selectedStore[3]}\n"
        "|------------------------------------|\n"
        "| [1] Cadastrar Produtos             |\n"
        "| [2] Efetuar Venda                  |\n"
        "| [3] Visualizar caixa               |\n"
        "| [4] Relatório de produtos          |\n"
        "| [5] Relatório de Estoque Baixo     |\n"
        "|------------------------------------|\n"
        "| [9] Excluir produtos               |\n"
        "|------------------------------------|\n"
        "| [0] Sair                           |\n"
        "|------------------------------------|"
    """