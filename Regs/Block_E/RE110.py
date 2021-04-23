from ..IReg import IReg


class RE110(IReg):

    def __init__(self):
        self._header = ['REG',
                        'VL_TOT_DEBITOS',
                        'VL_AJ_DEBITOS',
                        'VL_TOT_AJ_DEBITOS',
                        'VL_ESTORNO_CRED',
                        'VL_TOT_CREDITOS',
                        'VL_AJ_CREDITOS',
                        'VL_TOT_AJ_CREDITOS',
                        'VL_ESTORNOS_DEBITOS',
                        'VL_SLD_CREDOR_ANT',
                        'VL_SLD_APURADO',
                        'VL_TOT_DED',
                        'VL_ICMS_RECOLHER',
                        'VL_SLD_CREDOR_TRANSPORTAR',
                        'DEB_ESP']

        self._hierarchy = "3"
