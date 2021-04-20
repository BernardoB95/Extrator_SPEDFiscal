from ..IReg import IReg


class RD610(IReg):

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
                        'VL_BC_ICMS_UF',
                        'VL_ICMS_UF',
                        'VL_RED_BC',
                        'VL_PIS',
                        'VL_COFINS',
                        'COD_CTA']

        self._hierarchy = "3"
