## 3. MONTA E EXIBE O RELATÓRIO DOS PRODUTOS ##
def RelProds(Produtos):
    if not Produtos:
        print("Nenhum produto cadastrado...")
        return

    maxCod = max(len(str(prod.codigo)) for prod in Produtos)
    maxNome = max(len(prod.nome) for prod in Produtos)
    maxValComp = max(len(f"{prod.preco_compra:.2f}") for prod in Produtos)
    maxValVend = max(len(f"{prod.preco_venda:.2f}") for prod in Produtos)
    maxQnt = max(len(str(prod.quantidade)) for prod in Produtos)

    maxCod = max(maxCod, len("Código"))
    maxNome = max(maxNome, len("Nome"))
    maxValComp = max(maxValComp, len("Valor Compra"))
    maxValVend = max(maxValVend, len("Valor Venda"))
    maxQnt = max(maxQnt, len("Quantidade"))

    print(
        f"{'Código'.center(maxCod)} | "
        f"{'Nome'.center(maxNome)} | "
        f"{'Valor Compra'.center(maxValComp)} | " 
        f"{'Valor Venda'.center(maxValVend)} | " 
        f"{'Quantidade'.center(maxQnt)}"
    )
    print("-" * (maxCod + maxNome + maxValComp + maxValVend + maxQnt + 10))

    for prod in Produtos:
        print(f"{prod.codigo}".ljust(maxCod), "|", 
              f"{prod.nome}".ljust(maxNome), "|", 
              f"{prod.preco_compra:.2f}".ljust(maxValComp), "|", 
              f"{prod.preco_venda:.2f}".ljust(maxValVend), "|", 
              f"{prod.quantidade}".ljust(maxQnt))

## 4. EXIBE O RELATÓRIO DOS PRODUTOS COM MENOS DE 5 EM ESTOQUE ##
def RelBaixo(prodBaixo):
    RelProds(prodBaixo)
