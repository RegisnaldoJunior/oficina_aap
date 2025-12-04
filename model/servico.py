class Servico:
    CATEGORIAS = [
        'Preventiva', 'Corretiva', 'Pintura', 
        'Elétrica', 'Mecânica', 'Funilaria', 'Outros'
    ]
    
    def __init__(self, nome, descricao=None, valor_mao_obra=0.0, 
                 tempo_estimado=None, categoria=None, id=None):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.valor_mao_obra = valor_mao_obra
        self.tempo_estimado = tempo_estimado  # em minutos
        self.categoria = categoria if categoria in self.CATEGORIAS else 'Outros'
    
    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'descricao': self.descricao,
            'valor_mao_obra': self.valor_mao_obra,
            'tempo_estimado': self.tempo_estimado,
            'categoria': self.categoria
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            nome=data['nome'],
            descricao=data.get('descricao'),
            valor_mao_obra=data.get('valor_mao_obra', 0.0),
            tempo_estimado=data.get('tempo_estimado'),
            categoria=data.get('categoria'),
            id=data.get('id')
        )