
from databases.conecta import conecta
from Model.Produto import Produto

def inserir_produto(produto: Produto):
    conn = conecta()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Produto (nome, preco) VALUES (?, ?)", (produto.nome, produto.preco))
    conn.commit()
    conn.close()

def listar_produtos():
    conn = conecta()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Produto")
    produtos = cursor.fetchall()
    conn.close()
    return produtos
