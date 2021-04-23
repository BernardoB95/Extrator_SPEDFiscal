from ..IReg import IReg


class RD161(IReg):

    def __init__(self):
        self._header = ['REG',
                        'IND_CARGA',
                        'CNPJ_CPF_COL',
                        'IE_COL',
                        'COD_MUN_COL',
                        'CNPJ_CPF_ENTG',
                        'IE_ENTG',
                        'COD_MUN_ENTG']

        self._hierarchy = "4"
