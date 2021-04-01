from Core.IFactory import IFactory
from Regs.Block_1 import R1010


class R1010Factory(IFactory):

    def create_block_object(self, line):
        self.r1010 = _r1010 = R1010()
        _r1010.reg_list = line
        return _r1010
