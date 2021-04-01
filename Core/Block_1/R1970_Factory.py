from Core.IFactory import IFactory
from Regs.Block_1 import R1970


class R1970Factory(IFactory):

    def create_block_object(self, line):
        self.r1970 = _r1970 = R1970()
        _r1970.reg_list = line
        return _r1970
