from ..IReg import IReg


class RC110(IReg):

    def __init__(self):
        self._header = ['REG',
                        'COD_INF',
                        'TXT_COMPL']
