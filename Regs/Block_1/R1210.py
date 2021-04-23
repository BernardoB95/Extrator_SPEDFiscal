from ..IReg import IReg


class R1210(IReg):

    def __init__(self):
        self._header = ['REG',
                        'TIPO_UTIL',
                        'NR_DOC',
                        'VL_CRED_UTIL',
                        'CHV_DOCe']

        self._hierarchy = "3"
