from kivy.uix.screenmanager import Screen
from kivy.app import App

class LoginScreen(Screen):
    def fazer_login(self):
        username = self.ids.username_input.text
        password = self.ids.password_input.text
        
        # Validação simples
        if username == 'admin' and password == 'admin':
            self.manager.current = 'dashboard'
            self.ids.error_label.text = ""
        else:
            self.ids.error_label.text = "Usuário ou senha inválidos"
    
    def limpar_campos(self):
        self.ids.username_input.text = ""
        self.ids.password_input.text = ""
        self.ids.error_label.text = ""