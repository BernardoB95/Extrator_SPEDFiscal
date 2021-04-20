from ..IReg import IReg


class R1960(IReg):

    def __init__(self):
        self._header = ['REG',
                        'IND_AP',
                        'G1_01',
                        'G1_02',
                        'G1_03',
                        'G1_04',
                        'G1_05',
                        'G1_06',
                        'G1_07',
                        'G1_08',
                        'G1_09',
                        'G1_10',
                        'G1_11']

        self._hierarchy = "2"
