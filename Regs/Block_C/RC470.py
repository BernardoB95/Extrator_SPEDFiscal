from ..IReg import IReg


class RC470(IReg):

    def __init__(self):
        self._header = ['REG',
                        'COD_ITEM',
                        'QTD',
                        'QTD_CANC',
                        'UNID',
                        'VL_ITEM',
                        'CST_ICMS',
                        'CFOP',
                        'ALIQ_ICMS',
                        'VL_PIS',
                        'VL_COFINS']

        self._hierarchy = "5"
