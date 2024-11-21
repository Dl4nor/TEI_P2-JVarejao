import os
import main
from views import products as prodV, sobre as sobreV
from controllers import menu_controller as menuC, produto_controller as prodC
from models import users as userM, database as dbM, produto as prodM, stores as storeM
from utils import utillities as utilU

# Esse é todo o fluxo de execução
#  do código. Talvez dê pra entender
#  como funciona, se bem que nem eu 
#  entendo muito bem
def execution_flow():
    dbM.database_create()

    loginFail = 0
    
    while True:
        os.system('cls')

        firstMenuChoide = menuC.FirstMenu()
        if firstMenuChoide==1:
            while loginFail < 3 and firstMenuChoide == 1:
                succededLogin = menuC.LoginMenu(loginFail)
                if(succededLogin):
                    loginFail = 0
                    while succededLogin:
                        storeMenuChoice = menuC.StoreMenu()
                        if storeMenuChoice==1:
                            selectedStore = menuC.StoreListMenu()
                            while True:
                                storeControlMenuChoice = menuC.storeControlMenu(selectedStore)
                                if storeControlMenuChoice==1:
                                    prodC.CadProduto()
                                elif storeControlMenuChoice==2:
                                    productList = prodM.get_productList()
                                    prodV.RelProds(productList)
                                elif storeControlMenuChoice==3:
                                    lowProductList = prodM.get_lowProductList()
                                    prodV.RelProds(lowProductList)
                                elif storeControlMenuChoice==4:
                                    productList = prodM.get_productList()
                                    productSelected = prodV.RelDeleteProduct(productList)
                                    prodM.delete_product(productSelected)
                                elif storeControlMenuChoice==0:
                                    storeControlMenuChoice = None
                                    storeMenuChoice = None
                                    selectedStore = None
                                    break
                        elif storeMenuChoice==2:
                            menuC.storeRegisterMenu()
                        elif storeMenuChoice==3:
                            selectedStore = menuC.StoreListMenu()
                            storeM.delete_store(selectedStore)
                        elif storeMenuChoice==4:
                            currentUser = userM.get_user(main.connectedUserID)
                            userM.delete_user(currentUser)
                        elif storeMenuChoice==5:
                            stores = storeM.get_allStoreDicts()
                            users = userM.get_allUserDicts()
                            products = prodM.get_allProductDicts()
                            utilU.ExpDados(users, stores, products)
                        elif storeMenuChoice==0:
                            succededLogin = False
                            firstMenuChoide = None
                            storeMenuChoice = None
                else:
                    loginFail += 1

            if (loginFail == 3):
                os.system("cls")
                utilU.wait_print("Muitas tentativas falhas, fechando o programa...")
                os.system("cls")
                return 0
            
        elif firstMenuChoide==2:
            menuC.RegisterMenu()
        elif firstMenuChoide==3:
            sobreV.sobre()
        elif firstMenuChoide==0:
            break

    input("\n[ENTER P CONTINUAR...]")
    os.system("cls")