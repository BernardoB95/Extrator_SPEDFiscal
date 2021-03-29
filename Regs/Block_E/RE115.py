from ..IReg import IReg


class RE115(IReg):

    def __init__(self):
        self._header = ['REG',
                        'COD_INF_ADIC',
                        'VL_INF_ADIC',
                        'DESCR_COMPL_AJ']
