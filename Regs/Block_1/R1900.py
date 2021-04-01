from ..IReg import IReg


class R1900(IReg):

    def __init__(self):
        self._header = ['REG',
                        'IND_APUR_ICMS',
                        'DESCR_COMPL_OUT_APUR']
