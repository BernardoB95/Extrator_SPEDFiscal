from ..IReg import IReg


class RB020(IReg):

    def __init__(self):
        self._header = ['REG',
                        'IND_OPER',
                        'IND_EMIT',
                        'COD_PART',
                        'COD_MOD',
                        'COD_SIT',
                        'SER',
                        'NUM_DOC',
                        'CHV_NFE',
                        'DT_DOC',
                        'COD_MUN_SERV',
                        'VL_CONT',
                        'VL_MAT_TERC',
                        'VL_SUB',
                        'VL_ISNT_ISS',
                        'VL_DED_BC',
                        'VL_BC_ISS',
                        'VL_BC_ISS_RT',
                        'VL_ISS_RT',
                        'VL_ISS',
                        'COD_INF_OBS']

        self._hierarchy = "2"
