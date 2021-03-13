from ..IReg import IReg


class R0600(IReg):

    def __init__(self):
        self._header = ['REG',
                        'DT_ALT',
                        'COD_CCUS',
                        'CCUS']
