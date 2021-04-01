from Core.IFactory import IFactory
from Regs.Block_1 import R1980


class R1980Factory(IFactory):

    def create_block_object(self, line):
        self.r1980 = _r1980 = R1980()
        _r1980.reg_list = line
        return _r1980
