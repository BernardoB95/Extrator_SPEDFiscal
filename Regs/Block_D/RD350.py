from ..IReg import IReg


class RD350(IReg):

    def __init__(self):
        self._header = ['REG',
                        'COD_MOD',
                        'ECF_MOD',
                        'ECF_FAB',
                        'ECF_FX']
