from ..IReg import IReg


class R0015(IReg):

    def __init__(self):
        self._header = ['REG',
                        'UF_ST',
                        'IE_ST']

        self._hierarchy = "2"
