from ..IReg import IReg


class RD310(IReg):

    def __init__(self):
        self._header = ['REG',
                        'COD_MUN_ORIG',
                        'VL_SERV',
                        'VL_BC_ICMS',
                        'VL_ICMS']

        self._hierarchy = "3"
