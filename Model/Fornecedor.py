from Model.Pessoa import Pessoa

class Fornecedor(Pessoa):
    def __init__(self, id=None, nome=None, celular=None, descricao=None, cnpj=None, valor_unitario=0.0, valor_total=0.0):
        super().__init__(id, nome, celular)
        self.descricao = descricao
        self.cnpj = cnpj
        self.valor_unitario = valor_unitario
        self.valor_total = valor_total
