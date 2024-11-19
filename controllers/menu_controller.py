import views.relatorios as VRel
import os
import models.produto as MProd
import utils.utillities as UUtil
import bcrypt

# Tudo começa de algum lugar... Nesse caso, é daqui
def FirstMenu():
    os.system("cls")
    
    try:
        x = int(input(
            "|--------------------------|\n"
            "|  BEM VINDO AO J-VAREJÃO  |\n"
            "|    Escolha uma opção     |\n"
            "|--------------------------|\n"
            "| [1] Login                |\n"
            "| [2] Cadastrar            |\n"
            "|--------------------------|\n"
            "| [0] SAIR                 |\n"
            "|--------------------------|\n\n"
        ))
        return x
        
            
    except ValueError:
        UUtil.wait_print("Opção inválida :(")
        return None

# Menu de registro de conta:
# O usuário insere username e senha,
#  passamos esses dados apara database_user_register()
#  para registrar ele no banco de dados
def RegisterMenu():
    os.system("cls")

    username = input(
        "|--------------------------|\n"
        "|  BEM VINDO AO J-VAREJÃO  |\n"
        "|--------------------------|\n"
        "| Crie um username:\n"
        "| "
    )
    password = input(
        "| Crie uma senha:\n"
        "| "
    )
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    MProd.database_user_register(username, hashed_password.decode('utf-8'))

# Menu de Login:
# O usuário insere o username e a senha,
#  jogamos esse username e a senha criptografada
#  para a função que fará a validação de login
def LoginMenu(qntLoginFail):

    os.system("cls")

    username = input(
        "|--------------------------|\n"
        "|      TELA DE LOGIN       |\n"
        f"|       TENTATIVA: {qntLoginFail}       |\n"
        "|--------------------------|\n"
        "| Seu username:\n"
        "| "
    )
    password = input(
        "| Sua senha:\n"
        "| "
    )

    succeededLogin = MProd.database_user_login(username, password)

    if(succeededLogin):
        UUtil.wait_print("Usuário encontrado e logado com sucesso!!!")
        return True
    else: 
        return False


## 1. CRIA O MENU DO VAREJÃO DO SEU JÃO ##
def MainMenu():
    try:
        x = int(input(
            "Varejão do João\n"
            "[1] Cadastrar Produtos\n"
            "[2] Relatório de produtos\n"
            "[3] Relatório de Estoque Baixo\n"
            "[4] Exportar dados\n"
            "[0] Sair\n\n"
        ))
        return x
    except ValueError as ve:
        print(f"Erro!! - Valor inválido - {ve}")
        input("[ENTER]")
        return None

def Opcionar(x, Produtos, cod, produto):
    from controllers.produto_controller import CadProduto

    prodBaixo = []

    if x == 1:
        aux = CadProduto(cod, produto)
        if aux != None:
            Produtos.append(aux)
            cod = cod + 1
    if x == 2:
        VRel.RelProds(Produtos)
    if x == 3:
        for prod in Produtos:
            if prod.quantidade <= 5:
                prodBaixo.append(prod)
        VRel.RelBaixo(prodBaixo)
    if x == 4:
        UUtil.ExpDados(Produtos)

    return cod