from Core.IFactory import IFactory
from Regs.Block_1 import R1100


class R1100Factory(IFactory):

    def create_block_object(self, line):
        self.r1100 = _r1100 = R1100()
        _r1100.reg_list = line
        return _r1100
