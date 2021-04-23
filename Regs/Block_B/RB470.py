from ..IReg import IReg


class RB470(IReg):

    def __init__(self):
        self._header = ['REG',
                        'VL_CONT',
                        'VL_MAT_TERC',
                        'VL_MAT_PROP',
                        'VL_SUB',
                        'VL_ISNT',
                        'VL_DED_BC',
                        'VL_BC_ISS',
                        'VL_BC_ISS_RT',
                        'VL_ISS',
                        'VL_IS_RT',
                        'VL_DED',
                        'VL_ISS_REC',
                        'VL_ISS_ST',
                        'VL_ISS_REC_UNI']

        self._hierarchy = "2"
