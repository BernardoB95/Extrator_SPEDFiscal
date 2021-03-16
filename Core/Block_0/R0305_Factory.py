from Core.IFactory import IFactory
from Regs.Block_0 import R0305


class R0305Factory(IFactory):

    def create_block_object(self, line):
        self.r0305 = _r0305 = R0305()
        _r0305.reg_list = line
        return _r0305
