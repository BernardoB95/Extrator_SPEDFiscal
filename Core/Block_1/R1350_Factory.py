from Core.IFactory import IFactory
from Regs.Block_1 import R1350


class R1350Factory(IFactory):

    def create_block_object(self, line):
        self.r1350 = _r1350 = R1350()
        _r1350.reg_list = line
        return _r1350
