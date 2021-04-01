from Core.IFactory import IFactory
from Regs.Block_1 import R1360


class R1360Factory(IFactory):

    def create_block_object(self, line):
        self.r1360 = _r1360 = R1360()
        _r1360.reg_list = line
        return _r1360
