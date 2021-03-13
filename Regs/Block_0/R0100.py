from ..IReg import IReg


class R0100(IReg):

    def __init__(self):
        self._header = ['REG',
                        'NOME',
                        'CPF',
                        'CRC',
                        'CNPJ',
                        'CEP',
                        'END',
                        'NUM',
                        'COMPL',
                        'BAIRRO',
                        'FONE',
                        'FAX',
                        'EMAIL',
                        'COD_MUN']
