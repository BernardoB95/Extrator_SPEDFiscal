from ..IReg import IReg


class RK220(IReg):

    def __init__(self):
        self._header = ['REG',
                        'DT_MOV',
                        'COD_ITEM_ORI',
                        'COD_ITEM_DEST',
                        'QTDE_ORI',
                        'QTD_DEST']

        self._hierarchy = "3"
