class Veiculo:
    def __init__(self, placa, marca, modelo, ano=None, cor=None, 
                 cliente_id=None, observacoes=None, id=None):
        self.id = id
        self.placa = placa.upper()
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.cliente_id = cliente_id
        self.observacoes = observacoes
        self.historico_servicos = []
    
    def to_dict(self):
        return {
            'id': self.id,
            'placa': self.placa,
            'marca': self.marca,
            'modelo': self.modelo,
            'ano': self.ano,
            'cor': self.cor,
            'cliente_id': self.cliente_id,
            'observacoes': self.observacoes
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            placa=data['placa'],
            marca=data['marca'],
            modelo=data['modelo'],
            ano=data.get('ano'),
            cor=data.get('cor'),
            cliente_id=data.get('cliente_id'),
            observacoes=data.get('observacoes'),
            id=data.get('id')
        )