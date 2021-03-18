from ..IReg import IReg


class RC190(IReg):

    def __init__(self):
        self._header = ['REG',
                        'CST_ICMS',
                        'CFOP',
                        'ALIQ_ICMS',
                        'VL_OPR',
                        'VL_BC_ICMS',
                        'VL_ICMS',
                        'VL_BC_ICMS_ST',
                        'VL_ICMS_ST',
                        'VL_RED_BC',
                        'VL_IPI',
                        'COD_OBS']
