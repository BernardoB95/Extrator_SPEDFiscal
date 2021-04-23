from ..IReg import IReg


class RE250(IReg):

    def __init__(self):
        self._header = ['REG',
                        'COD_OR',
                        'VL_OR',
                        'DT_VCTO',
                        'COD_REC',
                        'NUM_PROC',
                        'IND_PROC',
                        'PROC',
                        'TXT_COMPL',
                        'MES_REF']

        self._hierarchy = "4"
