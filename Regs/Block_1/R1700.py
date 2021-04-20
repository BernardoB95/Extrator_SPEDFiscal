from ..IReg import IReg


class R1700(IReg):

    def __init__(self):
        self._header = ['REG',
                        'COD_DISP',
                        'COD_MOD',
                        'SER',
                        'SUB',
                        'NUM_DOC_INI',
                        'NUM_DOC_FIN',
                        'NUM_AUT']

        self._hierarchy = "2"
