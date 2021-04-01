from ..IReg import IReg


class R1200(IReg):

    def __init__(self):
        self._header = ['REG',
                        'COD_AJ_APUR',
                        'SLD_CRED',
                        'CRED_APR',
                        'CRED_RECEB',
                        'CRED_UTIL',
                        'SLD_CRED_FIM']
