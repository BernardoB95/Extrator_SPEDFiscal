from ..IReg import IReg


class RH020(IReg):

    def __init__(self):
        self._header = ['REG',
                        'CST_ICMS',
                        'BC_ICMS',
                        'VL_ICMS']
