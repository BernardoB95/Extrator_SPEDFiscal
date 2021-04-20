from ..IReg import IReg


class RK275(IReg):

    def __init__(self):
        self._header = ['REG',
                        'COD_ITEM',
                        'QTD_COR_POS',
                        'QTD_COR_NEG',
                        'COD_INS_SUBST']

        self._hierarchy = "4"
