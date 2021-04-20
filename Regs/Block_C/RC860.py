from ..IReg import IReg


class RC860(IReg):

    def __init__(self):
        self._header = ['REG',
                        'COD_MOD',
                        'NR_SAT',
                        'DT_DOC',
                        'DOC_INI',
                        'DOC_FIM']

        self._hierarchy = "2"
