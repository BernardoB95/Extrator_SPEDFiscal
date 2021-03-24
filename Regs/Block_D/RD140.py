from ..IReg import IReg


class RD140(IReg):

    def __init__(self):
        self._header = ['REG',
                        'COD_PART_CONSG',
                        'COD_MUN_ORIG',
                        'COD_MUN_DEST',
                        'IND_VEIC',
                        'VEIC_ID',
                        'IND_NAV',
                        'VIAGEM',
                        'VL_FRT_LIQ',
                        'VL_DESP_PORT',
                        'VL_DESP_CAR_DESC',
                        'VL_OUT',
                        'VL_FRT_BRT',
                        'VL_FRT_MM']
