from Core.IFactory import IFactory
from Regs.Block_0 import R0450


class R0450Factory(IFactory):

    def create_block_object(self, line):
        self.r0450 = _r0450 = R0450()
        return _r0450
