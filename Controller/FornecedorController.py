from databases.conecta import conecta
from Model.Fornecedor import Fornecedor
from Controller.PessoaController import inserir_pessoa

def inserir_fornecedor(f: Fornecedor):
    inserir_pessoa(f)
    conn = conecta()
    cursor = conn.cursor()
    cursor.execute("SELECT last_insert_rowid()")
    fornecedor_id = cursor.fetchone()[0]
    cursor.execute("""
        INSERT INTO Fornecedor (id, descricao, cnpj, valor_unitario, valor_total)
        VALUES (?, ?, ?, ?, ?)
    """, (fornecedor_id, f.descricao, f.cnpj, f.valor_unitario, f.valor_total))
    conn.commit()
    conn.close()

def listar_fornecedores():
    conn = conecta()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT Pessoa.id, nome, celular, descricao, cnpj, valor_unitario, valor_total
        FROM Pessoa
        JOIN Fornecedor ON Pessoa.id = Fornecedor.id
    """)
    fornecedores = cursor.fetchall()
    conn.close()
    return fornecedores
