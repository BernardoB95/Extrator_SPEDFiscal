from Core.IFactory import IFactory
from Regs.Block_1 import R1320


class R1320Factory(IFactory):

    def create_block_object(self, line):
        self.r1320 = _r1320 = R1320()
        _r1320.reg_list = line
        return _r1320
