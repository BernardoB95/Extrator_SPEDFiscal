from ..IReg import IReg


class R0210(IReg):

    def __init__(self):
        self._header = ['REG',
                        'COD_ITEM_COMP',
                        'QTD_COMP',
                        'PERDA']
