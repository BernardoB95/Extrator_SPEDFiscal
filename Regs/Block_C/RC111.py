from ..IReg import IReg


class RC111(IReg):

    def __init__(self):
        self._header = ['REG',
                        'NUM_PROC',
                        'IND_PROC']
