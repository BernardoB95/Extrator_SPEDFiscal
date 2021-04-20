from ..IReg import IReg


class RC120(IReg):

    def __init__(self):
        self._header = ['REG',
                        'COD_DOC_IMP',
                        'NUM_DOC_IMP',
                        'PIS_IMP',
                        'COFINS_IMP',
                        'NUM_ACDRAW']

        self._hierarchy = "3"
