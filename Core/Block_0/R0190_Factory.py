from Core.IFactory import IFactory
from Regs.Block_0 import R0190


class R0190Factory(IFactory):

    def create_block_object(self, line):
        self.r0190 = _r0190 = R0190()
        return _r0190
