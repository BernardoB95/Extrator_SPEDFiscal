from ..IReg import IReg


class RB025(IReg):

    def __init__(self):
        self._header = ['REG',
                        'VL_CONT_P',
                        'VL_BC_ISS_P',
                        'ALIQ_ISS',
                        'COD_MOD',
                        'COD_SIT',
                        'SER']
