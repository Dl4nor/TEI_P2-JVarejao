import os
from controllers.menu_controller import Menuzar, Opcionar
from models.produto import criar_produto_namedtuple

def main():
    produto = criar_produto_namedtuple()
    Produtos = []
    cod = 1

    while True:
        os.system('cls')

        x = Menuzar()
        if x == 0:
            break
        elif x in [1, 2, 3, 4]:
            cod = Opcionar(x, Produtos, cod, produto)
        else:
            print("\nValor inserido não é uma opção")
            input("[ENTER]")
            continue

        input("\n[ENTER P/ CONTINUAR...]")
    
if __name__ == "__main__":
    main()