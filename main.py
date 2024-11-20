import controllers.packages_controller as pacC
import os
from controllers import menu_controller as menuC
from models import users as userM, database as dbM, produto as prodM
from utils import utillities as utilU

connectedUser = ''

# Função main que executa o programa...
#  é isso, acho que não tenho mais o que dizer
# Ah, if __name__ verifica se o programa esta
#  sendo executado do arquivo main.py, caso não
#  o programa não abre
def main():
    dbM.database_create()

    produto = prodM.criar_produto_namedtuple()
    Produtos = []
    loginFail = 0
    cod = 1
    
    while True:
        os.system('cls')

        x = menuC.FirstMenu()
        if x==1:
            while True:
                succededLogin = menuC.LoginMenu(loginFail)
                if(succededLogin):
                    loginFail = 0
                    while True:
                        x = menuC.StoreMenu()
                        if x==1:
                            menuC.StoreListMenu()
                        elif x==2:
                            menuC.storeRegisterMenu()
                        else:
                            break

                        # x = menuC.MainMenu()
                        # if x == 0:
                        #     connectedUser = ''
                        #     break
                        # elif x in [1, 2, 3, 4]:
                        #     cod = CMenu.Opcionar(x, Produtos, cod, produto)
                        # else:
                        #     UUtil.wait_print("Valor inserido não é uma opção")
                        #     continue
                else:
                    loginFail += 1
                if (loginFail == 3):
                    utilU.wait_print("Muitas tentativas falhas, fechando o programa...")
                    os.system("cls")
                    return 0
        elif x==2:
            menuC.RegisterMenu()
        elif x==0:
            break

    input("\n[ENTER P CONTINUAR...]")
    os.system("cls")
    
if __name__ == "__main__":
    pacC.install_packages()
    main()