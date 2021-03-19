from ..IReg import IReg


class RC321(IReg):

    def __init__(self):
        self._header = ['REG',
                        'COD_ITEM',
                        'QTD',
                        'UNID',
                        'VL_ITEM',
                        'VL_DESC',
                        'VL_BC_ICMS',
                        'VL_ICMS',
                        'VL_PIS',
                        'VL_COFINS']
