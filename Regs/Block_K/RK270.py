from ..IReg import IReg


class RK270(IReg):

    def __init__(self):
        self._header = ['REG',
                        'DT_INI_AP',
                        'DT_FIN_AP',
                        'COD_OP_OS',
                        'COD_ITEM',
                        'QTD_COR_POS',
                        'QTD_COR_NEG',
                        'ORIGEM']
