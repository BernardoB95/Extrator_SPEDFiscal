from ..IReg import IReg


class RC495(IReg):

    def __init__(self):
        self._header = ['REG',
                        'ALIQ_ICMS',
                        'COD_ITEM',
                        'QTD',
                        'QTD_CANC',
                        'UNID',
                        'VL_ITEM',
                        'VL_DESC',
                        'VL_CANC',
                        'VL_ACMO',
                        'VL_BC_ICMS',
                        'VL_ICMS',
                        'VL_ISEN',
                        'VL_NT',
                        'VL_ICMS_ST']
