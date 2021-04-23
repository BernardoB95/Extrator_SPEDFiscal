from ..IReg import IReg


class R1250(IReg):

    def __init__(self):
        self._header = ['REG',
                        'VL_CREDITO_ICMS_OP',
                        'VL_ICMS_ST_RET',
                        'VL_FCP_ST_RET',
                        'VL_ICMS_ST_COMPL',
                        'VL_FCP_ST_COMPL']

        self._hierarchy = "2"
