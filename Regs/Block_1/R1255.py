from ..IReg import IReg


class R1255(IReg):

    def __init__(self):
        self._header = ['REG',
                        'COD_MOT_REST_COMPL',
                        'VL_CREDITO_ICMS_OP_MOT',
                        'VL_ICMS_ST_REST_MOT',
                        'VL_FCP_ST_RES_MOT',
                        'VL_ICMS_ST_COMPL_MOT',
                        'VL_FCP_ST_COMPL_MOT']
