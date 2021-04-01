from Core.IFactory import IFactory
from Regs.Block_1 import R1922


class R1922Factory(IFactory):

    def create_block_object(self, line):
        self.r1922 = _r1922 = R1922()
        _r1922.reg_list = line
        return _r1922
