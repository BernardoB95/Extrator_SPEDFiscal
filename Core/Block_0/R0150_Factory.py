from Core.IFactory import IFactory
from Regs.Block_0 import R0150


class R0150Factory(IFactory):

    def create_block_object(self, line):
        self.r0150 = _r0150 = R0150()
        _r0150.reg_list = line
        return _r0150