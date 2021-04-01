from Core.IFactory import IFactory
from Regs.Block_1 import R1700


class R1700Factory(IFactory):

    def create_block_object(self, line):
        self.r1700 = _r1700 = R1700()
        _r1700.reg_list = line
        return _r1700
