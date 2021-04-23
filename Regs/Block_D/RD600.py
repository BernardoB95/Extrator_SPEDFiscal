from ..IReg import IReg


class RD600(IReg):

    def __init__(self):
        self._header = ['REG',
                        'COD_MOD',
                        'COD_MUN',
                        'SER',
                        'SUB',
                        'COD_CONS',
                        'QTD_CONS',
                        'DT_DOC',
                        'VL_DOC',
                        'VL_DESC',
                        'VL_SERV',
                        'VL_SERV_NT',
                        'VL_TERC',
                        'VL_DA',
                        'VL_BC_ICMS',
                        'VL_ICMS',
                        'VL_PIS',
                        'VL_COFINS']

        self._hierarchy = "2"
