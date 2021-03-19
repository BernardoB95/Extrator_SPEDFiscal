from ..IReg import IReg


class RC420(IReg):

    def __init__(self):
        self._header = ['REG',
                        'COD_TOT_PAR',
                        'VLR_ACUM_TOT',
                        'NR_TOT',
                        'DESCR_NR_TOT']
