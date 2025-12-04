from datetime import datetime

class Cliente:
    def __init__(self, nome, telefone=None, email=None, endereco=None, id=None):
        self.id = id
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco
        self.data_cadastro = datetime.now().date()
        self.veiculos = []
    
    def to_dict(self):
        """Converte objeto para dicionário"""
        return {
            'id': self.id,
            'nome': self.nome,
            'telefone': self.telefone,
            'email': self.email,
            'endereco': self.endereco,
            'data_cadastro': str(self.data_cadastro)
        }
    
    @classmethod
    def from_dict(cls, data):
        """Cria objeto a partir de dicionário"""
        cliente = cls(
            nome=data['nome'],
            telefone=data.get('telefone'),
            email=data.get('email'),
            endereco=data.get('endereco'),
            id=data.get('id')
        )
        if 'data_cadastro' in data:
            cliente.data_cadastro = data['data_cadastro']
        return cliente