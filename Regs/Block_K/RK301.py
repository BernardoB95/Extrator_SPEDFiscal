from ..IReg import IReg


class RK301(IReg):

    def __init__(self):
        self._header = ['REG',
                        'COD_ITEM',
                        'QTD']

        self._hierarchy = "4"
