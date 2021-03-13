from Core.IFactory import IFactory
from Regs.Block_0 import R0100


class R0100Factory(IFactory):

    def create_block_object(self, line):
        self.r0100 = _r0100 = R0100()
        return _r0100