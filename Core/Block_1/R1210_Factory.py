from Core.IFactory import IFactory
from Regs.Block_1 import R1210


class R1210Factory(IFactory):

    def create_block_object(self, line):
        self.r1210 = _r1210 = R1210()
        _r1210.reg_list = line
        return _r1210
