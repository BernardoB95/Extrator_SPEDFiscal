from Core.IFactory import IFactory
from Regs.Block_1 import R1390


class R1390Factory(IFactory):

    def create_block_object(self, line):
        self.r1390 = _r1390 = R1390()
        _r1390.reg_list = line
        return _r1390
