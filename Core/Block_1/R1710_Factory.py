from Core.IFactory import IFactory
from Regs.Block_1 import R1710


class R1710Factory(IFactory):

    def create_block_object(self, line):
        self.r1710 = _r1710 = R1710()
        _r1710.reg_list = line
        return _r1710
