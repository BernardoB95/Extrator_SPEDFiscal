from ..IReg import IReg


class RC174(IReg):

    def __init__(self):
        self._header = ['REG',
                        'IND_ARM',
                        'NUM_ARM',
                        'DESCR_COMPL']

        self._hierarchy = "4"
