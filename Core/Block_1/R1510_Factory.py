from Core.IFactory import IFactory
from Regs.Block_1 import R1510


class R1510Factory(IFactory):

    def create_block_object(self, line):
        self.r1510 = _r1510 = R1510()
        _r1510.reg_list = line
        return _r1510
