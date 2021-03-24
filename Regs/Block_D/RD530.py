from ..IReg import IReg


class RD530(IReg):

    def __init__(self):
        self._header = ['REG',
                        'IND_SERV',
                        'DT_INI_SERV',
                        'DT_FIN_SERV',
                        'PER_FISCAL',
                        'COD_AREA',
                        'TERMINAL']
