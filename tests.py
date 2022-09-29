import validador as val

class TestServicosDeTi(object):
    def test_id(self):
        v = val.Validador()
        assert v.validar_id(1234) == True
        assert v.validar_id(0000) == False

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
#
#
