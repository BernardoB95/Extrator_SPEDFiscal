from ..IReg import IReg


class R1400(IReg):

    def __init__(self):
        self._header = ['REG',
                        'COD_ITEM_IPM',
                        'MUN',
                        'VALOR']

        self._hierarchy = "2"
