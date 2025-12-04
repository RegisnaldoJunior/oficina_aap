from model.peca_estoque import PecaEstoque

class PecaController:
    def __init__(self, db):
        self.db = db
    
    def cadastrar_peca(self, codigo, nome, descricao, quantidade, 
                      quantidade_minima, valor_compra, valor_venda, 
                      fornecedor, localizacao):
        """Cadastra uma nova peça no estoque"""
        peca_data = {
            'codigo': codigo,
            'nome': nome,
            'descricao': descricao,
            'quantidade': quantidade,
            'quantidade_minima': quantidade_minima,
            'valor_compra': valor_compra,
            'valor_venda': valor_venda,
            'fornecedor': fornecedor,
            'localizacao': localizacao
        }
        
        try:
            peca_id = self.db.insert('pecas_estoque', peca_data)
            
            # Registrar movimentação de entrada
            self.registrar_movimentacao(
                peca_id, 'entrada', quantidade, 
                'Cadastro inicial', None, 'sistema'
            )
            
            return peca_id
        except sqlite3.IntegrityError:
            return None  # Código duplicado
    
    def listar_pecas(self, filtro=None, apenas_baixo_estoque=False):
        """Lista peças do estoque"""
        if filtro:
            query = """
                SELECT * FROM pecas_estoque 
                WHERE codigo LIKE ? OR nome LIKE ? OR descricao LIKE ?
                ORDER BY nome
            """
            params = (f'%{filtro}%', f'%{filtro}%', f'%{filtro}%')
        elif apenas_baixo_estoque:
            query = "SELECT * FROM pecas_estoque WHERE quantidade <= quantidade_minima ORDER BY quantidade"
            params = ()
        else:
            query = "SELECT * FROM pecas_estoque ORDER BY nome"
            params = ()
        
        pecas = self.db.fetch_all(query, params)
        return [dict(peca) for peca in pecas]
    
    def registrar_movimentacao(self, peca_id, tipo, quantidade, motivo, os_id, usuario):
        """Registra movimentação no estoque"""
        mov_data = {
            'peca_id': peca_id,
            'tipo': tipo,
            'quantidade': quantidade,
            'motivo': motivo,
            'os_id': os_id,
            'usuario': usuario
        }
        
        # Atualizar quantidade no estoque
        if tipo == 'entrada':
            self.db.execute_query(
                "UPDATE pecas_estoque SET quantidade = quantidade + ? WHERE id = ?",
                (quantidade, peca_id)
            )
        elif tipo == 'saida':
            self.db.execute_query(
                "UPDATE pecas_estoque SET quantidade = quantidade - ? WHERE id = ?",
                (quantidade, peca_id)
            )
        
        self.db.insert('movimentacoes_estoque', mov_data)
        self.db.connection.commit()
    
    def verificar_estoque(self, peca_id, quantidade_necessaria):
        """Verifica se há estoque suficiente"""
        query = "SELECT quantidade FROM pecas_estoque WHERE id = ?"
        result = self.db.fetch_one(query, (peca_id,))
        
        if result and result['quantidade'] >= quantidade_necessaria:
            return True, result['quantidade']
        return False, result['quantidade'] if result else 0