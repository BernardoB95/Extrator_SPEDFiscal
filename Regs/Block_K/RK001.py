from ..IReg import IReg


class RK001(IReg):

    def __init__(self):
        self._header = ['REG',
                        'IND_MOV']
