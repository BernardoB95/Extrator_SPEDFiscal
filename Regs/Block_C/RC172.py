from ..IReg import IReg


class RC172(IReg):

    def __init__(self):
        self._header = ['REG',
                        'VL_BC_ISSQN',
                        'ALIQ_ISSQN',
                        'VL_ISSQN']
