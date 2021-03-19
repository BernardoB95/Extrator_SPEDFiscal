from ..IReg import IReg


class RC350(IReg):

    def __init__(self):
        self._header = ['REG',
                        'SER',
                        'SUB_SER',
                        'NUM_DOC',
                        'DT_DOC',
                        'CNPJ_CPF',
                        'VL_MERC',
                        'VL_DOC',
                        'VL_DESC',
                        'VL_PIS',
                        'VL_COFINS',
                        'COD_CTA']
