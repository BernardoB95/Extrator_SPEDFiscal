from ..IReg import IReg


class RC870(IReg):

    def __init__(self):
        self._header = ['REG',
                        'COD_ITEM',
                        'QTD',
                        'UNID',
                        'CST_ICMS',
                        'CFOP']
