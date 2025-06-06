from Model.Pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, id=None, nome=None, celular=None, rg=None, cargo=None):
        super().__init__(id, nome, celular)
        self.rg = rg
        self.cargo = cargo
