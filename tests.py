import ServicosDeTi
import SwInterno

class TestServicosDeTi(object):
    def test_id(self):
        v = Serv
        assert v
        assert v.validar_id(0000) == False
#get testar se retorna null


    def test_id_letra(self):
        v = val.Validador()
        assert v.validar_id('a234') == False
        assert v.validar_id('1234') == False

    def test_id_vazio(self):
        v = val.Validador()
        assert v.validar_id('') == False


class TestServicoDeSoftware(object):
    def test_versao(self):
        v = val.Validador()
        assert v.validar_versao('1234') == True

    def test_versao_vazio(self):
        v = val.Validador()
        assert v.validar_versao('') == False


class TestSwInterno(object):
    def test_internalizar(self):
        v = val.Validador()
        assert v.validar_internalizar('Software Internalizado') == True


class TestSwExterno(object):
    def test_implementar(self):
        v = SwInterno.implementar()
        assert v.validar_implementar('Software Implementado') == True
    def test_get_pro