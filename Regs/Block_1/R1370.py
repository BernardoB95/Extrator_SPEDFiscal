from ..IReg import IReg


class R1370(IReg):

    def __init__(self):
        self._header = ['REG',
                        'NUM_BICO',
                        'COD_ITEM',
                        'NUM_TANQUE']
