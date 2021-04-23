from ..IReg import IReg


class RK100(IReg):

    def __init__(self):
        self._header = ['REG',
                        'DT_INI',
                        'DT_FIN']

        self._hierarchy = "2"
