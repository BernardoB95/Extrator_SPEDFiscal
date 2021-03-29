from ..IReg import IReg


class RE530(IReg):

    def __init__(self):
        self._header = ['REG',
                        'IND_AJ',
                        'VL_AJ',
                        'COD_AJ',
                        'IND_DOC',
                        'NUM_DOC',
                        'DESCR_AJ']
