from Core.IFactory import IFactory
from Regs.Block_0 import R0600


class R0600Factory(IFactory):

    def create_block_object(self, line):
        self.r0600 = _r0600 = R0600()
        _r0600.reg_list = line
        return _r0600
