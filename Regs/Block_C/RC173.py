from ..IReg import IReg


class RC173(IReg):

    def __init__(self):
        self._header = ['REG',
                        'LOTE_MED',
                        'QTD_ITEM',
                        'DT_FAB',
                        'DT_VAL',
                        'IND_MED',
                        'TP_PROD',
                        'VL_TAB_MAX']
