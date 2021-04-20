from ..IReg import IReg


class RK215(IReg):

    def __init__(self):
        self._header = ['REG',
                        'COD_ITEM_DES',
                        'QTDE']

        self._hierarchy = "4"
