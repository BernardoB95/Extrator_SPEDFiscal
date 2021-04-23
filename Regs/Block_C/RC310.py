from ..IReg import IReg


class RC310(IReg):

    def __init__(self):
        self._header = ['REG',
                        'NUM_DOC_CANC']

        self._hierarchy = "3"
