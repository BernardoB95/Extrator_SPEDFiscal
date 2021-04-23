from ..IReg import IReg


class RK210(IReg):

    def __init__(self):
        self._header = ['REG',
                        'DT_INI_OS',
                        'DT_FIN_OS',
                        'COD_DOC_OS',
                        'COD_ITEM_ORI',
                        'QTD_ORI']

        self._hierarchy = "3"
