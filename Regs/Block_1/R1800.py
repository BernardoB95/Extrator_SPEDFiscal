from ..IReg import IReg


class R1800(IReg):

    def __init__(self):
        self._header = ['REG',
                        'VL_CARGA',
                        'VL_PASS',
                        'VL_FAT',
                        'IND_RAT',
                        'VL_ICMS_ANT',
                        'VL_BC_ICMS',
                        'VL_ICMS_APUR',
                        'VL_BC_ICMS_APUR',
                        'VL_DIF']
