import models.sales as saleM
import utils.utillities as utilU
import os

# Tela que representa o Caixa da loja
#  Registra o total vendido e lucro de
#  cada loja
def salesMenu_header():
    SaleValProftValList = saleM.get_moneyInfo()
    
    os.system("cls")
    
    if SaleValProftValList[0] and SaleValProftValList[1]:
        totalSaleVal = SaleValProftValList[0]
        totalProfit = SaleValProftValList[1]
    else:
        totalProfit = 0
        totalSaleVal = 0

    utilU.wait_print(
        "|------------------------------|\n"
        "|             CAIXA            |\n"
        "|------------------------------|\n"
       f"| Faturamento: R$ {totalSaleVal:.2f}\n"
        "|                              |\n"
       f"| Lucro total: R$ {totalProfit:.2f}\n"
        "|------------------------------|"
    )