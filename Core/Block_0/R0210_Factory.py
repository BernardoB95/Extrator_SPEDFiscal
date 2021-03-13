from Core.IFactory import IFactory
from Regs.Block_0 import R0210


class R0210Factory(IFactory):

    def create_block_object(self, line):
        self.r0210 = _r0210 = R0210()
        return _r0210
