from ..IReg import IReg


class RK300(IReg):

    def __init__(self):
        self._header = ['REG',
                        'DT_PROD']
