from model.database import DatabaseManager
from model.cliente import Cliente
from model.veiculo import Veiculo
from model.servico import Servico
from model.agendamento import Agendamento

class AppController:
    def __init__(self):
        self.db = DatabaseManager()
        self.current_user = None
        self._load_initial_data()
    
    def _load_initial_data(self):
        """Carrega dados iniciais se necessário"""
        # Verifica se existem serviços cadastrados
        servicos = self.db.fetch_all("SELECT COUNT(*) as count FROM servicos")
        if servicos[0]['count'] == 0:
            self._create_default_services()
    
    def _create_default_services(self):
        """Cria serviços padrão"""
        default_services = [
            ('Troca de Óleo', 'Troca de óleo do motor e filtro', 50.00, 30, 'Preventiva'),
            ('Alinhamento', 'Alinhamento e balanceamento', 120.00, 60, 'Mecânica'),
            ('Freios', 'Troca de pastilhas e discos', 200.00, 90, 'Mecânica'),
            ('Bateria', 'Troca de bateria', 40.00, 20, 'Elétrica'),
            ('Pintura', 'Pintura de porta', 300.00, 180, 'Pintura')
        ]
        
        for nome, desc, valor, tempo, cat in default_services:
            self.db.insert('servicos', {
                'nome': nome,
                'descricao': desc,
                'valor_mao_obra': valor,
                'tempo_estimado': tempo,
                'categoria': cat
            })
    
    def login(self, username, password):
        """Simula login (em produção, implementar autenticação real)"""
        # Para MVP, aceita qualquer credencial
        if username and password:
            self.current_user = username
            return True
        return False
    
    def logout(self):
        self.current_user = None
    
    def get_estatisticas(self):
        """Retorna estatísticas para o dashboard"""
        total_clientes = self.db.fetch_one("SELECT COUNT(*) as count FROM clientes")['count']
        total_veiculos = self.db.fetch_one("SELECT COUNT(*) as count FROM veiculos")['count']
        
        hoje = date.today().strftime('%Y-%m-%d')
        agendamentos_hoje = self.db.fetch_one(
            "SELECT COUNT(*) as count FROM agendamentos WHERE data = ?", 
            (hoje,)
        )['count']
        
        return {
            'total_clientes': total_clientes,
            'total_veiculos': total_veiculos,
            'agendamentos_hoje': agendamentos_hoje,
            'servicos_ativos': 0  # Implementar lógica
        }