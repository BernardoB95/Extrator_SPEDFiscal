from ..IReg import IReg


class RD180(IReg):

    def __init__(self):
        self._header = ['REG',
                        'NUM_SEQ',
                        'IND_EMIT',
                        'CNPJ_CPF_EMIT',
                        'UF_EMIT',
                        'IE_EMIT',
                        'COD_MUN_ORIG',
                        'CNPJ_CPF_TOM',
                        'UF_TOM',
                        'IE_TOM',
                        'COD_MUN_DEST',
                        'COD_MOD',
                        'SER',
                        'SUB',
                        'NUM_DOC',
                        'DT_DOC',
                        'VL_DOC']

        self._hierarchy = "3"
