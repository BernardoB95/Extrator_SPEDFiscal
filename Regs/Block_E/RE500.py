from ..IReg import IReg


class RE500(IReg):

    def __init__(self):
        self._header = ['REG',
                        'IND_APUR',
                        'DT_INI',
                        'DT_FIN']

        self._hierarchy = "2"
