from ..IReg import IReg


class RG130(IReg):

    def __init__(self):
        self._header = ['REG',
                        'IND_EMIT',
                        'COD_PART',
                        'COD_MOD',
                        'SERIE',
                        'NUM_DOC',
                        'CHV_NFE_CTE',
                        'DT_DOC',
                        'NUM_DA']

        self._hierarchy = "4"
