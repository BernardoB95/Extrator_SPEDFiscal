from ..IReg import IReg


class RC700(IReg):

    def __init__(self):
        self._header = ['REG',
                        'COD_MOD',
                        'SER',
                        'NRO_ORD_INI',
                        'NRO_ORD_FIN',
                        'DT_DOC_INI',
                        'DT_DOC_FIN',
                        'NOM_MEST',
                        'CHV_COD_DIG']

        self._hierarchy = "2"
