from ..IReg import IReg


class RC425(IReg):

    def __init__(self):
        self._header = ['REG',
                        'COD_ITEM',
                        'QTD',
                        'UNID',
                        'VL_ITEM',
                        'VL_PIS',
                        'VL_COFINS']

        self._hierarchy = "5"
