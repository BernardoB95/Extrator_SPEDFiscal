from ..IReg import IReg


class RD160(IReg):

    def __init__(self):
        self._header = ['REG',
                        'DESPACHO',
                        'CNPJ_CPF_REM',
                        'IE_REM',
                        'COD_MUN_ORI',
                        'CNPJ_CPF_DEST',
                        'IE_DEST',
                        'COD_MUN_DEST']

        self._hierarchy = "3"
