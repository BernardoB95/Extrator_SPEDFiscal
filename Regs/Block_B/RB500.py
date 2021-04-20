from ..IReg import IReg


class RB500(IReg):

    def __init__(self):
        self._header = ['REG',
                        'VL_REC',
                        'QTD_PROF',
                        'VL_OR']

        self._hierarchy = "2"
