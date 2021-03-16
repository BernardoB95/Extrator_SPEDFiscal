from Core.IFactory import IFactory
from Regs.Block_0 import R0002

class R0002Factory(IFactory):

    def create_block_object(self, line):
        self.r0002 = _r0002 = R0002()
        _r0002.reg_list = line
        return _r0002