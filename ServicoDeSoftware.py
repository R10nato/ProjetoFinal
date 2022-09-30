from abc import ABC


class SerticosDeSoftware(ABC):
    def __init__(self,versao,nome,id,cliente):
        super().__init__(id, cliente)
        self.versao = versao
        self.nome = nome


