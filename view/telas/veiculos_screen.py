from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner

class VeiculosScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.veiculos = []
        self.carregar_veiculos()
    
    def carregar_veiculos(self):
        # Dados de exemplo
        self.veiculos = [
            {'id': 1, 'placa': 'ABC1234', 'marca': 'Ford', 'modelo': 'Fiesta', 'ano': 2020, 'cliente': 'João Silva'},
            {'id': 2, 'placa': 'DEF5678', 'marca': 'Chevrolet', 'modelo': 'Onix', 'ano': 2021, 'cliente': 'Maria Santos'},
            {'id': 3, 'placa': 'GHI9012', 'marca': 'Volkswagen', 'modelo': 'Gol', 'ano': 2019, 'cliente': 'Pedro Oliveira'},
        ]
        self.atualizar_lista()
    
    def atualizar_lista(self):
        lista = self.ids.lista_veiculos
        lista.clear_widgets()
        
        for veiculo in self.veiculos:
            item = BoxLayout(orientation='horizontal', size_hint_y=None, height=50)
            item.add_widget(Label(text=veiculo['placa'], size_hint_x=0.2))
            item.add_widget(Label(text=veiculo['marca'], size_hint_x=0.2))
            item.add_widget(Label(text=veiculo['modelo'], size_hint_x=0.2))
            item.add_widget(Label(text=str(veiculo['ano']), size_hint_x=0.2))
            item.add_widget(Label(text=veiculo['cliente'], size_hint_x=0.2))
            lista.add_widget(item)
    
    def buscar_veiculo(self):
        termo = self.ids.busca_input.text.lower()
        if termo:
            resultados = [v for v in self.veiculos 
                         if termo in v['placa'].lower() 
                         or termo in v['modelo'].lower()]
            self.mostrar_resultados(resultados)
        else:
            self.atualizar_lista()
    
    def mostrar_resultados(self, resultados):
        lista = self.ids.lista_veiculos
        lista.clear_widgets()
        
        if resultados:
            for veiculo in resultados:
                item = BoxLayout(orientation='horizontal', size_hint_y=None, height=50)
                item.add_widget(Label(text=veiculo['placa'], size_hint_x=0.2))
                item.add_widget(Label(text=veiculo['marca'], size_hint_x=0.2))
                item.add_widget(Label(text=veiculo['modelo'], size_hint_x=0.2))
                item.add_widget(Label(text=str(veiculo['ano']), size_hint_x=0.2))
                item.add_widget(Label(text=veiculo['cliente'], size_hint_x=0.2))
                lista.add_widget(item)
        else:
            lista.add_widget(Label(text="Nenhum veículo encontrado"))
    
    def abrir_popup_novo_veiculo(self):
        content = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        content.add_widget(Label(text="Novo Veículo", font_size=20))
        
        placa_input = TextInput(hint_text="Placa", multiline=False)
        marca_input = TextInput(hint_text="Marca", multiline=False)
        modelo_input = TextInput(hint_text="Modelo", multiline=False)
        ano_input = TextInput(hint_text="Ano", multiline=False)
        cor_input = TextInput(hint_text="Cor", multiline=False)
        
        content.add_widget(placa_input)
        content.add_widget(marca_input)
        content.add_widget(modelo_input)
        
        ano_cor_layout = BoxLayout(orientation='horizontal', spacing=10)
        ano_cor_layout.add_widget(ano_input)
        ano_cor_layout.add_widget(cor_input)
        content.add_widget(ano_cor_layout)
        
        btn_salvar = Button(text="Salvar", size_hint_y=None, height=40)
        btn_cancelar = Button(text="Cancelar", size_hint_y=None, height=40)
        
        btn_layout = BoxLayout(orientation='horizontal', spacing=10)
        btn_layout.add_widget(btn_salvar)
        btn_layout.add_widget(btn_cancelar)
        content.add_widget(btn_layout)
        
        popup = Popup(title="Novo Veículo", content=content, size_hint=(0.8, 0.6))
        
        def salvar_veiculo(instance):
            novo_veiculo = {
                'id': len(self.veiculos) + 1,
                'placa': placa_input.text,
                'marca': marca_input.text,
                'modelo': modelo_input.text,
                'ano': ano_input.text,
                'cliente': "Cliente não definido"
            }
            self.veiculos.append(novo_veiculo)
            self.atualizar_lista()
            popup.dismiss()
        
        btn_salvar.bind(on_press=salvar_veiculo)
        btn_cancelar.bind(on_press=popup.dismiss)
        
        popup.open()