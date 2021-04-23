from ..IReg import IReg


class RD162(IReg):

    def __init__(self):
        self._header = ['REG',
                        'COD_MOD',
                        'SER',
                        'NUM_DOC',
                        'DT_DOC',
                        'VL_DOC',
                        'VL_MERC',
                        'QTD_VOL',
                        'PESO_BRT',
                        'PESO_LIQ']

        self._hierarchy = "4"
