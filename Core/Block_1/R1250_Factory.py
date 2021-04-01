from Core.IFactory import IFactory
from Regs.Block_1 import R1250


class R1250Factory(IFactory):

    def create_block_object(self, line):
        self.r1250 = _r1250 = R1250()
        _r1250.reg_list = line
        return _r1250
