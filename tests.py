import validador as val

class TestQuadrado(object):
    def test_lado(self):
        v = val.Validador()
        ladoA = 3
        ladoB = 4
        assert v.validar_quadrado(ladoA, ladoB) == False


