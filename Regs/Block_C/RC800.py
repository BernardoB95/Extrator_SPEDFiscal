from ..IReg import IReg


class RC800(IReg):

    def __init__(self):
        self._header = ['REG',
                        'COD_MOD',
                        'COD_SIT',
                        'NUM_CFE',
                        'DT_DOC',
                        'VL_CFE',
                        'VL_PIS',
                        'VL_COFINS',
                        'CNPJ_CPF',
                        'NR_SAT',
                        'CHV_CFE',
                        'VL_DESC',
                        'VL_MERC',
                        'VL_OUT_DA',
                        'VL_ICMS',
                        'VL_PIS_ST',
                        'VL_COFINS_ST']

        self._hierarchy = "2"
