import os
import main
from models import produto as prodM
from views import products as prodV
from utils import utillities as utilU

# Antigo menu de cadastro de produtos
#  que não utiliza Banco de Dados ainda
def CadProduto():
    os.system("cls")

    prodV.registerProduct_header()
    barcode = input(
        "| Qual o código do produto?\n"
        "| "
    )
    prodName = input(
        "|\n"
        "| Qual o nome do produto?\n"
        "| "
    )
    print(
        "|\n"
        "| O valor de Venda será definido \n"
        "|  como 1.25x o valor de compra\n"
        "|"
    )
    try:
        prodBuyVal = float(input(
            "| Qual o valor de compra do produto?\n"
            "| R$ "
        ))
    except ValueError as ve:
        print("| Erro!!! - Valor inserido não é compatível!!")

    try:
        prodQnt = int(input(
            "|\n"
            "| Qual a quantidade em estoque?\n"
            "| "
        ))
    except ValueError as ve:
        print("| Erro!!! - Valor inserido não é compatível")

    prodSellVal = prodBuyVal + (prodBuyVal * 0.25)

    utilU.wait_print(
        "| \n"
       f"| Valor de Venda definido para {prodSellVal}\n"
        "| \n"
        "| Produto cadastrado com sucesso!"
    )

    prodM.database_product_register(main.connectedStoreID, barcode, prodName, prodBuyVal, prodSellVal, prodQnt)