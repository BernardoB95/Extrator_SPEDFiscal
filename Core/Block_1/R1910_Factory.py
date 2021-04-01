from Core.IFactory import IFactory
from Regs.Block_1 import R1910


class R1910Factory(IFactory):

    def create_block_object(self, line):
        self.r1910 = _r1910 = R1910()
        _r1910.reg_list = line
        return _r1910
