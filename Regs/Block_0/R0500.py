from ..IReg import IReg


class R0500(IReg):

    def __init__(self):
        self._header = ['REG',
                        'DT_ALT',
                        'COD_NAT_CC',
                        'IND_CTA',
                        'NIVEL',
                        'COD_CTA',
                        'NOME_CTA']

        self._hierarchy = "2"
