from ..IReg import IReg


class RE240(IReg):

    def __init__(self):
        self._header = ['REG',
                        'COD_PART',
                        'COD_MOD',
                        'SER',
                        'SUB',
                        'NUM_DOC',
                        'DT_DOC',
                        'COD_ITEM',
                        'VL_AJ_ITEM',
                        'CHV_DOCe']
