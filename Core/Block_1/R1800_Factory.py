from Core.IFactory import IFactory
from Regs.Block_1 import R1800


class R1800Factory(IFactory):

    def create_block_object(self, line):
        self.r1800 = _r1800 = R1800()
        _r1800.reg_list = line
        return _r1800
