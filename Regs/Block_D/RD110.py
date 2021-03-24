from ..IReg import IReg


class RD110(IReg):

    def __init__(self):
        self._header = ['REG',
                        'NUM_ITEM',
                        'COD_ITEM',
                        'VL_SERV',
                        'VL_OUT']
