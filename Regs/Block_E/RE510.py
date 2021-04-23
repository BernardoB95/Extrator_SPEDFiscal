from ..IReg import IReg


class RE510(IReg):

    def __init__(self):
        self._header = ['REG',
                        'CFOP',
                        'CST_IPI',
                        'VL_CONT_IPI',
                        'VL_BC_IPI',
                        'VL_IPI']

        self._hierarchy = "3"
