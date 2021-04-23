from ..IReg import IReg


class RC165(IReg):

    def __init__(self):
        self._header = ['REG',
                        'COD_PART',
                        'VEIC_ID',
                        'COD_AUT',
                        'NR_PASSE',
                        'HORA',
                        'TEMPER',
                        'QTD_VOL',
                        'PESO_BRT',
                        'PESO_LIQ',
                        'NOM_MOT',
                        'CPF',
                        'UF_ID']

        self._hierarchy = "3"
