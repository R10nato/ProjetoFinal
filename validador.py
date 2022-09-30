import SwExterno
import SwInterno


class ValidadorServicosDeTi(object):
    def validar_id(self, id):
        if(id != 0):
            return True
        else:
            return False

    def validar_internalizar(self, result):
        if(result == SwExterno.internalizar()):
            return True
        else:
            return False

    def validar_implementar(self, result):
        if (result == SwInterno.implementar()):
            return True
        else:
            return False