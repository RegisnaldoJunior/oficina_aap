from datetime import datetime

class Orcamento:
    def __init__(self, agendamento_id, servicos, pecas=None, 
                 observacoes=None, status='pendente', id=None):
        self.id = id
        self.agendamento_id = agendamento_id
        self.servicos = servicos  # Lista de serviços com preços
        self.pecas = pecas or []  # Lista de peças com quantidades e preços
        self.observacoes = observacoes
        self.status = status
        self.data_criacao = datetime.now().date()
        self.valor_total = self.calcular_total()
    
    def calcular_total(self):
        total = sum(s['valor'] for s in self.servicos)
        total += sum(p['quantidade'] * p['valor_unitario'] for p in self.pecas)
        return total