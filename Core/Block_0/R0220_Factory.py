from Core.IFactory import IFactory
from Regs.Block_0 import R0220


class R0220Factory(IFactory):

    def create_block_object(self, line):
        self.r0220 = _r0220 = R0220()
        _r0220.reg_list = line
        return _r0220
