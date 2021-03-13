from Core.IFactory import IFactory
from Regs.Block_0 import R0000


class R0000Factory(IFactory):

    def create_block_object(self, line):
        self.r0000 = _r0000 = R0000()
        return _r0000
