from databases.conecta import conecta
from Model.Caixa import Caixa

def inserir_caixa(caixa: Caixa):
    conn = conecta()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Caixa (valor_a_pagar, valor_a_receber, id_fornecedor, id_cliente)
        VALUES (?, ?, ?, ?)
    """, (caixa.valor_a_pagar, caixa.valor_a_receber, caixa.id_fornecedor, caixa.id_cliente))
    conn.commit()
    conn.close()

def listar_caixas():
    conn = conecta()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Caixa")
    caixas = cursor.fetchall()
    conn.close()
    return caixas
