class Caixa():
    def __init__(self, id=None, valor_a_pagar=0.0, valor_a_receber=0.0, id_fornecedor=None, id_cliente=None):
        self.id = id
        self.valor_a_pagar = valor_a_pagar
        self.valor_a_receber = valor_a_receber
        self.id_fornecedor = id_fornecedor
        self.id_cliente = id_cliente
