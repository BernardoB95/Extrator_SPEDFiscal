from Core.IFactory import IFactory
from Regs.Block_1 import R1255


class R1255Factory(IFactory):

    def create_block_object(self, line):
        self.r1255 = _r1255 = R1255()
        _r1255.reg_list = line
        return _r1255
