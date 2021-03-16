from Core.IFactory import IFactory
from Regs.Block_0 import R0400


class R0400Factory(IFactory):

    def create_block_object(self, line):
        self.r0400 = _r0400 = R0400()
        _r0400.reg_list = line
        return _r0400
