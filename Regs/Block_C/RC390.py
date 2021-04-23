from ..IReg import IReg


class RC390(IReg):

    def __init__(self):
        self._header = ['REG',
                        'CST_ICMS',
                        'CFOP',
                        'ALIQ_ICMS',
                        'VL_OPR',
                        'VL_BC_ICMS',
                        'VL_ICMS',
                        'VL_RED_BC',
                        'COD_OBS']

        self._hierarchy = "3"
