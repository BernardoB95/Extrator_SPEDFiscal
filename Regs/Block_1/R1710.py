from ..IReg import IReg


class R1710(IReg):

    def __init__(self):
        self._header = ['REG',
                        'NUM_DOC_INI',
                        'NUM_DOC_FIN']
