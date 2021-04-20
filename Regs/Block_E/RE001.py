from ..IReg import IReg


class RE001(IReg):

    def __init__(self):
        self._header = ['REG',
                        'IND_MOV']

        self._hierarchy = "1"
