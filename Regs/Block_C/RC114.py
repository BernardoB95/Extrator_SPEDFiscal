from ..IReg import IReg


class RC114(IReg):

    def __init__(self):
        self._header = ['REG',
                        'COD_MOD',
                        'ECF_FAB',
                        'ECF_CX',
                        'NUM_DOC',
                        'DT_DOC']
