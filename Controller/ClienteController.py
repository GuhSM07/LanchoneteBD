from databases.conecta import conecta
from Model.Cliente import Cliente
from Controller.PessoaController import inserir_pessoa

def inserir_cliente(cliente: Cliente):
    inserir_pessoa(cliente)  # insere na tabela Pessoa
    conn = conecta()
    cursor = conn.cursor()
    cursor.execute("SELECT last_insert_rowid()")  # pega o último ID inserido
    cliente_id = cursor.fetchone()[0]
    cursor.execute("INSERT INTO Cliente (id, rg) VALUES (?, ?)", (cliente_id, cliente.rg))
    conn.commit()
    conn.close()

def listar_clientes():
    conn = conecta()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT Pessoa.id, nome, celular, rg FROM Pessoa
        JOIN Cliente ON Pessoa.id = Cliente.id
    """)
    clientes = cursor.fetchall()
    conn.close()
    return clientes
