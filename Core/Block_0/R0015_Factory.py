from Core.IFactory import IFactory
from Regs.Block_0 import R0015


class R0015Factory(IFactory):

    def create_block_object(self, line):
        self.r0015 = _r0015 = R0015()
        _r0015.reg_list = line
        return _r0015
