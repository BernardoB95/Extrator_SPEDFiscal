from ..IReg import IReg


class RC170(IReg):

    def __init__(self):
        self._header = ['REG',
                        'NUM_ITEM',
                        'COD_ITEM',
                        'DESCR_COMPL',
                        'QTD',
                        'UNID',
                        'VL_ITEM',
                        'VL_DESC',
                        'IND_MOV',
                        'CST_ICMS',
                        'CFOP',
                        'COD_NAT',
                        'VL_BC_ICMS',
                        'ALIQ_ICMS',
                        'VL_ICMS',
                        'VL_BC_ICMS_ST',
                        'ALIQ_ST',
                        'VL_ICMS_ST',
                        'IND_APUR',
                        'CST_IPI',
                        'COD_ENQ',
                        'VL_BC_IPI',
                        'ALIQ_IPI,',
                        'VL_IPI',
                        'CST_PIS',
                        'VL_BC_PIS',
                        'ALIQ_PIS',
                        'QUANT_BC_PIS',
                        'ALIQ_PIS',
                        'VL_PIS',
                        'CST_COFINS',
                        'VL_BC_COFINS',
                        'ALIQ_COFINS',
                        'QUANT_BC_COFINS',
                        'ALIQ_COFINS',
                        'VL_COFINS',
                        'COD_CTA',
                        'VL_ABAT_NT']

        self._hierarchy = "3"
