from ..IReg import IReg


class R1910(IReg):

    def __init__(self):
        self._header = ['REG',
                        'DT_INI',
                        'DT_FIN']

        self._hierarchy = "3"
