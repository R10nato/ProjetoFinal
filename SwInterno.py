from ServicosDeTi import ServicoDeSoftware


class SwInterno(ServicoDeSoftware):
    def __init__(self, linguagem, versao, nome):
        super().__init__(versao, nome)
        self.linguagem = linguagem

    def implementar():
        print('Software Implementado')
        return 'Software Implementado'
    
    implementar()


