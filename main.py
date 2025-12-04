from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
from kivy.lang import Builder
import os

# Importar telas
from view.telas.login_screen import LoginScreen
from view.telas.dashboard_screen import DashboardScreen
from view.telas.clientes_screen import ClientesScreen
from view.telas.veiculos_screen import VeiculosScreen
from view.telas.servicos_screen import ServicosScreen
from view.telas.agendamentos_screen import AgendamentosScreen
from view.telas.ordem_servico_screen import OrdemServicoScreen
from view.telas.estoque_screen import EstoqueScreen

# Carregar arquivos KV
Builder.load_file('view/telas/login_screen.kv')
Builder.load_file('view/telas/dashboard_screen.kv')
Builder.load_file('view/telas/clientes_screen.kv')
Builder.load_file('view/telas/veiculos_screen.kv')
Builder.load_file('view/telas/servicos_screen.kv')
Builder.load_file('view/telas/agendamentos_screen.kv')
Builder.load_file('view/telas/ordem_servico_screen.kv')
Builder.load_file('view/telas/estoque_screen.kv')

class OficinaApp(App):
    def build(self):
        self.title = "Oficina Manager Pro"
        Window.size = (1200, 700)
        
        # Criar ScreenManager
        sm = ScreenManager()
        
        # Adicionar telas
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(DashboardScreen(name='dashboard'))
        sm.add_widget(ClientesScreen(name='clientes'))
        sm.add_widget(VeiculosScreen(name='veiculos'))
        sm.add_widget(ServicosScreen(name='servicos'))
        sm.add_widget(AgendamentosScreen(name='agendamentos'))
        sm.add_widget(OrdemServicoScreen(name='ordem_servico'))
        sm.add_widget(EstoqueScreen(name='estoque'))
        
        return sm

if __name__ == '__main__':
    OficinaApp().run()