from ..IReg import IReg


class RC810(IReg):

    def __init__(self):
        self._header = ['REG',
                        'NUM_ITEM',
                        'COD_ITEM',
                        'QTD',
                        'UNID',
                        'VL_ITEM',
                        'CST_ICMS',
                        'CFOP']
