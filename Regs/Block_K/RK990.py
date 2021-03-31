from ..IReg import IReg


class RK990(IReg):

    def __init__(self):
        self._header = ['REG',
                        'QTD_LIN_K']
