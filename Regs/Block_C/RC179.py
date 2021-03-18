from ..IReg import IReg


class RC179(IReg):

    def __init__(self):
        self._header = ['REG',
                        'BC_ST_ORIG_DEST',
                        'ICMS_ST_REP',
                        'ICMS_ST_COMPL',
                        'BC_RET',
                        'ICMS_RET']
