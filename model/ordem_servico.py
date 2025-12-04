from datetime import datetime

class OrdemServico:
    STATUS = ['aberta', 'em_andamento', 'aguardando_pecas', 'concluida', 'cancelada']
    
    def __init__(self, numero, veiculo_id, km_veiculo=None, observacoes=None, 
                 status='aberta', id=None):
        self.id = id
        self.numero = numero
        self.veiculo_id = veiculo_id
        self.data_abertura = datetime.now().date()
        self.data_fechamento = None
        self.km_veiculo = km_veiculo
        self.observacoes = observacoes
        self.status = status
        self.valor_total = 0.0
        self.servicos = []
        self.pecas = []
    
    def calcular_total(self):
        total = sum(s['quantidade'] * s['valor_unitario'] for s in self.servicos)
        total += sum(p['quantidade'] * p['valor_unitario'] for p in self.pecas)
        self.valor_total = total
        return total
    
    def to_dict(self):
        return {
            'id': self.id,
            'numero': self.numero,
            'veiculo_id': self.veiculo_id,
            'data_abertura': str(self.data_abertura),
            'status': self.status,
            'km_veiculo': self.km_veiculo,
            'observacoes': self.observacoes,
            'valor_total': self.valor_total
        }