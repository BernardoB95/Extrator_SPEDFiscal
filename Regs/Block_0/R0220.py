from ..IReg import IReg


class R0220(IReg):

    def __init__(self):
        self._header = ['REG',
                        'UNID_CONV',
                        'FET_CONV']

        self._hierarchy = "3"
