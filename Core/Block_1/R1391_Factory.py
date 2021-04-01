from Core.IFactory import IFactory
from Regs.Block_1 import R1391


class R1391Factory(IFactory):

    def create_block_object(self, line):
        self.r1391 = _r1391 = R1391()
        _r1391.reg_list = line
        return _r1391
