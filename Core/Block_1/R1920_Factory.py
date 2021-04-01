from Core.IFactory import IFactory
from Regs.Block_1 import R1920


class R1920Factory(IFactory):

    def create_block_object(self, line):
        self.r1920 = _r1920 = R1920()
        _r1920.reg_list = line
        return _r1920
