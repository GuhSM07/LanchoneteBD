from databases.conecta import conecta
from Model.Funcionario import Funcionario
from Controller.PessoaController import inserir_pessoa

def inserir_funcionario(func: Funcionario):
    inserir_pessoa(func)
    conn = conecta()
    cursor = conn.cursor()
    cursor.execute("SELECT last_insert_rowid()")
    funcionario_id = cursor.fetchone()[0]
    cursor.execute("INSERT INTO Funcionario (id, rg, cargo) VALUES (?, ?, ?)", (funcionario_id, func.rg, func.cargo))
    conn.commit()
    conn.close()

def listar_funcionarios():
    conn = conecta()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT Pessoa.id, nome, celular, rg, cargo FROM Pessoa
        JOIN Funcionario ON Pessoa.id = Funcionario.id
    """)
    funcionarios = cursor.fetchall()
    conn.close()
    return funcionarios
