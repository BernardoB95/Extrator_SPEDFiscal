from ..IReg import IReg


class RK200(IReg):

    def __init__(self):
        self._header = ['REG',
                        'DT_EST',
                        'COD_ITEM',
                        'QTD',
                        'IND_EST',
                        'COD_PART']

        self._hierarchy = "3"
