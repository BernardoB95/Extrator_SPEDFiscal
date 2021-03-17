from ..IReg import IReg


class RB510(IReg):

    def __init__(self):
        self._header = ['REG',
                        'IND_PROF',
                        'IND_ESC',
                        'IND_SOC',
                        'CPF',
                        'NOME']
