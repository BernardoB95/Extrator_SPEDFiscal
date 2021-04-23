from ..IReg import IReg


class R1510(IReg):

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
                        'VL_BC_ICMS_ST',
                        'ALIQ_ST',
                        'VL_ICMS_ST',
                        'IND_REC',
                        'COD_PART',
                        'VL_PIS',
                        'VL_COFINS',
                        'COD_CTA']

        self._hierarchy = "3"
