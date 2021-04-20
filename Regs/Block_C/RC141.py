from ..IReg import IReg


class RC141(IReg):

    def __init__(self):
        self._header = ['REG',
                        'NUM_PARC',
                        'DT_VCTO',
                        'VL_PARC']

        self._hierarchy = "4"
