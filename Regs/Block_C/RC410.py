from ..IReg import IReg


class RC410(IReg):

    def __init__(self):
        self._header = ['REG',
                        'VL_PIS',
                        'VL_COFINS']

        self._hierarchy = "4"
