from ..IReg import IReg


class RK290(IReg):

    def __init__(self):
        self._header = ['REG',
                        'DT_INI_OP',
                        'DT_FIN_AP',
                        'COD_DOC_OP']

        self._hierarchy = "3"
