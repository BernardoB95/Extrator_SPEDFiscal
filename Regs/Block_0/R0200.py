from ..IReg import IReg


class R0200(IReg):

    def __init__(self):
        self._header = ['REG',
                        'COD_ITEM',
                        'DESCR_ITEM',
                        'COD_BARRA',
                        'COD_ANT_ITEM',
                        'UNID_INV',
                        'TIPO_ITEM',
                        'COD_NCM',
                        'EX_IPI',
                        'COD_GEN',
                        'COD_LST',
                        'ALIQ_ICMS',
                        'CEST']
