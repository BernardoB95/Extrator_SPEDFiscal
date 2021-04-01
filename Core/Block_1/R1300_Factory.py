from Core.IFactory import IFactory
from Regs.Block_1 import R1300


class R1300Factory(IFactory):

    def create_block_object(self, line):
        self.r1300 = _r1300 = R1300()
        _r1300.reg_list = line
        return _r1300
