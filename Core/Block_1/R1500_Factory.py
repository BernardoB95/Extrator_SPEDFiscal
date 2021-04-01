from Core.IFactory import IFactory
from Regs.Block_1 import R1500


class R1500Factory(IFactory):

    def create_block_object(self, line):
        self.r1500 = _r1500 = R1500()
        _r1500.reg_list = line
        return _r1500
