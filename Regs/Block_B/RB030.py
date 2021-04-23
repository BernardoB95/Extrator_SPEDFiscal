from ..IReg import IReg


class RB030(IReg):

    def __init__(self):
        self._header = ['REG',
                        'COD_MOD',
                        'SER',
                        'NUM_DOC_INI',
                        'NUM_DOC_FIN',
                        'DT_DOC',
                        'QTD_CANC',
                        'VL_CONT',
                        'VL_ISNT_ISS',
                        'VL_BC_ISS',
                        'VL_ISS',
                        'COD_INF_OBS']

        self._hierarchy = "2"
