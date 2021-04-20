from ..IReg import IReg


class R1110(IReg):

    def __init__(self):
        self._header = ['REG',
                        'COD_PART',
                        'SER',
                        'NUM_DOC',
                        'DT_DOC',
                        'CHV_NFE',
                        'NR_MEMO',
                        'QTD',
                        'UNID']

        self._hierarchy = "4"
