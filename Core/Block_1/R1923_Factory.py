from Core.IFactory import IFactory
from Regs.Block_1 import R1923


class R1923Factory(IFactory):

    def create_block_object(self, line):
        self.r1923 = _r1923 = R1923()
        _r1923.reg_list = line
        return _r1923
