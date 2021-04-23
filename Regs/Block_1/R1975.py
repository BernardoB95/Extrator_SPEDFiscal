from ..IReg import IReg


class R1975(IReg):

    def __init__(self):
        self._header = ['REG',
                        'ALIQ_IMP_BASE',
                        'G3_10',
                        'G3_11',
                        'G3_12']

        self._hierarchy = "3"
