import SwInterno


class Validador(object):
    def validar_id(self, id):
        if(id != 0):
            return True
        else:
            return False

    def validar_internalizar(self, result):

        self.result = 'Software Internalizado'
        print(SwInterno.imprimir())

        if(result   SwInterno.imprimir()):
            return False
        else:
            return True
        # se chamar o método, verifica se imprimiu