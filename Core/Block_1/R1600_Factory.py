from Core.IFactory import IFactory
from Regs.Block_1 import R1600


class R1600Factory(IFactory):

    def create_block_object(self, line):
        self.r1600 = _r1600 = R1600()
        _r1600.reg_list = line
        return _r1600
