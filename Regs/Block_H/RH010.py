from ..IReg import IReg


class RH010(IReg):

    def __init__(self):
        self._header = ['REG',
                        'COD_ITEM',
                        'UNID',
                        'QTD',
                        'VL_UNIT',
                        'VL_ITEM',
                        'IND_PROP',
                        'COD_PART',
                        'TXT_COMPL',
                        'COD_CTA',
                        'VL_ITEM_IR']
