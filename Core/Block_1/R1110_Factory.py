from Core.IFactory import IFactory
from Regs.Block_1 import R1110


class R1110Factory(IFactory):

    def create_block_object(self, line):
        self.r1110 = _r1110 = R1110()
        _r1110.reg_list = line
        return _r1110
