from Core.IFactory import IFactory
from Regs.Block_0 import R0300


class R0300Factory(IFactory):

    def create_block_object(self, line):
        self.r0300 = _r0300 = R0300()
        _r0300.reg_list = line
        return _r0300
