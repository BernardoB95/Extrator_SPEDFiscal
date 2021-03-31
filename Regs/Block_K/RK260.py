from ..IReg import IReg


class RK260(IReg):

    def __init__(self):
        self._header = ['REG',
                        'COD_OP_OS',
                        'COD_ITEM',
                        'DT_SAIDA',
                        'QTD_SAIDA',
                        'DT_RET',
                        'QTD_RET']
