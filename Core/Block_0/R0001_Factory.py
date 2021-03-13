from Core.IFactory import IFactory
from Regs.Block_0 import R0001


class R0001Factory(IFactory):

    def create_block_object(self, line):
        self.r0001 = _r0001 = R0001()
        return  _r0001