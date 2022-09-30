class SerticosDeSoftware():
    def __init__(self,versao,nome,id,cliente):
        super().__init__(id, cliente)
        self.versao = versao
        self.nome = nome

    def get_versao(self):
        return self.versao

    def set_versao(self, novaVersao):
        self.versao = novaVersao
        return True

    def get_nome(self):
        return self.nome
    def set_nome(self, novoNome):
        self.nome = novoNome
        return True
