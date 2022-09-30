from ServicosDeTi import ServicoDeSoftware


class SwExterno(ServicoDeSoftware):
    def __init__(self, proprietario, versao, nome):
        super().__init__(versao, nome)
        self.proprietario = proprietario

def internalizar():
    print('Software Internalizado')
    return 'Software Internalizado'
internalizar()

