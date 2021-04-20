from ..IReg import IReg


class RC171(IReg):

    def __init__(self):
        self._header = ['REG',
                        'NUM_TANQUE',
                        'QTDE']

        self._hierarchy = "4"
