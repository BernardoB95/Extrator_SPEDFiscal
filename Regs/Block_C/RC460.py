from ..IReg import IReg


class RC460(IReg):

    def __init__(self):
        self._header = ['REG',
                        'COD_MOD',
                        'COD_SIT',
                        'NUM_DOC',
                        'DT_DOC',
                        'VL_DOC',
                        'VL_PIS',
                        'VL_COFINS',
                        'CPF_CNPJ',
                        'NOM_ADQ']

        self._hierarchy = "4"
