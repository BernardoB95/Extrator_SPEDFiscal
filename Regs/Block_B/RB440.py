from ..IReg import IReg


class RB440(IReg):

    def __init__(self):
        self._header = ['REG',
                        'IND_OPER',
                        'COD_PART',
                        'VL_CONT_RT',
                        'VL_BC_ISS_RT',
                        'VL_ISS_RT']

        self._hierarchy = "2"
