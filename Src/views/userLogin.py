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
        "| [3] Sobre                |\n"
        "|--------------------------|\n"
        "| [0] SAIR                 |\n"
        "|--------------------------|"
    )