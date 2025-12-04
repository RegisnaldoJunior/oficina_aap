from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from datetime import datetime, timedelta

class AgendamentosScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.agendamentos = []
        self.carregar_agendamentos()
    
    def carregar_agendamentos(self):
        # Dados de exemplo
        hoje = datetime.now()
        self.agendamentos = [
            {
                'id': 1,
                'data': hoje.strftime('%d/%m/%Y'),
                'hora': '09:00',
                'veiculo': 'Ford Fiesta - ABC1234',
                'cliente': 'João Silva',
                'servicos': 'Troca de Óleo, Alinhamento',
                'status': 'Agendado'
            },
            {
                'id': 2,
                'data': hoje.strftime('%d/%m/%Y'),
                'hora': '14:00',
                'veiculo': 'Chevrolet Onix - DEF5678',
                'cliente': 'Maria Santos',
                'servicos': 'Freios',
                'status': 'Em andamento'
            },
            {
                'id': 3,
                'data': (hoje + timedelta(days=1)).strftime('%d/%m/%Y'),
                'hora': '10:30',
                'veiculo': 'Volkswagen Gol - GHI9012',
                'cliente': 'Pedro Oliveira',
                'servicos': 'Bateria',
                'status': 'Agendado'
            }
        ]
        self.atualizar_lista()
    
    def atualizar_lista(self):
        lista = self.ids.lista_agendamentos
        lista.clear_widgets()
        
        for ag in self.agendamentos:
            item = BoxLayout(orientation='horizontal', size_hint_y=None, height=60, spacing=5)
            
            # Data e Hora
            data_hora = BoxLayout(orientation='vertical', size_hint_x=0.15)
            data_hora.add_widget(Label(text=ag['data'], font_size=12))
            data_hora.add_widget(Label(text=ag['hora'], font_size=14, bold=True))
            
            # Veículo e Cliente
            veiculo_cliente = BoxLayout(orientation='vertical', size_hint_x=0.4)
            veiculo_cliente.add_widget(Label(text=ag['veiculo'], font_size=14, halign='left'))
            veiculo_cliente.add_widget(Label(text=ag['cliente'], font_size=12, halign='left'))
            
            # Serviços
            servicos = Label(text=ag['servicos'], size_hint_x=0.3, font_size=12, halign='left')
            
            # Status
            status = Label(text=ag['status'], size_hint_x=0.15, font_size=12)
            if ag['status'] == 'Agendado':
                status.color = (0, 0.5, 1, 1)  # Azul
            elif ag['status'] == 'Em andamento':
                status.color = (1, 0.5, 0, 1)  # Laranja
            elif ag['status'] == 'Concluído':
                status.color = (0, 0.7, 0, 1)  # Verde
            
            item.add_widget(data_hora)
            item.add_widget(veiculo_cliente)
            item.add_widget(servicos)
            item.add_widget(status)
            
            lista.add_widget(item)
    
    def filtrar_por_data(self):
        # Implementação simplificada
        data_filtro = self.ids.data_input.text
        if data_filtro:
            try:
                # Converte DD/MM/YYYY para objeto de data
                data_obj = datetime.strptime(data_filtro, '%d/%m/%Y')
                data_formatada = data_obj.strftime('%d/%m/%Y')
                
                resultados = [a for a in self.agendamentos if a['data'] == data_formatada]
                self.mostrar_resultados(resultados)
            except:
                self.ids.lista_agendamentos.clear_widgets()
                self.ids.lista_agendamentos.add_widget(
                    Label(text="Data inválida. Use DD/MM/AAAA")
                )
        else:
            self.atualizar_lista()
    
    def mostrar_resultados(self, resultados):
        lista = self.ids.lista_agendamentos
        lista.clear_widgets()
        
        if resultados:
            for ag in resultados:
                item = BoxLayout(orientation='horizontal', size_hint_y=None, height=60, spacing=5)
                
                data_hora = BoxLayout(orientation='vertical', size_hint_x=0.15)
                data_hora.add_widget(Label(text=ag['data'], font_size=12))
                data_hora.add_widget(Label(text=ag['hora'], font_size=14, bold=True))
                
                veiculo_cliente = BoxLayout(orientation='vertical', size_hint_x=0.4)
                veiculo_cliente.add_widget(Label(text=ag['veiculo'], font_size=14))
                veiculo_cliente.add_widget(Label(text=ag['cliente'], font_size=12))
                
                servicos = Label(text=ag['servicos'], size_hint_x=0.3, font_size=12)
                status = Label(text=ag['status'], size_hint_x=0.15, font_size=12)
                
                item.add_widget(data_hora)
                item.add_widget(veiculo_cliente)
                item.add_widget(servicos)
                item.add_widget(status)
                
                lista.add_widget(item)
        else:
            lista.add_widget(Label(text="Nenhum agendamento para esta data"))