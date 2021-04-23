from ..IReg import IReg


class RG125(IReg):

    def __init__(self):
        self._header = ['REG',
                        'COD_IND_BEM',
                        'DT_MOV',
                        'TIPO_MOV',
                        'VL_IMOB_ICMS_OP',
                        'VL_IMOB_ICMS_ST',
                        'VL_IMOB_ICMS_FRT',
                        'VL_IMOB_ICMS_DIF',
                        'NUM_PARC',
                        'VL_PARC_PASS']

        self._hierarchy = "3"
