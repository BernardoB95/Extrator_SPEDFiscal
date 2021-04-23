from ..IReg import IReg


class R1391(IReg):

    def __init__(self):
        self._header = ['REG',
                        'DT_REGISTRO',
                        'QTD_MOID',
                        'ESTOQ_INI',
                        'QTD_PRODUZ',
                        'ENT_ANID_HID',
                        'OUTR_ENTR',
                        'PERDA',
                        'CONS',
                        'SAI_ANI_HID',
                        'SAIDAS',
                        'ESTQ_FIN',
                        'ESTQ_INI_MEL',
                        'PROD_DIA_MEL',
                        'UTIL_MEL',
                        'PROD_ALC_MEL',
                        'OBS',
                        'COD_ITEM',
                        'TP_RESIDUO',
                        'QTD_RESIDUO']

        self._hierarchy = "3"
