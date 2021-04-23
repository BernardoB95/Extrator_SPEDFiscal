from ..IReg import IReg


class RC181(IReg):

    def __init__(self):
        self._header = ['REG',
                        'COD_MOT_REST_COMPL',
                        'QUANT_CONV',
                        'UNID',
                        'COD_MOD_SAIDA',
                        'SERIE_SAIDA',
                        'ECF_FAB_SAIDA',
                        'NUM_DOC_SAIDA',
                        'CHV_DFE_SAIDA',
                        'DT_DOC_SAIDA',
                        'NUM_ITEM_SAIDA',
                        'VL_UNIT_CONV_SAIDA',
                        'VL_UNIT_ICMS_OP_ESTOQUE_CONV_SAIDA',
                        'VL_UNIT_ICMS_ST_ESTOQUE_CONV_SAIDA',
                        'VL_UNIT_FCP_ICMS_ST_ESTOQUE_CONV_SAIDA',
                        'VL_UNIT_ICMS_NA_OPERACAO_CONV_SAIDA',
                        'VL_UNIT_ICMS_OP_CONV_SAIDA',
                        'VL_UNIT_ICMS_ST_CONV_REST',
                        'VL_UNIT_FCP_ST_CONV_REST',
                        'VL_UNIT_ICMS_ST_CONV_COMPL',
                        'VL_UNIT_FCP_ST_CONV_COMPL']

        self._hierarchy = "4"
