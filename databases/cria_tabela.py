from conecta import conecta

def criar_tabelas():
    conn = conecta()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Pessoa (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        celular TEXT
    );
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Cliente (
        id INTEGER PRIMARY KEY,
        rg TEXT,
        FOREIGN KEY (id) REFERENCES Pessoa(id)
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Funcionario (
        id INTEGER PRIMARY KEY,
        rg TEXT,
        cargo TEXT,
        FOREIGN KEY (id) REFERENCES Pessoa(id)
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Fornecedor (
        id INTEGER PRIMARY KEY,
        descricao TEXT,
        cnpj TEXT,
        valor_unitario REAL,
        valor_total REAL,
        FOREIGN KEY (id) REFERENCES Pessoa(id)
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Produto (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        preco REAL NOT NULL
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Caixa (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        valor_a_pagar REAL,
        valor_a_receber REAL,
        id_fornecedor INTEGER,
        id_cliente INTEGER,
        FOREIGN KEY (id_fornecedor) REFERENCES Fornecedor(id),
        FOREIGN KEY (id_cliente) REFERENCES Cliente(id)
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Compra (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_produto INTEGER,
        data TEXT,
        quantidade INTEGER,
        FOREIGN KEY (id_produto) REFERENCES Produto(id)
    );
    """)

    conn.commit()
    conn.close()

# Executa ao importar
criar_tabelas()
