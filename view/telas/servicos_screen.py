from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner

class ServicosScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.servicos = []
        self.carregar_servicos()
    
    def carregar_servicos(self):
        # Dados de exemplo
        self.servicos = [
            {'id': 1, 'nome': 'Troca de Óleo', 'valor': 50.00, 'categoria': 'Preventiva'},
            {'id': 2, 'nome': 'Alinhamento', 'valor': 120.00, 'categoria': 'Mecânica'},
            {'id': 3, 'nome': 'Freios', 'valor': 200.00, 'categoria': 'Mecânica'},
            {'id': 4, 'nome': 'Bateria', 'valor': 40.00, 'categoria': 'Elétrica'},
        ]
        self.atualizar_lista()
    
    def atualizar_lista(self):
        lista = self.ids.lista_servicos
        lista.clear_widgets()
        
        for servico in self.servicos:
            item = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
            item.add_widget(Label(text=servico['nome'], size_hint_x=0.5))
            item.add_widget(Label(text=f"R$ {servico['valor']:.2f}", size_hint_x=0.25))
            item.add_widget(Label(text=servico['categoria'], size_hint_x=0.25))
            lista.add_widget(item)
    
    def filtrar_por_categoria(self):
        categoria = self.ids.categoria_spinner.text
        if categoria != "Todas":
            resultados = [s for s in self.servicos if s['categoria'] == categoria]
            self.mostrar_resultados(resultados)
        else:
            self.atualizar_lista()
    
    def mostrar_resultados(self, resultados):
        lista = self.ids.lista_servicos
        lista.clear_widgets()
        
        if resultados:
            for servico in resultados:
                item = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
                item.add_widget(Label(text=servico['nome'], size_hint_x=0.5))
                item.add_widget(Label(text=f"R$ {servico['valor']:.2f}", size_hint_x=0.25))
                item.add_widget(Label(text=servico['categoria'], size_hint_x=0.25))
                lista.add_widget(item)
        else:
            lista.add_widget(Label(text="Nenhum serviço encontrado"))