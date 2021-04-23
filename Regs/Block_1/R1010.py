from ..IReg import IReg


class R1010(IReg):

    def __init__(self):
        self._header = ['REG',
                        'IND_EXP',
                        'IND_CCRF',
                        'IND_COMB',
                        'IND_USINA',
                        'IND_VA',
                        'IND_EE',
                        'IND_CART',
                        'IND_FORM',
                        'IND_AER',
                        'IND_GIAF1',
                        'IND_GIAF3',
                        'IND_GIAF4',
                        'IND_REST_RESSARC_COMPL_ICMS']

        self._hierarchy = "2"
