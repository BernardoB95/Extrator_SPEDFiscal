from ..IReg import IReg


class RD500(IReg):

    def __init__(self):
        self._header = ['REG',
                        'IND_OPER',
                        'IND_EMIT',
                        'COD_PART',
                        'COD-MOD',
                        'COD_SIT',
                        'SER',
                        'SUB',
                        'NUM_DOC',
                        'DT_DOC',
                        'DT_A_P',
                        'VL_DOC',
                        'VL_DESC',
                        'VL_SERV',
                        'VL_SERV_NT',
                        'VL_TERC',
                        'VL_DA',
                        'VL_BC_ICMS',
                        'VL_ICMS',
                        'COD_INF',
                        'VL_PIS',
                        'VL_COFINS',
                        'COD_CTA',
                        'TP_ASSINANTE']
