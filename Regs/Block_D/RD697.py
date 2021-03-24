from ..IReg import IReg


class RD697(IReg):

    def __init__(self):
        self._header = ['REG',
                        'UF',
                        'VL_BC_ICMS',
                        'VL_ICMS']
