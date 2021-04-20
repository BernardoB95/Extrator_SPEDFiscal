from ..IReg import IReg


class RK255(IReg):

    def __init__(self):
        self._header = ['REG',
                        'DT_CONS',
                        'COD_ITEM',
                        'QTD',
                        'COD_INS_SUBST']

        self._hierarchy = "4"
