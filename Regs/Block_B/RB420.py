from ..IReg import IReg


class RB420(IReg):

    def __init__(self):
        self._header = ['REG',
                        'VL_CONT',
                        'VL_BC_ISS',
                        'ALIQ_ISS',
                        'VL_ISNT_ISS',
                        'VL_ISS',
                        'COD_SERV']

        self._hierarchy = "2"
