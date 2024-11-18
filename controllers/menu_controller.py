from views.relatorios import RelProds, RelBaixo
from utils.exportador import ExpDados

## 1. CRIA O MENU DO VAREJÃO DO SEU JÃO ##
def Menuzar():
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
        RelProds(Produtos)
    if x == 3:
        for prod in Produtos:
            if prod.quantidade <= 5:
                prodBaixo.append(prod)
        RelBaixo(prodBaixo)
    if x == 4:
        ExpDados(Produtos)

    return cod