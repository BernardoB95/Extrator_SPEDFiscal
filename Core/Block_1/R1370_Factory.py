from Core.IFactory import IFactory
from Regs.Block_1 import R1370


class R1370Factory(IFactory):

    def create_block_object(self, line):
        self.r1370 = _r1370 = R1370()
        _r1370.reg_list = line
        return _r1370
