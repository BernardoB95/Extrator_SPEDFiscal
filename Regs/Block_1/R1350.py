from ..IReg import IReg


class R1350(IReg):

    def __init__(self):
        self._header = ['REG',
                        'SERIE',
                        'FABRICANTE',
                        'MODELO',
                        'TIPO_MEDICAO']

        self._hierarchy = "2"
