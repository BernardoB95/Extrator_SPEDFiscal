from ..IReg import IReg


class R1100(IReg):

    def __init__(self):
        self._header = ['REG',
                        'IND_DOC',
                        'NRO_DE',
                        'DT_DE',
                        'NAT_EXP',
                        'NRO_RE',
                        'DT_RE',
                        'CHC_EMB',
                        'DT_CHC',
                        'DT_AVB',
                        'TP_CHC',
                        'PAIS']

        self._hierarchy = "2"
