from datetime import datetime
import random
import string

class OSController:
    def __init__(self, db):
        self.db = db
    
    def gerar_numero_os(self):
        """Gera um número único para a OS"""
        ano = datetime.now().year
        numero = random.randint(1000, 9999)
        return f"OS-{ano}-{numero}"
    
    def criar_ordem_servico(self, veiculo_id, km_veiculo, observacoes):
        """Cria uma nova ordem de serviço"""
        numero_os = self.gerar_numero_os()
        
        os_data = {
            'numero': numero_os,
            'veiculo_id': veiculo_id,
            'km_veiculo': km_veiculo,
            'observacoes': observacoes
        }
        
        os_id = self.db.insert('ordens_servico', os_data)
        return os_id, numero_os
    
    def adicionar_servico_os(self, os_id, servico_id, quantidade=1, observacoes=None):
        """Adiciona um serviço à OS"""
        # Buscar valor do serviço
        query = "SELECT valor FROM servicos WHERE id = ?"
        servico = self.db.fetch_one(query, (servico_id,))
        
        if not servico:
            return False, "Serviço não encontrado"
        
        os_servico_data = {
            'os_id': os_id,
            'servico_id': servico_id,
            'quantidade': quantidade,
            'valor_unitario': servico['valor'],
            'observacoes': observacoes
        }
        
        try:
            self.db.insert('os_servicos', os_servico_data)
            
            # Atualizar valor total da OS
            self.atualizar_valor_total(os_id)
            
            return True, "Serviço adicionado com sucesso"
        except Exception as e:
            return False, f"Erro: {str(e)}"
    
    def adicionar_peca_os(self, os_id, peca_id, quantidade=1):
        """Adiciona uma peça à OS"""
        # Verificar estoque
        peca_controller = PecaController(self.db)
        disponivel, estoque_atual = peca_controller.verificar_estoque(peca_id, quantidade)
        
        if not disponivel:
            return False, f"Estoque insuficiente. Disponível: {estoque_atual}"
        
        # Buscar valor da peça
        query = "SELECT valor_venda FROM pecas_estoque WHERE id = ?"
        peca = self.db.fetch_one(query, (peca_id,))
        
        if not peca:
            return False, "Peça não encontrada"
        
        os_peca_data = {
            'os_id': os_id,
            'peca_id': peca_id,
            'quantidade': quantidade,
            'valor_unitario': peca['valor_venda']
        }
        
        try:
            self.db.insert('os_pecas', os_peca_data)
            
            # Registrar saída do estoque
            peca_controller.registrar_movimentacao(
                peca_id, 'saida', quantidade,
                f'OS #{os_id}', os_id, 'sistema'
            )
            
            # Atualizar valor total da OS
            self.atualizar_valor_total(os_id)
            
            return True, "Peça adicionada com sucesso"
        except Exception as e:
            return False, f"Erro: {str(e)}"
    
    def atualizar_valor_total(self, os_id):
        """Atualiza o valor total da OS"""
        query = """
            SELECT 
                COALESCE(SUM(os.quantidade * os.valor_unitario), 0) as total_servicos,
                COALESCE(SUM(op.quantidade * op.valor_unitario), 0) as total_pecas
            FROM ordens_servico o
            LEFT JOIN os_servicos os ON o.id = os.os_id
            LEFT JOIN os_pecas op ON o.id = op.os_id
            WHERE o.id = ?
            GROUP BY o.id
        """
        
        result = self.db.fetch_one(query, (os_id,))
        
        if result:
            valor_total = result['total_servicos'] + result['total_pecas']
            self.db.update('ordens_servico', os_id, {'valor_total': valor_total})