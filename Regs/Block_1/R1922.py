from ..IReg import IReg


class R1922(IReg):

    def __init__(self):
        self._header = ['REG',
                        'NUM_DA',
                        'NUM_PROC',
                        'IND_PROC',
                        'PROC',
                        'TXT_COMPL']
