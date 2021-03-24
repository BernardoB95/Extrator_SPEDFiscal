from ..IReg import IReg


class RD370(IReg):

    def __init__(self):
        self._header = ['REG',
                        'COD_MUN_ORIG',
                        'VL_SERV',
                        'QTD_BILH',
                        'VL_BC_ICMS',
                        'VL_ICMS']
