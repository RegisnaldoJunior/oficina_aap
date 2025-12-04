from datetime import datetime, date

class Agendamento:
    STATUS = ['agendado', 'em_andamento', 'concluido', 'cancelado']
    
    def __init__(self, veiculo_id, data, hora, servicos=None, 
                 observacoes=None, status='agendado', valor_total=0.0, id=None):
        self.id = id
        self.veiculo_id = veiculo_id
        self.data = data if isinstance(data, date) else datetime.strptime(data, '%Y-%m-%d').date()
        self.hora = hora
        self.servicos = servicos or []
        self.observacoes = observacoes
        self.status = status if status in self.STATUS else 'agendado'
        self.valor_total = valor_total
    
    def to_dict(self):
        return {
            'id': self.id,
            'veiculo_id': self.veiculo_id,
            'data': str(self.data),
            'hora': self.hora,
            'observacoes': self.observacoes,
            'status': self.status,
            'valor_total': self.valor_total
        }