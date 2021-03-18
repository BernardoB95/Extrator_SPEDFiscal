from ..IReg import IReg


class RC112(IReg):

    def __init__(self):
        self._header = ['REG',
                        'COD_DA',
                        'UF',
                        'NUM_DA',
                        'COD_AUT',
                        'VL_DA',
                        'DT_VCTO',
                        'DT_PGTO']
