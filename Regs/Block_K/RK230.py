from ..IReg import IReg


class RK230(IReg):

    def __init__(self):
        self._header = ['REG',
                        'DT_INI_OP',
                        'DT_FIN_OP',
                        'COD_DOC_OP',
                        'COD_ITEM',
                        'QTD_ENC']

        self._hierarchy = "3"
