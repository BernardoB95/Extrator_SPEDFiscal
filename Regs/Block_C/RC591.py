from ..IReg import IReg


class RC591(IReg):

    def __init__(self):
        self._header = ['REG',
                        'VL_FCP_OP',
                        'VL_FCP_ST']

        self._hierarchy = "4"
