from ..IReg import IReg


class RH030(IReg):

    def __init__(self):
        self._header = ['REG',
                        'VL_ICMS_OP',
                        'VL_BC_ICMS_ST',
                        'VL_ICMS_ST',
                        'VL_FCP']
