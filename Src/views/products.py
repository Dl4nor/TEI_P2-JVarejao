import controllers.menu_controller as menuC
import utils.utillities as utilU
import os

# Header do menu RegisterProduct()
def registerProduct_header():
    print(
        "|--------------------------|\n"
        "|   REGISTRE UM PRODUTO    |\n"
        "|--------------------------|"
    )

## 3. MONTA E EXIBE O RELATÓRIO DOS productList ##
def RelProds(productList):
    os.system("cls")

    if not productList:
        return None

    maxCod = max(len(prod[2]) for prod in productList)
    maxNome = max(len(prod[3]) for prod in productList)
    maxValComp = max(len(f"{prod[4]:.2f}") for prod in productList)
    maxValVend = max(len(f"{prod[5]:.2f}") for prod in productList)
    maxQnt = max(len(str(prod[6])) for prod in productList)

    maxCod = max(maxCod, len("Código"))
    maxNome = max(maxNome, len("Nome"))
    maxValComp = max(maxValComp, len("Valor Compra"))
    maxValVend = max(maxValVend, len("Valor Venda"))
    maxQnt = max(maxQnt, len("Quantidade"))

    print(
        f"{'Código'.center(maxCod)} | "
        f"{'Nome'.center(maxNome)} | "
        f"{'Valor Compra'.center(maxValComp)} | " 
        f"{'Valor Venda'.center(maxValVend)} | " 
        f"{'Quantidade'.center(maxQnt)}"
    )
    print(
        "-" * (maxCod + maxNome + maxValComp + maxValVend + maxQnt + 12)
    )

    for prod in productList:
        print(f"{prod[2]}".ljust(maxCod), "|", 
              f"{prod[3]}".ljust(maxNome), "|", 
              f"{prod[4]:.2f}".ljust(maxValComp), "|", 
              f"{prod[5]:.2f}".ljust(maxValVend), "|", 
              f"{prod[6]}".ljust(maxQnt))
        
    utilU.wait_print("")

# Mostra o relatório dos produtos sendo um menu
#  selecionável, para que o usuário escolha um
#  produto para deletar da loja
def RelSelectProduct(productList):

    selected = 0

    while True:
        os.system("cls")

        if not productList:
            return None

        maxCod = max(len(prod[2]) for prod in productList)
        maxNome = max(len(prod[3]) for prod in productList)
        maxValComp = max(len(f"{prod[4]:.2f}") for prod in productList)
        maxValVend = max(len(f"{prod[5]:.2f}") for prod in productList)
        maxQnt = max(len(str(prod[6])) for prod in productList)

        maxCod = max(maxCod, len("Código"))
        maxNome = max(maxNome, len("Nome"))
        maxValComp = max(maxValComp, len("Valor Compra"))
        maxValVend = max(maxValVend, len("Valor Venda"))
        maxQnt = max(maxQnt, len("Quantidade"))

        print(
            "   "
            f"{'Código'.center(maxCod)} | "
            f"{'Nome'.center(maxNome)} | "
            f"{'Valor Compra'.center(maxValComp)} | " 
            f"{'Valor Venda'.center(maxValVend)} | " 
            f"{'Quantidade'.center(maxQnt)}"
        )
        print(
            "  ",
            "-" * (maxCod + maxNome + maxValComp + maxValVend + maxQnt + 12)
        )

        for index, prod in enumerate(productList):
            if(index==selected):
                print( " > "
                    f"{prod[2]}".ljust(maxCod+3), "|", 
                    f"{prod[3]}".ljust(maxNome), "|", 
                    f"{prod[4]:.2f}".ljust(maxValComp), "|", 
                    f"{prod[5]:.2f}".ljust(maxValVend), "|", 
                    f"{prod[6]}".ljust(maxQnt))
            else:
                print( "   "
                    f"{prod[2]}".ljust(maxCod+3), "|", 
                    f"{prod[3]}".ljust(maxNome), "|", 
                    f"{prod[4]:.2f}".ljust(maxValComp), "|", 
                    f"{prod[5]:.2f}".ljust(maxValVend), "|", 
                    f"{prod[6]}".ljust(maxQnt))
                
        new_selected = menuC.listMenuSelect(selected, len(productList))

        if new_selected is None:
            return productList[selected]
        elif new_selected == 'a':
            return None
        else:
            selected = new_selected

# Header da função sell_qnt()
#  onde é realizada a venda de
#  produtos cadastrados
def sellProductQnt_header():
    os.system("cls")
    print(
        "|-------------------------|\n"
        "|          VENDAS         |\n"
        "|-------------------------|\n"
        "|"
    )
