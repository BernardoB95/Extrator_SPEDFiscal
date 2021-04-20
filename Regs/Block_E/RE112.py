from ..IReg import IReg


class RE112(IReg):

    def __init__(self):
        self._header = ['REG',
                        'NUM_DA',
                        'VL_AJ_DEBITOS',
                        'NUM_PROC',
                        'IND_PROC',
                        'PROC',
                        'TXT_COMPL']

        self._hierarchy = "5"
