from ..IReg import IReg


class RD100(IReg):

    def __init__(self):
        self._header = ['REG',
                        'IND_OPER',
                        'IND_EMIT',
                        'COD_PART',
                        'COD_MOD',
                        'COD_SIT',
                        'SER',
                        'SUB',
                        'NUM_DOC',
                        'CHV_CTE',
                        'DT_DOC',
                        'DT_A_P',
                        'TP_CT-e',
                        'CHV_CTE_REF',
                        'VL_DOC',
                        'VL_DESC',
                        'IND_FRT',
                        'VL_SERV',
                        'VL_BC_ICMS',
                        'VL_ICMS',
                        'VL_NT',
                        'COD_INF',
                        'COD_CTA',
                        'COD_MUN_ORIG',
                        'COD_MUN_DEST']

        self._hierarchy = "2"
