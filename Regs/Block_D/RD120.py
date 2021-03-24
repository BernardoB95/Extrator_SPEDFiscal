from ..IReg import IReg


class RD120(IReg):

    def __init__(self):
        self._header = ['REG',
                        'COD_MUN_ORIG',
                        'COD_MUN_DEST',
                        'VEIC_ID',
                        'UF_ID']
