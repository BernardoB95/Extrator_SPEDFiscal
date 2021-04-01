from Core.IFactory import IFactory
from Regs.Block_1 import R1990


class R1990Factory(IFactory):

    def create_block_object(self, line):
        self.r1990 = _r1990 = R1990()
        _r1990.reg_list = line
        return _r1990
