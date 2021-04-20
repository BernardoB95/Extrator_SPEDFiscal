from ..IReg import IReg


class RH990(IReg):

    def __init__(self):
        self._header = ['REG',
                        'QTD_LIN_H']

        self._hierarchy = "1"
