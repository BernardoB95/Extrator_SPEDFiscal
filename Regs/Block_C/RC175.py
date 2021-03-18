from ..IReg import IReg


class RC175(IReg):

    def __init__(self):
        self._header = ['REG',
                        'IND_VEIC_OPER',
                        'CNPJ',
                        'UF',
                        'CHASSI_VEIC']
