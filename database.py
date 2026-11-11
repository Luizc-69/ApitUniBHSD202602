import sqlite3
def get_db_connection():
    # Cria o arquivo banco_a3.db na mesma pasta do projeto
    conn = sqlite3.connect("banco_a3.db")
    conn.row_factory = sqlite3.Row  # Permite acessar colunas por nome
    return conn
def criar_tabelas():
    # Cria a tabela de registros caso ela não exista
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS registros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            descricao TEXT,
            ativo BOOLEAN DEFAULT TRUE
        )
    ''')
    conn.commit()
    conn.close()
