from ..IReg import IReg


class RC597(IReg):

    def __init__(self):
        self._header = ['REG',
                        'COD_AJ',
                        'DESCR_COMPL_AJ',
                        'COD_ITEM',
                        'VL_BC_ICMS',
                        'ALIQ_ICMS',
                        'VL_ICMS',
                        'VL_OUTROS']

        self._hierarchy = "4"
