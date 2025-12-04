from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout

class OrdemServicoScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.os_atual = None
        self.build_ui()
    
    def build_ui(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Cabeçalho
        header = BoxLayout(orientation='horizontal', size_hint_y=None, height=50)
        btn_voltar = Button(text='← Voltar', size_hint_x=None, width=100)
        btn_voltar.bind(on_press=lambda x: setattr(self.manager, 'current', 'dashboard'))
        
        self.titulo = Label(text='NOVA ORDEM DE SERVIÇO', font_size=20, bold=True)
        
        header.add_widget(btn_voltar)
        header.add_widget(self.titulo)
        layout.add_widget(header)
        
        # Dados da OS
        form_frame = BoxLayout(orientation='vertical', spacing=10, size_hint_y=None, height=300)
        
        # Número da OS
        os_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
        os_layout.add_widget(Label(text='OS Nº:', size_hint_x=0.3))
        self.os_numero = Label(text='', size_hint_x=0.7, font_size=16, bold=True)
        os_layout.add_widget(self.os_numero)
        form_frame.add_widget(os_layout)
        
        # Selecionar veículo
        veiculo_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
        veiculo_layout.add_widget(Label(text='Veículo:', size_hint_x=0.3))
        self.veiculo_spinner = Spinner(text='Selecione um veículo', size_hint_x=0.7)
        veiculo_layout.add_widget(self.veiculo_spinner)
        form_frame.add_widget(veiculo_layout)
        
        # KM do veículo
        km_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
        km_layout.add_widget(Label(text='KM do Veículo:', size_hint_x=0.3))
        self.km_input = TextInput(multiline=False, size_hint_x=0.7)
        km_layout.add_widget(self.km_input)
        form_frame.add_widget(km_layout)
        
        # Observações
        obs_layout = BoxLayout(orientation='vertical', size_hint_y=None, height=100)
        obs_layout.add_widget(Label(text='Observações:', size_hint_y=None, height=30))
        self.obs_input = TextInput(multiline=True, size_hint_y=0.7)
        obs_layout.add_widget(self.obs_input)
        form_frame.add_widget(obs_layout)
        
        layout.add_widget(form_frame)
        
        # Botões de ação
        btn_frame = BoxLayout(orientation='horizontal', size_hint_y=None, height=50, spacing=10)
        
        btn_nova = Button(text='Nova OS', background_color=(0, 0.6, 0.3, 1))
        btn_nova.bind(on_press=self.nova_os)
        
        btn_adicionar_servico = Button(text='+ Serviço', background_color=(0.2, 0.4, 0.8, 1))
        btn_adicionar_servico.bind(on_press=self.adicionar_servico)
        
        btn_adicionar_peca = Button(text='+ Peça', background_color=(0.8, 0.4, 0.2, 1))
        btn_adicionar_peca.bind(on_press=self.adicionar_peca)
        
        btn_finalizar = Button(text='Finalizar OS', background_color=(0.2, 0.6, 0.2, 1))
        btn_finalizar.bind(on_press=self.finalizar_os)
        
        btn_frame.add_widget(btn_nova)
        btn_frame.add_widget(btn_adicionar_servico)
        btn_frame.add_widget(btn_adicionar_peca)
        btn_frame.add_widget(btn_finalizar)
        
        layout.add_widget(btn_frame)
        
        # Itens da OS
        itens_label = Label(text='ITENS DA ORDEM DE SERVIÇO', size_hint_y=None, height=30, 
                           font_size=16, bold=True)
        layout.add_widget(itens_label)
        
        # Lista de itens
        scroll = ScrollView()
        self.itens_grid = GridLayout(cols=1, spacing=5, size_hint_y=None)
        self.itens_grid.bind(minimum_height=self.itens_grid.setter('height'))
        scroll.add_widget(self.itens_grid)
        layout.add_widget(scroll)
        
        # Total
        total_frame = BoxLayout(orientation='horizontal', size_hint_y=None, height=50)
        total_frame.add_widget(Label(text='TOTAL:', font_size=18, bold=True))
        self.total_label = Label(text='R$ 0,00', font_size=18, bold=True, color=(0, 0.6, 0, 1))
        total_frame.add_widget(self.total_label)
        layout.add_widget(total_frame)
        
        self.add_widget(layout)
        self.nova_os(None)
    
    def nova_os(self, instance):
        """Cria uma nova ordem de serviço"""
        # Gerar número da OS
        import random
        ano = 2024
        numero = random.randint(1000, 9999)
        self.os_numero.text = f"OS-{ano}-{numero}"
        
        # Limpar campos
        self.km_input.text = ''
        self.obs_input.text = ''
        
        # Limpar itens
        self.itens_grid.clear_widgets()
        self.total_label.text = 'R$ 0,00'
        
        # Carregar veículos
        self.carregar_veiculos()
    
    def carregar_veiculos(self):
        """Carrega lista de veículos no spinner"""
        # Simulação - em produção, buscar do banco
        self.veiculo_spinner.values = [
            'ABC1234 - Ford Fiesta - João Silva',
            'DEF5678 - Chevrolet Onix - Maria Santos',
            'GHI9012 - Volkswagen Gol - Pedro Oliveira'
        ]
    
    def adicionar_servico(self, instance):
        """Abre popup para adicionar serviço"""
        content = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        content.add_widget(Label(text='Adicionar Serviço', font_size=18))
        
        servico_spinner = Spinner(text='Selecione um serviço')
        servico_spinner.values = [
            'Troca de Óleo - R$ 50,00',
            'Alinhamento - R$ 120,00',
            'Freios - R$ 200,00',
            'Bateria - R$ 40,00'
        ]
        
        content.add_widget(servico_spinner)
        
        quantidade_input = TextInput(hint_text='Quantidade', text='1')
        content.add_widget(quantidade_input)
        
        btn_salvar = Button(text='Adicionar', size_hint_y=None, height=40)
        btn_cancelar = Button(text='Cancelar', size_hint_y=None, height=40)
        
        btn_layout = BoxLayout(orientation='horizontal', spacing=10)
        btn_layout.add_widget(btn_salvar)
        btn_layout.add_widget(btn_cancelar)
        content.add_widget(btn_layout)
        
        popup = Popup(title='Adicionar Serviço', content=content, size_hint=(0.8, 0.5))
        
        def salvar(instance):
            # Adicionar item à lista
            item_text = f"SERVIÇO: {servico_spinner.text} x{quantidade_input.text}"
            item = Label(text=item_text, size_hint_y=None, height=30)
            self.itens_grid.add_widget(item)
            
            # Atualizar total (simulação)
            self.atualizar_total()
            popup.dismiss()
        
        btn_salvar.bind(on_press=salvar)
        btn_cancelar.bind(on_press=popup.dismiss)
        
        popup.open()
    
    def adicionar_peca(self, instance):
        """Abre popup para adicionar peça"""
        content = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        content.add_widget(Label(text='Adicionar Peça', font_size=18))
        
        peca_spinner = Spinner(text='Selecione uma peça')
        peca_spinner.values = [
            'Filtro de Óleo - R$ 15,00',
            'Pastilha de Freio - R$ 80,00',
            'Bateria 60Ah - R$ 250,00',
            'Óleo 5W30 - R$ 35,00'
        ]
        
        content.add_widget(peca_spinner)
        
        quantidade_input = TextInput(hint_text='Quantidade', text='1')
        content.add_widget(quantidade_input)
        
        btn_salvar = Button(text='Adicionar', size_hint_y=None, height=40)
        btn_cancelar = Button(text='Cancelar', size_hint_y=None, height=40)
        
        btn_layout = BoxLayout(orientation='horizontal', spacing=10)
        btn_layout.add_widget(btn_salvar)
        btn_layout.add_widget(btn_cancelar)
        content.add_widget(btn_layout)
        
        popup = Popup(title='Adicionar Peça', content=content, size_hint=(0.8, 0.5))
        
        def salvar(instance):
            # Adicionar item à lista
            item_text = f"PEÇA: {peca_spinner.text} x{quantidade_input.text}"
            item = Label(text=item_text, size_hint_y=None, height=30)
            self.itens_grid.add_widget(item)
            
            # Atualizar total (simulação)
            self.atualizar_total()
            popup.dismiss()
        
        btn_salvar.bind(on_press=salvar)
        btn_cancelar.bind(on_press=popup.dismiss)
        
        popup.open()
    
    def atualizar_total(self):
        """Atualiza o valor total (simulação)"""
        # Simulação - em produção, calcular com base nos itens
        total = 0
        for child in self.itens_grid.children:
            if 'R$' in child.text:
                # Extrair valor do texto
                import re
                valores = re.findall(r'R\$\s*(\d+[\.,]?\d*)', child.text)
                if valores:
                    valor = float(valores[0].replace(',', '.'))
                    total += valor
        
        self.total_label.text = f'R$ {total:,.2f}'.replace('.', ',')
    
    def finalizar_os(self, instance):
        """Finaliza a ordem de serviço"""
        if not self.veiculo_spinner.text or self.veiculo_spinner.text == 'Selecione um veículo':
            self.mostrar_erro('Selecione um veículo!')
            return
        
        # Aqui você salvaria a OS no banco de dados
        self.mostrar_sucesso(f'Ordem de Serviço {self.os_numero.text} finalizada com sucesso!')
        self.nova_os(None)
    
    def mostrar_erro(self, mensagem):
        popup = Popup(title='Erro',
                     content=Label(text=mensagem),
                     size_hint=(0.6, 0.4))
        popup.open()
    
    def mostrar_sucesso(self, mensagem):
        popup = Popup(title='Sucesso',
                     content=Label(text=mensagem),
                     size_hint=(0.6, 0.4))
        popup.open()