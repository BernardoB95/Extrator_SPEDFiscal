from ..IReg import IReg


class RC400(IReg):

    def __init__(self):
        self._header = ['REG',
                        'COD_MOD',
                        'ECF_MOD',
                        'ECF_FAB',
                        'ECF_CX']

        self._hierarchy = "2"
