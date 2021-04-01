from Core.IFactory import IFactory
from Regs.Block_1 import R1960


class R1960Factory(IFactory):

    def create_block_object(self, line):
        self.r1960 = _r1960 = R1960()
        _r1960.reg_list = line
        return _r1960
