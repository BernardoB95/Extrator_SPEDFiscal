from ..IReg import IReg


class RC595(IReg):

    def __init__(self):
        self._header = ['REG',
                        'COD_OBS',
                        'TXT_COMPL']

        self._hierarchy = "3"
