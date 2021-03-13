from Core.IFactory import IFactory
from Regs.Block_0 import R0206


class R0206Factory(IFactory):

    def create_block_object(self, line):
        self.r0206 = _r0206 = R0206()
        return _r0206
