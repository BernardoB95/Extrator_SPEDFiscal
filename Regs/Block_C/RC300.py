from ..IReg import IReg


class RC300(IReg):

    def __init__(self):
        self._header = ['REG',
                        'COD_MOD',
                        'SER',
                        'SUB',
                        'NUM_DOC_INI',
                        'NUM_DOC_FIN',
                        'DT_DOC',
                        'VL_DOC',
                        'VL_PIS',
                        'VL_COFINS',
                        'COD_CTA']

        self._hierarchy = "2"
