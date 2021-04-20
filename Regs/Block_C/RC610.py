from ..IReg import IReg


class RC610(IReg):

    def __init__(self):
        self._header = ['REG',
                        'COD_CLASS',
                        'COD_ITEM',
                        'QTD',
                        'UNID',
                        'VL_ITEM',
                        'VL_DESC',
                        'CST_ICMS',
                        'CFOP',
                        'ALIQ_ICMS',
                        'VL_BC_ICMS',
                        'VL_ICMS',
                        'VL_BC_ICMS_ST',
                        'VL_ICMS_ST',
                        'VL_PIS',
                        'VL_COFINS',
                        'COD_CTA']

        self._hierarchy = "3"
