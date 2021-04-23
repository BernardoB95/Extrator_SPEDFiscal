from ..IReg import IReg


class RC140(IReg):

    def __init__(self):
        self._header = ['REG',
                        'IND_EMIT',
                        'IND_TIT',
                        'DESC_TIT',
                        'NUM_TIT',
                        'QTD_PARC',
                        'VL_TIT']

        self._hierarchy = "3"
