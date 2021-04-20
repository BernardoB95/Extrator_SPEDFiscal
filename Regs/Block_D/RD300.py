from ..IReg import IReg


class RD300(IReg):

    def __init__(self):
        self._header = ['REG',
                        'COD_MOD',
                        'SER',
                        'SUB', #
                        'NUM_DOC_INI',
                        'NUM_DOC_FIN',
                        'CST_ICMS',
                        'CFOP',
                        'ALIQ_ICMS',
                        'DT_DOC',
                        'CL_OPR',
                        'VL_DESC',
                        'VL_SERV',
                        'VL_SEG',
                        'VL_OUT_DESP',
                        'VL_BC_ICMS',
                        'VL_ICMS',
                        'VL_RED_BC'
                        'COD_OBS',
                        'COD_CTA']

        self._hierarchy = "2"
