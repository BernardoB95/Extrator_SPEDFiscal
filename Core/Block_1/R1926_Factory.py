from Core.IFactory import IFactory
from Regs.Block_1 import R1926


class R1926Factory(IFactory):

    def create_block_object(self, line):
        self.r1926 = _r1926 = R1926()
        _r1926.reg_list = line
        return _r1926
