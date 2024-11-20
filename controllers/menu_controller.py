
import os
import bcrypt
import keyboard
import main
from models import database as dbM, produto as prodM, users as userM, stores as storeM
from views import relatorios as relV, userLogin as ulV
from utils import utillities as utilU

# Tudo começa de algum lugar... Nesse caso, é daqui
def FirstMenu():
    os.system("cls")
    
    ulV.firstMenu_header()
    try:
        x = int(input("| "))
        return x
        
    except ValueError:
        utilU.wait_print("Opção inválida :(")
        return None

# Menu de registro de conta:
# O usuário insere username e senha,
#  passamos esses dados apara database_user_register()
#  para registrar ele no banco de dados
def RegisterMenu():
    os.system("cls")

    ulV.register_header()
    username = input(
        "| Crie um username:\n"
        "| "
    )
    password = input(
        "| Crie uma senha:\n"
        "| "
    )
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    userM.database_user_register(username, hashed_password.decode('utf-8'))

# Menu de Login:
# O usuário insere o username e a senha,
#  jogamos esse username e a senha criptografada
#  para a função que fará a validação de login
def LoginMenu(qntLoginFail):
    os.system("cls")

    ulV.login_header(qntLoginFail)
    username = input(
        "| Seu username:\n"
        "| "
    )
    password = input(
        "| Sua senha:\n"
        "| "
    )
    succeededLogin = userM.database_user_login(username, password)

    if(succeededLogin):
        main.connectedUser = username
        return True
    else: 
        return False

# Menu de loja:
# Usuário escolhe entre criar uma nova loja
#  ou entrar em uma loja já existente
def StoreMenu():
    os.system("cls")

    ulV.storeMenu_header()
    x = int(input("| "))

    return x

def StoreListMenu():
    os.system("cls")

    userId = userM.get_userId(main.connectedUser)
    storeList = storeM.get_storeList(userId)

    store = ulV.storeListMenu_header(storeList)

    print(f"Voce selecionou a loja: {store}")

def storeRegisterMenu():

    ulV.storeRegisterMenu_header()
    storeName = input(
        "| Insira o nome da loja:\n"
        "| "  
    )
    storeCNPJ = input(
        "| Insira o CNPJ da loja:\n"
        "| "
    )

    # userM.database_user_register(username, hashed_password.decode('utf-8'))
    storeM.database_store_register(main.connectedUser, storeName, storeCNPJ)

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
        relV.RelProds(Produtos)
    if x == 3:
        for prod in Produtos:
            if prod.quantidade <= 5:
                prodBaixo.append(prod)
        relV.RelBaixo(prodBaixo)
    if x == 4:
        utilU.ExpDados(Produtos)

    return cod

def listMenuSelect(selected, listLength):
    key = keyboard.read_event()

    if key.name == "up" and key.event_type == "down":
        return (selected - 1) % listLength
    elif key.name == "down" and key.event_type == "down":
        return (selected + 1) % listLength
    elif key.name == "enter" and key.event_type == "down":
        return None
    else:
        return selected