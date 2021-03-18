from ..IReg import IReg


class RC191(IReg):

    def __init__(self):
        self._header = ['REG',
                        'VL_FCP_OP',
                        'VL_FCP_ST',
                        'VL_FCP_RET']
