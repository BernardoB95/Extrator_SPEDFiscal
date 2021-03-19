from ..IReg import IReg


class RC815(IReg):

    def __init__(self):
        self._header = ['REG',
                        'COD_MOT_REST_COMPL',
                        'QUANT_CONV',
                        'UNID',
                        'VL_UNIT_CONV',
                        'VL_UNIT_ICMS_NA_OPERACAO_CONV',
                        'VL_UNIT_ICMS_OP_CONV',
                        'VL_UNIT_ICMS_OP_ESTOQUE_CONV',
                        'VL_UNIT_ICMS_ST_ESTOQUE_CONV',
                        'VL_UNIT_FCP_ICMS_ST_ESTOQUE_CONV',
                        'VL_UNIT_ICMS_ST_CONV_REST',
                        'VL_UNIT_FCP_ST_CONV_REST',
                        'VL_UNIT_ICMS_ST_CONV_COMPL',
                        'VL_UNIT_FCP_ST_CONV_COMPL']
