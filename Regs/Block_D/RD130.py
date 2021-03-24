from ..IReg import IReg


class RD130(IReg):

    def __init__(self):
        self._header = ['REG',
                        'COD_PART_CONSG',
                        'COD_PART_RED',
                        'IND_FRT_RED',
                        'COD_MUN_ORIG',
                        'COD_MUN_DEST',
                        'VEIC_ID',
                        'VL_LIQ_FRT',
                        'VL_SEC_CAT',
                        'VL_DESP',
                        'VL_PEDG',
                        'VL_OUT',
                        'VL_FRT',
                        'UF_ID']
