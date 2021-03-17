from ..IReg import IReg


class RB460(IReg):

    def __init__(self):
        self._header = ['REG',
                        'IND_DED',
                        'VL_DED',
                        'NUM_PROC',
                        'IND_PROC',
                        'PROC',
                        'COD_INF_OBS',
                        'IND_OBR']
