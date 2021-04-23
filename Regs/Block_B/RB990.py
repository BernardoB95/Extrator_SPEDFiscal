from ..IReg import IReg


class RB990(IReg):

    def __init__(self):
        self._header = ['REG',
                        'QTD_LIN_B']

        self._hierarchy = "1"
