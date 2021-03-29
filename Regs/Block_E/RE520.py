from ..IReg import IReg


class RE520(IReg):

    def __init__(self):
        self._header = ['REG',
                        'VL_SD_ANT_IPI',
                        'VL_DEB_IPI',
                        'VL_CRED_IPI',
                        'VL_OD_IPI',
                        'VL_OC_IPI',
                        'VL_SC_IPI',
                        'VL_SD_IPI']
