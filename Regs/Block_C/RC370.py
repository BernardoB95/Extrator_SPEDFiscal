from ..IReg import IReg


class RC370(IReg):

    def __init__(self):
        self._header = ['REG',
                        'NUM_ITEM',
                        'COD_ITEM',
                        'QTD',
                        'UNID',
                        'VL_ITEM',
                        'VL_DESC']

        self._hierarchy = "3"
