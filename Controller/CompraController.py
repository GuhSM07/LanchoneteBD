from databases.conecta import conecta
from Model.Compra import Compra

def inserir_compra(compra: Compra):
    conn = conecta()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Compra (id_produto, data, quantidade)
        VALUES (?, ?, ?)
    """, (compra.id_produto, compra.data, compra.quantidade))
    conn.commit()
    conn.close()

def listar_compras():
    conn = conecta()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT Compra.id, Produto.nome, data, quantidade
        FROM Compra
        JOIN Produto ON Compra.id_produto = Produto.id
    """)
    compras = cursor.fetchall()
    conn.close()
    return compras
