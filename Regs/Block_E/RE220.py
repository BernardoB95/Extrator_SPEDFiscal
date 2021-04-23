from ..IReg import IReg


class RE220(IReg):

    def __init__(self):
        self._header = ['REG',
                        'COD_AJ_APUR',
                        'DESCR_COMPL_AJ',
                        'VL_AJ_APUR']

        self._hierarchy = "4"
