from Core.IFactory import IFactory
from Regs.Block_1 import R1975


class R1975Factory(IFactory):

    def create_block_object(self, line):
        self.r1975 = _r1975 = R1975()
        _r1975.reg_list = line
        return _r1975
