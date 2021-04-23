from ..IReg import IReg


class RC465(IReg):

    def __init__(self):
        self._header = ['REG',
                        'CHV_CFE',
                        'NUM_CCF']

        self._hierarchy = "5"
