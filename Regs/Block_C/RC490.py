from ..IReg import IReg


class RC490(IReg):

    def __init__(self):
        self._header = ['REG',
                        'CST_ICMS',
                        'CFOP',
                        'ALIQ_ICMS',
                        'VL_OPR',
                        'VL_BC_ICMS',
                        'VL_ICMS',
                        'COD_OBS']

        self._hierarchy = "4"
