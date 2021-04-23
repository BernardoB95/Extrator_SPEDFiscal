from ..IReg import IReg


class R0150(IReg):

    def __init__(self):
        self._header = ['REG',
                        'COD_PART',
                        'NOME',
                        'COD_PAIS',
                        'CNPJ',
                        'CPF',
                        'IE',
                        'COD_MUN',
                        'SUFRAMA',
                        'END',
                        'NUM',
                        'COMPL',
                        'BAIRRO']

        self._hierarchy = "2"
