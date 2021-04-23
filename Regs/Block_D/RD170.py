from ..IReg import IReg


class RD170(IReg):

    def __init__(self):
        self._header = ['REG',
                        'COD_PART_CONSG',
                        'COD_PART_RED',
                        'COD_MUN_ORIG',
                        'COD_MUN_DEST',
                        'OTM',
                        'IND_NAT_FRT',
                        'VL_LIQ_FRT',
                        'VL_GRIS',
                        'VL_PDG',
                        'VL_OUT',
                        'VL_FRT',
                        'VEIC_ID',
                        'UF_ID']

        self._hierarchy = "3"
