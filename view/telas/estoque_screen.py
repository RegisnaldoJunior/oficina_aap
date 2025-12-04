from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout

class EstoqueScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.build_ui()
    
    def build_ui(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Cabeçalho
        header = BoxLayout(orientation='horizontal', size_hint_y=None, height=50)
        btn_voltar = Button(text='← Voltar', size_hint_x=None, width=100)
        btn_voltar.bind(on_press=lambda x: setattr(self.manager, 'current', 'dashboard'))
        
        titulo = Label(text='CONTROLE DE ESTOQUE', font_size=20, bold=True)
        
        header.add_widget(btn_voltar)
        header.add_widget(titulo)
        layout.add_widget(header)
        
        # Barra de ações
        acoes_frame = BoxLayout(orientation='horizontal', size_hint_y=None, height=50, spacing=10)
        
        btn_nova_peca = Button(text='+ Nova Peça', background_color=(0, 0.6, 0.3, 1))
        btn_nova_peca.bind(on_press=self.nova_peca)
        
        btn_entrada = Button(text='Entrada Estoque', background_color=(0.2, 0.4, 0.8, 1))
        btn_entrada.bind(on_press=self.entrada_estoque)
        
        btn_baixo_estoque = Button(text='Baixo Estoque', background_color=(1, 0.5, 0, 1))
        btn_baixo_estoque.bind(on_press=self.mostrar_baixo_estoque)
        
        acoes_frame.add_widget(btn_nova_peca)
        acoes_frame.add_widget(btn_entrada)
        acoes_frame.add_widget(btn_baixo_estoque)
        
        layout.add_widget(acoes_frame)
        
        # Barra de busca
        busca_frame = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
        busca_frame.add_widget(Label(text='Buscar:', size_hint_x=0.2))
        
        self.busca_input = TextInput(hint_text='Código ou nome da peça', size_hint_x=0.6)
        busca_frame.add_widget(self.busca_input)
        
        btn_buscar = Button(text='Buscar', size_hint_x=0.2)
        btn_buscar.bind(on_press=self.buscar_pecas)
        busca_frame.add_widget(btn_buscar)
        
        layout.add_widget(busca_frame)
        
        # Lista de peças
        scroll = ScrollView()
        self.lista_grid = GridLayout(cols=1, spacing=5, size_hint_y=None)
        self.lista_grid.bind(minimum_height=self.lista_grid.setter('height'))
        scroll.add_widget(self.lista_grid)
        layout.add_widget(scroll)
        
        # Carregar dados de exemplo
        self.carregar_pecas_exemplo()
        
        self.add_widget(layout)
    
    def carregar_pecas_exemplo(self):
        """Carrega dados de exemplo"""
        pecas = [
            {'codigo': 'FIL-001', 'nome': 'Filtro de Óleo', 'quantidade': 15, 'minimo': 5, 'valor': 15.00},
            {'codigo': 'PAST-002', 'nome': 'Pastilha de Freio', 'quantidade': 8, 'minimo': 4, 'valor': 80.00},
            {'codigo': 'BAT-003', 'nome': 'Bateria 60Ah', 'quantidade': 3, 'minimo': 2, 'valor': 250.00},
            {'codigo': 'OLEO-004', 'nome': 'Óleo 5W30 1L', 'quantidade': 25, 'minimo': 10, 'valor': 35.00},
            {'codigo': 'VELA-005', 'nome': 'Vela de Ignição', 'quantidade': 20, 'minimo': 15, 'valor': 25.00},
        ]
        
        for peca in pecas:
            item = self.criar_item_peca(peca)
            self.lista_grid.add_widget(item)
    
    def criar_item_peca(self, peca):
        """Cria um item da lista de peças"""
        item = BoxLayout(orientation='horizontal', size_hint_y=None, height=60, spacing=10)
        
        # Código e nome
        info_frame = BoxLayout(orientation='vertical', size_hint_x=0.4)
        info_frame.add_widget(Label(text=peca['codigo'], font_size=14, bold=True))
        info_frame.add_widget(Label(text=peca['nome'], font_size=12))
        item.add_widget(info_frame)
        
        # Estoque
        estoque_frame = BoxLayout(orientation='vertical', size_hint_x=0.3)
        quantidade = peca['quantidade']
        minimo = peca['minimo']
        
        estoque_frame.add_widget(Label(text=f'Estoque: {quantidade}', font_size=14))
        
        # Indicador de baixo estoque
        if quantidade <= minimo:
            alerta = Label(text=f'MÍNIMO: {minimo}', font_size=12, color=(1, 0, 0, 1), bold=True)
        else:
            alerta = Label(text=f'Mínimo: {minimo}', font_size=10, color=(0.5, 0.5, 0.5, 1))
        
        estoque_frame.add_widget(alerta)
        item.add_widget(estoque_frame)
        
        # Valor
        valor_frame = BoxLayout(orientation='vertical', size_hint_x=0.3)
        valor_frame.add_widget(Label(text='Valor:', font_size=12))
        valor_frame.add_widget(Label(text=f"R$ {peca['valor']:.2f}", font_size=14, bold=True))
        item.add_widget(valor_frame)
        
        return item
    
    def nova_peca(self, instance):
        """Abre formulário para nova peça"""
        content = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        content.add_widget(Label(text='Nova Peça no Estoque', font_size=18))
        
        campos = [
            ('Código:', TextInput(hint_text='Ex: FIL-001')),
            ('Nome:', TextInput(hint_text='Nome da peça')),
            ('Descrição:', TextInput(hint_text='Descrição (opcional)', multiline=True)),
            ('Quantidade Inicial:', TextInput(hint_text='0', text='0')),
            ('Quantidade Mínima:', TextInput(hint_text='5', text='5')),
            ('Valor de Compra:', TextInput(hint_text='0.00')),
            ('Valor de Venda:', TextInput(hint_text='0.00')),
            ('Fornecedor:', TextInput(hint_text='Fornecedor (opcional)')),
            ('Localização:', TextInput(hint_text='Prateleira/Armário'))
        ]
        
        self.campos_peca = {}
        
        for label_text, campo in campos:
            campo_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
            campo_layout.add_widget(Label(text=label_text, size_hint_x=0.4))
            campo_layout.add_widget(campo)
            content.add_widget(campo_layout)
            self.campos_peca[label_text[:-1].lower()] = campo
        
        btn_salvar = Button(text='Salvar', size_hint_y=None, height=40)
        btn_cancelar = Button(text='Cancelar', size_hint_y=None, height=40)
        
        btn_layout = BoxLayout(orientation='horizontal', spacing=10)
        btn_layout.add_widget(btn_salvar)
        btn_layout.add_widget(btn_cancelar)
        content.add_widget(btn_layout)
        
        popup = Popup(title='Nova Peça', content=content, size_hint=(0.9, 0.9))
        
        def salvar(instance):
            # Aqui você salvaria no banco de dados
            codigo = self.campos_peca['código'].text
            nome = self.campos_peca['nome'].text
            
            if not codigo or not nome:
                self.mostrar_mensagem('Erro', 'Código e nome são obrigatórios!')
                return
            
            # Adicionar à lista
            nova_peca = {
                'codigo': codigo,
                'nome': nome,
                'quantidade': int(self.campos_peca['quantidade inicial'].text or 0),
                'minimo': int(self.campos_peca['quantidade mínima'].text or 5),
                'valor': float(self.campos_peca['valor de venda'].text or 0)
            }
            
            item = self.criar_item_peca(nova_peca)
            self.lista_grid.add_widget(item)
            
            self.mostrar_mensagem('Sucesso', f'Peça {codigo} cadastrada com sucesso!')
            popup.dismiss()
        
        btn_salvar.bind(on_press=salvar)
        btn_cancelar.bind(on_press=popup.dismiss)
        
        popup.open()
    
    def entrada_estoque(self, instance):
        """Registra entrada no estoque"""
        content = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        content.add_widget(Label(text='Entrada no Estoque', font_size=18))
        
        # Selecionar peça
        peca_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
        peca_layout.add_widget(Label(text='Peça:', size_hint_x=0.3))
        peca_spinner = Spinner(text='Selecione a peça')
        peca_spinner.values = ['Filtro de Óleo', 'Pastilha de Freio', 'Bateria 60Ah', 'Óleo 5W30']
        peca_layout.add_widget(peca_spinner)
        content.add_widget(peca_layout)
        
        # Quantidade
        qtd_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
        qtd_layout.add_widget(Label(text='Quantidade:', size_hint_x=0.3))
        qtd_input = TextInput(hint_text='Quantidade', text='1')
        qtd_layout.add_widget(qtd_input)
        content.add_widget(qtd_layout)
        
        # Motivo
        motivo_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
        motivo_layout.add_widget(Label(text='Motivo:', size_hint_x=0.3))
        motivo_input = TextInput(hint_text='Compra, ajuste, etc.')
        motivo_layout.add_widget(motivo_input)
        content.add_widget(motivo_layout)
        
        btn_salvar = Button(text='Registrar Entrada', size_hint_y=None, height=40)
        btn_cancelar = Button(text='Cancelar', size_hint_y=None, height=40)
        
        btn_layout = BoxLayout(orientation='horizontal', spacing=10)
        btn_layout.add_widget(btn_salvar)
        btn_layout.add_widget(btn_cancelar)
        content.add_widget(btn_layout)
        
        popup = Popup(title='Entrada no Estoque', content=content, size_hint=(0.8, 0.6))
        
        def salvar(instance):
            self.mostrar_mensagem('Sucesso', 'Entrada registrada com sucesso!')
            popup.dismiss()
        
        btn_salvar.bind(on_press=salvar)
        btn_cancelar.bind(on_press=popup.dismiss)
        
        popup.open()
    
    def mostrar_baixo_estoque(self, instance):
        """Filtra itens com baixo estoque"""
        self.mostrar_mensagem('Baixo Estoque', 
                             'Mostrando apenas itens com estoque abaixo do mínimo.')
    
    def buscar_pecas(self, instance):
        """Busca peças no estoque"""
        termo = self.busca_input.text
        if termo:
            self.mostrar_mensagem('Busca', f'Buscando por: {termo}')
    
    def mostrar_mensagem(self, titulo, mensagem):
        popup = Popup(title=titulo,
                     content=Label(text=mensagem),
                     size_hint=(0.6, 0.4))
        popup.open()