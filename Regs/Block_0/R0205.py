from ..IReg import IReg


class R0205(IReg):

    def __init__(self):
        self._header = ['REG',
                        'DESCR_ANT_ITEM',
                        'DT_INI',
                        'DT_FIM',
                        'COD_ANT_ITEM']
