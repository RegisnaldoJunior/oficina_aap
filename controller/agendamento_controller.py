from datetime import datetime, date, timedelta

class AgendamentoController:
    def __init__(self, db):
        self.db = db
    
    def listar_agendamentos(self, data=None, status=None):
        """Lista agendamentos, com filtros opcionais"""
        query = """
            SELECT a.*, v.placa, v.marca, v.modelo, c.nome as cliente_nome
            FROM agendamentos a
            JOIN veiculos v ON a.veiculo_id = v.id
            JOIN clientes c ON v.cliente_id = c.id
            WHERE 1=1
        """
        params = []
        
        if data:
            query += " AND a.data = ?"
            params.append(data)
        
        if status:
            query += " AND a.status = ?"
            params.append(status)
        
        query += " ORDER BY a.data, a.hora"
        
        agendamentos = self.db.fetch_all(query, params)
        return [dict(ag) for ag in agendamentos]
    
    def verificar_disponibilidade(self, data, hora, duracao_minutos=60):
        """Verifica se há horário disponível"""
        hora_fim = self._calcular_hora_fim(hora, duracao_minutos)
        
        query = """
            SELECT COUNT(*) as count 
            FROM agendamentos 
            WHERE data = ? 
            AND (
                (hora <= ? AND self._calcular_hora_fim(hora, tempo_estimado) > ?)
                OR (hora < ? AND self._calcular_hora_fim(hora, tempo_estimado) >= ?)
            )
        """
        
        # Implementação simplificada - em produção, considerar tempo estimado dos serviços
        params = (data, hora, hora, hora_fim, hora)
        result = self.db.fetch_one(query, params)
        
        return result['count'] == 0
    
    def _calcular_hora_fim(self, hora_inicio, duracao_minutos):
        """Calcula hora de término baseado na duração"""
        horas, minutos = map(int, hora_inicio.split(':'))
        total_minutos = horas * 60 + minutes + duracao_minutos
        nova_hora = total_minutos // 60
        novo_minuto = total_minutos % 60
        return f"{nova_hora:02d}:{novo_minuto:02d}"
    
    def criar_agendamento(self, veiculo_id, data, hora, servicos_ids, observacoes):
        """Cria novo agendamento"""
        # Calcula valor total
        valor_total = 0
        tempo_total = 0
        
        for servico_id in servicos_ids:
            servico = self.db.fetch_one(
                "SELECT valor_mao_obra, tempo_estimado FROM servicos WHERE id = ?",
                (servico_id,)
            )
            if servico:
                valor_total += servico['valor_mao_obra']
                tempo_total += servico['tempo_estimado'] or 60
        
        # Verifica disponibilidade
        if not self.verificar_disponibilidade(data, hora, tempo_total):
            return None, "Horário indisponível"
        
        # Cria agendamento
        agendamento_data = {
            'veiculo_id': veiculo_id,
            'data': data,
            'hora': hora,
            'observacoes': observacoes,
            'valor_total': valor_total
        }
        
        try:
            agendamento_id = self.db.insert('agendamentos', agendamento_data)
            
            # Associa serviços
            for servico_id in servicos_ids:
                self.db.insert('agendamento_servicos', {
                    'agendamento_id': agendamento_id,
                    'servico_id': servico_id
                })
            
            return agendamento_id, "Agendamento criado com sucesso"
            
        except Exception as e:
            return None, f"Erro: {str(e)}"