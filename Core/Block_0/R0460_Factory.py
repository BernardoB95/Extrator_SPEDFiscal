from Core.IFactory import IFactory
from Regs.Block_0 import R0460


class R0460Factory(IFactory):

    def create_block_object(self, line):
        self.r0560 = _r0460 = R0460()
        _r0460.reg_list = line
        return _r0460
