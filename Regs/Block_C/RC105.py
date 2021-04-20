from ..IReg import IReg


class RC105(IReg):

    def __init__(self):
        self._header = ['REG',
                        'OPER',
                        'UF']

        self._hierarchy = "3"
