from ..IReg import IReg


class RC113(IReg):

    def __init__(self):
        self._header = ['REG',
                        'IND_OPER',
                        'IND_EMIT',
                        'COD_PART',
                        'COD_MOD',
                        'SER',
                        'SUB',
                        'NUM_DOC',
                        'DT_DOC',
                        'CHV_DOCe']
