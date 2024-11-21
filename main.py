import controllers.packages_controller as pacC
import controllers.main_controller as mainC
import os

connectedUserID = ''
connectedStoreID = ''

# Função main que executa o programa...
#  é isso, acho que não tenho mais o que dizer
# Ah, if __name__ verifica se o programa esta
#  sendo executado do arquivo main.py, caso não
#  o programa não abre
def main():
    mainC.execution_flow()

if __name__ == "__main__":
    os.system("cls")
    pacC.install_packages()
    main()