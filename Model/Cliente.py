from Model.Pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, id=None, nome=None, celular=None, rg=None):
        super().__init__(id, nome, celular)
        self.rg = rg
