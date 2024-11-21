
import os
import bcrypt
import main
from models import users as userM, stores as storeM
from views import userLogin as ulV, stores as storeV
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
    userID = userM.get_userId(username)

    if(succeededLogin):
        main.connectedUserID = userID
        return True
    else: 
        return False

# Menu de loja:
# Usuário escolhe entre criar uma nova loja
#  ou entrar em uma loja já existente
def StoreMenu():
    os.system("cls")

    storeV.storeMenu_header()
    try:
        x = int(input("| "))
        return x
    except ValueError:
        utilU.wait_print("Valor inválido!")
    
# Menu que lista as lojas com opções selecionáveis
#  com >>
def StoreListMenu():
    os.system("cls")

    storeList = storeM.get_storeList(main.connectedUserID)

    if not storeList:
        return None
    
    selected_store = storeV.storeListMenu_header(storeList)
    main.connectedStoreID = selected_store[0]

    return selected_store

# Menu de cadastro de lojas
def storeRegisterMenu():
    os.system("cls")
    storeCNPJ = None

    storeV.storeRegisterMenu_header()
    storeName = input(
        "| Insira o nome da loja:\n"
        "| "  
    )
    while storeCNPJ == None:
        storeCNPJ = input(
            "| Insira o CNPJ da loja:\n"
            "| "
        )
        if(len(storeCNPJ) != 14):
         storeCNPJ = None
         utilU.wait_print("Número de CNPJ inválido, tente novamente")

    storeM.database_store_register(main.connectedUserID, storeName, storeCNPJ)

## 1. CRIA O MENU DO VAREJÃO DO SEU JÃO ##
def storeControlMenu(selectedStore):
    os.system("cls")

    storeV.storeControlMenu_header(selectedStore)
    try:
        x = int(input("| "))
        return x
    except ValueError:
        utilU.wait_print(f"| Erro!! - Valor inválido")
        return None
    
