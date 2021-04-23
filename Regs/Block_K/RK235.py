from ..IReg import IReg


class RK235(IReg):

    def __init__(self):
        self._header = ['REG',
                        'DT_SAIDA',
                        'COD_ITEM',
                        'QTD',
                        'COD_INS_SUBST']

        self._hierarchy = "4"
