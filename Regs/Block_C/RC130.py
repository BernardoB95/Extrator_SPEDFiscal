from ..IReg import IReg


class RC130(IReg):

    def __init__(self):
        self._header = ['REG',
                        'VL_SERV_NT',
                        'VL_BC_ISSQN',
                        'VL_ISSQN',
                        'VL_BC_IRRF',
                        'VL_IRRF',
                        'VL_BC_PREV',
                        'VL_PREV']

        self._hierarchy = "3"
