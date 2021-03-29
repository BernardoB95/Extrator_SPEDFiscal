from ..IReg import IReg


class RE210(IReg):

    def __init__(self):
        self._header = ['REG',
                        'IND_MOV_ST',
                        'VL_SLD_CRED_ANT_ST',
                        'VL_DEVOL_ST',
                        'VL_RESSARC_ST',
                        'VL_OUT_CRED_ST',
                        'VL_AJ_CREDITOS_ST',
                        'VL_RETENCAO_ST',
                        'VL_OUT_DEB_ST',
                        'VL_AJ_DEBITOS_ST',
                        'VL_SLD_DEV_ANT_ST',
                        'VL_DEDUCOES_ST',
                        'VL_ICMS_RECOL_ST',
                        'VL_SLD_CRED_ST_TRANSPORTAR',
                        'DEB_ESP_ST']
