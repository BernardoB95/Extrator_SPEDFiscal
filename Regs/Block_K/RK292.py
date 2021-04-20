from ..IReg import IReg


class RK292(IReg):

    def __init__(self):
        self._header = ['REG',
                        'COD_ITEM',
                        'QTD']

        self._hierarchy = "4"
