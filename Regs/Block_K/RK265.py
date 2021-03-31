from ..IReg import IReg


class RK265(IReg):

    def __init__(self):
        self._header = ['REG',
                        'COD_ITEM',
                        'QTD_CONS',
                        'QTD_RET']
