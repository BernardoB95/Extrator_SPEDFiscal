from ..IReg import IReg


class RC405(IReg):

    def __init__(self):
        self._header = ['REG',
                        'DT_DOC',
                        'CRO',
                        'CRZ',
                        'NUM_COO_FIN',
                        'GT_FIN',
                        'VL_BRT']
