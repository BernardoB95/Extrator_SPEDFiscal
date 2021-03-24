from ..IReg import IReg


class RD150(IReg):

    def __init__(self):
        self._header = ['REG',
                        'COD_MUN_ORIG',
                        'COD_MUN_DEST',
                        'VEIC_ID',
                        'VIAGEM',
                        'IND_TFA',
                        'VL_PESO_TX',
                        'VL_TX_TERR',
                        'VL_TX_RED',
                        'VL_OUT',
                        'VL_TX_ADV']
