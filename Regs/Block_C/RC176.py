from ..IReg import IReg


class RC176(IReg):

    def __init__(self):
        self._header = ['REG',
                        'COD_MOD_ULT_E',
                        'NUM_DOC_ULT_E',
                        'SER_ULT_E',
                        'DT_ULT_E',
                        'COD_PART_ULT_E',
                        'QUANT_ULT_E',
                        'VL_UNIT_ULT_E',
                        'VL_UNIT_BC_ST',
                        'CHAVE_NFE_ULT_E',
                        'NUM_ITM_ULT_E',
                        'VL_UNIT_BC_ICMS_ULT_E',
                        'ALIQ_ICMS_ULT_E',
                        'VL_UNIT_LIMITE_BC_ICMS_ULT_E',
                        'VL_UNIT_ICMS_UL_T_E',
                        'ALIQ_ST_ULT_E',
                        'VL_UNIT_RES',
                        'COD_RESP_RET',
                        'COD_MOT_RES',
                        'CHAVE_NFE_RET',
                        'COD_PART_NFE_RET',
                        'SER_NFE_RET',
                        'NUM_NFE_RET,',
                        'ITEM_NFE_RET',
                        'COD_DA',
                        'NUM_DA',
                        'VL_UNIT_RESP_FCP_ST']
