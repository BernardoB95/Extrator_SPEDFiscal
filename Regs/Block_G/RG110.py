from ..IReg import IReg


class RG110(IReg):

    def __init__(self):
        self._header = ['REG',
                        'DT_INI',
                        'DT_FIN',
                        'SALDO_INI_ICMS',
                        'SOM_PARC',
                        'VL_TRIB_EXP',
                        'VL_TOTAL',
                        'IND_PER_SAI',
                        'ICMS_APROP',
                        'SOM_ICMS_OC']

        self._hierarchy = "2"
