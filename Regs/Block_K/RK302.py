from ..IReg import IReg


class RK302(IReg):

    def __init__(self):
        self._header = ['REG',
                        'COD_ITEM',
                        'QTD']
