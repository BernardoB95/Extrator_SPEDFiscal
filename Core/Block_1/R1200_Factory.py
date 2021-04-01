from Core.IFactory import IFactory
from Regs.Block_1 import R1200


class R1200Factory(IFactory):

    def create_block_object(self, line):
        self.r1200 = _r1200 = R1200()
        _r1200.reg_list = line
        return _r1200
