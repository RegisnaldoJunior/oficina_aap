class VeiculoController:
    def __init__(self, db):
        self.db = db
    
    def cadastrar_veiculo(self, placa, marca, modelo, ano, cor, cliente_id, observacoes):
        """Cadastra um novo veículo"""
        veiculo_data = {
            'placa': placa.upper(),
            'marca': marca,
            'modelo': modelo,
            'ano': ano,
            'cor': cor,
            'cliente_id': cliente_id,
            'observacoes': observacoes
        }
        
        try:
            veiculo_id = self.db.insert('veiculos', veiculo_data)
            return veiculo_id
        except sqlite3.IntegrityError:
            return None  # Placa duplicada
    
    def listar_veiculos(self, cliente_id=None):
        """Lista veículos, opcionalmente filtrando por cliente"""
        if cliente_id:
            query = """
                SELECT v.*, c.nome as cliente_nome 
                FROM veiculos v
                LEFT JOIN clientes c ON v.cliente_id = c.id
                WHERE v.cliente_id = ?
                ORDER BY v.placa
            """
            params = (cliente_id,)
        else:
            query = """
                SELECT v.*, c.nome as cliente_nome 
                FROM veiculos v
                LEFT JOIN clientes c ON v.cliente_id = c.id
                ORDER BY v.placa
            """
            params = ()
        
        veiculos = self.db.fetch_all(query, params)
        return [dict(veiculo) for veiculo in veiculos]
    
    def buscar_veiculo_por_placa(self, placa):
        """Busca veículo pela placa"""
        query = """
            SELECT v.*, c.nome as cliente_nome 
            FROM veiculos v
            LEFT JOIN clientes c ON v.cliente_id = c.id
            WHERE v.placa = ?
        """
        result = self.db.fetch_one(query, (placa.upper(),))
        return dict(result) if result else None
    
    def get_historico_veiculo(self, veiculo_id):
        """Retorna histórico de serviços do veículo"""
        query = """
            SELECT a.data, a.hora, a.status, group_concat(s.nome) as servicos
            FROM agendamentos a
            LEFT JOIN agendamento_servicos asv ON a.id = asv.agendamento_id
            LEFT JOIN servicos s ON asv.servico_id = s.id
            WHERE a.veiculo_id = ?
            GROUP BY a.id
            ORDER BY a.data DESC, a.hora DESC
        """
        historico = self.db.fetch_all(query, (veiculo_id,))
        return [dict(item) for item in historico]