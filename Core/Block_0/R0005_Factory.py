from Core.IFactory import IFactory
from Regs.Block_0 import R0005


class R0005Factory(IFactory):

    def create_block_object(self, line):
        self.r0005 = _r0005 = R0005()
        _r0005.reg_list = line
        return _r0005
