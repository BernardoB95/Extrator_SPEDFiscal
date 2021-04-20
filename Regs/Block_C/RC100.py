from ..IReg import IReg


class RC100(IReg):

    def __init__(self):
        self._header = ['REG',
                        'IND_OPER',
                        'IND_EMIT',
                        'COD_PART',
                        'COD_MOD',
                        'COD_SIT',
                        'SER',
                        'NUM-DOC',
                        'CHV_NFE',
                        'DT_DOC',
                        'DT_E_S',
                        'VL_DOC',
                        'IND_PGTO',
                        'VL_DESC',
                        'VL_ABAT_NT',
                        'VL_MERC',
                        'IND_FRT',
                        'VL_FRT',
                        'VL_SEG',
                        'VL_OUT_DA',
                        'VL_BC_ICMS',
                        'VL_ICMS',
                        'VL_BC_ICMS_ST',
                        'VL_ICMS_ST',
                        'VL_IPI',
                        'VL_PIS',
                        'VL_COFINS',
                        'VL_PIS_ST',
                        'VL_COFINS_ST']

        self._hierarchy = "2"
