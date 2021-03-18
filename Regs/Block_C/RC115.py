from ..IReg import IReg


class RC115(IReg):

    def __init__(self):
        self._header = ['REG',
                        'IND_CARGA',
                        'CNPJ_COL',
                        'IE_COL',
                        'CPF_COL',
                        'COD_MUN_COL',
                        'CNPJ_ENTG',
                        'IE_ENTG',
                        'CPF_ENTG',
                        'COD_MUN_ENTG']
