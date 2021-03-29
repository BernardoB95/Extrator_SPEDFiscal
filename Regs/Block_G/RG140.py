from ..IReg import IReg


class RG140(IReg):

    def __init__(self):
        self._header = ['REG',
                        'NUM_ITEM',
                        'COD_ITEM',
                        'QTDE',
                        'UNID',
                        'VL_ICMS_OP_APLICADO',
                        'VL_ICMS_ST_APLICADO',
                        'VL_ICMS_FRT_APLICADO',
                        'VL_ICMS_DIF_APLICADO']
