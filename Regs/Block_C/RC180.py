from ..IReg import IReg


class RC180(IReg):

    def __init__(self):
        self._header = ['REG',
                        'COD_RESP_RET',
                        'QUANT_CONV',
                        'UNID',
                        'VL_UNIT_CONV',
                        'VL_UNIT_ICMS_OP_CONV',
                        'VL_UNIT_BC_ICMS_ST_CONV',
                        'VL_UNIT_ICMS_ST_CONV',
                        'VL_UNIT_FCP_ST_CONV',
                        'COD_DA',
                        'NUM_DA']
