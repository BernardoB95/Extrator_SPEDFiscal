from Core.IFactory import IFactory
from Regs.Block_1 import R1001


class R1001Factory(IFactory):

    def create_block_object(self, line):
        self.r1001 = _r1001 = R1001()
        _r1001.reg_list = line
        return _r1001
