from databases.conecta import conecta
from Model.Pessoa import Pessoa

def inserir_pessoa(pessoa: Pessoa):
    conn = conecta()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Pessoa (nome, celular) VALUES (?, ?)
    """, (pessoa.nome, pessoa.celular))
    conn.commit()
    conn.close()

def listar_pessoas():
    conn = conecta()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Pessoa")
    pessoas = cursor.fetchall()
    conn.close()
    return pessoas
