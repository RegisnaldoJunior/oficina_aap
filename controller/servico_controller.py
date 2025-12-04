class ServicoController:
    def __init__(self, db):
        self.db = db
    
    def listar_servicos(self, categoria=None):
        """Lista serviços, com filtro por categoria"""
        if categoria:
            query = "SELECT * FROM servicos WHERE categoria = ? ORDER BY nome"
            params = (categoria,)
        else:
            query = "SELECT * FROM servicos ORDER BY categoria, nome"
            params = ()
        
        servicos = self.db.fetch_all(query, params)
        return [dict(servico) for servico in servicos]
    
    def cadastrar_servico(self, nome, descricao, valor_mao_obra, tempo_estimado, categoria):
        """Cadastra novo serviço"""
        servico_data = {
            'nome': nome,
            'descricao': descricao,
            'valor_mao_obra': valor_mao_obra,
            'tempo_estimado': tempo_estimado,
            'categoria': categoria
        }
        
        servico_id = self.db.insert('servicos', servico_data)
        return servico_id
    
    def get_categorias(self):
        """Retorna lista de categorias únicas"""
        query = "SELECT DISTINCT categoria FROM servicos ORDER BY categoria"
        categorias = self.db.fetch_all(query)
        return [cat['categoria'] for cat in categorias]