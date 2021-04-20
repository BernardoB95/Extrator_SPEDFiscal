from ..IReg import IReg


class RK250(IReg):

    def __init__(self):
        self._header = ['REG',
                        'DT_PROD',
                        'COD_ITEM',
                        'QTD']

        self._hierarchy = "3"
