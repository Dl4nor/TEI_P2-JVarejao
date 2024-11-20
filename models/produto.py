from models.database import bcrypt, sql, utilU, collections

# Antiga função utilizada para criar o Map
#  dos produtos (vai ser substituída por uma
#  que utiliza SQLite)
def criar_produto_namedtuple():
    """Cria o namedtuple para o modelo Produto."""
    return collections.namedtuple("Produtos", "codigo nome preco_compra preco_venda quantidade")
