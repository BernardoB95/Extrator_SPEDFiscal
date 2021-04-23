from ..IReg import IReg


class RC160(IReg):

    def __init__(self):
        self._header = ['REG',
                        'COD_PART',
                        'VEIC_ID',
                        'QTD_VOL',
                        'PESO_BRT',
                        'PESO_LIQ',
                        'UF_ID']

        self._hierarchy = "3"
