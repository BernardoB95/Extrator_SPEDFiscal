from ..IReg import IReg


class RD410(IReg):

    def __init__(self):
        self._header = ['REG',
                        'COD_MOD',
                        'SER',
                        'SUB'
                        'NUM_DOC_INI',
                        'NUM_DOC_FIN',
                        'DT_DOC',
                        'CST_ICMS',
                        'CFOP',
                        'ALIQ_ICMS',
                        'VL_OPR',
                        'VL_DESC',
                        'VL_SERV',
                        'VL_BC_ICMS',
                        'VL_ICMS']

        self._hierarchy = "3"
