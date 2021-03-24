from ..IReg import IReg


class RD510(IReg):

    def __init__(self):
        self._header = ['REG',
                        'NUM_ITEM',
                        'COD_ITEM',
                        'COD_CLASS',
                        'QTD',
                        'UNID',
                        'VL_ITEM',
                        'VL_DESC',
                        'CST_ICMS',
                        'CFOP',
                        'VL_BC_ICMS',
                        'ALIQ_ICMS',
                        'VL_ICMS',
                        'VL_BC_ICMS_UF',
                        'VL_ICMS_UF',
                        'IND_REC',
                        'COD_PART',
                        'VL_PIS',
                        'VL_COFINS',
                        'COD_CTA']
