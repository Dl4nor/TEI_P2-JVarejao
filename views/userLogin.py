import controllers.menu_controller as menuC
import os

# header usado no LoginMenu() - controller
def login_header(qntLoginFail):
    print(
        "|--------------------------|\n"
        "|      TELA DE LOGIN       |\n"
        f"|       TENTATIVA: {qntLoginFail}       |\n"
        "|--------------------------|"
    )

# header usado no RegisterMenu() - controller
def register_header():
    print(
        "|--------------------------|\n"
        "|  BEM VINDO AO J-VAREJÃO  |\n"
        "|--------------------------|"
    )

# header usado no FirstMenu() - controller
def firstMenu_header():
    print(
        "|--------------------------|\n"
        "|  BEM VINDO AO J-VAREJÃO  |\n"
        "|    Escolha uma opção     |\n"
        "|--------------------------|\n"
        "| [1] Login                |\n"
        "| [2] Cadastrar            |\n"
        "|--------------------------|\n"
        "| [0] SAIR                 |\n"
        "|--------------------------|"
    )


def storeMenu_header():
    print(
        "|--------------------------|\n"
        "|  BEM VINDO AO J-VAREJÃO  |\n"
        "|    Escolha uma opção     |\n"
        "|--------------------------|\n"
        "| [1] Entrar em uma loja   |\n"
        "| [2] Criar uma loja       |\n"
        "|--------------------------|\n"
        "| [0] Sair                 |\n"
        "|--------------------------|"
    )

def storeListMenu_header(storeList):
    print(
        "|--------------------------|\n"
        "|    SELECIONE UMA LOJA    |\n"
        "|--------------------------|"
    )

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

        new_selected = menuC.listMenuSelect(selected, len(storeList))

        if new_selected is None:
            return storeList[selected]
        else:
            selected = new_selected

    
    
def storeRegisterMenu_header():
    print(
        "|--------------------------|\n"
        "|    REGISTRE UMA LOJA     |\n"
        "|--------------------------|"
    )