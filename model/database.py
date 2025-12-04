import sqlite3
from datetime import datetime
from pathlib import Path

class DatabaseManager:
    def __init__(self, db_name='oficina.db'):
        self.db_path = Path(__file__).parent.parent / db_name
        self.connection = None
        self.connect()
        self.create_tables()
    
    def connect(self):
        """Estabelece conexão com o banco de dados"""
        self.connection = sqlite3.connect(self.db_path)
        self.connection.row_factory = sqlite3.Row
    
    def create_tables(self):
        """Cria todas as tabelas necessárias"""
        queries = [
            '''CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                telefone TEXT,
                email TEXT,
                endereco TEXT,
                data_cadastro DATE DEFAULT CURRENT_DATE
            )''',
            
            '''CREATE TABLE IF NOT EXISTS veiculos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                placa TEXT UNIQUE NOT NULL,
                marca TEXT NOT NULL,
                modelo TEXT NOT NULL,
                ano INTEGER,
                cor TEXT,
                cliente_id INTEGER,
                observacoes TEXT,
                FOREIGN KEY (cliente_id) REFERENCES clientes(id)
            )''',
            
            '''CREATE TABLE IF NOT EXISTS servicos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                descricao TEXT,
                valor_mao_obra REAL DEFAULT 0,
                tempo_estimado INTEGER,  -- em minutos
                categoria TEXT
            )''',
            
            '''CREATE TABLE IF NOT EXISTS pecas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                codigo TEXT UNIQUE,
                quantidade INTEGER DEFAULT 0,
                valor_unitario REAL DEFAULT 0,
                fornecedor TEXT,
                localizacao TEXT
            )''',
            
            '''CREATE TABLE IF NOT EXISTS agendamentos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                veiculo_id INTEGER NOT NULL,
                data DATE NOT NULL,
                hora TEXT NOT NULL,
                status TEXT DEFAULT 'agendado',
                observacoes TEXT,
                valor_total REAL DEFAULT 0,
                FOREIGN KEY (veiculo_id) REFERENCES veiculos(id)
            )''',
            
            '''CREATE TABLE IF NOT EXISTS agendamento_servicos (
                agendamento_id INTEGER,
                servico_id INTEGER,
                PRIMARY KEY (agendamento_id, servico_id),
                FOREIGN KEY (agendamento_id) REFERENCES agendamentos(id),
                FOREIGN KEY (servico_id) REFERENCES servicos(id)
            )''',
            
            '''CREATE TABLE IF NOT EXISTS orcamentos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                agendamento_id INTEGER,
                data_criacao DATE DEFAULT CURRENT_DATE,
                status TEXT DEFAULT 'pendente',
                valor_total REAL,
                observacoes TEXT,
                FOREIGN KEY (agendamento_id) REFERENCES agendamentos(id)
            )''',

             '''CREATE TABLE IF NOT EXISTS pecas_estoque (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            codigo TEXT UNIQUE NOT NULL,
            nome TEXT NOT NULL,
            descricao TEXT,
            quantidade INTEGER DEFAULT 0,
            quantidade_minima INTEGER DEFAULT 5,
            valor_compra REAL DEFAULT 0,
            valor_venda REAL DEFAULT 0,
            fornecedor TEXT,
            localizacao TEXT,
            data_cadastro DATE DEFAULT CURRENT_DATE
            )''',
        
            '''CREATE TABLE IF NOT EXISTS ordens_servico (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                numero TEXT UNIQUE NOT NULL,
                veiculo_id INTEGER NOT NULL,
                data_abertura DATE DEFAULT CURRENT_DATE,
                data_fechamento DATE,
                status TEXT DEFAULT 'aberta',
                km_veiculo INTEGER,
                observacoes TEXT,
                valor_total REAL DEFAULT 0,
                FOREIGN KEY (veiculo_id) REFERENCES veiculos(id)
            )''',
            
            '''CREATE TABLE IF NOT EXISTS os_servicos (
                os_id INTEGER,
                servico_id INTEGER,
                quantidade INTEGER DEFAULT 1,
                valor_unitario REAL,
                observacoes TEXT,
                PRIMARY KEY (os_id, servico_id),
                FOREIGN KEY (os_id) REFERENCES ordens_servico(id),
                FOREIGN KEY (servico_id) REFERENCES servicos(id)
            )''',
            
            '''CREATE TABLE IF NOT EXISTS os_pecas (
                os_id INTEGER,
                peca_id INTEGER,
                quantidade INTEGER DEFAULT 1,
                valor_unitario REAL,
                PRIMARY KEY (os_id, peca_id),
                FOREIGN KEY (os_id) REFERENCES ordens_servico(id),
                FOREIGN KEY (peca_id) REFERENCES pecas_estoque(id)
            )''',
            
            '''CREATE TABLE IF NOT EXISTS movimentacoes_estoque (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                peca_id INTEGER,
                tipo TEXT,  -- entrada, saida, ajuste
                quantidade INTEGER,
                motivo TEXT,
                os_id INTEGER,
                data DATE DEFAULT CURRENT_DATE,
                usuario TEXT,
                FOREIGN KEY (peca_id) REFERENCES pecas_estoque(id),
                FOREIGN KEY (os_id) REFERENCES ordens_servico(id)
            )'''

        ]
        
        cursor = self.connection.cursor()
        for query in queries:
            cursor.execute(query)
        self.connection.commit()
    
    def execute_query(self, query, params=()):
        """Executa uma query e retorna o cursor"""
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        return cursor
    
    def fetch_all(self, query, params=()):
        """Retorna todos os resultados"""
        cursor = self.execute_query(query, params)
        return cursor.fetchall()
    
    def fetch_one(self, query, params=()):
        """Retorna um único resultado"""
        cursor = self.execute_query(query, params)
        return cursor.fetchone()
    
    def insert(self, table, data):
        """Insere dados em uma tabela"""
        columns = ', '.join(data.keys())
        placeholders = ', '.join(['?' for _ in data])
        query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
        
        cursor = self.execute_query(query, tuple(data.values()))
        self.connection.commit()
        return cursor.lastrowid
    
    def update(self, table, record_id, data):
        """Atualiza dados em uma tabela"""
        set_clause = ', '.join([f"{key} = ?" for key in data.keys()])
        query = f"UPDATE {table} SET {set_clause} WHERE id = ?"
        
        params = tuple(data.values()) + (record_id,)
        self.execute_query(query, params)
        self.connection.commit()
    
    def delete(self, table, record_id):
        """Remove um registro"""
        query = f"DELETE FROM {table} WHERE id = ?"
        self.execute_query(query, (record_id,))
        self.connection.commit()
    
    def close(self):
        """Fecha a conexão com o banco"""
        if self.connection:
            self.connection.close()