import collections

def criar_produto_namedtuple():
    """Cria o namedtuple para o modelo Produto."""
    return collections.namedtuple("Produtos", "codigo nome preco_compra preco_venda quantidade")
