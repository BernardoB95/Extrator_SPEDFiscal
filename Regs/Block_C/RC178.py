from ..IReg import IReg


class RC178(IReg):

    def __init__(self):
        self._header = ['REG',
                        'CL_ENQ',
                        'VL_UNID',
                        'QUANT_PAD']

        self._hierarchy = "4"
