from ..IReg import IReg


class R1360(IReg):

    def __init__(self):
        self._header = ['REG',
                        'NUM_LACRE',
                        'DT_APLICACAO']
