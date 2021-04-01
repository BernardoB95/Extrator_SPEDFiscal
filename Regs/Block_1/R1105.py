from ..IReg import IReg


class R1105(IReg):

    def __init__(self):
        self._header = ['REG',
                        'COD_MOD',
                        'SERIE',
                        'NUM_DOC',
                        'CHV_NFE',
                        'DT_DOC',
                        'COD_ITEM']
