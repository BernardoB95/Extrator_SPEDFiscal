from ..IReg import IReg


class RC101(IReg):

    def __init__(self):
        self._header = ['REG',
                        'VL_FCP_UF_DEST',
                        'VL_ICMS_UF_DEST',
                        'VL_ICMS_UF_REM']
