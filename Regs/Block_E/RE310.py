from ..IReg import IReg


class RE310(IReg):

    def __init__(self):
        self._header = ['REG',
                        'IND_MOV_DIFAL',
                        'VL_SLD_CRED_ANT_DIFAL',
                        'VL_TOT_DEBITOS_DIFAL',
                        'VL_OUT_DED_DIFAL',
                        'VL_TOT_CREDITOS_DIFAL',
                        'VL_OUT_CRED_DIFAL',
                        'VL_SLD_DEV_ANT_DIFAL',
                        'VL_DEDUCOES_DIFAL',
                        'VL_RECOL_DIFAL',
                        'VL_SLD_CRED_TRANSPORTAR_DIFAL',
                        'DEB_ESP_DIFAL'
                        'VL_SLD_CRED_ANT_FCP',
                        'VL_TOT_DEB_FCP',
                        'VL_OUT_DEB_FCP',
                        'VL_TOT_CRED_FCP',
                        'VL_OUT_CRED_FCP'
                        'VL_SLD_DEV_ANT_FCP',
                        'VL_DEDUCOES_FCP',
                        'VL_RECOL_FCP',
                        'VL_SLD_CRED_TRANSPORTAR_FCP',
                        'DEB_ESP_FCP']
