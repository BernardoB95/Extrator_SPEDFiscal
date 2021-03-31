from ..IReg import IReg


class RK280(IReg):

    def __init__(self):
        self._header = ['REG',
                        'DT_EST',
                        'COD_ITEM',
                        'QTD_COR_POS',
                        'QTD_COR_NEG',
                        'IND_EST',
                        'COD_PART']
