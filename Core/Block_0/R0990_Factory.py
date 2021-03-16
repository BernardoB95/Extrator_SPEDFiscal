from Core.IFactory import IFactory
from Regs.Block_0 import R0990

class R0990Factory(IFactory):

    def create_block_object(self, line):
        self.r0990 = _r0990 = R0990()
        _r0990.reg_list = line
        return _r0990
