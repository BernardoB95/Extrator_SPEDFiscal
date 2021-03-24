from ..IReg import IReg


class RD400(IReg):

    def __init__(self):
        self._header = ['REG',
                        'COD_PART',
                        'COD_MOD',
                        'COD_SIT',
                        'SER',
                        'SUB',
                        'NUM_DOC',
                        'DT_DOC',
                        'VL_DOC',
                        'VL_DESC',
                        'VL_SERV',
                        'VL_BC_ICMS',
                        'VL_ICMS',
                        'VL_PIS',
                        'VL_COFINS',
                        'COD_CTA']
