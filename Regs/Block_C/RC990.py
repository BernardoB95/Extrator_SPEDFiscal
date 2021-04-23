from ..IReg import IReg


class RC990(IReg):

    def __init__(self):
        self._header = ['REG',
                        'QTD_LIN_C']

        self._hierarchy = "1"
