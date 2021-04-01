from ..IReg import IReg


class R1600(IReg):

    def __init__(self):
        self._header = ['REG',
                        'COD_PART',
                        'TOT_CREDITO',
                        'TOT_DEBITO']
