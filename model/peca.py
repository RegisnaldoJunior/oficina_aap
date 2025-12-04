class Peca:
    def __init__(self, nome, codigo=None, quantidade=0, valor_unitario=0.0,
                 fornecedor=None, localizacao=None, id=None):
        self.id = id
        self.nome = nome
        self.codigo = codigo
        self.quantidade = quantidade
        self.valor_unitario = valor_unitario
        self.fornecedor = fornecedor
        self.localizacao = localizacao
    
    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'codigo': self.codigo,
            'quantidade': self.quantidade,
            'valor_unitario': self.valor_unitario,
            'fornecedor': self.fornecedor,
            'localizacao': self.localizacao
        }