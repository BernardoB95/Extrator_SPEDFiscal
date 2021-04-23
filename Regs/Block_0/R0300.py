from ..IReg import IReg


class R0300(IReg):

    def __init__(self):
        self._header = ['REG',
                        'COD_IND_BEM',
                        'IDENT_MERC',
                        'DESCR_ITEM',
                        'COD_PRNC',
                        'COD_CTA',
                        'NR_PARC']

        self._hierarchy = "2"
