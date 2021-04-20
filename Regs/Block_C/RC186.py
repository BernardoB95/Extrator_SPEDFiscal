from ..IReg import IReg


class RC186(IReg):

    def __init__(self):
        self._header = ['REG',
                        'NUM_ITEM',
                        'COD_ITEM',
                        'CST_ICMS',
                        'CFOP',
                        'COD_MOT_REST_COMPL',
                        'QUANT_CONV',
                        'UNID',
                        'COD_MOD_ENTRADA',
                        'SERIE_ENTRADA',
                        'NUM_DOC_ENTRADA',
                        'CHV_DFE_ENTRADA',
                        'DT_DOC_ENTRADA',
                        'NUM_ITEM_ENTRADA',
                        'VL_UNIT_CONV_ENTRADA',
                        'VL_UNIT_ICMS_OP_CONV_ENTRADA',
                        'VL_UNIT_BC_ICMS_ST_CONV_ENTRADA',
                        'VL_UNIT_ICMS_ST_CONV_ENTRADA',
                        'VL_UNIT_FCP_ST_CONV_ENTRADA']

        self._hierarchy = "3"
