from ..IReg import IReg


class RE200(IReg):

    def __init__(self):
        self._header = ['REG',
                        'UF',
                        'DT_INI',
                        'DT_FIN']
