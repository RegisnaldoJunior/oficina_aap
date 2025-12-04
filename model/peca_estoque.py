class PecaEstoque:
    def __init__(self, codigo, nome, descricao=None, quantidade=0, 
                 quantidade_minima=5, valor_compra=0.0, valor_venda=0.0,
                 fornecedor=None, localizacao=None, id=None):
        self.id = id
        self.codigo = codigo
        self.nome = nome
        self.descricao = descricao
        self.quantidade = quantidade
        self.quantidade_minima = quantidade_minima
        self.valor_compra = valor_compra
        self.valor_venda = valor_venda
        self.fornecedor = fornecedor
        self.localizacao = localizacao
    
    def to_dict(self):
        return {
            'id': self.id,
            'codigo': self.codigo,
            'nome': self.nome,
            'descricao': self.descricao,
            'quantidade': self.quantidade,
            'quantidade_minima': self.quantidade_minima,
            'valor_compra': self.valor_compra,
            'valor_venda': self.valor_venda,
            'fornecedor': self.fornecedor,
            'localizacao': self.localizacao
        }
    
    def precisa_repor(self):
        return self.quantidade <= self.quantidade_minima