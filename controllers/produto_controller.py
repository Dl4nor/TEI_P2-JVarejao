
# Antigo menu de cadastro de produtos
#  que não utiliza Banco de Dados ainda
def CadProduto(cod, produto):
    nome = input("Qual o nome do produto?\n")

    try:
        valComp = float(input("Qual o valor de compra do produto?\n"))
    except ValueError as ve:
        print(f"Erro!!! - Valor inserido não é compatível - {ve}")
        return

    try:
        qnt = int(input("Qual a quantidade em estoque?\n"))
    except ValueError as ve:
        print(f"Erro!!! - Valor inserido não é compatível - {ve}")
        return

    valVend = valComp + (valComp * 0.25)

    return produto(cod, nome, valComp, valVend, qnt)