from ..IReg import IReg


class RG126(IReg):

    def __init__(self):
        self._header = ['REG',
                        'DT_INI',
                        'DT_FIM',
                        'NUM_PARC',
                        'VL_PARC_PASS',
                        'VL_TRIB_OC',
                        'VL_TOTAL',
                        'IND_PER_SAI',
                        'IND_PARC_APROP']

        self._hierarchy = "4"
