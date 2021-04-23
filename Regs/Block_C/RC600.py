from ..IReg import IReg


class RC600(IReg):

    def __init__(self):
        self._header = ['REG',
                        'COD_MOD',
                        'COD_MUN',
                        'SER',
                        'SUB',
                        'COD_CONS',
                        'QTD_CONS',
                        'QTD_CANC',
                        'DT_DOC',
                        'VL_DOC',
                        'VL_DESC',
                        'CONS',
                        'VL_FORN',
                        'VL_SERV_NT',
                        'VL_TERC',
                        'VL_DA',
                        'VL_BC_ICMS',
                        'VL_ICMS',
                        'VL_BC_ICMS_ST',
                        'VL_ICMS_ST',
                        'VL_PIS',
                        'VL_COFINS']

        self._hierarchy = "2"
