from ..IReg import IReg


class RD590(IReg):

    def __init__(self):
        self._header = ['REG',
                        'CST_ICMS',
                        'CFOP',
                        'ALIQ_ICMS',
                        'VL_OPR',
                        'VL_BC_ICMS',
                        'VL_ICMS',
                        'VL_BC_ICMS_UF',
                        'VL_ICMS_UF',
                        'VL_RED_BC',
                        'COD_OBS']
