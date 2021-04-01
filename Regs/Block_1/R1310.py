from ..IReg import IReg


class R1310(IReg):

    def __init__(self):
        self._header = ['REG',
                        'NUM_TANQUE',
                        'ESTQ_ABERT',
                        'VOL_ENTR',
                        'VOL_DISP',
                        'VOL_SAIDAS',
                        'ESTQ_ESCR',
                        'VAL_AJ_PERDA',
                        'VAL_AJ_GANHO',
                        'FECH_FISICO']
