from ..IReg import IReg


class R1320(IReg):

    def __init__(self):
        self._header = ['REG',
                        'NUM_BICO',
                        'NR_INTERV',
                        'MOT_INTERV',
                        'NOM_INTERV',
                        'CNPJ_INTERV',
                        'CPF_INTERV',
                        'VAL_FECHA',
                        'VAL_ABERT',
                        'VOL_AFERI',
                        'VOL_VENDAS']

        self._hierarchy = "4"
