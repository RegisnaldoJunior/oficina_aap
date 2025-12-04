from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from datetime import datetime

class DashboardScreen(Screen):
    def on_enter(self):
        self.atualizar_data_hora()
        self.atualizar_estatisticas()
        Clock.schedule_interval(self.atualizar_data_hora, 1)
    
    def atualizar_data_hora(self, *args):
        agora = datetime.now()
        self.ids.data_label.text = agora.strftime("%d/%m/%Y")
        self.ids.hora_label.text = agora.strftime("%H:%M:%S")
    
    def atualizar_estatisticas(self):
        # Exemplo de estatísticas
        self.ids.clientes_label.text = "25"
        self.ids.veiculos_label.text = "38"
        self.ids.agendamentos_label.text = "5"
        self.ids.receita_label.text = "R$ 2.850,00"
    
    def navegar_para(self, tela):
        self.manager.current = tela