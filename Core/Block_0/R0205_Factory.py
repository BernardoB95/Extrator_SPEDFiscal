from Core.IFactory import IFactory
from Regs.Block_0 import R0205


class R0205Factory(IFactory):

    def create_block_object(self, line):
        self.r0205 = _r0205 = R0205()
        return _r0205
