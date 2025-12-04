from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class ClientesScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.clientes = []
        self.carregar_clientes()
    
    def carregar_clientes(self):
        # Dados de exemplo
        self.clientes = [
            {'id': 1, 'nome': 'João Silva', 'telefone': '(11) 99999-9999', 'email': 'joao@email.com'},
            {'id': 2, 'nome': 'Maria Santos', 'telefone': '(11) 98888-8888', 'email': 'maria@email.com'},
            {'id': 3, 'nome': 'Pedro Oliveira', 'telefone': '(11) 97777-7777', 'email': 'pedro@email.com'},
        ]
        self.atualizar_lista()
    
    def atualizar_lista(self):
        lista = self.ids.lista_clientes
        lista.clear_widgets()
        
        for cliente in self.clientes:
            item = BoxLayout(orientation='horizontal', size_hint_y=None, height=50)
            item.add_widget(Label(text=cliente['nome'], size_hint_x=0.4))
            item.add_widget(Label(text=cliente['telefone'], size_hint_x=0.3))
            item.add_widget(Label(text=cliente['email'], size_hint_x=0.3))
            lista.add_widget(item)
    
    def buscar_cliente(self):
        termo = self.ids.busca_input.text.lower()
        if termo:
            resultados = [c for c in self.clientes if termo in c['nome'].lower()]
            self.mostrar_resultados(resultados)
        else:
            self.atualizar_lista()
    
    def mostrar_resultados(self, resultados):
        lista = self.ids.lista_clientes
        lista.clear_widgets()
        
        if resultados:
            for cliente in resultados:
                item = BoxLayout(orientation='horizontal', size_hint_y=None, height=50)
                item.add_widget(Label(text=cliente['nome'], size_hint_x=0.4))
                item.add_widget(Label(text=cliente['telefone'], size_hint_x=0.3))
                item.add_widget(Label(text=cliente['email'], size_hint_x=0.3))
                lista.add_widget(item)
        else:
            lista.add_widget(Label(text="Nenhum cliente encontrado"))
    
    def abrir_popup_novo_cliente(self):
        content = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        content.add_widget(Label(text="Novo Cliente", font_size=20))
        
        nome_input = TextInput(hint_text="Nome completo", multiline=False)
        telefone_input = TextInput(hint_text="Telefone", multiline=False)
        email_input = TextInput(hint_text="E-mail", multiline=False)
        endereco_input = TextInput(hint_text="Endereço", multiline=False)
        
        content.add_widget(nome_input)
        content.add_widget(telefone_input)
        content.add_widget(email_input)
        content.add_widget(endereco_input)
        
        btn_salvar = Button(text="Salvar", size_hint_y=None, height=40)
        btn_cancelar = Button(text="Cancelar", size_hint_y=None, height=40)
        
        btn_layout = BoxLayout(orientation='horizontal', spacing=10)
        btn_layout.add_widget(btn_salvar)
        btn_layout.add_widget(btn_cancelar)
        content.add_widget(btn_layout)
        
        popup = Popup(title="Novo Cliente", content=content, size_hint=(0.8, 0.8))
        
        def salvar_cliente(instance):
            novo_cliente = {
                'id': len(self.clientes) + 1,
                'nome': nome_input.text,
                'telefone': telefone_input.text,
                'email': email_input.text
            }
            self.clientes.append(novo_cliente)
            self.atualizar_lista()
            popup.dismiss()
        
        btn_salvar.bind(on_press=salvar_cliente)
        btn_cancelar.bind(on_press=popup.dismiss)
        
        popup.open()