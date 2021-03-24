from ..IReg import IReg


class RD360(IReg):

    def __init__(self):
        self._header = ['REG',
                        'VL_PIS',
                        'VL_COFINS']
