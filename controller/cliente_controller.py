from model.cliente import Cliente
from model.veiculo import Veiculo

class ClienteController:
    def __init__(self, db):
        self.db = db
    
    def cadastrar_cliente(self, nome, telefone, email, endereco):
        """Cadastra um novo cliente"""
        cliente_data = {
            'nome': nome,
            'telefone': telefone,
            'email': email,
            'endereco': endereco
        }
        
        try:
            cliente_id = self.db.insert('clientes', cliente_data)
            return cliente_id
        except Exception as e:
            print(f"Erro ao cadastrar cliente: {e}")
            return None
    
    def listar_clientes(self, filtro=None):
        """Lista todos os clientes, com filtro opcional"""
        if filtro:
            query = """
                SELECT * FROM clientes 
                WHERE nome LIKE ? OR telefone LIKE ? OR email LIKE ?
                ORDER BY nome
            """
            params = (f'%{filtro}%', f'%{filtro}%', f'%{filtro}%')
        else:
            query = "SELECT * FROM clientes ORDER BY nome"
            params = ()
        
        clientes = self.db.fetch_all(query, params)
        return [dict(cliente) for cliente in clientes]
    
    def buscar_cliente_por_id(self, cliente_id):
        """Busca cliente por ID"""
        query = "SELECT * FROM clientes WHERE id = ?"
        result = self.db.fetch_one(query, (cliente_id,))
        return dict(result) if result else None
    
    def atualizar_cliente(self, cliente_id, dados):
        """Atualiza dados do cliente"""
        self.db.update('clientes', cliente_id, dados)
        return True
    
    def excluir_cliente(self, cliente_id):
        """Exclui cliente (verifica se tem veículos primeiro)"""
        # Verifica se cliente tem veículos
        veiculos = self.db.fetch_one(
            "SELECT COUNT(*) as count FROM veiculos WHERE cliente_id = ?",
            (cliente_id,)
        )
        
        if veiculos['count'] > 0:
            return False, "Cliente possui veículos cadastrados. Exclua os veículos primeiro."
        
        self.db.delete('clientes', cliente_id)
        return True, "Cliente excluído com sucesso."