from ..IReg import IReg


class RE300(IReg):

    def __init__(self):
        self._header = ['REG',
                        'UF',
                        'DT_INI',
                        'DT_FIN']
