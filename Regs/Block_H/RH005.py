from ..IReg import IReg


class RH005(IReg):

    def __init__(self):
        self._header = ['REG',
                        'DT_INV',
                        'VL_INV',
                        'MOT_INV']

        self._hierarchy = "2"
