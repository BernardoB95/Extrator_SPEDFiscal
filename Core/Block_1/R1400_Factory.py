from Core.IFactory import IFactory
from Regs.Block_1 import R1400


class R1400Factory(IFactory):

    def create_block_object(self, line):
        self.r1400 = _r1400 = R1400()
        _r1400.reg_list = line
        return _r1400
