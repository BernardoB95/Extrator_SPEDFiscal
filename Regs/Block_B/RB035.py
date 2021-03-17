from ..IReg import IReg


class RB035(IReg):

    def __init__(self):
        self._header = ['REG',
                        'VL_CONT_P',
                        'VL_BC_ISS_P',
                        'ALIQ_ISS',
                        'VL_ISS_P',
                        'VL_ISNT_ISS_P',
                        'COD_SERV']
