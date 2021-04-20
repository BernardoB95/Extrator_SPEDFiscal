from ..IReg import IReg


class RC116(IReg):

    def __init__(self):
        self._header = ['REG',
                        'COD_MOD',
                        'NR_SAT',
                        'CHV_CFE',
                        'NUM_CFE',
                        'DT_DOC']

        self._hierarchy = "4"
