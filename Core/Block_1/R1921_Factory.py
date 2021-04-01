from Core.IFactory import IFactory
from Regs.Block_1 import R1921


class R1921Factory(IFactory):

    def create_block_object(self, line):
        self.r1921 = _r1921 = R1921()
        _r1921.reg_list = line
        return _r1921
