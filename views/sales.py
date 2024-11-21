import models.sales as saleM
import utils.utillities as utilU
import os

def salesMenu_header():
    SaleValProftValList = saleM.get_moneyInfo()
    
    os.system("cls")
    
    totalSaleVal = 0
    totalProfit = 0

    if SaleValProftValList != None:
        for saleValProfVal in SaleValProftValList:
            totalSaleVal += saleValProfVal[0]
            totalProfit  += saleValProfVal[1] 
    utilU.wait_print(
        "|------------------------------|\n"
        "|             CAIXA            |\n"
        "|------------------------------|\n"
       f"| Faturamento: {totalSaleVal}\n"
        "|                              |\n"
       f"| Lucro total: {totalProfit}\n"
        "|------------------------------|"
    )