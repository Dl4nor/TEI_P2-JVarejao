import utils.utillities as utilU
import os

# Header do StoreMenu(), primeiro menu
#  com o usuário logado
def storeMenu_header():
    print(
        "|--------------------------|\n"
        "|  BEM VINDO AO J-VAREJÃO  |\n"
        "|    Escolha uma opção     |\n"
        "|--------------------------|\n"
        "| [1] Entrar em uma loja   |\n"
        "| [2] Criar uma loja       |\n"
        "| [3] Excluir loja         |\n"
        "| [4] Excluir sua conta    |\n"
        "|--------------------------|\n"
        "| [5] Exportar dados       |\n"
        "|--------------------------|\n"
        "| [0] Sair                 |\n"
        "|--------------------------|"
    )

# Header do StoreListMenu(), menu onde
#  o usuário seleciona uma loja para entrar
#  ou para excluir
def storeListMenu_header(storeList):

    selected = 0

    while True:
        os.system("cls")
        print(
            "|--------------------------|\n"
            "|    SELECIONE UMA LOJA    |\n"
            "|--------------------------|"
        )
        for index, store in enumerate(storeList):
            if index == selected:
                print(
                f"| >> [{index}] {store[2]}\n"
                f"|        {store[3]}\n"
                "| "  
                )
            else:
                print(
                f"|    [{index}] {store[2]}\n"
                f"|        {store[3]}\n"
                "| "  
                )

        new_selected = utilU.listMenuSelect(selected, len(storeList))

        if new_selected is None:
            return storeList[selected]
        elif new_selected == 'a':
            return None
        else:
            selected = new_selected

# header do storeRegisterMenu(), menu de
#  cadastro de lojas
def storeRegisterMenu_header():
    print(
        "|--------------------------|\n"
        "|    REGISTRE UMA LOJA     |\n"
        "|--------------------------|"
    )

# header do storeControlMenu(), menu de controle
#  de loja (já dentro de uma loja)
def storeControlMenu_header(selectedStore):
   print(
        "|------------------------------------|\n"
       f"| {selectedStore[2]}\n"
       f"| {selectedStore[3]}\n"
        "|------------------------------------|\n"
        "| [1] Cadastrar Produtos             |\n"
        "| [2] Relatório de produtos          |\n"
        "| [3] Relatório de Estoque Baixo     |\n"
        "| [4] Excluir produtos               |\n"
        "|------------------------------------|\n"
        "| [5] Efetuar Venda                  |\n"
        "|------------------------------------|\n"
        "| [0] Sair                           |\n"
        "|------------------------------------|"
    )