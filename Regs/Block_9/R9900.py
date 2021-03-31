from ..IReg import IReg


class R9900(IReg):

    def __init__(self):
        self._header = ['REG',
                        'REG_BLC',
                        'QTD_REG_BLC']
