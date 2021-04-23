from ..IReg import IReg


class R0000(IReg):

    def __init__(self):
        self._header = ['REG',
                        'COD_VER',
                        'COD_FIN',
                        'DT_INI',
                        'DT_FIN',
                        'NOME',
                        'CNPJ',
                        'CPF',
                        'UF',
                        'IE',
                        'COD_MUN',
                        'IM',
                        'SUFRAMA',
                        'IND_PERFIL',
                        'IND_ATIV']

        self._hierarchy = "0"

